# Repository Agents Guide

## Purpose

This repository is a portable skill library for building websites and related marketing assets.

- In Claude Code, the repository is typically consumed as a skill library inside a client project.
- In Codex, the same directories should be treated as portable skills rooted at each folder that contains `SKILL.md`.
- `SKILL.md` is the portable execution unit.
- Detailed domain material belongs in `references/`.
- Deterministic helpers belong in `scripts/`.

Do not assume this repository must live under `.claude/skills/`. Resolve skills by repository-relative paths such as `website-builder/SKILL.md`, `design-system/SKILL.md`, or `sectors/legal/SKILL.md`.

## Baseline Rules

- Preserve existing Claude Code behavior unless a task explicitly requires a change.
- Prefer the skill-local `SKILL.md` first, then load only the specific files needed from that skill's `references/`.
- Treat `references/legacy-guidance.md` as preserved detailed guidance from the pre-standardized version of the skill.
- Do not bulk-load every reference file in a skill. Read only what the current task needs.
- Use bundled scripts when they are the safest or most repeatable path.
- Keep outputs implementation-oriented. Avoid abstract summaries when a concrete deliverable is expected.

## Routing

Use these skills as the default router:

- `website-builder`: Full website orchestration from docs and assets through deploy readiness.
- `i18n`: Language routing, multilingual structure, and shared versus locale-specific rules.
- `design-reference`: Extracting decisions from example websites.
- `sector-strategies` or `sectors/legal`: Sector-specific patterns and trust signals.
- `design-system`: Typography, palette, motion, spacing, and visual system decisions.
- `photo-manager`: Image cataloging, naming, dimensions, and logo selection.
- `page-builder`: Converting content and design decisions into pages and reusable UI.
- `seo`: Implementation of metadata, schema, sitemaps, and crawler-facing configuration.
- `deploy`: Build verification, deployment artifacts, and release readiness.

Use these cross-cutting skills whenever their lens materially improves the output:

- `language-standards`: Regional language and tone quality.
- `content-writing`: Website copy structure and clarity.
- `brand-alignment`: Audience and brand coherence.
- `sales-copywriting`: Conversion-focused messaging.
- `form-ux-design`: Any user-input flow.
- `ux-psychology`: Behavioral and heuristic UX review.

Use these support skills on demand:

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
