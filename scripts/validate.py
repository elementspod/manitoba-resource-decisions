"""Step 2 of 3: check data/raw/ before anything is published.

Every problem is reported as tab, row number (as in the sheet) and column, so it
can be fixed in the sheet without reading code. Errors stop the build and the
live site keeps the last good version. Warnings are reported but do not stop it.
"""
import csv, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
SCHEMA = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")

errors, warnings = [], []


def err(tab, row, col, msg):
    errors.append({"tab": tab, "row": row, "column": col, "problem": msg})


def warn(tab, row, col, msg):
    warnings.append({"tab": tab, "row": row, "column": col, "problem": msg})


def load(tab):
    p = RAW / f"{tab}.csv"
    if not p.exists():
        err(tab, None, None, "tab is missing")
        return [], []
    with open(p, newline="", encoding="utf-8") as fh:
        r = csv.DictReader(fh)
        return r.fieldnames or [], list(r)


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    data = {t: load(t) for t in SCHEMA["tabs"]}
    ids = {}
    for tab, spec in SCHEMA["tabs"].items():
        cols, rows = data[tab]
        for c in spec["columns"]:
            if c not in cols:
                err(tab, 1, c, "column is missing or was renamed (row 1 must match exactly)")
        for c in cols:
            if c and c not in spec["columns"]:
                warn(tab, 1, c, "extra column - it is ignored")
        if spec["id"]:
            seen = {}
            for i, r in enumerate(rows, start=2):
                v = (r.get(spec["id"]) or "").strip()
                if v in seen:
                    err(tab, i, spec["id"], f"'{v}' is used twice (also row {seen[v]})")
                seen[v] = i
                if v and not re.match(r"^[a-z0-9][a-z0-9-]*$", v):
                    err(tab, i, spec["id"], f"'{v}' - ids use lowercase letters, numbers and dashes only")
            ids[tab] = set(seen)

    for tab, spec in SCHEMA["tabs"].items():
        cols, rows = data[tab]
        no_source = 0
        for i, r in enumerate(rows, start=2):
            for c in spec.get("required", []):
                if not (r.get(c) or "").strip():
                    err(tab, i, c, "is empty but required")
            for c, allowed in spec.get("enums", {}).items():
                v = (r.get(c) or "").strip()
                if v and v not in allowed:
                    err(tab, i, c, f"'{v}' is not allowed. Use one of: {', '.join(allowed)}")
            for c, target in spec.get("refs", {}).items():
                v = (r.get(c) or "").strip()
                for part in [p.strip() for p in re.split(r"[;|]", v) if p.strip()]:
                    if part not in ids.get(target, set()):
                        err(tab, i, c, f"'{part}' does not exist in the {target} tab")
            for c in spec.get("dates", []):
                v = (r.get(c) or "").strip()
                if v and not ISO.match(v):
                    err(tab, i, c, f"'{v}' is not a date in the form YYYY-MM-DD")
            if "source_ref" in spec["columns"] and not (r.get("source_ref") or "").strip():
                no_source += 1
        if no_source:
            warn(tab, None, "source_ref", f"{no_source} of {len(rows)} rows have no source yet")

    (la0, la1), (lo0, lo1) = SCHEMA["bounds"]["lat"], SCHEMA["bounds"]["lon"]
    for tab, pairs in [("sites", [("lat", "lon")]), ("routes", [("lat_from", "lon_from"), ("lat_to", "lon_to")])]:
        for i, r in enumerate(data[tab][1], start=2):
            for a, b in pairs:
                la, lo = num(r.get(a)), num(r.get(b))
                if la is None or not la0 <= la <= la1:
                    err(tab, i, a, f"'{r.get(a)}' is not a latitude between {la0} and {la1}")
                if lo is None or not lo0 <= lo <= lo1:
                    err(tab, i, b, f"'{r.get(b)}' is not a longitude between {lo0} and {lo1}")
    for i, r in enumerate(data["instruments"][1], start=2):
        for c in ("x", "y"):
            if (r.get(c) or "").strip() and num(r.get(c)) is None:
                err("instruments", i, c, f"'{r.get(c)}' is not a number")

    report = {"ok": not errors, "errors": errors, "warnings": warnings}
    (ROOT / "data" / "validation.json").write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    for e in errors:
        print(f"ERROR   {e['tab']}  row {e['row']}  {e['column']}: {e['problem']}")
    for w in warnings:
        print(f"warning {w['tab']}  row {w['row']}  {w['column']}: {w['problem']}")
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
