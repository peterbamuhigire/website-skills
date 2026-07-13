---
name: brand-strategy
description: Use when discovery must establish audience, positioning, differentiation, architecture, and a decision-ready brand brief before design or copy. Use `brand-storytelling` after the strategy exists and `agency-positioning` for the agency's own commercial offer.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Brand Strategy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Turn verified business, customer, category, and competitive evidence into a brand brief that downstream design, copy, and page work can use without guessing.

<!-- dual-compat-start -->
## Use When

- A new or repositioned brand needs a shared strategic foundation.
- Design or content teams are making conflicting audience, promise, or tone assumptions.
- Brand architecture, category framing, differentiation, or naming direction requires a decision.

## Do Not Use When

- The approved brief already exists and the task is narrative execution; use `brand-storytelling`.
- The task is the web agency's offer, fees, or qualification posture; use `agency-positioning`.
- The request is only visual styling; route the approved brief to the design-system engine.

## Inputs

| Artefact | Source | Required? | If absent |
|---|---|---:|---|
| Business model, offer, constraints, and decision owner | Client brief and discovery | yes | Stop and issue a discovery gap list. |
| Audience evidence and buying context | Interviews, CRM, research, sales notes | yes | Mark hypotheses and prohibit unsupported audience claims. |
| Competitor and category evidence | Verified market sources | conditional | Produce provisional differentiation and request research. |

## Workflow

1. Confirm the strategic decision, audience, geography, and decision owner.
2. Separate verified facts, stakeholder opinions, and hypotheses.
3. Define category, primary audience, frame of reference, problem, value, proof, and exclusions.
4. Compare credible positioning territories and choose one with an explicit trade-off.
5. Decide brand architecture, personality, voice principles, and promise-to-proof boundaries.
6. Write `docs/brand-brief.md` and record unresolved tests and downstream implications.
7. Stop before design when the decision owner, core audience, or proof boundary is unresolved; recover with a narrowed provisional brief and validation plan.

## Quality Standards

- Make one defensible positioning choice; do not combine incompatible territories.
- Trace claims to evidence and label hypotheses.
- State whom the brand is not for and what it will not claim.
- Give design and copy teams operational language, not adjective clouds.

## Anti-Patterns

- Listing five audiences as equally primary. Fix: choose one buying audience and define secondary users.
- Calling generic virtues differentiators. Fix: tie differentiation to a capability, method, access, proof, or business model.
- Selecting an archetype before positioning. Fix: decide market meaning first, then use archetype only if it clarifies behaviour.
- Inventing customer insight. Fix: label the hypothesis and specify how to test it.
- Writing a mood-board brief. Fix: include category, audience, promise, proof, exclusions, and decision rationale.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| `docs/brand-brief.md` | Design system, storytelling, content, and page teams | Names audience, category, positioning, promise, proof, voice, architecture, exclusions, and unresolved hypotheses. |
| Positioning decision record | Client decision owner | Compares credible options and records why the selected territory wins. |
| Validation plan | Research and commercial owners | Every material hypothesis has an owner, method, and decision consequence. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Evidence register | Claim, source, status, limitation | Distinguishes facts, opinions, and hypotheses. |
| Approval record | Decision, owner, date, conditions | Downstream teams can identify the approved version. |

## Capability Contract

Default to read-only discovery and analysis. Editing the brief requires authority. Customer contact, research recruitment, publishing positioning, changing live brand assets, or claiming stakeholder approval requires explicit authority.

## Degraded Mode

When customer research, competitor evidence, or stakeholder access is unavailable, return a provisional brief with confidence labels and validation questions. Mark market fit `not assessed`.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence supports one distinct buying reason | Commit to that positioning territory | Generic compromise positioning |
| Evidence conflicts across segments | Choose a primary segment or split the offer | One brand promise serving incompatible needs |
| Proof cannot support the desired promise | Narrow the claim or build proof first | Credibility failure in copy and sales |

## Worked Example

A Kampala payroll firm wants to be "trusted, innovative, and professional". Interviews show SME owners value correction before statutory deadlines, while enterprise buyers require integration depth. Choose the SME compliance-recovery territory for the current offer, cite the response workflow as proof, and record enterprise integration as a separate future proposition.

<!-- dual-compat-end -->

## References

- `references/brand-discovery-questions.md` - discovery prompts and evidence collection.
- `references/positioning-frameworks.md` - positioning, architecture, and differentiation choices.
- `references/legacy-guidance.md` - preserved CBBE, mantra, archetype, and brief guidance.
