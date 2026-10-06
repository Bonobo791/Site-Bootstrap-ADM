# Selected-target deployment setup

Read when a host is selected or release preparation is requested. Implement configuration and local smoke tests within current authorization; production access/deploys follow target/session boundaries.

Contents: [target](#d01-target-and-artifact-contract), [configuration](#d02-environment-and-release-configuration), [container](#d03-node-and-docker-if-requested), [health](#d04-health-readiness-and-provenance), [CDN](#d05-proxy-and-cdn-if-used), [recovery](#d06-data-migration-and-recovery-if-used), [release](#d07-release-and-rollback-record), [gate](#d08-release-readiness).

## D01 Target and artifact contract

**Files:** selected adapter/host configuration, README commands and release runbook.

Record primary host, artifact type/output path, runtime/adapter, start command/port, base path/origin, redirects/headers, build-time versus runtime settings and who releases.

| Profile | Publish/run contract | Smoke evidence |
| --- | --- | --- |
| Files-only website | Publish generated HTML/assets; no server start or private runtime env | Page, asset, metadata, redirect/404 and headers from served output |
| Hybrid content site | Publish static output plus actual endpoint runtime | Static smoke plus valid/rejected endpoint requests |

Build every **selected** target, not every adapter available. A local framework preview can differ from the deployment runtime; verify selected-host assumptions separately.

## D02 Environment and release configuration

**Files:** environment registry, chosen host settings/runbook and controlled CI deployment job only if requested.

- Use separate dev/test/preview/production resources/credentials. Define which environments may write to which providers.
- Required runtime secrets are injected by the host's secret mechanism, never committed or embedded as client/build constants.
- Genuine build-time CMS secrets use the platform build-secret facility; inspect generated output for leakage.
- Static configuration substitutions require rebuilding. Runtime switching requires an actual server endpoint or deployment-owned runtime JSON; verify caching and update procedure.
- Default optional tracking/external-write features off in clones/preview; no inherited IDs/destinations.
- Document selected origin/port/adapter selectors, exact valid values and startup failure when invalid.
- Limit deployment credential scope. Fork PR verification cannot gain those credentials.
- Branch checks/release restrictions are observed/admin-configured where available; otherwise leave owner tasks pending.

**Evidence:** invalid config fails; intended environment uses isolated resources; same server artifact honors changed runtime values; secret sentinel absent from output/layers/logs. Production provider values are operator evidence, not a prerequisite for local checks.

## D03 Node and Docker, if requested

**Files:** compatible Node adapter/start script, `Dockerfile`, `.dockerignore` and optionally a selected local compose file.

1. Define compatible runtime/image versions; pin reviewed image digest when building reproducibly.
2. Use multi-stage install/build/runtime stages. Frozen install and required generation precede framework build.
3. Copy only necessary production output/dependencies; use an unprivileged runtime user where compatible.
4. Exclude env, git history, node_modules, local DB/backups/reports and secrets from context.
5. No secrets in ARG/ENV/layers. Use build secret mounts only for an actual build requirement; runtime credentials are injected later.
6. Bind documented port/address suitable for the host and implement graceful termination where needed.
7. Persistent storage is a selected explicit volume/provider; don't place durable app data in an ephemeral container filesystem.
8. Container startup does not blindly run destructive migration/purge tasks or serve before required readiness. Define release migration sequencing separately.

**Commands:** actual `docker build`; run image with isolated env/ports; HTTP smoke; shutdown/restart; inspect image/config/build output without printing actual secrets. Record exact command/image digest. If container tooling is unavailable, Docker readiness remains pending.

**Done:** built image runs intended target, uses appropriate storage/secret boundaries and terminates/restarts safely.

## D04 Health, readiness and provenance

**Files:** non-sensitive commit marker; liveness/readiness routes only for a runtime that needs them.

- Static site: generate a public marker such as `build.json` with commit SHA, and verify actual page/asset output. No fake health API.
- Server: liveness confirms process responsiveness without session/DB/provider lookup. Readiness checks only required dependencies/schema, with explicit timeout/failure.
- Expose safe status/SHA, never DB strings, tokens, account metadata or raw exception details.
- Treat local SHA absent during development explicitly; release verification requires expected artifact identity.
- Cache marker/health/readiness/runtime settings appropriately, normally bypass shared CDN cache. A stale cached response cannot prove new code serves.
- Define independently what proves scheduler ticks, provider delivery and restore. Health proves none of them.

**Tests:** expected SHA served; DB outage leaves liveness available but readiness unavailable where DB required; malformed config/startup failure; cache headers/no secret output. Static marker matches built artifact.

## D05 Proxy and CDN, if used

**Files:** host/CDN route/cache settings, proxy contract and purge/release script only when selected.

- Verify DNS/TLS, origin scheme/Host, redirect loop prevention, actual forwarded headers and trusted IP chain.
- Preserve framework origin/CSRF controls. Only compensate for an observed trusted-proxy requirement, with explicit endpoint origin/abuse tests.
- Public HTML has reviewed bounded TTL; hashed assets can use long immutable caching. Unversioned media needs a reviewed invalidation policy.
- Bypass API/auth/private pages/preview/runtime settings/health/provenance. Test two accounts cannot receive another's cached response.
- Purge only after expected SHA is serving and required readiness succeeds, once per release event. Don't duplicate CI and startup purges.
- Scope CDN admin credentials to operator/deployment task, never browser/runtime public config.

**Evidence:** actual response headers/cache behavior, allowed/forged proxy requests, expected SHA then one purge; not just configuration files.

## D06 Content and provider recovery, if used

**Files:** selected content/media recovery procedure and actual provider retention/backups record.

1. For Git-backed content, record the known-good revision and rehearse restoring synthetic content/schema into an isolated checkout; rebuild and inspect the pages.
2. For externally stored CMS/media/contact data, record actual provider backup/retention/export/recovery capabilities and owner.
3. Rehearse only the selected recovery contract using isolated resources; verify files/content, access, generated schema and usable page/endpoint output.
4. Keep sensitive exports/keys out of public git and build context. Choose recovery objectives from actual requirements and observations.
5. Files-only output does not imply a database backup requirement. An untested provider checkbox does not establish recovery.

**Done:** observed recovery for the actual selected stores. Missing provider access stays pending. No database or paid backup service is added by default.

## D07 Release and rollback record

Use `assets/release-runbook.template.md` adapted into `docs/release-runbook.md`.

Record prerequisite checks/provider configuration, reviewed release SHA/artifact, migration step/owner if needed, publish/start procedure, expected origin/cache behavior, smoke requests and rollback path.

After an authorized release, verify served expected SHA; public/private/endpoint paths; selected provider sandbox/live boundary; cache invalidation; logs/readiness; scheduler/alert evidence if selected. Record actual outcomes, not deployment intent.

Operator tasks need an owner and clear evidence request. Do not repeatedly ask for permission for already authorized reversible setup; stop only at an action genuinely outside authorization.

## D08 Release readiness

All applicable local/integration gates pass; intended SHA's CI passes; selected deployed artifact/providers serve correctly; indexing/privacy/cache/resource isolation reviewed; actual restore and scheduler/alert checks pass where relevant.

If any evidence is unavailable, mark the specific D requirement pending. Report local/scoped feature readiness separately. No server/CDN/container/DB requirements apply to a files-only site unless its brief selects them.
