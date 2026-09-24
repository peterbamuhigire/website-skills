# Experiment Charter and Test Discipline

Parent skill: [experimentation](../SKILL.md). Read when deciding whether an idea deserves a test at all, before filling in the hypothesis template, when tracking is not yet trusted, when no baseline or benchmark exists, or when a result improves one metric and harms another.

This file complements [the hypothesis template](hypothesis-template.md) (the fields every test file carries), [the statistical significance primer](stat-significance-primer.md) (sizing and confidence intervals) and [the pre-build validation playbook](pre-build-validation-and-rollout-playbook.md) (cheapest-first validation). It adds the gate before a test, the charter that frames it, the tracking gate, expectations to set with clients, the tie-break for mixed results, a plain-English p-value explanation, and a method for setting a target when no baseline exists.

## 1. Seven questions before building a feature or variant

Answer all seven in writing. Any weak answer sends the idea back for rework or to a cheaper method.

| # | Question | Passing answer |
|---|---|---|
| 1 | Why will this move the current one metric? | A hypothesis naming the metric and the expected lift, written before building |
| 2 | Can we measure its effect? | The event exists and fires once per real action, or will before launch (section 3) |
| 3 | How long will it take to build, and can we test the risk more cheaply? | An estimate, plus the cheapest rung from the pre-build playbook that could answer the question |
| 4 | Will it make the site more complicated? | Nothing added that every visitor must now learn; if the description needs "and", split it |
| 5 | How risky is it (technical, user trust, lock-in)? | Named risks with rollback |
| 6 | How new is it? | Small tweaks are easy for competitors to copy; say whether that matters |
| 7 | What do users say, and does their behaviour agree? | Quotes from the insight loop and a behavioural signal that points the same way |

Every shipped feature carries an engagement metric. A feature nobody uses is a cost: plan its removal and measure the effect of removing it.

## 2. The experiment charter

Write the charter first; it frames why the test exists. Then fill in the hypothesis template, which holds the technical design. Keep the charter to one page.

| Charter field | Content | Feeds hypothesis template section |
|---|---|---|
| What we want to learn, and why now | The decision that is waiting on this result | 3 |
| The problem and who feels it | Segment, situation and evidence of the problem | 1, 2 |
| Hypothesis | "[Specific, repeatable action] will create [expected result] for [segment]", worded so that data can prove it wrong | 3 |
| What we will build or change | The minimum needed to test the hypothesis, not the full feature | 6 |
| Is it safe? | Trust, accessibility, privacy, legal, pricing and brand risks, with rollback | 9 |
| Line in the sand and actions | The target, its source, and the action if reached, missed or inconclusive (see `one-metric-kpi-contract.md` in `marketing-measurement-system`) | 4, 8 |
| What would prove it wrong | The results that invalidate the hypothesis | 8 |
| What would make it unsafe to continue | Guard-rail breaches and harm signals that stop the test early | 5, 7 |
| How we conclude and clean up | Stopping rule, decision owner, code and flag removal date | 7, 11 |

Pre-registration means the line and the three actions exist before the first visitor is exposed. A charter completed after the result is a story, not a test.

## 3. Tracking-readiness gate

No test starts until tracking is trusted. A spreadsheet is acceptable; untested tracking is not.

| Check | Pass condition |
|---|---|
| Primary event | Fires once per real action, in the confirmation state, with a value and a deduplication key; tested by hand on each variant |
| Assignment event | Fires once per visitor on first exposure |
| Campaign tags | UTM values survive redirects and reach the form or CRM where needed |
| Offline and chat sources | Unique link, QR code, promo code or WhatsApp keyword per source, plus a "how did you hear" field |
| CRM reconciliation | Site-recorded conversions match CRM or order records within an agreed tolerance for a recent week |
| Consent | The consent state is known for each audience; for EEA, UK and Swiss visitors using Google tags, Consent Mode v2 is in place (register CW-10) |
| Baseline | At least 28 days of clean data for the primary metric, or the no-baseline method in section 8 |

If any check fails, fix the tracking first. Record the failure in the experiment logbook.

## 4. Test before you optimise

Two different activities are often confused.

| | Test | Optimise |
|---|---|---|
| Purpose | Find out whether a channel, offer or concept works at all | Improve something already shown to work |
| Scale | Few variants: for example two adverts pointing to two landing pages | Many variants, one variable at a time |
| Questions | What does a customer cost? How many are available? Are they the customers we want? | Which headline, form length or layout performs best? |
| Budget | Capped and small | Grows with the evidence |

Rules:

- Do not optimise a channel or page that has not passed a test.
- Look for large changes first (a new offer, a new page structure, a different enquiry route), then fine-tune small elements once the large question is settled.
- Every channel's response tends to decay as it gets crowded. Keep a small share of effort for new tests even when a channel is working.

## 5. Set win-rate expectations honestly

Most tests do not produce a winner. Weinberg and Mares quote growth practitioner Andrew Chen's experience that only one to three of every ten tests win. Treat this as one practitioner's anecdote, not a benchmark, but use it to set expectations:

- Tell the client at the start that most tests will be losses or inconclusive, and that these still produce learning.
- Report losses and inconclusive results in the monthly report and the quarterly review, with what was learned.
- Never promise a lift, a win rate or a revenue increase from a testing programme.
- Measure the programme on learning velocity (tests decided per quarter, decisions made) as well as on wins.

## 6. When one metric wins and another loses

A variant can lift the primary metric and harm another (a shorter form raises enquiries but lowers the qualified share). Decide these cases by rule, not by preference.

1. **Before the test**, record the quarter's strategic objective in the measurement plan: the one metric and its guard-rails.
2. **Ask the owner** at planning time: "Which matters more this quarter: [growth metric] or [quality or profit metric]?" Write the answer into the decision rule.
3. **At decision time**, check:
   - Did the primary metric move beyond the minimum meaningful effect, with a confidence interval that excludes zero?
   - Did any guard-rail breach its floor?
   - Does the direction of the trade-off serve the recorded objective?
4. **Decide:**
   - Primary wins and guard-rails hold: ship.
   - Primary wins, a guard-rail breaches: do not ship. Iterate on a version that protects the guard-rail.
   - Primary wins, a secondary metric (not a guard-rail) falls: ship only if the recorded objective favours the primary; record the cost.
   - Lift not significant: it is not a win, whatever the point estimate. Record it as inconclusive.

Worked example (illustrative). A clinic's quarter objective is "qualified consultation bookings", because doctors' time is the constraint. A shorter booking form lifts completed bookings but lowers the share that sales marks as qualified, and qualified bookings are flat. The guard-rail (qualified share) breaches: kill the variant and test a short form with one qualifying question.

## 7. Explain p-values correctly

Use these words with clients and in reports.

**Plain-English definition.** A p-value answers: "If this change truly had no effect, how often would we see a difference at least this large just from normal variation?" A small p-value means the result would be surprising if the change did nothing.

**What a p-value is not:**

- It is not the probability that the variant works.
- It is not the probability that the result was "due to chance".
- It does not tell you how big the effect is or whether it matters commercially.

**How to read it:**

- The usual threshold is 0.05, fixed before the test. A result at p = 0.07 or p = 0.20 is not significant; do not call it "nearly a win".
- Always report the effect size and its confidence interval with the p-value.
- A 95% confidence interval comes from a method that, over many repeated experiments, would contain the true effect about 95% of the time. It does not mean there is a 95% probability that the true effect lies inside this particular interval.
- Checking results repeatedly and stopping when p dips below the threshold inflates false positives; follow the stopping rule in the hypothesis template.

**Client phrases:**

- "The variant's lift was [x]% with a 95% interval from [a]% to [b]%. Because the interval includes zero, we cannot tell it apart from no effect."
- "A result this large would be unusual if the change did nothing, so we treat it as a real difference. The likely size is between [a] and [b]."

## 8. Setting a line when no baseline or benchmark exists

New sites, new offers and East African markets often have no usable history and no credible external benchmark. Derive a working line from the site's own improvement curve.

1. Run a sequence of improvement iterations on the metric over two to six weeks (for example, successive sign-up page revisions).
2. Record the metric daily or weekly with dates of each change.
3. Plot the values and fit a simple trend (a moving average or a curve that flattens).
4. Read where the curve levels off. That level is the working ceiling for the current design.
5. Compare the ceiling with what the business model needs (see the lead arithmetic in `marketing-measurement-system`).
   - Ceiling above the requirement: set the line at the requirement and move on to the next constraint.
   - Ceiling below the requirement: further small changes will not close the gap. Rethink the offer, the audience or the model.
6. Replace the working line with the client's measured baseline once three months of clean data exist.

Caveats:

- The trend describes what happened during the iterations; it does not prove which change caused what. Use controlled tests for causal claims.
- Seasonality and campaign spikes distort a short series. Note them on the chart.
- Croll and Yoskovitz illustrate the method with a sign-up rate that rose over thirty days and flattened near a ceiling. Treat that example as an illustration of the method, not as a target.

## 9. Anti-patterns

| Anti-pattern | Correction |
|---|---|
| Building the full feature to test the idea | Answer the seven questions; test the cheapest version |
| Starting a test with untested tracking | Pass the tracking-readiness gate first |
| Optimising a channel nobody has tested | Test cost, volume and fit before optimising |
| Promising a win rate or lift | Set expectations from section 5; report learning |
| Deciding mixed results by preference | Pre-record the objective and the tie-break |
| "Almost significant" wins | Not significant is inconclusive |
| Describing a p-value as the chance the variant works | Use the definition in section 7 |

## Sources

- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics: Use Data to Build a Better Startup Faster*. O'Reilly Media. (Seven questions before building a feature, the experiment charter pattern, the no-baseline trend method.)
- Lin, L. C. (2013) *Decode and Conquer: Answers to Product Management Interviews*, 2nd edn. Impact Interview. (Win-lose result tie-break by strategic objective; significance reading.)
- Weinberg, G. and Mares, J. (2014) *Traction: A Startup Guide to Getting Customers*. S-curves Publishing. (Tracking before testing, test versus optimise, channel decay, win-rate anecdote attributed to Andrew Chen.)
- Currentness register 2026-09-23, claim CW-10.
