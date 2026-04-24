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

## Repo Model

- `SKILL.md` is the concise execution layer
- Every `SKILL.md` must place this exact line immediately below the first top-level `# ...` heading, never in frontmatter: `Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.`
- `references/` contains detailed material, including `legacy-guidance.md`
- `scripts/` contains deterministic helpers where needed
- [AGENTS.md](./AGENTS.md) provides repository-level routing and quality rules for Codex

Claude-specific consumption at `.claude/skills/` still works, but the repository should not be treated as dependent on that path.

## Repository Structure

### Core Build Skills

```text
i18n/SKILL.md               <- Multi-language infrastructure
language-standards/SKILL.md <- Language and tone standards
content-writing/SKILL.md    <- Copywriting standards
brand-alignment/SKILL.md    <- Brand coherence quality gate
design-reference/SKILL.md   <- Reference-site analysis
sector-strategies/SKILL.md  <- Industry-specific design and trust signals
website-builder/SKILL.md    <- Master orchestrator and system owner for operating references
design-system/SKILL.md      <- Fonts, colours, visual identity, motion
photo-manager/SKILL.md      <- Asset cataloguing, logo selection, image organisation
page-builder/SKILL.md       <- Content to pages and components
seo/SKILL.md                <- Search-facing implementation
blog-writer/SKILL.md        <- Blog production
deploy/SKILL.md             <- QA, launch checks, deployment, rollback, canonical CI pipeline
```

### Enforcement Skills (Phase 10 — added 2026-04-16)

```text
accessibility-audit/SKILL.md <- WCAG 2.2 AA gate: axe-core + manual + screen reader
visual-qa/SKILL.md           <- Screenshot diff + hierarchy/overflow/empty-section + AI-slop
security-gate/SKILL.md       <- Dep audit + headers + SRI + secrets + supply chain + compliance
```

### Operating Discipline Skills (Phase 11 — added 2026-04-16)

```text
observability/SKILL.md        <- RUM + error tracking + analytics + alert thresholds
experimentation/SKILL.md      <- Hypothesis template + stat primer + A/B infra + quarterly review
design-quality-score/SKILL.md <- 7-category rubric + slop-scan (CI step 12)
```

Phase 11 also adds: `glossary.md` (canonical names), `docs/doc-style-guide.md`
(writing standards), `docs/deprecation-policy.md` (rename/retirement rules),
`certification/` (syllabus + 60-question exam + cohort records), and
`dashboards/quality-scorecard.md` (generated-artefact contract).

### Authority Skills (Phase 12 — added 2026-04-16)

```text
africa-excellence/SKILL.md    <- Low-bandwidth, mobile-money UX, USSD-aware,
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
seo-audit/SKILL.md               <- Post-build SEO audit
blog-idea-generator/SKILL.md     <- Blog ideation
email-sender/SKILL.md            <- Self-hosted contact-form handler
form-ux-design/SKILL.md          <- Form UX guidance
ux-psychology/SKILL.md           <- Behavioral UX review lens
image-compression/SKILL.md       <- Build-time image compression
policy-pages/SKILL.md            <- Privacy and terms guidance
color-selection/SKILL.md         <- Color palette design
sales-copywriting/SKILL.md       <- Persuasion and conversion copywriting
brand-strategy/SKILL.md          <- Brand brief development
brand-storytelling/SKILL.md      <- Narrative and story structure
brand-style-guide/SKILL.md       <- Client-facing style guide
cro-audit/SKILL.md               <- Conversion audit
social-media/SKILL.md            <- Social strategy and service layer
skill-writing/SKILL.md           <- Skill authoring
skill-safety-audit/SKILL.md      <- Skill safety review
update-claude-documentation/     <- Top-level documentation maintenance
east-african-english/SKILL.md    <- Legacy English-only standard
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

Full reference: `deploy/references/ci-troubleshooting.md`,
`deploy/references/performance-gate.md`, `deploy/references/africa-calibration.md`.

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
  slowdown); see `deploy/references/africa-calibration.md`

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

Full primary-source extractions live in `book-extractions/`:
`kennedy-ultimate-sales-letter-extraction.md`,
`brunson-dotcomsecrets-ignite-extraction.md`,
`kennedy-no-bs-sales-success-extraction.md`,
`kennedy-no-bs-price-strategy-extraction.md`.

For brand-level messaging, use `book-extractions/storybrand-sb7-framework.md`
(customer = hero, brand = guide) as the upstream foundation; Kennedy and
Brunson then drive the actual sales-page copy.
