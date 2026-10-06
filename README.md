# Site-Bootstrap-ADM

Template repository for Advanced Digital Marketing LTDA websites, with a bootstrap skill and templates based on [The Lippincott Team](https://github.com/Bonobo791/the-lippincott-team). Use **`$site-bootstrap-adm`** before building a standard website.

The package has 46 setup requirement groups for static and server-enabled content websites. It covers pinned tooling, layouts, CMS content/build order, media, SEO, redirects, contact endpoints, privacy, testing and selected hosting. Each applicable task specifies files, configuration, commands, positive/negative tests, evidence and blockers.

## Lippincott template example

[The worked example](skills/site-bootstrap-adm/references/lippincott-example.md) maps the inspected Astro/TinaCMS project into a neutral new-site foundation:

- Shared layout, tokens, navigation and responsive/keyboard checks.
- Selected content collections, CMS schema/client generation and local build.
- Canonical metadata, sitemap/robots, optimized media and URL migration checks.
- Optional contact runtime with bounded input, origin/abuse controls and truthful delivery.
- Release SHA, selected host/cache and content/provider recovery evidence.

Real-estate content, Sierra CRM, branding, recipients, tracking IDs and CDN accounts are selected separately for each project.

## Detailed setup

[Shared](skills/site-bootstrap-adm/references/shared-setup.md) · [Static pages](skills/site-bootstrap-adm/references/static-site.md) · [Server endpoints](skills/site-bootstrap-adm/references/hybrid-site.md) · [Testing](skills/site-bootstrap-adm/references/testing.md) · [Privacy](skills/site-bootstrap-adm/references/privacy-operations.md) · [Data lifecycle](skills/site-bootstrap-adm/references/data-lifecycle.md) · [Deployment](skills/site-bootstrap-adm/references/deployment.md)

Templates create bootstrap/task records, route policies, an environment registry, agent rules and a release runbook. Local, provider integration and release readiness have separate evidence gates.

## Fast-check

The ordinary test suite must discover real website properties alongside regressions. Define independent content/canonical/config/form invariants; cover hostile input, replay shrunk failures and prove detectable faults. Scoped Stryker guidance covers meaningful selected modules.

The bundled synthetic analytics gate demonstrates the harness. Apply the pattern to the target's actual website logic; the demo does not prove target coverage or tracking transport safety.

## Install and invoke

For an agent supporting `~/.agents/skills`, copy the skill from this repository:

```sh
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/site-bootstrap-adm && \
  cp -R skills/site-bootstrap-adm ~/.agents/skills/
```

Use the host's corresponding directory when different; merge an existing installation deliberately.

> Use $site-bootstrap-adm to prepare this Astro content website from the Lippincott template example. Include fast-check and exact setup tasks before feature work.

For apps use [App-Bootstrap-ADM](https://github.com/Bonobo791/App-Bootstrap-ADM).

## Validate this repository

```sh
python3 scripts/validate.py
cd skills/site-bootstrap-adm/assets/fast-check-example
npm ci --ignore-scripts
npm test
```

The demo is locked separately from any website being prepared. Refresh official framework/provider compatibility on reuse.

Prepared 2026-10-06. [Source provenance](skills/site-bootstrap-adm/references/sources.md) identifies pinned snapshots. MIT covers the original guidance/templates/demo; source projects retain their own licenses.
