# Website Skills — Kaizen Wave 1 Report

Date: 2026-08-11
Repository: `C:\wamp64\www\website-skills`
Owner: website-skills maintainer
Wave: 1
Scope: assigned P0 repairs and the smallest safe P1 evidence improvement

## Executive result

The repository started on a clean `main...origin/main` baseline. The exercise
baseline was 60 active skills, 60/60 contract checks, 28/28 routing fixtures,
five baseline test functions, quick-validator pass, and source-ingestion
guardrail pass (`C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md`, website-skills
row). The diagnostic raw score was 59.4/100, the exercise-published score was
55.0/100 after the mandatory `min(raw, 55)` cap, and maturity was L2 — repeatable
with material evidence gaps. The repository's permanent 65-point cap remains
unchanged in `README.md` and
`skills/quality-gates/kaizen-engine-and-product-improvement/SKILL.md`.

Wave 1 repaired current catalogue documentation, active route references,
broken-link candidates, standards-register currency, unsafe source provenance,
and rollback authority boundaries. It added a fictional local benchmark for
links, semantics, accessibility inputs, and performance-budget inputs. The
post-change raw score is held at 59.4/100 pending independent re-audit; passing
structural and lab checks is not treated as a score award. The published score
therefore remains 55.0/100. Post-change maturity remains L2, with a measured
lab slice but no production or outcome evidence.

## Evidence and method

The governing method was the reference cycle in the master assignment and the
workspace assessment:

`Observe → Baseline → Select → Experiment → Check → Standardise → Teach → Re-measure`

The implementation also followed the required skill-writing, skill-safety,
composition, advanced-testing, and anti-slop instructions. Canonical skill
logic remains model-neutral. Route changes use explicit
`design-system-skills:<skill>` locators where the target was relocated; no
vendor-specific procedure was added to a `SKILL.md`.

The repository baseline and exercise scoring rules were taken from
`C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md`. Standards refresh used only the
workspace source register at
`C:\wamp64\www\KAIZEN-STANDARDS-SOURCE-REGISTER.md`; rows without a matching
workspace record remain `NOT ASSESSED`.

## Baseline inventory, score, and maturity

| Measure | Baseline | Wave 1 result | Evidence and limit |
|---|---:|---:|---|
| Active skills | 60 | 60 | Registry and filesystem agree; no catalogue expansion |
| Contract validation | 60/60 | 60/60 | `scripts/validate-skill-contracts.py` exit 0 |
| Routing fixtures | 28/28 | 28/28 | `scripts/routing-smoke-test.py` exit 0; 100% top-three result |
| Baseline test functions | 5 | 10 passed | New tests cover counts, routes, provenance, rollback, and fixture benchmark |
| Reported heuristic link candidates | 23 | 0 targeted candidates | Independent local relative-link scan; full drift-check remained NOT ASSESSED |
| Source-ingestion findings | 0 | 0 | `scripts/source_ingestion_guardrail.py` exit 0; this does not prove rights |
| Diagnostic raw score | 59.4/100 | 59.4/100 held | No numerical uplift awarded without independent re-audit |
| Exercise-published score | 55.0/100 | 55.0/100 | Exercise-only cap; permanent repository cap remains 65 |
| Maturity | L2 | L2 | Local lab evidence improved; production and outcome evidence remain absent |

The baseline score and maturity are diagnostic, not certification. No claim of
production readiness, field accessibility, field performance, or successful
remote rollback is made by this report.

## Files changed

### Catalogue, routes, and standards

- `AGENTS.md`, `CLAUDE.md`, and `README.md` — corrected the quality-gates
  category count to six and made current relocated design routes explicit.
- `scripts/validate-skill-registry.py` — checks the filesystem-derived total,
  current README and CLAUDE category counts, and manifest-to-relocation-map
  agreement.
- `docs/relocation-map.md` was already the machine-readable route target; no
  route row was invented. Current consumers now use the external-engine form.
- `templates/README.md`, `templates/skill/SKILL.md`,
  `skills/agency-ops/agency-positioning/SKILL.md`,
  `universal-guidelines/UNIVERSAL-DESIGN-GUIDELINES.md`,
  `new-project.sh`, `new-project.ps1`, `prompts/new-project-kickstart.md`, and
  `docs/onboarding-validation/2026/report.md` — repaired current stale paths
  and relocated-route wording.
- `README.md`, `docs/roadmap-public.md`, `docs/licensing-matrix.md`,
  `glossary.md`, and `performance-budgets.json` — replaced references to
  removed plan/evaluation paths with files that exist or with the current
  public roadmap wording.
- `docs/standards-register.md` — aligned the WCAG, Search Essentials, and Core
  Web Vitals entries with STD-001, STD-015, and STD-016 from the workspace
  register; refreshed matching review dates and declared unmatched rows
  `NOT ASSESSED`.

### Provenance and rollback

- `skills/orchestration/premium-ui-ux-design/references/source-register.md` —
  removed local EPUB paths and third-party library-site metadata from active
  provenance, retained a quarantine disposition, and defined the evidence
  required before any source is re-added.
- `skills/orchestration/premium-ui-ux-design/SKILL.md` — changed the source
  register description to a provenance and rights gate rather than an active
  local-library source claim.
- `scripts/rollback.sh` — requires explicit approval, exact target binding,
  pre-provisioned known hosts, safe target characters, a whitelisted reload
  service, release-root containment, post-swap verification, temporary key
  storage outside the user SSH directory, and original-symlink recovery on
  swap or reload failure.
- `skills/launch-ops/deploy/SKILL.md`,
  `skills/launch-ops/deploy/references/rollback-runbook.md`, and
  `skills/launch-ops/deploy/references/ci-troubleshooting.md` — document the
  new rollback contract and recovery boundary.

### Deterministic local evidence

- `fixtures/website-kaizen/fixture.json`, `index.html`, `about.html`, and
  `styles.css` — fictional/test-labelled two-page local fixture.
- `scripts/website_fixture_benchmark.py` — standard-library benchmark for
  internal links, HTML landmarks/headings, metadata, image alt inputs, form
  label inputs, and available performance-budget inputs.
- `tests/test_website_fixture_benchmark.py` — deterministic repeat-run test.
- `tests/test_kaizen_wave1_contracts.py` — count, relocation, provenance, and
  rollback contract tests.
- `skills/meta/skill-writing/references/skill-authoring-best-practices.md`,
  `skills/content-copy/blog-writer/references/editorial-standards.md`, and
  `skills/seo-search/seo/references/llms-txt-and-ai-crawlers.md` — removed
  dead links and converted illustrative, unavailable destinations into
  explicitly labelled placeholders rather than pretending they are repository
  files or real URLs.

## Improvement contracts

### W1-P0-01 — catalogue truth and route integrity

- Gap: Current documentation and route references could drift from the 60-file
  filesystem catalogue; the baseline also reported stale relocation routes and
  23 heuristic broken-link candidates.
- Root cause: Counts and paths were repeated manually, while a relative-link
  heuristic treated unavailable examples, removed directories, and relocated
  skills as actionable paths.
- Change: Added filesystem/category/count and manifest/relocation-map checks to
  `scripts/validate-skill-registry.py`; corrected current docs, templates,
  prompts, and active route references; removed dead links and code-block URL
  placeholders.
- Hypothesis: A fresh agent will receive a route that resolves through the
  manifest or global engine-routing table, and future catalogue drift will fail
  a deterministic gate.
- Owner: website-skills maintainer.
- Measure: registry exit 0; 60 active skills; 28/28 routes; targeted relative
  link scan reports 0 candidates.
- Risk: External consumers may still use historic names or removed plan paths.
  The route map remains the compatibility record; historical plans were not
  bulk-rewritten.
- Rollback: Revert the touched documentation and validator files as one patch;
  no catalogue files were removed or renamed.
- Acceptance evidence: `python -X utf8 scripts/validate-skill-registry.py`,
  `python -X utf8 scripts/routing-smoke-test.py`, pytest, and the targeted link
  scan all exited 0 after the change.
- Standardisation: Registry checks now make current count and relocation-map
  consistency part of the repository gate.
- Re-audit: 2026-08-18.

### W1-P0-02 — provenance and standards currency

- Gap: The source register contained unsafe third-party library-site metadata;
  the standards register had a review date before the workspace register date.
- Root cause: Local extraction provenance was recorded as active source metadata,
  and standards currency was maintained independently from the workspace source
  register.
- Change: Quarantined the unsafe source register without replacing it with an
  invented publisher, author, URL, or rights claim. Updated matched standards
  entries and left unmatched rows visibly `NOT ASSESSED`.
- Hypothesis: Agents will not treat an unverified local or piracy-site
  identifier as authority, and mutable standards will have a dated review
  control tied to the workspace source register.
- Owner: website-skills maintainer with design/website standards owner.
- Measure: No `z-library`, `z-lib`, EPUB, or local-download identifier remains
  in the active source register; source-ingestion guardrail remains at zero;
  matched standards show the 2026-08-11 register date and 2026-11-11 review.
- Risk: Removing provenance reduces historical traceability. The quarantine
  note preserves the disposition and states the evidence needed for lawful
  re-entry; it does not claim the source material is verified.
- Rollback: Restore the previous register only after a rights and provenance
  review; otherwise retain the quarantine and create a verified bibliography.
- Acceptance evidence: safety scan of changed surfaces produced no findings,
  `scripts/source_ingestion_guardrail.py` exited 0, and the provenance test
  passed.
- Standardisation: Source registers must contain bibliographic and rights
  evidence, not local download paths or third-party metadata; workspace STD IDs
  are recorded at the point of standards use.
- Re-audit: 2026-08-18 for P0; 2026-11-11 for standards currency.

### W1-P0-03 — rollback authority, target, and recovery

- Gap: The previous helper wrote a private key under the user's SSH directory,
  used `accept-new`, accepted an arbitrary reload command, and did not bind
  approval to an exact target or prove recovery after a failed swap/reload.
- Root cause: The helper mixed credential staging, target selection, mutation,
  and reload authority without a narrow validation contract or recovery path.
- Change: `scripts/rollback.sh` now validates explicit authority and target
  binding, uses an existing known-hosts file with strict checking, stages the
  key in a mode-restricted temporary file, allows only named reload services,
  constrains release symlinks to the declared release root, verifies the swap,
  and attempts to restore the original pair on failure.
- Hypothesis: A caller with incomplete authority or an unsafe target will stop
  before remote mutation, while a failed remote operation leaves a recoverable
  and logged state when the recovery command itself succeeds.
- Owner: website-skills release operator.
- Measure: shell syntax exit 0; valid local validation exit 0; invalid target
  validation exit 3; static safety assertions pass; remote end-to-end rollback
  remains NOT ASSESSED.
- Risk: Requiring a known-hosts file and explicit approval can block an
  unprepared release operator. This is an intentional release safety trade-off.
- Rollback: Restore the prior helper only under an explicit security decision;
  retain the new runbook contract and do not silently re-enable unknown-host
  acceptance.
- Acceptance evidence: Git Bash `-n` exit 0; `ROLLBACK_VALIDATE_ONLY=1` valid
  test exit 0; mismatched `ROLLBACK_TARGET` exit 3; pytest static contract
  passed.
- Standardisation: The deploy skill, rollback runbook, and troubleshooting
  guide now carry the same environment contract and recovery boundary.
- Re-audit: 2026-08-18; run only against a disposable, explicitly authorised
  deployment target.

### W1-P1-01 — local website behaviour benchmark

- Gap: No production benchmark demonstrated website links, semantics,
  accessibility inputs, or performance-budget inputs; field Core Web Vitals
  were unavailable.
- Root cause: Existing evidence was mainly skill contracts and routing fixtures,
  not a small runnable website artefact.
- Change: Added the fictional `website-kaizen-local-fixture` and a deterministic
  standard-library benchmark. It checks local link resolution, one main landmark,
  one H1, language, navigation, heading order, image-alt and form-label inputs,
  metadata, and the declared raw fixture ceiling against the available global
  budget input.
- Hypothesis: A small local fixture will make representative regressions
  observable without pretending to be a client site or field dataset.
- Owner: website-skills maintainer.
- Measure: Benchmark status PASS on two pages; fixture asset bytes 2,026;
  declared total-weight input 350 KB; field Core Web Vitals `NOT ASSESSED`.
- Risk: A synthetic fixture can overstate real browser, assistive-technology,
  network, content, or production quality.
- Rollback: Remove the fixture and its two test/benchmark files if a fresh audit
  shows that they add noise; preserve the P1 gap rather than weakening the
  benchmark.
- Acceptance evidence: `python -X utf8 scripts/website_fixture_benchmark.py`
  exited 0; repeat-run pytest assertion passed; all existing gates remained
  green.
- Standardisation: Keep lab, render, system, and production evidence as
  separate fields. Promote this fixture to a release gate only after a second
  wave confirms useful defect detection.
- Re-audit: 2026-08-25.

## Before/after evidence classification

| Evidence class | Wave 1 status | Interpretation |
|---|---|---|
| Structural | PASS | Registry, contracts, route fixtures, file counts, and link scan passed |
| Behavioural | PASS for the local fixture and input validation branches | The fixture and rollback validation are bounded tests, not full workflows |
| Render | NOT ASSESSED | No browser render or visual diff was run for the fixture |
| System | NOT ASSESSED | No disposable Linux host, remote deployment target, service reload, or field telemetry was used |
| Production | NOT ASSESSED | No production site or field Core Web Vitals dataset was supplied |
| Semantic source support | NOT ASSESSED portfolio-wide | The provenance quarantine removes an unsafe reference; it does not verify every design rule |

## Test commands and results

All commands below were run from `C:\wamp64\www\website-skills` after the
patch unless explicitly marked otherwise.

| Command | Result | Exit |
|---|---|---:|
| `git status --short --branch` baseline | Clean `main...origin/main` before edits | 0 |
| `python -X utf8 scripts/website_fixture_benchmark.py` | PASS; lab-only JSON; field Core Web Vitals `NOT ASSESSED` | 0 |
| `python -X utf8 scripts/validate-skill-registry.py` | `registry valid: 60 skills` | 0 |
| `python -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | 60 active, one template, zero debt | 0 |
| `python -X utf8 scripts/routing-smoke-test.py` | 28/28 top-three hits (100.0%) | 0 |
| `python -X utf8 scripts/source_ingestion_guardrail.py --root .` | findings: 0 | 0 |
| `python -X utf8 skills/meta/skill-writing/scripts/quick_validate.py` over all 60 skill directories | checked 60, failed 0 | 0 |
| `python -m pytest -q` | 10 passed | 0 |
| `C:\Program Files\Git\bin\bash.exe -n scripts/rollback.sh` | shell syntax valid | 0 |
| rollback validation with test-labelled inputs and matching target | PASS; remote state `NOT ASSESSED` | 0 |
| rollback validation with mismatched target | refused as expected | 3 |
| `git diff --check` | no whitespace errors; Git emitted line-ending normalisation warnings | 0 |
| targeted deterministic relative-link scan | 0 candidates after triage | 0 |

### Checks not assessed

- `bash scripts/drift-check.sh` through the Windows system shim failed because
  `/bin/bash` was unavailable. An explicit Git Bash run timed out after 124
  seconds while scanning the large repository. Neither result is a pass, and
  no post-change drift-check verdict is claimed.
- The target repository has no `scripts/engine_compliance.py`; that named
  canonical engine scanner was unavailable and is `NOT ASSESSED`.
- The target repository has no local `scripts/skill_catalog_guardrails.py`;
  the available source-ingestion guardrail and zero-debt contract validator
  were run instead. Catalog guardrail equivalence is `NOT ASSESSED`.
- No browser, assistive-technology, render, disposable Linux, remote host,
  production site, field telemetry, or independent human review was available.

## Remaining P0, P1, and P2

### Remaining P0

- Obtain a bounded, disposable target and independently test rollback swap,
  reload failure, recovery, and log retention. Do not test against a live host
  without named authority.
- Complete the drift-check run in an available Bash environment and inspect the
  generated report. The current timeout is an evidence gap, not a failure claim.
- Reconcile standards rows not represented in the workspace register. They are
  intentionally not certified by this wave.

### Remaining P1

- Add a browser-rendered fixture run with explicit PASS/FAIL/NOT ASSESSED fields
  for visual, accessibility-tool, and performance-lab evidence.
- Add a second independent fixture review to test whether the local benchmark
  catches seeded link, landmark, metadata, and budget failures without widening
  its scope.
- Add semantic claim-support review for design guidance; a URL or local source
  record alone is not semantic proof.

### Remaining P2

- Maintain the workspace source register with owner, applicability, access date,
  version/effective date, confidence, and next review only for mutable claims.
- Add a cross-agent discovery smoke matrix for `AGENTS.md`, `CLAUDE.md`,
  canonical `SKILL.md`, and a generic manual route. Actual vendor loader
  behaviour remains untested here.
- Improve the repository drift checker so it skips fenced examples or reports
  them as intentional placeholders without hiding real links.

## Claude, Codex, and generic-agent compatibility

- Canonical skill procedures remain in `SKILL.md`; repository-wide routing and
  safety rules remain in `AGENTS.md`.
- `CLAUDE.md` retains the Claude-specific repository guidance and now carries
  the corrected catalogue count. No duplicated rollback or benchmark procedure
  was added there.
- Codex can use the repository-relative paths and manifest route contract in
  `AGENTS.md`, `README.md`, and `skills/manifest.yml`.
- A generic agent without automatic instruction-file loading can still use the
  explicit repository controller and canonical `SKILL.md` paths. Automatic
  vendor discovery was not executed in this wave and is `NOT ASSESSED`.

## Unrelated or pre-existing changes

The baseline `git status --short --branch` was clean before edits. No
pre-existing or unrelated working-tree changes were observed. All dirty files
listed by the final diff were part of this bounded Wave 1 patch.

## Residual risks and rollback of this wave

The largest residual risk is evidence interpretation: the local fixture can
prove only small deterministic checks, and the hardened rollback helper has not
run against a real or disposable remote target. The standards register still
contains `NOT ASSESSED` rows, and the timed-out drift-check leaves one
repository-wide validation gap.

To roll back this code change, revert the Wave 1 file set as a reviewed patch;
no commit, push, fetch, pull, reset, or broad deletion was performed. Do not
restore the quarantined source metadata or the old rollback host-key behaviour
without a separate security decision and acceptance evidence.

## Next wave recommendation

The next highest-value experiment is an independently reviewed disposable
rollback test plus a browser-rendered version of the local fixture. This will
close the largest gap between the current structural/lab evidence and the
production claims that remain unavailable. Recalculate the raw and capped score
only after those results are retained and reviewed.
