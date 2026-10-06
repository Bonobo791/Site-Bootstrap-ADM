# It's a Plan publication

## Contents

- Capabilities and current constraints
- Preflight and project creation
- Ordered publication
- Retry and readback

## Capabilities and current constraints

Discover the installed It's a Plan MCP tools and read their current declarations before calls. The 2026-10-06 interface supports native projects, initiatives, cycles, documents, issues, subtasks and directional issue links. Responses expose `structuredContent.ok/status/data` or `error`; inspect both tool errors and envelope errors. Current project descriptions have a 2000-character limit. Put the full plan in a document, not the project description.

| Tool suffix | Contract to preserve |
|---|---|
| `list_teams`, `list_projects` | Inspect actual team/project access, naming collisions and existing plan markers. |
| `create_project` | `name`, unique `key`, concise `description`, `preset`; key is uppercase letter followed by letters/digits, at most 10 chars. Current schema has no `teamId`. |
| `copy_project` | Creates a new project from a selected source team's configuration; use only when appropriate and authorized. Explicitly select safe configuration sections. |
| `get_project` | Use returned `project.ref` as `projectKey`; resolve columns, types, labels, members, flags and permissions here. |
| `create_document` | `projectKey`, Markdown `content`, `title`, optional visibility and metadata. Save full plan plus stable plan ID/version. |
| `create_initiative` | `projectKey`, `title`, `description`, optional owner/priority/start/target, `status: planned`. |
| `create_cycle` | `projectKey`, `name`, `goal`, `startDate`, `endDate`; cycle dates cannot overlap. |
| `create_issue` | `projectKey`, actual `columnId`; description/title; optional `initiativeId`, `cycleId`, owner, type, estimate, start/due, labels, parent. |
| `link_issues` | Actual internal numeric `issueId`, `targetIssueId`, directional `kind`. |
| `get_issue` and list tools | Verify descriptions, native membership, dates, estimates and links. |

Schemas may change. Do not add imaginary `teamId`, project due date, initiative parent or feature-toggle fields. Current project update does not enable features; if required native features are unavailable, report the specific configuration/access blocker. Do not replace requested cycles with labels and then claim completion.

## Preflight and project creation

1. Use existing authorization: invoking this workflow to publish the ready plan authorizes the corresponding project, document, initiatives, cycles, tasks and dependency links. It does not authorize inviting people, sending messages, spawning platform agents, cron schedules, changing unrelated boards or deploying production.
2. Resolve intended team, name/key, owner visibility and actual start/cadence. Inspect `list_teams` and `list_projects`, including permissions when useful. Find matching key/name/plan marker before creation. A new product needs a new project, not a phase initiative appended to Moderaty Dev or another unrelated board.
3. Create a stable `plan-id` for this product/version before the first write. Put it in the concise project description and document metadata. Record every returned ID immediately in a persistent ID map with the plan. Choose a key once; current valid keys are immutable. Never reuse a conflicting project just because its name is similar.
4. Current `create_project` uses the connection's active team, not an arbitrary `teamId`. Verify binding from supported connection information. If intended team cannot be addressed, resolve that destination before creating. `list_teams` shows memberships, not proof of an active-team switch. An authorized configuration-only copy from an existing project of the correct team can be a supported alternative. Inspect its schema; exclude agents, schedules, webhooks, actions and old documents unless explicitly requested. Avoid copying source policies/labels that do not fit.
5. After creation inspect returned team/ref and `get_project`. If the team differs, stop population and report the exact mismatch; do not silently proceed or delete the project. Resolve correction with supported capabilities. Always use the returned qualified ref such as `<teamRef>.<key>`, not a bare key when multiple teams could collide.
6. Verify required `availableFeatures`, enabled flags and create/read permissions for initiatives, cycles, documents and work items. Resolve columns by `stateType`, issue type by returned types, and users by returned assignable members. Do not hardcode today's IDs. Respect auto-assignment/WIP policies. Only use native estimate fields when enabled; preserve effort estimates in task descriptions and the plan when not enabled.

## Ordered publication

1. Save the full plan document with stable ID/version, selected bootstrap and inspected revision, scope/requirements, answer/decision summary, task/cycle tables, capacity, launch criteria and blockers. Choose project-shared or private visibility from the brief; project-shared does not mean internet-public. Never include credentials or unnecessary personal data.
2. Create phase initiatives with outcome/entry/exit criteria and dates. Record local `I01` → numeric ID. Optionally link the plan document to initiatives when supported/appropriate.
3. Read existing cycles, then create the agreed native cycles with exact non-overlapping dates, goals and capacity/contingency in goal text. Record local `CY01` → numeric ID. Do not use `create_agent_schedule`: cycles are project timeboxes.
4. Create tasks, parents before children if used, in the appropriate returned backlog/unstarted state. Assign real member IDs only when agreed. Carry the complete task record in description, including `[plan-id / T001]` marker, acceptance checks, dependency local IDs and estimates. Set native initiative/cycle/start/due fields for committed work; omit cycle/dates for later/unresolved work. Parent work must not duplicate leaf estimates.
5. Map dependencies after all task IDs exist. If T001 must finish before T002, call `link_issues({issueId: <T001 numeric>, targetIssueId: <T002 numeric>, kind: 'blocks'})`. One directional edge is sufficient; do not add both reciprocals. Use `parentId` for hierarchy, never as a substitute for a blocking link.
6. Update the document/publication ledger with returned refs/IDs and verify results. Re-read before updates; supported update tools replace some lists such as labels, so preserve unrelated values. No task becomes completed merely by writing its plan.

## Retry and readback

Publishing is not atomic. After an error/timeout, list and inspect existing records by stable plan marker/local ID before retrying. A call may have succeeded despite a timeout. Reconcile data, record successful operations and create only missing items; do not blindly rerun the whole batch. Keep dependent mutations sequential; bounded independent reads can run in parallel. Honor retryability/rate limits and do not retry deterministic permission/validation failures unchanged.

Initiatives are paged (current maximum page size 100); read every page. `list_issues` is limited (current maximum 500) and has no cursor in the current schema. For larger plans enumerate per initiative/cycle/parent and de-duplicate IDs, then compare against the manifest. Fetch each relevant `get_issue` to verify full descriptions/links and any truncated data. Use `list_cycles` and `list_documents` plus document readback.

Verify team/ref, plan marker/version/content, expected initiative/task/cycle counts, all task memberships/owners/dates, non-overlap/capacity, dependency direction, acceptance evidence text and backlog separation. Return actual created IDs/links and precise remaining items on partial failure. Preserve the ready plan and ID map durably; use an existing git-backed project or the host's persistent file store. Prefer URLs returned by the service or verified deployment metadata. Never invent a project URL from an assumed hostname/route.

If the connector is unavailable, preserve a publication-ready plan, report the missing capability and follow the host's authorized plugin connection workflow. Do not claim a project exists. Browser fallback follows host policy and requires approval if a sufficient plugin is unavailable/repeatedly fails; a skill is not permission to probe sessions or handle credentials.
