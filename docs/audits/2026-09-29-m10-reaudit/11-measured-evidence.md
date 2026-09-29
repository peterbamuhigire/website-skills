# Measured evidence

Host: Windows 11, Git Bash; engine root `C:\wamp64\www\website-skills`; HEAD
`ec72bca`; 29 September 2026; `PYTHONDONTWRITEBYTECODE=1`. Working tree clean
before and after the runs (`git status --short` empty apart from this folder).

## Declared validators (task list)

| Command | Exit | Key output |
|---|---:|---|
| `python scripts/validate-skill-registry.py` | 0 | `dependency_minimalism: PASS`; `design routes: PASS (8 routed design skills exist)`; `registry valid: 62 skills` |
| `python scripts/website_fixture_benchmark.py` | 0 | `"status": "PASS"`, `"evidence_type": "lab fixture only"`; pages `index.html`, `about.html` PASS; raw fixture assets 2,026 bytes against a 350 KB budget; dependency minimalism PASS; `"field_core_web_vitals": "NOT ASSESSED"` |
| `python scripts/routing-smoke-test.py --min-rank1 92 --lint-fixtures` | 0 | `37/37 top-3 hits (100.0%); lexical proxy, not live routing`; `precision@1: 35/37 (94.6%)`; `owned negatives: 21 (pass 21, fail 0, not assessed 0)`; `fixture lint findings: 0` |
| `python scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | 0 | `62 active skills, 1 templates`; `zero debt` |
| `python -X utf8 -m pytest -q -p no:cacheprovider tests` | 0 | `131 passed in 71.34s` |

## Slop-scan gate self-test and other CI gates

The README and `AGENTS.md` document `scripts/slop-scan.sh` but no separate
self-test command; its self-test is carried by `tests/test_slop_scan.py` (fail
fixture exits 1, pass fixture exits 0, missing dist exits 5, tampered vendored
detector yields `NOT_ASSESSED`, visitor-mode runs), included in the 131 passes.
The remaining steps of `.github/workflows/skill-engine-quality.yml` were also run:

| Command | Exit | Key output |
|---|---:|---|
| `python -X utf8 scripts/validate-search-doctrine.py` | 0 | `search-doctrine: PASS (18 canonical files, currentness verified)` (local assertions, not fresh external verification) |
| `python -X utf8 scripts/check-vendored-detector.py` | 0 | `manifest PASS (20 files, source commit 3fe84a6…); source comparison PASS` |
| `node scripts/validate-slop-pack.mjs` | 0 | `PASS: 20 pack rules checked against 49 registry rules` |
| `node hooks/test-*.js` (4 files) | 0 each | destructive-bash-gate, drift-check-hook, plugin-hook-config, quality-gate |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | 0 | `findings: 0` |
| `bash scripts/test-banned-phrase-scan.sh` | 0 | `dirty fixture produces >=5 hits (got 9)`; `6/6 passed` |

## Engine Eval Readiness (recomputed)

Inputs from `chwezi-engine-agents/docs/operations/m10-kaizen-evidence/M10-14/eval-readiness.json`
and `readiness/coverage.json`, cross-checked against the smoke run above.

| Slot | Input | Fraction |
|---|---|---:|
| T1 | 3 of 3 validators declared in `catalog/engines.yaml` pass (registry, fixture benchmark, routing smoke); re-run here, all exit 0 | 1.0000 |
| T2_p1 | 35 / 37 | 0.9459 |
| T2_neg | 21 / 21 | 1.0000 |
| T2_cov | 1 / 62 skills with ≥ 3 positives and ≥ 2 owned negatives (30 skills have any positive; 14 any owned negative) | 0.0161 |
| T2_clean | 0 undeclared of 3 cross-engine pairs ≥ 0.75 (all three `canonical_owner` or `mirrored_domain_pack`) | 1.0000 |
| T3 | 0 executed; 0 `grading.json` | 0 (`NOT_ASSESSED`) |

- T1 points = 30 × 1.0000 = 30.00
- T2 mean = (0.9459 + 1.0000 + 0.0161 + 1.0000) ÷ 4 = 2.9620 ÷ 4 = 0.7405; T2 points = 40 × 0.7405 = 29.62
- T3 points = 30 × 0 = 0.00
- **Readiness = 59.62 → 59.6.** The auditor agrees with the executor's figure.

Note: T1 is exact against the declared list but that list understates what the
engine's CI enforces; widening it would not change T1 today (all pass) but would
make T1 a stronger signal. Lexical T2 figures are a drift guard, not proof of live
routing. While T3 is unexecuted the Readiness ceiling is 70.

## NOT_ASSESSED list

| Item | Cause |
|---|---|
| T3 behavioural runs | Zero-spend rule; 0 `grading.json` files |
| Live routing (model-executed) | Zero-spend rule; lexical proxy only |
| Rendered visual quality, browser and assistive-technology behaviour | No rendered site evaluated; fixtures are lab structure checks |
| Field Core Web Vitals | Reported `NOT ASSESSED` by the benchmark itself |
| Deployment, rollback and production smoke | No deployment in scope |
| Conversion, retention and revenue outcomes | No client data |
| Skill fan-in (`skill_fanin.py`) | Not run in this audit |
| Fresh external standards verification | No web research; standards judged from the engine's own records |
| Remote CI at HEAD | Not re-queried; executor recorded success |
