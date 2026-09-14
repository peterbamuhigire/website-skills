# Book-informed website product-engineering synthesis

Status: adopted on 2026-09-14.

## Practices to standardise

### Start each page with a scenario

Name the audience, trigger, job, desired outcome, confidence barrier, and
next action before selecting a layout or copy. Turn the scenario into a page
goal, content hierarchy, primary and secondary paths, and measurable
acceptance. A page is not complete because it looks polished; its critical
journey must be understandable, usable, accessible, and recoverable.

### Specify the whole journey and its failure states

For the primary journey, cover discovery, understanding, action, confirmation,
and recovery. Include realistic content length, mobile/touch interaction,
loading, empty, error, validation, success, consent, and interruption states.
Make diagnostics actionable: explain what happened, what the visitor can do
next, and how to recover without losing work.

### Build in stages and learn from friction

Prefer a narrow, testable first release or experimental version when the
unknowns are material. Keep a friction log with the scenario, observed
obstacle, evidence, likely cause, impact, owner, and next experiment. After
launch, combine qualitative feedback with adoption, value, conversion,
performance, accessibility, and support signals. Refresh the page or
experiment hypothesis from evidence, not a calendar alone.

### Connect design-system and engineering proof

Pages should use the governed token/component source, state contracts, and
accessibility semantics. Define performance budgets and critical-flow checks
before implementation; verify on representative devices, networks, and
content. Record SEO/search evidence separately from UX and conversion claims.

## Deliberate exclusions

- No generic AI visibility or training-data promise is added without current,
  claim-level evidence.
- No vendor-specific tool or framework is required where the page outcome can
  be achieved with a simpler implementation.

## Sources

- Drew Hoskins, The Product-Minded Engineer.
- Michael Mangialardi, Design Systems for Developers: Learn How to Code Design
  Systems That Scale.
- Almantas Karpavičius, Software Craftsmanship Using AI.
