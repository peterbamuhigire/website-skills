---
name: customer-service-website-ops
description: Use when designing post-launch website support triage, escalation, recovery language, and retention operations. Use `service-blueprint-website-delivery` for end-to-end delivery design and `agency-client-retention` for commercial renewal strategy.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Customer Service Website Ops
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Designing or upgrading the support layer attached to a premium website or retainer.
- Writing customer-facing language for triage, recovery, refunds, escalations, or churn risk.
- Training a small agency team or a client's internal team to handle service interactions consistently.
- Converting recurring complaints into structural fixes via the service blueprint.
- Re-engaging a client after a missed SLA, a bug, an outage, or a public mistake.

## Do Not Use When

- The interaction is a sales conversation, not a service one. Use `premium-sales-conversation`.
- The work belongs to the client's existing customer service team and they have a stronger SOP.
- The complaint is legal in nature and must be routed to counsel before any agency response.

## Inputs

- The service blueprint and SLA matrix for the engagement.
- The recent ticket and complaint history, if any.
- The client's brand voice and service tone.
- The retainer scope and exclusion list.
- The internal escalation matrix and on-call rota.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Service scope, SLA, and exclusions | Signed agreement and blueprint | yes | Acknowledge receipt only; stop promises or remedies. |
| Incident or request evidence | Ticket, logs, monitoring, customer report | yes | State what is known and begin evidence collection. |
| Escalation owners and brand tone | Operations and brand owners | yes | Use neutral holding copy and escalate ownership gap. |

## Workflow

1. Triage the interaction. Identify whether it is a question, a defect, a service breach, an escalation, a churn risk, or a hostile interaction.
2. Match the interaction to the SLA target. State the target back to the customer in the first reply.
3. Use the service language pattern: acknowledge → be specific about what happened → state the next step → commit to a time → name a person.
4. Resolve at the lowest competent level. Escalate only when SLA is at risk or scope is unclear.
5. Close the loop in writing. Send the resolution summary even when the interaction was verbal.
6. Log the interaction with the structural cause. Patterns route to the service blueprint for permanent fix.
7. Run a recovery gesture only when the breach was real and customer trust is at risk; never as a default discount.
8. Feed retention data to `agency-client-retention` and `monthly-report`.
9. Stop before refund, public statement, contractual admission, or scope expansion without the authorised owner; recover with a timed holding update.

## Quality Standards

- Every customer-facing message identifies a person, a next step, and a time.
- Apologies are specific and one-time. They do not repeat in the same thread.
- "Sorry" is followed by "what we are doing", not by another "sorry".
- Service language is plain, accountable, and locally appropriate. Avoid corporate softening that hides the agency.
- Recovery gestures are proportional and tracked. Default discounts erode margin and train poor behaviour.
- Internal handoffs are written, not verbal. The customer must not have to re-explain the issue at each step.
- Recurring complaints become structural changes within one quarter or are escalated to leadership.

## Anti-Patterns

- "We are sorry for any inconvenience this may have caused" — generic, passive, low-trust.
- Apology spirals with no concrete action. Fix: apologise once, then give the recovery step and time.
- Letting one loud customer dictate scope changes. Fix: separate recovery from an authorised change request.
- Treating tickets as a queue to clear. Fix: log structural cause and route recurring defects to the blueprint.
- Hiding bad news behind delay. Fix: send a factual holding update before the customer has to chase.
- Treating a reporting customer as the problem. Fix: protect respectful escalation and investigate the signal.

## Outputs

- Service triage matrix with SLA per interaction type.
- Customer-facing message templates: acknowledgement, holding update, resolution, recovery, escalation, exit.
- Internal escalation matrix and on-call rota.
- Monthly service report covering volume, SLA compliance, structural fixes shipped, and trust signals.
- Updated service blueprint cells where structural fixes were made.
- Recovery and retention gestures tracked with cost and outcome.

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Triage and response record | Customer and support owner | Names severity, evidence, owner, next action, and next update time. |
| Recovery decision | Account and finance owners | Links verified breach, proportional remedy, authority, cost, and follow-up. |
| Structural improvement entry | Blueprint and retention teams | Recurring cause has an owner, due date, and verification condition. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| SLA timeline | Timestamped event log | Separates observed facts, customer statements, and pending checks. |
| Closure evidence | Resolution test and customer update | No unresolved check is called closed. |

## Capability Contract

Default to read-only triage. Ticket edits and drafted messages require service authority. Sending messages, issuing refunds or credits, admitting liability, changing production, or making public statements requires explicit approval.

## Degraded Mode

Without logs, account history, or an authorised owner, draft a timed holding update. Mark root cause and SLA compliance `not assessed`; never invent a resolution.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Safety, privacy, security, or legal impact | Escalate immediately and limit disclosure | Harmful informal resolution |
| Verified service breach with trust loss | Correct, explain, and consider proportional recovery | Empty apology or automatic discount |
| Request is outside scope | Explain boundary and offer a change path | Silent scope expansion |

## Worked Example

After a contact-form outage, acknowledge the verified submission window, name the engineer and next update time, restore and test the path, then notify affected customers where records permit. Do not promise compensation until the account owner confirms impact and authority.

<!-- dual-compat-end -->

## References

- `references/service-language-patterns.md` — phrasing for acknowledgement, holding, resolution, recovery, escalation, refund, and exit.
- `references/triage-and-escalation-matrix.md` — interaction types, SLAs, and ownership.
- `references/recovery-and-retention-gestures.md` — proportional recovery, when to use, when to refuse.
- `references/post-launch-support-runbook.md` — first 90 days after launch, the period premium relationships are won or lost.
