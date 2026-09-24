# Legacy-Site Performance Audit

Parent skill: [deploy](../SKILL.md). Read when a prospect or new retainer client
already has a site (often WordPress, Shopify, Wix or a page builder) and needs a
performance audit, a retrofit plan or evidence for a rebuild decision. Search
and conversion findings belong to `seo-audit` and `cro-audit`; this file covers
speed and stability.

## Audit procedure

1. **Scope.** List the five to ten templates that carry revenue (home, top
   service or product, contact or booking, checkout, top blog post). Audit
   templates, not every URL.
2. **Field first.** Check CrUX (PageSpeed Insights field section, Search
   Console) for the origin and key URLs. Record p75 LCP, INP and CLS per device
   class, or `NOT_ASSESSED` if no record exists.
3. **Lab baseline.** Run the engine's stress profile and Lighthouse default
   mobile, three runs each, median, Lighthouse version recorded.
4. **Inventory third parties.** Count third-party origins, bytes and
   main-thread time per template. Measure the tax of the heaviest three with the
   block-domain method in [third-party cost measurement](third-party-cost-measurement.md).
5. **Weight audit.** Run `scripts/route-weight-budget.mjs` against a saved copy
   of the rendered pages where possible, or read the Lighthouse network table.
6. **Findings table.** One row per issue: template, evidence (lab or field),
   cause, fix, effort, expected direction of effect, owner.
7. **Decision.** Retrofit, partial rebuild, or full rebuild. Recommend a rebuild
   only when the platform prevents the fixes that matter (for example a theme
   or app layer that cannot be made to pass the budget).

## Common retrofit checklist

| Area | Check | Typical fix |
|---|---|---|
| Hero | LCP image lazy-loaded, set as CSS background, or oversized | Real `<img>`, eager, `fetchpriority="high"`, responsive candidates |
| Scripts | Plugin or app scripts in `<head>` on every page | Load per page type; `defer`; remove unused plugins or apps |
| Chat, maps, video, social | Live embeds on load | Facades or links (see third-party facades) |
| Fonts | Several families and weights from a font service | Self-host, subset, two weights, preload, `font-display` |
| Images | No dimensions; no modern formats | Dimensions; AVIF or WebP; responsive `srcset` |
| Caching | No page cache; `no-store` HTML | Page or edge cache with revalidation (see edge caching) |
| Tag manager | "Fire everything on all pages" | Page-type triggers; fire after load; server-side tagging where justified |
| Commerce | Review, pop-up and upsell apps on every template | Product-template-only reviews; minimal checkout; delayed pop-ups |

Platform-specific tactics (plugin names, enqueue options, theme settings)
change often. Check the platform's current documentation before naming a
plugin or setting in a client report.

## Modernisation checklist for 2014–2018-era builds

Many small-business sites still carry patterns from responsive-era tutorials.
Check each and record the fix:

1. **Viewport:** remove `maximum-scale=1` and `user-scalable=no`; blocking zoom
   fails users with low vision.
2. **Images:** convert density-only (`1x/2x/3x`) `srcset` on fluid images to
   width descriptors plus `sizes`; add dimensions; lazy-load below the fold
   only; AVIF or WebP; cap mobile hero candidates at about 2x density; check
   the hero against the above-fold budget.
3. **Iframes and video:** replace the padding-bottom percentage hack with
   `aspect-ratio`; lazy-load iframes; use facades for video and maps; add
   posters; remove autoplay.
4. **Layout:** replace float and percentage box-maths layouts with Grid or Flex
   and `gap`; `box-sizing: border-box`; remove fixed pixel heights from content
   blocks (they break with longer Kiswahili or French strings and with zoom).
5. **Typography:** root font size back to 100%; fluid scale; body text at least
   16 px equivalent; typeface chosen with a reason (design-system-skills).
6. **Icons:** replace icon fonts loaded from a CDN with self-hosted inline SVG or
   an SVG sprite, labelled or hidden from assistive technology.
7. **Navigation:** rebuild the menu toggle as an accessible disclosure button
   (`aria-expanded`, Escape to close, focus handling, 44 by 44 px target, usable
   without JavaScript).
8. **Colour:** check every text and background pair against WCAG 2.2 AA; give
   buttons and links a non-colour signifier and a visible focus state.
9. **Motion:** remove JavaScript scroll-listener parallax and any auto-scroll or
   scroll-jacking; use static layers or transform- and opacity-only effects
   behind a reduced-motion guard.
10. **Routing:** replace hash-routed content (`#news`) with real URLs whose
    content is in the initial HTML.
11. **Security:** remove API keys from client JavaScript; stop inserting remote
    strings with `innerHTML`; move data fetching to build or edge time; add a
    content security policy.
12. **Dead dependencies:** check every external API and CDN for shutdown or
    breaking changes.

## Report language

- "Real visitors on phones saw the main content at [X] s (75th percentile,
  [period]). In our low-end stress test the same page took [Y] s."
- "Removing or deferring [tag] made [page] [N] s faster in our test. Its
  business value is [value / not measured]."
- Do not promise a Lighthouse score. Promise specific fixes and a field
  re-measurement date.

## Outputs

- Findings table with evidence class on every row.
- Retrofit or rebuild recommendation with reasons.
- Re-measurement plan (28-day field window after fixes).

## Sources

- LaGrone, B. (2016) *Web Design Blueprints*, Packt Publishing — used as a
  catalogue of dated responsive, flat, parallax and hash-routing patterns to
  retire; none of its code is to be copied.

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — platform playbooks for WordPress and commerce platforms, third-party
  inventory and field-first diagnosis.
