# Static content-site setup

Apply to public pages, including the public portion of a hybrid site or app. A files-only host has no request-time server, secret store or database. A build-time Git-backed CMS can remain static.

Contents: [output](#s01-output-and-site-origin), [UI](#s02-layout-navigation-and-accessibility), [content](#s03-content-contracts), [CMS](#s04-cms-and-generation), [media](#s05-images-fonts-and-assets), [SEO](#s06-search-and-sharing), [URLs](#s07-url-migration-and-errors), [testing](#s08-static-verification), [handoff](#s09-static-readiness).

## S01 Output and site origin

**Files:** `astro.config.mjs` or existing framework config; `src/lib/config/site.ts`; route matrix; production-origin configuration.

- For a files-only Astro target set static output and add no server adapter solely for future possibilities. For an existing hybrid site preserve needed adapter/non-prerendered routes and apply H01-H07.
- Configure one validated production canonical origin: scheme, exact host, no credentials, path/query/fragment policy. Local origin is for local serving; preview indexing/canonical behavior must be explicit.
- Determine trailing-slash and base-path policy using the selected host; use it consistently in URLs, internal links and redirects.
- Record build output directory and asset paths. No server-only env lookup may be required after deployment.
- Keep JS proportional to actual interaction. A menu/form enhancement needs specific hydration, not global application state by default.

**Commands:** selected clean install → content generation if applicable → `npm run check` → `npm run build` → `npm run preview`.

**Tests:** served output includes the landing page/assets/404; canonical origin cannot be a copied domain or an invalid production value; assets resolve with the selected base path; no request-time endpoint assumed available.

**Done:** inspect actual output and served routes. Document deploy directory, origin/base-path and adapter decision.

## S02 Layout, navigation and accessibility

**Files:** shared layout, header/footer/nav, `src/styles/tokens.css` or existing tokens, accessible interactive components, public error page.

1. Define semantic landmarks, single primary page heading, title/description slots and a skip link to main content.
2. Define color/spacing/type/container tokens, narrow/wide layout rules, visible focus and reduced-motion behavior.
3. Implement mobile navigation with keyboard operation, accurate expanded state, focus management and meaningful link labels.
4. Render core content/links without browser JS; enhance only real interactive requirements. A no-JS contact form must still work if its delivery route is selected.
5. Provide meaningful empty/error states. Set document language; add localization infrastructure only for actual languages with real translated content.
6. Keep header/footer/CTA data centralized in content/config, without inherited phone, email, brand or domain.

**Tests:** narrow/desktop layouts; keyboard tab/activate/escape where applicable; menu opening/closing; visible focus; content/links with JS disabled; long titles/copy; reduced motion. Include automated accessibility checks where available and manual keyboard/contrast review.

**Done:** mobile/desktop screenshots of actual templates plus recorded interaction results. A screenshot alone does not prove functional navigation.

## S03 Content contracts

**Files:** content collection schema in the selected framework, `src/lib/content/` adapters, representative synthetic content fixtures and validation tests.

Specify each selected collection, not a universal mega-schema:
- Page: stable slug, title, description, draft/publish state and supported body.
- Blog, if requested: author, publish/update dates, taxonomy, hero media, excerpt and canonical override policy.
- Claims/local data, if used: original source URL, checked date, geographic/metric scope and reporting period.
- Links/CTA: accepted URL schemes, internal/external classification and approved contact destinations.
- Media: source/reference, alt decision, dimensions or resolvable image metadata, attribution when required.

Reject duplicate slugs, invalid dates/URLs/references, missing required fields and visually empty rich text. Schema markup must come from visible supported content. Draft/preview material must not enter public output, sitemap or feeds.

**Tests:** valid minimal/full fixtures; empty/whitespace/empty rich-text blocks; duplicate slugs; unsupported link schemes; invalid/future date policy; missing media; draft exclusion; externally absent/null values. Properties target actual validation or URL/content transforms, with independently specified expected behavior.

**Done:** malformed content fails usefully before publication; one source of truth drives rendered pages/metadata/feeds.

## S04 CMS and generation

**Conditional:** N/A when authoring does not use a CMS.

**Files:** e.g. `tina/config.ts`, selected content paths such as `src/content/`, generation/check scripts, expected schema-lock/generated artifacts, editor route/build settings only if requested.

1. Define collections/fields matching S03. Record which paths the CMS edits and how editor routes remain preview/admin scoped.
2. Establish schema/client generation before framework dev/build. Record exactly which generated files are committed versus ignored according to the selected version.
3. Provide a local content/generation/build path without cloud credentials. Cloud-backed editing is a separate integration gate.
4. Pin the CMS version and verify its actual CLI flags/lock-generation behavior. Lippincott's Tina pipeline wraps Astro with Tina generation and has separate local/cloud builds; verify commands before adapting.
5. For Tina, inspect generated schema for invalid serialized leaf UI metadata after field-function changes; regenerate the schema lock and run an adapted schema consistency check when applicable. Never hand-edit generated artifacts to conceal a source-schema problem.
6. Trigger regeneration when content or schema changes. Document why bare framework dev/build may serve stale CMS-generated data.
7. Verify who can edit/publish, preview URLs, branch selection and credential handling using isolated non-production configuration.

**Scripts to establish:** `dev` with local CMS wrapper where needed; `content:generate` if generation is separable; `content:check`; `build:local` without cloud checks; production `build` with its actual cloud prerequisites.

**Tests:** clean generation; edit a fixture and see new content in built HTML; schema/lock consistency; malformed fields; draft exclusion; local build with cloud secrets unset. Cloud editor authentication/publish flow needs actual sandbox evidence.

**Done:** exact working pipeline/committed artifacts documented. Cloud CMS integration stays pending until exercised, even if local generated types compile.

## S05 Images, fonts and assets

**Files:** framework image components/pipeline, local public/media directories, font CSS and asset provenance.

- Choose local/framework-processed assets by default when suitable; explicitly allow remote image origins only when needed.
- Set dimensions/aspect ratios, responsive sizes, useful formats and loading priority for actual above-the-fold media. Do not lazy-load the principal image blindly.
- Decorative images use empty alt; informative images use meaningful content-specific alt. Do not enforce a nonempty alt value on decorative media.
- Keep source licensing/provenance, optimized output and favicon/social image paths consistent. Remove sample assets and copied brand identifiers.
- Use locally hosted licensed fonts where appropriate; don't add an external font request by accident.
- Test broken/missing remote media and long captions, not only happy-path placeholder assets.

**Evidence:** built asset references resolve; no layout shifts from omitted media space; screenshots at narrow/wide widths; representative image payload size recorded. Set performance budgets appropriate to content rather than copying project-specific thresholds.

## S06 Search and sharing

**Files:** shared SEO component/helper, sitemap/robots generation, social preview assets; RSS/schema helpers only when content calls for them.

For every indexable public page:
1. Render unique meaningful title/description, one normalized canonical URL and correct document language.
2. Render social title/description/image with absolute valid URLs and accessible image metadata where supported.
3. Build sitemap from public canonical URLs, excluding drafts, admin, preview, search/private variants and duplicate variants.
4. Configure robots intentionally per environment. Robots directives are crawl guidance, never access control.
5. Use `noindex` headers/meta for selected private/admin/preview surfaces; do not block crawling merely to hide a noindex header that must be observed.
6. For a blog, generate RSS from published entries with valid dates/canonical links.
7. Generate only applicable structured data from visible supported facts. No invented ratings, claims or local figures.
8. Remove arbitrary query strings/fragments from canonical URLs; choose a reviewed exception policy for legitimate canonical parameters.

**Tests:** assertions over built HTML, sitemap/feed and HTTP headers where supported; duplicates; draft/private leakage; malformed origin; slug encoding; trailing slash/base path; canonical consistency. Check social images actually return successfully.

**Done:** known public route inventory matches output metadata/sitemap; environment indexing policy is explicit.

## S07 URL migration and errors

**Conditional:** redirect map required for an actual migration; otherwise record N/A.

**Files:** old-URL inventory, canonical redirect map in host/framework configuration, 404 page and redirect tests.

- Map a retired URL permanently only to a genuine equivalent. Choose intentional 404/410 when no equivalent exists.
- Avoid chains, loops, open redirects and blanket redirects to the homepage.
- Preserve only reviewed query semantics; never forward credentials or arbitrary personal data.
- Remove obsolete URLs from internal links/sitemap.
- Verify redirect status/location and 404/410 behavior against the selected served target, since a generic dev server may not apply host redirects.

**Tests:** every mapping, no-equivalent URL, loop/chain prevention, unknown URL, query handling, encoded paths and base-path variants.

**Done:** observed served statuses/locations agree with the inventory; missing pages do not return a misleading successful homepage.

## S08 Static verification

**Files:** deterministic/properties for real URL/content helpers; built-output inspection script; Playwright config and UI smoke tests.

Run check/lint/format/test → local CMS generation where needed → build → serve built output → browser/output tests. Avoid testing only a dev server while claiming production output verified.

Minimum assertions:
- Representative page of each template renders with actual content/metadata.
- All intended internal links/media references resolve; drafts/admin do not leak.
- Navigation/menu/CTA work at narrow and desktop widths; JS-disabled essential paths work.
- Sitemap/robots/feed and 404/redirect behavior match the route matrix.
- No inherited identifiers, secrets or enabled tracker in generated HTML/JS.
- fast-check discovers meaningful canonical/content/config properties, with regressions and fault evidence.

Choose representative viewport dimensions and document them; add edge widths/long content. Measure a selected performance budget once there is realistic content. A high Lighthouse score is not functional/security evidence.

## S09 Static readiness

**Local ready:** clean local generation/build, meaningful tests, actual built-output and browser verification, truthful handling of absent integrations.

**Static release ready:** selected host serves expected files/statuses/headers and release SHA; DNS/TLS/indexing/canonical/redirect settings verified; any requested CMS provider flow verified.

**N/A by default:** sessions, database migrations/backups, entitlements, queues, application health endpoints and server secrets.

If adding contact, request-time preview, a private API key or runtime config served by this repository, first apply hybrid setup. An external hosted form can preserve files-only hosting, but its provider, privacy, success/failure and origin behavior are still integration tasks.
