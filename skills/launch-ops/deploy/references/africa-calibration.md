# Africa-Realistic Gate Calibration

Parent skill: [deploy](../SKILL.md). Read when setting or explaining the lab
network profile, device assumptions, weight budgets or market speed claims.

The enforcement gates are only premium if they reflect the conditions the
site's actual users face. This reference is how the engine calibrates
Lighthouse budgets, network profiles, image budgets, and feature behaviour
for the African market. The full pattern library is in
`africa-excellence/SKILL.md`; this file is the calibration-specific subset
consumed by the Phase 10 gates.

## Network Profile

The blocking lab gate uses a deliberate **low-end stress profile**. It is a
worst-case floor chosen on purpose, not a measurement of the typical visitor.

| Parameter | Value | Where the value comes from |
|---|---|---|
| Downlink | 1638 Kbps (~1.6 Mbps) | WebPageTest "3G" connectivity preset (SRC-WPT-CONNECTIVITY) |
| Uplink | 768 Kbps | WebPageTest "3G" preset |
| RTT | 300 ms | WebPageTest "3G" preset |
| CPU slowdown (simulate) | 4x | Lighthouse default mobile CPU multiplier (SRC-LH-THROTTLING) |
| Screen emulation | 412 x 823, DPR 1.75 | Lighthouse mobile emulation, "moto g power (2022)" (SRC-LH-CONSTANTS) |

These values live in `performance-budgets.json` under `network_profile`
(`is_median: false`) and in `lighthouserc.json`. Earlier versions of this file
attributed the profile to "African 3G median telco data". That attribution was
wrong: the numbers are a synthetic tool preset. Label every lab result with the
profile name, the Lighthouse version and the run count.

### How the stress profile compares with other evidence

| Evidence | Down / RTT | Status |
|---|---|---|
| Engine stress profile (WPT "3G"), a throttled Slow-4G/3G profile | 1.6 Mbps / 300 ms | Deliberate conservative STRESS floor, not a measurement; blocks deploy |
| Lighthouse default mobile ("Slow 4G") | 1.6 Mbps / 150 ms, 4x CPU | Advisory comparison config `lighthouserc.default-mobile.json` |
| Uganda, UCC QoS drive tests, Aug-Sep 2024, 30 towns, peak hours (SRC-UCC-QOS-2024) | roughly 5-16 Mbps mean mobile download by operator (MTN 16.3, Airtel 15.5, Lycamobile 5.3); latency 69-84 ms | Regulator drive tests, not a user median; about two years old; figures come from an Ecofin Agency summary dated 2025-01-20 and are not verified against the UCC table (register 2026-09-24) |
| Uganda, SpeedOf.Me, H1 2026 (SRC-SPEEDOFME) | median download 8.4 Mbps; latency 192 ms | Small self-selected browser-test sample, mixed desktop and mobile, page undated; not Ookla, not UCC |
| Kenya, search-reported Ookla median 45.37 Mbps and a StatRanker snapshot of 50.63 Mbps, about Oct 2025 (SRC-KE-SPEED) | roughly 45-50 Mbps | Secondary reports; snapshot month unconfirmed; the Ookla page was not accessible. No source was found for the earlier "28 ms" Kenya latency, so it is withdrawn |
| Uganda, Tanzania and Rwanda Ookla Speedtest Global Index; Opensignal Uganda (SRC-OOKLA) | not fetched | `NOT_ASSESSED` (site refused the fetch); do not quote a figure. Tanzania and Rwanda: no source found |

Every source found puts market speeds above 1.6 Mbps: the 1.6 Mbps / 300 ms
profile is **not** a measured Ugandan or East African median (SRC-NET-SYNTH,
register 2026-09-24). It is defensible only as a deliberately conservative
stress profile for the constrained and congested tail: rural users, congested
cells, 3G fallback, prepaid users who have exhausted a bundle, and low-end
devices. No source quantifies that tail (inference). Passing the profile is
strong evidence that the median visitor is well served; it says nothing
precise about any market's median. The gate thresholds are unchanged, because
the register gives no reason to weaken a worst-case floor.

Rules:

- Never describe the stress profile as "the African median" or as "typical"
  in a proposal, report or skill, and never say Ugandan users average 1.6 Mbps.
  Say "our throttled Slow-4G/3G stress test".
- State market speeds only from a dated, named source in the currentness
  register, with its limit. Uganda, Tanzania and Rwanda Ookla and Opensignal
  figures are `NOT_ASSESSED`.
- Crowdsourced speed medians over-represent people who run speed tests. Treat
  them as an upper bound for the typical visitor, not as the floor.
- Calibrate against field data when it exists: see
  [lab-to-field calibration](lab-to-field-calibration.md).

Rationale: measuring on a studio fibre connection gives scores that do not
predict the experience of the slowest customers. A premium engine for
African markets protects the tail as well as the median.

## Weight Budget

The binding cap is the **total first-load weight per route: 350 KB**. The total
counts, for the route's built page: the HTML document (gzip), linked and inline
CSS (gzip), same-origin and inline JavaScript (gzip), font files, and every
eager (non-lazy) image at the srcset candidate a 412 px mobile viewport would
load. Nothing else is added; there is no separate "icons" allowance. Icons and
other assets count inside whichever category they belong to (inline SVG in the
HTML, sprites in the images).

Five category ceilings sit beneath the total. Each is enforced on its own, and
they are separate limits: they add up to more than 350 KB (30 + 30 + 80 + 80 +
200 = 420 KB), so a page cannot spend every ceiling at once; the total is what
stops it.

| Line | Ceiling | How it is enforced |
|---|---|---|
| Total first load | 350 KB (route overrides may only go lower) | `route-weight-budget.mjs`; Lighthouse `total-byte-weight` per route |
| HTML | 30 KB gzip | `route-weight-budget.mjs` |
| CSS | 30 KB gzip | `route-weight-budget.mjs` |
| JS | 80 KB gzip (60 KB on `/`, 90 KB on `/contact/`) | `route-weight-budget.mjs` |
| Fonts | 80 KB per page | `route-weight-budget.mjs`, plus `check-font-performance.sh` |
| Above-fold image | 200 KB (150 KB on `/`) | `route-weight-budget.mjs` |
| Third-party JavaScript | 0 KB unless allowlisted | `route-weight-budget.mjs`; `audit-third-party-js.sh` |

A route budget above the global total is rejected as invalid unless the route
carries an `exception_decision` entry pointing to its decision record.

Templates (`/blog/[slug]/`, `/services/[slug]/`) are gated through one
representative built page each: the route's `representative` path if set, else
the first matching page in alphabetical order. Lighthouse runs on the same page.
A budgeted route with no built page is `NOT_ASSESSED` and blocks release unless
the budget marks it `"optional": true` with a decision entry (for a site with no
blog, for example).

`scripts/perf-gate.sh` enforces the lines above at build time through
`scripts/route-weight-budget.mjs`: HTML, CSS and JS are gzip-compressed at
level 9 as a transfer-size proxy; fonts and images count raw bytes; lazy
images are excluded from first load; any non-allowlisted external script fails
the zero third-party budget. Lighthouse `total-byte-weight` is the lab
cross-check. Before 2026-09-23 the script measured raw HTML bytes only, so the
JS, CSS, font and image budgets were not enforced; treat earlier gate passes
accordingly.

## Low-Bandwidth Fallback

Every interactive feature must degrade gracefully on a connection that
intermittently drops to 2G (256 Kbps). This is not hypothetical — mobile
network quality fluctuates across African markets, and a premium site
earns its reputation on the worst-case commute, not the studio wi-fi.

Required behaviours:

- Form submit retries transparently on network flap.
- Form content preserved on navigation.
- Non-critical images lazy-loaded with `loading="lazy"`.
- No feature *requires* a CDN asset to function; degraded state is never
  a white page.
- Progressive enhancement: every CTA that triggers JS also works via a
  server round-trip (form submit, full-page nav).

## Data-Cost Respect

Africa still prices data per-megabyte on many plans. The engine enforces:

- No autoplay video, muted or not, above the fold on mobile.
- No preload of non-critical assets.
- No unsolicited downloads (e.g. PDF brochures on hover).
- `Save-Data` header honoured: when present, the site serves a reduced
  asset variant (AVIF only, no webfont variants, no LQIP blur).

## Save-Data Header Handling

Astro/Nginx pattern:

```js
// Astro middleware
export async function onRequest({ request, locals }, next) {
  if (request.headers.get('save-data') === 'on') {
    locals.saveData = true;
  }
  return next();
}
```

When `locals.saveData` is true:

- Use `fetchpriority="low"` on hero images.
- Skip web-font loading; fall back to system stack.
- Serve smaller image variants.
- Render a lightweight hero (text + link, no media).

## Device Reality

Lighthouse's mobile emulation is a "moto g power (2022)" screen with a 4x CPU
multiplier applied to whatever machine runs the test. The multiplier is
relative: a fast CI runner slowed 4x is not the same as a slow phone. Record
Lighthouse's `benchmarkIndex` from the report with every gate run so that runs
on different hardware can be compared.

The old reference to "Moto G4-class" devices is retired; the Moto G4 dates from
2016. Name current reference devices from the client's own analytics (device
model report) rather than from assumption. When analytics are not yet
available, test on at least one low-cost Android handset of the brands the
client's customers actually carry, and record the model, Android version,
browser and connection in the release evidence. Market-share claims about any
brand are volatile; state them only with a dated source.

Browsers to cover:

- Chrome on Android (dominant on Android)
- Samsung Internet on Samsung Galaxy devices
- Opera Mini or other proxy/lite browsers when analytics show them
- Safari on older iPhones (SE-class) where the audience includes iOS users

Playwright covers Chromium and WebKit; real-device testing on a low-cost
Android handset is required before launch of a premium build.

## Language and Locale

- Primary languages: English, French, Kiswahili, with project-specific
  additions (Luganda, Amharic, Yoruba, Hausa, Zulu, Arabic for North Africa).
- Font subsetting is critical. Arabic adds ~150 KB to a typical font; subset
  per language and do not ship a pan-African font bundle.
- Currency formatting must respect locale: UGX and KES have no decimals in
  many UI contexts; NGN has decimals but kobos are unusual in display.

## Trust Signals

Country-specific trust signals raise conversion and are enforced per sector
in `africa-excellence/references/africa-trust-signals.md`. Examples:

- Uganda: URSB registration number on footer, PDPO registration statement,
  mobile money logos on pricing pages.
- Kenya: KEBS certification (sector-dependent), ODPC compliance statement,
  M-Pesa logo on pricing.
- Nigeria: CAC number, NDPC compliance, payment-gateway logos (Paystack,
  Flutterwave).
- South Africa: Information Regulator statement, PAIA manual link,
  ZA payment logos (PayFast, Zapper).

## Gate Implications

The Phase 10 gates reference this calibration:

- `perf-gate.sh` → enforces every `performance-budgets.json` category
  through `scripts/route-weight-budget.mjs` and runs Lighthouse on the stress
  profile; INP is enforced from field data, not from the lab run
- `a11y-gate.sh` → tests reading order in at least English and one other
  project language
- `visual-qa.sh` → captures at 375 wide (a common small-phone width) as the
  first baseline
- `security-gate.sh` → compliance matrix covers Uganda DPPA, Kenya DPA,
  Nigeria DPA 2023, POPIA, GDPR

## Calibration Review Cadence

Review this calibration at least every six months (Lighthouse and speed data
change quickly) or when any of the following changes:

- A new dated speed report for the client's primary market is published.
- Field p75 LCP diverges from the lab result by more than the tolerance in
  the lab-to-field calibration reference.
- The Lighthouse major version bundled by `@lhci/cli` changes.
- A major device platform's market share crosses 10%.
- A new data-protection law is enacted in a target market.

Document revisions in `project-log/decisions/`.

## Reading

- `docs/source-registers/performance-currentness-2026-09-23.json` — dated
  sources for every threshold, version and speed figure in this file.
- Ookla Speedtest Global Index country pages (monthly; crowdsourced).
- GSMA Mobile Economy Report and Opensignal reports (check the publication
  date; quote only dated figures).
- DataReportal Digital reports for key countries (annual).
- [Lab-to-field calibration](lab-to-field-calibration.md) and
  [performance gate](performance-gate.md).
- `africa-excellence/references/low-bandwidth-patterns.md` — full pattern
  library.
- `performance-budgets.json` — machine-readable version of the budget.
