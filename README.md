# Manitoba resource decisions

An interactive map of mineral and mineral-related infrastructure projects in Manitoba: producing mines, processing plants, exploration properties, legacy sites awaiting remediation, and the rail, port, road and transmission routes that connect them. Click any site to see what is known about it, including its regulatory history where one exists.

A second view shows the approval steps a project can pass through (provincial, federal and, where relevant, Nunavut) and what each step is able to consider. The steps are always drawn in the same place, so that projects can be compared: selecting a project highlights the steps it went through and greys out the ones it did not use.

- **Live site:** https://elementspod.github.io/manitoba-resource-decisions/
- **Approval steps view:** https://elementspod.github.io/manitoba-resource-decisions/process.html
- **Repository:** https://github.com/elementspod/manitoba-resource-decisions
- **Data status (for editors):** https://elementspod.github.io/manitoba-resource-decisions/status.html

**Status: working draft.** Most site locations are approximate (only a handful come from a named source), regulatory histories are summaries, and several entries are unverified leads. Approximate locations are shown with a dashed ring on the map. Do not cite it yet.

## What is in this folder

| File | What it is |
| --- | --- |
| `index.html` | The provincial map |
| `process.html` | The approval steps (decision-flow) view |
| `README.md` | This file |
| `status.html` | Data status page: last build, row counts, any problems |
| `data/` | The data file the pages read, plus the check results |
| `scripts/` | The scripts that pull, check and build the data |
| `config/` | Holds the link to the published Google Sheet |
| `.github/workflows/` | The nightly build |

## Where the data lives

The data is edited in a Google Sheet, not in this repository. Every night (and whenever the build is run by hand), a GitHub Action reads the published sheet, checks it against `data/schema.json`, and writes `data/data.json`. The pages read from that one file.

- If the check finds a problem, the live site is not updated, and the [data status page](https://elementspod.github.io/manitoba-resource-decisions/status.html) says which tab, row and column to fix.
- The sheet link is kept in `config/sheet-url.txt`.
- To run a build by hand: Actions → Build and publish → Run workflow.

## Licence

Code: MIT (see LICENSE). Data: CC BY 4.0 (see LICENSE-DATA.md). Please credit the project as described there.

## Related

A companion to the [Deep-Sea Mining Knowledge Board](https://github.com/elementspod/deep-sea-mining-knowledge-board). The two share conventions but are kept as separate repositories.

Part of research associated with The Elements of Deep Sea Mining.
