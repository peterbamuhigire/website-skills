# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Repo Is

This is a Claude Code skills library built from `SKILL.md` files that teach Claude how to build static websites from markdown content and assets. It is not a standalone application.

It is commonly added as a Git submodule at `.claude/skills/` in client website projects, but the repository is also maintained as a portable skill system that Codex can consume directly.

The repository now operates as a portable agency system with explicit layers for:

- qualification and intake
- strategy and research
- build and SEO
- launch and rollback operations
- governance and operator onboarding

Premium is the default commercial standard for this repository. Website work must be framed and delivered as a credible business asset: strategy, world-class content, SEO/GEO, premium UX, conversion architecture, technical quality, measurement, handover, and post-launch improvement. If a brief cannot support that standard, the correct response is paid discovery, a smaller premium scope, or no-bid/no-build.

## Repo Model

- `SKILL.md` is the concise execution layer
- Skills live under `skills/<category>/<skill-name>/SKILL.md` across 11 thematic categories (see "Skill Categories" below).
- Every `SKILL.md` must place this exact line immediately below the first top-level `# ...` heading, never in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- `references/` contains detailed material, including `legacy-guidance.md`
- `scripts/` contains deterministic helpers where needed
- [AGENTS.md](./AGENTS.md) provides repository-level routing and quality rules for Codex

Claude-specific consumption at `.claude/skills/` still works, but the repository should not be treated as dependent on that path.

## Blog & Article Research — Always Use the Digital Research Engine

**Every blog post, article, or thought-leadership piece must be researched with the digital-research-engine before drafting** (applies to `content-copy/blog-writer`, `content-copy/blog-idea-generator`, and any page carrying editorial/blog content). Never write a blog post from assumed knowledge alone. Real examples, statistics, market figures, and cited research must come from a live research wave, with sources verified and credit given to the original authors (named researchers, institutions, regulators).

- **Engine location:** `digital-research-engine` (on this machine: `C:\Users\Peter\Documents\Claude Projects\digital-research-engine\skills\`). The repo is cloned on every device Peter works on; if the path differs, locate the `digital-research-engine` repo locally rather than skipping research.
- **Method:** Start with `research-orchestration/SKILL.md` and run a planned multi-agent wave — one research agent per cohort/region, each briefed per the engine's standard agent-brief structure. The orchestrator does the synthesis; research agents return raw, sourced findings only.
- **Attribution is mandatory.** Cite real, locatable sources with URLs; name the student/academic researchers, universities, and regulators whose work you draw on. Mark anything unverifiable as UNVERIFIED — confirm it or frame it without inventing authors, titles, or statistics. Never fabricate a citation. Close each piece with a short "Sources & the researchers worth crediting" block.

The repository root should contain project documentation plus `docs/`, `skills/`, and `projects/` where relevant. Root-level operational directories such as `scripts/`, `templates/`, `tests/`, and `tools/` stay at root when they serve the repository rather than a single skill.

## Repository Structure

### Skill Categories

Skills are organised under `skills/<category>/<skill>/` in 11 thematic categories:

- **`agency-ops/`** (11) — agency-client-retention, agency-positioning, authority-offers, customer-service-website-ops, email-sender, launch-campaigns, monthly-report, policy-pages, premium-sales-conversation, service-blueprint-website-delivery, social-media
- **`brand/`** (4) — brand-alignment, brand-storytelling, brand-strategy, brand-style-guide
- **`build/`** (8) — color-selection, design-reference, design-system, i18n, image-compression, page-builder, photo-manager, sector-strategies
- **`commerce/`** (4) — ecommerce, ecommerce-analytics, ecommerce-checkout, ecommerce-funnel
- **`content-copy/`** (10) — blog-idea-generator, blog-writer, content-writing, east-african-english, french-native-copy, language-standards, long-form-sales-copy, premium-commercial-writing, sales-copywriting, swahili-native-copy
- **`launch-ops/`** (4) — deploy, experimentation, marketing-measurement-system, observability
- **`meta/`** (3) — skill-safety-audit, skill-writing, update-claude-documentation
- **`orchestration/`** (5) — africa-excellence, premium-ui-ux-design, premium-website-product, website-builder, website-experience-mapping
- **`quality-gates/`** (4) — accessibility-audit, design-quality-score, security-gate, visual-qa
- **`seo-search/`** (3) — google-ai-search, seo, seo-audit
- **`ux-conversion/`** (4) — cro-audit, form-ux-design, they-ask-you-answer, ux-psychology

Always reference skills by their full categorised path: `skills/<category>/<skill>/SKILL.md`.

### Core Build Skills

```text
skills/build/i18n/SKILL.md               <- Multi-language infrastructure
skills/content-copy/language-standards/SKILL.md <- Language and tone standards
skills/content-copy/french-native-copy/SKILL.md <- Native-quality French copy execution
skills/content-copy/swahili-native-copy/SKILL.md <- Native-quality Kiswahili copy execution
skills/content-copy/content-writing/SKILL.md    <- Copywriting standards
skills/brand/brand-alignment/SKILL.md    <- Brand coherence quality gate
skills/build/design-reference/SKILL.md   <- Reference-site analysis
skills/build/sector-strategies/SKILL.md  <- Industry-specific design and trust signals
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
skills/ux-conversion/form-ux-design/SKILL.md          <- Form UX guidance
skills/ux-conversion/ux-psychology/SKILL.md           <- Behavioral UX review lens
skills/build/image-compression/SKILL.md       <- Build-time image compression
skills/agency-ops/policy-pages/SKILL.md            <- Privacy and terms guidance
skills/build/color-selection/SKILL.md         <- Color palette design
skills/content-copy/sales-copywriting/SKILL.md       <- Persuasion and conversion copywriting
skills/brand/brand-strategy/SKILL.md          <- Brand brief development
skills/brand/brand-storytelling/SKILL.md      <- Narrative and story structure
skills/brand/brand-style-guide/SKILL.md       <- Client-facing style guide
skills/ux-conversion/cro-audit/SKILL.md               <- Conversion audit
skills/agency-ops/social-media/SKILL.md            <- Social strategy and service layer
skills/meta/skill-writing/SKILL.md           <- Skill authoring
skills/meta/skill-safety-audit/SKILL.md      <- Skill safety review
skills/meta/update-claude-documentation/     <- Top-level documentation maintenance
skills/content-copy/east-african-english/SKILL.md    <- Legacy English-only standard
```

### External Skill Set

```text
proposal-skills/ <- Separate Git submodule for proposal generation
```

## Skill Execution Order

Website build skills are sequential:

1. `i18n`
2. `design-reference` when reference sites are part of the brief
3. `brand-strategy` when a project needs a structured brand brief
4. `sector-strategies` or a sector-specific skill
5. `design-system`
6. `photo-manager`
7. `page-builder`
8. `seo`
9. `deploy`
10. `seo-audit` when post-build auditing is needed

`website-builder` orchestrates this sequence. It reads the enabled-language setup, the client content set, and the available assets, then routes work through the relevant downstream skills.

Cross-cutting skills such as `language-standards`, `content-writing`, and `brand-alignment` apply throughout the workflow instead of owning a single output artifact.

## Current Agency Engine Layers

The repository should be understood in five layers:

1. Commercial layer: qualification, offers, proposals, proof positioning
2. Strategy layer: discovery, strategy brief, trust architecture, page-goal mapping, search intent
3. Build layer: design system, images, pages, SEO, and authority assets
4. Launch layer: QA, deployment, rollback, observability, review windows
5. Governance layer: role-based training, maintenance cadence, quality metrics, safety review, documentation hygiene

## Plugin Guidance

Recommended before website development work:

```text
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
/plugin marketplace add anthropics/claude-code
/plugin install frontend-design@claude-code-plugins
```

Use plugins where they materially improve design, implementation, debugging, or QA output.

## Canonical CI Pipeline (Phase 10)

Every client project built on the engine inherits the 15-step pipeline at
`templates/ci/website.yml` via `scripts/install-canonical-ci.sh <project>`.
Pipeline order is fixed: install → lint → unit → build → e2e-smoke →
metadata-audit → perf-gate → a11y-gate → visual-qa → security-gate →
drift-check → design-quality-score → deploy → post-deploy-smoke →
rollback-ready.

Any gate failure blocks deploy. Thresholds live in `lighthouserc.json` and
`performance-budgets.json` and are non-negotiable; adjustments require a
decision entry under `project-log/decisions/`.

Full reference: `skills/launch-ops/deploy/references/ci-troubleshooting.md`,
`skills/launch-ops/deploy/references/performance-gate.md`, `skills/launch-ops/deploy/references/africa-calibration.md`.

## Hard Repository Expectations

- Prefer zero unnecessary JS
- Prefer self-hosted assets over third-party runtime dependencies
- Keep outputs distinctive; avoid generic templates
- Source content from project docs rather than inventing client facts
- Design mobile-first and check multilingual expansion risks
- Treat privacy and terms pages as standard trust infrastructure
- Run `skill-safety-audit` when a skill changes materially
- Update top-level docs when the operating model changes materially
- Every skill uses the canonical SKILL.md structure in `docs/doc-style-guide.md`
- Every skill keeps the required acknowledgement line directly under the first `# ...` heading without duplicating it
- Canonical names live in `glossary.md`; renames follow `docs/deprecation-policy.md`
- Every project ships through the canonical CI pipeline; if the pipeline
  is not installed and green, the project is not shipped on the engine
- Thresholds in `lighthouserc.json` and `performance-budgets.json` are
  calibrated for African 3G mobile reality (1.6 Mbps, 300ms RTT, 4x CPU
  slowdown); see `skills/launch-ops/deploy/references/africa-calibration.md`

## Direct-Response Copy for Sales Pages

When building landing pages, sales pages, VSL scripts, webinar funnels,
book funnels, order pages, upsell/OTO pages, or application pages, use
the `long-form-sales-copy` skill, which applies:

- Kennedy's 28-step Ultimate Sales Letter system (headline, Johnson Box,
  Damaging Admission, Hidden Benefit, value stack, Beat the Price,
  Creative P.S., Power of a Sequence)
- Brunson's funnel scripts (Star-Story-Solution 35-beat long-form,
  Perfect Webinar close, OTO Bump, Soap Opera + Seinfeld email
  sequences, 7 phases of a lead, 100-Visitor Test)
- Kennedy's 5 Propositions stack (USP + UVP + Irresistible Offer +
  Unique Safety Proposition + Unique Experience Proposition)

Full primary-source extractions live in `skills/book-extractions/`:
`kennedy-ultimate-sales-letter-extraction.md`,
`brunson-dotcomsecrets-ignite-extraction.md`,
`kennedy-no-bs-sales-success-extraction.md`,
`kennedy-no-bs-price-strategy-extraction.md`.

For brand-level messaging, use `skills/book-extractions/storybrand-sb7-framework.md`
(customer = hero, brand = guide) as the upstream foundation; Kennedy and
Brunson then drive the actual sales-page copy.
