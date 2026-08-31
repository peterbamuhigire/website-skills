---
name: content-writing
description: Use when website pages or interface copy need clear message hierarchy, genuine voice, scannable structure, and evidence-aware editing; use `blog-writer` for articles and `sales-copywriting` for persuasion frameworks.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Content Writing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Turn business facts and audience needs into clear website copy with a defined page job, credible claims, and an implementable structure.

<!-- dual-compat-start -->
## Use When

- Drafting or revising home, about, service, contact, FAQ, support, or interface copy.
- Existing copy is generic, unclear, internally focused, or disconnected from the page's purpose.
- A page-builder needs approved headings, body copy, proof, CTAs, and state microcopy.

## Do Not Use When

- The deliverable is a full article; use `blog-writer`.
- The core task is direct-response persuasion or a long sales page; use `sales-copywriting` or `long-form-sales-copy`.
- The task is only native-language execution; pair with the applicable language skill after the message is sound.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Page goal, audience, and next action | Sitemap, brief, or experience map | yes | Stop polishing and return the missing page-strategy decisions. |
| Offer, process, proof, and business facts | Client files or interviews | yes | Draft only supported sections and label proof gaps. |
| Voice, language, and sector constraints | Brand and language owners | conditional | Use restrained neutral prose and list unresolved choices. |
| Layout or component constraints | Design/page owner | conditional | Return modular copy blocks and note assumed limits. |

## Workflow

1. State the page job: rank, educate, compare, prove, convert, reassure, onboard, or retain.
2. Stop if the audience, offer, or next action is unclear; return the decisions needed.
3. Build the message hierarchy: orientation, problem, promise, proof, process, objections, and next step.
4. Mine supplied customer language and business evidence; separate fact, claim, proof, and inference.
5. Draft headings and sections around reader questions using [the message hierarchy framework](references/message-hierarchy-framework.md).
6. Add proof close to the claim it supports and write CTA text that describes the next step.
7. Cover empty, error, confirmation, and reassurance copy for relevant forms or interactions.
8. Edit for clarity, rhythm, scannability, regional language, and [the genuine-writing gate](../premium-commercial-writing/references/genuine-writing-and-ai-slop-gate.md).
9. If proof or layout constraints invalidate the draft, revise the claim or return the gap; do not fill it with slogans.

Recovery: repair the page strategy or proof map, then rerun the message and state review.

## Quality Standards

- Each page has one primary job and a coherent next action.
- Important claims are proved, attributed, softened, or removed.
- The copy contains business-specific offer, audience, process, geography, constraints, or examples.
- Headings carry meaning when scanned without the paragraphs.
- CTA, form, error, and confirmation language set accurate expectations.
- The handoff is broken into implementable sections, not a continuous essay.

## Anti-Patterns

- Polishing a page with no defined job. Fix: resolve strategy before prose.
- Opening with "Welcome" or company history. Fix: orient the reader to their need and available path.
- Inventing testimonials, numbers, credentials, or local facts. Fix: record the proof gap and soften the claim.
- Using generic CTA labels everywhere. Fix: name the action and expected result.
- Applying every writing rule mechanically. Fix: select rules that serve this page and audience.
- Writing only the happy path. Fix: include error, empty, privacy, and confirmation microcopy where relevant.
- Flattening distinctive brand language. Fix: preserve intentional phrases unless they obstruct comprehension or evidence.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Page copy deck | Page builder and approver | Sections, headings, proof, CTA, and component notes are complete and ordered. |
| Claim and proof notes | Client or editor | Material claims point to proof or carry an explicit qualification. |
| Microcopy set | Form and interface owner | Labels, help, error, consent, loading, and confirmation states are covered where applicable. |

## References

- [Legacy detailed guidance](references/legacy-guidance.md) for preserved writing patterns.
- [Message hierarchy framework](references/message-hierarchy-framework.md) for page-level sequencing.
- [Reader empathy and voice of customer](references/reader-empathy-and-voc.md) for objections and buyer language.
- [UX writing pattern library](references/ux-writing-pattern-library.md) for interface states.
- [Business vocabulary](references/business-vocabulary.md) for precise commercial language.
- [Website page writing patterns](../premium-commercial-writing/references/website-page-writing-patterns.md) for premium page types.
- [Human English and reader-centred craft](../../../book-extractions/human-english-craft-synthesis-2026.md) for reader-fit register, grammar, collocation, rhythm, and proof/read-aloud.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Page-purpose statement | One sentence | Audience, page job, and next action are named. |
| Claim-proof map | Inline table or notes | Every material claim has proof status and owner. |
| Editorial acceptance record | Checklist | Clarity, specificity, states, voice, and unresolved gaps are recorded. |

## Capability Contract

Read access to briefs and source material is required. Review defaults to read-only. Editing project copy requires explicit authority. Search or network access may verify current claims; publishing and production changes require separate authority.

## Degraded Mode

When proof, layout context, research, or editing access is unavailable, return the narrowest qualified modular draft plus a gap list. Mark evidence, interface states, and stakeholder approval `not assessed` where applicable.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Page job is unclear | Stop and resolve it | Polished copy with no commercial purpose |
| Claim has strong proof | State it specifically near the proof | Vague credibility |
| Claim lacks proof | Soften, remove, or request evidence | Misrepresentation |
| User input flow exists | Add full-state microcopy | Silent errors and abandonment |
| Conversion structure dominates | Hand off to `sales-copywriting` | Scope collision and weak persuasion |

## Worked Example

Input: a law firm's service page says "We provide world-class legal solutions." Revision: name the relevant matter, who it serves, the firm's documented process, and the consultation next step; omit outcome claims unsupported by case evidence.

For health-institution or public-health content, load [institutional health communication](references/institutional-health-communication.md).

## Read Next

- `premium-commercial-writing` for high-stakes commercial and authority copy.
- `sales-copywriting` for conversion arguments, proof, and resistance handling.
- `page-builder` for implementation into reusable sections and components.
