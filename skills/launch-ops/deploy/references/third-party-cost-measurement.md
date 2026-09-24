# Third-Party Cost Measurement

Parent skill: [deploy](../SKILL.md). Read when a client, marketer or partner
asks to add any external script, tag, pixel, widget or embed, and at every
quarterly tag review.

The engine's default is zero third-party runtime JavaScript. This file is the
procedure for the exceptions: it turns "please add this tag" into a measured,
owned and reviewable decision. Pair it with
[third-party facades](../../../build/page-builder/references/third-party-facades.md),
which supplies the zero-JavaScript or click-to-load alternatives to offer first.

## Onboarding procedure (every new tag or widget)

1. **Owner and value.** Name the client-side business owner and the measurable
   value the tag must produce (for example "attribute enquiries to paid
   campaigns"). No owner or no measurable value: decline.
2. **Zero-JS alternative first.** Check for a link, a WhatsApp click-to-chat
   button, a static image, a server-side integration or a build-time embed. If
   one meets the need, stop here.
3. **Least-cost mode.** If JavaScript is unavoidable, choose the vendor's
   lightest mode (async or lite script, sampling, server-side tagging).
4. **Measure the performance tax.** Run the page on the stress profile with the
   tag and with the tag's domains blocked (WebPageTest block-domain setting or
   DevTools request blocking), three runs each, median of each:
   `tax = median(metric, with tag) − median(metric, tag blocked)` for LCP, TBT,
   total bytes and main-thread time. Record the result.
5. **Single point of failure test.** Simulate the vendor responding slowly (for
   example a delayed or hanging request) and confirm the page still renders and
   its primary action still works. A tag that can blank the page is rejected or
   moved behind a facade.
6. **Loading strategy.** Choose, in order of preference: click-to-load facade,
   load when in view, load when the browser is idle, load after first
   interaction. Never render-blocking. Consent-dependent tags load only after
   consent where the law or policy requires it.
7. **Allowlist line.** Add the origin to `.third-party-allowed` as
   `<origin>  # <purpose>; owner <name>; decided <date>; review <date>`.
8. **Budget and alert.** Record the accepted tax as the tag's budget and watch
   field INP and LCP after release (see `observability`).
9. **Quarterly review.** Re-measure; remove tags whose value is unproven,
   orphaned or duplicated (for example two analytics tools recording the same
   events).

## Sequencing rules

- First-party critical content first; third-party tags late in the document.
- Always `async` or `defer`; prefer `defer` where order matters.
- Preconnect only to origins that will certainly be used on that page.
- Stagger third-party loads rather than starting many at once.
- Load by page type: nothing extra on checkout, forms or payment pages.

## Offloading options (check current support before recommending)

- Server-side tagging instead of browser tags.
- Server-side A/B testing instead of client-side flicker scripts.
- Build-time rendering of social posts instead of live feeds.
- Worker-based tag offloading libraries: check the project's maintenance status
  and compatibility before use; treat as experimental.

## Stakeholder demonstration

For a marketing lead who wants "all the tags", show two filmstrips side by side
from the stress profile: with and without the marketing domains. Say what the
difference costs every mobile visitor and ask which tag proves its value. Keep
the numbers to what was measured; never quote another company's figures as a
forecast.

## Vendor request template

> We are adding [tool] to [site]. Our performance budget for third-party code on
> [page type] is [N] KB and [M] ms of main-thread time on a low-end mobile
> profile. Please confirm: an async or lite mode; a server-side or API
> alternative; sampling options; the domains the script loads; and behaviour
> when your service is slow or unavailable.

## Evidence produced

| Evidence | Acceptance condition |
|---|---|
| Tax measurement record | Profile, Lighthouse or WebPageTest version, three-run medians with and without the tag |
| SPOF test note | Slow-vendor behaviour observed and described |
| Allowlist line | Purpose, owner, decision date and review date present |
| Quarterly review entry | Keep/remove decision with reason |

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — inventory, remove/reduce/replace, facades, sequencing, offloading and
  governance for third-party code.
