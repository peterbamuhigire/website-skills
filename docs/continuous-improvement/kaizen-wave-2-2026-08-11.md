# Website Skills - Kaizen Wave 2 Report

Date: 2026-08-11
Repository: `C:\wamp64\www\website-skills`
Owner: website-skills maintainer
Wave: 2
Scope: independent challenge of Wave 1 drift, rollback, and local-fixture evidence

## Executive result

Wave 2 confirmed that the Wave 1 local fixture was useful but under-tested, the
rollback contract had an untested CI integration boundary, and the existing
repository-wide drift script was not a bounded gate in this Windows checkout.
The Wave 1 report recorded the old Git Bash drift run as timed out and therefore
`NOT ASSESSED`; a fresh rerun reached the same evidence gap before the script
produced a result. The old script also created a timestamped report and relied on
unbounded filesystem scans and shell heuristics.

The bounded replacement now completes in the local checkout, reads a stable
Git-listed Markdown scope with file and byte ceilings, and keeps the date-based
deprecation check explicit through `--as-of`. Wave 2 adds static and validation
tests for rollback target confinement, authority, last-safe state, and recovery
without opening an SSH session. It also mutates copies of the local website
fixture to prove that broken links, semantic structure, and budget inputs fail.

No remote rollback, browser render, field Core Web Vitals collection, production
site check, or disposable-host recovery was executed. Those states remain
`NOT ASSESSED`.

## Fresh re-audit findings

The re-audit started from the existing Wave 1 working tree. `git diff HEAD` showed
Wave 1 files and no unrelated changes in this repository before Wave 2 edits.
The Wave 1 commands for registry, contracts, routing, source ingestion, the
fixture, tests, and rollback syntax were rerun and remained green. The local
fixture benchmark passed on both declared pages, but its only behavioural test
repeated the positive case; it did not prove failure detection.

The Wave 1 rollback test checked source markers and local validation. It did not
exercise a disposable target, and the canonical CI rollback job did not pass the
new `DEPLOY_KNOWN_HOSTS`, `ROLLBACK_APPROVED`, `ROLLBACK_TARGET`,
`ROLLBACK_REASON`, or `RELOAD_SERVICE` inputs. That mismatch could cause a
failure hook to stop before its intended authority decision. Wave 2 wires the
inputs explicitly and keeps approval unset unless the release owner supplies it.

The first drift challenge was decisive. The prior `scripts/drift-check.sh` scan
was run through Git Bash with a bounded command timeout and did not complete.
The Wave 1 report records the same gate as a 124-second timeout and correctly
left it `NOT ASSESSED` ([Wave 1 report](kaizen-wave-1-2026-08-11.md)). A green
structural suite therefore did not prove repository-wide drift control.

## Wave 1 challenge and result

| Wave 1 assumption challenged | Challenge | Result |
| --- | --- | --- |
| A positive fixture repeat proves useful website behaviour | Copy the fixture, then seed a missing link, remove the main landmark, and provide a zero-weight budget | Each mutation exited 1 and reported the matching failed check ([Wave 2 tests](../../tests/test_kaizen_wave2.py)) |
| Static rollback markers prove safe rollback | Check exact target binding, missing authority, escaped path segments, reload-service allowlisting, last-safe variables, recovery verification, and CI variable wiring | Local validation rejected each unsafe case with exit 3; remote state stayed `NOT ASSESSED` ([rollback script](../../scripts/rollback.sh)) |
| A repository-wide shell scan is a completed gate | Rerun the old scan, then replace the unbounded implementation with a fixed Git-listed scope and repeat the new command | Old scan remained unassessed; new default and fixed-date scans completed with exit 0 ([drift checker](../../scripts/drift_check.py)) |

The challenge did not weaken an existing test or remove a failing fixture. It
added negative controls and retained the strict drift failure as visible
evidence.

## Exact Wave 2 files

Wave 2 changed only these files in `website-skills`:

- `scripts/drift-check.sh` - thin Bash entrypoint for the bounded checker.
- `scripts/drift_check.py` - deterministic scope, link, deprecation, style,
  length, and duplicate-window checks.
- `scripts/rollback.sh` - explicit missing-input handling, log-safe reason
  validation, last-safe state recording, and recovery verification.
- `templates/ci/website.yml` - explicit rollback environment contract.
- `skills/launch-ops/deploy/SKILL.md` - operator-facing rollback contract.
- `skills/launch-ops/deploy/references/rollback-runbook.md` - CI variable and
  recovery documentation.
- `tests/test_kaizen_wave2.py` - drift repeatability, fixture mutations, and
  rollback shell/static tests.
- `docs/continuous-improvement/kaizen-wave-2-2026-08-11.md` - this evidence
  record.

Wave 1 fixture files, Wave 1 tests, and Wave 1 documentation were preserved.

## Improvement contracts

### W2-P0-01 - bounded and deterministic drift evidence

- Gap: The repository-wide drift gate did not complete in the available Git Bash
  environment, so its result was `NOT ASSESSED`. The old implementation used
  unbounded filesystem traversal, shell process loops, a timestamped report,
  and a heuristic duplicate scan.
- Root cause: Scope, ordering, report content, and temporal deprecation input
  were implicit runtime behaviour rather than an explicit contract.
- Change: `scripts/drift-check.sh` now delegates to
  `scripts/drift_check.py`. The checker uses Git-listed Markdown files, excludes
  generated and external-content areas, sorts paths, enforces a 600-file and
  16 MiB scope ceiling, skips fenced code for Markdown links and style checks,
  and emits a stable report. The deprecation check runs only when the caller
  supplies `--as-of YYYY-MM-DD`; otherwise that sub-check is visibly
  `NOT ASSESSED`.
- Hypothesis: A bounded, stable scope will finish in CI and local Git Bash while
  retaining repository-wide coverage of active Markdown and making any scope
  breach an explicit failure.
- Owner: website-skills maintainer.
- Measure: The post-change default wrapper completed with exit 0 over 455
  Markdown files; the fixed-date run also completed with exit 0. The repeat-run
  test compares stdout and report bytes ([Wave 2 tests](../../tests/test_kaizen_wave2.py)).
- Risk: A future repository may exceed the ceiling or place intentional prose in
  a scope excluded for performance. The date check can remain unassessed if an
  operator does not supply its date.
- Rollback: Restore the previous Bash body only through a reviewed decision; if
  the new checker rejects a legitimate scope, raise the fixed ceiling with a
  measured finding or narrow a named exclusion rather than removing the cap.
- Acceptance evidence: `bash scripts/drift-check.sh` exit 0; the same command
  with `DRIFT_AS_OF=2026-08-11` exit 0; the strict negative control exits 4;
  `python -m pytest -q tests/test_kaizen_wave2.py` passes the repeatability
  assertion. The strict result is not presented as a release pass.
- Standardisation: The existing CI entrypoint remains the canonical route, while
  bounded scope, explicit date input, stable output, and exit 9 for scope breach
  are now part of the script contract.
- Re-audit: 2026-08-18, including a repository-growth test near the ceiling.

### W2-P0-02 - rollback authority, target confinement, and recovery

- Gap: Wave 1 improved the helper but only proved static markers and validation
  inputs. The canonical CI rollback job did not provide the new required
  variables, and missing variables did not consistently use the documented exit
  3 path.
- Root cause: The script contract and CI adapter were changed in separate
  surfaces, while the negative tests did not cover missing authority, escaped
  target paths, or recovery verification markers as one contract.
- Change: `scripts/rollback.sh` now checks required variables through an explicit
  prerequisite function, rejects unsafe path segments and log-unsafe reasons,
  retains strict known-host checking, records `LAST_SAFE_CURRENT` and
  `LAST_SAFE_PREVIOUS`, and verifies the pair after recovery. The remote branch
  still allows only named reload services. `templates/ci/website.yml` passes the
  exact authority and known-host path variables without enabling approval.
  `deploy/SKILL.md` and the rollback runbook document the same boundary.
- Hypothesis: An operator or CI job missing authority, target agreement, or a
  safe release-root binding will stop before SSH mutation, while a later failure
  will have an explicit last-safe pair and a checked recovery path.
- Owner: website-skills release operator.
- Measure: Shell syntax exits 0. Local validation accepts the test-labelled
  inputs with exit 0 and rejects missing approval, target mismatch, escaped path,
  and unapproved service values with exit 3. No remote branch was executed.
- Risk: Required CI variables can block a rollback hook on an unprepared runner;
  that is the intended safety trade-off. Remote recovery remains dependent on
  host permissions, filesystem semantics, and service privileges.
- Rollback: Disable the CI adapter only through an explicit release decision;
  preserve strict host-key checking and target confinement. Revert the script and
  docs as one reviewed patch if a disposable-host test identifies a defect.
- Acceptance evidence: static assertions cover target confinement, authority,
  last-safe variables, strict host checking, and recovery; validation-only shell
  tests pass; no SSH call is made because every behavioural test sets
  `ROLLBACK_VALIDATE_ONLY=1` ([Wave 2 tests](../../tests/test_kaizen_wave2.py)).
- Standardisation: The rollback script, deploy skill, runbook, and CI template
  now share one named environment contract. Remote rollback remains an operator-
  authorised action, not a local test shortcut.
- Re-audit: 2026-08-18 on a disposable, explicitly authorised target only.

### W2-P1-01 - adversarial local website fixture

- Gap: Wave 1 proved only a positive local fixture result. It did not show that a
  future agent could detect a broken internal link, a missing semantic landmark,
  or an exceeded raw budget input.
- Root cause: The fixture test asserted repeatability but had no seeded negative
  controls.
- Change: `tests/test_kaizen_wave2.py` copies the local fixture into a temporary
  directory and independently mutates one link, one semantic landmark, and a
  temporary budget file. The source fixture is not edited by the test. Each
  mutation must return exit 1 and identify its matching failed category.
- Hypothesis: Negative controls will prevent a positive-only lab benchmark from
  being mistaken for regression detection, while keeping the benchmark small
  and local.
- Owner: website-skills maintainer.
- Measure: The three seeded mutations each fail the benchmark with exit 1; the
  unchanged benchmark continues to pass and reports field Core Web Vitals as
  `NOT ASSESSED` ([benchmark](../../scripts/website_fixture_benchmark.py)).
- Risk: A synthetic fixture does not represent browser rendering, assistive
  technology, production network conditions, or real content. Its scope remains
  lab-only.
- Rollback: Remove only the Wave 2 negative-control test if it becomes flaky;
  retain the positive fixture and leave unproven browser and production states
  visible.
- Acceptance evidence: `python -m pytest -q` passes all 13 collected tests;
  the targeted test records link, semantics, and budget failures without
  changing the checked-in fixture.
- Standardisation: Representative fixture tests must include at least one
  positive and one failure path, with lab, render, system, and production
  evidence kept separate.
- Re-audit: 2026-08-25 with an independently reviewed browser-rendered fixture
  only if a browser environment is authorised and available.

## Before, Wave 1, and Wave 2 measures

| Measure | Before Wave 1 | Wave 1 | Wave 2 | Evidence |
| --- | ---: | ---: | ---: | --- |
| Active skills | 60 | 60 | 60 | Registry command remained `registry valid: 60 skills` ([Wave 1 report](kaizen-wave-1-2026-08-11.md)); Wave 2 registry gate exit 0 |
| Contract validation | 60/60 | 60/60 | 60/60 | Wave 1 report; `validate-skill-contracts.py` exit 0 |
| Routing fixtures | 28/28 | 28/28 | 28/28 | Wave 1 report; `routing-smoke-test.py` exit 0 |
| Test evidence | 5 baseline functions | 10 passed | 13 passed | Wave 1 report; `python -m pytest -q` exit 0 |
| Drift check | `NOT ASSESSED` | `NOT ASSESSED` after old scan timeout | Default exit 0 over 455 scoped Markdown files; fixed-date exit 0 | `scripts/drift-check.sh`; strict negative control exit 4 |
| Fixture failure detection | No fixture | Positive two-page lab result | Broken-link, semantics, and budget mutations each exit 1 | `tests/test_kaizen_wave2.py` |
| Rollback evidence | Unsafe helper | Validation/static evidence; remote `NOT ASSESSED` | Validation/static evidence with explicit CI contract; remote `NOT ASSESSED` | `scripts/rollback.sh`; validation-only tests |
| Browser rendering | `NOT ASSESSED` | `NOT ASSESSED` | `NOT ASSESSED` | No browser command was run |
| Field Core Web Vitals | `NOT ASSESSED` | `NOT ASSESSED` | `NOT ASSESSED` | No production site or field dataset was supplied |

The Wave 1 diagnostic raw score was held at 59.4/100 and the exercise-published
score at 55.0/100; Wave 2 does not award an uplift because render, system,
production, and outcome evidence remain absent ([Wave 1 report](kaizen-wave-1-2026-08-11.md)).
Maturity remains L2: the repository now has stronger structural and local-lab
evidence, but not the outcome chain required for L3 or above.

## Evidence classification

| Evidence class | Wave 2 state | Boundary |
| --- | --- | --- |
| Structural | PASS | Registry, contracts, routes, quick validation, source guardrail, shell syntax, and static safety assertions passed |
| Behavioural | PASS for local fixture failures and rollback input refusal | No remote deployment or service reload was executed |
| Render | NOT ASSESSED | No browser render or screenshot comparison was run |
| System | NOT ASSESSED | No disposable Linux host, SSH target, filesystem swap, or service reload was used |
| Production | NOT ASSESSED | No production site, telemetry, or field dataset was supplied |
| Semantic support for all website guidance | NOT ASSESSED | The existing standards/source registers remain the source of record; this wave did not perform a portfolio-wide claim-support review ([standards register](../../docs/standards-register.md)) |

## Test commands and exits

Commands were run from `C:\wamp64\www\website-skills`. Exit values below are
retained as evidence; expected negative exits are not converted to passes.

| Command | Result | Exit |
| --- | --- | ---: |
| `python -m pytest -q` | 13 tests passed | 0 |
| `python -m pytest -q tests/test_kaizen_wave2.py` | Drift, fixture mutation, and rollback tests passed | 0 |
| `python -X utf8 scripts/validate-skill-registry.py` | `registry valid: 60 skills` | 0 |
| `python -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | 60 active skills; zero debt | 0 |
| `python -X utf8 scripts/routing-smoke-test.py` | 28/28 top-three routing hits | 0 |
| `python -X utf8 scripts/source_ingestion_guardrail.py --root .` | Findings: 0 | 0 |
| all 60 skill directories through `skills/meta/skill-writing/scripts/quick_validate.py` | Checked 60; failed 0 | 0 |
| `C:\Program Files\Git\bin\bash.exe -n scripts/rollback.sh` | Shell syntax valid | 0 |
| `C:\Program Files\Git\bin\bash.exe -n scripts/drift-check.sh` | Shell syntax valid | 0 |
| `C:\Program Files\Git\bin\bash.exe scripts/drift-check.sh` | Bounded default scan completed over 455 Markdown files | 0 |
| `DRIFT_AS_OF=2026-08-11 C:\Program Files\Git\bin\bash.exe scripts/drift-check.sh` | Fixed-date scan completed | 0 |
| `DRIFT_STRICT=1 ... scripts/drift-check.sh` | Expected strict negative control; existing style findings retained | 4 |
| validation-only rollback with approved, matching test inputs | Remote state `NOT ASSESSED` | 0 |
| validation-only rollback with missing authority, target mismatch, escaped path, or unapproved service | Refused before SSH | 3 |
| old Wave 1 drift command through Git Bash with the bounded audit runner timeout | No result produced; `NOT ASSESSED` | 124 |
| `git diff --check` | No whitespace errors; line-ending normalisation warnings are emitted by Git for existing mixed-line-ending files | 0 |

The full test suite did not run a remote rollback. No command in this report
claims that a remote host, service reload, browser, or field metric was
observed.

## Safety review

Safety surfaces reviewed: the changed rollback script, deploy skill and runbook,
canonical CI template, bounded drift checker, fixture benchmark, and Wave 2
tests. The changed instructions add no installer, remote fetch, new package,
credential collection, log exfiltration, or hidden production action. The
rollback helper still requires explicit approval, an exact target binding, a
readable known-hosts file, strict host-key checking, an allowlisted reload
service, and a release-root confinement check.

The orchestrator's post-wave changed-file scan also reviewed both recursive
cleanup calls. Each cleanup now reasserts that its `mktemp` result begins with
the exact validated target and the expected `.rollback.*` or
`.rollback-recovery.*` prefix immediately before deletion. The static assertions
in `tests/test_kaizen_wave2.py`, the 13-test suite, Bash syntax check, and
`git diff --check` passed after this defence-in-depth change.

Safety status: **Safe for the inspected local surfaces; remote rollback remains
NOT ASSESSED.** No remote rollback was executed. A disposable target with named
authority is required before any system-level safety claim is made.

## Anti-slop review

- The fixture is labelled fictional and local; it is not a client case study or
  a production performance result.
- The report distinguishes structural, behavioural, render, system, and
  production evidence. Unexecuted browser, field, and remote checks remain
  `NOT ASSESSED`.
- Numeric measures are tied to the Wave 1 report or to the command table above.
  No new external statistic, named organisation, court case, statute, or URL was
  introduced by Wave 2.
- The strict drift negative control remains visible. Existing teaching/reference
  text that triggers style warnings was not silently deleted to create a pass.
- No vendor-specific procedure was added to a canonical `SKILL.md`; the GitHub
  Actions environment variables are confined to the CI adapter.

## Claude, Codex, and generic-agent portability

| Consumer | Status | Evidence and limit |
| --- | --- | --- |
| Claude | Contract preserved | Claude-specific repository guidance remains in `CLAUDE.md`; the canonical skill procedure stays in `SKILL.md`. Claude loader behaviour was not executed in this wave, so runtime discovery is `NOT ASSESSED`. |
| Codex | Contract preserved | `AGENTS.md` and repository-relative `skills/<category>/<skill>/SKILL.md` paths remain the Codex route. Codex runtime discovery was not separately executed, so runtime discovery is `NOT ASSESSED`. |
| Generic agent | Manual route available | A generic runner can read `AGENTS.md`, `CLAUDE.md`, the named `SKILL.md`, and the scripts by repository-relative path. Automatic instruction discovery has no universal proof and remains `NOT ASSESSED`. |
| CI runner | Adapter updated | GitHub Actions receives explicit rollback variables in `templates/ci/website.yml`; a missing or unreadable runner known-hosts path stops before SSH. |

The bounded checker uses Python standard-library modules and Git-listed files;
its shell entrypoint requires Bash and Python. If either capability is absent,
the caller must report the gate as unavailable rather than claim a pass.

## Residual P0, P1, P2, and `NOT ASSESSED` states

### Residual P0

- Remote rollback swap, reload-failure recovery, recovery verification, and log
  retention still require a disposable, explicitly authorised target. Owner:
  release operator. Re-audit: 2026-08-18.
- Any source-register row not matched to the workspace standards register remains
  `NOT ASSESSED`; this wave did not refresh external standards. Owner: website
  and design standards owners. Re-audit: 2026-11-11 or before use.

### Residual P1

- Browser-rendered fixture evidence, automated accessibility-tool evidence, and
  performance-lab evidence remain `NOT ASSESSED`. Owner: website-skills
  maintainer. Re-audit: 2026-08-25 if a browser environment is available.
- Semantic claim-support review for all website guidance remains
  `NOT ASSESSED`. A live source URL or register row is not semantic proof.
  Owner: website and design standards owners. Re-audit: 2026-08-25.

### Residual P2

- Strict drift mode still reports existing banned-term, duplicate-window, and
  forbidden-construction findings. The default gate preserves the prior warning
  behaviour; a future change should triage teaching/reference exceptions with
  evidence rather than add broad exclusions. Owner: website-skills maintainer.
- Cross-vendor instruction discovery was documented but not runtime-tested for
  Claude, Codex, or a generic agent. Owner: ecosystem maintainer. Re-audit:
  2026-11-11.
- The fixed drift scope ceiling must be reviewed when the repository grows. A
  scope breach must fail visibly; it must not be solved by deleting files from
  the check.

### Not assessed by design

- Field Core Web Vitals.
- Browser rendering and screenshot fidelity.
- Assistive-technology outcomes.
- Remote rollback and service reload.
- Production website behaviour, conversion, telemetry, and incident recovery.
- Portfolio-wide semantic support of every current website claim.

## Score and re-audit decision

The Wave 1 raw diagnostic score remains held at 59.4/100 and the exercise score
remains capped at 55.0/100. Wave 2 adds retained behavioural evidence and closes
the old drift completion gap in the local checkout, but it does not justify a
score award for unobserved render, system, production, or outcome dimensions.
The repository remains L2 with a measured structural/local-lab slice and
material evidence gaps.

Next re-audit: 2026-08-18 for rollback and drift scope; 2026-08-25 for browser
and semantic evidence if the required environments and owners are available.

No commit, push, fetch, pull, reset, publish, remote rollback, sibling-repository
edit, or workspace-level report edit was performed.
