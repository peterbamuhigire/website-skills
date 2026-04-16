# Website Skills

Portable website-building and agency-operating skills for Claude Code and Codex.

This repository works in two modes without changing the directory layout:

- `Claude Code`: commonly consumed as a Git submodule at `.claude/skills/` inside client projects
- `Codex`: consumed directly as a repository of portable skills rooted at directories that contain `SKILL.md`

Projects can share the same skills, and updates propagate when downstream projects pull the latest repo state.

The repository now also functions as a portable website agency engine. It contains build skills plus:

- qualification and intake operations
- strategy and research artifacts
- proof and authority systems
- launch and rollback operations
- governance, onboarding, and maintenance standards

## Portability Contract

- `SKILL.md` is the concise execution layer for each skill
- `references/` holds detailed guidance, including preserved `legacy-guidance.md` files
- `scripts/` holds deterministic helpers where a workflow benefits from automation
- [AGENTS.md](/C:/wamp64/www/website-skills/AGENTS.md) defines repository-wide routing and working rules for Codex
- Consumers should not assume the repo must live under a host-specific path such as `.claude/skills/`

## Architecture

```text
website-skills/              <- this repo (often submoduled into .claude/skills/)
|-- AGENTS.md                Repo-wide routing and quality rules
|-- README.md                Overview and operating model
|-- CLAUDE.md                Claude-specific repo guidance
|-- templates/               Client-facing content templates
|-- prompts/                 Project-specific generation prompts
|-- plans/                   Phase plans and system expansion work
|-- docs/                    Evaluation and system documentation
|-- website-builder/         Master orchestrator for build and operating references
|-- design-system/           Visual system decisions
|-- page-builder/            Page and component production
|-- photo-manager/           Asset cataloging and image selection
|-- seo/                     Search-facing implementation
|-- deploy/                  QA, launch, rollback, and deployment operations
|-- i18n/                    Language infrastructure
|-- sector-strategies/       Sector design and trust-pattern guidance
|-- sectors/                 Sector-specific specializations
|-- accessibility-audit/     WCAG 2.2 AA enforcement gate
|-- visual-qa/               Screenshot diff, structural assertions, AI-slop scan
|-- security-gate/           Dep audit, headers, SRI, secrets, supply chain, compliance
|-- scripts/                 Canonical runners for every gate (perf, a11y, visual, security)
|-- tests/visual/            Baseline directory contract for visual QA
|-- reports/                 Per-build output directory (bundle, lighthouse, a11y, visual, security)
|-- templates/ci/            Canonical CI pipeline inherited by client projects
|-- project-log/decisions/   Decision log for non-obvious trade-offs
|-- blog-writer/             Blog production
|-- blog-idea-generator/     Blog ideation
|-- policy-pages/            Privacy and terms guidance
|-- seo-audit/               Search audit workflow
|-- skill-writing/           Skill authoring guidance
|-- skill-safety-audit/      Skill safety review
`-- proposal-skills/         Separate proposal-generation submodule
```

## Core Build Skills

- `website-builder`: orchestrates the website workflow and owns cross-skill operating references
- `i18n`: language routing, multilingual structure, and shared versus locale-specific rules
- `design-reference`: extracts design decisions from reference websites
- `sector-strategies` and `sectors/legal`: industry-specific trust patterns and content priorities
- `design-system`: typography, palette, motion, spacing, and visual-system decisions
- `photo-manager`: image cataloging, naming, dimensions, and logo selection
- `page-builder`: converts content and design decisions into pages and reusable UI
- `seo`: metadata, schema, sitemap, and crawler-facing configuration
- `deploy`: verification, release readiness, rollout, rollback, and post-launch checks

## Enforcement Gates (Phase 10)

Every project shipped on the engine must pass the canonical CI pipeline
at `templates/ci/website.yml`. These skills own the individual gates:

- `accessibility-audit`: WCAG 2.2 AA gate — axe-core + manual + screen reader
- `visual-qa`: screenshot diff, hierarchy/overflow/empty-section assertions, AI-slop scan
- `security-gate`: dependency audit, security headers, SRI, secrets, supply chain, Africa + GDPR compliance

Canonical commands (runnable from any client project with the skills submodule):

```bash
bash .claude/skills/scripts/perf-gate.sh      # Lighthouse + weight budgets on 3G
bash .claude/skills/scripts/a11y-gate.sh      # axe-core against every route
bash .claude/skills/scripts/visual-qa.sh      # Playwright diff + structure + slop
bash .claude/skills/scripts/security-gate.sh  # dep audit + headers + SRI + secrets + supply-chain
bash .claude/skills/scripts/install-canonical-ci.sh <project>  # one-time bootstrap
```

## Cross-Cutting Skills

- `language-standards`: regional language and tone quality
- `content-writing`: website copy structure and clarity
- `brand-alignment`: audience and brand coherence
- `sales-copywriting`: conversion-focused messaging
- `form-ux-design`: user-input flow design
- `ux-psychology`: behavioral and heuristic UX review

## Support Skills

- `blog-idea-generator`, `blog-writer`
- `brand-strategy`, `brand-storytelling`, `brand-style-guide`
- `color-selection`
- `policy-pages`
- `email-sender`
- `ecommerce`, `ecommerce-funnel`, `ecommerce-checkout`, `ecommerce-analytics`
- `agency-positioning`, `agency-client-retention`, `monthly-report`
- `they-ask-you-answer`, `social-media`
- `seo-audit`, `cro-audit`
- `skill-writing`, `skill-safety-audit`, `update-claude-documentation`

## Agency Engine Layers

The repository currently spans five operating layers:

1. Commercial layer: qualification, offers, proposals, proof positioning
2. Strategy layer: discovery, strategy brief, trust architecture, page-goal mapping, search intent
3. Build layer: design system, assets, pages, SEO, and authority content
4. Launch layer: QA, deployment, rollback, observability, review windows
5. Governance layer: training, maintenance cadence, quality metrics, safety review, documentation hygiene

## Current Phase Additions

Recent agency-engine expansion work added the following reference layers:

- `2026-04-14`: Phase 2 added intake, qualification, proposal, kickoff, artifact standards, and stage-gate operations
- `2026-04-14`: Phase 3 added website strategy briefs, competitor synthesis, trust architecture, page-goal mapping, and intent mapping
- `2026-04-14`: Phase 6 added QA matrix, launch verification, deployment and rollback runbooks, observability baseline, and a Playwright starter
- `2026-04-14`: Phase 9 added role-based training, governance policy, maintenance cadence, quality metrics dashboard, and the handbook index
- `2026-04-16`: Phase 10 added hard enforcement gates — `accessibility-audit`, `visual-qa`, and `security-gate` skills; canonical CI pipeline at `templates/ci/website.yml`; 13 canonical scripts; `lighthouserc.json` and `performance-budgets.json`; Africa 3G calibration; deploy + website-builder skill updates. See [Phase 10 completion](./docs/plans/2026-04-16-phase-10-enforcement-gates-completion.md).

## Working Model

When a task is ambiguous, follow this order:

1. Identify the smallest skill that fully owns the request.
2. Read that skill's `SKILL.md`.
3. Load only the reference files required for the exact subtask.
4. Confirm required upstream artifacts exist before proceeding.
5. If the task spans multiple skills, make the handoff explicit: input artifact, output artifact, and next owning skill.

## Quality Expectations

- Preserve repository portability across Claude Code and Codex
- Keep `SKILL.md` concise and execution-focused
- Keep heavy theory and examples in `references/`
- Prefer additive changes over restructures
- Avoid duplicating logic already owned by another skill or shared reference
- Treat scripts and references as part of the skill surface area during review

## Related Docs

- [AGENTS.md](./AGENTS.md) — repository routing and quality rules
- [CLAUDE.md](./CLAUDE.md) — Claude-specific repo guidance
- [docs/plans/INDEX.md](./docs/plans/INDEX.md) — plans index and status
- [docs/plans/NEXT_FEATURES.md](./docs/plans/NEXT_FEATURES.md) — priority roadmap
- [docs/plans/website-agency-engine](./docs/plans/website-agency-engine) — 12-phase master roadmap
- [docs/evaluation/2026-04-12](./docs/evaluation/2026-04-12) — evaluation driving Phase 10–12
