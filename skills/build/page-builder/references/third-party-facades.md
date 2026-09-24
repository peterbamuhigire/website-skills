# Third-Party Facades and Zero-JS Substitutes

Parent skill: [page-builder](../SKILL.md). Read when a page needs chat, a map,
video, a social feed, reviews or any other embed that would normally load a
third-party script or iframe.

The engine ships zero third-party runtime JavaScript by default. When a client
wants the function an embed provides, offer the substitute first; offer a
facade (a lightweight placeholder that loads the real embed only when asked)
second; allow a live embed only through
[third-party cost measurement](../../../launch-ops/deploy/references/third-party-cost-measurement.md).

## Substitution table

| Request | First choice (no third-party JS) | Facade (if the live embed is truly needed) |
|---|---|---|
| Live chat widget | Visible WhatsApp click-to-chat button and phone link (see below) | "Live chat" button that injects the vendor script on click, shows "Loading chat…", and falls back to phone and email if the script fails |
| Google Map | Static map image (self-hosted, sized, compressed) plus the written address, landmark directions and an "Open in Maps" link | Tap-to-load interactive map in a reserved box |
| YouTube or Vimeo video | Poster image with a play button linking to the video; transcript or summary on the page | Click-to-load player (lite embed pattern) with the poster in place until click |
| Facebook or Instagram feed | Build-time rendered posts (fetched during the build, output as static HTML) or a plain "Follow us" link | None needed |
| Review widget | Curated, attributed testimonials in the page HTML with a link to the review platform | Click-to-load widget below the fold |
| Booking or calendar embed | Link or button to the booking page; form on the site | Load the embed on the booking page only, after interaction |

## WhatsApp and phone as the primary contact path

In markets where customers already use WhatsApp for business, a visible
WhatsApp button and a tap-to-call phone number are both a zero-JavaScript
contact path and a trust signal: they show that a real, reachable business
stands behind the site.

Phrasing rule (Digital Research register 2026-09-24, claim MKT-001): call
WhatsApp a dominant messaging channel in East Africa. Do not write that it is
used by "90%+ of smartphone users": no source measures that share. If a
percentage is used, cite its source, base and date (for example Pew 2023,
adults: at least half in every country surveyed, including Kenya) and check
the client's own audience data.

Build rules:

- Use a plain link: `https://wa.me/<international-number-without-plus>?text=<url-encoded message>`.
  Prefill a short, specific message ("Hello, I'd like a quote for …"), not a
  generic greeting.
- Show the number in text as well, formatted for the market (for example
  `+256 7XX XXX XXX`), so visitors on desktop or without WhatsApp can still act.
- Add a `tel:` link for calls. State the hours when someone answers.
- Give the button an accessible name ("Chat with us on WhatsApp") and a visible
  focus style; do not rely on the logo alone.
- Keep it fixed on mobile only if it does not cover content or other controls;
  reserve space so it causes no layout shift.
- Track clicks as a named conversion event (see `marketing-measurement-system`),
  without loading a WhatsApp script.
- Do not state WhatsApp usage figures for a country unless they come from a
  named, dated survey (currentness register MK-03: no admissible figure for
  Uganda or Kenya when checked on 2026-09-23).

## Three-phase facade pattern

1. **Render** a lightweight placeholder with the same dimensions as the final
   embed (no layout shift), an accessible button, and a text alternative.
2. **Warm up** (optional): on hover, focus or touch-start, preconnect to the
   vendor origin.
3. **Load** the real embed on click, move focus sensibly, and show a loading
   state. If loading fails or takes too long, show a fallback link.

Conditional loading: when `Save-Data` is on, or the effective connection is 2G
or slower, keep the substitute and do not load the embed automatically. The
Network Information and Device Memory APIs are not available in every browser;
treat their absence as "unknown", not as "fast".

## Poster images

- The poster is a real `<img>` with dimensions and a modern format, within the
  image budget. If it is the hero, it follows the LCP rules (eager,
  `fetchpriority="high"`).
- Add a visible play control and descriptive alternative text.
- The poster must not be a screenshot of the vendor's player chrome.

## Acceptance checks

- Page passes `route-weight-budget` with zero third-party scripts on load.
- Placeholder and final embed occupy the same box (no CLS on click).
- Keyboard users can activate the facade; focus is managed after load.
- The fallback path works with JavaScript disabled.

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — facades, click-to-load and conditional loading of third parties;
  localised substitutions are this engine's own.
- Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask
  Before Building a Website*, Wiley — visible contact details as a trust
  requirement.
