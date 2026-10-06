# Privacy and operations

Read when analytics, personal data or external operations apply. Deployment details use D01-D08; website data lifecycle uses L01. These are derived product safeguards, not copied legal conclusions.

Contents: [off by default](#p01-default-off-and-capability-scope), [runtime config](#p02-runtime-configuration-and-exact-hosts), [eligibility/data](#p03-eligibility-payload-and-preferences), [activation tests](#p04-analytics-verification), [data operation](#p05-personal-data-and-operation-evidence).

## P01 Default-off and capability scope

**Files:** environment registry, explicit analytics flag, route/event registry and client initializer only if measurement is requested.

- Fresh clone, fork, local and preview send zero tracking requests. Never activate from a website ID alone or use another project's ID as fallback.
- No requested measurement means no collector/script/event integration; still inspect output for inherited tracking.
- Prefer optional self-hosted Umami for requested marketing measurement, preserving agreed scope. Advertising conversion integrations are separate explicit features.
- Register intended public routes/events. A signup/checkout click is intent, not verified signup/payment.
- No session replay, broad autocapture, account IDs, emails, text, private-path or token collection in the default marketing pattern.
- Consent/preferences/notices must match the selected product and deployment; do not copy another project's jurisdiction, retention or notice timing.

**Done:** explicit off defaults and zero-request evidence, or a fully configured requested opt-in with remaining activation checks recorded.

## P02 Runtime configuration and exact hosts

**Files:** server-only validated settings; uncached public projection such as `/api/analytics`; client eligibility helper. For files-only hosts, actual deployment-owned runtime JSON/config delivery instead.

Required deployment-owned values:
- Explicit enable flag parsed according to a documented literal policy.
- Approved collector origin and website ID, no inherited fallback.
- Exact hostname allowlist including intentional aliases.
- Reviewed public route/event registry, allowed UTM values and applicable preference policy.

Validate enabled config. Public settings exclude credentials; endpoint should not require session/DB to answer. Set no-store/cache bypass. Treat unavailable config as ineligible, with safe visible diagnostics.

Independently check actual browser hostname. Suffix matching, hostname substrings and an ID alone are insufficient. This prevents accidental fork activation; public IDs/host gates are not protection against adversarial collector spoofing.

Keep activation values runtime-only, absent from built HTML/JS substitution. A static artifact has no private runtime env: document who produces runtime JSON, how values change, and how stale config is prevented.

**Tests:** same artifact toggled at runtime, invalid enabled settings, exact aliases, lookalike suffix/subdomain, local/preview/fork and missing endpoint; public projection and logs contain no private credentials.

## P03 Eligibility, payload and preferences

**Files:** pure eligibility/payload sanitizer, bounded transport, opt-out/preference helper and tests.

Define the state machine and data contract:
1. Config valid + enabled; current exact host allowed.
2. Current route explicitly public. Account/admin/OAuth/invite/reset and other private routes are ineligible.
3. Parse URL/query, including encoding/duplicate keys. Sensitive auth/contact keys deny collection under the selected policy, even when empty. Do not inspect only an unparsed string.
4. Rebuild payload URL from approved path and query registry. Remove fragments, click IDs and arbitrary query values. Review duplicate/unknown UTM behavior.
5. Referrer is absent or approved origin-only; never raw full referrer.
6. DNT/GPC and selected opt-out/consent policy gate dispatch. Private navigation/opt-out cancels pending work; a late settings reply cannot reactivate collection.
7. Event names/properties come from a static approved allowlist; no user-supplied text/IDs.
8. Transport sends only the reviewed payload, with no credential/cookie leakage. Verify collector API, CORS/CSP and browser referrer/credentials behavior.
9. Retry only under a tested deduplication contract; don't duplicate accepted events blindly.

Prefer explicit limited collection transport without a third-party tracker script when compatible with the agreed design. Don't assume Umami's script defaults implement this full policy.

**Properties:** hostile encoded queries, unregistered/private paths, config host variants, cancellation sequences and arbitrary payload inputs cannot leak forbidden data or create ineligible requests. Oracle comes from the registry/specification, not the sanitizer calling itself.

## P04 Analytics verification

**Evidence required before activation:**
- Inspect actual permitted network payload/header/referrer, collector acceptance and dashboard result using synthetic events.
- Zero collector requests for disabled/local/preview/fork/wrong-host/private/sensitive-query/opt-out/preference cases.
- Public → private navigation and delayed config response cannot revive collection.
- Runtime switch on the same artifact; no hard-coded activation values in distributed assets.
- Approved events/UTM values only; duplicate/out-of-registry values excluded according to policy.
- Collection storage/retention/deletion and notices agree with actual chosen provider setup.
- Errors are safe and do not retry into duplicates or log credentials/data.

Use real browser network observations in addition to pure helper tests. A green gate helper alone does not prove transport/payload safety. Activation remains pending when collector/provider/notices are unverified.

## P05 Personal data and operation evidence

For selected CMS/contact/integrations, register actual stores, access, retention/deletion and notices under L01. Contact/email data is personal data even if the site has no accounts/database.

For selected jobs/hosting/recovery:
- Use isolated development resources; dry-run has a tested write contract.
- Report partial/incomplete work honestly; preserve checkpoints/leases and bounded retry.
- Completed ticks and actual missed-tick alert delivery are separate from health.
- Provider-supported backups/PITR need an isolated restore; CI and a backup checkbox prove no recovery.
- CDN/proxy/CSRF work follows the actual selected host, never a copied bypass.

Continue independent development without production credentials. Record exact operator tasks/evidence when provider or production access is outside scope. No invented deployment, delivery, legal compliance or recovery success.
