# Shared setup before feature work

Read for every profile. Suggested paths are contracts to adapt, not an instruction to replace an existing structure.

Contents: [inventory](#c01-inventory-and-repo-policy), [toolchain](#c02-toolchain-and-dependencies), [scripts](#c03-executable-quality-commands), [routes/config](#c04-route-and-environment-contracts), [errors](#c05-failure-and-request-boundaries), [tests](#c06-test-foundation), [CI](#c07-continuous-integration), [public reuse](#c08-public-repository-hygiene), [handoff](#c09-developer-handoff).

## C01 Inventory and repo policy

- **Inspect:** `AGENTS.md` at applicable directory levels, README, package scripts, lockfile, runtime pin, framework config, CI, adapters, env access, test discovery, git status and branch. Inventory existing routes/services before choosing a profile.
- **Files:** merge `AGENTS.md`; create `docs/bootstrap.md`, `docs/bootstrap-tasks.md` and an isolated checkout/worktree where needed.
- **Specify:** allowed branches/actions, exact verification commands, generated-file rules, production/provider boundaries, and how to report pending evidence. A fresh repo may use `dev` for integration and `main` for releases; existing rules take priority.
- **Verify:** record `git status --short` and `git branch --show-current`; identify unrelated edits. Confirm the working directory contains the intended repository.
- **Done:** task inventory/profile/capabilities recorded, unrelated work preserved, no operation depending on an unknown policy performed.

## C02 Toolchain and dependencies

1. Select compatible current stable versions using official framework/package support information. Preserve a compatible existing stack and lockfile.
2. Record one runtime pin such as `.node-version` or `.nvmrc`, `package.json#engines` and `packageManager`. Keep values consistent with CI/container config.
3. Use exactly one package manager and its committed lockfile. Add only selected framework, checks, test runner and fast-check; add integration packages when the matching capability is selected.
4. Put test/build tools in dev dependencies. Runtime packages belong in production dependencies only when the production output needs them.
5. Document install prerequisites and any required dependency lifecycle scripts. Do not blindly apply `--ignore-scripts` to a framework install that needs them.
6. Exclude generated build output, dependency directories and real env files with adapted ignore rules. Preserve content/schema lock artifacts required by the chosen CMS's workflow.

**Commands:** `node --version`, selected manager `--version`; `npm ci` or `pnpm install --frozen-lockfile` in a clean isolated checkout. Use the selected manager for every later command.

**Tests/evidence:** installation does not change the lockfile; declared/runtime/CI versions agree; missing optional provider credentials do not prevent unrelated development. An absent required native/lifecycle artifact must fail visibly, not be papered over.

## C03 Executable quality commands

Install compatible tooling and create the following script contracts. Existing names may differ; record exact equivalents. No empty scripts, unconditional success or swallowed errors.

| Script | Required behavior | Typical Astro implementation |
| --- | --- | --- |
| `dev` | Start the actual local editor/framework pipeline | CMS generation wrapper if needed |
| `check` | Framework templates + strict TS checks | `astro check` |
| `lint` | ESLint or established equivalent checks source and selected scripts | Framework-aware config; avoid generated/vendor output |
| `format:check` | Check formatting without rewriting | Prettier check with framework plugins where required |
| `test` | Run deterministic tests **and properties** once, fail on no tests | `vitest run` or existing runner |
| `test:watch` | Optional interactive developer runner | Separate from CI |
| `test:e2e` | Browser tests against the appropriate built target | Playwright; meaningful navigation/interaction |
| `build` | Required content/codegen then production build | Astro build |
| `preview` or `start` | Run the actual built target for smoke tests | Preview is not automatically the production server |
| `test:mutation` | Scoped Stryker with reviewed accounting | Only after meaningful selected modules exist |

**Files:** framework strict `tsconfig.json`, framework-aware lint/format config, ignores, `package.json` and test config. Check non-framework server/scripts separately if the framework checker does not cover them.

Before a stack/provider/version decision is resolved, record proposed script contracts as pending. Replace them with exact executable commands once configured; never report a proposed command as installed or run.

**Run:** `npm run check`, `npm run lint`, `npm run format:check`, `npm test`, `npm run build`, or manager equivalents. Record outputs and discovered tests. Document build order explicitly.

**Done:** commands actually run the promised tools, fail on relevant defects and work in a clean clone with documented non-production prerequisites.

## C04 Route and environment contracts

**Files:** `docs/routes.md` using the route matrix, `docs/environment.md` using the registry, `.env.example`, and a selected framework config module such as `src/lib/config/site.ts` or `src/lib/server/env.ts`.

For each route record path/pattern, rendering mode, audience, access rule, mutations, indexing, cache policy, analytics eligibility and test. An app's marketing page and dashboard must have separate rows.

For each variable record purpose, secret/public classification, build/runtime use, applicable environments, default, validation, missing-config behavior and owner. Prefer explicit feature flags and exact allowlists over accidental enablement from a populated ID.

- Parse boolean/number/list values explicitly, including whitespace/empty/invalid values. Define minimum/maximum units for timeouts, body limits, batch sizes and TTLs.
- Validate required config at its actual use/startup boundary. Optional disabled features need no credentials; enabled incomplete features fail visibly.
- Separate dev/test/preview/production origins, accounts, storage and secrets. Preview cannot accidentally use production writes or analytics.
- Public build configuration is embedded in output. Static files do not read host runtime env by themselves. Server runtime config must use the framework's supported private mechanism.
- Don't expose private configuration through errors, client imports, public settings endpoints or serialized page data.

**Tests:** unset optional feature; enabled missing/invalid config; exact-host mismatch; malformed URL/boolean/bounds; secret sentinel absent from client HTML/JS/maps/public JSON and logs. Inspect actual generated output, not only source imports.

**Done:** every env access has a registry entry; disabled defaults are safe; real credentials are unnecessary for unrelated checks; no copied provider/site identifiers.

## C05 Failure and request boundaries

**Files:** only where calls exist, `src/lib/server/http.ts`, input schemas, redaction helper and framework error boundary.

For every network/processor boundary specify accepted method/content type, input schema, maximum bytes/items, timeout/cancellation, allowed destination, retry policy and success evidence. Treat third-party JSON and persisted nullable fields as untrusted.

- Check HTTP status before parsing success; validate response shape; distinguish absence, rejection, timeout, provider outage and partial completion.
- Bound fetches and long operations. Retries are finite and must respect idempotency. A timeout after a write may be an unknown outcome requiring reconciliation.
- Return safe actionable errors and appropriate status codes. Do not return success after a required downstream failure.
- Log operation, safe error class and non-sensitive correlation ID. Redact tokens/cookies/authorization, DB query parameters, bodies and personal data. Don't log arbitrary URLs.
- A dependency outage must not silently sign everyone out, fabricate empty data or report a job complete.
- Preserve framework origin/CSRF protections. Proxy compensation belongs in the selected host contract, with tests.

**Tests:** malformed/non-JSON response, wrong status, missing nullable field, timeout/abort, partial batch failure, retry exhaustion, log redaction and no forbidden side effects. For a files-only site with no network/server behavior, server helpers are N/A; content/build failures remain applicable.

**Done:** users can tell whether work completed; logs diagnose failures without exposing supplied data.

## C06 Test foundation

Read all testing requirements T01-T07. Set up runner discovery, controlled fixtures/time, fast-check options and an invariant register before implementing new domain behavior.

**Files:** runner config, `tests/fixtures/` or adjacent fixtures, `docs/testing-invariants.md`, real `*.test.*` and `*.pbt.test.*`. Add Playwright configuration for a browser-visible project. Use portable synthetic fixtures without real customers.

**Done:** ordinary test command discovers both test types, initial properties cover actual bootstrap behavior, at least one relevant deliberately broken contract produces a failing test. If only the harness exists, mark substantive property coverage pending.

## C07 Continuous integration

**File:** `.github/workflows/checks.yml`, adapted for the target manager/build pipeline.

Order: checkout intended SHA → pin runtime/manager → frozen install → required codegen → check/lint/format → deterministic + property tests → production build → required built-output checks. Browser/DB jobs can run separately using isolated resources.

- Restrict workflow permissions, normally `contents: read`; pin actions to reviewed full commit SHAs.
- Define job timeout, test failure artifact upload and bounded artifact retention. Exclude env, tokens and personal data from logs/reports.
- Cache dependencies with manager/runtime/lockfile keys. Don't use caches as substitutes for generation/migrations.
- Fork PR verification uses no production secrets or privileged write triggers. No untrusted PR code with deployment credentials.
- Use disposable test storage; include clean migrations. Provider sandbox verification requiring credentials is a separate controlled job/run, not a fake green mock labeled integration.
- Keep deployment separate from verification unless the project's reviewed release policy explicitly combines them.
- Configure branch required checks through available authorized admin capability or leave an explicit owner task; a YAML file does not enforce branch protection.

**Tests/evidence:** local equivalent commands pass; a real CI run on the intended SHA passes. Workflow/branch protection remain pending until exercised/observed.

## C08 Public repository hygiene

**Files:** root README, chosen LICENSE, ignore rules; sanitize templates, fixtures, screenshots and generated artifacts.

- Document what can run locally and which providers are optional. Keep account creation/payment/production credentials outside the default setup path.
- Choose the license with the owner when unresolved; preserve third-party licenses and attribution. Do not assume source-project code can be relicensed.
- Remove inherited brands, domains, analytics IDs, mail destinations, project IDs, bucket names, dataset/customer rows and hard-coded production origins.
- Inspect tracked files and output for secrets, credentials and copied identifiers. If actual secrets reached history, removing the current file is insufficient; follow authorized rotation/history handling.
- Verify generated fixtures are synthetic, public source citations contain no private data, and examples cannot perform live external writes by default.

**Done:** a fresh clone can follow the README, applicable checks pass, diff/artifact review is recorded, no accidental account/service activation.

## C09 Developer handoff

Record exact commands, required config, task evidence, skipped modules with reasons, generated-file rules and first-feature dependencies. Keep `AGENTS.md` commands in sync with scripts.

Use separate gates:
1. **Local foundation:** reproducible install, actual checks/tests/build, selected minimal UI/server/data boundaries verified.
2. **Integration:** real CMS/provider/DB/email/billing sandbox paths and failure cases verified where selected.
3. **Release:** CI, deployed SHA, provider setup, monitoring/privacy/recovery evidence.

Name any pending integration and the feature work it blocks. Commit verified owned changes under the target's policy. Push/merge/deploy according to session authorization and applicable target rules.
