# Recommendations

## Priority Order

1. fix cross-skill contradictions
2. add hard validation and QA gates
3. strengthen orchestration contracts
4. operationalize accessibility and performance
5. deepen CRO and premium design review

## Improve Existing Skills

### website-builder

- add a canonical pipeline manifest
- define required and optional artifacts
- define stage pass/fail criteria
- refuse ambiguous states rather than improvising

### i18n

- choose one canonical root-routing model
- add multilingual slug-map standards
- validate translation completeness and metadata parity
- define fallback behavior for missing translations

### photo-manager

- resolve flat vs categorized directory structure permanently
- remove instructions to delete originals
- formalize `_catalog.json` schema
- remove carousel assumptions unless globally allowed

### page-builder

- ban fictional testimonials and invented proof
- define page-type templates with required/optional sections
- add stronger component contracts
- add screenshot-based review criteria

### seo

- add canonical metadata schema
- validate metadata completeness route by route
- formalize schema selection by page type
- strengthen internal-linking rules

### blog-writer

- unify markdown source-of-truth model
- add frontmatter schema validation
- add multilingual slug relationship rules
- strengthen citation and internal-linking standards

### deploy

- create one canonical verification script
- integrate performance and accessibility smoke tests
- resolve redirect logic with i18n

## New Skills To Create

### accessibility-audit

Purpose:

- make accessibility a mandatory pre-deploy gate

### lighthouse-performance-gate

Purpose:

- turn performance promises into measurable acceptance criteria

### visual-qa

Purpose:

- review actual screenshots for hierarchy, consistency, overflow, and AI slop

### cro-engine

Purpose:

- apply CRO logic during generation, not only during audit

### content-schema-validator

Purpose:

- validate markdown/frontmatter/contracts before generation

### analytics-and-measurement

Purpose:

- standardize event tracking, conversions, and KPI readiness

### premium-art-direction

Purpose:

- raise visual outputs from “good” to agency-grade through stronger art-direction patterns and review loops

## System-Level Improvements

### Create A Canonical Build Contract

Define one repository-wide specification for:

- input locations
- output locations
- artifact schemas
- skill ownership

### Introduce Stage Gates

Recommended gates:

- content
- design
- build
- performance
- accessibility
- SEO
- CRO
- deploy

### Reduce Narrative Duplication

Keep high-level docs high-level. Keep operational truth in one place.

### Add Golden Projects

Create 2-3 reference projects that serve as quality baselines and regression examples.

### Add A Hard “Never Fabricate” Rule

The system should never invent:

- testimonials
- clients
- metrics
- awards
- certifications
- locations

## Expected Outcome

If the repo fixes contract drift and adds strong QA automation, it can realistically move from **7.1/10** into the **8.3–8.8/10** range. A true 9+ rating requires performance, accessibility, CRO, and visual QA to become enforced system behavior.
