# Re-vendor the slop detector after the banned-font gate change, 6 November 2026

## Why

The design engine's banned-font gate (`hooks/lib/font-matcher.js`) now counts a quoted banned family name only where it is used as a font (action DG6, design engine commits `0398cdf`, `afbce48`, `44d06bd` and `05f6fb8`). This engine carries a vendored, hash-checked copy of that matcher under `scripts/vendor/chwezi-slop/`, so the copy had drifted from its source.

## Before

`python3 -X utf8 scripts/check-vendored-detector.py --source <design engine checkout>` exited 1: manifest PASS (20 files, source commit `72a3a37`), source comparison `DRIFT differs from source: hooks/lib/font-matcher.js`.

## Change

`python3 -X utf8 scripts/check-vendored-detector.py --sync-from <design engine checkout>` ("synced 20 files ... at `05f6fb8`"). The diff is exactly two files:

- `scripts/vendor/chwezi-slop/hooks/lib/font-matcher.js`: the design engine's DG6 change (+104, -9).
- `scripts/vendor/chwezi-slop/VENDOR.json`: the new SHA-256 of that file and `source_commit` `05f6fb8f70a4f19119eb4a57bb069fd0a3540377`.

The other 19 vendored files are unchanged.

## After (2026-11-06, Linux, Python 3.14.10, Node 22)

| Command | Result |
|---|---|
| `check-vendored-detector.py --source <design engine checkout>` | exit 0: manifest PASS (20 files), source comparison PASS |
| `check-vendored-detector.py --no-source` | manifest PASS; source comparison `NOT_ASSESSED` (as in a consuming project) |
| `node scripts/validate-slop-pack.mjs` | PASS: 20 pack rules checked against 51 registry rules |
| `validate-skill-registry.py` | `registry valid: 62 skills` |
| `pytest -q -p no:cacheprovider` | 280 passed |
| `validate-checkout-size.py`, `check_portable_references.py` | PASS, PASS |

## Effect on this engine

`scripts/slop-scan.sh` and the visual QA gate use the vendored detector's static rules. A quoted banned-family name in a script is no longer reported unless it is used as a font; real font declarations (CSS, run-font assignments, font-named setters) are still reported. The matcher's behaviour was verified in the design engine (131 of 131 hook tests); this engine's own gates were not re-run against a rendered site.

## Not assessed

Browser gates (`perf-gate.sh`, `a11y-gate.sh`, `visual-qa.sh`) need a consuming project with locked tools and were not run.
