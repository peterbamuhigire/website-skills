# Lean Design Cycle and Deliverable Selection

Parent skill: [premium-ui-ux-design](../SKILL.md). Read when turning a feature request or page brief into a design, deciding which design artefact to produce next, planning how much visual polish to apply, or setting up the working rhythm between design, engineering and the client.

Use with `ux-strategy-differentiation-and-meaning.md` (what to build and why), `pm-collaboration-rules.md` (client participation) and `../../../launch-ops/experimentation/references/pre-build-validation-and-rollout-playbook.md` (proving demand before build).

## 1. Working stance

Apply five properties to every design task:

1. **Hypothesis-led.** Start from the metric and the user problem, not the feature.
2. **User-centred.** Keep constant contact with real users; you are not the user.
3. **Cross-functional.** Designers, engineers and the product owner work together in short cycles; no long hand-offs.
4. **Data-informed.** Numbers show what is happening; research shows why. Vision proposes, testing checks.
5. **Iterative.** Nothing is finished; it is ready for its next iteration. Abandoning an experiment without studying it is flailing, not iterating.

## 2. The nine-step design cycle

| Step | Do this | Skip when |
|---|---|---|
| 1. Understand the problem | Restate the request in problem language (not "add comments" but "users cannot ask each other questions, which hurts engagement"). Establish who the users are, their device and context, their need, and what internal staff (support, sales, engineering) already know. | Never |
| 2. Design the test first | Define the success metric, the test method and the measurement window before sketching. | Almost never; it can take five minutes |
| 3. Write design stories | Describe what must become possible, not how: "People who are stuck can quickly find out how to solve the problem." Include staff and administrator stories ("Support can add a new answer the same day a new problem appears"). | Bug fixes, small copy changes, visual A/B variants |
| 4. Brainstorm briefly | Small group who know the problem. State the problem and success measure; everyone writes ideas silently in one or two sentences; read aloud without debate; group ideas by metric affected, ease and problem solved. Fifteen minutes; no voting. | Rarely |
| 5. Decide | Plot options on expected return versus expected cost; get cost estimates from engineering and side-effects from marketing, support and sales. Pick a direction to validate; certainty is not required. | Never |
| 6. Try to disprove it cheaply | Use a feature stub, landing page or manual service to test whether anyone wants it (see the pre-build validation playbook). | When building is faster than testing |
| 7. Sketch several approaches | Only now draw. Include real copy, every interactive state, error states, menu contents and what each button does. Produce several versions and show them to four or five users, rotating which one they see first. | When the change is better shown directly in code or a mock-up |
| 8. Build an interactive prototype | For multi-step flows, costly-to-fix changes, or genuine uncertainty between approaches. | Single-step changes; single-CTA pages; when the real feature is as quick to build and cheap to roll back |
| 9. Test and iterate | Put it in front of users, fix, repeat. If you expect the first design to be right, you have spent too long up front. | Never |

## 3. Diagnose the pain behind requests

Treat user requests like symptoms presented to a doctor:

1. Find where it hurts: interview about habits, likes and dislikes; observe use of the current product and of competitors.
2. When someone asks for a feature, ask why they want it.
3. Design the simplest treatment for the underlying pain, then test that the pain has gone and no new pain has appeared.

Worked pattern: three buyers all ask for "more case studies".

| Stated need | Underlying pain | Simpler treatment |
|---|---|---|
| "I don't know what to buy" | Too many choices | Recommended packages or a short selector |
| "Is it worth it?" | Uncertain return | Outcome evidence placed next to the offer |
| "Is this company reputable?" | Trust | A static client logo grid and verifiable credentials |

Do not ask customers to design the product, accept every request, or ignore requests entirely.

## 4. Cup holders versus brakes

Before committing to any item, answer: what problem does this solve, and how important is it compared with every other problem we could solve now?

Likely cup holders (low return for now): visual polish before core flows work; retention features before there are users to retain; decorative animation; anything that cannot be tied to a metric. If you cannot complete the sentence "This will move [metric] by making it easier for users to [task]", treat the item as a cup holder.

Worked failure to avoid: a new feature was judged to need a place in the main navigation, which forced a navigation redesign, which forced a visual redesign; on launch nobody used the feature. Test demand first through a temporary entry point, a stub or a manual service.

## 5. Observe experienced users before designing

- Watch how experienced users actually work. Their workarounds and shortcuts reveal features worth building natively (for example, reviewers who skip to the likely decision point of a recording suggest a visual timeline and faster playback).
- Keep key actions on the screen where users need them, never hidden in a profile or overflow menu.
- When users must trust an automated system, show its intent in a consistent, glanceable place.
- Check what shapes and colours signal. The same red reads as "danger, act now" in a box and as "boundary, handled" as a line; test the meaning, not only the look.

### Competitor evidence

- Build the competitor list from what customers name in interviews, what stakeholders mention, the words customers would type into search, and roundup articles in niche media. Look beyond the first page of results.
- Recruit four or five regular users of a competitor product and watch them use it at the time they normally would. Ask what they like, hate and find confusing, what is missing, how they learnt it, why they chose it, and (for business tools) which parts of their job they still do outside it.
- The market gap is often the small share of a bloated product that people actually use, delivered more simply.

## 6. Storyboard the valuable moments

Before prototyping a new concept, storyboard it:

1. **List the panels.** Show only the most valuable moments of the journey, online and offline, across its full real duration (minutes for a ride, weeks for an event booking).
2. **Choose the fastest visual format.** Sketches, collages or adapted screenshots; same aspect ratio for every panel; borrow existing UI rather than designing new UI.
3. **Lay out and caption.** One or two short lines under each panel. Review: does it flow, is it concise, is it easy to follow?

Borrow proven features, interaction patterns and business-model ideas from competitors and from unrelated products, and recombine them. Record every borrowed pattern and its origin.

## 7. Choose the deliverable by what you must learn

| Deliverable | Use to | Do not use to |
|---|---|---|
| Flow diagram or sitemap | Work out routes through the product, estimate scope, explain navigation to engineers | Validate hypotheses or test with users |
| Sketch | Compare approaches quickly; decide what belongs together on a screen | Gather user feedback (too abstract); a sketch of boxes marked "text" is not a sketch |
| Wireframe | Settle every screen-level detail: copy, CTAs, navigation, states. Linked wireframes give most of a prototype's value for a fraction of the time | Finalise visual design |
| Interactive prototype | Test complex, costly-to-fix or contested interactions; give engineers a precise behaviour spec. Fake the back end | Impress investors |
| Visual design mock-up | Apply the visual layer once interaction is validated | Early usability testing: polish attracts comments on looks and suppresses criticism |

### Paper prototypes

Avoid paper for user testing: people handle paper differently from screens, it cannot show states or error recovery, and participants spend effort interpreting the paper. Paper is acceptable for early team brainstorming, printed materials, quick early mobile sketches, small embedded screens, or when no computer is available.

### Route by value and resources

| Project situation | Route |
|---|---|
| High business value, adequate time | Sketch, wireframe, high-fidelity wireframe, interactive prototype test, visual design, code |
| Moderate value | Sketch, wireframe, visual design, code |
| Low-visibility back-office or admin screen | Sketch, then code using the existing design system |

### Wireframe production steps

1. Research related products, patterns and the project's guiding principle.
2. Summarise the research on one sheet: business and user objectives, personas, contexts of use, competitor cues, audience quotes.
3. Map the user flow: how many screens, where users arrive from (which channel and message) and where they finish.
4. Draft quickly without colour or styling.
5. Add detail top to bottom, left to right, and test early (first-impression and preference tests).
6. Turn the wireframes into a clickable prototype.

## 8. Visual design at the right time

Visual design is not decoration. It:

1. **Supports information design.** Content-heavy products need a restrained visual layer that makes the content the focus.
2. **Reinforces the desired action.** Group the CTA visually with the information needed to decide (price, name, image). A poor visual layer can hide an element the interaction design placed correctly.
3. **Sets tone and builds trust.** High-price purchases need a sophisticated visual layer; tone that signals the wrong audience (for example, a playful cartoon style on an adult product) drives the right buyers away. Verify tone with first-impression tests on the real target market, not with designers' taste.

Do not polish during prototyping and usability testing, or before the structure is proven: polish distracts participants, discourages criticism and makes the team reluctant to discard a broken design.

Instead of polishing every screen, invest once in a flexible visual standard: palette, type sizes and colours for heading levels and body, grid column sizes, a consistent icon set, standards for boxes, backgrounds and separators, and a flexible header and footer. Engineers can then combine the standard with wireframes to build presentable screens without a separate visual pass for each iteration. (Apply the design-system-skills typography and colour doctrine when choosing the standard.)

## 9. Team rhythm

Replace the sequential specification, mock-up, build hand-off with this loop:

1. The product owner names the metric to move.
2. Designer and engineers take part in quick user research together; engineers attend at least some sessions.
3. The team agrees the smallest viable experiment.
4. The designer sketches and prototypes while engineers start back-end work in parallel.
5. Engineers watch prototype tests.
6. After launch the whole team watches the metrics and iterates.

A default engagement sequence for client work: personas and analytics; user journeys; wireframes and prototypes; user testing (iterate until tasks succeed); look-and-feel drafts (two or three styles applied to one real screen); detailed designs with a style guide and developer documentation; A/B tests on key messages and patterns after launch.

## Sources

- Klein, L. (2013) *UX for Lean Startups: Faster, Smarter User Experience Research and Design*. O'Reilly Media.
- Levy, J. (2015) *UX Strategy: How to Devise Innovative Digital Products that People Want*. O'Reilly Media.
- Fekeshazi, Z. *Product Managers' Guide to UX Design*. UX Studio (year not recorded).
- Deacon, P. B. (2020) *UX and UI Design Strategy: A Step-by-Step Guide* (publisher not recorded).
