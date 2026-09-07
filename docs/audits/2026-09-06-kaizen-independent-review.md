# Independent website fixture review, 6 September 2026

Disposition updated 7 September 2026: the P2 overflow finding and blank-metadata
gaps are CLOSED by the authorised narrow repair below. The zero-budget
response-shape mismatch is also CLOSED after the main owner's correction;
the full suite now passes all 38 tests.
Image-path coverage is unchanged. Fixture PASS is not a browser or website-release
verdict. The original review evidence below is historical.

## Scope and evidence

Reviewed the working-tree diff of
[benchmark](../../scripts/website_fixture_benchmark.py) and
[tests](../../tests/test_website_fixture_benchmark.py), plus the fixture and budget
inputs. Read root AGENTS, relevant manifest routes, local Kaizen/adoption,
authoring/style and safety-review instructions. The Kaizen and safety skills
kept remediation separate from this read-only review and missing outcome evidence
explicit. Preflight: `NO_TIME_SENSITIVE_CLAIMS`; no external research or other
repository access was needed.

Baseline HEAD: `4a7cdb0728adecc12f908dc0549f34151a53e433`.
Inspected SHA-256:

- Benchmark: `4B34088C784CE67C07704F80AB74CFE1C44CA896F1AB280E1A05B7E547309FC0`.
- Tests: `C9A1C6F20BE17C4A3C05FE1B8B2905915DD6D36DD5A5DF10A3CAA81ECB008E65`.

| Check | Observed result | Exit |
|---|---|---:|
| `python -B -X utf8 -m pytest tests/test_website_fixture_benchmark.py -q -p no:cacheprovider` | 8 passed; includes two deterministic CLI runs | 0 |
| In-memory CLI probe matrix | 39 cases: 30 structured FAIL, 5 PASS, 4 uncaught exceptions | 0 (probe harness, not gate approval) |
| In-memory nested/enumerated-asset probes | Baseline 2,104 bytes; nested 1 MiB adds exactly 1,048,576 bytes and fails budget; enumerated outside asset rejected | 0 |
| Scoped `git diff --check` | No whitespace errors | 0 |

The probe matrix replaced `Path.read_text` responses and invoked `main()` with
captured stdout. Asset probes mocked enumeration/stat for a nested asset and
enumeration of an existing outside-fixture repository file. No probe edited
fixture files. Native tests used their existing temporary copies. Real filesystem
symlink/junction traversal was NOT ASSESSED; mocked enumeration does not prove it.

## Original P2: extreme budgets escape the structured failure handler (closed)

At benchmark lines 109–111, `math.isfinite` raises `OverflowError` for the valid
JSON integer `10**400` in any of the three required budget fields. Separately,
`total_weight_kb = 1e308` passes the finite-number check but multiplication at
line 117 overflows before `int(...)` completes. Line 148 does not catch
`OverflowError`. Each of these four probes produced an uncaught exception and
empty stdout instead of a JSON FAIL record. Consumers parsing stdout cannot
recover the expected finding. The large-integer failure occurs in newly added
validation; the finite-float multiplication weakness was already present.

Reproduction: independently replace one field in an in-memory copy of
`performance-budgets.json`, return its JSON from the budget-file read, then call
`main()`. Use `10**400` for each required key and `1e308` for `total_weight_kb`.

Acceptance: define numeric range/conversion handling and return structured FAIL
for unsupported magnitudes without traceback. Add CLI regressions for these four
cases, ordinary positive values and boundary handling. Existing tests contain no
custom-budget cases. Owner: main benchmark/test maintainer; code change requires
separate authorisation.

## Confirmed controls and retained limits

- Empty/non-list catalogues, duplicate resolved page aliases and an existing
  absolute page outside the fixture fail. Escaping anchor links also fail.
- Removing a description makes both page metadata and aggregate status FAIL.
  Nested assets contribute to the raw-byte ceiling. Malformed budget roots,
  missing keys, booleans, zero, negative, string, null, NaN and infinity fail.
- Two of the five probe passes were finite `1e308` JS/CSS budgets: these satisfy
  the current positive-number contract. They are not measured gzip results.
- The other three passes expose retained coverage limits: whitespace-only title,
  whitespace-only description, and `<img src="../../AGENTS.md" alt="test">`.
  Lines 68/85 check metadata presence/truthiness, not meaningful text; line 56
  inspects only anchor/link `href`, not image/script `src`. These are pre-existing,
  not aggregation or page-catalogue regressions. Narrow any assurance accordingly;
  require separate regressions if nonblank metadata or all-resource confinement
  becomes the intended contract. The image target was not fetched by this probe.

The original review wrote only this report. Browser rendering, accessibility outcomes, measured
performance, Core Web Vitals, production traffic, conversion and release authority
remain NOT ASSESSED. No numeric readiness score is inferred. Re-review the budget
finding after the main owner's correction; broader engine release gates were not
run for this two-file independent review.

## Authorised repair disposition, 7 September 2026

- Overflow CLOSED: numeric validation and raw-ceiling conversion translate
  `OverflowError` into a descriptive `ValueError`, which the existing CLI handler
  reports as JSON FAIL with exit 1. No arbitrary new budget ceiling was introduced;
  finite checks remain; the subsequent zero-budget correction below permits
  non-negative limits.
- Blank metadata CLOSED: the parser records text only while inside a title;
  metadata requires nonblank title text and stripped description content. Empty,
  whitespace, nonbreaking-space entities and comment-only title cases fail.
  Body text does not satisfy the title check. Split title text/entities and a
  padded nonblank description still pass. This is text-presence validation, not
  a browser-equivalent HTML parser or a judgement about copy quality.
- Added 15 regression cases: four overflow CLI cases, three exact-byte budget
  boundaries, six blank-metadata cases, one comment/body isolation case and one
  valid text-chunk/entity case. Before the repair, the expanded focused suite
  recorded 10 failed and 13 passed, exit 1; after repair, 23 passed, exit 0.
- Before the main owner's zero-budget correction,
  `python -B -X utf8 -m pytest -q -rs -p no:cacheprovider`: **36 passed, 1 failed**,
  exit 1. `tests/test_kaizen_wave2.py:87` expects `performance_budget_inputs` for
  zero budgets. The already-reviewed finite-positive validation rejects zero
  through the short JSON error shape, which lacks that key. That validation
  branch predates this repair. The unrelated test was not edited by this sidecar.
  This historical failure is superseded by the verification below.
- `python -B -X utf8 scripts/website_fixture_benchmark.py`: PASS, exit 0;
  unchanged fixture totals 2,104 bytes. Scoped diff check passes.

Edits were limited to the benchmark, its named test file and this report using
`apply_patch`. Tests mutate temporary copies/custom budgets only; boundary tests
also verify fixture bytes remain unchanged by the benchmark. Existing main-worker
changes were preserved. Image/script path checks and broader browser scope were
not changed. The image-path limitation above remains OPEN; all browser, field and
release-authority limits remain NOT ASSESSED.

## Zero-budget re-verification, 7 September 2026

Disposition: CLOSED. The main owner's finite non-negative budget contract treats
zero as a legitimate no-byte allowance. The existing all-zero fixture mutation
now returns `performance_budget_inputs.status = FAIL` rather than the short
invalid-input error shape. The added negative/boolean/string-limit test also
passes; overflow and metadata regressions remain passing.

Re-ran `python -B -X utf8 -m pytest -q -rs -p no:cacheprovider` from the repository
root: **38 passed**, exit **0**. This re-verification changed only this report;
no code edits were made. Image-path and browser-outcome dispositions are unchanged.
