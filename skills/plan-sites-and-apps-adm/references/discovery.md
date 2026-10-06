# Discovery interview

## Contents

- Interview method and completion
- Common questions
- Website questions
- App questions
- Timeline, operations and destination

## Interview method and completion

Use the questions as a coverage bank, not a script to recite. Ask relevant questions in rounds, one main question per turn by default. Offer choices with a recommendation and trade-off; allow a free-form answer. Use the user's language and explain technical choices through the experience they enable. Ask for a concrete example when an answer such as “modern,” “simple,” “secure” or “like Moderaty” has several possible meanings.

Record each question ID as answered, N/A with a reason, delegated or open. Split multi-part answers into decisions so later changes remain traceable. Carry supplied answers forward. A question tool without an answer is not an answer; address required unresolved facts in the next planning turn. If the user stops the interview, honor it, record assumptions and label the result appropriately.

Resolve launch-critical decisions before a ready plan: purpose/users, primary journey, launch scope, content/design, data/identity boundaries, budget/operating limits, start/target dates and timezone, capacity/cadence, reviewers and intended project/team. An unselected provider may become a decision task blocking integration. Optional improvements may stay deferred. Distinguish a missing choice from missing credentials: ask for requirements and provider names, never secret values in chat or public records.

## Common questions

| ID | Ask and follow up |
|---|---|
| Q01 | What problem should this solve, and what happens today without it? |
| Q02 | Who will use it first? Separate buyers, readers, staff, administrators and partners. |
| Q03 | What is the most important action each primary user should complete? |
| Q04 | Describe a real successful visit/session from arrival to outcome. What would cause failure? |
| Q05 | Which measurable result makes launch successful? Baseline, target, measurement owner and review date? |
| Q06 | New project, replacement, migration or extension? Which code/content/data must survive? |
| Q07 | Which features are required at launch, optional if time permits, and explicitly later? |
| Q08 | Which features, styles, vendors or experiences should be excluded? |
| Q09 | Which references do you like, and precisely which layout, navigation or interaction from each? What do you dislike? |
| Q10 | Which brand assets, colors, typography and tone exist? Who approves changes? |
| Q11 | Which languages, locations, currencies and timezones must launch support? |
| Q12 | Which devices, browsers and assistive technologies matter? Accessibility obligations or target? |
| Q13 | Who supplies/approves copy, images, video and licensed assets? What is ready now? |
| Q14 | Build budget and monthly operating ceiling? Paid-service prohibitions or procurement delays? |
| Q15 | Portability, self-hosting, open source and future handoff requirements? Existing stack or hosting? |
| Q16 | Contractual policies, retention limits or client approvals? Obtain sources instead of inventing compliance. |

## Website questions

Use these for public content, marketing, portfolios and contact/CMS websites. An interactive page alone does not require accounts or a database.

| ID | Ask and follow up |
|---|---|
| S-Q01 | Every launch page and its visitor/action? Which navigation items are primary? |
| S-Q02 | Which services/products/locations need separate pages? Required information on each? |
| S-Q03 | Single page or distinct URLs for search, sharing and navigation? |
| S-Q04 | Who edits after launch, how often, from what device, with what technical ability? |
| S-Q05 | Need a CMS, drafts, preview, approvals or scheduling? Which are required now? |
| S-Q06 | Blog, case study, FAQ, team, testimonial or listing collections? Required fields, relationships and ordering? |
| S-Q07 | Repeated layouts/components? Reference page specifying intended structure? |
| S-Q08 | Header, navigation, footer and calls to action? Mobile menu behavior? |
| S-Q09 | Original photos/video? Cropping, alt text, captions, attribution, weight and reduced-motion preference? |
| S-Q10 | Search audiences, queries, geographies and conversions? Existing research or ranking pages? |
| S-Q11 | Title/canonical/social-image rules and structured data justified by actual content? |
| S-Q12 | Replacing a domain/site? URL inventory, redirects, canonical domain and migration owner? |
| S-Q13 | Draft, search, preview or private pages to exclude from sitemap/indexing? |
| S-Q14 | Necessary form fields? Optional, sensitive, repeated or conditional inputs? |
| S-Q15 | Submission destinations: mailbox, CRM, queue or several? Which delivery is mandatory for success? |
| S-Q16 | User response after delivery, invalid input, outage or abuse? Expected reply time? |
| S-Q17 | Follow-up owner, consent wording, retention/deletion and notification preferences? |
| S-Q18 | Upload, booking or payment truly needed? Does it introduce persistent application workflows? |
| S-Q19 | Runtime search, preview or third-party widgets? External-data freshness and outage behavior? |
| S-Q20 | Analytics/conversions wanted? Exact production hosts, opt-out/consent and data exclusions? |
| S-Q21 | Performance targets on representative devices/networks? Animation versus load cost? |
| S-Q22 | Project-owned domain, DNS, email, CMS and hosting accounts? Configuration owner for each? |
| S-Q23 | Files-only host sufficient, or must it run contact/preview endpoints? |
| S-Q24 | Launch acceptance: content, links, search metadata, accessibility, form receipt and rollback? |

## App questions

Use these for durable workflows, accounts, permissioned data, portals and SaaS. Activate identity, storage, payments, jobs and uploads only when needed. A browser-only utility can be an app without accounts/database.

| ID | Ask and follow up |
|---|---|
| A-Q01 | User roles and operations each can/cannot perform? |
| A-Q02 | Main workflow step by step: input, state transitions, result and follow-up? |
| A-Q03 | First usable slice and explicit launch completion criteria? |
| A-Q04 | Invalid input, duplicates, partial saves, concurrent editing and interruptions? |
| A-Q05 | Accounts needed? Creation, verification, invitation, recovery and removal? |
| A-Q06 | Sign-in methods, session duration, logout/revocation, multi-device and privileged access? |
| A-Q07 | Organizations/tenants needed? Membership roles, ownership transfer and invitations? |
| A-Q08 | Owner of each entity? Sharing/public links, revocation and expiration? |
| A-Q09 | Persistent entities/fields/relationships? Unique constraints, units, valid states and history? |
| A-Q10 | Private/sensitive data? Access, export, deletion and retention rules? |
| A-Q11 | Existing-data import? Source format, validation, deduplication, rollback and audit? |
| A-Q12 | Anonymous/offline use? Sync conflicts and unsaved work? |
| A-Q13 | Subscriptions, one-time payments or free limits? Currency, prices, entitlements, trial and cancellation? |
| A-Q14 | Authoritative payment status? Retries, refunds, disputes, late events and outage behavior? |
| A-Q15 | Exceeded limits or entitlement changes during an operation? |
| A-Q16 | Transactional versus optional notifications? Triggers, recipients, unsubscribe and failures? |
| A-Q17 | Required APIs/OAuth providers? Scopes, tokens/revocation, rate limits, costs and sandboxes? |
| A-Q18 | User-supplied API keys? Storage, disclosure and revocation rules? |
| A-Q19 | AI/model features? External inputs, evaluation, usage limits, latency, costs and failures? |
| A-Q20 | Background/scheduled operations? Timezone, bounds, retries, idempotency and catch-up? |
| A-Q21 | Missed jobs or failed alerts: detector, owner and response? |
| A-Q22 | Upload types/sizes, storage ownership, access URLs, scanning and deletion? |
| A-Q23 | Search/filter/sort/pagination? Empty or permission-filtered results? |
| A-Q24 | Screens and states: loading, empty, success, validation, maintenance, expired session, forbidden? |
| A-Q25 | Keyboard, screen reader, mobile or large-data interaction requirements? |
| A-Q26 | Users, concurrency and data volume now/later? Latency/availability targets? |
| A-Q27 | Public health disclosure and private readiness checks? |
| A-Q28 | Browser-test journeys and property-test business invariants? |
| A-Q29 | Acceptable recovery loss/window? Backup owner and isolated restore evidence? |
| A-Q30 | Public marketing/help/legal pages? Indexing and analytics exclusions? |
| A-Q31 | Administrator/support visibility? Actions needing audit history or confirmation? |
| A-Q32 | Selected storage/auth/payment/email/job/host services available? Missing accounts/access/decisions? |

## Timeline, operations and destination

| ID | Ask and follow up |
|---|---|
| O-Q01 | Exact start date and timezone? Interpret relative dates in the user's timezone. |
| O-Q02 | Exact launch date? Fixed by event/contract or flexible? |
| O-Q03 | Implementers, writers, reviewers and operators? Actual names versus role placeholders? |
| O-Q04 | Each person's weekly hours and working days? Leave, holidays and other commitments? |
| O-Q05 | Work-session size and one-week/two-week/custom cycle preference? |
| O-Q06 | Review turnaround, final acceptance owner and backup? |
| O-Q07 | Lead times for domain/DNS, provider approval, legal copy, integration or import? |
| O-Q08 | Contingency for uncertainty and launch fixes? A suggested percentage remains a proposal until accepted. |
| O-Q09 | Infeasible deadline: reduce scope, add capacity or move date? Which outcomes must survive? |
| O-Q10 | Target repository name/visibility/license, branch policy, CI and release permissions? |
| O-Q11 | Intended It's a Plan team, new project name/key and naming conventions? |
| O-Q12 | Initiative/task owners and reviewers? Resolve actual member IDs. |
| O-Q13 | Plan document shared within project or private? Client/confidential details to omit? |
| O-Q14 | Preview/sandbox/production environments, configuration owners and authorization? |
| O-Q15 | Launch checklist, rollback trigger, observation window and support owner? |
| O-Q16 | Feedback and scope-change review/reprioritization after launch? |

There are 88 question topics before follow-ups. Resolve applicable coverage; question quantity alone is not completion.
