---
name: agency-client-retention
description: Use when designing post-launch retainers, review cadence, expansion offers, churn controls, recurring-revenue capacity, or client reporting. Use `monthly-report` for one evidence-backed report and `customer-service-website-ops` for incident handling.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Agency Client Retention
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- The task matches this domain: Client pricing, delivery structure, and retention systems for a premium website design and SEO agency. Use when packaging services, setting pricing, onboarding new clients, planning monthly communication, or designing the quarterly strategy review. Covers the Rule of Five Ones pricing architecture, Land-Deliver-Retain model, monthly communication rhythm, Seed the Vision quarterly framework, and performance-based deal structures. Designed for agencies targeting $10,000–$25,000+ website projects with 24-month+ client relationships.
- The user needs domain-specific strategy, writing, or planning in this area.
- A care plan or maintenance retainer needs specifying: off-host backups, monthly site inspection, contact audit, access hygiene, performance scorecard, client grading, or account expansion.

## Do Not Use When
- Another skill is clearly narrower and better matched to the request.
- The task is unrelated to this domain or needs direct implementation instead.

## Inputs
- Business context, target audience, and the artifact or decision being developed.
- Any existing materials, constraints, or supporting references already available.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Signed scope, launch evidence, service history | Delivery and account records | yes | Stop package or renewal advice and reconcile the account. |
| Client outcomes, telemetry, and feedback | Reports, analytics, interviews | yes | Mark performance unassessed and avoid outcome claims. |
| Capacity, costs, margins, and authority | Agency operations | yes | Do not quote or commit a retainer. |

## Workflow
1. Read the current business context and the concrete task to solve.
2. Use only the relevant detailed guidance and references for the request at hand.
3. Produce the strategy, writing, or framework output this skill is responsible for.
4. Check the result for clarity, realism, and handoff readiness.
5. Decide retain, repair, expand, reprice, or exit; stop before commercial commitment without account and finance authority.

## Quality Standards
- Outputs must be specific, usable, and grounded in the available evidence.

## Anti-Patterns
- Generic framework dumps with no decision made. Fix: choose retain, repair, expand, reprice, or exit and name the evidence.
- Inventing facts to complete the output. Fix: mark the account measure `not assessed` and request its source.
- Ignoring the actual audience, offer, or business constraints. Fix: reconcile the recommendation to signed scope, outcomes, and capacity.
- Do not hide recurring unprofitable work. Fix: trace hours and reprice, narrow, automate, or exit.
- Do not propose expansion before resolving a trust breach. Fix: close recovery actions first.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Retention and account plan | Account and delivery owners | Names client outcomes, service package, cadence, risks, owners, margin, and next decision. |
| Review and expansion brief | Client and commercial owner | Uses verified results and one relevant next step without hidden scope. |
| Capacity and revenue model | Agency leadership | Reconciles contracted work, hours, costs, fee, margin, and escalation threshold. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Account health register | Outcome, service, trust, margin, risk, source | Every rating has dated evidence or says `not assessed`. |
| Retention decision log | Decision, owner, rationale, follow-up date | Commercial actions are traceable. |

## Capability Contract
Default to read-only account analysis. Editing plans requires authority. Contacting clients, changing scope or price, issuing credits, renewing, terminating, or spending requires explicit commercial approval.

## Degraded Mode
When telemetry, cost, or client evidence is unavailable, return an account gap register and provisional options. Mark satisfaction, profitability, renewal probability, and performance `not assessed`.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Outcomes and trust are strong; capacity is viable | Renew or offer evidence-linked expansion | Premature upsell |
| Trust or delivery is weak but recoverable | Repair before expansion | Churn accelerated by selling |
| Scope is persistently unprofitable | Reprice, narrow, automate, or exit | Recurring margin erosion |
| Retainer is being designed or renewed | Include the care-plan components (off-host backups with restore tests, monthly inspection, contact audit, access hygiene) and a fast-signal component beside slow-compounding work | Silent site decay and churn in the 90–120-day window |

## Worked Example
A care retainer consumes twice its allowance because content approvals are unmanaged. Reconcile hours and outcomes, repair the approval workflow, then present a priced content add-on or narrower care scope; do not disguise the overrun as goodwill.

<!-- dual-compat-end -->

## References
- [client-site-care-plan.md](references/client-site-care-plan.md) — read when care-plan specification: off-host backups with restore tests, monthly inspection, content streams, contact audit, access hygiene, tiers.
- [performance-retainer-service.md](references/performance-retainer-service.md) — read when selling and delivering site speed as a monthly scorecard, tag review and tune-up service.
- [client-grading-and-contact-plan.md](references/client-grading-and-contact-plan.md) — read when setting AA–D client grades, affordable contact per grade, cost-to-serve triggers and renewal-predicting surveys.
- [account-cube-expansion-sequence.md](references/account-cube-expansion-sequence.md) — read when choosing where an existing client's next piece of work comes from (Account Cube, need-versus-wish test).
- [new-client-assimilation-and-retention-rhythm.md](references/new-client-assimilation-and-retention-rhythm.md) — read when planning the first 120 days after signature and the monthly review call with client homework.
- [key-client-relationship-health.md](references/key-client-relationship-health.md) — read when managing strategic accounts, executive sponsors, multi-threading and trust recovery.
- [retainer-design-and-cost-to-fulfil.md](references/retainer-design-and-cost-to-fulfil.md) — read when designing a fast-signal plus slow-compounding retainer or checking a fee against cost to fulfil.
- Start with `references/legacy-guidance.md` when you need the preserved detailed instructions from the previous skill version (Rule of Five Ones, Land-Deliver-Retain, Seed the Vision).
- Use `references/deal-structures.md` for the engagement pricing architecture and proposal structure inherited from earlier phases.
- Use `references/monthly-report-template.md` for the standard monthly client report format.

Phase 8 references (retainer, automation, and revenue expansion):
- Use `references/retainer-package-catalog.md` when productising or selling retainers — 5 packages (Care, SEO, Content Growth, CRO, Tech Support), fees $750–$3,000/mo, deliverables, SLAs, exclusions, upsell paths, capacity math.
- Use `references/post-launch-review-cadence.md` when planning the 30-day, 90-day, quarterly, and annual review meetings — agendas, deliverables, conversion goals, churn early-warning signals.
- Use `references/expansion-offers-matrix.md` when recommending expansion at a review milestone — 9 productised offers (landing pages, multilingual, content engine, lead magnet, CRO sprint, analytics, sector page, authority talk, re-engagement) with fees, durations, decision matrix.
- Use `references/subscription-economy-model.md` when running the agency itself as a recurring-revenue business — Tzuo's PADRE model, the subscription P&L, MRR/ARR/NRR/GEI metrics, churn types and reduction (Tzuo + Warrillow), the 9 subscription business models mapped to our retainers.
- Use `references/okrs-and-client-reporting.md` when setting internal quarterly OKRs or designing client KPI reports — Doerr's FACTS framework, committed vs aspirational OKRs, CFRs, the strict separation between internal OKRs and client KPIs.
- Use `references/hybrid-agency-operating-model.md` when designing internal operations — Roetzer's productised services, 7-variable pricing formula, RER KPI, capacity math (120–140 hrs/mo per consultant), 17 A-player traits, daily/weekly/monthly rhythm, Client-in-Residence role.
- Use `references/automation-opportunities-backlog.md` when deciding what to automate — 9 prioritised opportunities, 3 automation rules, what not to automate (strategy, case studies, discovery calls, sales follow-ups, authority content), implementation arc by year.
