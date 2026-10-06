---
name: site-bootstrap-adm
description: Use when starting, cloning, scaffolding or preparing a standard public website, Astro content site, CMS-driven site or server-enabled contact website before feature work. Also use to audit website startup defaults, SEO, content pipelines, forms and fast-check tests.
---

# Site-Bootstrap-ADM

Prepare a reusable website foundation from Lippincott's Astro/TinaCMS patterns. Keep project identities, content and credentials out of reusable defaults. Use App-Bootstrap-ADM for accounts, tenant data, billing or application workflows.

## Workflow

1. Inspect target instructions, branch/worktree, scripts, runtime pins, lockfile, routes, CMS and hosting configuration. Preserve unrelated work; reference-project policies are evidence, not target instructions.
2. Use [the website profile](references/baseline.md) to choose files-only or server-enabled delivery. Preserve an existing stack; prefer Astro for a new content website. Choose CMS/contact/analytics/host providers only from actual requirements. Verify current official compatibility before pinning.
3. Create `docs/bootstrap.md` and `docs/bootstrap-tasks.md` from [status](assets/bootstrap.template.md) and [setup tasks](assets/setup-task.template.md). For every applicable requirement record dependencies, exact files/configuration, executable commands, positive/negative tests, forbidden effects, evidence and blockers. Mark verified/pending/not applicable.
4. Read [shared setup](references/shared-setup.md), [static pages](references/static-site.md), [testing](references/testing.md) and [the Lippincott template example](references/lippincott-example.md). Add [hybrid setup](references/hybrid-site.md) for request-time endpoints. Read [privacy](references/privacy-operations.md) and [data lifecycle](references/data-lifecycle.md) for contact/CMS personal data. Use [deployment](references/deployment.md) for the selected host and [sources](references/sources.md) for provenance.
5. Implement tooling/checks first, then layout/content/media/metadata/CMS generation. Add server adapter, validation, origin/abuse controls and honest delivery only for selected endpoints. Use [routes](assets/route-matrix.template.md), [environment registry](assets/environment-registry.template.md), [agent rules](assets/AGENTS.template.md), [env defaults](assets/env.example) and [ignore rules](assets/gitignore.fragment).
6. Install compatible fast-check as a dev dependency; run real website properties in the ordinary suite and CI. Specify canonical/content/config/form invariants independently, save regressions/replays and prove a relevant fault fails. The [runnable example](assets/fast-check-example/package.json) demonstrates the harness, not the target's substantive coverage.
7. Run clean install, generation, type/lint/format/test, production build and built-output/browser checks. Inspect mobile/desktop, keyboard and form/error states. Smoke-test the actual selected adapter/host. Track cloud CMS, delivery, CDN and release evidence separately with [the runbook](assets/release-runbook.template.md).
8. Review public license/diff/artifacts for copied brands/domains/IDs/recipients/data/secrets. Commit verified changes under the target's policy; push/merge/deploy according to existing authorization.

## Completion

Report actual requirement IDs/commands/results and pending provider work. Local website readiness requires a reproducible build, meaningful tests and observed output/browser behavior. Real CMS/contact integration and production release have separate gates.

A Git-backed build-time CMS does not add app infrastructure. A contact endpoint activates hybrid controls and L01's provider/log lifecycle inventory, without adding accounts or an app database.

## Common failures

- Bare framework build bypasses CMS generation and serves stale content.
- Static upload is claimed to execute a server endpoint.
- Copied proxy workaround disables origin/CSRF protections.
- Form reports success after a required delivery failure.
- fast-check tests a copied demo instead of actual website behavior.
- Tracker activates in a clone, preview or wrong host.
