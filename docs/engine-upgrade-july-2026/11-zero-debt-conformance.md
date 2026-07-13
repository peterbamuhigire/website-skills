# July 2026 Zero-Debt Conformance Record

Date: 13 July 2026

Benchmark: canonical `skills-web-dev` skill-writing, composition, engine-audit, anti-slop, and AI-slop-audit contracts.

## Scope and before state

Filesystem discovery found one active root, `skills/`, containing 59 active `SKILL.md` files. No inactive alias files or skill templates were mixed into the active count. The pre-change canonical scanner reported 0 fully compliant skills and 395 findings:

| Finding | Before |
|---|---:|
| Capability contract | 56 |
| Decision rules | 59 |
| Degraded mode | 58 |
| Five anti-patterns | 34 |
| Frontmatter YAML | 2 |
| Identity mismatch | 3 |
| Input contract | 59 |
| Output contract | 2 |
| Portable metadata | 59 |
| Portable sections | 5 |
| Trigger | 58 |

The causes were a pre-July portable skeleton with generic list inputs and outputs, descriptions that did not act as triggers, absent permission and degraded-mode contracts, and two unquoted YAML descriptions containing colons.

## Implemented cohorts

- Agency operations and brand.
- Build, commerce, and conversion.
- Content, native-language copy, and launch operations.
- Meta, orchestration, quality gates, and search.
- Shared authoring standard, template, validator, zero-debt baseline, routing fixtures, smoke test, CI, and maintainer documentation.

Domain guidance, acknowledgement lines, directly linked references, examples, and repository taxonomy were preserved. No skill was added, removed, renamed, or deactivated to improve a score.

## Final evidence

Final machine results at release:

| Check | Final result |
|---|---|
| Local contract validator | Pass: 59 active skills, one template, zero findings |
| Routing fixtures | Pass: 28/28 expected skills in the top three (100%) |
| Canonical engine scanner | Pass: 59/59 fully compliant, zero findings |
| Canonical quick validator | Pass: 59/59 skill directories |
| Repository tests | Pass: 5 tests |
| Syntax and limits | Pass: 18 shell scripts, workflow YAML, JSON fixtures, maximum entrypoint 249 lines |
| Diff check | Pass |
| AI slop audit | A — clean: no blocking finding; the sole lexical hit was the precise technical name `screenshot-diff-harness.md`; repeated pre-July filler was removed |

## Outside conformance debt

Production-equivalent benchmark packs, independent client and specialist review, calibration rounds, and 30/90-day outcome telemetry remain capability and evidence expansion. They do not waive or reopen structural skill conformance.
