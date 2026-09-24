# AI Feature Discovery and Risk Framing

Parent skill: [premium-ui-ux-design](../SKILL.md). Read when a website or client portal will include a predictive, generative or agent-driven feature (chat assistant, recommendation, forecast, automated triage), before any interface is designed.

Use with `ai-interface-trust-and-control-spec.md` (the interface rules that follow this framing) and `../../website-experience-mapping/references/validation-research-method-playbook.md` (research methods and integrity rules). For component-level agent and output patterns, also consult `C:\wamp64\www\design-system-skills\skills\04-web-and-ui-design\ai-agent-ux\SKILL.md` and `...\ai-output-design\SKILL.md`.

## 1. First question: does this need AI?

Before scoping, answer in writing:

1. Which user decision or task does the feature improve, and what does it cost the user today to do it without AI?
2. Could a rule, a search filter, a template or a better form solve it?
3. What does each AI call cost (money, latency, energy) and how often will it run?
4. What happens to the user if the output is wrong?

If a simpler mechanism solves the problem, recommend it. Minimise unnecessary AI calls in the design.

## 2. Three pillars and the team

- An AI feature depends on three pillars that must move together: the **interface**, the **model** and the **data**. Never iterate one in isolation; a strong interface on poor data fails, and so does a strong model behind a confusing interface.
- Staff the work with four roles present from day one and in every key decision: product owner, UX designer, engineer, and data or AI specialist. Decisions without UX produce hidden automation; decisions without the data specialist over-promise capability.
- Common causes of AI project failure to check at kickoff: unclear goals, poor data quality, missing expertise, and no user-centred design. (Do not quote failure-rate statistics unless you have verified the source.)

### Hidden automation rule

Any automated behaviour that changes an outcome for the user must be visible, interruptible and overridable, and users must be told it exists and how to override it. Silent automation that users cannot see or counter is a safety defect, not a style choice.

## 3. Value matrix: replace "accuracy" with the cost of each error

Model accuracy figures mean little to buyers. A system that is right most of the time may still be unacceptable if its errors are expensive. Build a value matrix with stakeholders:

|  | System says yes | System says no |
|---|---|---|
| **Actually yes** | True positive: value gained | False negative: missed event |
| **Actually no** | False positive: false alarm | True negative: correctly ignored |

Procedure:

1. List the four outcomes for this feature in plain words (for example, "fraud flagged and real", "genuine customer blocked").
2. For each, record the real-world cost (money, time, safety, reputation, legal exposure) and the real-world benefit.
3. Net them out per cell.
4. Decide which error is worse: false alarms or misses.
5. Choose the model posture:

| Posture | Minimises | Use when | Interface consequence |
|---|---|---|---|
| Balanced | Neither in particular | Errors cost roughly the same | Show an overall confidence cue and let users inspect the basis |
| Conservative | False alarms | Alerts are costly (fatigue, fines, customer friction) | Explain the caution; give a manual route to catch misses |
| Aggressive | Misses | Missing a real event is severe | Provide volume controls, quick dismissal and a "why flagged" reason on every alert |
| Context-dependent | Shifts with the situation | The business can define acceptable trade-offs per context | Show which threshold is active and why |

Rule: never accept a headline accuracy figure as a success criterion until the value matrix is agreed.

## 4. System map (digital twin) workshop

Run this with the whole team before designing screens:

1. Draw the chain: real-world subject or process → data captured → model → prediction or output → interface → user action → real-world outcome.
2. Label each arrow with the data that moves and the person or component responsible.
3. Mark every point where the system decides without the user knowing.
4. Mark the steps with the highest failure risk.
5. Design an interface intervention (explanation, confirmation, override, alert) at each high-risk decision point.
6. Note where user corrections feed back into the model, and whether that loop exists yet.

## 5. Storyboard every AI interaction

Each storyboard must include six elements:

1. **Establishing shot:** who the user is, where, and in what situation.
2. **Things:** devices, equipment, data and interfaces involved.
3. **People:** everyone who interacts with the system, not only the primary user.
4. **Faces:** what each person feels at each stage.
5. **Transitions:** action to action, action to result, and at least one **subject-to-system** transition where the system reads the real world (a document, a photo, a sensor reading) and produces a judgement. This is where value is created and where mental models break.
6. **Conclusion:** what changed in the real world, not merely "a dashboard appears".

Also draw the branch where the system is wrong. Use rough sketches and annotate each frame with the system's role ("predicts X here", "recommends Y here").

## 6. Vision prototypes (long-horizon concepts)

Use when a stakeholder's ambition needs grounding, a use case has no precedent, or ethics and bias need discussing concretely.

- Set the horizon one to two years out or further; anything shippable within a few sprints is a tactical prototype.
- Show a complete flow from problem recognition to real-world value, not a gallery of screens.
- Deliver as a short narrated video (one to two minutes): open with the use case in the user's voice, walk through the flow, close by stating the value delivered.
- Use realistic content: numbers that add up, plausible names and measurements; no placeholder text.
- Cover one or two use cases in depth.
- Explore the extremes: maximum automation, minimum automation, and the most radical interpretation. The extremes reveal the design space.
- Decide separately what the minimum shippable version is; hold the vision lightly.

## 7. Research for AI features

Focus on the decisions users make, not their opinions of an interface:

- "What decision are you trying to make here?"
- "What would you do differently if you knew this earlier?"
- "What is the most expensive mistake you make regularly?"

Methods, in priority order:

1. **Contextual inquiry:** watch real work; note when decisions happen, what data is consulted, what is missed, where speed matters and where errors are costly.
2. **Diary study (two to four weeks):** users log decisions, what would have helped, the consequences, and moments of uncertainty and what would have given confidence.
3. **Expert interviews:** separate sessions with domain experts (what good looks like) and users (what they need).

Never substitute generated personas or simulated participants for real people (see the research integrity rules in the validation playbook).

### Test scenarios specific to AI

Add these tasks to every rapid iterative test round:

- The system gives a wrong prediction: does the user notice and cope?
- The user disagrees with a recommendation: can they override it?
- A low-confidence output appears: does the user understand what it means?
- The user must correct a mistake: how does the correction flow work?
- A boundary or refusal is triggered: does the user understand why and what to do next?

## 8. Bias review

Assume every model is biased by its training data. For each feature:

1. Ask what and who is absent from the data. Systems learn only from what was captured; look first for what is missing.
2. Check outputs for demographic, temporal (historical inequality) and feedback-loop bias (the system shows people more of what they already clicked).
3. When using generative tools for content or imagery, write specific prompts that counter default stereotypes, and review every output for who is missing.
4. Use a second, different model or a human panel to audit outputs for representativeness.
5. Test deliberately with under-represented user groups.
6. Publish a known-limitations section in user help that names known biases.
7. Give users a way to flag biased outputs, and route those flags to the team.

## 9. Ethics checklist

| Principle | Design requirement |
|---|---|
| Control | Users can adjust or opt out of AI features; data storage, processing, sharing and deletion are under user control; explicit consent flows exist |
| Trust | Consistent behaviour; errors acknowledged, not hidden; data use explained plainly; every decision has an accessible explanation |
| Diversity | Training data coverage reviewed; known gaps documented |
| Safety | Privacy and security treated as safety requirements; informed consent before the system affects people's lives; conversational features stress-tested with adversarial inputs |
| Balance | AI augments rather than replaces people; environmental and running cost considered |

Guard against three psychological risks:

- **Presumed neutrality:** users over-trust machine output. Add deliberate friction (review steps, "check this" prompts) where stakes are high.
- **Under-reliance:** users reject unfamiliar suggestions. Build trust gradually with small verifiable wins.
- **Deskilling:** users lose skills they hand over. Keep people practising the judgement parts of the task.

Designers can build accountability features, explanations and feedback mechanisms into the specification without separate approval; do so by default.

## 10. Add these steps to the project plan

| Phase | Additions |
|---|---|
| Discovery | System-map workshop; value-matrix workshop; bias review in the research plan |
| Design | Storyboards with subject-to-system transitions; all four error types designed (see the interface spec); confidence and uncertainty treatment from the start |
| Validation | Rapid iterative testing (three or four rounds of three or four people) with the AI-specific scenarios above; real participants only |
| Iteration | Update interface, model and data together; log which interface changes affected model performance and the reverse; keep an audit trail of design decisions |

Keep design specifications aligned with the real component library; where possible, prototype in production front-end code.

### Text notation for fast AI-assisted prototyping

When generating prototype code from a text description, describe layouts in a consistent notation so variants are quick to produce and review:

- Indent to show parent and child components.
- Write each element as `[ComponentName: key properties]`.
- Use `→` for state changes or conditions, `|` for alternatives, `//` for design intent.

Example:

```
[AccountSummary: two-column]
  [InsightCard: col-1, confidence=medium]  // plain-language summary first
    [Headline: one sentence]
    [NextSteps: max 3]
  [TrendChart: col-2, history=solid, forecast=dashed → range band]
```

Review generated code against the design system before any client sees it.

## Sources

- Nudelman, G. with Kempka, D. *UX for AI* (year and publisher not recorded in the source notes).
- Synechron Inc. (2018) *Bridge the User Experience Gap in Enterprise Applications for Financial Services & Insurance*. Synechron.
