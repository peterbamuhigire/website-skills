# AI Interface Trust and Control Specification

Parent skill: [premium-ui-ux-design](../SKILL.md). Read when specifying or reviewing the interface of a chat assistant, copilot panel, AI search, recommendation, forecast, anomaly alert or agent workflow on a website or client portal.

Complete `ai-feature-discovery-and-risk-framing.md` first. Component specs for approval tiers, checkpoints, progress tiers, inline refinement and source citation live in `C:\wamp64\www\design-system-skills\skills\04-web-and-ui-design\ai-agent-ux\` and `...\ai-output-design\`; this file sets the behavioural rules they must satisfy.

## 1. Seven generative interaction patterns

| Pattern | What it does | Rules |
|---|---|---|
| Restating | The system restates its reading of the request before acting | Always restate ambiguous requests; offer "edit interpretation" before proceeding |
| Autocomplete | Suggests completions while the user types | Appear fast enough to feel immediate; two or three suggestions at most; visually distinct from typed text; Tab accepts, Escape dismisses; never auto-accept |
| Talk-back | Narrates what the system found or did | Lead with the conclusion ("Three invoices are overdue"); two or three sentences, then "more"; tie every statement to specific data; one consistent voice |
| Initial suggestions | Offers starting points before any input | Three to five, chosen by role, history or context; labelled as suggestions, not results; mix of types; refreshed periodically |
| Next steps | Proposes follow-on actions after a result | Secondary to the main action; three at most; relevant to what just happened; one-line reason each |
| Regenerate with adjustments | Lets users redo output with a changed parameter | Controls for length, tone, detail and focus; regenerate always visible; keep the original until the user replaces it; offer a before/after comparison |
| Boundaries (guardrails) | Stops harmful, off-topic or non-permitted output | Explain in plain language why; offer an alternative route; never show raw error codes or model refusal text; identical requests must meet identical boundaries; state the boundaries during onboarding; test them adversarially |

## 2. Communicate capability and limits

Users fail in two directions: over-trust ("it is always right") and under-trust ("it just makes things up"). Calibrate both.

- State the domain at first use: "This assistant reads [data type] to help you [outcome]. It works best when you [behaviour]."
- Show examples of good and poor requests.
- Distinguish generated content from verified records visually.
- Never claim more capability than the system has; over-claiming destroys trust permanently.
- Show data freshness or knowledge cut-off where it matters.
- Distinguish "I don't know" from "I found nothing".
- Show known failure modes openly in onboarding and help ("It struggles with handwritten notes"). Honesty about weaknesses builds trust.
- Position the system as augmenting staff ("surfaces patterns that would take days to find by hand"), never as replacing their judgement.

### Mental model alignment

- Use analogies people already know ("like a fast junior analyst whose findings you check"); avoid technical descriptions of the model.
- Show what the system "sees": the data used, the time period covered and the inputs it handles best.
- Keep one voice and one self-reference throughout the product (do not alternate between "the system", "the AI" and "I").
- Recommended framing: a capable junior colleague. It does delegated work you review, makes mistakes you catch, improves with guidance, and brings speed while you bring judgement.

## 3. Trust requirements

Design for five trust dimensions: reliable and consistent behaviour; ownership of mistakes; responsible, explained data handling; openness to user feedback; and a route to challenge decisions that cause harm.

Mandatory behaviours:

- **Show the basis** of every recommendation (which data, which pattern).
- **Show confidence** alongside predictions in plain language.
- **Lead with limitations** at first use.
- **Keep an audit trail** of system decisions and their outcomes, visible to the user where appropriate.
- **Be consistent:** the same input should produce materially the same output. Inconsistency erodes trust faster than occasional error.
- **Provide a human override** for every automated decision.
- **Answer "why?"** for every recommendation.

Build trust in stages: small verifiable wins at first use; more complex predictions with reasons in early use; more delegation once trust is earned; autonomous operation within defined zones, with monitoring, for experienced users.

Trust-destroying patterns to reject in review: contradicting earlier sessions without explanation; uncertain output styled as certain; silent errors; unexplainable recommendations; data used in ways users did not agree to.

## 4. Errors and uncertainty

Design all four error types before launch:

| Error type | Interface treatment | Message shape |
|---|---|---|
| Data problem (missing, corrupt, out of range) | Flag the specific input at the point of entry | "I couldn't process [item] because [field] looks incomplete. Check [field]." |
| Low confidence | Show a range or a qualified statement, not a single precise value | "I'm not confident here. The data suggests [range], but there may be factors I can't see." |
| Boundary reached | Friendly explanation plus an alternative | "I can't [action] here. I can help you [alternative]." |
| Fabricated or unverifiable output | Mark any statement that cannot be traced to a source as "verify this"; never style free-text summaries like data-backed facts | Link each claim to its source or label it unverified |

Uncertainty language: define three bands with distinct visual weight and wording, for example "The analysis shows…" (high), "The data suggests…" (medium, lighter treatment), "Early indication only; verify before acting" (low, muted with a warning cue). Set band thresholds with the data specialist; show numeric percentages only when they are calibrated and meaningful to the user.

Error copy rules: no raw codes; never just "AI failed"; say what did not work and what the user can do; always offer at least one recovery route; keep messages short (about 30 words) with a link to detail.

## 5. Onboarding

Avoid four anti-patterns: the feature tour nobody retains; the empty input box with no guidance; the over-promise; and assuming users understand how models work.

Instead:

1. Open with a use case and a completed example output.
2. Offer three to five curated starter requests that show the system at its best.
3. State the domain, the best way to ask, and what it will not do, before users hit a boundary mid-task.
4. Show a real output before asking for real input.
5. Progress from watching, to guided practice, to independent use.

For business tools, provide role-based request libraries: templates grouped by job function, each showing the expected output type, which users can adapt and save.

Treat every empty state as a guided starting point ("You haven't connected any data yet. Most people in your role start with one of these three").

## 6. Conversational assistants

Choose the design priority by assistant type:

| Type | Interaction | Priority |
|---|---|---|
| Task assistant | Narrow, structured, linear | Completion rate and error recovery |
| Question-and-answer | Open questions over a knowledge base | Answer quality, sources and confidence |
| Generative copilot | Open-ended, iterative creation | Adjustment controls, quality checks, speed of iteration |
| Agent | Multi-step autonomous work | Transparency, approval gates, reversibility |

Conversation rules:

- Keep context within a session and show what the assistant remembers; provide "start over / clear context".
- Business copilots must keep state across sessions, work from live data through integrations, and log every recommendation with its data basis.
- Lead each reply with the answer; short paragraphs or bullets; a one-line summary before long answers; "show more" for detail.
- Give input guidance, suggestions while typing, voice input where useful, and a visible working indicator (silence reads as broken).
- When misunderstood, restate, offer rephrasing suggestions, and never force the user to restart.

Every assistant must have a scope statement, polite handling of off-topic requests, an escalation route to a person, and an honest "I don't know".

### Copilot placement

| Layout | Screen share (approximate) | Use when |
|---|---|---|
| Side panel | About a quarter to a third | The assistant supports a primary task the user continues in parallel |
| Large overlay | About half to two-thirds | The assistant interaction is the task; underlying content is reference |
| Full page | Whole screen | The assistant is the primary interface |

The more central the assistant is to the task, the more space it gets. The panel must open and close without disrupting work; outputs must be actionable ("apply this"), show their data source, carry a one-click feedback control, and be easy to copy, share or export.

## 7. AI-led information architecture

Shift from browse, filter, find, act to ask or be shown, understand, act, refine. For analytical products, specify five page types:

1. **Overview:** a plain-language summary of the current state, key metric cards with trends, anomalies surfaced automatically, recommended next actions.
2. **Category analysis:** drill-down with a category summary, comparison to baseline, and a search box pre-seeded with relevant questions.
3. **Natural-language search results:** the restated query, results grouped by relevance, confidence per result, refine controls.
4. **Item detail:** the full record with a narrative summary, questions and answers about this item, next steps and related items.
5. **Processing, unavailable and empty states:** progress for long tasks, estimated completion, and the last known state when the service is unavailable.

### Relevance-ranked dashboards

Fixed layouts lead to blindness to fixed positions; rule-based reordering becomes brittle. When ranking items by predicted interest (weighting role, past actions, trend direction, severity and time sensitivity):

- Show why each item is ranked where it is ("Priority because three new events today").
- Let users pin, hide and reorder, and always offer "show all".
- Show what changed since the last visit.
- For trending views, show the rate of change and its time window, and distinguish "high and rising" from "high but falling".
- Guard against bias: add a "new and not yet tracked" group so absent items can surface; counter feedback loops that show only familiar items; balance recent items against persistent important ones.

### Forecasts and anomaly alerts

- Solid line for history, a labelled vertical "now" line, dashed line for forecast, and a band that widens as the horizon extends. A parallel-sided band misrepresents uncertainty.
- Never show a forecast without the historical baseline, and never as a single precise value when uncertainty is high.
- Show seasonal patterns separately, name the forecasting approach in plain words, offer horizon choices, and report how accurate past forecasts were.
- Annotate anomalies on the chart itself, not in a separate list: a marker for a single outlier, a vertical rule for a sudden shift, a highlighted segment for a value unusual for its time, a shaded region for an unusual pattern shape.
- Give each anomaly a severity and a one-line reason; let users mark false alarms as normal; state the detector's false-alarm tendency in help text.
- Add a one-sentence narrative to every chart explaining what it shows.

## 8. Agent workflows

The interaction model shifts from request and response to setting a goal and monitoring its execution.

- **Show both levels:** the overall plan (which sub-tasks exist) and the progress of each worker step.
- **Asynchronous status:** queued, in progress, needs review, complete; notify by email or push when review is needed; use a status view rather than a spinner for long tasks.
- **Editable plan:** show the plan as a checklist the user can add to, remove from and reorder mid-run; pause and cancel always visible; show completed steps and their outputs before continuing.
- **Approval gates:** mark in the plan which steps need approval; give enough context to decide, not a bare yes/no; default to approval for anything irreversible (sending messages, payments, changing records).
- **Reversibility:** undo for recent actions wherever possible; stage changes for before/after comparison; explicit warning before irreversible actions.
- **Reasoning log:** timestamped actions with reasons, distinguishing "I decided" from "you instructed".

## 9. Progressive disclosure and feedback

Three layers for any AI output: a one-sentence headline; a short summary of supporting data; full detail with method, ranges and sources. Default to the first or second layer, always offer the full layer, and let experienced users set their default.

Feedback mechanisms:

- One-click approval ("Was this useful?").
- Outcome correction ("It predicted X; what actually happened?").
- Implicit signals: accepted, edited or ignored.
- Override reasons captured in one tap ("wrong category", "outdated data", "I know something it doesn't").

Keep feedback effortless, acknowledge it, frame it as improving results rather than reporting bugs, and where the system learns from corrections, show the effect, keep a history of what the user has taught it, and offer "reset to default".

## 10. Review checklist: how AI changes familiar patterns

| Pattern | Check |
|---|---|
| Navigation | Relevance surfacing is designed as deliberately as the menu |
| Search | Handles conversational queries, shows confidence, supports refinement by dialogue |
| Forms | AI-filled fields are visibly marked and easy to correct |
| Empty states | Offer AI-guided starting points |
| Error states | Interpret what the user was trying to do and offer a recovery route |
| Help | Available in context throughout, not only as a separate section |
| Charts | Carry a narrative layer and on-chart annotations |
| Decision support | Present a recommendation with confidence plus a human override |

## Sources

- Nudelman, G. with Kempka, D. *UX for AI* (year and publisher not recorded in the source notes).
