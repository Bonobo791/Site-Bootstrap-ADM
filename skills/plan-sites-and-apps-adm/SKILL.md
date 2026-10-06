---
name: plan-sites-and-apps-adm
description: Use when planning a new website, app, portal or SaaS, interviewing a user about product requirements, preparing a launch roadmap, or organizing a new site/app project in It's a Plan. Also use when refining an incomplete brief into phases, tasks and scheduled cycles before building.
---

# Plan Sites & Apps ADM

Interview the user, resolve the launch scope and publish an executable plan in It's a Plan. Use the selected ADM bootstrap as the foundation. Give planning, implementation, provider integration and production launch separate completion evidence.

## Interview and decisions

1. Read the supplied brief, prior answers, target instructions and relevant existing work. Preserve decisions and existing authorization. Start with a short account of the intended outcome and the most important unanswered question. Create the [answer ledger](assets/answer-ledger.template.md); record answers as confirmed, proposed, open or deferred, with their source and planning impact.
2. Read [the discovery guide](references/discovery.md). Ask many specific questions across successive rounds, one main question at a time. Use up to three closely related questions when the user prefers batches. Use an available question tool for helpful optional choices and plain chat for required missing facts. Continue read-only research while waiting. Skip answered questions, branch on actual needs and revisit contradictions. Accept “I don't know” by explaining choices or creating a bounded decision/research task.
3. Establish outcome, audience, launch functionality, content/design, accessibility, budget, data/integrations, operating constraints, deadline, timezone, real capacity and project destination. Use the website or app question bank. Explore concrete journeys, exception paths and exclusions. Summarize each topic before moving on. Follow up until the user can recognize the planned experience.
4. Use [bootstrap selection](references/bootstrap-mapping.md). Read the selected `$site-bootstrap-adm` or `$app-bootstrap-adm` skill and its references in planning mode. Record the repository and inspected commit. These repositories contain skills/templates and a test demo, not a finished deployable product. Plan the actual target scaffold, neutralization, setup and release work. Preserve an existing stack; verify current official compatibility before recommending versions/providers.

## Plan and schedule

5. Use [the planning contract](references/plan-contract.md) and [plan template](assets/project-plan.template.md). Define numbered requirements, observable acceptance criteria, scope exclusions, journeys, page/route and data boundaries, design/content contracts, decisions, provider choices and blockers. Compare approaches for consequential decisions with several viable answers. Keep secrets and private data out of public artifacts and project descriptions.
6. Map each selected bootstrap requirement ID to tasks, or record N/A with a reason. Use the [task template](assets/task.template.md) to expand setup and feature work into work sessions with exact deliverables, files/configuration, commands or named research outcomes, positive/negative checks, forbidden effects, evidence and dependencies. Include fast-check against actual product logic, unit/integration/browser checks, provider sandbox checks and launch/recovery tasks. The bundled demo is not product coverage.
7. Represent phases as ordered initiatives with measurable outcomes and exit criteria. Use [cycles and capacity](references/scheduling.md) to schedule tasks across dated native cycles. Initiatives describe outcomes; cycles describe time commitments and may contain work from multiple initiatives. Account for each person's availability, reviews, provider lead time and contingency. Resolve deadline/capacity conflicts by changing scope, staffing or dates with the user.
8. Fill the [schedule manifest](assets/schedule.template.json), using the [calendar example](assets/schedule-example.json) and scheduling reference for fields. Run `python3 scripts/validate_schedule.py <schedule.json>` relative to this skill directory. Review requirement coverage, unknowns, task granularity and launch criteria manually too. The script checks dates, references, dependencies and capacity; it cannot establish estimate quality, user agreement or release readiness.
9. Present the concrete plan, timeline, costs, trade-offs, assumptions and launch blockers for substantive review. Incorporate corrections. A request to publish once the plan is ready already authorizes project creation; do not request the same permission again. Resolve facts required for accurate publication. If the user delegates an unknown, record the accepted assumption and confidence. Label unresolved drafts as drafts.

## Publish and hand off

10. Follow [the It's a Plan integration](references/its-a-plan.md) to create a new project, plan document, phase initiatives, native cycles, tasks and directional blocking links. Inspect current tool schemas and use returned IDs and the team-qualified project `ref`. Keep a durable local-to-remote ID map. Resume interrupted publication by reconciling existing records before retrying; avoid duplicate projects.
11. Read back the project, document, initiatives, cycles and tasks. Verify counts, descriptions, owners, membership, dates, estimates, dependency direction and scheduled/backlog separation. Publish pending work in planned/unstarted states. Implementation or launch is not complete because the plan exists. Report partial publication precisely and continue recoverable work.
12. Return the actual project link, selected bootstrap, phase/task/cycle counts, date range and blockers. Hand off the first ready work session with its prerequisites and acceptance criteria. Begin bootstrap/build/deployment when the user's current authorization includes that work. Update the approved plan when scope or capacity changes.

## Guard against incomplete plans

| Situation | Required action |
|---|---|
| The brief is short | Continue the interview; avoid genre defaults. |
| A form adds server work | Keep the website profile and add its hybrid requirements. |
| Deadline or capacity is unknown | Ask or obtain an accepted provisional calendar before assigning native cycles. |
| A create call times out | Reconcile the stable plan marker and remote records before retrying. |
| Native initiative/cycle support is blocked | Preserve the plan and report the exact structural blocker. |
| Provider access or production evidence is missing | Create a blocker/gate task; keep launch readiness pending. |
