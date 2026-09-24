# One Metric KPI Contract

Parent skill: [marketing-measurement-system](../SKILL.md). Read when choosing the single number a website launch or retainer will be managed to this quarter, when admitting or removing a KPI, when setting a target, or when receiving campaign measurement definitions from the digital-marketing engine.

This file complements [KPI tree and definitions](kpi-tree-and-definitions.md), which sets the three-layer tree and the definition card. It adds four things the tree does not: an admission test for every metric, the one-metric discipline, the source of each target, and a pre-committed action for each result. Formulas for particular business models are in [model metric definitions and lead arithmetic](model-metric-definitions-and-lead-arithmetic.md).

## 1. Admit a metric only if it passes four tests

Run every candidate metric through this test before it reaches a dashboard, a proposal or a monthly report.

| Test | Question | Fails when |
|---|---|---|
| Comparative | Can it be compared across periods, cohorts, channels or segments? | It is a single figure with nothing to compare it with. |
| Understandable | Can the client team remember it and discuss it without a glossary? | Only the analyst can explain it. |
| Rate or ratio | Is it a rate (per visitor, per week, per enquiry) rather than a running total? | It can only go up (total downloads, cumulative followers, all-time sign-ups). |
| Behaviour-changing | Is the action for "up", "down" and "flat" written down before data is collected? | Nobody can say what they would do differently. |

Then tag the metric with its type. The tags show the client how much weight each number can carry.

| Tag pair | Meaning | Reporting rule |
|---|---|---|
| Quantitative / qualitative | "What and how much" versus "why" | Pair every surprising quantitative movement with a qualitative explanation from the [customer insight loop](customer-insight-loop.md). |
| Reporting / exploratory | Tracks a known question versus searches for an unknown one | Exploratory findings are hypotheses; they go to `experimentation`, not into the target set. |
| Leading / lagging | Predicts the outcome versus records it after the fact | A leading indicator earns its place only after cohorts show it moves before the outcome. |
| Correlated / causal | Moves with the outcome versus shown to drive it | Write "causal" only when a controlled test has shown it. Otherwise say "moves with". |

Decision after the test:

- Passes all four and drives a named decision: keep as a KPI.
- Explains but does not decide: keep as a diagnostic, below the fold of the report.
- Fails and decides nothing: remove it.

Vanity metrics are context-dependent. Page views and visits are legitimate for a publisher selling advertising inventory, and unique viewers are a fair way to rate a single article. They are never evidence of business growth on their own. Report them as diagnostics, never as the headline.

## 2. Start from the goal, not from the metrics

Metrics chosen before the goal is stated end up scattered across the funnel. Use this order:

1. Write the goal of the site, page or feature in one sentence (for example, "more qualified consultation bookings from clinic owners").
2. List the stages of the journey: arrive, engage, act, return, refer.
3. Cross out every stage the change cannot affect. A form redesign cannot change arrival; do not measure arrival for it.
4. For each remaining stage, choose one metric tied to the goal.
5. Name one primary metric and three to five guard-rails.
6. Set measurement windows (for example 1, 7 and 30 days) before launch.
7. For a feature with two sides, such as an event listing used by organisers and attendees, measure both sides.
8. Include revenue or monetisation metrics only if earning is part of the stated goal.

## 3. Choose the One Metric That Matters

At any one time the client team manages to one number: the metric that measures the riskiest assumption at the current stage. The other KPIs are still tracked; the one metric is the number everybody can quote with its current value.

### Procedure

1. List the three to five metrics the team looks at most often. Remove any that fail section 1.
2. Name the riskiest assumption for the website at its current stage (see the stage table below).
3. Choose the metric that measures that risk directly. Prefer a rate.
4. Record its current value, date and source.
5. Draw the line in the sand (section 4).
6. Ask: "If the whole team worked only on this number, what would break?" The answers are the guard-rails.
7. Revisit the choice when the line is crossed or when a new constraint appears.

### Stage table for website work

The business's own stage declaration belongs in its marketing or business plan (the business-plan engine owns it). The website side adopts that declaration and picks a site-level metric that serves it.

| Stage | Question the site must answer | Typical website one metric |
|---|---|---|
| Empathy | Do the right people recognise the problem we describe? | Share of target-segment visitors who take the first action (register interest, answer a question) |
| Stickiness | Do people who act once come back and act again? | Repeat enquiry, repeat order or return-visit rate for a defined cohort |
| Virality | Do customers bring customers? | Share of active customers who refer or share in a period |
| Revenue | Does the site produce money at an acceptable cost? | Revenue per visitor, or cost per qualified enquiry against the allowable cost |
| Scale | Does it keep working across channels, regions and services? | Revenue per visitor or payback by channel and region |

Do not buy traffic for a site whose visitors do not come back or convert (the stickiness stage has not been passed). Paid traffic into a leaking funnel spends money to confirm the leak.

### Tests for a good one metric

- **Litmus test.** The team is in trouble if it cannot name its one metric, names the wrong one for its stage, names several, or does not know the current value.
- **Five-word test.** A good operating metric is simple, immediate, actionable, comparable and fundamental.
- **Squeeze effect.** Pushing one metric exposes the next constraint (traffic rises, then conversion becomes the limit). Expect the one metric to change as constraints move, and say so in the plan.

## 4. Draw the line in the sand

A line in the sand is a numeric target agreed before the work starts. It says what counts as success and what happens next. Without it, most results land in an ambiguous middle and nobody can decide whether to continue.

### Three admissible sources for the line

| Source | When to use | What to record |
|---|---|---|
| Business-model arithmetic | The plan only works if the metric reaches a level (for example, sales capacity needs a number of qualified enquiries per month) | The calculation, with its inputs and their owners |
| External baseline | A comparable, current, sourced figure exists for the same market and model | Source, year, market and model. Figures older than the current review cycle or from another market are context only, never targets. |
| The client's own trend | Neither of the above exists | The trend method in `../../experimentation/references/experiment-charter-and-test-discipline.md` (no-baseline section) |

The benchmark tables in startup and marketing books are mostly from 2008–2014 United States web data. Do not use them as lines for East African clients. Use the client's own baseline once three months of clean data exist, as [KPI tree and definitions](kpi-tree-and-definitions.md) already requires.

### Honest adjustment rule

- The line may be moved, but only on evidence. The admissible evidence is qualitative data from a specific segment showing that customers get real value at the new level (for example, calls to customers who use the service fortnightly rather than weekly show that they are satisfied and renewing).
- Never lower a line to make a result pass. Croll and Yoskovitz put it this way: "you shouldn't move the line to your ability; rather, you need to move your ability to the line."
- Record every change: old line, new line, evidence, date and who approved it.

### Line worksheet

| Field | Entry |
|---|---|
| Metric | Name and formula (numerator ÷ denominator over window) |
| Baseline | Value, date range, source system |
| Line | Target value and date |
| Line source | Model arithmetic / external baseline (source, year, market) / own trend |
| Review date | When the line is checked |
| Action if reached | What the team doubles down on |
| Action if missed | What stops or is redesigned |
| Action if inconclusive | What evidence is gathered next |
| Guard-rail floors | The levels that other metrics must not fall below |
| Who may change the line | Named role, and the evidence required |

## 5. The KPI contract row

Extend the definition card in [KPI tree and definitions](kpi-tree-and-definitions.md) with these columns. A KPI without them is reported as "definition incomplete".

| Column | Content |
|---|---|
| Type tags | Quantitative or qualitative; reporting or exploratory; leading or lagging; correlated or causal |
| Stage served | The stage from section 3 |
| One metric? | Yes for exactly one row per quarter |
| Line and line source | From section 4 |
| Action if reached / missed | From section 4 |
| Guard-rail floor | For guard-rail rows only |

## 6. Retainer and report framing

- Anchor each retainer quarter to one agreed number with three to five guard-rails. Put the remaining metrics in an appendix.
- Open the monthly report with the one metric: current value, line, trend since the start of the quarter, and "on track: yes / no".
- Say "no" when the answer is no, and name the next action. Honest status earns more trust than a long chart pack.
- Never promise that the line will be reached. The retainer commits to the work and the measurement, not to the outcome.

### Phrase bank

- "For this quarter we will manage the site to one number: [metric, defined as numerator ÷ denominator over window]. It stands at [baseline] ([source], [dates])."
- "Our line is [target] by [date], derived from [model arithmetic / named source and year / our own trend]. If we reach it we will [action]; if we do not we will [action]."
- "[Guard-rail] must not fall below [floor] while we pursue this."
- "On track: no. [Metric] is [value] against a line of [target]. The cause we can evidence is [cause]; next month we will [action]."
- "This movement coincides with [change]. We have not tested whether [change] caused it."

## 7. Receiving from social-media-skills

The digital-marketing engine (social-media-skills) defines campaign measurement: the UTM naming convention and the campaign conversion events. This skill receives those definitions; it does not define or rename them. The landing-page brief and the full receiving procedure for campaign pages are in `launch-campaigns` (`../../../agency-ops/launch-campaigns/references/channel-to-site-handoff-receiving.md`); this section covers only the measurement checks.

### What arrives

| Artefact | Owned by | Received here as |
|---|---|---|
| UTM table and naming convention | social-media-skills | Adopted as-is into the source and medium map |
| Campaign conversion events (name, trigger, value, deduplication rule) | social-media-skills | Mapped to site events in the event and source plan |
| Consent scope for the campaign audience | social-media-skills, with the client's compliance owner | Checked against the site's consent implementation |

### Checks on receipt

1. **UTM convention adopted as-is.** Do not rename parameters or values. Confirm that the five standard parameters are covered and that values are lower-case and consistent. If the site already has its own convention (for example, in the SEO event map), campaign links use the campaign convention and the difference is recorded in a mapping note, not silently merged. Confirm UTM values survive redirects and reach the CRM where sales needs them.
2. **Conversion event names mapped to site events.** Build a mapping table: campaign event name, site event name, trigger, where it fires (confirmation state, not a page view), value, deduplication key, consent basis, destinations, QA status. Every campaign event must map to exactly one site event that fires once per real action.
3. **Consent mode for EEA, UK and Swiss traffic.** Where the campaign may reach visitors in the EEA, the UK or Switzerland and the site uses Google tags, confirm that a consent management platform passes Consent Mode v2 signals, including `ad_user_data` and `ad_personalization` (register CW-10). This is not a legal requirement in Uganda or Kenya but affects EU-facing campaigns.
4. **Uganda and Kenya data rules.** For Ugandan data subjects, confirm that consent to collect is captured and that a written objection to direct marketing can be honoured within 14 days (register PL-01). For Kenyan data subjects, confirm consent and a free, simple opt-out; objections to direct marketing are absolute (register PL-02).
5. **Return, do not repair.** If a definition is missing a trigger, value or deduplication rule, or conflicts with an existing site event, return it to the campaign owner with the field, the reason and the decision needed. Do not redefine it here.

Handed back to social-media-skills: the mapping table, the tracking QA log (each event tested once per real action, with dates) and any returned definitions.

## 8. Anti-patterns

| Anti-pattern | Correction |
|---|---|
| Forty KPIs with equal weight | One metric, three to five guard-rails, the rest in an appendix |
| A target with no stated source | Record model arithmetic, a dated external source or the client's own trend |
| Lowering the line to pass | Move it only on segment-level evidence; record the change |
| A test or campaign with no pre-agreed line | Write the line and the actions before data is collected |
| Calling a correlation a cause | Tag it "correlated" until a controlled test shows otherwise |
| Renaming campaign UTMs or events on receipt | Adopt as-is; map and return with reasons |

## Sources

- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics: Use Data to Build a Better Startup Faster*. O'Reilly Media. (Metric tests, One Metric That Matters, lines in the sand, stages.)
- Lin, L. C. (2013) *Decode and Conquer: Answers to Product Management Interviews*, 2nd edn. Impact Interview. (Goal-first metric selection.)
- Currentness register 2026-09-23, claims CW-10, PL-01 and PL-02.
