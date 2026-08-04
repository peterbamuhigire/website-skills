# Narrative information architecture and audience empathy

[Owning skill](../SKILL.md)

Use this reference when a website must help a person understand, decide, trust, and act. It translates durable narrative lessons into website delivery decisions; it is not a request to turn a website into fiction.

## Source basis and limits

| Source | Admitted use | Limit |
|---|---|---|
| *Digital Storytelling* (Carolyn Handler Miller) | Interactive choices, audience fit, modular structure, characters, dialogue, emotion, rewards, development documents, and project-team handoffs. | Historical technology and platform examples are not current implementation guidance. |
| *Video Game Storytelling* (Evan Skolnick) | Conflict, tension, character motivation, audience identification, exposition, believability, dialogue, and cross-discipline narrative language. | Game narrative frameworks are adapted as decision-support patterns, not copied as website templates. |
| *Dynamic Characters* (3DTotal.com) | Silhouette, gesture, visual hierarchy, framing, value separation, and readable visual intent. | Photoshop-specific production instructions are dated; visual-system decisions still route to `design-system-skills`. |
| *Anatomy for Artists* (Tom Fox) | None. | The supplied extraction contains only `Part1`; do not attribute anatomy-specific claims to it. |

## Audience-to-architecture translation

For every primary journey, create an audience action map before page production:

| Field | Required decision |
|---|---|
| Audience actor | Name the person or group, their context, capability, language, and access constraint. Do not use “the user” as the only description. |
| Job and stakes | State what they need to accomplish, what could go wrong, and why the decision matters now. |
| Tension or uncertainty | Name the doubt, cost, risk, effort, or competing priority that can block action. |
| Proof and source | Attach the smallest credible evidence that reduces that uncertainty; record provenance and permission. |
| Choice and consequence | Identify the meaningful choice the page asks the person to make and what happens after each path. |
| Emotional state | Record the starting emotion and the intended safe state after the interaction, without manipulating fear or vulnerability. |
| Next action | Define one primary CTA, its expected value, its fallback, and the measurement event. |
| Failure and recovery | Define validation, error, offline, language, support, and back-navigation behaviour. |

## Narrative information architecture rules

1. Establish the audience problem and page promise before introducing the organisation.
2. Order sections by decision dependency: orientation, relevance, proof, objection handling, choice, action, reassurance.
3. Keep one critical path visible; use secondary paths for comparison, education, support, or procurement.
4. Use modular content blocks when audiences or locales need different evidence, examples, or reading depth. Do not create hidden duplicate truths.
5. Seed important information before the decision point and pay it off where the user acts. A page must not make the user hunt for the condition that changes the decision.
6. Treat headings, link labels, image crops, contrast, whitespace, and component states as narrative signals. Visual drama cannot compensate for unreadable content or weak task clarity.
7. Show customer agency: the organisation may be the guide, proof provider, or enabler, but the audience remains the actor.

## Empathy translated into production checks

- Read the first viewport with no assumed prior knowledge. The actor, problem, value, and next step should be identifiable.
- Test the route at the audience's likely device, bandwidth, language, literacy, and support conditions; route current device or platform claims to Digital Research.
- Inspect whether the visual focal point supports the intended action. A decorative image must not compete with the task or hide a warning.
- Check text hierarchy, link purpose, focus order, alternative text, captions, reduced-motion behaviour, form error recovery, and zoom/reflow with the accessibility gate.
- Ask a reviewer to describe the page's promise, proof, decision, and next step in one sentence each. If they disagree, return the page to mapping.

## Required delivery artefact

The website-builder handoff must include an audience action map, page-goal matrix, narrative sequence, proof/source register, CTA/event map, failure/recovery notes, and unresolved assumptions. Page-builder may not invent a missing beat, claim, or audience need.
