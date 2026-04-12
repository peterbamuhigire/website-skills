# Gap Analysis

## Main System Gaps

### 1. Contract Drift Between Skills

This is the biggest blocker to world-class status.

Examples found:

- blog content location conflicts: `docs/{lang}/blog/` vs `docs/blogs/`
- image structure conflicts: categorized image folders vs one flat `src/assets/images/`
- root routing conflicts: client-side language detection vs nginx root redirect
- source-of-truth conflicts in photo handling: “never modify originals” vs “delete originals”
- pattern conflicts: some references still encourage carousels while page-builder bans them
- authenticity conflict: page-builder allows fictional testimonials, which undermines trust and compliance

### 2. Weak Enforcement Layer

The repository has many excellent rules, but too few hard checks.

Missing:

- canonical artifact schemas
- path validation
- translation completeness checks
- automated Lighthouse gates
- accessibility regression checks
- stronger build-time quality validation

### 3. Accessibility Is Not A First-Class Pipeline Stage

Accessibility appears across the docs, but the system lacks:

- a dedicated accessibility audit/build skill
- automated contrast checking
- keyboard and focus verification
- stronger acceptance criteria before deploy

### 4. Performance Is More Aspirational Than Operational

The repo repeatedly targets `<500KB` and `95+ Lighthouse`, but lacks:

- a standard performance command
- route-level measurement
- CI failure on regression
- budget manifests for fonts, images, and JS

### 5. CRO Is Stronger In Audit Than In Generation

There is good CRO thinking, but it is not yet a full generation-time operating system. The repo needs stronger logic for page intent, CTA strategy, proof sequencing, and offer architecture before launch.

## Premium Design Bottlenecks

### No Visual QA Loop

There is no first-class mechanism for screenshot review, hierarchy checks, consistency checks, or detecting low-quality visual output from actual pages.

### Too Much Burden On The Model

The repo depends on the model to remember, reconcile, and prioritize a large number of instructions across many files. That increases variance and weakens repeatability.

### Weak Component Contracting

The repo explains what components should do, but less often defines structured contracts for props, fallbacks, states, and content schemas.

## SEO / Content Gaps

- insufficient canonical content schemas
- weak internal-linking orchestration
- AI-search/GEO guidance discussed more than systematically encoded

## Bottom-Line Limiters

The main blockers preventing world-class status are:

- inconsistent contracts
- insufficient automation
- weak performance and accessibility enforcement
- too much reliance on interpretation
- no strong visual QA loop
- CRO not yet deeply embedded into generation-time logic
