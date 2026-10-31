# README kaizen record (31 October 2026)

This is a scoped cycle on one file, `README.md`, run with the Portfolio Kaizen steps: Observe, Baseline, Select, Experiment, Check, Standardise, Teach, Re-measure. Peter Bamuhigire asked for the READMEs to be "smarter and better reading overall". The cycle changed the README and the documentation index, and it added four reference pages. It touched no skill body, script or test. **It publishes no engine score.** The published score stays at the pass-2 figure (raw 62.9, capped 62.9) in the README section "Quality and improvement".

- Branch: `kaizen/2026-10-readme-kaizen`, created from `main` at `b111c0b`. The working tree was clean at the start (`git status --porcelain` printed nothing).
- Tools: two read-only scripts held outside the repository (a readability-metrics script and a preservation checker). They are not committed. Python 3.14.8, Node.js 22.23.1, PyYAML 6.0.3, and pytest 9.0.3 from a scratch virtual environment outside the checkout. Nothing was installed.

## Observe

The README was 480 lines and 9,334 words with six H2 sections and no contents list. Words per section before the change (counted by whitespace, so they differ slightly from the metrics script):

| Section (old) | Words | What made it hard to read |
|---|---:|---|
| Installation | 382 | Five long bold-labelled paragraphs. |
| Capabilities | 1,218 | A 62-row skill table after the category table. |
| Related engines | 165 | Fine. |
| Quality gates and validation | 808 | Dense tables and notes. |
| Quality and improvement | 3,395 | Calendar, open items, and a 2,587-word list of what the October cycles changed. |
| References | 3,056 | About 220 lines of citations. |

The two opening paragraphs held 168 and 127 words, with the standards, the privacy statutes and the gates in one run-on block. The first command came at line 13, after a prerequisites paragraph. Nothing near the top said which skill to use for a given job.

**What reads the README.** Found with `git grep`, not assumed:

- `scripts/validate-skill-registry.py` and `tests/test_kaizen_wave1_contracts.py` read the sentence "Its N active skills" and the category-table rows (`| `category` | N | ... |`).
- `AGENTS.md` cites the README section "Validating this repository".
- `docs/README.md` links `README.md#quality-and-improvement` and `README.md#what-the-october-2026-kaizen-improved`.
- Nothing reads the skill table, the calendar, the References section or the detailed change list.

**Baseline metrics** (before the first edit, on `main` at `b111c0b`):

| Metric | Before |
|---|---:|
| words | 9,334 |
| h2 | 6 |
| toc | 0 |
| first_cmd (line of the first fenced block) | 13 |
| longest_sec (words) | 3,500 |
| long_lines (over 300 characters) | 54 |
| max_line (characters) | 1,171 |
| sent_len (words per sentence) | 18.0 |
| fre (Flesch reading ease) | 45 |

**Baseline validators** (exit codes, all run on a Linux host): size 0, registry 0, contracts 0, routing 0 (41 of 44 first, 44 of 44 in the top three), search doctrine 0, source registers 0, portable references 0, source ingestion 0, vendored detector 0, slop pack 0, four hook tests 0, agent-integration test 0, accessibility-context test 0, drift check 0, pytest 0 (280 passed).

## Select

All eight improvements were applied. Where one was applied in part, the reason is given.

| Item | Decision |
|---|---|
| R1 Front door | Applied. Two plain paragraphs say what the engine is and who it is for. "At a glance" has six facts, each measured on 2026-10-31. "Start here" has three numbered steps with exact commands. The first fenced block is on line 22. |
| R2 Contents | Applied. A ten-link contents list follows the front door. All links resolve (see Check). |
| R3 Structure | Applied. The README now has 12 H2 sections. The longest holds 1,000 words, and it is split into H3 subsections. The largest undivided section is "Validating this repository" at 590 words; every other section or subsection is 280 words or fewer. |
| R4 Find the right skill | Applied. Twelve tasks map to 13 skills. Every skill was found with `find` and has routing prompts in `tests/routing/fixtures.json`. |
| R5 No walls of text | Applied. No paragraph or table cell is over the limits. Lines over 300 characters fell from 54 to 16. |
| R6 Plain English | Applied. Mean sentence length is 12.3 words. Terms such as slop scan, lexical proxy, CI, LCP and SRI are defined at first use. |
| R7 Say it once | Applied with one deliberate exception. The October improvements section stays (Peter asked for it) and is tightened from 2,587 to about 1,000 words. The full write-up now lives in `docs/october-2026-kaizen-changes.md`, so the summary and the detail overlap on purpose. |
| R8 Relocate bulk | Applied to four blocks (see Experiment). Each moved block passed the test: no script, test, manifest or router reads it, a summary and a link stay in the README, and the preservation check reports it as moved. |

**Not moved, and why.** The category table and the "Its 62 active skills" sentence stay because the registry validator and a test read them. The heading "Validating this repository" stays because `AGENTS.md` cites it. The two anchors that `docs/README.md` links stay. The gate and validator tables stay: they are short and are the engine's operating reference.

**Where the skeleton changed.** "At a glance" and "Start here" are H3 sections under one H2, "The short version", so that the contents list comes before the third H2 and the front door still fits in 22 lines. "Related engines" and "References" come after "Contributing, author and licence", because the brief puts engine-specific sections last. The skeleton's "Validate" section is "Quality gates and validation", with "Validating this repository" as an H3.

## Experiment

| Commit | Theme | What it changed |
|---|---|---|
| `c704a07` | Structure, front door and relocation | Rewrote the README (9,334 to 4,421 words). Added `docs/skill-catalogue.md` (the 62-row table), `docs/references.md` (all citations), `docs/date-gated-checks.md` (the calendar) and `docs/october-2026-kaizen-changes.md` (the detailed change write-up). |
| `570d13e` | Plain English | Split the long sentences in the start steps, the build order, the not-run list and the kaizen introduction. Turned the build order into a numbered list. |
| `7ad2c62` | Index | Added the four pages and this record to `docs/README.md` and updated the sentence that describes the README sections. This commit links this record before the record exists. The record commit that follows resolves the link. The validators were not run at that intermediate commit. |
| the record commit | Record | Added this file. |

**What moved where.** Moved text is verbatim except for link paths, heading levels and the words "this README", which became "the README".

| Old README block | New home | Left in the README |
|---|---:|---|
| The 62-row skill table | `docs/skill-catalogue.md` | The category table, a task table of 12 jobs, a link. |
| The References section (books, repositories, standards, websites) | `docs/references.md` | Two sentences and a link. |
| The date-trigger calendar | `docs/date-gated-checks.md` | The first failing date and a link. |
| The detailed October change list | `docs/october-2026-kaizen-changes.md` | A tightened section with the measures table and one entry per change. |

**Deliberate changes to facts.** These are corrections or additions, not copies:

1. The dependency-override entry said the override "removes that one record (15 to 13 high, zero critical)". One record cannot lower a count by two. The experiment log (`WSK-09`) says it removes "only the compression record" and lowers high records 15 to 13. The README now says it removes the compression advisory and lowers the high-severity package records from 15 to 13 (zero critical). The relocated detail page keeps the original wording.
2. "At a glance" and the tests row of the measures table now cite a pytest run of 280 of 280 on 2026-10-31 at `b111c0b` (pytest 9.0.3, Python 3.14.8). The earlier text said no pytest was available on that host.
3. The measures table said "re-measured" without saying which column. It now says that the word applies to the 31 October end figure.
4. New installer text: update, list and remove commands. A reinstall overwrites owned files and does not delete files removed upstream (read from `scripts/install-engine.js`). `list-installed` and `uninstall --engine website-skills --scope project` were run in a scratch project, together with `install.sh --scope project` and `doctor`: 504 files installed, `doctor` reported 0 missing and 0 modified, and uninstall removed 504 files.
5. New date-gate evidence: `validate-source-registers.py --as-of 2026-11-30` exits 0, and `--as-of 2026-12-01` exits 1 with 8 findings.
6. New "How it works" lines (router, build order, five layers, premium default, canonical pipeline) restate `AGENTS.md`. No new number appears in them.
7. The licence line is new: five licence parts by path (MIT, CC BY 4.0, CC BY-SA 4.0, CC BY-NC 4.0 and a proprietary layer), read from `LICENSE`. The author line omits the telephone number that the skill acknowledgement lines carry.

## Check

**Validators.** The same set was run before the first edit and after the last README edit, with the documentation index and a stub of this record in the tree. Exit codes are identical.

| Check | Before | After |
|---|---:|---:|
| `validate-checkout-size.py` | 0 | 0 |
| `validate-skill-registry.py` | 0 | 0 |
| `validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | 0 | 0 |
| `routing-smoke-test.py --min-rank1 92 --lint-fixtures` | 0 | 0 |
| `validate-search-doctrine.py` | 0 | 0 |
| `validate-source-registers.py` | 0 | 0 |
| `check_portable_references.py` | 0 | 0 |
| `source_ingestion_guardrail.py --root .` | 0 | 0 |
| `check-vendored-detector.py` | 0 | 0 |
| `node scripts/validate-slop-pack.mjs` | 0 | 0 |
| the four `hooks/test-*.js` files | 0 each | 0 each |
| `tests/agent-integration/test_website_agent_contract.py` | 0 | 0 |
| `node --test tests/a11y-gate-context.test.mjs` | 0 | 0 |
| `scripts/drift-check.sh` | 0 (615 Markdown files) | 0 (620 Markdown files; bound 650) |
| `python3 -m pytest -q tests` (scratch virtual environment) | 0, 280 passed | 0, 280 passed |

The registry validator printed `registry valid: 62 skills` and `design routes: PASS (15 routed design skills exist)` both times. Package entries rose from 851 to 856 (cap 5,000).

**Preservation check** (`main` against the branch, run after the last README edit):

```text
links: old README 88 targets; new README 24; moved to docs 70; LOST 0
commands: old README 29; kept in README 28; moved to docs 1; LOST 0
anchors: 3 README.md#<name> links in tracked files; BROKEN 0
in-page links: 13 anchors used; BROKEN 0
RESULT: OK
```

In the anchors line above, `<name>` stands for the word the checker prints in that place. Printing the literal word made the checker read this record as a link to a missing anchor, which it is not. The one moved command is the code span `git grep` in the machine-paths row of the measures table; it now sits in `docs/october-2026-kaizen-changes.md`. The 70 moved link targets are the citation URLs in `docs/references.md` and the evidence links in the detail page.

**Metrics after:**

| Metric | Before | After | Target | Result |
|---|---:|---:|---|---|
| words | 9,334 | 4,421 | at most +5%, aim -10% | Met (-52.6%). |
| h2 | 6 | 12 | none | n/a |
| toc | 0 | 1 | 1 | Met. |
| first_cmd | 13 | 22 | 40 or less | Met. |
| longest_sec | 3,500 | 1,000 | 1,500 or less, 1,200 preferred | Met. |
| long_lines | 54 | 16 | at most 27 | Met. |
| max_line | 1,171 | 458 | 700 or less | Met. |
| sent_len | 18.0 | 12.3 | 16.5 or less | Met. |
| fre | 45 | 61 | no lower than 45, aim 50 | Met (+16). |

No target was missed. The word count needs context: the README fell by 4,913 words, but four pages now hold the relocated text. The README and the four pages together run 11,444 words against 9,334 before. About 990 of the extra words are the October summary that now exists twice, on purpose, and about 730 are new front-door and overview text (the short version, contents, task table and How it works).

**Not checked.** The page was not rendered in a browser or on GitHub, so heading anchors were checked with the preservation script's slug rule, which approximates GitHub's, and not by clicking. The nested fenced blocks inside the numbered "Start here" list follow CommonMark but were not rendered. Both are `NOT_ASSESSED`. The browser gates, a completed `npm audit`, `post-deploy-smoke.sh`, `rollback.sh` against a real host and `new-project.sh` were not run, as the README already states.

## Standardise

Conventions for the next editor of `README.md`:

1. **Shape.** Title and two plain paragraphs; "The short version" (At a glance, six measured facts; Start here, three numbered steps with exact commands); Contents; Find the right skill; How it works; What is inside; Install and update; Quality gates and validation; Quality and improvement; What the October 2026 kaizen improved; Contributing, author and licence; Related engines; References.
2. **Limits.** The first fenced command within 40 lines. No section over 1,200 words. No paragraph over 90 words. No table cell over 35 words. Mean sentence length 16 words or fewer. A line over 300 characters needs a reason.
3. **Text that something reads.** Keep the sentence "Its N active skills", the category-table rows `| `category` | N | ... |`, the heading "Validating this repository", and the anchors `#quality-and-improvement`, `#what-the-october-2026-kaizen-improved` and `#find-the-right-skill`. Change one of these only with its reader, in the same commit.
4. **Where bulk goes.** Catalogues, citations, calendars and per-change write-ups live under `docs/`. The README keeps a summary and a link. Update the docs page and the README summary together.
5. **Numbers.** Re-measure any number you touch, and give the date and the command. When a skill is added or removed, update the category table, the "Its N active skills" sentence, `docs/skill-catalogue.md` and the figures in "At a glance".
6. **After editing.** Run the metrics script, the engine validators, and the preservation check against `main`.

## Teach

1. Write the front door first. A reader should know what the engine is, run one command and name the next skill within the first 40 lines.
2. Before moving a block out of the README, search for what reads it (`git grep` the file name and the heading text), then run the validators. Moving a block that a validator reads breaks the registry check.
3. Say a fact once. If a detail exists in an evidence file, link it and keep one sentence here.

## Re-measure and next cycle

- Re-run the metrics script at the next documentation wave. The targets above are the gate.
- The "At a glance" numbers (44 of 44, 41, 280, 504 files, 62.9) are copied by hand and will drift. A small check that compares them with the validators' output would prevent that. It is not built.
- Nothing checks that `docs/skill-catalogue.md` lists exactly the 62 skills in the registry. The README table is validated; the catalogue page is not. A parity check in `scripts/validate-skill-registry.py` is a candidate backlog item.
- No cross-engine mismatch was found, and no other repository was touched.
