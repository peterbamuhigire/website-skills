---
name: marketing-measurement-system
description: Use when a premium website needs a KPI tree, event plan, customer-insight loop, loyalty measures, and decision-ready reporting; use `observability` for telemetry implementation and `experimentation` for causal tests.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Marketing Measurement System
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Connect the website's business outcome to behavioural evidence, customer insight, channel contribution, retention, and operating decisions.

<!-- dual-compat-start -->
## Use When

- A new website or retainer needs a measurement architecture and evidence cadence.
- Owners cannot explain whether the website contributes to business outcomes.
- Marketing, sales, CRM, email, paid, referral, or offline data must connect to website behaviour.
- Loyalty and retention need to be designed into the digital experience.

## Do Not Use When

- The request is only to install analytics or alerts; use `observability`.
- A defined hypothesis needs a controlled test; use `experimentation`.
- The client will provide neither access nor approved measurement; renegotiate scope rather than invent a dashboard.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Business model, outcome, strategy, and decision cadence | Business owner | yes | Stop KPI design and return a decision-framing brief. |
| Experience map, sitemap, conversion paths, and offers | Website strategy | yes | Produce only a provisional outcome model. |
| Existing analytics, CRM, advertising, email, and offline sources | Data/tool owners | conditional | Mark source coverage gaps and avoid unsupported historical baselines. |
| Customer cohorts, retention data, targets, and definitions | Finance, sales, product, or marketing owners | conditional | Use hypotheses, not fabricated benchmarks. |
| Consent, privacy, retention, and access constraints | Compliance owner | yes before collection | Block collection designs that lack lawful governance. |

## Workflow

1. State one primary business outcome and the decisions measurement must support.
2. Stop if the outcome is not owned, measurable enough to guide action, or compatible with privacy constraints.
3. Build the KPI tree from business outcome through behavioural drivers to leading indicators using [KPI definitions](references/kpi-tree-and-definitions.md).
4. Define each metric: formula, grain, source, owner, target or decision band, comparison period, latency, and caveat.
5. Map channels to the website and define source/medium, handoff, attribution limits, and offline reconciliation.
6. Specify events against experience stages, including consent, identity, deduplication, and quality checks.
7. Define the customer-insight loop using [customer insight guidance](references/customer-insight-loop.md); do not impose a fixed quantitative/qualitative ratio without evidence.
8. Add loyalty and retention measures appropriate to the business model using [the loyalty plan](references/loyalty-and-retention-plan.md).
9. Design a one-page decision view and an evidence pack for monthly reporting.
10. Run the quarterly review; change priorities or budget only when evidence and authority support the decision.
11. If sources conflict, pause conclusions, reconcile definitions, and record the unresolved variance.

Recovery: repair metric definitions or source lineage, then rerun reconciliation before reporting.

## Quality Standards

- Every KPI has a formula, source, owner, decision use, comparison period, and data-quality caveat.
- Vanity metrics appear only as diagnostic context, never as the primary outcome.
- Events map to a customer stage and a real decision.
- Attribution limits, consent, retention, and identity handling are explicit.
- Retention and loyalty measures match the business model rather than a generic dashboard.
- Reviews end with owned decisions, not unexplained charts.

## Anti-Patterns

- Reporting page views as business success. Fix: connect diagnostic traffic to an owned outcome.
- Copying industry benchmarks as targets. Fix: establish the client's baseline and decision threshold.
- Treating the website as isolated from CRM or offline sales. Fix: define source handoffs and reconciliation.
- Optimising engagement while qualified demand falls. Fix: use outcome and guardrail metrics together.
- Measuring acquisition but ignoring retention in a recurring model. Fix: add cohort and renewal measures.
- Hiding bad or missing data. Fix: show the quality issue and recovery owner.
- Mixing conflicting metric definitions. Fix: create a governed definition and reconcile history explicitly.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| KPI tree and metric dictionary | Business, analytics, and reporting owners | Outcome, drivers, formulas, sources, owners, targets/bands, and caveats are complete. |
| Event and source plan | `observability` and implementation owners | Events, parameters, stages, consent, QA, and source handoffs are specified. |
| Insight and loyalty plan | Marketing and service owners | Cadence, cohorts, methods, owners, and decisions are explicit. |
| Monthly evidence and quarterly review templates | `monthly-report` and leadership | Each view supports named decisions and records data quality. |

## References

- [KPI tree and definitions](references/kpi-tree-and-definitions.md)
- [Customer insight loop](references/customer-insight-loop.md)
- [Loyalty and retention plan](references/loyalty-and-retention-plan.md)
- [Quarterly business review](references/quarterly-business-review.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Metric lineage | KPI-to-source map | Every reported metric is traceable to source and formula. |
| Source-quality register | Table | Access, freshness, completeness, reconciliation, and limitations are recorded. |
| Decision log | Monthly/quarterly record | Evidence, decision, owner, due date, and follow-up measure are explicit. |

## Capability Contract

Read access to business definitions and available data is required. Analysis defaults to read-only. Editing analytics plans or dashboards requires authority. Data collection, CRM changes, customer contact, production mutation, spending, and budget reallocation require explicit owner approval and privacy compliance.

## Degraded Mode

When source access, reliable history, network, or analytics tooling is unavailable, return the narrowest qualified KPI dictionary and instrumentation plan with baselines and data quality marked `not assessed`. Never infer performance or set precise targets from absent data.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Metric changes a named decision | Keep as KPI | Dashboard clutter |
| Metric explains but does not decide | Keep as diagnostic | Vanity metric promotion |
| Sources disagree materially | Reconcile before interpretation | False driver narratives |
| Direct outcome is delayed | Use validated leading indicator with guardrail | Optimising a weak proxy |
| Collection lacks consent or purpose | Remove or redesign | Privacy and trust harm |

## Worked Example

A B2B site receives many form submissions but sales labels few as qualified. The system defines qualified lead rate with CRM ownership, maps form and CRM identifiers, reports the reconciliation gap, and avoids celebrating raw submission growth.

## Read Next

- `observability` implements the telemetry contract.
- `experimentation` tests causal hypotheses.
- `monthly-report` communicates validated monthly evidence.
- `ecommerce-analytics` owns commerce-specific funnels and revenue measures.
