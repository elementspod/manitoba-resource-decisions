// Manitoba mining ecosystem map: where the page gets its data.
//
// HOW TO CONNECT THE GOOGLE SHEET (April):
// 1. In the Google Sheet: File > Share > Publish to web.
// 2. For EACH tab, choose the tab name and "Comma-separated values (.csv)", then Publish.
// 3. Paste each link below, between the quotes. Links look like:
//    https://docs.google.com/spreadsheets/d/e/2PACX-.../pub?gid=123456&single=true&output=csv
// 4. Leave a link empty ("") and the page uses the snapshot in data/<tab>.csv instead.
//
// The tab names in the sheet must match the keys below exactly.
window.MAP_CONFIG = {
  sheet: {
    meta: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=1090299241&single=true&output=csv",
    stages: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=1546083628&single=true&output=csv",
    categories: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=1091783644&single=true&output=csv",
    subgroups: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=995025980&single=true&output=csv",
    relationship_types: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=1431436695&single=true&output=csv",
    actors: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=496234165&single=true&output=csv",
    links: "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYc0eSe7Rw8novgTBLpGudWiFToxtikfxkEAdWE9iAsgo3Amy8BlmX-MfCpJIy59LXYmweGBLz4rZs/pub?gid=1242250853&single=true&output=csv"
  },
  // Snapshot folder used when a sheet link is empty or the sheet can't be reached.
  fallback: "data/"
};
