# Lippincott website template example

Inspected source: `Bonobo791/the-lippincott-team` at `92bfa5ad5d876730c09198d7b3d9c63923715b24`, 2026-10-06. Adapt these patterns to a new website with neutral identity and synthetic content.

## Source-to-template mapping

| Lippincott source | Set up in a new website | Requirement / proof |
| --- | --- | --- |
| `astro.config.mjs` | Astro output, canonical site URL, only selected adapter; files-only baseline until an endpoint is needed | S01/H01: build and serve correct artifact |
| `src/layouts/Base.astro` | Shared semantic layout, skip link, header/footer, document metadata, responsive tokens | S02/S06: built metadata, keyboard/mobile/desktop checks |
| `src/content/` + `tina/config.ts` | Minimal selected collections, draft/content validation, CMS schema/client generation | S03/S04: source edit reaches rebuilt HTML |
| `scripts/check-tina-schema.mjs` | Version-aware generated schema check when Tina uses serialized field UI metadata | S04: lock/schema consistent, useful failure |
| `src/pages/api/contact.ts` | Neutral contact schema, streamed body cap, exact origin/proxy contract, abuse control and bounded delivery | H02-H04: rejected input has zero delivery |
| `scripts/deploy/write-commit-marker.mjs` | Safe release SHA marker | D04: served identity matches expected artifact |
| Metadata/redirect/media checks | Public canonical/sitemap/404/redirect and optimized asset validation | S05-S08: assertions on built served output |

## Recorded source commands

Lippincott pins Astro `7.2.8`, pnpm `10.34.5` and Node `>=22.22.0`. These identify the inspected snapshot; verify supported versions before starting a later target.

Source scripts:

```sh
pnpm install --frozen-lockfile
pnpm dev
pnpm build:local
pnpm test
pnpm preview
```

`dev` wraps Astro with `tinacms dev`. `build:local` writes the marker and uses `tinacms build --local --skip-cloud-checks` before Astro's production build. Source production `build` uses `--content=local` with its actual cloud requirements. Do not invent a separate Tina CLI generation flag; inspect the pinned version.

The new website must also install real framework type, lint and format scripts under C03. They are required enhancements; the source package does not prove those script names already exist.

## Neutral example project contract

Prepare:
- `astro.config.mjs`, strict `tsconfig.json`, selected scripts and one lockfile.
- `src/layouts/Base.astro`; neutral header/footer/tokens; accessible 404.
- `src/content/` selected collections and `tina/config.ts` only if CMS is selected.
- Shared SEO helper, sitemap/robots and synthetic page/media fixtures.
- Unit/property/built-output/browser tests.
- `docs/bootstrap.md`, task/route/env records and selected release runbook.
- Contact server files/config only after the delivery target/adapter is selected.

Start with landing/about/contact content or the actual brief's pages. Choose titles, images, destinations and canonical origin for the new project. Real-estate listings, Sierra CRM, phone/email, client branding, Bunny CDN and every adapter are conditional source features.

## Minimal verification scenario

1. Unset cloud/tracking/provider secrets; clean local generation/build still works for selected local content.
2. Edit title/body in synthetic content; rebuilt HTML changes and draft remains excluded.
3. Inspect canonical/sitemap/social image and unknown URL behavior.
4. Verify menu/links/keyboard/narrow/desktop output.
5. If contact is selected, serve the built adapter; valid sandbox delivery succeeds honestly; malformed/oversized/cross-origin input sends nothing.
6. Record missing cloud editor, actual recipient, DNS/CDN/release checks as pending.

Do not copy the source's global origin-check workaround. Preserve framework checks and implement compensation only for an observed trusted-proxy requirement.
