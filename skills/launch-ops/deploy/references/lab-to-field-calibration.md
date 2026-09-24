# Lab-to-Field Calibration

Parent skill: [deploy](../SKILL.md). Read after launch, at every quarterly
review, or whenever a client asks why a site that "passed Lighthouse" feels
slow to real visitors. Field capture itself is owned by
[observability](../../observability/SKILL.md).

Lab tests (Lighthouse, WebPageTest, DevTools) are reproducible and block
deploy. Field data (first-party RUM, CrUX, the Search Console Core Web Vitals
report, the PageSpeed Insights field section) records what real visitors
experienced. Core Web Vitals are judged at the **75th percentile of field
data, per device class** (web.dev, checked 2026-09-23; register CW-01). Use
both; neither replaces the other.

## Evidence classes and how to label them

| Class | Examples | Can prove | Cannot prove |
|---|---|---|---|
| Lab, stress profile | `lighthouserc.json` runs | The build meets the engine's floor under a harsh, named profile | What real visitors experience |
| Lab, default mobile | `lighthouserc.default-mobile.json`, PageSpeed lab section | Comparability with Google's lab numbers | Field outcomes |
| Field, first-party RUM | `web-vitals` beacons to the agency endpoint | p75 per route template, device class and connection | Causes, unless the attribution build is used |
| Field, CrUX | PageSpeed field section, CrUX API, Search Console | Chrome-user p75 at origin or URL level | Anything for low-traffic sites with no CrUX record |

Every number in a report states: metric, class (lab or field), profile or
percentile, segment and period. "LCP 1.8 s" alone is not acceptable.

## Calibration procedure (run 28 days after launch, then quarterly)

1. **Collect field p75** for LCP, INP and CLS per route template and device
   class from RUM (and CrUX where the origin has a record). Minimum sample: note
   the session count; below a few hundred sessions per segment, mark the
   segment `insufficient data` rather than reporting a p75.
2. **Collect lab medians** for the same templates on both profiles (three runs
   each, same Lighthouse version).
3. **Compare** field p75 LCP with the lab stress-profile LCP.
   - Field slower than the stress-profile lab result: the lab is too
     optimistic for this audience. Investigate TTFB (origin distance, cache
     misses), third parties that load only in production, consent banners,
     and device CPU. Consider a stricter lab profile for this client and log a
     decision entry.
   - Field much faster than the default-mobile lab result: the audience is on
     faster networks than assumed. Keep the stress gate (it protects the tail)
     but report the field result as the success measure.
   - Field INP above 200 ms while lab TBT passes: interaction cost appears only
     with real input. Use RUM attribution (INP phases, longest script) to find
     the handler; see [INP-safe interaction patterns](../../../build/page-builder/references/inp-safe-interaction-patterns.md).
4. **Record** the comparison table, the decision (keep, tighten, investigate)
   and the owner in `project-log/decisions/`.
5. **Re-measure** after the fix over a full 28-day window before claiming an
   improvement.

## Tolerance rule

Treat a gap of more than 25% between field p75 LCP and the matching lab
median as a calibration finding that needs a written explanation. The 25%
figure is an engine working rule, not an external standard; adjust it per
client by decision entry.

## Sites with no CrUX record

Most small and medium business sites in East African markets are unlikely to
appear in CrUX because CrUX publishes only origins with enough eligible Chrome
traffic; check the specific origin rather than assuming. Where CrUX has no
record, first-party RUM is mandatory for any claim about real-visitor speed.
Without RUM, say "field performance: NOT_ASSESSED".

## Worked example (illustrative; all figures are invented)

Suppose a Kampala clinic site passes the stress gate with lab LCP 1.9 s. After 28 days,
RUM shows mobile p75 LCP 3.1 s on the booking page, with 1,400 sessions. The
attribution build shows `timeToFirstByte` dominating. Origin hosting is in
Europe with no edge cache. Decision: move HTML to edge caching with
revalidation, re-measure for 28 days, report field p75 before and after. The
client report says: "Lab test: 1.9 s on our low-end stress profile. Real
visitors on phones: 3.1 s at the 75th percentile. Cause: server distance. Fix
scheduled for [date]; we will report the new real-visitor figure on [date]."

## Anti-patterns

- Reporting a lab score as proof of user experience. Fix: pair it with field
  p75 or mark field `NOT_ASSESSED`.
- Loosening the lab gate because field looks good. Fix: keep the floor; the
  gate protects the slowest visitors.
- Comparing runs from different Lighthouse versions. Fix: pin and record the
  version.
- Reporting one run. Fix: median of at least three.
- Borrowing another company's case-study uplift as a forecast. Fix: present it
  as the direction of effect and measure the client's own before and after.

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — lab versus field doctrine and the feedback loop.
- web.dev "Web Vitals" (SRC-WEBDEV-VITALS, checked 2026-09-23) for thresholds
  and the p75 rule; see `docs/source-registers/performance-currentness-2026-09-23.json`.
