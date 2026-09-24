# Performance as a Retainer Service

Parent skill: [agency-client-retention](../SKILL.md). Read when designing,
pricing or renewing a care plan or growth retainer that includes site speed, or
when a client asks what they get each month for performance.

Speed decays after launch: new images, new tags, plugin or content changes.
Selling performance as a recurring, evidenced service keeps the site fast and
gives the retainer visible, measurable output.

## Service components

| Component | Cadence | Evidence delivered |
|---|---|---|
| Field Core Web Vitals scorecard (p75 LCP, INP, CLS per key template and device class) | Monthly | Scorecard with period, session counts, change from last month; `NOT_ASSESSED` where RUM or CrUX has no data |
| Lab regression run on the stress profile | Monthly and on every release | Lighthouse medians with version; weight report |
| Tag and third-party review | Quarterly | Inventory, measured tax of heavy tags, keep/remove decisions (see [third-party cost measurement](../../../launch-ops/deploy/references/third-party-cost-measurement.md)) |
| Tune-up sprint | Quarterly or half-yearly | Fix list with before/after field figures after a full measurement window |
| Content-team hygiene training | Once, then on staff change | Short workshop: image sizes, embeds, when to ask before adding a tag |
| Incident response for speed regressions | As needed | Alert, cause, fix, re-measure |

## Report layout: four moments

Structure the monthly speed panel around the visitor's questions:

1. **Is it happening?** Time to first byte and first paint.
2. **Is it useful?** LCP: when the main content appears.
3. **Is it usable?** INP: how quickly taps and clicks respond.
4. **Is it stable?** CLS: whether things jump around.

For each: the field p75 this month, the trend, the main cause of slow visits,
and the next fix with a date.

## Language

- "[N]% of real visits to [template] had good [metric] this month ([change]
  since last month). The main cause of the remaining slow visits is [cause];
  we will [fix] by [date]."
- "Our lab test on a low-end phone profile showed [X] s; real visitors saw [Y] s
  at the 75th percentile."
- Never promise a Lighthouse score. Promise the gates, the scorecard and a
  fix-and-re-measure cycle.

## Pricing and packaging

Include the scorecard and regression run in every care plan. Sell the tune-up
sprint and tag review as a higher tier or a fixed-fee add-on; price by the
number of templates and third-party tags in scope. Route the commercial wording
of the offer to the proposal engine; this skill owns delivery and evidence.

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — performance culture, budgets as accountability, tune-up sprints and
  the four loading moments.
