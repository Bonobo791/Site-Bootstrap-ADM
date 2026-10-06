# Website personal-data lifecycle

## L01 Contact, CMS and provider data

Apply when contact submissions, newsletter/provider integrations, editor identities or logs contain personal data. Files-only delivery can still collect data through external services.

**Files:** `docs/data-lifecycle.md`, matching privacy/contact copy, selected provider configuration and deletion/retention procedures.

Record every actual store: delivery provider, recipient/mailbox/CRM, CMS account/content, logs and optional analytics. For each record fields, purpose, access, retention trigger/duration, deletion mechanism, owner and evidence.

- Transmit only validated selected fields to the approved recipient/provider.
- Keep submitted text/email/tokens out of diagnostic logs and marketing events.
- State whether the response means accepted or delivered and what happens after provider failure.
- Provide the product's actual retention/deletion process. Provider retention/backups require observed/documented capability; live deletion is not proof of immediate backup erasure.
- Match notices to the actual integration and scope. Do not copy legal jurisdictions/retention periods.
- Use isolated synthetic submissions when verifying provider delivery/deletion.

**Tests/evidence:** rejected input sends nothing; safe logs; approved recipient sees the intended synthetic submission; selected deletion/retention procedure works; notices and provider settings agree. Unavailable provider evidence stays pending.

This inventory does not require sessions, a local database, export APIs, queue workers or database backup infrastructure.
