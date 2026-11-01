# Website Skills Engine

The Website Skills Engine is a library of agent skills for planning, writing, building, auditing, launching and maintaining static websites. It builds sites from markdown content and approved assets, and it works in Claude Code and Codex. Its 62 active skills cover eleven categories, and every release passes executable checks (scripts that run, not checklists).

It is for website agencies, freelance developers, and in-house marketing and product teams. It pays particular attention to East African markets: constrained bandwidth, mobile money and local languages. Use it when you plan, write, build, audit, launch or maintain a site, or when you run a web agency.

## The short version

### At a glance

- **62 skills** in 11 categories, each at `skills/<category>/<skill>/SKILL.md`.
- **Three copy languages:** English, French and Kiswahili. French and Kiswahili have their own native-copy skills.
- **Executable release gates:** performance, accessibility, security, visual QA, slop scan (a detector for banned fonts, gradients and filler copy) and post-deploy smoke checks. A gate never passes when it could not run.
- **Routing:** the right skill is in the top three for 44 of 44 test prompts and first for 41. This is a lexical proxy (it matches words, not meaning), not live routing.
- **Tests:** 280 of 280 pytest tests pass (pytest 9.0.3, Python 3.14.8, 2026-10-31).
- **Audit score:** 62.9 of 100, against a cap of 65 and a target of 95. A score never overrides a blocked release gate.

### Start here

1. **Load the engine.** In Claude Code, add the marketplace and install the plugin. It carries all 62 skills. For Codex, or for a clone and installer, see [Install and update](#install-and-update).

   ```text
   /plugin marketplace add https://github.com/peterbamuhigire/website-skills
   /plugin install website@chwezi-website
   ```

2. **Check the catalogue.** In a clone of this repository, run the registry validator. It ends with `registry valid: 62 skills`.

   ```sh
   python3 -X utf8 scripts/validate-skill-registry.py
   ```

3. **Ask for a job in plain words.** The router in `AGENTS.md` sends a whole-site request to `website-builder`. For example: "Build a complete premium company website from client documents and assets through deploy readiness." Other jobs are in [Find the right skill](#find-the-right-skill).

## Contents

- [Capabilities](#capabilities)
- [Find the right skill](#find-the-right-skill)
- [How it works](#how-it-works)
- [What is inside](#what-is-inside)
- [Install and update](#install-and-update)
- [Quality gates and validation](#quality-gates-and-validation)
- [Quality and improvement](#quality-and-improvement)
- [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved)
- [Contributing, author and licence](#contributing-author-and-licence)
- [Related engines](#related-engines)
- [References](#references)

## Signup security default

For public signup forms, use Cloudflare Turnstile Managed mode with server-side token validation to reduce bot-driven and other unauthorised automated use. Native Android signup uses Firebase App Check with Play Integrity and a Turnstile WebView fallback when expected attestation is unavailable. See the [signup human-validation reference](skills/build/page-builder/references/signup-human-validation.md).

## Capabilities

The engine holds 62 skills in 11 categories, grouped under [What is inside](#what-is-inside). The [skill catalogue](docs/skill-catalogue.md) lists each one. The table under Find the right skill is the capability map: common tasks and the skill that handles each.

### Find the right skill

Name the job in plain words and the router picks the skill. These twelve jobs are a starting point. Every skill named here has routing test prompts in `tests/routing/fixtures.json`.

| You want to | Use |
|---|---|
| Build a whole site from a brief, through release | `website-builder` |
| Decide what a premium site offer includes, or when to decline a bid | `premium-website-product` |
| Map the visitor journey before page structure | `website-experience-mapping` |
| Set typography, colour, spacing, motion and component tokens | `design-system` |
| Turn approved copy and tokens into responsive pages | `page-builder` |
| Add locale routes, language switching and hreflang | `i18n` |
| Write French or Kiswahili that reads as native | `french-native-copy` or `swahili-native-copy` |
| Research and draft a cited blog article | `blog-writer` |
| Implement metadata, structured data and sitemaps | `seo` |
| Check a site against WCAG 2.2 AA, the W3C accessibility guidelines | `accessibility-audit` |
| Check headers, dependencies, secrets and `security.txt` before release | `security-gate` |
| Publish, smoke-test and prove rollback readiness | `deploy` |

Other jobs, such as e-commerce, retainers, monthly reports, policy pages and audits, are in the [skill catalogue](docs/skill-catalogue.md). Design, typography, colour and UX work belongs to the design engine (see [Related engines](#related-engines)).

**What it does not do.** A skill or a passed checklist is evidence for review, not a certificate of a live site's results. Field performance, legal compliance and conversion claims still need their own evidence.

## How it works

- **One router.** `AGENTS.md` is the runner-agnostic router. `CLAUDE.md` imports it. A skill's `SKILL.md` is the portable unit of execution. Detail sits in its `references/` folder, and repeatable helpers sit in `scripts/`.
- **A fixed build order.** `website-builder` runs the sequence below. Steps 2, 3 and 10 apply only when their condition holds.
  1. `i18n`
  2. `design-reference`, when reference sites are part of the brief
  3. `brand-strategy`, when a brand brief is needed
  4. `chwezi-design-engine:sector-strategies`, or a sector-specific skill
  5. `design-system`
  6. `photo-manager`
  7. `page-builder`
  8. `seo`
  9. `deploy`
  10. `seo-audit`, when a post-build audit is needed
- **Five layers.** Commercial (qualification, offers, proposals), strategy (discovery, trust, search intent), build (design system, images, pages, SEO), launch (QA, deployment, rollback, observability) and governance (training, cadence, metrics, safety review).
- **One pipeline.** Every project ships through the canonical continuous integration (CI) pipeline in `templates/ci/website.yml`, installed by `scripts/install-canonical-ci.sh`. A failed gate blocks deploy.
- **Premium by default.** Work is accepted only when it can be delivered as a credible business asset. If the brief cannot support that, the engine recommends paid discovery, a smaller scope, or a no-bid or no-build decision.

## What is inside

### Categories

The table is generated from `skills/*/*/SKILL.md` (62 files; no aliases or templates are counted) and matches `skills/manifest.yml`. Each skill, with a one-line description, is in the [skill catalogue](docs/skill-catalogue.md).

| Category | Skills | Coverage |
|---|---:|---|
| `agency-ops` | 14 | Agency positioning, offers, sales, delivery, support, reporting, retention and referrals |
| `brand` | 2 | Brand strategy and brand storytelling |
| `build` | 6 | Reference analysis, design systems, internationalisation, pages and image assets |
| `commerce` | 5 | Store strategy, checkout, funnels, analytics and omnichannel retail |
| `content-copy` | 11 | Page, blog, sales and long-form copy; voice; English, French and Kiswahili standards |
| `launch-ops` | 4 | Deployment, experimentation, measurement and observability |
| `meta` | 3 | Skill writing, skill safety review and router documentation |
| `orchestration` | 6 | End-to-end website delivery, experience mapping, premium, hospitality and African-market builds |
| `quality-gates` | 6 | Accessibility, visual QA, design quality, consistency, security and Kaizen review |
| `seo-search` | 3 | SEO implementation, SEO audit and Google AI search |
| `ux-conversion` | 2 | Conversion audit and buyer-question content |
| **Total** | **62** | |

### What it produces

- Strategy and positioning briefs, sitemaps and page specifications.
- Website copy in English, French and Kiswahili.
- Design tokens and component rules.
- Production pages with structured data and analytics event maps.
- Scaffolded multilingual static-site projects.
- Accessibility, security, SEO, conversion and design-quality audit reports.
- Release evidence with rollback plans.
- Privacy and terms pages, monthly client reports, and retainer and referral programmes.

### Standards it follows

- **Accessibility:** WCAG 2.2 AA with the WAI-ARIA Authoring Practices.
- **Security:** OWASP ASVS 5.0.0 (Application Security Verification Standard) for verifiable controls, the OWASP Top 10:2025 for threat awareness, and RFC 9116 for `security.txt`.
- **Search:** Google Search Essentials and the Google structured-data guidelines, with Schema.org.
- **Performance:** the Core Web Vitals thresholds published on web.dev.
- **Privacy:** the Uganda Data Protection and Privacy Act 2019, the Kenya Data Protection Act 2019, POPIA, the Nigeria Data Protection Act 2023 and the GDPR.

### Beyond the skills

- **Gates:** performance budgets enforced through Lighthouse CI, an accessibility gate built on axe-core, security and supply-chain checks, visual regression, and a slop scan run by a vendored copy of the `chwezi-slop` detector.
- **Worked example:** `examples/service-site-five-page/`, a complete deliverable with its release record, gate table and rollback plan.
- **Certification:** a syllabus and exam for operators, in `certification/`.

## Install and update

### Prerequisites

- **Node.js 18 or later** for the installer. `install.sh` and `install.ps1` exit without it.
- **Python 3.11 or later** for the validators and the Codex model-policy helper, which imports `tomllib`.
- **`PyYAML`** for the routing, contract and agent-integration checks, and **`pytest`** for the test suite. The repository has no requirements file, so install both yourself. CI installs them unpinned on Python 3.12 and runs the slop-pack and hook tests on Node.js 22.
- **Git** for the manual route, for `new-project` scaffolding, and because one test and the drift check read the Git index.

The counts in this README were measured on 2026-10-31 with Python 3.14.8, PyYAML 6.0.3, pytest 9.0.3 and Node.js 22.23.1.

### Claude Code plugin

The repository ships `.claude-plugin/marketplace.json` (marketplace `chwezi-website`) and `.claude-plugin/plugin.json` (plugin `website`, version 1.1.0, all 62 skills). The two install commands are in [Start here](#start-here).

The plugin registers three hooks from `hooks/hooks.json`:

- a Bash pre-check that blocks recognised destructive commands until the operator separately approves an override (`hooks/destructive-bash-gate.js`);
- an advisory quality gate after file edits (`hooks/quality-gate.js`; set `CHWEZI_QUALITY_GATE_PROFILE` to `minimal`, `standard` or `strict`);
- a documentation drift check when a response ends (`hooks/drift-check-hook.js`).

### Installer

Both entry points delegate to `scripts/install-engine.js`. It copies the engine into `~/.claude` (`--scope user`, the default) or `./.claude` (`--scope project`) and records ownership in `.chwezi/install-state.json`. It also accepts `--dry-run` and `--json`.

```sh
git clone https://github.com/peterbamuhigire/website-skills
cd website-skills
./install.sh --scope project        # macOS, Linux or Git Bash
.\install.ps1 --scope project       # Windows PowerShell
node scripts/install-engine.js doctor --scope project
```

Add `--dry-run` to `install.sh` to list the files first (504 on 2026-10-31); nothing is written. Run `doctor` from the project folder that holds the `.claude` folder.

**Update.** Pull this checkout and run the installer again. It overwrites the files it owns. It does not delete files that were removed upstream, so uninstall first if you want an exact copy.

**List or remove.** `node scripts/install-engine.js list-installed --scope project` lists installed engines. `node scripts/install-engine.js uninstall --engine website-skills --scope project` removes only the files the installer wrote, and it stops if any were modified unless you pass `--force`. Both commands ran in a scratch project on 2026-10-31.

### Codex

Codex reads `AGENTS.md`. Its Codex-only section runs `.codex/ensure_model_policy.py --runtime codex --check` with Python 3.11 or later (`python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`). Add `--apply` only when drift is reported. `--check` only reads. With `--runtime claude` the helper prints `NOT_APPLICABLE` and exits 0, and Claude skips that section.

### Manual route

Clone the repository and point the agent at `CLAUDE.md`, which imports `AGENTS.md`, the runner-agnostic router. To start a client site, copy `new-project.sh` (or `new-project.ps1`) into an initialised Git repository and run it. It adds this engine as a submodule at `.claude/skills/`, creates the `en`, `fr` and `sw` content folders, and copies the content templates.

## Quality gates and validation

### The release gates

The gate scripts run against a built site, from the root of a consuming project:

- `scripts/perf-gate.sh` (budgets in `performance-budgets.json`, Lighthouse configuration in `lighthouserc.json`)
- `scripts/a11y-gate.sh`
- `scripts/security-gate.sh`
- `scripts/visual-qa.sh`
- `scripts/slop-scan.sh`, which uses the vendored detector in `scripts/vendor/chwezi-slop/`, verified by `scripts/check-vendored-detector.py`
- `scripts/post-deploy-smoke.sh`

Set `SKILLS_DIR` to this checkout; reports go to the project's `reports/` folder. A gate never downloads its tools and never passes when it could not run.

| Gate | Needs in the consuming project | Stops with, when it is missing |
|---|---|---|
| `perf-gate.sh` | a locked `@lhci/cli` in `package.json` and `package-lock.json`; Lighthouse drives a browser | exit 3 |
| `a11y-gate.sh` | locked `serve`, `@playwright/test` and `@axe-core/playwright`, and a browser Playwright can drive | exit 3 |
| `visual-qa.sh` | locked `@playwright/test`; it also runs `slop-scan.sh` | exit 4 |
| `security-gate.sh` | `jq`, `npm`, a lockfile and registry access for `npm audit` | exit 6 (an audit that did not complete is a failure, not zero findings) |
| `slop-scan.sh` | Node.js 18 or later; no network | exit 5 |
| `post-deploy-smoke.sh <url>` | `curl` and a deployed HTTPS URL | exit 3 |
| `metadata-audit.sh <dist>`, `html-perf-lint.mjs <dist>`, `drift-check.sh` | nothing beyond Bash, Node.js, Python and Git | not applicable |

### Validating this repository

Run these from the repository root. They match `.github/workflows/skill-engine-quality.yml` and the validators declared in `.skills-engine/engine-manifest.yaml`.

| Command | What it checks | Needs |
|---|---|---|
| `python3 -X utf8 scripts/validate-checkout-size.py` | the 5,000-entry caps for the full checkout and the package, and manifest parity | Git |
| `python3 -X utf8 scripts/validate-skill-registry.py` | the skill total and category counts in this README against the filesystem and relocations, and that the 15 routed design skills exist | design engine checkout for the last check; without one it is `NOT_ASSESSED` |
| `python3 -X utf8 scripts/validate-skill-contracts.py --baseline quality/skill-contract-baseline.json` | the zero-debt skill contract | PyYAML |
| `python3 -X utf8 scripts/routing-smoke-test.py --min-rank1 92 --lint-fixtures` | a lexical routing proxy over `tests/routing/fixtures.json`, not live routing | PyYAML |
| `python3 -X utf8 scripts/validate-search-doctrine.py` | the search doctrine files and their currentness register, judged by today's date (no `--as-of` option) | none |
| `python3 -X utf8 scripts/validate-source-registers.py [--as-of YYYY-MM-DD]` | expired or malformed review dates in `docs/standards-register.md` and `docs/source-registers/*.json` | none |
| `python3 -X utf8 scripts/check_portable_references.py` | machine-specific paths and broken relative links | none |
| `python3 -X utf8 scripts/source_ingestion_guardrail.py --root .` | rejects book-dump folders | none |
| `python3 -X utf8 scripts/check-vendored-detector.py` | the hash manifest of the vendored detector, then a comparison with the design engine | design engine checkout for the comparison |
| `node scripts/validate-slop-pack.mjs` | the website slop pack against the vendored registry | Node.js |
| `for t in hooks/test-*.js; do node "$t" \|\| exit 1; done` | the four hook test files | Node.js |
| `python3 -m pytest -q` | the test suite | pytest, PyYAML and a Git checkout |

**Notes on running them**

- **The design engine is found, not assumed.** The vendored-detector check and the registry validator look for it through `--source`, then `CHWEZI_DESIGN_ENGINE_ROOT`, then `CHWEZI_ENGINES_ROOT` (a folder of checkouts), then the folders beside this checkout. They try `design-system-skills` and `chwezi-design-engine`. When none is found the comparison is `NOT_ASSESSED`, which is reported and is never a pass.
- **Re-vendoring the detector is a reviewed step.** Run `python3 -X utf8 scripts/check-vendored-detector.py --sync-from <design engine checkout>`. It refuses a source with uncommitted changes and rewrites `scripts/vendor/chwezi-slop/VENDOR.json`. Review the diff, then rerun the slop-pack validator, the tests and the worked example's slop scan.
- **pytest is a hard prerequisite.** `python3 -m unittest discover -s tests` is not a substitute: on 2026-10-31 it ran 10 tests and failed to import nine modules that import `pytest`. The pytest run needs a Git checkout, not an exported archive, because `tests/test_kaizen_wave2.py::test_drift_check_is_bounded_and_repeatable` calls `git ls-files`. It takes one to two minutes.
- **Two checks are not collected by pytest and are not CI steps.** Run `python3 -X utf8 tests/agent-integration/test_website_agent_contract.py` (it reads the engine manifest) and `node --test tests/a11y-gate-context.test.mjs` directly.
- **Declared and CI-run validators differ.** The manifest declares eight validators: registry, skill contracts, routing, search doctrine, source registers, portable references, source ingestion and tests.
  - The CI workflow runs the size, portable-reference, contract, routing, search-doctrine, source-register, vendored-detector, slop-pack, hook and pytest steps.
  - `source-ingestion-guardrail.yml` runs the ingestion guardrail.
  - `validate-skill-registry.py` is declared but is not a CI step.
- **Date-based checks fail on a future date unless sources are re-verified.** See [Date-gated checks](#date-gated-checks).

**Not run on a plain Linux host without a locked project:**

- the browser gates (`perf-gate.sh`, `a11y-gate.sh`, `visual-qa.sh`);
- a completed `npm audit`;
- `post-deploy-smoke.sh`;
- `rollback.sh` against a real host;
- `new-project.sh`, which clones the published repository over the network.

Run each of them in a consuming project with the locked tools installed.

## Quality and improvement

The engine follows the Portfolio Kaizen Standard. It is a cycle of measure, change, check and record, with a published audit score capped at 65 out of 100 and a plan that targets 95.

The evidence for the October 2026 cycles is in two folders:

- [`docs/kaizen/2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/README.md) holds the 29 October cycle.
- [`docs/kaizen/2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/README.md) holds the 31 October cycle (pass 2).

Each holds the frozen baseline, backlog, experiment log, validation record, final report and next-cycle file. Earlier records are indexed in [`docs/README.md`](docs/README.md). The documentation wave's own follow-ups are in [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md). The commits of both cycles are on `main`; on 2026-10-31 none had been pushed.

### Latest published score

Pass 2 ([final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md)) scored the engine at raw 62.9 out of 100. The capped score, `min(raw, 65)`, is also 62.9, so the cap does not bind. The pass-2 baseline was 55.7 and the 29 October final was 60.0.

The target of 95 is not met, and these scores do not override a blocked release gate. The worked example is blocked for release on purpose. The standing blockers for the engine are:

- the Lighthouse CI dependency tree;
- the lab largest contentful paint (LCP) of a font-using site;
- visual capture specs;
- staging-edge header proof;
- counsel review of privacy wording.

The pass-2 test host could not run real pytest or any browser gate. A real pytest run on a clean clone on 2026-10-31 (pytest 9.0.3) passed 280 of 280 tests. No browser gate was run in that check.

### Open items that matter to a user

These are the highest priority (P0) in [`06-next-cycle.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md).

1. **The vendored detector was behind the design engine.** The pass-2 report records the default check exiting 1 with `DRIFT` on three files. Commit `ae6487c` re-synced it to design-engine commit `72a3a37`, and the check now exits 0.
   - The sync added two rules: positive `tabindex` and minimum target size.
   - A positive `tabindex` now fails `slop-scan.sh`. The target-size rule is browser tier, so that scan does not run it.
   - The item stays on the P0 list because `06-next-cycle.md` is a frozen record.
   - Whether the website slop pack needs entries for the two rules is undecided.
2. **The Lighthouse CI dependency tree is not remediated or re-audited.** `@lhci/cli` 0.15.1 was still the latest release on 2026-10-31 and pins Lighthouse 12.6.1, while Lighthouse is at 13.6.0. The 29 October audit of the disposable QA dependency tree found 15 high-severity package records and no critical record. That is not a count of unique advisories or a statement about every production dependency.
3. **The lab LCP of a font-using five-page site is above the unchanged 2,000 ms assertion.** The worked example bundles no fonts, so it cannot test this.

Also open, and relevant when you rely on a skill:

- The privacy-statute checks are identifier-level, and three rest on search summaries. The Nigerian NDPR and NDPA naming is inconsistent across five files.
- The static-catalogue page pattern and the manual mobile-money wording need an owner decision.
- 30 of the 62 skills have no positive routing fixture.
- The provenance of one register record, `LOCAL_CARTER_EPUB_2026`, is unresolved.
- Routing results are a lexical proxy, not live-model evidence.

### Date-gated checks

Two currentness validators fail once a recorded review date passes. The first failures come on 2026-12-01. Four standards-table rows and one register with three claims reach their review date on 2026-11-30 (`--as-of 2026-11-30` exits 0, `--as-of 2026-12-01` exits 1 with 8 findings). Moving a date needs a source check behind it.

The full calendar, with the records behind each date, is in [`docs/date-gated-checks.md`](docs/date-gated-checks.md). The next-cycle file also sets a monthly backlog review on 2026-11-30 and a full engine audit with the 65 cap on 2027-01-31.

## What the October 2026 kaizen improved

Two cycles ran in October 2026.

- The first, on 29 October, is recorded in its [final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md) and [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md).
- Pass 2, on 31 October, is recorded in its [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md), [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md), [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md) and [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md).

Everything below was kept, and each code change has its own commit. Neither report records a reverted experiment.

Every hash of this repository is on `main`, checked with `git merge-base --is-ancestor` and `git show --stat`. `7582bbf` and `72a3a37` are design-engine commits, confirmed there with a read-only `git cat-file`.

In the Basis column, **re-measured** means the 31 October end figure was run again on 2026-10-31 on `main` at `8c2d59b`. Every other figure is copied from the evidence file named beside it. The write-up of each change, with the check behind it, is in [`docs/october-2026-kaizen-changes.md`](docs/october-2026-kaizen-changes.md).

### Measures

| Measure | 29 Oct start | 29 Oct end | 31 Oct start | 31 Oct end | Basis |
|---|---:|---:|---:|---:|---|
| Score, raw (of 100) | 55.5 | 60.0 | 55.7 | 62.9 | Copied from the scorecards. A judgement, not a measurement. |
| Score, capped `min(raw, 65)` | 55.5 | 60.0 | 55.7 | 62.9 | Copied. The cap never binds and the target of 95 is not met. |
| Routing, rank-1 precision | 35/37 (94.6%) | 37/40 (92.5%) | 37/40 (92.5%) | 41/44 (93.2%) | **Re-measured**, `routing-smoke-test.py`, exit 0, 44/44 in the top three. A lexical proxy. |
| Owned routing negatives passing | 21 | 22 | 22 | 24 | **Re-measured**, same run: 24 of 24. |
| Tests passing | 130 (1 failed) | 153 | 153 | 280 | Copied. The 29 October counts are real pytest; the 31 October pass used a stand-in runner. A pytest 9.0.3 run at `b111c0b` on 2026-10-31 passed 280 of 280. |
| Machine-specific paths in active content | not measured | not measured | 25 | 0 | **Re-measured**, `check_portable_references.py` exit 0. History documents keep 47 paths at fixed ceilings. |
| Routed design skills the registry check verifies | none found by default | 8 | 8 | 15 | **Re-measured**, `validate-skill-registry.py` exit 0. |
| Overdue review dates | 2 claims | 0 claims | 6 standards rows | 0 | **Re-measured**, `validate-source-registers.py` and `validate-search-doctrine.py` exit 0. No validator read the standards table before 31 October. |

The 31 October start score is below the 29 October end score because the fresh look found defects the first cycle had not measured.

### Defects fixed, most serious first

- **The security gate failed open (critical, `f548bb3`).** With no lockfile or registry access, `scripts/security-gate.sh` read npm's error as zero findings and printed `npm audit high=0 critical=0`. It now stops with exit 6. Five of nine new tests failed on the old script; all nine pass.
- **The accessibility gate crashed on every page (`e510d6b`).** The runner now creates an explicit browser context and page. `node --test tests/a11y-gate-context.test.mjs` passes 2 of 2. The earlier browser run is copied from the 29 October record, not repeated.
- **The subresource integrity (SRI) check misread canonical links (`e85a746`, `ebce413`, `430ad66`).** `check-sri.sh` treated a canonical URL as an external asset. It now parses script and stylesheet assets and requires a correctly sized digest and `crossorigin`. Ten SRI tests.
- **The metadata audit passed pages that fail WCAG (`0a28183`).** It now fails a missing `<html lang>`, a zoom-locking viewport, and a `maximum-scale` below 2. Eleven of 18 new tests failed on the old script; all 18 pass.
- **The language pack claimed more than the engine can produce (`51931d2`).** "First-class" now requires a native-copy skill. Only Kiswahili has one; the other nine languages are layout-supported only. Speaker figures are labelled unsourced and `NOT_ASSESSED`.
- **The hero lint named logos as hero images (`f936529`).** Images of 64 px or less in both dimensions are no longer ranked. Warnings on the five-page example fell from 5 to 0.

### The vendored detector and new checks

- **The design engine is found, not assumed (`53dddac`, `38c9bb1`, `bd71a48`).** `scripts/design_engine_root.py` resolves it through `--source`, `CHWEZI_DESIGN_ENGINE_ROOT`, `CHWEZI_ENGINES_ROOT`, then both sibling folder names. Eleven tests cover each branch.
- **The detector was re-synced (`ae6487c`).** The registry went from 49 to 51 rules, and the default check went from exit 1 to exit 0. One behaviour changed: a positive `tabindex` is now a blocking warning in `slop-scan.sh`.
- **Machine paths and broken links are checked (`0b29417`).** `scripts/check_portable_references.py` runs in CI. Active findings went from 25 to 0.
- **Checkout and package size are capped (`7c2a181`, `4733227`, `dbc8b69`).** `scripts/validate-checkout-size.py` fails closed at 5,000 entries.
- **A worked deliverable exists (`a63a05b`).** [`examples/service-site-five-page/`](examples/service-site-five-page/README.md) is a synthetic site. Its test injects eleven defects and each is caught. The applied-proof score rose from 25 to 40, a judgement.

### Routing, currentness and documentation

- **A whole-site request now reaches `website-builder` (`af0ad1e`).** The prompt ranks third of 62 and rank-1 precision rose from 92.5% to 93.2%. Thirty of 62 skills still have no fixture.
- **A static catalogue with manual settlement has guidance (`4351295`).** The cost is recorded: rank-1 precision fell from 94.6% to 92.5%, so the router did not improve on that measure. The page pattern is still an owner decision.
- **The standards register has an expiry check (`e52de53`).** Six rows were past their review dates and no validator read the table. All were re-verified on 2026-10-31, and Schema.org 30.0 became 30.1 and Lighthouse 13.5.0 became 13.6.0.
- **Overdue Google Search and model records were refreshed (`8cfb82f`, `1940e21`, `b6e5cdb`).** `validate-search-doctrine.py` went from failing to passing.
- **A dependency override is documented (`1a02b98`).** Overriding `serve`'s `compression` to 1.8.2 removes the compression advisory and lowers the high-severity package records from 15 to 13 (zero critical). The gate still blocks.
- **The documentation matches the repository (`6d88f51`, `565963c`, `d89c769`, `4624a48`, `9fdebd0`, `1c7e007`, `8c2d59b`).** The README, `docs/README.md`, `CONTRIBUTING.md`, `AGENTS.md` and the relocation map were brought up to date.

None of this changes the score, the release blockers or the open items above.

## Contributing, author and licence

**Contributing.** [`CONTRIBUTING.md`](CONTRIBUTING.md) lists the steps and the local gates. In short: read `AGENTS.md` and `docs/skill-authoring-standard.md`, start a new skill from `templates/skill/SKILL.md`, update the routing fixtures when routing changes, and run the validators in [Validating this repository](#validating-this-repository). Never store book extractions or book summaries in the repository.

**Author.** Peter Bamuhigire, [techguypeter.com](https://techguypeter.com).

**Licence.** The repository carries four open licences by path (MIT, CC BY 4.0, CC BY-SA 4.0 and CC BY-NC 4.0) and a proprietary layer. `LICENSE` summarises them and `docs/licensing-matrix.md` is authoritative.

## Related engines

This repository owns website strategy, build, launch and retainer work. Other engines own the neighbouring work. A skill or router line names them through the engine-routing table of the machine, never by a path.

- **Design.** [`chwezi-design-engine`](https://github.com/peterbamuhigire/chwezi-design-engine) (held in a folder called `design-system-skills` on some machines) owns typography, colour, layout and the anti-slop doctrine. The skills relocated there (`color-selection`, `ux-psychology`, `form-ux-design`, `brand-style-guide`, `brand-visual-identity`, `sector-strategies`, `legal-sector-ui-ux`) are listed in [`docs/relocation-map.md`](docs/relocation-map.md).
- **Proposals.** [Proposal Skills](https://github.com/peterbamuhigire/proposal-skills) owns proposal, tender and commercial wording. It is an external engine, and this repository does not embed it. An earlier submodule was removed in commit `37780ba`, and `docs/licensing-matrix.md` records it as separately licensed.
- **Social campaigns.** [Social Media Skills](https://github.com/peterbamuhigire/social-media-skills) hands over landing-page briefs through `ad-to-site-journey-handoff`. `launch-campaigns` receives them.
- **Research and currentness.** The Digital Research engine supplies the currentness gate and the research method that every blog post and every standards claim must pass.
- **Engineering standard.** [`chwezi-dev-engine`](https://github.com/peterbamuhigire/chwezi-dev-engine) holds the canonical skill-writing standard and the `quick_validate.py` and `engine_compliance.py` checks used in `CONTRIBUTING.md`.

## References

The citations behind the engine's skills are in [`docs/references.md`](docs/references.md): books, repositories studied in the September 2026 ten-repository Kaizen, standards and official sources, and websites and articles.

Book methods are paraphrased into task-oriented references with a short attribution. Book extractions and book summaries are never stored in this repository (see `docs/continuous-improvement/book-source-retirement-2026-09-24.md`).
