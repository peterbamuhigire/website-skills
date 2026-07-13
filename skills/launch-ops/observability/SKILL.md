---
name: observability
description: Use when a live website needs real-user performance, error tracking, analytics, source health, alerts, and an operator runbook; use `marketing-measurement-system` for KPI design and `deploy` for release promotion.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Observability
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Make website health and user outcomes observable through project-scoped telemetry, actionable alerts, privacy controls, and tested runbooks.

<!-- dual-compat-start -->
## Use When

- A site is approaching launch and needs day-one telemetry and operational ownership.
- A new route, template, form, or interactive feature changes event or error coverage.
- A performance, reliability, or conversion regression needs live evidence.
- Monthly reporting requires source-reachability and event-contract verification.

## Do Not Use When

- The task is a one-time synthetic quality audit; use the relevant quality gate.
- The task is KPI or business-target design; use `marketing-measurement-system`.
- The task is deployment promotion; use `deploy` after telemetry preflight.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Primary domain, routes, critical journeys, and release identity | Project and deploy owners | yes | Return a coverage gap; do not provision blind telemetry. |
| Event taxonomy and KPI/source plan | SEO/measurement owners | yes | Stop analytics implementation until definitions exist. |
| Provider, endpoint, consent, retention, and data-residency decisions | Project/compliance owner | yes | Produce options only; do not collect data. |
| Named on-call owner, escalation path, and runbook | Operations owner | yes for launch | Block launch readiness. |
| Project-scoped credentials and production authority | Secret/release owners | yes for mutation | Stop at configuration and verification plan. |

## Workflow

1. Inventory critical routes, journeys, events, errors, performance signals, sources, and owners.
2. Stop if consent, retention, data routing, on-call ownership, or production authority is unresolved.
3. Record provider decisions and project-scoped boundaries; never share properties or credentials across clients.
4. Implement real-user performance telemetry using [RUM guidance](references/rum-implementation.md), including Save-Data handling and an explicit sampling decision.
5. Implement error tracking with release tags, environment separation, source-map controls, and PII scrubbing using [error-tracking guidance](references/error-tracking.md).
6. Implement analytics events exactly as governed, including consent and deduplication using [analytics integration](references/analytics-integration.md).
7. Configure source-health probes and actionable alerts from [alert thresholds](references/alert-thresholds.md).
8. Write or update the project runbook from [the runbook template](references/runbook-template.md).
9. Preflight in a non-production environment, then verify real production events, errors, performance payloads, alerts, and source health after authorised deploy.
10. If telemetry is silent or malformed, treat the source as unhealthy, investigate consent/network/configuration, and block evidence-dependent reporting.

Recovery: repair the failing source or configuration, then rerun preflight and production verification before reporting.

## Quality Standards

- Every primary route and critical journey has appropriate performance, error, and outcome coverage.
- Telemetry is project-scoped, consent-aware, minimised, and governed by retention policy.
- Errors carry release and environment context without exposing secrets or unnecessary PII.
- Alerts have thresholds, owner, severity, route, and runbook action.
- Source health is tested before reports consume it.
- Sampling decisions account for low-bandwidth and long-tail users and are documented rather than assumed.

## Anti-Patterns

- Shipping analytics without error or performance context. Fix: cover the whole operational signal set.
- Sharing one analytics property across clients. Fix: provision project-scoped isolation.
- Uploading public source maps or PII-rich breadcrumbs. Fix: use private upload and scrubbing controls.
- Creating alerts with no owner or action. Fix: attach severity, route, and runbook step.
- Treating a silent pipeline as zero incidents. Fix: monitor source health and expected event flow.
- Sampling away slow-network users by default. Fix: document representative sampling and inspect segment coverage.
- Reporting from an unreachable source. Fix: mark it unavailable and block the dependent conclusion.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Telemetry implementation and configuration | Deploy and operations owners | RUM, errors, analytics, and source health are project-scoped and observed. |
| Alert and ownership register | On-call operator | Every alert has threshold, severity, owner, route, and runbook action. |
| Operational runbook | Support and incident owners | Diagnosis, escalation, privacy, rollback handoff, and source contacts are actionable. |
| Source-reachability record | Monthly reporting | Each source has an observed status and timestamp. |

## References

- [RUM implementation](references/rum-implementation.md)
- [Error tracking](references/error-tracking.md)
- [Analytics integration](references/analytics-integration.md)
- [Alert thresholds](references/alert-thresholds.md)
- [Runbook template](references/runbook-template.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Telemetry preflight | Test output or captured event records | Expected payloads, consent behaviour, and environment tags are observed. |
| Production verification | Timestamped event/error/performance/source checks | Each critical source is observed after authorised deployment. |
| Alert and runbook test | Test notification and response record | Routing and operator action are demonstrated. |

## Capability Contract

Read and execution access are required for inspection and preflight. Review defaults to read-only. Editing instrumentation, provisioning providers, uploading source maps, network calls, secret use, production changes, alerts, and external notifications require explicit authority and least privilege.

## Degraded Mode

When provider access, network, credentials, production traffic, or alert delivery is unavailable, return the narrowest qualified configuration and verification artefacts with those dimensions marked `not assessed`. Never interpret a silent or inaccessible source as healthy or as zero events.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Current provider meets isolation, consent, and operations needs | Retain and document | Tool churn |
| Provider cannot meet governance requirements | Select an approved alternative | Privacy or tenancy breach |
| Source health fails | Block dependent reporting and investigate | False business conclusions |
| Alert has no actionable response | Redesign or remove it | Alert fatigue |
| Production authority is absent | Stop at preflight plan | Unauthorised collection or mutation |

## Worked Example

A site shows zero form submissions after launch, but the analytics health probe also fails. The report marks the source unavailable rather than claiming zero demand, then follows the runbook to inspect consent, endpoint, and deployment configuration.

## Read Next

- `marketing-measurement-system` defines metrics and event purpose.
- `deploy` owns release promotion and production smoke.
- `monthly-report` consumes reachable validated sources.
- `customer-service-website-ops` owns incident communication and recovery.
