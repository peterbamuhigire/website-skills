# RUM Attribution and Segmentation

Parent skill: [observability](../SKILL.md). Read when extending the RUM
contract in [rum-implementation](rum-implementation.md) so that field data can
explain *why* a metric is poor, and when aggregating field data for reports.

## Use the attribution build

Import from `web-vitals/attribution` instead of `web-vitals` on sites where
diagnosis matters (all retainer clients). The `web-vitals` package was at
version 6.2.2 on npm when checked on 2026-09-23; `onFID` no longer exists. Pin
the version in the client project and re-check field names on upgrade.

```js
import { onLCP, onINP, onCLS, onTTFB } from 'web-vitals/attribution';

function send(metric) {
  const a = metric.attribution || {};
  const body = {
    site: SITE_SLUG,
    route_template: ROUTE_TEMPLATE,          // e.g. "/services/[slug]/", not the raw URL
    metric: metric.name,
    value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
    rating: metric.rating,
    id: metric.id,
    navigation_type: metric.navigationType,
    connection: navigator.connection?.effectiveType ?? 'unknown',
    save_data: navigator.connection?.saveData ?? null,
    visitor: localStorage.getItem('rv') ? 'returning' : 'new',
    // LCP sub-parts
    lcp_target: a.target, lcp_ttfb: a.timeToFirstByte, lcp_load_delay: a.resourceLoadDelay,
    lcp_load_duration: a.resourceLoadDuration, lcp_render_delay: a.elementRenderDelay,
    // INP phases
    inp_target: a.interactionTarget, inp_type: a.interactionType,
    inp_input_delay: a.inputDelay, inp_processing: a.processingDuration,
    inp_presentation: a.presentationDelay,
    // CLS
    cls_target: a.largestShiftTarget,
  };
  navigator.sendBeacon('/rum', JSON.stringify(body));
}
onLCP(send); onINP(send); onCLS(send); onTTFB(send);
try { localStorage.setItem('rv', '1'); } catch (_) { /* storage blocked: visitor stays "new" */ }
```

Only send the fields that apply to each metric; the schema must match the
endpoint contract and the analytics event map. The visitor flag uses first-party
storage; check the consent requirements for the audience before setting it.

## Required segments

| Segment | Why |
|---|---|
| Route template | Fixes are made per template, not per URL |
| Device class (mobile, desktop) | Core Web Vitals are assessed per device class |
| Connection (`effectiveType`, `saveData`) | Separates network cost from code cost; absent in some browsers |
| New vs returning visitor | Cold cache versus warm cache behave differently |

## Aggregation rules

- Report the 75th percentile per metric per segment for the period (28 days
  matches CrUX windows).
- Report the share of "good" sessions: good-rated sessions ÷ all sessions for
  that metric and segment.
- Record the session count beside every p75; mark small segments
  `insufficient data`.
- Do not average percentiles across segments; recompute from raw events.

## Triage table: attribution to fix

| Attribution shows | Likely cause | Fix owner |
|---|---|---|
| LCP dominated by `timeToFirstByte` | Origin distance, cache miss, slow server | deploy (edge caching) |
| LCP dominated by `resourceLoadDelay` | Hero discovered late (CSS background, JS-injected, lazy) | page-builder |
| LCP dominated by `resourceLoadDuration` | Hero too heavy | image-compression |
| LCP dominated by `elementRenderDelay` | Render-blocking CSS or scripts, font blocking | page-builder, design-system |
| INP high `inputDelay` | Main thread busy (hydration, third parties) at interaction time | page-builder, deploy (third parties) |
| INP high `processingDuration` | Heavy handler | page-builder ([INP-safe patterns](../../../build/page-builder/references/inp-safe-interaction-patterns.md)) |
| INP high `presentationDelay` | Large DOM update or layout after the handler | page-builder |
| CLS `largestShiftTarget` repeats | Unsized media, injected banner, font swap | page-builder |

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — field capture dimensions and lab/field feedback.
- `web-vitals` README (GoogleChrome/web-vitals, read 2026-09-23) for attribution
  field names; web.dev Web Vitals (SRC-WEBDEV-VITALS) for p75 assessment.
