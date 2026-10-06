# Planning contract

## Required plan sections

| Section | Required content |
|---|---|
| Identity | Stable plan ID/version, date, author/reviewer, state, project/team, timezone, target code repository and visibility |
| Brief | Problem, audience/roles, outcomes/KPIs, primary journeys and the user's constraints |
| Scope | Numbered R001… requirements with must/should/later priority, source, observable acceptance; exclusions and deferred backlog |
| Experience | Sitemap/screens, navigation, content/component inventory, visual references and chosen details, brand/assets, responsive/accessibility states |
| Behavior | Normal, validation, empty, forbidden, duplicate, concurrency, outage and recovery paths as applicable |
| Architecture | Selected bootstrap/revision, preserved/new stack, routes/public-private boundary, state/data ownership, identity, integrations and deployment target |
| Data | Entities/fields/relationships, constraints, personal-data destinations, consent/preferences, retention/export/deletion and recovery owners |
| Decisions | Accepted choices with reasons; proposed assumptions/confidence; bounded research decisions with owner, deadline and blocked tasks |
| Bootstrap | All selected source IDs, applicability reasons, task mapping and local/integration/release evidence gates |
| Work | Initiative/phase outcomes and exits, granular tasks, dependencies, owners/reviewers, estimates, confidence and required evidence |
| Calendar | Start/launch target, capacity/cadence/workdays, dated cycles, per-resource commitments, lead times, review/contingency allowances and critical path |
| Cost | Build and recurring ceilings, selected service costs verified from official sources, expected usage and unresolved spending decisions |
| Quality | Acceptance-to-test matrix; unit, integration, property and browser boundaries; performance/accessibility/privacy; provider and recovery checks |
| Release | Environment/config/secrets names, artifact/runtime/SHA, domain/DNS, migration, observability, smoke tests, launch approval/authorization, rollback and post-launch owner |
| Publication | Project marker/ref, plan-document ID, initiative/cycle/task/link ID map, readback results and any exact unsynced items |

Choose only applicable sections/modules; make N/A reasons explicit. Do not invent legal obligations, prices, benchmarks or provider capabilities. Consult official documentation for selected current software/providers. Record provider research as a task when the brief permits deferring selection.

## Initiative structure

Use ordered titles such as `01 · Foundation and setup`. Give each initiative a goal, scope/requirement IDs, entry prerequisites, exit evidence, owner, start/target dates and phase status. Suggested phases are starting points, not a mandatory count:

| Website | App |
|---|---|
| Scope/content/design decisions | Scope/workflows/domain and design decisions |
| Repository/tooling/website foundation | Repository/tooling/server boundary foundation |
| Content/layout/media/SEO | Selected data/identity/authorization foundation |
| Selected contact/CMS/runtime integrations | Small usable feature slices and selected providers |
| Product verification and real delivery | Product/provider verification and recovery |
| Launch/observation/handoff | Launch/observation/handoff |

Unresolved prerequisites get real tasks, not vague initiative prose. Independent work may overlap phases, but an exit-dependent task waits for its prerequisite. Avoid empty initiatives that only repeat a page name. Separate tasks for writing/approving content from rendering it when they have different owners or dependencies.

## Task record

Use `assets/task.template.md` from the skill's main resource directory. Every execution task needs:

- Stable local ID and action title with one verifiable outcome.
- Initiative and requirement IDs, including namespaced bootstrap IDs.
- Owner/resource and reviewer; real platform assignment only after resolving members.
- Dependencies, blockers, readiness, estimate range/chosen planning estimate, confidence and external lead time.
- Cycle and start/due dates for committed work; nullable dates/cycle for unscheduled or unresolved work.
- Exact deliverable and target files/exports/schema/configuration, or a precise named decision/output for research/content tasks.
- Ordered steps and executable commands when known; mark commands requiring later verification.
- Observable acceptance, positive and negative/failure cases, forbidden side effects, test layers and evidence required for completion.

Split work larger than the user's agreed session size. Include implementation and meaningful verification in estimates, or create an explicit linked verification task. Do not split into cosmetic checklist fragments with no independent completion outcome. Parent/child grouping is optional; a parent is not a dependency link. Avoid double-counting parent estimates when children already carry the work.

## Testing and fast-check

State behavior before test mechanics. Cover real functions/services and built pages; avoid tests that assert their own fixture or reproduce implementation. Map R IDs to checks with expected outputs. For requests name the test, method/path/body and correlation-ID behavior; capture safe error detail and full stack in restricted diagnostics, redacting secrets/personal data. Review existing coverage first. The user's 80% coverage target is a planning target, not proof of sufficient behavior coverage or permission to add trivial tests.

Create product-specific fast-check tasks for invariant definition, runner/CI integration, generated inputs with fresh state per run, shrunk regressions, seed/path replay and a relevant deliberate fault. Website candidates include canonical/redirect/content/metadata rules and hostile form input producing no delivery side effects. App candidates include owner isolation, session expiry, valid state transitions, idempotent payments/jobs and authoritative entitlements. Add only applicable domains. Preserve independent expected behavior; the bootstrap demo only illustrates harness use.

Separate unit/property checks, disposable integration, browser journeys and actual provider sandboxes. Include accessible mobile/desktop UI states and representative performance checks where required. Scope mutation testing to important modules and define example/property kill accounting; do not claim it ran during planning.

## Review and handoff

Check every must-have R ID and applicable bootstrap ID has at least one task and acceptance/evidence. Check every scheduled task belongs to an initiative/cycle and names its prerequisites. Review secrets, public artifacts, data transfers, provider costs and launch/recovery blockers as concrete requirements, not generic warnings.

Present a plan the user can assess: product behavior, launch scope, chosen approach, calendar, cost and open decisions. Record agreed changes and delegated assumptions. Planning completion means an accepted actionable plan and verified project publication, not a built or deployed product.
