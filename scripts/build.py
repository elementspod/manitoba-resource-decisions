"""Step 3 of 3: turn data/raw/*.csv into data/data.json, the one file every page reads."""
import csv, datetime, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
NUMERIC = {"lat", "lon", "lat_from", "lon_from", "lat_to", "lon_to", "x", "y", "stage"}


def conv(k, v):
    v = (v or "").strip()
    if k in NUMERIC and v != "":
        f = float(v)
        return int(f) if f.is_integer() else f
    return v


out = {"built": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "counts": {}}
for tab, spec in SCHEMA["tabs"].items():
    with open(ROOT / "data" / "raw" / f"{tab}.csv", newline="", encoding="utf-8") as fh:
        rows = [{k: conv(k, r.get(k)) for k in spec["columns"]} for r in csv.DictReader(fh)]
    out[tab] = rows
    out["counts"][tab] = len(rows)

(ROOT / "data" / "data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("Built data/data.json:", ", ".join(f"{t} {n}" for t, n in out["counts"].items()))
