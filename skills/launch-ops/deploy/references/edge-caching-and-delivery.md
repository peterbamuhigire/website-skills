# Edge Caching and Delivery

Parent skill: [deploy](../SKILL.md). Read when choosing hosting, CDN and cache
headers for a static site, when field TTFB is high, or when deciding whether to
use prefetch or prerender.

On a high-latency mobile connection, time to first byte and connection setup
dominate the first visit. Static sites can be served from a CDN edge close to
the visitor; do it deliberately and verify it.

## Cache policy recipe (static output)

| Resource | Cache-Control pattern | Why |
|---|---|---|
| Fingerprinted assets (`app.3f9a.js`, `site.a1b2.css`, fonts, images with hashed names) | `public, max-age=31536000, immutable` | The file name changes when the content changes |
| HTML documents | `public, max-age=0, s-maxage=<short>, stale-while-revalidate=<longer>` at the edge, or the host's equivalent | Visitors get a cached page at edge speed while the edge fetches a fresh copy in the background |
| Sitemaps, `robots.txt`, feeds | short `max-age` with revalidation | Search engines see changes quickly |
| Personalised or form-result pages | `private, no-store` only where genuinely private | `no-store` on ordinary HTML blocks back/forward cache reuse |

`stale-while-revalidate` behaviour, and whether a host honours it at the edge,
differs between CDNs and hosting platforms. Check the host's current
documentation and verify with response headers (`age`, cache-status headers)
before claiming it works.

## Delivery checklist

1. Serve text assets compressed (Brotli where the host supports it, otherwise
   gzip); verify `content-encoding` on HTML, CSS and JS.
2. Serve over HTTP/2 or HTTP/3; check the protocol in DevTools or WebPageTest.
3. Choose a host or CDN with points of presence near the client's audience.
   Check the provider's current PoP map for the target countries; do not state
   PoP locations from memory.
4. Where the host supports 103 Early Hints, consider it for critical CSS and the
   hero image. HTTP/2 Server Push is no longer an option in Chrome.
5. Keep pages eligible for the back/forward cache: no `unload` handlers, no
   `Cache-Control: no-store` on ordinary HTML. Check with the DevTools
   back/forward cache panel.
6. Measure TTFB from the target market (WebPageTest location or RUM
   `timeToFirstByte` attribution), not only from the studio.

## Speculative loading: data-cost aware

Prefetching or prerendering the next likely page can make navigation feel
instant, but it spends the visitor's data. On prepaid, per-megabyte data this
is a real cost.

Rules:

- Default off. Enable only for one or two high-confidence next steps (for
  example the primary CTA's destination).
- Prefer prefetch over prerender; prefer conservative eagerness (on pointer
  down or hover intent) over eager.
- Skip speculation when `Save-Data` is on or the effective connection type is
  2G or slower.
- Speculation Rules are browser-specific; check current support before relying
  on them and treat unsupported browsers as the normal path.

## Worked example

A Nairobi retailer's field p75 TTFB is 1.4 s because HTML is served from a
single origin abroad with `no-cache`. Change: hashed assets immutable for a
year; HTML cached at the edge with a short shared max-age and
`stale-while-revalidate`; Brotli verified. Re-measure RUM TTFB over 28 days and
report the before and after at p75.

## Sources

- Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly
  Media — edge HTML caching with stale-while-revalidate, compression, HTTP/3,
  Early Hints, speculation and back/forward cache guidance.
- Grigorik, I. *High Performance Browser Networking*, O'Reilly — latency and
  connection-setup cost model.
