# Release and recovery record

## Selected target

- Profile / host / adapter / artifact path:
- Runtime/image digest and start or publish command:
- Production origin / port / base path:
- Authorized release scope, actor and boundary:
- Required environment registry/provider configuration:
- Branch/check policy:
- Reviewed SHA/artifact:
- Actual CI run on that SHA:
- Dependencies/services with separate resources:
- Operator tasks still pending:

## Release sequence

1. Verify local and selected integration gates.
2. Verify actual provider/secret/origin/indexing/privacy configuration.
3. Perform only the authorized migration/release steps, with owner and compatibility/rollback plan.
4. Publish/start selected artifact.
5. Verify expected served SHA and readiness; inspect actual public/private/endpoint behavior.
6. Purge selected CDN once, after identity/readiness verification, if applicable.
7. Verify selected provider, scheduler, alerts and safe logs.

| Check | Exact request/command | Expected observation | Actual evidence/date or pending |
| --- | --- | --- | --- |
| Expected SHA | | | pending |
| Public content/assets/404/metadata | | | pending |
| Private access/no cache leakage | | | pending |
| Endpoint rejection/valid sandbox path | | | pending |
| Dependency health/readiness | | | pending |
| Optional tracking eligibility/payload | | | pending |
| Completed scheduler tick + missed-tick alert | | | pending |
| Selected delivery/provider state | | | pending |

## Rollback and recovery, if applicable

- Previous compatible artifact and exact rollback procedure:
- Database compatibility/destructive migration limits:
- Actual backup/PITR capability and retention:
- Isolated restore destination and guard:
- Restore procedure:
- Integrity/permissions/schema/usability checks:
- Observed recovery point/time and requirements:
- Keys/backup access owner and alert delivery:
- Last actual restore evidence:

## Final readiness

- Local foundation:
- Selected integration:
- Production release:
- Exact pending evidence/owner:
- N/A checks and reasons:

A health 200, source push, CI success or provider checkbox cannot substitute for served identity, real integration behavior or recovery.
