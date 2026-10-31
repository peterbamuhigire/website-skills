# Website engine Kaizen, pass 2: scope and evidence

Assessment date: 2026-10-31. This is the second October 2026 cycle. It continues the 29 October cycle in `docs/kaizen/2026-10-engine-kaizen/`; it does not repeat it.

## Step 0: preconditions

| Item | Value |
|---|---|
| Starting branch | `kaizen/2026-10`, HEAD `c41cfcbcd79bff31a42c35a84a00702ee8f82b01`. Eighteen commits ahead of `origin/main`; never pushed. |
| Pass 2 branch | `kaizen/2026-10-pass2`, created from that HEAD with `git switch -c`. |
| Uncommitted files at start | Two modified files, both in the 29 October evidence folder: `04-validation-record.md` and `05-final-report.md`. They record the post-hoc marketplace re-run on clean commit `c41cfcb`. |
| Handling | Left exactly as found: not edited, staged, committed, stashed or reverted. Blob hashes before and after creating the branch were identical (`71b11469bf8c294e1d871e424afd07e4b1f90c1a`, `12c49b5e0a4ba852a585676fd2d1bcac9dc5fda7`). Every commit in this cycle adds explicit paths only. |
| Remote | `origin` only. No push, tag, release or pull request in this cycle. |

Read before acting: the Portfolio Kaizen Standard and the currentness gate (Digital Research engine), the router `AGENTS.md`, `skills/quality-gates/kaizen-engine-and-product-improvement/SKILL.md`, the 29 September re-audit folder, the July 2026 upgrade folder, and the 29 October cycle's final report, next-cycle file, baseline scorecard, backlog, experiment log and validation record. The 29 October open items are the primary backlog input; each was confirmed open before it was acted on or deferred.

## Environment and what could not run

This pass ran on a Linux workstation with Python 3.14, Node 22 and npm 10. The following limits apply to every result below.

- `pytest` is not installed and must not be installed. The registered test command (`python -m pytest -q`) therefore cannot run as registered; it is `NOT_ASSESSED` as registered. Fourteen of the fifteen `tests/test_*.py` files use plain pytest functions that `unittest` cannot collect. As a stand-in, a small pytest-compatible runner kept outside the checkout executed 152 test cases from those 14 files, and `unittest` ran the one `unittest` test (`tests/test_approval_adapter.py`): 153 in total, equal to the 153 the 29 October cycle reported under real pytest. This is labelled "pytest-shim" wherever it is cited and is not a pytest pass.
- The repository has no root `package.json` or lockfile. The release gates expect a consuming project with its own exact, committed lockfile (`scripts/require-locked-qa-tools.mjs`), so `npm ci --ignore-scripts` was not applicable and was not run. No package was installed.
- No Chromium or Chrome is installed. Lighthouse, axe through Playwright, visual capture and the header check that starts a preview server are therefore `NOT_ASSESSED`. Their exact failures are recorded below.
- No `sudo`, no host service change, no model call, no deployment target, no staging URL.

## Baseline validator run (fresh, before any change)

| Command | Exit | Result |
|---|---:|---|
| `python3 scripts/validate-skill-registry.py` | 0 | 62 skills; eight routed design skills found |
| `python3 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | 0 | 62 active, 1 template, zero debt |
| `python3 scripts/routing-smoke-test.py --min-rank1 92 --lint-fixtures` | 0 | 37/40 rank-1 (92.5%), 40/40 top-three, 22/22 owned negatives, lint 0 |
| `python3 scripts/website_fixture_benchmark.py` | 0 | two-page fixture passes; field CWV `NOT ASSESSED` |
| `python3 scripts/validate-search-doctrine.py` | 0 | 18 canonical files; currentness verified |
| `python3 scripts/validate-checkout-size.py` | 0 | 1,015 full and 814 package entries against 5,000; zero symlinks |
| `python3 scripts/source_ingestion_guardrail.py --root .` | 0 | zero findings |
| `python3 scripts/check-vendored-detector.py` | 0 | manifest passes (20 files); **source comparison `NOT_ASSESSED`: sibling `../chwezi-design-engine` absent** |
| `node scripts/validate-slop-pack.mjs` | 0 | 20 pack rules against 49 registry rules |
| `python3 scripts/drift_check.py --root . --as-of 2026-10-31` | 0 | 603 Markdown files |
| `hooks/test-*.js` (four files) | 0 | 61, 8, 7 and 15 cases pass |
| `python3 tests/agent-integration/test_website_agent_contract.py` | 0 | engine contract passes; the universal catalogue was present |
| `node --test tests/a11y-gate-context.test.mjs` | 0 | 2/2 |
| `bash scripts/test-banned-phrase-scan.sh` | 0 | 6/6 |
| pytest-shim over `tests/test_*.py` plus `unittest` for the approval adapter | 0 | 153 cases pass (stand-in, see above) |
| `python3 -m pytest -q` (as registered) | 1 | `No module named pytest`: `NOT_ASSESSED` |
| `a11y-gate.sh`, `perf-gate.sh`, `visual-qa.sh` in an empty project | 3, 3, 4 | `qa-tools: consuming project package.json and package-lock.json are required`: `NOT_ASSESSED` |
| `security-gate.sh` in an empty project | 2 | See defect WSK2-D1: the npm audit step reported `high=0 critical=0` after an `ENOLOCK` error |
| `slop-scan.sh`, `design-quality-score.sh` in an empty project | 5, 5 | no `dist/`: `NOT_ASSESSED` |

The detailed baseline values are frozen in `01-baseline-scorecard.md`.

## Step 1: observe

The three practitioner tasks were run from fixtures kept outside the checkout. Business facts in the fixtures are fictional and use the reserved `example.com` domain; the two credential-shaped strings in the defect fixture are the public documentation example values of two cloud providers, not credentials. No enquiry, payment, deployment or submission occurred. "Router" below means the engine's lexical routing proxy (`scripts/routing-smoke-test.py` scoring over skill names, descriptions and "Use When" text); live-model routing is `NOT_ASSESSED`.

### Task 1: five-page service site from a brief to release

**Request.** "Build a five-page website for a small bicycle repair business from this brief, with home, services, about, contact and privacy pages, and take it through every release gate with a rollback plan."

**Router choice.** `deploy` (15.9), then `policy-pages` (12.9), `security-gate` (11.8), `content-writing` (10.4), `agency-positioning` (8.7). `website-builder`, the documented orchestrator for "a complete website ... through ... deploy readiness", is not in the top five. `deploy` owns only the last stage, so the first hand-off is wrong for the most common request. Defect WSK2-D3.

**What was built.** A written brief (business facts, audience, voice, constraints, exclusions), five pages under directory routes, one stylesheet with no JavaScript, a decorative SVG mark, a 5.5 KB share image generated with the standard library, `robots.txt`, `sitemap.xml` and `.well-known/security.txt`. Total 25.7 KB. The typeface decision follows the engine precedent in `tests/gates/pass/slop-dist/styles.css`: Public Sans for text and Source Serif 4 for headings, with a system fallback and no bundled font files. The measured font weight of 0 KB is therefore not representative of a shipped site.

**Gate results on the finished site.**

| Gate | Result |
|---|---|
| `html-perf-lint.mjs` | Pass, 0 errors, 5 warnings (HPL-101). The warning names the 40 px decorative header mark as the "hero image" on every page; the LCP element is text. False positive, defect WSK2-D8. |
| `route-weight-budget.mjs` | Pass on all five routes, 2.4 to 2.7 KB each |
| `metadata-audit.sh` | Pass |
| `banned-phrase-scan.sh` | Pass, 0 hits across 26 patterns |
| `content_link_graph.py` | Pass: 5 pages, 20 edges, no broken links or orphans |
| `check-sri.sh` | Pass |
| `slop-scan.sh` | Pass: block 0, warning 0, advisory 0 |
| `scan-secrets.sh` (in a scratch git work tree) | Pass |
| `check-security-txt.sh` | **Fail, correctly.** The first draft lacked the `Policy` field the engine requires; adding it left one failure: `placeholder value found`, because the gate rejects `example.com`. A synthetic site must not pass a release gate, so this is the expected result. |
| `supply-chain-check.sh` | Exit 4: no `package.json`. A zero-dependency site has no lockfile to check; in the canonical pipeline the QA tools create one. |
| `check-security-headers.sh`, `a11y-gate.sh`, `perf-gate.sh`, `visual-qa.sh` | `NOT_ASSESSED` (exit 3): QA tools not locked in a consuming project; no browser |
| `design-quality-score.sh` | Exit 3: no scored rubric report. The rubric score is a reviewer judgement and was not fabricated. |
| `rollback.sh` with `ROLLBACK_VALIDATE_ONLY=1` | Missing authority exits 3; a mismatched target exits 3; an authorised local validation exits 0 and states that remote state is `NOT ASSESSED`. |

**Guidance gaps.** The engine has a `release-evidence` artefact whose example is an empty header (`"gates": []`), a rollback runbook and a validated rollback helper, but no complete worked deliverable showing a brief turned into pages, a gate table and a release decision. The September re-audit made the same finding (applied proof). Selected as WSK2-02.

### Task 2: small catalogue with WhatsApp enquiry and mobile-money payment

**Request.** "Build a small product catalogue website where customers send an enquiry on WhatsApp and pay by mobile money."

**Router choice.** `ecommerce` (12.2), `africa-excellence` (11.4), `retail-commerce-operating-system` (9.0). The first two are right. A narrower prompt ("Add a WhatsApp order button and MTN mobile money payment instructions to a static product catalogue page") routes first to `retail-commerce-operating-system` (12.7), then `ecommerce-checkout` (11.1), `africa-excellence`, then `ecommerce` (8.8). That is a lexical-proxy result; the 29 October guidance sits in `ecommerce`, and `ecommerce-checkout` is the skill that would add a payment integration the task does not want.

**What the engine now provides.** `skills/commerce/ecommerce/SKILL.md` (lines 42 to 46) holds the 29 October static-catalogue section: seller-owned destination, response owner and hours, manual settlement as a seller process, no invented number or link. `skills/build/page-builder/references/third-party-facades.md` holds the `wa.me` link build rules and the phrasing rule for WhatsApp usage claims.

**Where the engine has no skill or guidance to follow.**

1. No page-level pattern says what a static catalogue page may show for manual mobile-money settlement. The only pattern in `skills/orchestration/africa-excellence/references/mobile-money-ux.md` (pattern 3, "Manual paybill / merchant code", lines 64 to 79) assumes a backend: a "Paid? Enter reference number" field, webhook reconciliation, a pending state persisted in local storage. A static catalogue has none of these, so the two pieces of guidance contradict each other for this site type. Defect WSK2-D9; deferred to `06-next-cycle.md` (needs the owner's decision on a `catalogue-lite` skill, which the September roadmap proposed, rather than another reference).
2. No product-card fact list, enquiry message template carrying a product reference, or "an enquiry does not reserve stock" copy block.
3. No fixture that a catalogue page keeps price, stock and payment details out of structured data until the seller verifies them.

### Task 3: audit an existing page with deliberate defects

**Request.** "Audit this existing page for accessibility, performance, metadata and copy defects and tell me which release gates catch them."

**Router choice.** `seo-audit` (12.0), `accessibility-audit` (11.1), `french-native-copy` (9.9). A narrower accessibility prompt routes correctly to `accessibility-audit`. A copy-review prompt ("Review the page copy for filler phrases and generic AI-sounding language before launch") routes first to `launch-campaigns` (9.1), then `language-standards`, `long-form-sales-copy`; the engine's banned-phrase gate belongs to `brand-voice` and `design-quality-score`, neither of which has a single positive routing fixture. Defect WSK2-D4.

**Fixture.** One page with 24 seeded defects across accessibility, performance, metadata, copy, security and links.

| Seeded defect | Offline gate result |
|---|---|
| Two render-blocking head scripts (one third party) | Caught: HPL-001 twice; route weight reports the third-party script against a zero budget |
| Image with no width and height | Caught: HPL-002 |
| `document.write` | Caught: HPL-004 |
| `loading="lazy"` on the hero image | **Missed** here: the hero has no dimensions, so the lint cannot rank it and picks a smaller image. HPL-002 still fails the page. Recorded as a limitation. |
| 420 KB hero image | **Missed** by the weight gate because the image is lazy and so not counted as first-load weight. The same limitation. |
| Description of 2 characters | Reported as WARN only; the file header says a description "must" be 50 to 165 characters. Recorded as WSK2-D7. |
| Missing canonical, `og:title`, `og:image` | Caught: three FAIL lines |
| Title `Home` | Not flagged; the written rule only requires a non-empty, distinct title |
| Banned phrases: welcome framing, "cutting-edge", "seamless", "world-class", "passionate about", "take your business to the next level", "In today's fast-paced digital world" | Caught: 8 hits by the banned-phrase scan and three headline rules by the slop scan |
| Inter as primary font; purple gradient | Caught by the slop scan (blocking) |
| `outline: none` with no replacement; heading level skipped | Caught by the slop scan (warnings) |
| External script without `integrity` or `crossorigin` | Caught: two SRI failures |
| Live-looking payment and cloud keys in inline script | Caught by the secrets scan (two) |
| No `security.txt` | Caught |
| Broken internal link | Caught by the link graph |
| `<html>` without `lang` | **No offline gate.** The browser-based axe gate would report `html-has-lang`; it could not run here. Defect WSK2-D6. |
| Viewport meta with `user-scalable=no, maximum-scale=1` | **No offline gate.** Axe `meta-viewport` would report it; not run. |
| Image without `alt`; text at `#999` on white; input with no label; "Click here" link text; clickable `<span onclick>` | `NOT_ASSESSED` offline: these depend on the axe gate (the 29 October run, with a browser, detected one critical and two serious findings on a similar fixture). |
| `http://` image on an HTTPS page; `target="_blank"` without `rel` | **No gate** checks either. Recorded for the next cycle. |

## Defects

| ID | Severity | Location | Finding |
|---|---|---|---|
| WSK2-D1 | **Critical** | `scripts/security-gate.sh` lines 40 to 43 | The dependency-audit step fails open. `npm audit --json` is allowed to fail (`|| AUDIT_EXIT=$?`), the counts are read with `jq ... \|\| echo 0`, and `AUDIT_EXIT` is never used. When npm cannot audit (no lockfile, registry unreachable), the error JSON has no `vulnerabilities`, both counts become 0 and the log prints `npm audit high=0 critical=0`. A release gate must treat an audit that did not run as a failure. |
| WSK2-D2 | Major | `scripts/check-vendored-detector.py` lines 38 and 144 | The default sibling is `../chwezi-design-engine`, so on a checkout that sits beside `design-system-skills` the source comparison reports `NOT_ASSESSED` by default. The 29 October cycle fixed the same mismatch in the registry validator (`53dddac`) but not here. No configurable root exists. |
| WSK2-D3 | Major | `skills/orchestration/website-builder/SKILL.md` line 3 (description) and the "Use When" list | A plain whole-site build request does not rank `website-builder` in the top five. |
| WSK2-D4 | Major | `tests/routing/fixtures.json` | 30 of 62 skills have no positive fixture; two (`deploy`, `ecommerce`) meet three positives and two owned negatives. A copy-review request routes to `launch-campaigns`. |
| WSK2-D5 | Major | Active content: `AGENTS.md` lines 61, 74, 371, 561; `rules/common/core.md` line 10; `MEMORY.md` line 8; `docs/standards-register.md` line 4; `docs/source-registers/search-ai-currentness-2026-09-05.json` line 205; and 18 skill files (the list is in `01-baseline-scorecard.md`) | 26 machine-specific absolute paths (`C:\wamp64\www\...` and `C:/wamp64/www/...`) in active engine content. One resolves to a file that no longer exists in the design engine (`skills/orchestration/website-experience-mapping/references/innovation-sprint-dvfs-reframe-and-assumption-testing.md` line 5). A further 41 sit in history documents and client prompts. No validator checks any of them. |
| WSK2-D6 | Minor | `scripts/metadata-audit.sh` | No static check for `<html lang>` (WCAG 3.1.1, level A) or a viewport meta that blocks zoom. Both are covered only by the browser-based axe gate. |
| WSK2-D7 | Minor | `scripts/metadata-audit.sh` lines 7 and 55 to 61 | The header says a description "must" be 50 to 165 characters; the code warns only. Whether too short should fail is a threshold decision for the owner. |
| WSK2-D8 | Minor | `scripts/html-perf-lint.mjs` (HPL-101) | A page whose only image is a small decorative mark gets a "hero image" warning on every page. |
| WSK2-D9 | Minor | `skills/orchestration/africa-excellence/references/mobile-money-ux.md` lines 64 to 79 | Manual-settlement pattern assumes a backend; contradicts the static-catalogue route (see Task 2). |
| WSK2-D10 | Minor | `skills/orchestration/africa-excellence/references/african-language-pack.md` lines 7 and 14 to 25 | "10 first-class African languages" while only French and Kiswahili have native-copy skills; the speaker figures carry no source. |
| WSK2-D11 | Minor | `docs/standards-register.md` rows 12, 13, 14, 16, 19, 20 | Six rows have a `Next review` date before 2026-10-31 (2026-10-01 for five, 2026-08-01 for structured data). Only the JSON registers are machine-checked. |
| WSK2-D12 | Minor | `.skills-engine/engine-manifest.yaml`; `.github/workflows/skill-engine-quality.yml` | Registered test command needs `pytest`; 14 of 15 `tests/test_*.py` files cannot be collected by `unittest`. Not a defect in CI (it installs pytest); a portability limit on hosts without it. |

## Points where guidance was missing, contradictory or ignored

- **Missing:** a worked end-to-end site (WSK2-02); a static-catalogue page pattern (WSK2-D9); static `lang` and viewport checks (WSK2-D6); mixed-content and `rel` checks.
- **Contradictory:** the manual mobile-money pattern against the static-catalogue route (WSK2-D9); the metadata header against its implementation (WSK2-D7); "10 first-class languages" against two native-copy skills (WSK2-D10).
- **Ignored:** the engine's own "no machine-specific absolute paths" principle (WSK2-D5), and its "unavailable check is not a pass" principle, in the security gate (WSK2-D1).
