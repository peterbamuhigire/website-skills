---
name: sales-copywriting
description: Use when a website page needs a conversion argument, value proposition, proof sequence, objection handling, risk reduction, or CTA ladder; use `content-writing` for general page clarity and `long-form-sales-copy` for full direct-response assets.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Sales Copywriting
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Build credible persuasion from customer language, a clear offer, proportionate proof, and an honest next step.

<!-- dual-compat-start -->
## Use When

- A landing, product, service, or campaign page needs a stronger conversion argument.
- Headlines, value propositions, proof, objections, guarantees, or CTAs need revision.
- Existing copy is clear but does not help the right buyer decide or act.

## Do Not Use When

- The task is general informational or interface copy with no persuasion problem; use `content-writing`.
- The deliverable is a complete long-form sales letter, VSL, or multi-page direct-response funnel; use `long-form-sales-copy`.
- The offer, audience, or evidence basis is undefined; resolve those inputs before drafting.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Audience, awareness, and traffic source | Commercial brief or analytics | yes | Return the missing audience decisions; do not write for "everyone". |
| Offer, price, terms, and desired action | Offer owner | yes | Stop if the actual exchange cannot be stated accurately. |
| Voice-of-customer, objections, and alternatives | Interviews, reviews, sales/support notes | conditional | Label assumptions and propose message-mining work. |
| Proof, guarantee authority, and claim constraints | Client and compliance owner | yes for claims | Remove unsupported claims or guarantees. |

## Workflow

1. Define the audience, awareness level, traffic context, page goal, and CTA commitment.
2. Stop if the offer or proof burden is unresolved.
3. Mine customer language, objections, desired outcomes, alternatives, and switching risks using [message mining and proof](references/message-mining-and-proof.md).
4. Write the value proposition and test it against specificity, relevance, differentiation, and evidence.
5. Choose the smallest useful persuasion structure: headline/CTA revision, claim-proof sequence, PASTOR, or 4 Ps.
6. Place proof near claims and answer the highest-cost objections before the ask.
7. Add honest risk reduction and CTA reassurance; never invent scarcity, guarantees, or outcomes.
8. Draft variants only when each expresses a meaningful hypothesis.
9. Review with [the professional writing gate](../premium-commercial-writing/references/professional-writing-quality-gate.md).
10. If proof fails, revise the promise and rerun the argument rather than adding hype.

## Quality Standards

- The right buyer can identify the offer, value, evidence, and next step quickly.
- The persuasion level matches awareness, traffic source, purchase risk, and brand.
- Proof is specific, attributable, and adjacent to the claim.
- Objections are answered honestly without manipulative pressure.
- CTA language states the action, expected result, and relevant reassurance.
- Variants differ by a testable message choice, not synonyms.

## Anti-Patterns

- Starting with a framework before understanding the buyer. Fix: mine audience language and objections first.
- Listing features without consequences. Fix: connect each relevant feature to a supported buyer outcome.
- Hiding the action in a generic CTA. Fix: name the next step and reward.
- Using fake urgency or scarcity. Fix: state only verifiable limits and dates.
- Inventing proof, guarantees, or testimonials. Fix: request evidence or reduce the claim.
- Applying PASTOR or 4 Ps mechanically. Fix: select only the structure the buyer decision requires.
- Producing cosmetic variants. Fix: tie each variant to an explicit hypothesis.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Conversion-copy draft or revision | Page owner and implementer | Audience, promise, proof, objections, risk reduction, and CTA are coherent. |
| Message and proof bank | Future campaigns | Entries retain source, audience, and approved-use context. |
| CTA ladder and variants | CRO/experimentation owner | Each CTA matches commitment level and each variant has a hypothesis. |

## References

- [Website messaging framework](references/website-messaging-framework.md) for page structure.
- [Message mining and proof](references/message-mining-and-proof.md) for research.
- [Value proposition and CTA lab](references/value-proposition-and-cta-lab.md) for hypotheses.
- [Headlines](references/headline-mastery.md), [resistance and objections](references/resistance-and-objections.md), and [closing and guarantees](references/closing-and-guarantees.md) for focused branches.
- [PASTOR and 4 Ps](references/pastor-and-4ps.md) when a full persuasion sequence is justified.
- [Legacy detailed guidance](references/legacy-guidance.md) for preserved framework material.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Message-mining record | Source-tagged bank | Customer language, objections, and proof remain traceable. |
| Claim-proof review | Table or annotations | Every material promise has support or a qualification. |
| Variant hypothesis record | Short table | Each variant names the changed belief and expected behaviour. |

## Capability Contract

Read access to offer and evidence is required. Review defaults to read-only; source editing requires explicit authority. Search may verify current claims. Publishing, experimentation, spending, guarantees, pricing changes, and external communications require explicit authority from their owners.

## Degraded Mode

Without customer research, analytics, proof, or editing access, return a qualified message hypothesis and evidence-gathering plan. Do not present an assumed objection, claim, or conversion lift as measured fact.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Low-commitment informational page | Use light claim-proof-CTA structure | Over-selling |
| High-risk purchase with many objections | Use a fuller persuasion sequence | Unanswered buyer resistance |
| Proof does not support promise | Narrow the promise | Misrepresentation |
| Full VSL or long-form funnel requested | Route to `long-form-sales-copy` | Neighbour collision |

## Worked Example

Input: a training provider claims "transform your career" but has only a documented syllabus and instructor credentials. Revision: promise the specific skills and learning format, show those credentials, and invite the buyer to review the next cohort; omit the outcome guarantee.

## Read Next

- `premium-commercial-writing` for premium tone and claim discipline.
- `long-form-sales-copy` for full direct-response assets.
- `cro-audit` for diagnosis after implementation.
- `experimentation` for controlled message tests.
