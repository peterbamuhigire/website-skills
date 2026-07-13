---
name: local-in-person-acquisition
description: "Use when planning ethical face-to-face acquisition for a niche local web studio through territories, short audits, walk-in conversations, follow-up, and pipeline tracking. Use `agency-positioning` to choose the niche and `premium-sales-conversation` after qualification."
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Local In-Person Acquisition
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Planning a local client-acquisition push for a niche web design / branding studio.
- Building a territory plan and daily prospecting cadence for one city or zone.
- Preparing what to say walking into a business cold, and what to leave behind.
- Using a free quick website audit as the reason to start a conversation.
- Handling the standard SMB objections at the doorstep or counter.
- Designing the follow-up sequence after a first in-person contact.
- Tracking the in-person pipeline (visits, conversations, meetings, sales).

## Do Not Use When

- The acquisition channel is inbound, paid ads, cold email, or content marketing
  (use `they-ask-you-answer`, `social-media`, or `seo`).
- The task is choosing or validating the niche itself (use
  `agency-positioning/references/niche-selection-rubric.md` first — niche before doors).
- The task is the sales conversation *after* a qualified lead is sitting down with you
  (use `premium-sales-conversation` and `agency-positioning` proposal references).
- The task is building the audit deliverable as a paid product (use
  `seo-audit` and `agency-positioning/references/premium-audit-offers.md`).

## Inputs

- The chosen niche and city/zone (from `agency-positioning`).
- A reachable prospect list, or the means to build one by walking a defined area.
- One portfolio piece or a niche-relevant mockup to show on a phone or tablet.
- A repeatable free-audit checklist (see `references/5-minute-audit-checklist.md`).

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Approved niche, territory, and no-go rules | `agency-positioning` and local plan | yes | Stop route design. |
| Verifiable prospect and website facts | Public evidence and observation | yes | Do not make an audit claim. |
| Contact, consent, safety, and CRM rules | Agency operations | yes | Draft only; do not visit or contact. |

## Workflow

1. **Confirm the niche and territory.** Acquisition starts only after the niche
   passes the guardrail in `agency-positioning`. Map the zone: cluster the
   target businesses by street/area density so a day's route is walkable.
2. **Set the daily cadence.** Target 25–50 in-person contacts per active
   prospecting day. Track *conversations*, not just doors — a contact only
   counts when you speak to a person. See `references/cadence-and-crm.md`.
3. **Lead with the audit, not the pitch.** Run the 5-minute audit on the
   prospect's current site (or note its absence) before or during the visit, so
   the opening is an observation about their business, not a sales line. See
   `references/5-minute-audit-checklist.md`.
4. **Open, qualify, and reach the decision-maker.** Use the scripts in
   `references/walk-in-pitch-scripts.md`. Ask directly who owns the website
   decision; insist on a real conversation, not "send me an email".
5. **Show, don't tell.** Show one relevant before/after or a quick mockup built
   for a business like theirs. Leave a one-page leave-behind with a single next
   action.
6. **Handle objections with the bank.** Use `references/objection-bank.md` for
   the five SMB classics. Acknowledge, explore, then respond — never argue.
7. **Follow up on a schedule.** Run the Day 1 / 3 / 7 / 14 sequence in
   `references/cadence-and-crm.md`. Most deals need five or more touches; one
   visit is a start, not a close.
8. **Log every interaction and qualify with BANT.** Record the visit, the
   person, the outcome, and the next action the same day. Qualify Budget,
   Authority, Need, Timeline at the doorstep.
9. **Read the pipeline weekly.** Review contact rate, conversation rate,
   meeting rate, and close rate weekly, not monthly — the cycle is short enough
   that monthly review wastes a month of correction.

8. Stop on refusal, unsafe access, or unverifiable evidence; recover by suppressing contact or returning to desk research.

## Quality Standards

- **Niche-first.** Every visit is to a business inside the chosen niche. "Anyone
  on the street" prospecting dilutes the positioning and the referral compounding.
- **Conversation is the unit.** Measure conversations and their outcomes, not
  doors knocked. A reachable 25 beats an unreachable 60.
- **Respect the owner's time.** Never pitch during a rush. For a busy
  brick-and-mortar business, be a customer first; ask when the owner is free.
- **One next action per contact.** Every leave-behind and every follow-up asks
  for exactly one thing (a 15-minute slot, a reply, a look at a mockup).
- **Honest audits.** The audit names real, checkable issues (mobile, speed, SSL,
  stale footer year, missing call button). No invented problems, no fake urgency.
- **Five-touch persistence.** Do not record a "no" until the follow-up sequence
  is exhausted or the prospect explicitly opts out.

## Anti-Patterns

- Pitching the service in the first sentence instead of opening with an
  observation or a free offer.
- Leaving a card during a rush and calling it a touch. Fix: count only a real conversation or consented follow-up.
- Quoting at the doorstep. Fix: qualify the business problem and decision process first.
- Knocking every business in sight. Fix: stay within the approved niche and territory.
- Following up after refusal. Fix: stop immediately and record suppression.
- Logging door count as progress. Fix: report defined conversations, meetings, and qualified opportunities.
- Reusing a generic pitch. Fix: name the prospect's actual context and observed issue.

## Outputs

- A territory map and route plan for the niche in one city/zone.
- A daily prospecting log (contacts, conversations, outcomes, next actions).
- A reusable walk-in pitch, opener, and one-page leave-behind.
- A completed 5-minute audit per serious prospect.
- A weekly pipeline read: contact / conversation / meeting / close rates.

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Territory and route plan | Acquisition owner | Names niche, boundaries, safe cadence, no-go conditions, and daily owner. |
| Audit and conversation record | Sales owner | Separates observed website facts from hypotheses and records consented next action. |
| Pipeline register | Agency leadership | Every touch has date, outcome, permission, next action, owner, and source. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Prospect audit | Dated observation with URL or visible evidence | No scare claim or invented loss estimate. |
| Funnel review | Visits, conversations, meetings, sales with definitions | Rates reconcile to raw records. |

## Capability Contract
Planning defaults to read-only. Visits, calls, messages, CRM changes, location tracking, photography, or collection of personal data require explicit authority, respectful consent, and local safety rules.

## Degraded Mode
Fallback if maps, prospect evidence, safe access, or contact authority are unavailable: return a desk-based territory hypothesis and audit template. Mark conversion and on-site facts `not assessed`.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Niche and dense safe territory are validated | Run a bounded route pilot | Random door-knocking |
| Prospect is busy, refuses, or asks to stop | Leave immediately and suppress follow-up | Harassment and trust damage |
| Audit reveals a verifiable priority and interest | Book qualified discovery | Doorstep quoting without diagnosis |

## Worked Example
Visit ten owner-operated lodges on a pre-approved route outside peak check-in time. Show one verified mobile booking friction point, ask permission to send the audit, and log a next step. A refusal ends the sequence and enters the suppression field.

<!-- dual-compat-end -->

## References

- `references/walk-in-pitch-scripts.md` — the 30-second pitch, the 10-second
  opener, free-offer openers, reaching the decision-maker, the leave-behind, and
  what to show on the phone/tablet.
- `references/5-minute-audit-checklist.md` — the seven-point quick audit used as
  the door-opener, and how it feeds `seo-audit` and a paid engagement.
- `references/objection-bank.md` — scripted, non-arguing responses to the five
  SMB objections plus "no budget", using the Acknowledge-Explore-Respond pattern.
- `references/cadence-and-crm.md` — daily contact targets, the Day 1/3/7/14
  follow-up sequence, doorstep BANT qualification, CRM logging, and the weekly
  pipeline KPIs.
- `references/sources.md` — attributed sources (Jeb Blount, RAIN Group, SPOTIO,
  SiteSwan, QCFixer) with confidence flags.

## Notes

- This skill is the "GO IN PERSON" channel: deliberately the opposite of cold
  email / voice-bot outreach, which buyers increasingly tune out.
- Niche selection is upstream (`agency-positioning/references/niche-selection-rubric.md`);
  the paid audit product and proposal are downstream (`agency-positioning`,
  `premium-sales-conversation`); referrals from happy in-person clients are
  handled by `referral-program`.
- Africa calibration: brick-and-mortar SME density is high in trading centres and
  markets; relationship-first, in-person norms favour this channel. Frame price in
  the local market band and accept mobile-money payment realities — see
  `../../orchestration/africa-excellence/SKILL.md`.
- This skill has no bundled scripts; the workflow is documentary.
