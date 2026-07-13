---
name: monthly-report
description: Use when producing an evidence-backed monthly website or SEO client report from live telemetry and project logs. Use `agency-client-retention` for account strategy, `ecommerce-analytics` for commerce diagnosis, and `seo-audit` for technical SEO review.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Monthly Report
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- The task matches this domain: Generate a complete professional monthly client report from raw data. Use when producing monthly reports for website design and SEO clients. Claude gathers data through a structured interview, writes plain-English commentary on every metric, drafts the Executive Summary, What We Did, and Next Month Plan sections, then outputs a formatted markdown report ready to copy into a PDF or email. Integrates with agency-client-retention (template and rhythm), ecommerce-analytics (metrics framework), and seo-audit (SEO commentary).
- The user needs domain-specific strategy, writing, or planning in this area.

## Do Not Use When
- Another skill is clearly narrower and better matched to the request.
- The task is unrelated to this domain or needs direct implementation instead.

## Inputs
- Business context, target audience, and the artifact or decision being developed.
- Any existing materials, constraints, or supporting references already available.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Target month and client outcomes | Account owner | yes | Stop and confirm reporting period and audience. |
| Reachable telemetry with metric definitions | Analytics and runbook | yes | Refuse metric reporting and file a source gap. |
| Dated change, decision, incident, and experiment logs | `project-log/` | yes | Report no activity claim without records. |

## Workflow
1. Confirm the target month with the user (default: calendar month just ended).
2. **Pre-flight the live telemetry sources.** Per
   `observability/references/analytics-integration.md`, confirm the
   analytics provider is reachable and the RUM endpoint is responding.
   If any source is unreachable, **refuse to render** — do not fall back
   to operator-narrated metrics. File an incident and resolve before
   running the skill.
3. Read `project-log/CHANGELOG.md` and filter entries to the target month. If the log
   does not exist or the month has no entries, stop and follow the recovery rules in
   `references/project-log-integration.md` — never fabricate activity.
4. Read every file in `project-log/decisions/`, `project-log/incidents/`,
   and `project-log/experiments/` dated inside the target month. Read the
   prior month's `project-log/monthly/YYYY-MM.md` if present.
5. Generate the monthly roll-up at `project-log/monthly/YYYY-MM.md` using the format in
   `templates/project-log-template.md`. This is the raw material for the report.
6. Generate the client-facing report from the roll-up using `commentary-formulas.md` for
   plain-English translation of metrics. Every metric cites the live
   source that produced it. Apply `report-qa-checklist.md` before delivery.
7. Output as markdown ready for PDF export or email. Confirm every metric in the report
   traces back to a log snapshot dated inside the target month **and** to
   a live telemetry source named in the project runbook.

## Quality Standards
- Outputs must be specific, usable, and grounded in the available evidence.

## Anti-Patterns
- Generic framework dumps with no decision made. Fix: state the measured implication and next owner.
- Inventing facts to complete the output. Fix: mark the metric `not assessed` and name its missing source.
- Ignoring the actual audience, offer, or constraints. Fix: write to the client's agreed outcomes and decision cadence.
- Do not render a report when a telemetry source is unreachable. A report
  with narrated metrics in place of live data is drift; refuse and file an
  incident.
- Re-running experiment analysis inside the report. Fix: surface the decided result from the experiment logbook; `experimentation` owns analysis.
- Comparing mismatched periods or definitions. Fix: reconcile dates, filters, currency, and metric semantics first.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Monthly roll-up | Account and audit owners | Every activity, incident, and experiment is dated and source-linked. |
| Client report | Client decision-makers | States outcome, movement, cause limits, work done, risks, and next actions in plain language. |
| Data-gap register | Telemetry and account owners | Names unavailable source, affected claim, owner, and recovery action. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Metric lineage | Metric, definition, source, period, filter | Every reported number has reproducible provenance. |
| QA record | Completed report checklist | Unreachable or unassessed sources are not recorded as passed. |

## Capability Contract
Default to read-only reporting. Writing the report requires authorised project files. Changing telemetry, correcting source data, sending the report, or representing client approval requires explicit authority.

## Degraded Mode
If live telemetry or required logs are unavailable, do not render a performance report. Return the data-gap and incident record plus the non-metric sections that can be supported; mark performance `not assessed`.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Sources reachable and definitions reconcile | Render the report | Unsupported metric narrative |
| Source is unavailable or period mismatches | Refuse affected metrics and recover source | Narrated or incomparable data |
| Experiment has a logged decision | Report the decision, not a new analysis | Conflicting experiment conclusions |

## Worked Example
If Search Console is reachable but the conversion endpoint is down, report verified search visibility only, open a telemetry incident, and mark lead performance `not assessed`. Do not infer enquiries from clicks.

<!-- dual-compat-end -->

## References
- `references/project-log-integration.md` — the contract between this skill and the client project's `project-log/` directory. Start here.
- `references/commentary-formulas.md` — plain-English translation patterns for metrics.
- `references/report-qa-checklist.md` — pre-delivery quality gate.
- `references/legacy-guidance.md` — preserved detailed instructions from the previous skill version.
- `templates/project-log-template.md` (repo root) — the log format this skill reads from.
- `observability/references/analytics-integration.md` — source-reachability
  pre-flight contract.
- `observability/references/alert-thresholds.md` — the thresholds that
  become the month's narrative when an alert has fired.
- `experimentation/references/experiment-logbook-template.md` — the
  experiment log the report surfaces decisions from.
- This skill has no bundled scripts. Execution is documentary.

