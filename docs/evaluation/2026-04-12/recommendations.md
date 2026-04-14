# Recommendations

## Priority Order

1. add hard validation layers for performance, accessibility, and rendered output
2. integrate the Phase 6 QA and E2E standards into a canonical CI path
3. prove the Phase 9 governance model in real multi-operator use
4. continue reducing documentation drift and legacy contradiction
5. complete the missing roadmap areas that still limit the engine's ceiling

## Highest-Leverage Next Steps

### 1. Create A Real Performance Gate

Add a first-class acceptance gate that can fail a project or a repository change when:

- Lighthouse drops below the accepted threshold
- JS budget exceeds the limit
- image or asset budgets regress materially

The repo already states performance standards. It now needs enforcement.

### 2. Create A Real Accessibility Gate

Accessibility is too important to remain only a shared principle.

Add:

- keyboard and focus checks
- structured accessibility acceptance criteria
- automated checks plus manual QA requirements

### 3. Add A Visual QA Layer

This is the most important missing premium-quality mechanism.

Add a visual QA layer that checks:

- hierarchy
- spacing consistency
- overflow
- empty or weak sections
- mobile visual integrity
- generic or low-intent output

### 4. Wire Phase 6 Into CI

The Playwright starter and QA matrix are valuable, but they should become the beginning of a
canonical CI flow rather than a manual option.

Recommended direction:

- build
- smoke and navigation E2E
- form E2E where possible
- metadata and crawl checks
- launch artifact verification

### 5. Validate The Governance Model In Practice

Run the Phase 9 framework against real operator onboarding:

- strategist
- implementer
- SEO/content operator
- QA/launch operator

Success should be measured, not assumed.

### 6. Continue Documentation Consolidation

Use the new governance policy actively.

Specifically:

- remove stale or duplicated claims
- clean up repo-level documentation
- keep `SKILL.md` concise and put operational depth in owning references
- update evaluation docs whenever the system changes materially

## Targeted Skill Recommendations

### website-builder

- keep using it as the system owner for cross-skill orchestration, governance, and handbook indexing
- add a clearer machine-readable build contract over time

### deploy

- turn the new runbooks and checklists into a more executable path
- add a canonical CI example that teams can copy directly into client projects

### design-system and page-builder

- add visual QA acceptance criteria
- keep narrowing the gap between design ambition and rendered-output review

### seo

- move from strong guidance to stronger route-level validation
- connect the topic/intent system more tightly to metadata completeness checks

### monthly-report and retention layers

- connect the Phase 9 quality metrics dashboard to actual recurring review artifacts
- make the scorecard and repository evolution rhythm observable, not only defined

## Expected Outcome

If the repository adds hard performance and accessibility gates, a visual QA layer, and a
canonical CI path, it can reasonably move from **8.5/10** into the **9.0-9.3/10** range.

That would be enough to describe it as a genuinely world-class agency engine rather than an
advanced but still partially operator-dependent system.
