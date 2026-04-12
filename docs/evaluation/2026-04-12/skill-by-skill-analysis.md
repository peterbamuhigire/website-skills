# Skill-By-Skill Analysis

## website-builder

Strengths: clear entry point, sensible pipeline intent, strong high-level system vision.

Weaknesses: orchestration is too narrative, input/output contracts are loose, and multilingual path assumptions are inconsistent.

Improvements: add a pipeline manifest, stage exit criteria, and canonical artifact ownership.

## design-system

Strengths: one of the strongest skills; strong typography, hierarchy, spacing, motion, and anti-generic design guidance.

Weaknesses: still advisory rather than validated; no screenshot-based quality gate.

Improvements: add canonical token schema and visual QA acceptance checks.

## page-builder

Strengths: strong practical UX guidance, good multilingual awareness, useful anti-pattern coverage.

Weaknesses: allows fictional testimonials, component contracts are still loose, and quality depends heavily on model synthesis.

Improvements: ban invented proof, define page-type templates, and add screenshot QA criteria.

## seo

Strengths: broad and commercially relevant, especially for multilingual SEO, schema, sitemaps, and content support.

Weaknesses: implementation claims are stronger than enforcement mechanisms, and metadata contracts need tightening.

Improvements: add route-level validation and a canonical SEO input schema.

## blog-writer

Strengths: strong editorial ambition, strong voice guidance, good SEO integration.

Weaknesses: major conflict over content location, unclear multilingual slug contract, and weak structural validation.

Improvements: unify source-of-truth model, add frontmatter validation, and strengthen multilingual publishing rules.

## i18n

Strengths: serious multilingual thinking from the start, good text-expansion awareness, good hreflang intent.

Weaknesses: root-routing conflicts with deploy, and parity/fallback rules need more formalization.

Improvements: pick one routing model, add parity validation, and formalize missing-translation behavior.

## photo-manager

Strengths: good catalog-first mindset, useful dimension awareness, useful OG-image thinking.

Weaknesses: conflicts with README and itself on source-of-truth and directory structure; includes risky deletion guidance.

Improvements: keep originals immutable, define one canonical storage model, and formalize `_catalog.json`.

## deploy

Strengths: good static hosting awareness, useful multi-language checklist mindset.

Weaknesses: redirect logic conflicts with i18n, and verification is too manual.

Improvements: create one canonical verification script and integrate performance/accessibility smoke tests.

## brand-alignment

Strengths: commercially valuable, strong customer-centric framing, good voice authenticity emphasis.

Weaknesses: not structured enough for downstream automation.

Improvements: produce a formal brand-alignment artifact or checklist that downstream skills consume.

## content-writing

Strengths: practical, high-signal writing guidance focused on clarity, scanning, and benefits.

Weaknesses: mostly prose guidance without measurable validation.

Improvements: add content QA templates and measurable copy checks.

## sector-strategies

Strengths: major differentiator, strong sector-specific trust and design psychology.

Weaknesses: some sector guidance conflicts with global rules, and customization still relies on strong operator judgment.

Improvements: enforce global rules consistently and add sector-specific acceptance criteria.

## cro-audit

Strengths: strong commercial layer, useful prioritization model, materially better than average.

Weaknesses: audit-focused rather than generation-focused.

Improvements: pair it with a generation-time CRO skill.

## seo-audit

Strengths: useful verification layer with broad checklist coverage.

Weaknesses: still largely manual.

Improvements: convert major checks into scripts and standardized outputs.

## Summary

Best skills today:

- `design-system`
- `page-builder`
- `content-writing`
- `brand-alignment`
- `seo`
- `sector-strategies`

Highest strategic improvement opportunity:

- `website-builder`
- `i18n`
- `photo-manager`
- `deploy`
- `blog-writer`
