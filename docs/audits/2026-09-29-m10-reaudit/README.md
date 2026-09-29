# Website engine: M10-14 measured re-audit (29 September 2026)

Independent measured re-audit of `website-skills` at committed HEAD `ec72bca`
(62 active skills, 11 categories). The embedded or externally resolved
`proposal-skills` engine is out of scope.

## The numbers

| Number | Score /100 | Basis |
|---|---:|---|
| **Engine Eval Readiness (measured)** | **59.6** | T1 30.00 + T2 29.62 + T3 0 (`NOT_ASSESSED`, zero-spend rule) |
| Raw overall | **55.3** | Judged dimensions, with routing judged at 62 |
| Measured-constrained overall | **55.2** | Routing replaced by Readiness 59.6 |
| **Published overall** | **55.2** | `min(55.2, 65)`; the 65 cap does not bind |

Weighting: output-type readiness 30, skill depth and worked examples 25,
standards currency 15, taxonomy 10, doctrine 10, hygiene 10 (hygiene = mean of
redundancy, discovery/routing and safety). No dimension, group, skill or output
type scored 70 or above.

## Verdict

The website engine is a disciplined, well-gated catalogue that is visibly short
of world-class. Its contract layer is uniform (zero contract debt across 62
skills), its executable gates are real and tested (131 tests, a hash-checked
vendored slop detector, a fixture benchmark, a search-doctrine currentness
check), and its doctrine of refusing unassessed evidence is consistent. What
holds it in the mid-50s is applied proof: every skill's worked example is a
one-to-three-sentence scenario rather than an artefact, the `examples/` folder
holds one service-page prototype, the fixture sites are two-page lab fixtures,
and no behavioural (Tier 3) run exists. Routing precision is high on a lexical
proxy, but only 1 of 62 skills meets the fixture-coverage bar. E-commerce-lite
and African-language delivery beyond French and Kiswahili are the weakest output
types. The prior 6 September audit published no numeric score; this is the first
measured baseline.

## Files

| File | Contents |
|---|---|
| [00-executive-summary.md](00-executive-summary.md) | Verdict, headline findings, strengths, path to the bar |
| [01-methodology-and-rubric.md](01-methodology-and-rubric.md) | Method, commands, rubric, weighting, limitations, independence |
| [02-coverage-and-taxonomy.md](02-coverage-and-taxonomy.md) | Taxonomy score and named deficiencies |
| [03-existing-groups-audit.md](03-existing-groups-audit.md) | Per-group scores and 21 sampled per-skill scores |
| [05-per-output-type-readiness.md](05-per-output-type-readiness.md) | Eight output types, scored and ranked |
| [09-master-scorecard.md](09-master-scorecard.md) | All 11 dimensions, labels, groups, output types, the three numbers |
| [10-roadmap-to-world-class.md](10-roadmap-to-world-class.md) | P0/P1/P2 moves with target scores |
| [11-measured-evidence.md](11-measured-evidence.md) | Commands, exit codes, output lines, Readiness arithmetic, `NOT_ASSESSED` list |

- `04-gap-analysis-new-skills.md`: not re-run in the M10-14 measured re-audit (missing skills are named in 02 and 10).
- `06-standards-benchmark.md`: not re-run in the M10-14 measured re-audit (no fresh external research).
- `07-hardening-existing-skills.md`: not re-run in the M10-14 measured re-audit (hardening moves are named in 10).
- `08-reading-list.md`: not re-run in the M10-14 measured re-audit.
