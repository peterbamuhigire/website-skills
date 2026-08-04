---
name: brand-storytelling
description: Use when an approved brand strategy must become an evidence-based narrative for About pages, case studies, heroes, or campaigns. Use `brand-strategy` to decide positioning and `premium-commercial-writing` when persuasion, SEO, and offer conversion dominate.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Brand Storytelling
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Build truthful brand narratives with a clear audience role, tension, proof, and next step.

<!-- dual-compat-start -->
## Use When

- An About page, case study, hero, founder story, or campaign needs narrative structure.
- The approved brand brief must be expressed through repeatable story principles.
- Raw interviews or project evidence need shaping without inventing drama.

## Do Not Use When

- Positioning and audience are not approved; use `brand-strategy` first.
- The task is mainly offer persuasion, objection handling, SEO, or conversion; use `premium-commercial-writing`.
- There is no evidence for a claimed origin, result, customer quote, or turning point.

## Inputs

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Approved brand brief | `brand-strategy` | yes | Stop and request or create the upstream brief. |
| Story evidence | Interviews, project records, approved quotes, timelines | yes | Produce an interview plan, not a fictional narrative. |
| Page goal and audience action | Content or page brief | yes | Return a story spine only and mark CTA unresolved. |

## Workflow

1. Confirm the audience, page job, approved positioning, and desired action.
2. Use the narrative information-architecture reference to name the audience actor, stakes, tension, proof, choice, consequence, and the organisation's enabling role.
3. Build a fact bank with sources, permissions, dates, and uncertainty.
4. Choose the simplest suitable narrative spine; keep the customer as agent where appropriate.
5. Define situation, tension, choice, action, evidence, outcome, and next step.
6. Draft in the brand's voice, preserving exact approved quotations and qualifying outcomes.
7. Check continuity, claim support, dignity, privacy, readability, and commercial relevance.
8. Stop when a material fact or permission is missing; recover with questions or a clearly marked structural draft.

## Quality Standards

- Every material beat must be verified or explicitly framed as interpretation.
- Narrative serves the page decision; it does not delay the useful answer.
- Customers are not reduced to props, and quotes remain faithful to source.
- Specific details earn their place and have permission where needed.
- The story spine can be mapped to page hierarchy, proof, CTA, accessibility, and a measurable audience action.

## Anti-Patterns

- Making the brand the hero of every story. Fix: show the customer's agency and the brand's enabling role.
- Inventing a dramatic founder hardship. Fix: use verified stakes or omit the arc.
- Forcing every case study into a hero's journey. Fix: choose the shortest structure that explains the decision and result.
- Using an unattributed composite quote as testimony. Fix: paraphrase without quotation marks or obtain approval.
- Ending with sentiment but no page action. Fix: connect the earned meaning to one relevant next step.
- Treating an emotional beat as permission to exaggerate a claim. Fix: attach source, permission, and status to every material beat.
- Using a dramatic image that hides the page task or excludes people. Fix: route visual decisions through design-system and accessibility review.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Narrative brief and story spine | Writer, designer, and page builder | Names audience, page job, beats, evidence, voice, CTA, and exclusions. |
| Draft narrative | Content owner | Every claim and quote traces to the fact bank; structure supports the page goal. |
| Reusable story rules | Content team | Defines repeatable voice, protagonist, proof, tension, and ending conventions. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Story fact bank | Fact, source, permission, status | No material beat lacks a source or qualification. |
| Claim and quote check | Line-level review record | Exact quotes, results, names, and dates are verified. |

## Capability Contract

Default to read-only analysis of source material. Editing requires authorisation. Publishing, contacting interviewees, using personal stories or testimonials, and changing approved quotations require explicit authority and permissions.

## Degraded Mode

When the brand brief, sources, or permissions are unavailable, return interview questions and a structural outline. Mark unsupported beats `not assessed`; never fabricate dialogue, results, or consent.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Page needs rapid trust | Lead with outcome and proof, then concise origin | Self-indulgent chronology |
| Case has a consequential decision | Use situation-choice-action-result | Decorative drama with no insight |
| Evidence or permission is weak | Anonymise, qualify, or omit | Fabrication and privacy harm |

## Worked Example

For a clinic case study, open with the verified appointment backlog, explain the staff's choice to simplify triage, show the site's supporting role, and report only the measured reduction supplied by the clinic. Do not invent a patient quotation; acceptance requires written permission for any named staff or patient detail.

<!-- dual-compat-end -->

## References

- `references/narrative-spine-and-emotional-arc.md` - narrative selection and emotional pacing.
- `../orchestration/website-builder/references/narrative-information-architecture-and-empathy.md` - translate audience empathy and narrative beats into page architecture, proof, choice, recovery, and measurement.
- `references/story-templates.md` - practical page and case-study structures.
- `references/content-strategy.md` - channel and content-system application.
- `references/legacy-guidance.md` - preserved story frameworks.
