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

---

## Addendum — Post-Phase 12 (2026-04-16)

Recommendations #1 through #4 above are **done**. Recommendation #5 (validate
governance in practice) has its infrastructure in place but not yet the
operational evidence. Recommendation #6 (documentation consolidation) is now
CI-enforced via drift-check.

The forward-looking recommendations below replace the priority order above as
the active worklist.

### New Priority Order

1. Enrol the first certification cohort and run real operators through end-to-end
   projects (the single remaining governance proof).
2. Ship live telemetry on the first retainer client and activate the scorecard
   generation script.
3. Provision GrowthBook self-host and run the first documented experiment.
4. Publish the first open-source benchmark site under the licensing matrix.
5. Clear the drift-check's pre-existing findings (banned-term instances,
   absolute-path links, dated framing) as the first quarterly documentation
   audit's workload.
6. Run the two-operator blind rubric calibration on the worked examples.

### New highest-leverage next steps

#### 1. First operator-validation cycle

Recruit or assign a strategist, a designer/builder, an SEO+content operator,
and a QA+launch operator (minimum four; target five). Each runs one real
project end-to-end. Friction logs under
`docs/onboarding-validation/2026/<operator>/friction-log.md`. Success is
measured, not assumed: ramp-time targets per persona, quality variance ≤ 5%,
zero blocking interventions from the founder on gated work.

#### 2. First live-telemetry client

Instrument the next retainer client per `observability/SKILL.md`: RUM via
`web-vitals`, Sentry, Plausible or GA4, alerts per
`observability/references/alert-thresholds.md`. Implement
`scripts/generate-quality-scorecard.sh` to rewrite
`dashboards/quality-scorecard.md` weekly from that data.

#### 3. First experiment

Pick a retainer client with ≥ 1,000 primary-metric events per week. File the
hypothesis per `experimentation/references/hypothesis-template.md`. Provision
GrowthBook. Run to the stopping rule. File the decision.

#### 4. First benchmark site

Target a Ugandan SME services site as the reference implementation (or
similar; the Maduuka SaaS marketing site is a candidate). Separate
repository, public, indexed, CC BY-SA licensed. Must pass every Phase 10 gate
and score ≥ 9/10 on the rubric. "How this site was built" walkthrough
published alongside.

#### 5. First quarterly documentation audit

Run `DRIFT_STRICT=1 scripts/drift-check.sh`; file a written audit report
under `project-log/decisions/2026-Q2-docs-audit.md`. Resolve the pre-existing
banned-term instances and absolute-path links. Establish the quarterly
cadence.

#### 6. First conference or workshop

Target DevFest Africa 2026 or DroidConKE 2026. A talk that demonstrates the
actual scorecard and the canonical CI is worth more than five generic agency
talks. Application windows open mid-year.

### Revised targeted-skill recommendations

- `website-builder`: The build contract and maintenance calendar now name
  the full Phase 10/11/12 chain. Next: generation scripts for the scorecards.
- `deploy`: Canonical CI + launch decision record are in place. Next:
  operationalise the rollback drill during the first certification cohort's
  practical exam.
- `design-system` and `page-builder`: Design-quality rubric is live; feeding
  observed friction from scored projects back into these two skills is the
  next iteration loop.
- `seo`: Analytics-event-map is the monthly-report contract. Next: route-
  level validation via metadata-audit is already in the pipeline (CI step 6);
  tie it more tightly to the page-goal map.
- `monthly-report`: Now refuses without live telemetry. Next: prove it
  against the first live client in Q2.

### Revised expected outcome

With the above priorities executed within 12 months:

- demonstrated score reaches the same ~9.2 band as the infrastructure score
- the engine's authority claim (benchmark + certification + scorecard +
  published case studies) is externally verifiable
- a re-run of this evaluation in Q2 2027 should move the overall to **≥ 9.4**
  with both infrastructure and demonstrated scores aligned.
