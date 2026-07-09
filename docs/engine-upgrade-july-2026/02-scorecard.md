# Scorecard — Website Skills

## Method

Scores measure what the repository can presently support with evidence. The sum is capped at 65 by the audit mission; it is not a claim that the engine is 65% complete.

### 1. Richness — 14/20

Coverage is exceptional in breadth: 59 skills span commercial, content, build, quality, launch, SEO, African-market, and operational work, with substantial reference sets for core skills such as `agency-positioning`, `seo`, `page-builder`, and `website-builder`. The depth is uneven and remains reference-led rather than demonstrated by finished projects. It lacks an authoritative benchmark corpus and several advanced skills are essentially instruction-only.

Deficiencies: (1) add source-register, worked examples, and edge-case references to `retail-commerce-operating-system`, `long-form-sales-copy`, and `cross-page-design-consistency-audit`; (2) publish three complete anonymised benchmark project packs; (3) add an evidence index linking each high-stakes claim to a standard, edition/date, and owner.

### 2. Robustness — 13/20

The engine specifies clear gates, upstream artifacts, anti-patterns, and a canonical CI workflow. Robustness falls because the central deployment path is absent, the portability assumptions conflict, and the repository has no executable fixture proving gates, failures, or recovery. A gate described in prose is not a dependable release control.

Deficiencies: (1) repair and test CI/deploy paths; (2) add fixture sites with expected-pass and expected-fail snapshots for every gate; (3) add a machine-readable release manifest with explicit waiver and exception records.

### 3. World-Class Output Capability — 12/20

The premium, anti-slop, accessibility, performance, security, content, and measurement intent is strong. However, no evidence pack shows a complete client-quality output passing every required stage, calibrated human visual review, multilingual native review, analytics verification, and handover. The missing design-system engine dependency also leaves presentation quality externally contingent.

Deficiencies: (1) certify benchmark sites against the entire contract; (2) add professional deliverable templates and completed exemplars; (3) require independent human acceptance for visual, language, legal, and accessibility claims.

### 4. Architecture & Discoverability — 10/15

The 11-category hierarchy and orchestrator layer are comprehensible, and `SKILL.md` has a consistent shape. Discoverability is impaired by 57-versus-59 documentation drift, a `skill-writing`/`skill-creator` identity mismatch, duplicate or historic routing, and unresolvable relocated-skill calls.

Deficiencies: (1) introduce `skills/manifest.yml` as the canonical registry; (2) add relocation aliases with expiry and an automated link checker; (3) generate README, CLAUDE, and router indexes from the manifest.

### 5. Composability & Reuse — 10/15

Shared templates, references, a canonical CI and project-artifact maps provide real composition. Yet dependencies and inputs/outputs are prose paths, not typed contracts; most skills have no runnable examples, and project output schemas are not validated.

Deficiencies: (1) define a standard artifact contract with JSON Schema/frontmatter; (2) add reusable client-project starter fixtures and golden outputs; (3) version shared policies and enforce cross-skill compatibility in CI.

### 6. Currency & Compliance — 7/10

The engine names WCAG 2.2 AA, RFC 9116, GDPR, current Google AI Search guidance, 3G/Africa calibration and security controls. It appropriately warns against AI-search myths. What is missing is a dated standards register, jurisdiction matrix ownership, legal-review boundary, and scheduled source refresh.

Deficiencies: (1) create a standards register with URLs, version/date, applicability, owner and next review; (2) distinguish legal information from jurisdiction-specific legal advice; (3) schedule quarterly checks for Google, WCAG/W3C, privacy, payment, and platform changes.

| Raw total | Hard cap | Final audited score |
|---:|---:|---:|
| 66/100 | 65/100 | **65/100** |

## Master ranking appendix

| Rank | Engine | Capped score | Verdict |
|---:|---|---:|---|
| 1/1 | website-skills | 65/100 | Strong knowledge surface, with execution evidence and integrity work outstanding. |
