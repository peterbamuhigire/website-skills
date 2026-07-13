---
name: design-reference
description: Use when analysing client-supplied reference or competitor websites into an implementation-facing design direction; do not use for defining tokens or building pages, which belong to design-system and page-builder.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Design Reference
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use when
- A client supplies sites they admire and needs those preferences translated into design decisions.
- A premium engagement needs competitor patterns, trust signals, differentiation, or a structured reference worksheet before `design-system`.

## Do not use when
- The task is token, typography, colour, or component specification; use `design-system`.
- The task is production page implementation; use `page-builder` after direction is approved.
- No URL, capture, or inspectable comparison exists; request evidence before analysis.

## Required Inputs
| Input | Source | Required | If absent |
|---|---|---:|---|
| Reference URLs and what the client admires | Client brief | yes | Stop and request at least one reference or a named comparison set. |
| Audience, offer, sector, and brand constraints | Discovery artefacts | yes | Produce only a qualified observation log; do not infer positioning. |
| Existing site or competitor set | Project files or research | no | Label the work inspiration analysis, not competitive analysis. |

## Workflow
1. Confirm the comparison question, audience, constraints, and inspectable sources; stop if none exists.
2. Inspect the relevant pages and states at agreed viewports, recording URLs and observed facts separately from inference.
3. Classify each useful pattern as adopt, adapt, or reject using the decision rules.
4. Synthesize page, trust, content, interaction, and visual implications without copying brand assets.
5. Validate traceability and hand the approved direction to `design-system`.
6. Recovery: if a source becomes inaccessible, preserve captured evidence, mark affected checks unassessed, and request an equivalent source.

## Quality standards
- Recommendations distinguish observation, inference, and client preference and cite the exact source/page/state.
- The synthesis names adopt/adapt/reject decisions and gives downstream implementation implications.
- Unknown behaviour remains unassessed; no competitor claim is inferred from visual similarity.

## Anti-patterns
- Auditing without a comparison question. Fix: name the audience decision and lens first.
- Recording taste words without evidence. Fix: cite the exact URL, state, and pattern.
- Copying another brand. Fix: abstract the principle and document a differentiated adaptation.
- Treating a screenshot as interaction proof. Fix: inspect live or mark it not assessed.
- Recommending an infeasible pattern. Fix: test brand, content, accessibility, and technical constraints.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not copy a reference site's styling; extract the underlying pattern and explain fit.
- Do not treat screenshots as proof of responsive or interactive behaviour; verify or mark it unassessed.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| `docs/design-reference.md` | `design-system` and project owner | Names adopted, adapted, and rejected patterns with URL/page evidence and rationale. |
| Competitor worksheet, when scoped | Positioning and UX work | Required rows are complete and unknown values are labelled, not guessed. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Reference observation register | URL, page/state, observation, implication | Every recommendation traces to a viewed source or is marked as an inference. |

## Capability Contract
Default to read-only browser and file inspection. Creating the design-reference artefact is allowed when requested; never edit a source website, publish, purchase access, or reuse protected assets without explicit authority.

## Degraded Mode
If browsing, authentication, rendering, or responsive inspection is unavailable, analyse only supplied captures or files, list unassessed states, and do not report them as passes. If no inspectable evidence exists, stop with the exact evidence request.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Pattern supports the audience goal and brand | Adopt with an implementation rationale | Taste-based copying |
| Pattern conflicts with constraints | Adapt and record the constraint | Infeasible direction |
| Pattern depends on unverified behaviour | Mark unassessed and request evidence | False certainty |
| Pattern is distinctive to another brand | Reject or abstract the principle | Imitation and IP risk |

## Worked Example
Given three law-firm references, record that two expose sector-specific proof beside the first enquiry CTA, adapt that principle to verified client matters, and reject copying their imagery or typography. Give `design-system` a proof-placement rule, not a mood-board adjective.

## References
- Use `references/competitor-analysis-worksheet.md` to analyse competitors as positioning and trust inputs, not just design inspiration.
- Use `references/research-synthesis-template.md` to turn reference and sector analysis into differentiated design direction.

<!-- dual-compat-end -->
## Canonical worksheet format

For premium engagements ($20k+), use Levy's 19-column competitive matrix as the canonical format. See `references/levy-competitive-matrix.md`. Local sector adaptations live in the "Local additions" subsection of `references/competitor-analysis-worksheet.md`.

Minimum data set: 5 direct + 3 indirect competitors fully filled, with A–F heuristic grades and a 1-page distilled brief.
