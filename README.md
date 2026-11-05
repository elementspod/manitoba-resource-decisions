# Manitoba resource decisions

An interactive map of mineral and mineral-related infrastructure projects in Manitoba: producing mines, processing plants, exploration properties, legacy sites awaiting remediation, and the rail, port, road and transmission routes that connect them. Click any site to see what is known about it, including its regulatory history where one exists.

A second view shows the approval steps a project can pass through (provincial, federal and, where relevant, Nunavut) and what each step is able to consider. The steps are always drawn in the same place, so that projects can be compared: selecting a project highlights the steps it went through and greys out the ones it did not use.

A third view maps the ecosystem of players involved in mineral exploration and mine development in Manitoba — regulators, industry, finance, Indigenous rights holders and organizations, communities and civil society, professional services, and downstream markets. Players are grouped into categories and subcategories, with typed relationships showing how they connect (regulates, consults, funds, partners, opposes, etc.). Multiple layouts let you rearrange the network by stage of the mine life cycle, by who bears costs vs captures benefits, and by formal vs informal influence.

•Live site (provincial map): https://elementspod.github.io/manitoba-resource-decisions/

•Approval steps view: https://elementspod.github.io/manitoba-resource-decisions/process.html

•Mining ecosystem network: https://elementspod.github.io/manitoba-resource-decisions/manitoba-mining-map/

•Repository: https://github.com/elementspod/manitoba-resource-decisions

•Data status (for editors): https://elementspod.github.io/manitoba-resource-decisions/status.html

**Status: working draft.** Most site locations are approximate (only a handful come from a named source), regulatory histories are summaries, and several entries are unverified leads. Approximate locations are shown with a dashed ring on the map. The mining ecosystem network also contains partly verified and unverified entries, flagged on each actor’s panel. Do not cite yet.

## What is in this folder

| File | What it is |
| --- | --- |
| `index.html` | The provincial map |
| `process.html` | The approval steps (decision-flow) view |
| `manitoba-mining-map/` | The mining ecosystem network visualization |
| `README.md` | This file |
| `status.html` | Data status page: last build, row counts, any problems |
| `data/` | The data file the pages read, plus the check results |
| `scripts/` | The scripts that pull, check and build the data |
| `config/` | Holds the link to the published Google Sheet |
| `.github/workflows/` | The nightly build |

## Where the data lives

The data is edited in Google Sheets, not in this repository.

For the provincial map and approval steps view: Every night (and whenever the build is run by hand), a GitHub Action reads the published sheet, checks it against data/schema.json, and writes data/data.json. The pages read from that one file. If the check finds a problem, the live site is not updated, and the data status page says which tab, row and column to fix. The sheet link is kept in config/sheet-url.txt. To run a build by hand: Actions → Build and publish → Run workflow.

For the mining ecosystem network: The page reads directly from a separate published Google Sheet (CSV per tab). Sheet links are kept in manitoba-mining-map/assets/config.js. Snapshots in manitoba-mining-map/data/ are used as a fallback when a link is empty or the sheet can’t be reached. The page footer reports whether the data came live from the sheet and how many data problems were found.

## Licence

Code: MIT (see LICENSE). Data: CC BY 4.0 (see LICENSE-DATA.md). Please credit the project as described there.

## Related

A companion to the [Deep-Sea Mining Knowledge Board](https://github.com/elementspod/deep-sea-mining-knowledge-board). The two share conventions but are kept as separate repositories.

Part of research associated with The Elements of Deep Sea Mining.
