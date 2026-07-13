---
name: premium-sales-conversation
description: Use when qualifying and diagnosing a premium website opportunity before any quote, proposal, or scope is written. Use `agency-positioning` to define the offer and fee posture, and the proposal engine for regulated bids or formal responses.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Premium Sales Conversation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- A prospect requests a website, ecommerce, web app, or content hub at a fee level that requires premium framing.
- The agency must screen for fit before investing in a proposal.
- A buyer is comparing on price and the agency must surface premium value or walk away.
- The conversation must result in either paid discovery, a signed retainer, a mutual no-fit decision, or a referral.
- An existing client is renewing or expanding scope and the conversation must reframe value before pricing.

## Do Not Use When

- The buyer has fully scoped, validated, premium work and only needs a written quote.
- The conversation is purely technical due diligence with no commercial decision in scope.
- A regulated procurement requires a formal RFP path; in that case route to the proposal engine.

## Inputs

- Prospect's first message, source of lead, and any prior touchpoints.
- The agency's current offer ladder, fee floors, and capacity.
- The agency's published proof: case studies, performance numbers, sector experience.
- A short list of questions the agency will not start work without answers to.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Offer, fee floor, capacity, and no-fit rules | `agency-positioning` and operations | yes | Stop pricing discussion and obtain current boundaries. |
| Prospect context and decision process | Lead record and conversation | yes | Gather context; do not draft a proposal. |
| Verified relevant proof | Published case studies or approved records | conditional | Qualify claims and avoid proof-dependent promises. |

## Workflow

1. Open with role and outcome. State who you are, who the agency serves, and the outcome the conversation will produce ("by the end of this 30 minutes we will know whether we are a fit, and what the next step is").
2. Earn the right to ask. Spend one minute on context the prospect cares about, not a generic agency intro.
3. Diagnose the buyer's situation with behavioural questions: what triggered this, what they have tried, what almost worked, what is at stake if it fails.
4. Frame the problem in their words, then in business terms. State it back. Confirm it.
5. Surface the cost of the status quo. Convert it to a number when possible.
6. Establish premium fit: budget order of magnitude, decision rights, timeline, and operational readiness.
7. Position the premium offer in outcome language, not deliverables. Show one or two proof points that match the prospect's situation.
8. Handle objections from a defensible position, not from anxiety. Use the objection-handling library.
9. Close to a single next step: paid discovery, signed proposal, mutual no-fit decision, or referral.
10. Write the next-step confirmation in the same call or within one business hour. Include the price floor and the date.
11. Stop when authority, budget order, problem, timeline, or readiness remains unknown; recover with paid discovery or a no-fit route.

## Quality Standards

- Every premium sales call ends with a written next step within one business hour.
- The agency walks away from misfit work with the same clarity it uses to close fit work.
- Pricing is anchored to the outcome and the agency's standard, not to the prospect's budget cap.
- Discovery is paid where the cost of designing the answer is non-trivial. Free discovery is reserved for retainer fits and referrals.
- The call surfaces the buyer's verbatim language so it can be reused in copy, proposal, and onboarding.

## Anti-Patterns

- Pitching before diagnosing the buyer. Fix: establish trigger, stakes, attempts, authority, and readiness first.
- Discounting before an objection. Fix: hold the approved fee posture and diagnose the concern.
- Reading from a deck. Fix: use a question path and reflect the buyer's language.
- Replacing qualification with optimism. Fix: record observable fit and no-fit evidence.
- Saying yes to misfit work because the calendar is empty. Fix: close no-fit or refer against the approved rules.

## Outputs

- Written call summary with diagnosis, agreed problem statement, agreed outcome, and price floor.
- Next-step confirmation: paid discovery agreement, proposal scope, no-fit message, or referral.
- Verbatim quote bank for content and copy.
- Updated CRM record: stage, fit score, rationale.
- Any objections that recur fed back to the objection library.

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Qualification record | Sales owner | Records evidence for fit, authority, need, timing, budget order, and risks. |
| Call summary and next step | Prospect and delivery owner | Uses agreed language, one next action, owner, fee posture, and date. |
| Proposal input brief | Proposal team | Contains validated assumptions and explicitly open questions. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision log | Fit/no-fit/discovery decision and rationale | Decision is based on recorded facts, not enthusiasm. |
| Verbatim insight bank | Approved buyer phrases with context | Distinguishes quotes from paraphrase. |

## Capability Contract

Read-only preparation is the default. CRM edits and draft follow-ups require authority. Contacting prospects, booking commitments, offering discounts, agreeing scope, or sending a proposal requires explicit commercial authority.

## Degraded Mode

When the prospect, fee floor, proof, or CRM access is unavailable, return a conversation guide and missing-decision list. Mark qualification and agreement `not assessed`.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Problem and value are clear but scope is not | Offer paid discovery | Giving away design work in a proposal |
| Fee floor or decision authority is incompatible | Close no-fit cleanly | Discount-led misfit engagement |
| Fit, proof, authority, and readiness align | Advance one agreed scope path | Premature multi-option proposal |

## Worked Example

A school requests "a modern website" before term. Diagnose enrolment leakage, content ownership, approval rights, and deadline consequences. If the caller lacks decision authority and fee range is unresolved, do not quote; schedule the decision owner or close no-fit with a referral.

<!-- dual-compat-end -->

## References

- `references/qualification-and-discovery-questions.md` — diagnostic question bank and fit scoring.
- `references/premium-objection-handling.md` — script-level responses to price, timeline, scope, technology, and trust objections.
- `references/premium-pricing-defence.md` — how to anchor and defend premium fees without discounting.
- `references/no-fit-and-referral-scripts.md` — clean exits and high-trust referrals.
