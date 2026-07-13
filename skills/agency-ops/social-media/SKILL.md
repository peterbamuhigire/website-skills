---
name: social-media
description: Use when planning measurable social-media channels, content, offer-led campaigns, list capture, or retainers tied to a website. Use `launch-campaigns` for a timed multi-channel launch and the social-media engine for platform-specialist execution.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Social Media
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- The task matches this domain: Social media strategy and management tied to measurable business outcomes. Use when a client needs social media built alongside their website, or as a standalone social media audit or campaign strategy. Covers platform selection, content strategy, offer-led social campaigns, retargeting posture, list-building, analytics, and agency pricing structures for social media retainers.
- The user needs domain-specific strategy, writing, or planning in this area.

## Do Not Use When
- Another skill is clearly narrower and better matched to the request.
- The task is unrelated to this domain or needs direct implementation instead.

## Inputs
- Business context, target audience, and the artifact or decision being developed.
- Any existing materials, constraints, or supporting references already available.

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Audience, offer, goal, and website destination | Brand and commercial brief | yes | Stop channel planning and define the conversion path. |
| Channel baseline and content capacity | Account analytics and team | yes | Recommend a limited pilot and mark forecasts unassessed. |
| Consent, access, and approval rules | Channel owner | yes for activation | Draft only; do not publish or import audiences. |

## Workflow
1. Read the current business context and the concrete task to solve.
2. Decide whether the goal is awareness, capture, nurture, or conversion before choosing channels or content.
3. Use only the relevant detailed guidance and references for the request at hand.
4. Produce the strategy, writing, or framework output this skill is responsible for.
5. Check the result for clarity, realism, measurement readiness, and handoff readiness.
6. Stop before publishing, paid spend, account changes, or customer contact without explicit channel authority and final asset approval.

7. Stop activation when proof, consent, destination, or approval is missing; recover with a draft-only test plan.

## Quality Standards
- Outputs must be specific, usable, and grounded in the available evidence.
- Every social plan must name the offer, CTA, destination, and metric.

## Anti-Patterns
- Generic framework dumps with no decision made. Fix: choose the channel role, offer, CTA, and measure.
- Optimising engagement when the goal is leads or revenue. Fix: trace content to a destination and qualified event.
- Inventing facts to complete the output. Fix: mark the claim or baseline `not assessed`.
- Ignoring the audience, offer, or capacity. Fix: constrain platform, cadence, and format to evidence and owners.
- Publishing unverified testimonials or results. Fix: trace every claim to approved proof.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Social channel and content plan | Content and account owners | Names audience, platform role, content pillars, capacity, CTA, destination, cadence, and exclusions. |
| Campaign and measurement brief | Media and analytics owners | Defines offer, audience, events, source, baseline, budget boundary, and review decision. |
| Editorial queue | Content producer | Every item has proof, format, owner, approval, CTA, and status. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Channel rationale | Audience/channel evidence and rejected options | Platform choice is not based on popularity alone. |
| Performance register | Source, period, metric, limitation | Vanity metrics are separated from leads and revenue. |

## Capability Contract
Analysis defaults to read-only. Editing plans or drafts requires authority. Publishing, messaging, account changes, audience imports, retargeting, and paid spend require explicit approval.

## Degraded Mode
Without analytics, account access, or reliable audience evidence, return a small test plan and mark baseline and performance `not assessed`. Never invent reach, conversion, or audience consent.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Audience uses channel and team can sustain it | Assign a defined channel role | Unsustainable platform sprawl |
| Offer and destination are ready | Run a tracked conversion test | Engagement with no business path |
| Proof or consent is missing | Draft, qualify, or stop activation | Misleading claims or unlawful outreach |

## Worked Example
A Kampala law firm has LinkedIn capacity but no verified case-result permissions. Publish educational posts pointing to a consultation guide, not result claims; acceptance requires tagged website visits and qualified enquiry tracking, not follower growth alone.

<!-- dual-compat-end -->

## References
- Use `references/repurposing-and-launch-support.md` when social media must distribute website content, support a launch sequence, or map posts to page-level CTAs.
- Use `references/direct-response-social.md` when the work requires tracked offers, landing pages, retargeting, or measurable social acquisition.

