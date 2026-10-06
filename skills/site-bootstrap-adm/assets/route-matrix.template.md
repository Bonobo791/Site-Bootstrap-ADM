# Route contracts

Create one row per route or same-contract family. The rows below illustrate distinct policies; replace paths with actual routes and omit unselected capabilities. No row grants access by itself.

| Path/pattern | Render/runtime | Audience/access | Allowed mutations | Indexing | Cache | Analytics | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| / | Static or server-public | Everyone | None | Public canonical | Reviewed public TTL | Only explicit opt-in eligibility | Built metadata/page/network |
| /admin or preview | Selected CMS runtime | Verified editor | Authorized CMS changes | Noindex | No-store | Denied | Unauthorized/draft/cache tests |
| /api/contact | Server endpoint | Public with origin/abuse policy | Validated lead delivery | Non-indexable endpoint | No-store | No submitted-data collection | Input/origin/zero-effect/delivery tests |
| /api/analytics | Runtime public settings | No session/DB dependency | None | Non-indexable endpoint | No-store | Config only | Runtime/no-secret/host tests |
| /api/health or marker | Selected runtime/static marker | Safe public status | None | Non-indexable | Cache bypass | Denied | SHA/outage/redaction tests |

Also record slash/base-path policy, canonical origin by environment, response statuses, redirect map, exact origin/CSRF policy, trusted proxy chain and query/payload rules for each relevant family.
