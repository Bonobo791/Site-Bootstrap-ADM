# Repository guidance

Adapt to this project's actual stack and user instructions.

## Scope and branches

Make focused changes in an isolated dev checkout/worktree; main is release. Preserve unrelated edits. Commit verified work locally. Pushes, merges, deploys and production access follow explicit user authorization/project policy. Never force-push by default.

## Before feature work

Invoke $site-bootstrap-adm when available. Classify static or server-enabled website behavior and selected capabilities. Keep docs/bootstrap.md and docs/bootstrap-tasks.md verified/pending/not-applicable with evidence. Each applicable requirement needs exact files/config/commands/tests/done criteria. Keep docs/routes.md and docs/environment.md current. Record actual runtime/package manager/commands/integrations here after inspection. Do not guess commands or inherit another project's identifiers/secrets/data.

## Verification

Keep check, lint/format, test and build green. Include fast-check in the ordinary suite. Define independent invariants/detectable faults in docs/testing-invariants.md; pair properties with regressions and scoped Stryker --ignoreStatic where applicable. Inspect mobile/desktop screenshots for UI changes.

Preserve established property/mutation contracts. Never weaken tests or thresholds to conceal failure. Validate review findings against current code; reproduce real behavioral bugs before fixes.

## Boundaries

Use isolated dev/test credentials/disposable DBs. Production access and writes follow this target's policy and session authorization. Keep secrets server-only and out of logs/artifacts; show safe errors. No silent fallback or fake integration success.

Analytics defaults off; activation needs owned runtime settings, exact hosts and reviewed public-route/data/preferences policy.

## Handoff

Report changed behavior, results and pending provider/operator checks. Local green does not prove CI, delivery, deployment or recovery.
