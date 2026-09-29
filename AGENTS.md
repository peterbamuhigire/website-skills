# Repository Agents Guide

## Codex-only model setup and Kaizen review

Apply this section only when the active runner is Codex. Claude and other
runners must skip it and retain their own models and full engine capabilities.

Before substantive Codex work, resolve this engine's directory and an available
Python 3.11+ interpreter (use its absolute path if absent from PATH), then run
`python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`.
If it reports configuration drift, Peter authorises the bounded
`--runtime codex --apply` repair, followed by `--check`. The helper backs up
changes and preserves unrelated settings. If Python or configuration access is
unavailable, report the limitation; do not replace the user's config wholesale.
Read `.codex/model-policy.md` for the full contract. Use Luna (`gpt-6-luna`) with high reasoning by
default for orchestration, research, audit, review, and implementation. Use Astra (`gpt-6-astra`) only when
Peter explicitly selects it for the task; never select or fall back to GPT-5.6. Report unavailable required GPT-6
models. A running session may need restarting for root settings to apply.


Every Kaizen cycle MUST check latest official model releases and actual
runtime availability, record dated evidence and a retain/change decision,
and evaluate better candidates before recommending replacement. Preserve the
pins until Peter authorises a verified change. Missing model-currentness
evidence is `NOT_ASSESSED`. This Codex adapter must not change CLAUDE.md,
Claude configuration, domain doctrine, permission settings or skill access.

## Universal agent integration

See `.skills-engine/engine-manifest.yaml` for the declarative contract used by the optional universal coordination package. The router and domain SKILL.md files remain authoritative.

The package may read the router, discover skills, inspect Git, and run only declared checks. Missing evidence is NOT ASSESSED; writes, pulls, publication, submissions, ledger/filing changes, deployment, or control changes require explicit approval.

Project context: if the working project root holds a `PROJECT.md` with `project_schema: 1`, read it before planning. It points to this engine's own context sources and never replaces them.

## Rules

Book extractions, book summaries and raw book text must never be stored in this
repository (owner rule, 2026-09-24). Convert a book's method into a
task-oriented skill reference in original words with a brief citation; route
volatile claims through the Digital Research currentness gate. The removed
`book-extractions/` folder's capability map is in
`docs/continuous-improvement/book-source-retirement-2026-09-24.md`.

Turn a book's method into a task-oriented skill reference (procedure, checklist,
template, decision rules, phrase bank) written in original words, cite the book
briefly (author, year, title, publisher), and keep verbatim quotes under 25 words
and rare. The former `book-extractions/` folder was removed on 2026-09-24.
`scripts/source_ingestion_guardrail.py` rejects any file placed in a
`book-extractions/`, `book-dumps/`, `raw-books/` or `source-books/` directory.

Always-on cross-cutting principles live in `rules/` — see `rules/README.md`.
Load `rules/common/core.md` alongside the routed skill for any non-trivial task;
it is short and does not replace the skill, only sets the baseline the skill
operates within.

## Mandatory Digital Research currentness gate for Kaizen

Every Kaizen audit, skill edit, reference update, validator change, and
standardisation decision MUST begin with the Digital Research Engine at
`C:\wamp64\www\digital-research-engine`. Read its `source-evaluation` and
`source-verification` skills and the currentness gate reference
`docs/continuous-improvement/kaizen-currentness-gate.md`.

Before admitting any standard, policy, law, technology, platform capability,
software version, command, security control, benchmark, or lifecycle claim,
record source scope, publication/version date, access date, freshness class,
review date, support status, and uncertainty. Use current authoritative
primary sources; quarantine stale/ambiguous/unsupported claims and mark them
`NOT_ASSESSED`. Books are durable concept inputs only.

The shared agent, command, hook, evidence, and handoff contract is mapped to
website work in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md);
the central registry lives in `C:\wamp64\www\chwezi-dev-engine\docs\engine-control-plane.json`.

## Purpose

This repository is a portable skill library for building websites and related marketing assets.

- In Claude Code, the repository is typically consumed as a skill library inside a client project.
- In Codex, portable skills live under `skills/<category>/<skill-name>/SKILL.md` across 11 thematic categories (agency-ops, brand, build, commerce, content-copy, launch-ops, meta, orchestration, quality-gates, seo-search, ux-conversion).
- `SKILL.md` is the portable execution unit.
- Detailed domain material belongs in `references/`.
- Deterministic helpers belong in `scripts/`.

Do not assume this repository must live under `.claude/skills/`. Resolve local skills by repository-relative paths such as `skills/orchestration/website-builder/SKILL.md` or `skills/build/design-system/SKILL.md`; resolve relocated design skills such as `sector-strategies` through `skills/manifest.yml` and the global engine-routing table. The repository root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant; root-level operational directories such as `scripts/`, `templates/`, `tests/`, and `tools/` are not skills unless they contain their own `SKILL.md`.

It teaches agents to build static websites from markdown content and assets; it is not a standalone application.

It is referenced from the global engine-routing table in client website projects. Claude Code and Codex should resolve the local checkout and consume `skills/<category>/<skill-name>/SKILL.md` directly.

The repository now operates as a portable agency system with explicit layers for:

- qualification and intake
- strategy and research
- build and SEO
- launch and rollback operations
- governance and operator onboarding

Claude-specific projects may still point at this repository from their own configuration, but the repository should not be treated as dependent on `.claude/skills/` or any nested submodule path.

## Baseline Rules

- Preserve existing Claude Code behavior unless a task explicitly requires a change.
- Premium is the default commercial standard for this website engine. Website work is accepted only when it can be delivered as a credible business asset with premium strategy, content, SEO, UX, technical quality, measurement, and handover. If the brief cannot support that standard, recommend paid discovery, a smaller premium scope, or a no-bid/no-build decision.
- Website work must be framed and delivered as a credible business asset: strategy, world-class content, SEO/GEO, premium UX, conversion architecture, technical quality, measurement, handover, and post-launch improvement.
- Prefer the skill-local `SKILL.md` first, then load only the specific files needed from that skill's `references/`.
- Every `SKILL.md` must include this exact acknowledgement line immediately below the first top-level `# ...` heading, not in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- Treat `references/legacy-guidance.md` as preserved detailed guidance from the pre-standardized version of the skill.
- Do not bulk-load every reference file in a skill. Read only what the current task needs.
- Use bundled scripts when they are the safest or most repeatable path.
- Keep outputs implementation-oriented. Avoid abstract summaries when a concrete deliverable is expected.
- Author or normalise active skills against `docs/skill-authoring-standard.md` and start new entries from `templates/skill/SKILL.md`.
- Before releasing any skill-engine change, run the zero-debt contract validator, routing smoke test, registry validator, tests, canonical per-skill quick validator, and canonical engine scanner. A missing or unavailable check is not a pass.
- When search, AI-answer visibility, crawler policy, structured data, or
  webmaster reporting changes, also run `scripts/validate-search-doctrine.py`.

## Routing

Use these skills as the default router:

- `premium-website-product`: Default premium website product layer. Use for every revenue-critical website and for agency-side positioning where website design itself must be sold as a premium, market-making service.
- `website-builder`: Full website orchestration from docs and assets through deploy readiness.
- `i18n`: Language routing, multilingual structure, and shared versus locale-specific rules.
- `design-reference`: Extracting decisions from example websites.
- `chwezi-design-engine:sector-strategies` or `chwezi-design-engine:legal-sector-ui-ux`: Sector-specific patterns and trust signals.
- `design-system`: Typography, palette, motion, spacing, and visual system decisions.
- `photo-manager`: Image cataloging, naming, dimensions, and logo selection.
- `page-builder`: Converting content and design decisions into pages and reusable UI.
- `seo`: Implementation of metadata, schema, sitemaps, crawler controls, and
  the layered cross-platform discoverability model: SEO foundation, answer
  clarity, probabilistic GEO, entity presence, and post-discovery SXO.
- `google-ai-search`: Official Google Search guidance for AI Overviews, AI Mode,
  AEO/GEO mythbusting, Search Console measurement, local/ecommerce readiness,
  and agentic-experience preparation.
- `skills/seo-search/google-ai-search/references/ai-search-response-mode-planning.md`:
  qualified concept input for response-mode planning, entity clarity, outcome
  separation, and reversible experiments; it never supplies current platform facts.
- Do not route ambiguous “AIO” or model-training placement as a separate ranking
  system. Separate training, live retrieval, citation, representation, referral,
  and conversion outcomes.
- `deploy`: Build verification, deployment artifacts, and release readiness. Owns the canonical CI pipeline at `templates/ci/website.yml` and its troubleshooting reference.
- `accessibility-audit`: WCAG 2.2 AA enforcement gate — axe-core, manual checklist, screen-reader smoke scripts. Runs in the canonical CI pipeline as a hard gate.
- `visual-qa`: Rendered-output review loop — Playwright screenshot diff, heading/overflow/empty-section assertions, AI-slop scan. Runs in the canonical CI pipeline as a hard gate.
- `security-gate`: Dependency audit, security headers, `security.txt`, SRI, secrets scan, supply-chain, and Africa + GDPR compliance matrix. Runs in the canonical CI pipeline as a hard gate.
- `observability`: RUM, error tracking, analytics, and alerting contract for every shipped site. Feeds `dashboards/quality-scorecard.md`.
- `experimentation`: Hypothesis template, statistical-significance primer, A/B infrastructure (GrowthBook default), quarterly review.
- `design-quality-score`: 7-category rubric and slop-scan. Runs as canonical CI step 12 (advisory on PR, blocking on main).
- `africa-excellence`: Africa-realistic pattern layer (low-bandwidth, mobile-money UX, USSD-aware, language pack, trust signals, cultural patterns).
- `premium-ui-ux-design`: Premium website UX and visual-quality layer. Use before design-system/page-builder on premium, lead-generation, ecommerce, high-ticket, or public proof work.

Use these cross-cutting skills whenever their lens materially improves the output:

- `language-standards`: Regional language and tone quality; owns the cross-language consistency policy and routes French and Kiswahili to their native-copy skills.
- `french-native-copy`: Native-quality French copywriting execution. Mandatory for any French page, microcopy, email, or metadata; never produce French by raw translation.
- `swahili-native-copy`: Native-quality Kiswahili copywriting execution. Mandatory for any Kiswahili page, microcopy, email, or metadata; never produce Kiswahili by raw translation.
- `premium-commercial-writing`: Premium-fee-worthy commercial writing across website copy, landing pages, blogs, SEO/GEO pages, documents, and offer pages.
- `content-writing`: Website copy structure and clarity.
- `chwezi-design-engine:brand-visual-identity`: Audience and brand coherence (brand-consistency gate reference).
- `sales-copywriting`: Conversion-focused messaging.
- `chwezi-design-engine:form-ux-design`: Any user-input flow.
- `chwezi-design-engine:ux-psychology`: Behavioural and heuristic UX review.

Use these support skills on demand:

- `blog-idea-generator`, `blog-writer`
- `brand-strategy`, `brand-storytelling`, `brand-style-guide`
- `color-selection`
- `policy-pages`
- `email-sender`
- `ecommerce`, `retail-commerce-operating-system`, `ecommerce-funnel`, `ecommerce-checkout`, `ecommerce-analytics`
- `agency-positioning`, `agency-client-retention`, `monthly-report`
- `they-ask-you-answer`, `social-media`
- `seo-audit`, `cro-audit`
- `skill-writing`, `skill-safety-audit`, `update-claude-documentation`
- `observability`, `experimentation`, `design-quality-score`, `africa-excellence`

Premium agency operating-system skills (added 2026-05-05):

- `website-experience-mapping`: outside-in alignment diagrams, journey maps,
  experience maps, ecosystem maps, mental-model diagrams. Run before
  page-builder on every premium build that must change behaviour.
- `service-blueprint-website-delivery`: frontstage / backstage blueprint for
  the agency's own delivery operations, SLAs, and recovery. Use during
  proposal scoping, kickoff, and every retainer review.
- `premium-sales-conversation`: structured premium discovery and objection
  handling. Use before any quote, proposal, or scoping document.
- `customer-service-website-ops`: post-launch service language, triage,
  escalation, recovery, retention. Use to design SOPs, train support, and
  recover trust after incidents.
- `marketing-measurement-system`: KPI tree, customer insight loop, loyalty
  layer, and quarterly business review that drives budget reallocation.
- `local-in-person-acquisition`: in-person, door-to-door client acquisition for a
  niche studio — territory and cadence, the free-audit door-opener, walk-in pitch
  and objection scripts, follow-up sequence, pipeline KPIs. Use to run the
  "go in person" channel after the niche is chosen in `agency-positioning`.
- `referral-program`: generous, systematic client referrals — reward structures,
  ask scripts and timing, cross-niche/partner routing, formal tracking and the
  ethics check. Use once clients reach the Advocate phase.
- `delivery-automation`: the agency's own tooling, reusable assets, and workflow
  automation for faster/cheaper delivery — build-vs-buy, the automation-opportunity
  audit, the honest AI-assisted-delivery reality, productized-delivery SOPs.

## Repository Structure

### Skill Categories

Skills are organised under `skills/<category>/<skill>/` in 11 thematic categories:

- **`agency-ops/`** (14) — agency-client-retention, agency-positioning, authority-offers, customer-service-website-ops, delivery-automation, email-sender, launch-campaigns, local-in-person-acquisition, monthly-report, policy-pages, premium-sales-conversation, referral-program, service-blueprint-website-delivery, social-media
- **`brand/`** (2) — brand-storytelling, brand-strategy
- **`build/`** (6) — design-reference, design-system, i18n, image-compression, page-builder, photo-manager
- **`commerce/`** (5) — ecommerce, retail-commerce-operating-system, ecommerce-analytics, ecommerce-checkout, ecommerce-funnel
- **`content-copy/`** (11) — blog-idea-generator, blog-writer, brand-voice, content-writing, east-african-english, french-native-copy, language-standards, long-form-sales-copy, premium-commercial-writing, sales-copywriting, swahili-native-copy
- **`launch-ops/`** (4) — deploy, experimentation, marketing-measurement-system, observability
- **`meta/`** (3) — skill-safety-audit, skill-writing, update-claude-documentation
- **`orchestration/`** (6) — africa-excellence, hospitality-website-product, premium-ui-ux-design, premium-website-product, website-builder, website-experience-mapping
- **`quality-gates/`** (6) — accessibility-audit, cross-page-design-consistency-audit, design-quality-score, kaizen-engine-and-product-improvement, security-gate, visual-qa
- **`seo-search/`** (3) — google-ai-search, seo, seo-audit
- **`ux-conversion/`** (2) — cro-audit, they-ask-you-answer

Always reference skills by their full categorised path: `skills/<category>/<skill>/SKILL.md`.

### Core Build Skills

```text
skills/build/i18n/SKILL.md               <- Multi-language infrastructure
skills/content-copy/language-standards/SKILL.md <- Language and tone standards
skills/content-copy/french-native-copy/SKILL.md <- Native-quality French copy execution
skills/content-copy/swahili-native-copy/SKILL.md <- Native-quality Kiswahili copy execution
skills/content-copy/content-writing/SKILL.md    <- Copywriting standards
chwezi-design-engine:brand-visual-identity <- External brand coherence quality gate (brand-consistency gate reference)
skills/build/design-reference/SKILL.md   <- Reference-site analysis
chwezi-design-engine:sector-strategies  <- External industry design and trust signals
skills/orchestration/website-builder/SKILL.md    <- Master orchestrator and system owner for operating references
skills/build/design-system/SKILL.md      <- Fonts, colours, visual identity, motion
skills/build/photo-manager/SKILL.md      <- Asset cataloguing, logo selection, image organisation
skills/build/page-builder/SKILL.md       <- Content to pages and components
skills/seo-search/seo/SKILL.md                <- Search-facing implementation
skills/seo-search/google-ai-search/SKILL.md   <- Google AI Overviews / AI Mode readiness
skills/content-copy/blog-writer/SKILL.md        <- Blog production
skills/launch-ops/deploy/SKILL.md             <- QA, launch checks, deployment, rollback, canonical CI pipeline
skills/orchestration/premium-website-product/    <- Premium website-as-product strategy, content, SEO, stack, launch, and agency proof gate
skills/orchestration/premium-ui-ux-design/       <- Premium website UI/UX and visual quality gate
```

### Enforcement Skills (Phase 10 — added 2026-04-16)

```text
skills/quality-gates/accessibility-audit/SKILL.md <- WCAG 2.2 AA gate: axe-core + manual + screen reader
skills/quality-gates/visual-qa/SKILL.md           <- Screenshot diff + hierarchy/overflow/empty-section + AI-slop
skills/quality-gates/security-gate/SKILL.md       <- Dep audit + headers + security.txt + SRI + secrets + supply chain + compliance
```

### Operating Discipline Skills (Phase 11 — added 2026-04-16)

```text
skills/launch-ops/observability/SKILL.md        <- RUM + error tracking + analytics + alert thresholds
skills/launch-ops/experimentation/SKILL.md      <- Hypothesis template + stat primer + A/B infra + quarterly review
skills/quality-gates/design-quality-score/SKILL.md <- 7-category rubric + slop-scan (CI step 12)
```

Phase 11 also adds: `glossary.md` (canonical names), `docs/doc-style-guide.md`
(writing standards), `docs/deprecation-policy.md` (rename/retirement rules),
`certification/` (syllabus + 60-question exam + cohort records), and
`dashboards/quality-scorecard.md` (generated-artefact contract).

### Authority Skills (Phase 12 — added 2026-04-16)

```text
skills/orchestration/africa-excellence/SKILL.md    <- Low-bandwidth, mobile-money UX, USSD-aware,
                                 language pack, trust signals, cultural patterns
```

Phase 12 also adds: `LICENSE` (MIT + CC BY + CC BY-SA + CC BY-NC + proprietary),
`docs/licensing-matrix.md`, `docs/roadmap-public.md`, and
`dashboards/public-scorecard.md` (quarterly public quality record).

Canonical scripts under `scripts/`: `perf-gate.sh`, `a11y-gate.sh`,
`visual-qa.sh`, `security-gate.sh`, `drift-check.sh`, `slop-scan.sh`,
`design-quality-score.sh`, `install-canonical-ci.sh`, `metadata-audit.sh`,
`post-deploy-smoke.sh`, `rollback.sh`, and gate-specific helpers.
Canonical configs at repo root: `lighthouserc.json`, `performance-budgets.json`.
Canonical CI pipeline at `templates/ci/website.yml`.

### Support And Audit Skills

```text
skills/seo-search/seo-audit/SKILL.md               <- Post-build SEO audit
skills/content-copy/blog-idea-generator/SKILL.md     <- Blog ideation
skills/agency-ops/email-sender/SKILL.md            <- Self-hosted contact-form handler
chwezi-design-engine:form-ux-design                    <- External form UX guidance
chwezi-design-engine:ux-psychology                     <- External behavioural UX review lens
skills/build/image-compression/SKILL.md       <- Build-time image compression
skills/agency-ops/policy-pages/SKILL.md            <- Privacy and terms guidance
chwezi-design-engine:color-selection                  <- External colour palette design
skills/content-copy/sales-copywriting/SKILL.md       <- Persuasion and conversion copywriting
skills/brand/brand-strategy/SKILL.md          <- Brand brief development
skills/brand/brand-storytelling/SKILL.md      <- Narrative and story structure
chwezi-design-engine:brand-style-guide                <- External client-facing style guide
skills/ux-conversion/cro-audit/SKILL.md               <- Conversion audit
skills/agency-ops/social-media/SKILL.md            <- Social strategy and service layer
skills/meta/skill-writing/SKILL.md           <- Skill authoring
skills/meta/skill-safety-audit/SKILL.md      <- Skill safety review
skills/meta/update-claude-documentation/     <- Top-level documentation maintenance
```

### External Skill Set

```text
proposal-skills <- Separate proposal-generation engine resolved from the global routing table
```

## Skill Execution Order

Website build skills are sequential:

1. `i18n`
2. `design-reference` when reference sites are part of the brief
3. `brand-strategy` when a project needs a structured brand brief
4. `chwezi-design-engine:sector-strategies` or a sector-specific skill
5. `design-system`
6. `photo-manager`
7. `page-builder`
8. `seo`
9. `deploy`
10. `seo-audit` when post-build auditing is needed

`website-builder` orchestrates this sequence. It reads the enabled-language setup, the client content set, and the available assets, then routes work through the relevant downstream skills.

Cross-cutting skills such as `language-standards`, `content-writing`, and `chwezi-design-engine:brand-visual-identity` (brand-consistency gate) apply throughout the workflow instead of owning a single output artifact.

## Current Agency Engine Layers

The repository should be understood in five layers:

1. Commercial layer: qualification, offers, proposals, proof positioning
2. Strategy layer: discovery, strategy brief, trust architecture, page-goal mapping, search intent
3. Build layer: design system, images, pages, SEO, and authority assets
4. Launch layer: QA, deployment, rollback, observability, review windows
5. Governance layer: role-based training, maintenance cadence, quality metrics, safety review, documentation hygiene

## Cross-Engine Handoffs

- Proposal to website delivery: consume approved proposal scope, discovery assumptions, content/SEO promises, timeline, commercial exclusions, support package, and acceptance criteria before build planning.
- Proposal to SRS: route portal, ecommerce, SaaS, AI, integration, data, governance, or regulated workflow scope to the SRS engine before committing to page-builder or implementation detail.
- SRS to website delivery: use signed requirements, UX/content/form specifications, acceptance criteria, analytics events, and launch readiness conditions as build inputs.
- Website delivery to Google AI Search: when a brief promises Google AI
  visibility, AI Overviews, AI Mode, AEO/GEO, Search Console AI performance, or
  agentic readiness, route through `google-ai-search` before `seo` and
  `page-builder`.
- Website delivery to implementation: route custom backend, API, SaaS, AI, infrastructure, security, observability, and reliability work to the master engineering engine with clear artefacts and constraints.
- Website launch to observability, experimentation, retention: after launch, route evidence to `observability`, `experimentation`, `marketing-measurement-system`, `agency-client-retention`, `monthly-report`, and `customer-service-website-ops`.
- Marketing campaign to website (channel-to-site journey): `social-media-skills`
  (`ad-to-site-journey-handoff`) hands over the landing-page brief, message-match
  table, UTM convention and conversion-event definitions; this engine accepts or
  returns the package and owns build, performance, tags, QA evidence and the fix
  loop through `launch-campaigns/references/channel-to-site-handoff-receiving.md`,
  `page-builder`, `marketing-measurement-system` and `cro-audit`.
- Art direction to design engine: `design-reference` hands style-fit answers,
  the style thesis, mobile job map, cost flags and borrow map to
  `chwezi-design-engine` (`art-direction-routes`) for route options and
  direction boards.
- Website maintenance/support to proposal engine: when support scope, SLA, retainer, or change-request language must be sold or renewed, route commercial wording back to the proposal engine.

## Blog & Article Research — Always Use the Digital Research Engine

**Every blog post, article, or thought-leadership piece must be researched with the digital-research-engine before drafting** (applies to `content-copy/blog-writer`, `content-copy/blog-idea-generator`, and any page carrying editorial/blog content). Never write a blog post from assumed knowledge alone. Real examples, statistics, market figures, and cited research must come from a live research wave, with sources verified and credit given to the original authors (named researchers, institutions, regulators).

- **Engine location:** resolve `digital-research-engine` from the device's global engine-routing table. On this machine the canonical checkout is `C:\wamp64\www\digital-research-engine`; do not substitute a retired checkout alias.
- **Method:** Start with `research-orchestration/SKILL.md` and run a planned multi-agent wave — one research agent per cohort/region, each briefed per the engine's standard agent-brief structure. The orchestrator does the synthesis; research agents return raw, sourced findings only.
- **Article SEO/SERP standard:** Before drafting any article, run the digital-research-engine's three-wave article study: map intent and 3–7 query clusters; read the accessible top five results for each cluster; then synthesise the content gap, AI-answer opportunities, keyword map, internal links and verified primary-source plan. Use an approved search/API tool rather than direct Google SERP scraping. Record query date, provider, exact queries, result URLs and read status. Treat search visibility as competitive evidence, never as proof or a ranking promise; do not invent search volumes. For bilingual content, research English and French intent separately and translate the decision, not just the words.
- **Attribution is mandatory.** Cite real, locatable sources with URLs; name the student/academic researchers, universities, and regulators whose work you draw on. Mark anything unverifiable as UNVERIFIED — confirm it or frame it without inventing authors, titles, or statistics. Never fabricate a citation. Close each piece with a short "Sources & the researchers worth crediting" block.

## Enforcement and Quality Gates (Phases 10 + 11)

Every project shipped on the engine inherits the 15-step canonical CI pipeline at
`templates/ci/website.yml` via `scripts/install-canonical-ci.sh`. The
pipeline is the single source of enforcement. Adjustments to thresholds or
suppressions require a decision entry under `project-log/decisions/`.

Pipeline order is fixed: install → lint → unit → build → e2e-smoke →
metadata-audit → perf-gate → a11y-gate → visual-qa → security-gate →
drift-check → design-quality-score → deploy → post-deploy-smoke →
rollback-ready. Any gate failure blocks deploy. Thresholds live in
`lighthouserc.json` and `performance-budgets.json` and are non-negotiable.
Full reference: `skills/launch-ops/deploy/references/ci-troubleshooting.md`,
`skills/launch-ops/deploy/references/performance-gate.md`, `skills/launch-ops/deploy/references/africa-calibration.md`.

- Canonical commands: `perf-gate.sh`, `a11y-gate.sh`, `visual-qa.sh`,
  `security-gate.sh`, `drift-check.sh`, `slop-scan.sh`,
  `design-quality-score.sh`.
- Canonical configs: `lighthouserc.json`, `performance-budgets.json`.
- Reports directory contract: `reports/bundle/`, `reports/lighthouse/`,
  `reports/a11y/`, `reports/visual/`, `reports/security/`, `reports/drift/`,
  `reports/design-quality/`.
- Visual baseline contract: `tests/visual/baseline/`.
- Africa calibration: `skills/launch-ops/deploy/references/africa-calibration.md` (labelled
  low-end stress profile, not a median; 350 KB weight budget enforced per category by
  `scripts/route-weight-budget.mjs`; Save-Data handling) + `skills/orchestration/africa-excellence/`
  skill for pattern-level standards. Lab gates block deploy; field p75 decides success; INP is
  enforced from field/RUM data.

## Governance (Phase 11)

- `glossary.md` — canonical-name authority; `drift-check.sh` enforces.
- `docs/doc-style-guide.md` — writing standards for every file.
- `docs/deprecation-policy.md` — rename and retirement rules.
- `certification/` — operator programme (syllabus, exam bank, cohort records).
- `docs/onboarding-validation/2026/report.md` — multi-operator validation.
- `dashboards/quality-scorecard.md` — internal generated scorecard contract.

## Public Authority (Phase 12)

- `LICENSE` + `docs/licensing-matrix.md` — explicit per-path licensing.
- `docs/roadmap-public.md` — public view of the roadmap.
- `dashboards/public-scorecard.md` — quarterly public quality record.

## Hard Repository Expectations

- Prefer zero unnecessary JS
- Prefer self-hosted assets over third-party runtime dependencies
- Keep outputs distinctive; avoid generic templates
- Source content from project docs rather than inventing client facts
- Design mobile-first and check multilingual expansion risks
- Treat privacy and terms pages as standard trust infrastructure
- Update top-level docs when the operating model changes materially
- Every skill uses the canonical SKILL.md structure in `docs/doc-style-guide.md`
- Every skill also satisfies the July 2026 contract in `docs/skill-authoring-standard.md`; new skills start from `templates/skill/SKILL.md`
- Run `scripts/validate-skill-contracts.py` against `quality/skill-contract-baseline.json` and `scripts/routing-smoke-test.py` before release; the baseline accepts no findings and routing requires the expected skill in the top three
- Every skill keeps the required acknowledgement line directly under the first `# ...` heading without duplicating it
- Canonical names live in `glossary.md`; renames follow `docs/deprecation-policy.md`
- Every project ships through the canonical CI pipeline; if the pipeline
  is not installed and green, the project is not shipped on the engine
- Thresholds in `lighthouserc.json` and `performance-budgets.json` are set
  against a deliberate conservative throttled Slow-4G/3G stress profile
  (WebPageTest "3G" values: 1.6 Mbps, 300 ms RTT, with a 4x CPU slowdown and
  Lighthouse mobile emulation). It is a worst-case floor, not a market median
  (measured Uganda figures found are roughly 5-16 Mbps UCC drive tests and 8.4
  Mbps SpeedOf.Me, each with limits; Ookla and Opensignal for Uganda, Tanzania
  and Rwanda are NOT_ASSESSED); see
  `skills/launch-ops/deploy/references/africa-calibration.md` and
  `docs/source-registers/performance-currentness-2026-09-23.json`. Lab gates
  block deploy; field Core Web Vitals at p75 decide success. INP is enforced
  from field/RUM data, never from Lighthouse navigation runs.
- `scripts/perf-gate.sh` enforces every budget category through
  `scripts/route-weight-budget.mjs` and runs `scripts/html-perf-lint.mjs`.

## Direct-Response Copy for Sales Pages

When building landing pages, sales pages, VSL scripts, webinar funnels,
book funnels, order pages, upsell/OTO pages, or application pages, use
the `long-form-sales-copy` skill, which applies the engine's own
procedures (informed by Kennedy and Brunson, cited in each reference):

- a sales-letter build procedure in six workstreams (promise and
  headline, credibility and honest admissions, offer and value build,
  risk reversal and guarantee, close and postscript, sequence and
  follow-up)
- funnel scripts in five movements, plus webinar closes, one-time
  offers, follow-up email sequences, the phases of a lead and a
  100-visitor test
- an offer-proposition stack (unique selling, value, offer, safety and
  experience propositions) with copy-level price framing

The working procedures live in task-oriented references:
`skills/content-copy/long-form-sales-copy/references/sales-letter-build-procedure.md`,
`funnel-scripts-and-sequences.md` and `offer-propositions-and-price-framing.md`;
price strategy in `skills/agency-ops/authority-offers/references/price-strategy-and-discount-policy.md`;
premium selling in `skills/agency-ops/premium-sales-conversation/references/sales-process-and-takeaway-selling.md`.
Pricing and packages pages use
`skills/content-copy/sales-copywriting/references/pricing-page-choice-architecture.md`;
headline generation and the mandatory direct-response ethics filter use
`skills/content-copy/sales-copywriting/references/headline-families-and-ethics-filter.md`.

For brand-level messaging, use
`skills/brand/brand-storytelling/references/sb7-brandscript-worksheet.md`
(customer = hero, brand = guide) as the upstream foundation; the long-form
procedures then drive the actual sales-page copy.

## Working Model

When a task is ambiguous, follow this order:

1. Identify the smallest skill that fully owns the request.
2. Read that skill's `SKILL.md`.
3. Load only the reference files required for the exact subtask.
4. If the skill depends on upstream artifacts, confirm those artifacts exist before proceeding.
5. If the task spans multiple skills, keep the handoff explicit: note the input artifact, the output artifact, and the next skill that should consume it.

## Quality Expectations

- Preserve repository portability across Claude Code and Codex.
- Avoid product-specific path assumptions in skill instructions and execution.
- Keep `SKILL.md` concise and execution-focused.
- Keep heavy theory, examples, and long-form detail in `references/`.
- Prefer additive changes over restructures.
- Do not duplicate the same logic across multiple skills when a shared reference or upstream skill already owns it.

## Safety

- Run `skill-safety-audit` when a skill changes materially.
- Treat scripts and reference files as part of the skill surface area during review.
- Do not accept hidden side effects, installers, or instructions that bypass repository norms.

<!-- chwezi-design-engine:trigger v4 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`chwezi-design-engine`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from the active runner's global engine-routing table or
`AGENTS.md`** — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from chwezi-design-engine. Hard rule: never use a banned AI-slop font
as primary type — hard ban: Inter, Geist, Roboto, Open Sans, Lato, Arial, Fraunces, IBM Plex (all
faces); secondary ban: Space Grotesk, Instrument Serif, Instrument Sans, Poppins, Montserrat, Nunito, Nunito Sans, Newsreader, Cormorant (all cuts), Crimson Pro, Plus Jakarta Sans, DM Sans, Outfit, Playfair Display, Lora, Space Mono;
Roboto Mono and IBM Plex Mono are banned as monospace choices; Source Sans 3 only as a paired
body face; no bare system stacks alone. State the chosen typeface and reason before producing
any artifact.
<!-- /chwezi-design-engine:trigger -->
<!-- chwezi-design-engine:relocated v1 -->
**Relocated design skills.** These skills were moved OUT of website-skills into the
`chwezi-design-engine` engine (resolve its path from your global routing table). Any reference
to them by name resolves there, NOT in this repo:
`color-selection`, `ux-psychology`, `form-ux-design`, `brand-style-guide`, `brand-alignment` (historical
name; folded into `brand-visual-identity` and its brand-consistency gate reference),
`sector-strategies`, `legal` (now `legal-sector-ui-ux`), `data-visualization`,
`premium-ui-ux-design` (the general design version; website keeps its build-coupled orchestration entry).
Still build-coupled and kept here: `design-system`, `page-builder`, `visual-qa`, `website-builder`.
<!-- /chwezi-design-engine:relocated -->

## Human-English editorial standard (2026-08 Kaizen)

Load [the Human-English five-pass review](skills/content-copy/language-standards/references/human-english-five-pass-review.md) for every web page, landing page, blog, SEO/GEO asset, CTA, form, error message, email, and support message. Apply its five passes with `language-standards`, `content-writing`, `premium-commercial-writing`, the relevant native-copy skill, and the anti-slop/visual/accessibility gates.

Website copy must be reader-first, specific, grammatical, scannable, and honest about the offer, proof, process, limits, and next action. Do not create “human” copy with fake colloquialisms, errors, generic welcome language, keyword stuffing, or unsupported superlatives. Record page job, audience, source/proof map, language and market, state-copy review, proof status, gaps, reviewer, and date.

Apply Digital Research's `docs/continuous-improvement/machine-errors-editorial-gate-2026-09-03.md`
to page copy and repeated interface modules. Review ME1-ME7 for semantic repetition, decorative
symmetry, over-explanation, inflated promise, generic examples, rhetorical mannerisms, and
insight-shaped filler. Preserve repeated navigation, state, accessibility, or legal copy only when
its function is documented; unavailable evidence is `NOT_ASSESSED`.

Apply AS1-AS7 from the shared gate to website visuals and repeated modules. Purple gradients,
glassmorphism, neon glow, AI-beige defaults, decorative editorial scaffolding, and decorative motion
are no-ship choices; record `cli`, `browser`, `llm_only`, or `human_review` evidence and mark missing
render evidence `NOT_ASSESSED`.

## DOMAIN PROMPT GENERATION CONTRACT

For a prompt handoff, read the local [domain prompt contract](docs/ai-prompting/domain-prompt-compilation-contract.md). Generate a ready-to-paste prompt for one page or journey slice with audience/job, real content, hierarchy, states, responsive/accessibility/performance constraints, assets, output, and render checks. Prefer HTML/CSS/SVG when exact layout or copy matters. **Ready-to-paste prompt:** include assumptions, visual risks, and acceptance checks. **Failure action:** fix one failed state locally; rebuild when the structure is wrong.

## PORTFOLIO CRAFT CONTRACT

Load `C:\wamp64\www\chwezi-engine-agents\docs\operations\portfolio-craft-standard-2026-09-04.md` when available. Build a website one user journey and state at a time: frame the job and conversion, inspect the current page/data flow, implement one meaningful slice with real content and assets, render it at relevant breakpoints, exercise loading/empty/error/focus/consent paths, refine, and record browser/accessibility/performance proof. Motion must explain a state or action; typography, layout, colour, assets, and copy need product reasons. Do not generate an entire site and call it finished. Apply `Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure` to kaizen itself. Missing browser, render, live, or stakeholder evidence is `NOT ASSESSED`, never a pass.
