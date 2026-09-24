# Journey Acceptance and Friction Evidence

Parent skill: [website-builder](../SKILL.md). Read when setting page goals from user scenarios, specifying failure states, keeping a friction log, staging an experimental release, or planning post-launch adoption and value measurement. Also used by `page-builder` and `experimentation`.

A page is not complete because it looks polished. Its critical journey must be understandable, usable, accessible, and recoverable, and there must be evidence that it is.

## 1. Start each page with a scenario

Complete the scenario before choosing a layout or writing copy.

| Field | Entry |
|---|---|
| `audience` | who arrives (role, context, device) |
| `trigger` | what made them come now |
| `job` | what they are trying to get done |
| `desired_outcome` | what success looks like for them |
| `confidence_barrier` | the doubt or risk that could stop them |
| `next_action` | the single step the page must make easy |

Turn the scenario into:

1. a page goal (one sentence, outcome-based);
2. a content hierarchy that answers the confidence barrier before the ask;
3. one primary path and at most two secondary paths;
4. measurable acceptance criteria (section 3).

## 2. Specify the whole journey and its failure states

For the primary journey, cover five stages: discovery, understanding, action, confirmation, recovery.

For each interactive step, specify:

- realistic content length (longest real name, address, product title, translation);
- mobile and touch interaction;
- loading, empty, error, validation, success, consent, and interruption states (network loss, timeout, back button, session expiry).

Diagnostic copy must be actionable. Every error or failure message states:

1. what happened;
2. whether the visitor's work or data was kept;
3. what the visitor can do next;
4. how to recover without starting again, or where to get help.

## 3. Acceptance criteria template

Write acceptance per journey, not per component.

```
Journey: [name]
Given [scenario and starting state]
When [the visitor performs the step, including on a narrow touch screen]
Then [observable outcome]
And  [state copy shown for failure X, with recovery path]
And  [accessibility condition: keyboard, focus, labels, announcements]
And  [performance condition checked on a representative device and network]
Evidence: [test record, screenshot, recording, or log reference]
```

A journey passes only when every failure state listed for it has been triggered or inspected and recorded.

## 4. Build in stages when unknowns are material

Prefer a narrow, testable first release or an experimental version when the page depends on material unknowns (audience behaviour, content availability, integration reliability, legal wording).

Staging rules:

- Define what the first release must prove and what it deliberately omits.
- Keep the omitted scope visible in the backlog with an owner.
- Choose the simplest implementation that meets the page outcome; do not require a vendor-specific tool or framework when a simpler build achieves it.
- Set the evidence that will decide the next stage before release.

## 5. Keep a friction log

Record friction from usability sessions, support contacts, analytics, recordings (where consented), and team walkthroughs.

| Field | Entry |
|---|---|
| `scenario` | which journey and step |
| `observed_obstacle` | what the visitor struggled with, in plain words |
| `evidence` | source and date (session note, ticket, event data) |
| `likely_cause` | content, layout, interaction, performance, technical, policy |
| `impact` | how many visitors or how severe; mark `NOT_ASSESSED` if unknown |
| `owner` | person responsible |
| `next_experiment` | the change to try and how it will be judged |

Review the log at each stage gate and after launch. Close an entry only with evidence that the obstacle is resolved.

## 6. Connect design-system and engineering proof

- Build pages from the governed token and component source, with defined state contracts and accessibility semantics.
- Define performance budgets and critical-flow checks before implementation.
- Verify on representative devices, networks, and real content lengths.
- Record search evidence separately from UX and conversion claims; a search improvement is not evidence of usability, and the reverse.

## 7. Measure adoption and value after launch

Combine qualitative and quantitative signals:

| Signal | Example evidence |
|---|---|
| Adoption | share of intended visitors who start the journey |
| Value | completion of the job; repeat use; qualified outcomes |
| Conversion | goal events tied to the page goal |
| Performance | field and lab measurements against the budget |
| Accessibility | audit findings and assistive-technology test results |
| Support | contacts, complaints, and questions linked to the journey |
| Qualitative feedback | interviews, on-page feedback, sales and support notes |

## 8. Post-launch learning loop

1. Set a baseline at launch.
2. Review signals at an agreed interval and after any material change.
3. Update the page or the experiment hypothesis from evidence, not from a calendar alone.
4. Record each change, its reason, and its result in the friction log or experiment record.
5. Feed confirmed lessons into the component library, content standards, or stage-gate checklists.

## 9. Deliberate exclusions

- Do not add a generic AI-visibility or training-data promise to a page goal without current, claim-level evidence.
- Do not treat visual polish, a passing lab score, or stakeholder approval as journey acceptance.

## Sources

- Drew Hoskins, *The Product-Minded Engineer* (publisher and year not recorded in the source synthesis).
- Michael Mangialardi, *Design Systems for Developers: Learn How to Code Design Systems That Scale* (publisher and year not recorded).
- Almantas Karpavičius, *Software Craftsmanship Using AI* (publisher and year not recorded).
