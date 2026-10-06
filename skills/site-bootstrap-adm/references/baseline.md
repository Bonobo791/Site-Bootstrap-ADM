# Website profile and order

Use Lippincott as the template example. Its content pages, CMS pipeline, SEO, redirects, media and contact boundaries are applicable patterns; its client identity/providers/policies remain project-specific.

| Behavior | Apply | Conditional additions |
| --- | --- | --- |
| Public HTML/assets served as files | C01-C09, S01-S09, T01-T07 | Build-time CMS, selected host and optional analytics |
| Content with contact/search/preview/runtime settings | Static requirements plus H01-H07 | Only selected endpoint/provider controls |
| Personal data reaches CMS/contact provider or logs | L01 and relevant P requirements | Actual provider retention/deletion evidence |
| Accounts, tenant records, paid entitlements or app workflows | Use App-Bootstrap-ADM | Preserve already verified public content requirements |

## Resolve decisions

Record purpose/users/first page, current stack/manager, canonical origin/slash/base-path, selected content collections/CMS, primary host and any contact/analytics integration. Record branch/release boundaries and isolated resources. Unspecified providers remain pending with named blockers; continue independent layout/content/testing work.

## Implementation order

1. C01-C03: inventory, policy, pinned compatible toolchain and actual scripts.
2. C04-C07 and T01-T07: route/config registry, failure boundaries, runner/fast-check/CI.
3. S01-S09: static output, layout, content/schema, selected CMS generation, images, SEO, redirects and built-browser checks.
4. H01-H07 if server endpoints are selected: adapter, input/origin/abuse/delivery and real packaging.
5. L01/P01-P05 as applicable: provider/log personal-data policy and tracking safeguards.
6. D01-D08 for the selected host: artifact/runtime/cache/provenance and relevant recovery.
7. C08-C09: clean-clone/public review, verified commit and scoped handoff.

Expand every applicable ID into exact task records. Install only selected CMS/adapters/services. Database/session/billing/queue setup belongs to the app project when requested.

Lippincott's current package scripts have tests despite stale AGENTS prose claiming otherwise. Verify current source/commands, and preserve this target's actual instructions.
