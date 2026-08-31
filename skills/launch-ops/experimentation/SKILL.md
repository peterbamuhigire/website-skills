---
name: experimentation
description: Use when a measured website question needs a pre-registered controlled test, power check, guardrails, analysis, and decision; use `cro-audit` to diagnose opportunities and `marketing-measurement-system` to define KPIs.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Experimentation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Turn a measurable uncertainty into a controlled learning cycle with a declared hypothesis, stopping rule, guardrails, and decision.

<!-- dual-compat-start -->
## Use When

- Existing analytics cannot resolve a conversion, engagement, or retention question.
- A proposed change should be tested before broad rollout.
- A redesign or message change needs causal evidence rather than before/after opinion.

## Do Not Use When

- The metric or opportunity is undefined; use `marketing-measurement-system` or `cro-audit` first.
- A bug, accessibility failure, security defect, or legal issue needs correction; fix it without experimentation.
- Traffic or event volume cannot support the required effect within a useful window; use qualitative or staged methods.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Decision question and falsifiable hypothesis | Product/marketing owner | yes | Return a hypothesis workshop brief. |
| Baseline metric, event definitions, traffic, and variance | Analytics owner | yes | Do not calculate or run a test from guessed data. |
| Minimum meaningful effect and decision horizon | Business owner | yes | Stop; statistical detectability alone is not business value. |
| Guardrails, segment rules, implementation owner, and platform | Project team | yes for launch | Produce a design only; do not activate the test. |
| Authority to expose users and change production | Named owner | yes for mutation | Stop at preflight evidence. |

## Workflow

1. Write the hypothesis and decision using [the hypothesis template](references/hypothesis-template.md).
2. Stop if the question is not falsifiable, the metric is unstable, or the effect would not change a decision.
3. Calculate sample size and duration from observed baseline data using [the significance primer](references/stat-significance-primer.md).
4. Choose the simplest valid design and declare unit of assignment, exposure, variants, exclusions, primary metric, guardrails, and stopping rule.
5. Pre-register ship, kill, iterate, and inconclusive decisions before implementation.
6. Implement deterministic assignment and instrumentation with least-privilege production access.
7. Preflight assignment balance, exposure events, outcome events, contamination, accessibility, performance, and rollback.
8. Run to the stopping rule; stop early only for a declared safety or guardrail trigger.
9. Analyse effect size and uncertainty, inspect segments only as pre-declared or exploratory, and record data-quality limitations.
10. Decide, clean up losing code, update the baseline, and share learning.
11. If telemetry fails during the run, pause interpretation, repair the evidence chain, and classify affected data.
12. Apply the Kaizen conversion loop: record the observation, standardise only a guarded win, teach the learning into the owning pattern, and schedule the next baseline.

## Quality Standards

- Hypothesis, minimum meaningful effect, stopping rule, guardrails, and decision rules exist before exposure.
- Sample planning uses observed data and documents assumptions.
- Assignment and outcome events are verified before launch.
- Reports include effect size, uncertainty, runtime, exclusions, and data-quality caveats.
- Inconclusive is a valid result; no post-hoc redefinition creates a winner.
- Experiment code and flags have a dated cleanup owner.
- The experiment record states what was learned about the audience problem, not only whether a variant won.
- A low-cost or qualitative learning path is used when traffic cannot support a reliable controlled test.

## Anti-Patterns

- Running a test "to see what happens". Fix: write a falsifiable hypothesis and decision first.
- Peeking and stopping on a favourable fluctuation. Fix: follow the pre-registered rule.
- Calling a small sample a win from point estimate alone. Fix: report uncertainty and practical significance.
- Changing multiple uncontrolled elements. Fix: isolate the variable or use a justified factorial design.
- Ignoring seasonality or campaign contamination. Fix: schedule or model known effects and record them.
- Shipping a winner without verified instrumentation. Fix: establish the new measured baseline.
- Keeping losing variants indefinitely. Fix: assign cleanup ownership and deadline.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Experiment plan and logbook | Product, implementation, and analytics owners | Hypothesis, design, sample plan, metrics, stopping and decision rules are complete. |
| Preflight evidence | Release owner | Assignment, events, guardrails, accessibility, performance, and rollback are observed. |
| Results and decision record | Business owner and monthly reporting | Effect, uncertainty, caveats, decision, and cleanup action are explicit. |
| Quarterly learning review | Retainer owner | Wins, losses, inconclusive tests, belief changes, and next priorities are summarised. |

## References

- [Hypothesis template](references/hypothesis-template.md)
- [Statistical significance primer](references/stat-significance-primer.md)
- [A/B infrastructure](references/ab-infrastructure.md)
- [Experiment logbook template](references/experiment-logbook-template.md)
- [Quarterly review template](references/quarterly-review-template.md)
- [Kaizen conversion experiment loop](references/kaizen-conversion-experiment-loop.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Pre-registration | Versioned plan | It predates exposure and contains all decision rules. |
| Instrumentation and assignment check | Test output or screenshots/logs | Events and allocation were observed, not assumed. |
| Analysis record | Reproducible calculation and narrative | Inputs, exclusions, effect, uncertainty, and limitations are traceable. |

## Capability Contract

Read access to analytics and project context is required. Analysis defaults to read-only. Editing flags, instrumentation, or production exposure requires explicit authority. Network, spending, user exposure, destructive cleanup, and claims of statistical or business success require observed evidence and named approval.

## Degraded Mode

When trustworthy data, execution, network, platform, or production authority is unavailable, return the narrowest qualified pre-registered design or qualitative alternative and mark power, instrumentation, and outcomes `not assessed`. Never manufacture a sample estimate or winner.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Adequate data and practical test duration | Run controlled test | Opinion-led rollout |
| Insufficient power within decision horizon | Use qualitative or staged evidence | Noisy false winner |
| Guardrail breaches | Stop and mitigate | User or business harm |
| Result is uncertain at stopping rule | Record inconclusive and decide next evidence | Post-hoc winner creation |
| Telemetry integrity fails | Pause interpretation | Decisions from corrupted data |

## Worked Example

A consultation CTA change has a business-defined minimum meaningful lift, but baseline event volume implies a six-month test while the campaign lasts four weeks. The skill rejects the A/B test and recommends moderated user sessions plus a staged rollout with observational monitoring.

For health or high-trust messages, load [message trust and uncertainty experimentation](references/message-trust-and-uncertainty-experimentation.md).

## Read Next

- `marketing-measurement-system` defines the KPI tree.
- `observability` ensures event and performance data are trustworthy.
- `cro-audit` diagnoses candidate problems.
- `monthly-report` communicates decisions without re-analysing the test.
