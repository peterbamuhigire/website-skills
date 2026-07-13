---
name: launch-campaigns
description: Use when sequencing an established offer through prelaunch, launch, close, and follow-up across a website, email, WhatsApp, or blog. Use `authority-offers` when the offer itself is undefined and `sales-copywriting` for deep page persuasion.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Launch Campaigns
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- The brief includes a launch window, deadline, waitlist, event, cohort, enrolment period, announcement, relaunch, or offer push.
- The website needs coordinated prelaunch, launch, and follow-up assets instead of a single isolated page.
- The task needs campaign sequencing tied to website pages, blog content, email, WhatsApp, or CTA routing.

## Do Not Use When
- The work is only evergreen page copy with no campaign timing.
- Another narrower skill already owns the task and no sequencing is required.
- The offer has no defined audience, offer, proof, or next step yet.

## Inputs

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Approved offer, audience, goal, and dates | Offer owner or campaign brief | yes | Stop; route undefined offers to `authority-offers`. |
| Proof and objection inventory | Case studies, sales notes, brand brief | yes | Qualify claims and use an education-first sequence. |
| Channel access and consent rules | Channel owners and subscriber records | yes for activation | Draft only; do not send, publish, or import contacts. |

## Workflow
1. Clarify the campaign goal, audience segment, and fixed dates before drafting.
2. Define the campaign sequence: prelaunch, launch, follow-up, and close.
3. Map each stage to the right asset and CTA.
4. Write only the assets required for the current stage and channel mix.
5. Check tone, proof, and urgency against the sector's trust requirements.
6. Verify dates, links, consent, owners, and rollback before activation; stop and issue a gap list if any release-critical item is unresolved.

7. Stop activation on an unresolved date, consent, owner, or link; recover by correcting and rechecking the release register.

## Quality Standards
- Sequence must feel coherent across channels and pages.
- Urgency must be real, evidenced, and proportionate.
- Launch copy must teach, qualify, and persuade without sounding theatrical or manipulative.
- Every asset must point to one clear next step.

## Anti-Patterns
- Copying infoproduct hype into a trust-sensitive sector. Fix: use the buyer's decision process and verified proof.
- Inventing scarcity or a countdown. Fix: state the real enrolment, capacity, or event constraint.
- Asking for high commitment before earning trust. Fix: sequence education and proof before the sales ask.
- Drafting channels independently. Fix: maintain one message and CTA map across every asset.
- Sending without consent or link checks. Fix: verify audience permissions, destinations, owners, and suppression rules.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Campaign sequence and message map | Copy and channel owners | Every stage has a date, audience, message job, proof, CTA, destination, and owner. |
| Asset and release checklist | Production and launch owner | Required assets, approvals, links, consent checks, and rollback are observable. |
| Measurement brief | Commercial owner | Names source, baseline, campaign event, success measure, and review date. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Release checklist | Dated pass/fail register | No unassessed item is recorded as passed. |
| Claim and link register | Claim/source and CTA/destination pairs | Every claim and public destination has been checked. |

## Capability Contract

Read and search are required. Editing is limited to authorised campaign files. Sending messages, publishing pages, importing contacts, changing tracking, or spending on ads requires explicit authority and a final audience/date confirmation.

## Degraded Mode

Fallback if required capabilities are unavailable:

Without channel access, live dates, proof, or analytics, return a draft sequence with affected checks marked `not assessed`. Never simulate a send, publish action, consent pass, or performance result.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Offer or audience is not approved | Stop and route upstream | Coordinated promotion of the wrong proposition |
| Proof is thin or trust is high-stakes | Lead with education and verified process | Hype that damages credibility |
| Fixed date and consented audience exist | Use timed multi-channel sequence | Unnecessary urgency and channel spam |

## Worked Example

For a Kampala training cohort closing on 30 September, map a proof-led article to a waitlist email, a launch page, two consented WhatsApp reminders, and a final enrolment notice. Acceptance: each asset uses the same cohort dates and application URL; the close message is suppressed for confirmed applicants.

<!-- dual-compat-end -->

## References
- `references/website-launch-sequence-framework.md` — primary framework for campaign stages, asset mapping, CTA posture, proof use, and Africa-adapted launch guidance.

## Notes
- Route to `sales-copywriting` for deep page persuasion work, `blog-writer` for launch-supporting articles, and `website-builder` when the launch work changes the actual site build.


