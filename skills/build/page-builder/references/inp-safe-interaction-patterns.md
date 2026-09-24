# INP-Safe Interaction Patterns

Parent skill: [page-builder](../SKILL.md). Read when building any interactive
island (menu, search, filter, gallery, form, calculator, chat or AI assistant)
or when field INP exceeds 200 ms at p75.

Interaction to Next Paint (INP) measures how long the page takes to show a
visual response after a tap, click or key press, across the whole visit. Good
is 200 ms or less at the 75th percentile of field data (web.dev, checked
2026-09-23). Lighthouse navigation runs cannot measure it; total blocking time
is only a lab proxy. INP has three phases: input delay (the main thread is
busy), processing (your handlers run) and presentation delay (style, layout and
paint of the result).

## Patterns

| Situation | Pattern |
|---|---|
| Any handler | Acknowledge within one frame (pressed state, spinner, text change), then defer heavy work |
| Filtering or searching as the user types | Debounce (around 300 ms), memoise the result, or commit on blur or submit |
| Long loops or large renders | Break work into chunks and yield to the browser between chunks (`scheduler.yield()` where supported, `setTimeout` fallback); keep each task well under 50 ms |
| Heavy parsing or computation | Move it to a web worker |
| Long lists and infinite scroll | Render smaller batches and request the next batch earlier; virtualise very long lists |
| Scroll-driven effects | IntersectionObserver or CSS instead of scroll handlers; passive listeners if a handler is unavoidable |
| Hydration | Hydrate inputs, primary CTAs and navigation first; decorative widgets last or never |
| Third parties | Nothing heavy runs at first interaction; schedule vendor work for idle time |
| Layout | Batch DOM reads before writes; never read layout inside a loop that writes |

Browser support for scheduling APIs (`scheduler.postTask`, `scheduler.yield`,
`requestIdleCallback`) differs; check current compatibility tables and always
ship a fallback.

## Streaming or AI assistant islands

If a client wants an on-site assistant that streams text:

- Batch DOM updates (for example every 50–100 ms or every few tokens), never
  one write per token.
- Parse markdown and highlight code in a worker.
- Reserve space and keep line height stable to avoid layout shift.
- Provide a keyboard-accessible Stop control.
- Announce streamed text with `aria-live="polite"`; use `assertive` only for
  errors.
- Buffer whole grapheme clusters before rendering (matters for Arabic,
  Ethiopic and emoji).
- Measure INP during active streams, plus time to first token and stall rate.
  Budgets for these are product decisions; set them from user research, not
  from a book.

## Worked example

A Kampala property site lists 200 homes with a "Search by area" box. The first
build filters all 200 cards on every key press; on a low-cost Android the
typing stutters. Fixes: debounce 300 ms, memoise the filter, paginate to 12
results per page on the server or at build time, give thumbnails dimensions,
and announce "Showing 12 homes in Ntinda" politely. Verify with the RUM INP
attribution (processing duration should fall) over the next 28 days.

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — main-thread scheduling, INP checklist and streaming-interface
  guidance.
- web.dev Web Vitals (SRC-WEBDEV-VITALS, checked 2026-09-23) for thresholds.
