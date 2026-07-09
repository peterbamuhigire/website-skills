# Website Skills Engine Upgrade Audit — July 2026

## Executive verdict

**Current audited score: 65/100 (hard cap; uncapped rubric sum: 66/100).** Website Skills is an unusually broad and promising website-delivery engine: 59 portable skills, substantive reference material, and a serious aspiration toward accessibility, security, performance, measurement, multilingual delivery, and Africa-realistic quality. It is not yet demonstrably world-class end to end. The central gap is between extensive instructions and repeatable, verified client-project output. Broken/stale routing and CI paths, weak executable examples, and incomplete evidence for live delivery prevent a 95+ assessment.

For this single-engine audit, the master ranking is **1/1**. This is a scope position, not a comparative claim about any other repository.

## Top five priorities

1. Repair the canonical CI portability contract: remove the assumed `.claude/skills` path or make it an explicit installer input; correct the missing deploy-runner reference; add a fixture project that proves all 15 stages.
2. Replace stale internal routing after the design-skill relocation. `README.md`, `CLAUDE.md`, templates, plans, and many references still point to absent skills such as `brand-alignment`, `form-ux-design`, and `sector-strategies` without a machine-resolvable handoff.
3. Establish three maintained, runnable benchmark sites with source, brief, decisions, CI reports, accessibility evidence, visual baselines, analytics contract, and handover. These are the missing proof that the engine can deliver rather than merely prescribe.
4. Add a manifest-driven skill registry and automated integrity tests for frontmatter, acknowledgements, relative links, declared outputs, references, scripts, relocation aliases, and README counts.
5. Turn the quality gates into calibrated evidence: versioned rule packs, reproducible test fixtures, false-positive policy, human-review records, and release criteria that work on Windows as well as Linux CI.

## Score summary

| Dimension | Weight | Raw | Evidence-led verdict |
|---|---:|---:|---|
| Richness | 20 | 14 | Broad coverage and many references; several important skills have no references or worked examples. |
| Robustness | 20 | 13 | Strong stated gates, but incomplete executable proof and a broken deployment path. |
| World-class output capability | 20 | 12 | Excellent quality ambition; no benchmark-client corpus or end-to-end acceptance evidence. |
| Architecture & discoverability | 15 | 10 | Clear 11-category taxonomy, undermined by stale counts/routes and competing router claims. |
| Composability & reuse | 15 | 10 | Shared artifacts and CI exist; contracts are prose-first, not manifest/test enforced. |
| Currency & compliance | 10 | 7 | WCAG 2.2, RFC 9116, Google AI guidance and GDPR lens are present; ownership/version review is uneven. |
| **Uncapped total** | **100** | **66** | |
| **Audited total (hard cap)** | **65** | **65** | Capped by mission rule. |

Read the accompanying discovery and scorecard before acting on individual backlog items. The backlog is designed to move the engine to 95+ without removing its valuable existing breadth.

## Master ranking appendix

| Rank | Engine | Capped score | Verdict |
|---:|---|---:|---|
| 1/1 | website-skills | 65/100 | High-potential engine requiring executable proof and routing/CI repair. |
