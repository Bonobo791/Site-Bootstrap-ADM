# Testing, including fast-check

Read for every profile. Install a useful harness before features; extend independent rules and tests before implementing each new behavior.

Contents: [runner](#t01-runner-and-discovery), [invariants](#t02-invariant-register), [properties](#t03-property-construction-and-state), [replay](#t04-run-controls-and-replay), [layers](#t05-profile-verification-layers), [mutation](#t06-faults-mutation-and-review), [evidence](#t07-testing-completion).

## T01 Runner and discovery

**Files:** runner config, `package.json` scripts, fast-check dev dependency + lockfile, adjacent `*.test.ts`/`*.pbt.test.ts` or runner-equivalent JS.

1. Preserve the existing runner; prefer Vitest for a new TS app when compatible. Node's test runner is sufficient for plain JS modules.
2. Pin compatible fast-check/tooling versions through the chosen manager. The bundled example pins fast-check 4.9.0; verify compatibility on reuse.
3. Make properties discoverable by the ordinary `test` command and CI. Name examples and properties distinctly. Fail on no tests; don't exclude properties merely to get fast green.
4. Define source/test include/exclude rules explicitly. Exclude dependencies, generated builds, temporary mutation copies and unrelated worktrees to avoid duplicate discovery.
5. Configure framework plugins where required. Use the correct node/browser test environment and timeout for bounded async/property work; don't extend timeouts to hide deadlocks.
6. Put pure rules in real production modules; unit tests import those modules. Integration tests call actual handlers/services/persistence. Mocks belong at transport/clock/provider seams.

**Commands:** clean install → ordinary `test`. Inspect discovered test names/files, including at least one actual `.pbt.test.`. A targeted properties script is additional; it cannot replace ordinary discovery.

**Done:** deterministic tests and meaningful properties execute in the normal suite/CI. A synthetic copied demo proves the harness pattern only.

## T02 Invariant register

**File:** `docs/testing-invariants.md`. Create an entry before writing the property.

| Required field | What to record |
| --- | --- |
| ID/requirement | Independently stated business/config contract and applicable capability |
| Boundaries | Accepted/rejected cases, relevant time/size/count limits and failure transitions |
| Oracle | Specification, reference model, before-state snapshot or conservation law |
| Input strategy | Valid/hostile domains, boundary values, duplicates and operation sequences |
| Observations | Real outputs, persisted before/after state, effects and forbidden effects |
| Detectable fault | Concrete wrong change that must turn the test red |
| Deterministic regressions | Named fixtures for known and shrunk failures |
| Evidence | Exact command, test count/result, replay seed/path and fault/mutation result |
| Limitations | Unspecified transitions, integration assumptions and pending checks |

The implementation must not compute its own expected result. Separately review whether the rule itself matches the product requirement. A generator cannot discover an absent business rule.

| Profile/capability | Candidate independent rule | Concrete fault |
| --- | --- | --- |
| Static URL/metadata | Canonical uses configured origin, normalized public path and no forbidden query/fragment | Preserve raw query or accept wrong origin |
| Static content | Invalid/empty/draft content cannot enter published output | Treat an empty rich-text block as publishable |
| Contact | Rejected input has zero provider/lead writes | Deliver before validation |
| Runtime analytics | Disabled/wrong-host/private/credential pages send nothing | Remove opt-in or change exact host to suffix matching |

Choose real applicable rules; do not create billing/jobs simply to populate this table.

## T03 Property construction and state

- Prefer construction with `fc.record`, `fc.array`, maps and uniqueness constraints. Cover valid and hostile inputs deliberately. Excessive `filter`/preconditions hide input regions and slow shrinking.
- Include empty/one/max/one-over values, Unicode/encoding, malformed nullable external data and duplicate/reordered operations where relevant.
- Use block-bodied predicates with assertions and no returned Assertion object.
- For async behavior use `fc.asyncProperty` and await the actual operation and `fc.assert`.
- Create/reset logical state **inside each generated run**, not only before each test. Rollback transactions/isolated namespaces/guarded disposable reset are valid if they cover all effects.
- Reset mock implementations as well as calls. Domain functions and authorization must remain real. Use disposable persistence for claims about data state/transactions.
- Inject/generate clock values and bound delays. Real clock reads produce irreproducible expiry/rate/retention tests. Fake-timer/async-property deadlocks require fixing the harness.
- Observe final state/response and forbidden effects, not just a mocked method's count.
- Generated operation arrays suit sequential workflows. Use model commands for real state machines and controlled scheduling for actual concurrency; no mandatory complexity for simple validation.
- Use realistic bounded domains; run count is not exhaustive coverage.

A per-run async persistence test has this shape:

```ts
await fc.assert(
  fc.asyncProperty(caseArbitrary, async (scenario) => {
    const fixture = await createDisposableFixture(scenario);
    try {
      const before = await fixture.snapshot();
      const response = await realOperation(fixture, scenario);
      assertContract(response, before, await fixture.snapshot(), scenario);
    } finally {
      await fixture.dispose();
    }
  }),
  propertyOptions()
);
```

The fixture/oracle names are adaptation points, not supplied production functions. Cleanup and seed must cover side effects outside the database too.

## T04 Run controls and replay

**Files:** a shared property-options helper adapted from `assets/fast-check-example/property-options.mjs`; optional targeted test script/CI manual job.

- Default `numRuns` to 100. Parse `FC_NUM_RUNS` as a positive safe integer; reject invalid/empty/unsafe input if supplied.
- Use focused 1,000/10,000-run checks for important rules when needed. These supplement ordinary CI; more samples cannot fix a bad oracle.
- Parse `FC_SEED` within the supported signed 32-bit integer range. `FC_PATH` requires a seed and valid replay-path format. Preserve env overrides through test env mocks.
- On failure record seed/path, shrunk synthetic counterexample, violated contract and exact test/file. Avoid logging actual credentials/customer fixtures.
- Replay **only the failed property**, with the same compatible version/arbitrary/implementation. Applying one shrink path to unrelated properties is not a valid replay.
- Add the shrunk case to deterministic regression tests, fix the logic/specification issue, rerun replay and ordinary suite. Don't narrow input merely to conceal it.

Examples, adapted to real script/test names:

```sh
FC_NUM_RUNS=1000 npm test
FC_SEED=123 FC_PATH='0:1' npx vitest run src/lib/example.pbt.test.ts -t 'exact property name'
```

The seed/path above illustrate syntax and are not known failure evidence. Use the values emitted by the actual failure. For the bundled Node example, select the failed test with `node --test --test-name-pattern='exact test name' eligibility.test.mjs`.

## T05 Profile verification layers

| Layer | Static pages | Hybrid endpoints |
| --- | --- | --- |
| Unit/regression | Actual content/URL/config helpers | Body/schema/origin/abuse/delivery contract |
| Properties | Metadata/content/environment invariants | Rejected payload/host/rate/zero-effect rules |
| Integration | Generated CMS schema/content + built files | Actual handler/adapter + isolated provider failures |
| Provider | CMS cloud editor if selected | Actual sandbox lead/email/API delivery |
| Browser | Each template/nav/keyboard/responsive/SEO/404 | Form loading/success/error/duplicate/no-JS |
| Release | Served files/headers/SHA | Served content + endpoint/cache/secret behavior |

**Files:** separate integration fixtures and Playwright tests; built-output inspector where useful. Server browser tests use isolated accounts/resources, never production DB.

Run browser tests against the selected built artifact/start command, not only dev. Inspect representative narrow/desktop screenshots and long/empty/error content. Verify actions and direct HTTP requests as well as visual state.

Provider mocks establish local contracts. They cannot mark a real callback, delivery, payment or backup verified.

## T06 Faults, mutation and review

1. Choose a real invariant's concrete fault, deliberately apply it in a disposable copy, run the targeted test and observe red.
2. Restore correct source, rerun the test and ordinary affected suite. Record the changed contract and evidence; never leave the fault in the target.
3. Where meaningful domain modules exist, install/configure compatible Stryker + runner. Scope mutation to actual hand-authored modules, exclude generated/vendor code and irrelevant static/UI scaffolding.
4. Run scoped Stryker with `--ignoreStatic`; inspect survivor/timeouts/no-coverage separately. Follow target cache/concurrency policy.
5. Add deterministic regressions for genuine missing behavior; justify equivalent/unreachable mutants. Preserve established thresholds instead of weakening them for green.
6. Record whether properties participate in mutation kills. Document whether example tests alone or properties also establish kills. Preserve an existing project's accounting.
7. No universal 100% mutation target is inherited from a reference project. No meaningful mutable logic means mutation N/A with a reason, not fabricated coverage.
8. Review omitted requirements, state transitions, integration assumptions and oracles separately. Validate review findings against source; reproduce actual bugs before fixes.

Fast-check, deterministic examples, deliberate faults/mutation and requirements review serve different purposes. None alone proves all edge cases.

## T07 Testing completion

Record actual versions/config/discovery, invariant entries, normal suite result, regression/replay/fault results, selected migration/browser/provider checks and scoped mutation accounting.

A green harness that only tests array reversal or this bundle's demo leaves actual project property coverage pending. An unexecuted CI file leaves CI pending. Mock integrations leave provider verification pending.

### Runnable pattern

In `assets/fast-check-example/` run `npm ci --ignore-scripts` then `npm test`. The locked synthetic gate demonstrates exact-host/private-route/encoded-credential rules, validated controls and regressions.

It is not a tracker, payload sanitizer, consent implementation or DB test. Adapt its options/assertion pattern to actual production behavior and retain its limitations in the evidence.
