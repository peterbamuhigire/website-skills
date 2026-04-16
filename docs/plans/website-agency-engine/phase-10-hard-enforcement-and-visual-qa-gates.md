# Phase 10 - Hard Enforcement and Visual QA Gates

## Objective

Convert the standards already documented across the repository into machine-enforced gates
that fail builds, block deploys, and prevent regressions. Install the canonical CI pipeline
that every client project inherits on day one, and add the rendered-output review loop the
2026-04-12 evaluation identifies as the most important missing premium-quality mechanism.

## Why This Phase Matters

The current limiter is not knowledge. It is enforcement. The 2026-04-12 evaluation scores
**Performance and Accessibility Enforcement at 7.3/10** - the lowest dimension - and lists
"insufficient hard validation" as the first bottom-line limiter.

Premium quality cannot survive at scale on social enforcement. A senior operator can hold
the line for one project; ten projects shipped by three operators cannot. Without machine
gates:

- Lighthouse targets become aspirational
- accessibility violations ship undetected
- visual hierarchy collapses on mobile and nobody catches it
- security regressions land because nobody ran the audit
- the canonical CI path stays a recommendation rather than an inheritance

This phase is what makes "world-class" stop being a self-rating and start being a property
that can be observed on every project on every PR.

## Core Outcomes

- one canonical performance gate command that fails on regression
- one canonical accessibility gate command that fails on serious or critical violations
- one canonical visual QA layer that screenshot-diffs every primary template
- one canonical security and compliance gate that runs on every PR
- one canonical CI pipeline that runs every gate and blocks deploy on failure
- one inherited workflow file that every client project copies into `.github/workflows/`
- new skills, references, and scripts that turn the gates into operator routines

## Workstreams

### 1. Performance Gate

Build a first-class performance enforcement layer.

Required scope:

- one canonical command (`pnpm run perf-gate` or `npm run perf-gate`) that runs Lighthouse
  CI against every primary route on a built static preview
- a `lighthouserc.json` configuration committed to the repository with thresholds:
  - performance >= 95
  - accessibility >= 95
  - best-practices >= 95
  - seo >= 100
- route-level performance budgets defined in `performance-budgets.json`:
  - LCP <= 2.0s on simulated 3G
  - INP <= 200ms
  - CLS <= 0.1
  - JS budget <= 80 KB gzip per route on first load
  - CSS budget <= 30 KB gzip per route on first load
  - image budget <= 200 KB per above-the-fold image after compression
- bundle analysis report emitted to `reports/bundle/`
- third-party JS audit script that flags any external runtime dependency
- font performance check (subsetting, `font-display: swap`, preload of critical weights)

Failure of any threshold must block the deploy step in CI.

### 2. Accessibility Gate

Promote accessibility from a distributed expectation to a dedicated operating layer.

Required scope:

- a new top-level `accessibility-audit/SKILL.md` skill
- one canonical command (`pnpm run a11y-gate`) that runs axe-core against every primary route
- WCAG 2.2 AA baseline written into `accessibility-audit/references/wcag-baseline.md`
- automated checks for:
  - landmark structure (one main, one banner, one contentinfo)
  - heading hierarchy (no skipped levels)
  - form label association
  - colour contrast (4.5:1 body, 3:1 large text)
  - language attribute on `<html>`
  - skip link presence
  - alt text on every img and meaningful svg
- manual checklist for the QA operator covering keyboard navigation, focus order, and
  reduced-motion respect
- screen reader smoke test scripts for NVDA (Windows) and VoiceOver (macOS/iOS), one
  script per primary template

Any axe-core violation at "serious" or "critical" severity must block the deploy step.

### 3. Visual QA Layer

Install the rendered-output review loop the evaluation flags as the most important
missing premium-quality mechanism.

Required scope:

- a new top-level `visual-qa/SKILL.md` skill
- Playwright-based screenshot diff harness with baselines stored under `tests/visual/baseline/`
- per-template captures at three viewports: 375px, 768px, 1280px
- per-template captures in light and dark modes if the project supports both
- difference threshold: 0.1% pixel difference, with a documented review and approval flow
- automated hierarchy check: assert one h1 per page, no orphan h3 without h2, no h4 without h3
- automated overflow check: assert no element renders horizontal scroll at 375px
- automated empty-section check: warn on any section with fewer than 60 words of body copy
- AI-slop scan on rendered output using the heuristics already published in
  `design-system/references/ai-slop-prevention.md`, extended with:
  - detection of generic gradient backgrounds (banned palettes)
  - detection of stock-icon overuse
  - detection of low-information hero sections
- structured visual review checklist for the QA operator covering hierarchy, spacing,
  typography rhythm, and trust-signal placement

Failed visual diff requires explicit reviewer approval to merge.

### 4. Canonical CI Pipeline

Wire every gate into one canonical pipeline that every client project inherits.

Required scope:

- one workflow file at `templates/ci/website.yml` that becomes the system standard
- pipeline order:
  1. install dependencies (with cache)
  2. lint and type-check
  3. unit tests
  4. build
  5. start preview server
  6. e2e smoke tests (homepage, services, contact form, sitemap)
  7. metadata audit (every page has title, description, og:image, og:title, hreflang)
  8. performance gate (workstream 1)
  9. accessibility gate (workstream 2)
  10. visual QA layer (workstream 3)
  11. security and compliance gate (workstream 5)
  12. deploy step (only on green main; uses the deploy skill's runbook)
  13. post-deploy smoke test
  14. rollback automation hook
- copy-into-project bootstrap script: `scripts/install-canonical-ci.sh <project-path>`
- a CI troubleshooting reference at `deploy/references/ci-troubleshooting.md`
- documented requirement: any client project that does not run this pipeline cannot
  claim to have shipped on the world-class engine

### 5. Security and Compliance Gate

Make security and privacy a CI-time responsibility rather than a launch-day surprise.

Required scope:

- a new top-level `security-gate/SKILL.md` skill that bundles the existing security
  guidance into one operational gate
- dependency audit step (`pnpm audit` or `npm audit`) with a "high" severity threshold
  that blocks deploy
- CSP header validation against the baseline at `security-gate/references/csp-baseline.md`
- security headers audit (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy,
  Permissions-Policy)
- Subresource Integrity (SRI) check on any third-party asset that survived design review
- privacy and cookie compliance matrix at `security-gate/references/compliance-matrix.md`
  covering Uganda DPPA 2019, Kenya Data Protection Act 2019, Nigeria NDPR, South Africa POPIA, and GDPR
- supply-chain scan (lockfile audit, package-name typosquat detection)
- secrets scan that blocks any commit containing API keys, tokens, or credentials

Any "high" or "critical" security finding must block the deploy step.

### 6. Africa-Realistic Gate Calibration

The gates must reflect the constraints of the actual market the agency serves.

Required scope:

- performance budgets validated on a simulated 3G connection (1.6 Mbps down, 750 Kbps up,
  300ms RTT) representative of intermittent African mobile networks
- a route-level "weight budget" reference for primary templates targeted at <= 350 KB
  total transfer on first load including HTML, CSS, JS, and the largest above-the-fold image
- a documented "low-bandwidth fallback" check: every interactive feature must degrade
  gracefully on a connection that drops to 2G
- a documented "data-cost respect" rule: no autoplay video, no preloading non-critical
  assets, no unsolicited large downloads
- the canonical CI pipeline must include a "data weight budget" assertion alongside the
  Lighthouse score

This calibration is what makes the gates appropriate for the African market rather than
copied from a US or EU benchmark.

## Repository Outputs Required

- `accessibility-audit/SKILL.md` and supporting references
- `visual-qa/SKILL.md` and supporting references
- `security-gate/SKILL.md` and supporting references
- `templates/ci/website.yml` canonical CI workflow
- `lighthouserc.json` reference configuration
- `performance-budgets.json` reference configuration
- `scripts/install-canonical-ci.sh` bootstrap script
- `tests/visual/baseline/` baseline directory contract
- `deploy/references/ci-troubleshooting.md`
- updates to `deploy/SKILL.md` to point at the canonical CI pipeline
- updates to `website-builder/SKILL.md` to reference the gates as part of the build contract
- a new entry in `project-log/decisions/` documenting why these gates exist and their thresholds

## Success Criteria

- A re-run of the `docs/evaluation/` framework moves Performance and Accessibility
  Enforcement from 7.3 to >= 9.2.
- One canonical command exists for each gate and can be invoked from any client project.
- The canonical CI workflow is in use on at least three client projects within four
  weeks of phase completion.
- A deliberately broken PR (Lighthouse regression, axe violation, screenshot drift,
  high-severity dependency CVE) is rejected by CI without operator intervention.
- No client project ships without the gates running and passing.

## Risks to Avoid

- Treating the gates as suggestions. If they can be skipped, they are not gates.
- Setting thresholds too generously to avoid noisy CI. Premium positioning requires
  premium thresholds.
- Building five separate ad-hoc CI files instead of one canonical workflow. The whole
  point is inheritance.
- Letting visual QA become a one-person opinion. The structured review checklist is
  the gate; the human is the reviewer of the gate's findings.
- Forgetting Africa-specific calibration. A site that scores 95 on a US fibre connection
  but 60 on a Kampala 3G is not premium for the actual market.
- Adding gates without writing scripts that any operator can run. Gates that only the
  founder knows how to invoke do not scale.

## Reading Material To Buy And Provide At This Stage

- *High Performance Browser Networking* by Ilya Grigorik: the canonical reference for
  performance budgets and network reality.
- *Web Performance in Action* by Jeremy Wagner: practical performance engineering
  including budget enforcement.
- *Inclusive Components* by Heydon Pickering: pattern-by-pattern accessibility for the
  exact components a static site uses.
- *Accessibility for Everyone* by Laura Kalbag: organisational and operational view of
  accessibility as an engineering discipline.
- *Form Design Patterns* by Adam Silver: form accessibility in practical depth.
- *Refactoring UI* by Adam Wathan and Steve Schoger: visual quality heuristics that
  inform the visual QA review checklist.
- *Continuous Delivery* by Jez Humble and David Farley: pipeline design and the
  philosophy of automated quality gates.
- *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim: evidence that gated
  pipelines correlate with both quality and delivery speed.
- *The Tangled Web* by Michal Zalewski: the security model that the security-gate
  baseline is grounded in.
- *Building Secure and Reliable Systems* by Heather Adkins et al. (Google SRE): the
  intersection of security gates and reliability engineering.
