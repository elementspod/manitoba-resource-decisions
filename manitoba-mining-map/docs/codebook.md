# Codebook: Manitoba mining ecosystem map

The page reads seven tabs from the Google Sheet "Manitoba mining map — data". Tab names and column headers must match exactly. The page skips rows it can't use and lists them in the footer as data problems, so after any edit, reload the live page and check that the footer says "0 data problems".

General rules (same as the DSM board):
- Never change an `id`. Other rows point to it.
- Never delete a relationship that ended. Add a note saying when and how it ended.
- No editor notes ("VERIFY", "TODO") in `description` or `note`. Those are public text.
- Uncertainty goes in `verification_status` and `verification_note`, not in the description.

## meta
| column | meaning |
|---|---|
| key | `compiled` (date, YYYY-MM-DD), `compiler`, `note` |
| value | text shown in the page footer and side panel |

## stages
| column | meaning |
|---|---|
| id | 0 to 5, in order. Actors refer to these numbers. |
| name | stage label shown on the life-cycle view |

## categories (the 7 top-level groups)
| column | meaning |
|---|---|
| id | short id, e.g. `gov` |
| name | label |
| color_slot | 1 to 7. Each slot is one colour in the page's validated palette. Don't reuse a slot. |
| description | shown when the group is opened |

## subgroups
| column | meaning |
|---|---|
| id | short id, e.g. `gov-mines` |
| category | a `categories.id` |
| name, description | shown in the map and panel |

## relationship_types
| column | meaning |
|---|---|
| id | e.g. `regulates` |
| label | shown in legend and panel |
| family | line colour: `auth` authority, `duty` consultation, `part` partnership/ownership, `money` money and markets, `svc` services/advice, `adv` advocacy, `opp` opposition |
| dash | line pattern within the family: empty = solid, `6 3` = dashed, `1 3` = dotted, `2 3` = short dash |

Direction matters. A link reads "source → type → target":
`regulates`, `oversees`, `consult` (Crown holds duty toward the Nation), `delegated` (company carries out engagement with the Nation), `partners`, `owns` (owner → owned), `funds` (funder → funded), `buys` (buyer → seller), `supplies`, `advises`, `advocates` (lobbyist → target), `represents`, `opposes` (challenger → challenged).

## actors (one row per organization)
| column | meaning | shown on page? |
|---|---|---|
| id | permanent id | no |
| name, short_name | full name; short label for the map (optional) | yes |
| subgroup | a `subgroups.id` | yes |
| description | role in Manitoba, plain and neutral, 1–4 sentences | yes |
| projects | free text | yes |
| stages | stage ids separated by semicolons, e.g. `0;1;2` | yes |
| stakes | −2 (mostly bears costs or risks) to +2 (mostly captures benefits). Editorial judgement. | yes |
| formal_power | 0–3: legal authority to approve, refuse or require consent. Editorial judgement. | yes |
| informal_power | 0–3: money, publicity, litigation, relationships. Editorial judgement. | yes |
| verification_status | `verified` (claims in the description checked against the listed sources), `partial` (some claims checked, the gap is in the note), `unverified` (role not established from sources) | yes |
| verification_note | what is not confirmed, in public-friendly words | yes |
| scores_review | `pending`, `approved` or `changed` (Eric's sign-off on stakes and power scores) | no |
| eric_review | Eric's decision or comment on the row | no |
| last_verified | date a person last opened the sources and checked the row | no |
| contributed_by | handle of whoever added or last verified the row | no |
| source1_title … source4_title, source1_url … source4_url | up to four sources; at least one URL is required | yes |

## links (one row per relationship)
| column | meaning | shown on page? |
|---|---|---|
| source, target | actor ids | yes |
| type | a `relationship_types.id` | yes |
| note | short, specific, public | yes |
| source_url | link supporting this relationship (shown as [source]). Blank for the first export: evidence currently sits in the two actors' sources. | yes |
| verification_status | `verified` or `partial`, as for actors | no |
| eric_review, last_verified, contributed_by | as for actors | no |
