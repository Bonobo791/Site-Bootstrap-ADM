# Environment registry

Replace illustrative names with actual framework/provider names. Include only selected capabilities. Secrets and project IDs have no copied values.

| Name | Purpose/capability | Public/private | Build/runtime | Dev/test/preview/production | Default | Validation + bounds | Missing/invalid behavior | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SITE_URL | Canonical/app origin | Public value | Explicit per target | Isolated origins | Chosen local origin | URL scheme/host/path/query policy | Fail selected production config | |
| ANALYTICS_ENABLED | Requested marketing collection | Server config/public projection | Runtime | Off in local/preview/fork | false | Explicit boolean policy | Ineligible | |
| UMAMI_URL / UMAMI_WEBSITE_ID | Requested collector | Public values via projection, no credentials | Runtime | Deployment-owned | Empty | Approved origin/ID | Invalid enabled config diagnosed; no collection | |
| ANALYTICS_ALLOWED_HOSTNAMES | Exact deployment host gate | Public projection | Runtime | Explicit aliases | Empty | Exact hostname list | No collection | |
| DRY_RUN | Only for tested external-write feature | Private | Runtime | Explicit | true | Boolean + exact write prohibition | Safe documented failure | |

Add bounds/units for body size, timeout, batch limit, session/lease/retention duration when those settings exist. Record how secrets are injected, public projections are served, invalid values are tested and sentinel leakage is checked. A static host cannot magically supply private runtime env to built files.
