# Site-Bootstrap-ADM

This repository contains a reusable agent skill, templates, examples, and reference material for preparing websites for Advanced Digital Marketing LTDA. It draws on [The Lippincott Team](https://github.com/Bonobo791/the-lippincott-team). Use `$site-bootstrap-adm` for a standard content website.

This repository is a website-preparation toolkit, not a deployable website. It does not contain a project's pages, CMS account, production content, or hosting configuration. The skill guides work in the actual website project and records what to build, test, configure, and verify before launch.

## Quick start

For an agent that supports skills in `~/.agents/skills`, install the planner and website bootstrap skills from the repository root:

```sh
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/plan-sites-and-apps-adm && \
  cp -R skills/plan-sites-and-apps-adm ~/.agents/skills/
test ! -e ~/.agents/skills/site-bootstrap-adm && \
  cp -R skills/site-bootstrap-adm ~/.agents/skills/
```

Use the host's corresponding skill directory when it differs. If the skill already exists, review and merge changes deliberately.

For a new site whose requirements are not agreed, run the planner first:

> Use $plan-sites-and-apps-adm to interview me about a new website, select the ADM bootstrap, and publish the agreed plan in It's a Plan with initiatives, tasks, and cycles.

After agreeing the plan, or when you already have an agreed plan, ask your agent to prepare the actual website project from it. For example:

> Use $site-bootstrap-adm to prepare [project path or repository] from the agreed website plan for [purpose and audience]. Preserve the existing stack; for a new content site, prefer Astro. Keep undecided CMS, contact, analytics, and hosting choices visible for me. Create the bootstrap and setup-task records, verify the site's real build and tests, and document the selected host's launch steps.

Your coding agent needs access to the actual website project. The skill prepares and verifies work there. The site's build, hosting, and release procedure depends on its stack and selected host, so this repository has no universal `npm run dev` or deployment command. Follow the commands recorded in the prepared project's README and `docs/release-runbook.md`. Production release follows that project's policy and authorization.

For account, tenant-data, billing, or other app workflows, use [App-Bootstrap-ADM](https://github.com/Bonobo791/App-Bootstrap-ADM).

## What is included

The website skill covers 46 setup requirement groups for static and server-enabled content sites. It guides decisions about the toolchain, layout, CMS generation, content and media, SEO, redirects, contact endpoints, privacy, tests, and the selected host. For each applicable requirement, the project records files, configuration, commands, positive and negative tests, evidence, and blockers.

The repository also includes:

- Website setup templates for `docs/bootstrap.md`, `docs/bootstrap-tasks.md`, routes, environment settings, agent instructions, and a release runbook.
- Static-site and hybrid-endpoint guidance, privacy and data-lifecycle notes, testing guidance, and host-specific deployment references.
- A Lippincott worked example that maps a real Astro/TinaCMS project into a neutral site foundation. Its branding, real-estate content, CRM, recipients, tracking IDs, and CDN accounts stay project-specific.
- A Fast-check demo that shows the test harness. It does not prove that a prepared website's actual behavior is correct.
- The Plan Sites & Apps skill for interviewing about a new product and deciding whether to use this website workflow or App-Bootstrap-ADM.

## How the workflow works

The skill inspects the target project's instructions, existing stack, scripts, routes, CMS, and hosting settings. It preserves an existing stack and prefers Astro for a new content website. It selects a CMS, contact service, analytics tool, or host only when the project requirements call for one.

The workflow records the applicable requirements in `docs/bootstrap.md` and `docs/bootstrap-tasks.md`. It then guides implementation, testing, local build checks, browser review, and selected-host smoke tests. Static pages and request-time endpoints have different launch requirements. A contact endpoint needs its own server runtime and privacy, abuse, and delivery checks.

The detailed requirements live in [Shared setup](skills/site-bootstrap-adm/references/shared-setup.md), [Static pages](skills/site-bootstrap-adm/references/static-site.md), [Server endpoints](skills/site-bootstrap-adm/references/hybrid-site.md), [Testing](skills/site-bootstrap-adm/references/testing.md), [Privacy](skills/site-bootstrap-adm/references/privacy-operations.md), [Data lifecycle](skills/site-bootstrap-adm/references/data-lifecycle.md), and [Deployment](skills/site-bootstrap-adm/references/deployment.md).

## Launch a prepared website

Use the generated project's release notes for the exact launch command and destination. The bootstrap workflow leaves host selection and project configuration tied to that site instead of assuming a provider.

Before release, the target project should:

1. Select the actual output type and host. A files-only site publishes generated HTML and assets. A site with runtime endpoints also needs the selected server adapter and endpoint runtime.
2. Record the selected build, publish, and runtime commands in its README and adapt `skills/site-bootstrap-adm/assets/release-runbook.template.md` into `docs/release-runbook.md`.
3. Run the target's clean install, content generation, type, lint, format, test, and production-build checks. Test the built output and the actual selected host or adapter. Review mobile, keyboard, form, and error states where they apply.
4. Verify the deployed revision, pages, assets, metadata, redirects, and headers. If the site has endpoints, test valid and rejected requests and confirm the delivery path. Keep provider, CDN, and recovery checks marked pending when no evidence is available.

The checks below validate this toolkit and its bundled examples. They do not launch or deploy the website created from it.

## Plan a new site or app

Use the bundled [Plan Sites & Apps ADM skill](skills/plan-sites-and-apps-adm/SKILL.md) before bootstrap work. It has 88 question topics with website and app branches, an answer ledger, requirement-to-task mapping, phase initiatives, capacity-based cycles, and launch criteria. It selects this website bootstrap or App-Bootstrap-ADM from the product requirements.

After the interview and plan review, it can create an It's a Plan project with a plan document, initiatives, dated cycles, granular tasks, and blocking links. It reconciles interrupted writes and reads the structure back. Unknown dates, capacity, and provider decisions stay visible.

If you are installing the planner separately:

```sh
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/plan-sites-and-apps-adm && \
  cp -R skills/plan-sites-and-apps-adm ~/.agents/skills/
```

> Use $plan-sites-and-apps-adm to interview me about a new website, select the ADM bootstrap, and publish the agreed plan in It's a Plan with initiatives, tasks, and cycles.

The [schedule checker](skills/plan-sites-and-apps-adm/scripts/validate_schedule.py) checks dates, dependency order, and resource capacity. It does not estimate work or prove product readiness. Planning does not execute a production launch.

## Lippincott template example

[The worked example](skills/site-bootstrap-adm/references/lippincott-example.md) maps the inspected Astro/TinaCMS project into a neutral new-site foundation:

- Shared layout, tokens, navigation, and responsive and keyboard checks.
- Selected content collections, CMS schema and client generation, and local build.
- Canonical metadata, sitemap and robots files, optimized media, and URL migration checks.
- Optional contact runtime with bounded input, origin and abuse controls, and truthful delivery.
- Release SHA, selected host and cache, and content and provider recovery evidence.

Real-estate content, Sierra CRM, branding, recipients, tracking IDs, and CDN accounts are selected separately for each project.

## Fast-check

The ordinary test suite should discover real website properties alongside regressions. Define independent content, canonical URL, configuration, and form invariants; cover hostile input, replay shrunk failures, and prove detectable faults. Scoped Stryker guidance covers selected modules.

The bundled synthetic analytics gate demonstrates the harness. Apply the pattern to the target's actual website logic; the demo does not prove target coverage or tracking transport safety.

## Validate this repository

Run these commands from the repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s skills/plan-sites-and-apps-adm/scripts -p 'test_*.py'
python3 skills/plan-sites-and-apps-adm/scripts/validate_schedule.py skills/plan-sites-and-apps-adm/assets/schedule-example.json
cd skills/site-bootstrap-adm/assets/fast-check-example
npm ci --ignore-scripts
npm test
```

The repository's CI workflow uses Python 3 and Node.js `24.19.0`. The prepared website may need different versions, which its own toolchain files should specify.

The demo has a separate lockfile from any website prepared with this workflow. Check official framework and provider compatibility again when you reuse the guidance.

Prepared 2026-10-06. [Source provenance](skills/site-bootstrap-adm/references/sources.md) identifies pinned snapshots. The MIT license covers the original guidance, templates, and demo; source projects retain their own licenses.
