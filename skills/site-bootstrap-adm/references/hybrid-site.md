# Server-enabled content-site setup

Apply after shared and static setup when public content has request-time endpoints. Keep content pages static where useful. Public contact/search/config routes do not imply app accounts, a database or billing.

Contents: [adapter](#h01-server-runtime-and-route-boundaries), [input](#h02-request-validation), [abuse](#h03-origin-and-abuse-controls), [delivery](#h04-contact-and-external-delivery), [preview/config](#h05-preview-search-and-runtime-config), [testing](#h06-hybrid-verification), [readiness](#h07-hybrid-readiness).

## H01 Server runtime and route boundaries

**Files:** selected adapter/framework config, route matrix, server-only config and endpoint modules such as `src/pages/api/contact.ts` in Astro.

1. Select the actual primary host/adapter; verify its supported runtime, streaming/body API, response format and packaging. Do not install all adapters.
2. Mark only request-time routes non-prerendered where the framework requires it. For Astro, confirm adapter + non-prerendered endpoint are packaged in the production output; files-only upload cannot execute it.
3. Separate build-time CMS values from runtime server secrets. Keep contact/email/API credentials server-only.
4. Define routes/methods/access/indexing/cache rules. API/contact/private preview/runtime settings use appropriate no-store policy.
5. Unknown adapter selection fails visibly; it must not quietly select a different hosting target.
6. For portable hosting only when requested, add the compatible Node adapter/start command and D03 container contract.

**Tests:** build/serve selected adapter; POST reaches real handler; static pages/assets still work; wrong method and unknown route fail correctly; secret sentinel absent from public bundle; runtime configuration changes take effect without an assumed rebuild.

**Done:** output can actually serve both content and endpoints. Record tested target/start command; alternate targets stay N/A or pending.

## H02 Request validation

**Files:** contact/input schema, bounded body reader, handler and adjacent deterministic/property tests.

Specify:
- Allowed methods/content types and response format.
- Field types, trimming/normalization, minimum/maximum lengths, allowed values, encoding and email/link validation policy.
- Maximum streamed byte count, file/multipart acceptance policy and maximum field/item count.
- How malformed encoding, duplicate fields, oversized bodies and unexpected keys are handled.
- Which validated fields may leave the service; never forward arbitrary request objects.

Read with an enforced streaming cap where supported; `Content-Length` is untrusted and not the only check. Reject oversized streaming/chunked payloads even when the header is absent/wrong. Validate on the server, independently of browser validation.

**Tests:** minimal/full valid form; blank/whitespace; missing/duplicate/unknown field; malformed encoding/content type; unexpected file; exact size boundary and one over; absent/forged length; invalid email; generated hostile/Unicode values. Assert rejected input creates no lead/email/provider write.

**Done:** actual endpoint responses and observed forbidden effects agree with the schema; no mutation before validation finishes.

## H03 Origin and abuse controls

**Files:** origin/host configuration, trusted-proxy policy, rate limiter/abuse guard and tests.

- Preserve framework CSRF/origin checks. Define exact allowed site origins and an explicit missing-Origin policy suitable for the chosen form/API callers.
- Document CDN/proxy origin Host and forwarded header behavior. Trust client IP only from a documented trusted proxy chain; arbitrary forwarded input is not an identity.
- Add honeypot and bounded rate/size/time controls appropriate to the public endpoint. Define limiter key, window, capacity, expiry, storage and behavior if storage fails.
- In-memory limiting is per process; choose shared enforcement or document the limitation for multi-instance deployments.
- Do not copy Lippincott's global origin-check bypass. Its proxy workaround is project-specific and requires endpoint compensation, not a starter default.
- Keep abuse rejection responses safe and accessible. Avoid logging submitted content or constructing email headers from raw values.

**Tests:** valid origin, lookalike host/subdomain, cross-origin, missing origin according to policy, forged proxy header, burst/window expiry with controlled time, honeypot, limiter failure and rejection with zero delivery.

**Done:** browser form succeeds under the actual proxy contract; hostile callers do not bypass the documented boundary.

## H04 Contact and external delivery

**Files:** server delivery client, contact route, form component/progressive enhancement, success/error state and provider runbook.

1. Select a provider/destination from the brief; keep destinations/credentials configurable without inherited CRM/email addresses.
2. Define transport timeout, status/response schema, accepted-versus-delivered semantics and idempotency strategy for retries/double submissions.
3. Keep server validation/abuse controls before delivery. Escape template content and forbid user-controlled headers/destination.
4. Return honest outcomes: provider acceptance is not necessarily final email delivery; provider rejection/outage cannot produce a thank-you success.
5. Provide loading/disabled-submit and recoverable error states; preserve entered data without logging it.
6. Use isolated sandbox/dry-run credentials initially. A dry-run contract explicitly forbids writes and labels its response; never silently pretend delivery.

**Tests:** accepted lead/email, upstream rejection/non-JSON/timeout, repeated submit, empty configuration, malicious header input, wrong origin, oversized body and no-JS form where supported. Unit mocks test seams; real sandbox delivery confirms actual recipient/provider behavior separately.

**Done:** exact success contract and retry effects verified; real configured delivery remains pending until observed. Default starter does not send to another project's recipient.

## H05 Preview, search and runtime config

Apply each submodule only if requested.

| Module | Setup | Required tests/evidence |
| --- | --- | --- |
| CMS preview/admin | Authentication/access mechanism, draft scope, no-store/noindex, signed/time-bounded preview links if selected | Unauthorized/expired/tampered access refused; drafts inaccessible publicly; cache cannot expose content |
| Search endpoint | Public data projection, validated query, result/response/timeout bounds, approved downstream origin | Empty/hostile/huge queries; no private fields; bounded failure behavior |
| Analytics settings | P01-P03; runtime-only validated opt-in/host/routes; uncached public projection with no credentials | Same artifact responds to runtime change; disabled config has zero collector requests; no DB/session dependency |
| Other public API | Method/input/output/access/cache/error/rate contracts | Positive and hostile requests through real handler |

An analytics runtime endpoint need not add a database. For a files-only site, deployment-owned public runtime JSON can support opt-in without a repository server; verify how it is generated/updated and kept uncached.

## H06 Hybrid verification

Run the normal quality suite, then selected adapter build/start and Playwright/integration requests against it.

Observe:
- Public content pages/SEO/static media still work.
- Each endpoint's valid path, wrong method/type/size/origin, provider outage and no-secret/error response.
- Rejections cause zero delivery/writes; accepted responses match the provider contract.
- API/runtime-config/private preview bypass public cache.
- Server-only variables are absent from browser output; source/commit marker matches intended artifact.
- Mobile/desktop form loading/success/error/keyboard states; duplicate submissions and no-JS fallback.

Use controlled time for rate-limit tests and fresh per-property state. Exercise a deliberate validator/origin/side-effect fault. Mark real provider or CDN behavior pending unless actually observed.

## H07 Hybrid readiness

**Local ready:** shared/static checks plus actual server packaging, handler boundaries, isolated delivery failures and browser paths.

**Integration ready:** actual sandbox CMS/contact/provider behavior, selected proxy/IP/cache contract and no copied recipients.

**Release ready:** expected server/content SHA, secrets injected at runtime, cache bypass, DNS/TLS and truthful delivery/monitoring runbook.

Contact data activates L01's store/retention/deletion inventory for the actual delivery provider, recipient and logs. That does not add accounts, app persistence or backups to this site.

Accounts, tenant data, billing, job infrastructure and database backup routines remain N/A unless requested. For accounts, tenant data, billing or application jobs, use App-Bootstrap-ADM and preserve verified website requirements.
