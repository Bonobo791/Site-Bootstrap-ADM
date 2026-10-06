# Bootstrap selection and task expansion

| Intended product | Required planning source | Profile |
|---|---|---|
| Public pages, blog, portfolio or marketing website | `$site-bootstrap-adm`, [Site-Bootstrap-ADM](https://github.com/Bonobo791/Site-Bootstrap-ADM) | Files-only unless runtime requirements select hybrid delivery |
| Website with CMS/contact/preview/runtime search | Website skill and applicable hybrid references | Files-only for build-time CMS or an external hosted form; hybrid for site-owned runtime routes |
| Interactive utility, portal, account workflow or SaaS | `$app-bootstrap-adm`, [App-Bootstrap-ADM](https://github.com/Bonobo791/App-Bootstrap-ADM) | Activate storage/identity/providers only when needed |
| App with public marketing pages | App skill plus its public-page references | One app with public/private route boundaries |
| Independent website and app | Both profiles in their workstreams | Separate projects when the user chooses separate ownership/releases |

Find installed skills by frontmatter name rather than saved UUID. For public distribution read `skills/<skill-name>/SKILL.md` at the repository's inspected commit. This planner may be bundled without the other bootstrap; fetch/install the selected one with an available authorized GitHub capability. Do not assume a local sibling exists. If access fails, keep revision/commands unverified while preserving the interview.

Inspect repository metadata/head and record the commit. Review target instructions before planning cloning, edits or release actions. Pin the source at implementation time and review upstream changes when it differs. Preserve licenses. Use the new product's branding, domains, content, recipients, accounts and privacy choices.

## Requirement coverage

Namespace IDs by profile (`site:C01`, `app:C01`) in combined plans. Enumerate IDs from current source references; the counts below describe the inspected 2026-10-06 packages and can change. Record each ID as applicable or N/A with a reason. Map applicable IDs to concrete task IDs and evidence.

| Groups | Planning work |
|---|---|
| Site C01–C09 | Context, runtime/manager pins, quality scripts, route/env contracts, errors, tests, CI, public hygiene, handoff |
| Site S01–S09 | Layout/tokens, page/content, selected CMS generation, media, metadata, navigation/redirects, output/browser checks |
| Site H01–H07 | Adapter/routes, input limits, origin/abuse, truthful delivery, runtime features, hybrid verification/readiness |
| Site L01 | Contact/CMS/provider/log lifecycle, access/retention/deletion |
| App C01–C09 | Shared context/tooling/contracts/errors/tests/CI/hygiene/handoff |
| App A01–A12 | Server boundaries; selected session, ownership, schema/migrations, billing, APIs, jobs, uploads, lifecycle, UI and readiness |
| App M01–M03 | Public layout/metadata, indexing exclusions, media/performance/browser checks |
| Both T01–T07 | Runner, independent invariants, properties/fresh state, replay/regressions, layers, relevant faults/mutation scope, completion |
| Both P01–P05 | Default-off analytics, hosts/public routes, preferences/payload exclusions, actual transport and personal-data operations |
| Both D01–D08 | Selected host/artifact/env/runtime/proxy/cache, readiness/provenance, appropriate recovery, release/rollback and launch evidence |

Read references for exact ID definitions; this table does not replace them. Site currently has 46 groups; app has 44. Optional CMS, DB, auth, payments, jobs, uploads and paid services need a reason in the brief. Lippincott's Astro/TinaCMS and Moderaty's SvelteKit are examples, not authority to copy their business features or workarounds.

## Implementation handoff

Plan the target scaffold, local foundation, actual integrations and release verification. For existing code plan changes instead of copying over it. Name framework files or leave them pending a stack-decision task. Do not invent commands claimed to exist.

Each setup task carries its ID, prerequisites, concrete files/exports/schema/configuration, install/generate/check/build commands, positive/negative behavior, forbidden effects and evidence path. Evidence stays pending until performed. Put provider selection/access before integration and use sandboxes/disposable storage for tests.

Block launch until meaningful tests, built browser/host behavior, required real provider operations and recovery checks pass. A project board, CI file, installed package or synthetic demo cannot establish these results.
