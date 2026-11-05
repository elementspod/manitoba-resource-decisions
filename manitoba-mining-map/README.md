# Manitoba mining ecosystem map

Interactive network of the players in mineral exploration and mine development in Manitoba. Plain HTML/CSS/JS, no build step. D3 v7.8.5 is vendored in `assets/vendor/` with its licence (ISC).

## Files
- `index.html`: the page
- `assets/config.js`: published Google Sheet CSV links, one per tab
- `data/*.csv`: snapshot of the sheet, used when a link is blank or the sheet can't be reached
- `docs/codebook.md`: what each column means
- `sheet-import/manitoba-map-data.xlsx`: all seven tabs in one workbook, for creating the Google Sheet

## Setup (April)
1. In Google Drive: New > File upload > `sheet-import/manitoba-map-data.xlsx`, then open it and choose File > Save as Google Sheets. Rename it "Manitoba mining map — data". Check the tab names are: meta, stages, categories, subgroups, relationship_types, actors, links.
2. File > Share > Publish to web: publish each tab as CSV (one at a time) and paste each link into `assets/config.js`.
3. Commit and push. Open the live page and check the footer says "Data loaded live from the Google Sheet" and "0 data problems".

The page must be served from a web server (GitHub Pages or the site). Opened as a local file, the browser blocks the data requests.

## Snapshots
Re-export each tab as CSV into `data/` on the same monthly cadence as the DSM board, and tag a release.
