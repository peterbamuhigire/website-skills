# Channel-to-Site Handoff: Receiving Side

Parent skill: [launch-campaigns](../SKILL.md). Read when a marketing campaign
(paid search, paid social, email, WhatsApp, influencer or offline with a short
link) will send people to a page this engine builds or maintains, or when a
campaign's clicks are not turning into enquiries.

## Who owns what

The `social-media-skills` engine (digital marketing and advertising) owns
campaign strategy, ads, audiences, the **landing-page brief**, the
**message-match table**, the **UTM convention** and the **conversion-event
definitions**. Its skill `ad-to-site-journey-handoff` produces the package;
resolve that engine from the global routing table.

This engine owns everything from acceptance of that package to a live,
measured page: build, performance, accessibility, tag implementation, QA
evidence and the post-launch fix loop. Do not rewrite the campaign strategy or
the event definitions; if they are wrong, return them with reasons.

| Handed over (by marketing) | Artefact | Receiving owner here |
|---|---|---|
| Landing-page brief (page job, audience temperature, headline, offer, proof, objections, CTA, form spec, mandatories, variants) | Brief document | `page-builder` with `sales-copywriting` / `premium-commercial-writing` |
| Message-match table (each ad promise and the page element that answers it) | Table | `page-builder`; checked by `cro-audit` |
| UTM table and naming convention | Spreadsheet | `marketing-measurement-system` (adopt as-is) |
| Conversion events with triggers, values and dedup rules | Event list | `marketing-measurement-system` and `observability` |
| Consent scope (EEA/UK/CH visitors; Uganda or Kenya data processing) | Checklist | `policy-pages`, `security-gate`, `observability` |
| Journey RACI and dates | Table | Project owner in `website-builder` |

| Handed back (by this engine) | Artefact | Consumer |
|---|---|---|
| Acceptance record or return-with-reasons list | Dated note | Campaign strategist |
| Built page URL(s) and variant IDs | Release note | Media operator |
| Tracking QA log (each event tested once per real action) | Log with dates | Analyst |
| Performance and accessibility results against the stated targets | Gate reports (lab) and, after 28 days, field p75 | Account lead |
| Weekly then monthly funnel and fix list | Report | Both engines |

## Acceptance checklist (run before build starts)

Accept the package only when:

1. There is **one page job** and one primary action.
2. The **conversion event** is defined with a trigger, a location (the thank-you
   or confirmation state), a value and a dedup rule.
3. Every **ad promise** in the message-match table can be answered truthfully
   on the page with available, consented proof. Unsupported promises go back to
   marketing; never invent proof to match an ad.
4. **Offer facts** (price, terms, deadline and its real reason) are confirmed by
   the commercial owner.
5. **Form fields** are the ones sales actually uses; consent text and privacy
   link are specified; no pre-ticked boxes.
6. **Consent scope** is known. For EEA, UK or Swiss visitors using Google tags,
   a consent management platform with Consent Mode v2 signals is required
   (register CW-10). Uganda and Kenya obligations follow the client's privacy
   notice and the data-protection rules recorded by `policy-pages` (register
   PL-01, PL-02).
7. **Owners and dates** exist for copy, build, tags, QA and traffic go-live.

Missing items are returned as a numbered list with the field, the reason and
the decision needed. Build may start on a qualified draft only with placeholders
marked `not assessed`.

## Build rules for campaign pages

- **Message match above the fold**: the headline echoes the ad's promise in the
  visitor's words; the first proof sits near the headline.
- **Awareness level**: cold traffic needs more explanation and story before the
  offer; warm and retargeting traffic can lead with the offer.
- **One primary action**; a visible human route (tap-to-call and WhatsApp
  click-to-chat with the promised response time).
- **Performance**: the page passes the engine's performance gate on the stress
  profile and stays within its route budget; no third-party scripts beyond the
  agreed tags, loaded per [third-party cost measurement](../../../launch-ops/deploy/references/third-party-cost-measurement.md).
- **Accessibility**: WCAG 2.2 AA (register CW-05).
- **Consistency**: page, contact scripts, reviews and photography tell the same
  story as the ads (run the [touchpoint consistency audit](touchpoint-consistency-audit.md)).
- **Pricing presentation** follows [pricing-page choice architecture](../../../content-copy/sales-copywriting/references/pricing-page-choice-architecture.md).

## Tag implementation and QA

1. Adopt the UTM convention exactly; do not rename parameters. Preserve UTM
   values through redirects and into form submissions where the CRM needs them.
2. Implement each conversion event where the definition says it fires (the
   confirmation state for a lead, not the button click), with the dedup rule.
3. Map event names to each platform's current event list on the day of build
   and record the date; platform names change.
4. Test each event once per real action in a staging or preview environment and
   once in production; log the result, date and tester.
5. Confirm forms reach a monitored inbox or CRM and WhatsApp is monitored at the
   promised response time.
6. Never mark tracking or consent as working without a dated test record.

## Go-live and post-launch loop

- Report lab gate results before traffic starts; the campaign's go/no-go gate is
  owned by marketing, and this engine supplies the web-side evidence.
- After launch: weekly for the first month, then monthly, review the funnel
  (visits by source, form starts, submissions, qualified leads), form drop-off,
  response times and field Core Web Vitals once 28 days of data exist.
- Rank fixes by expected impact and effort; agree them with the strategist;
  re-run the affected gates after material page changes.

## Worked example

A Kampala clinic's search campaign promises "Same-week fertility consultation".
The brief arrives with a message-match table, a `booking_confirmed` event and a
UTM table. Acceptance finds the "same-week" promise unverified: the clinic's
calendar shows ten-day waits. The package is returned; marketing changes the ad
to "Consultation within 10 days". The page is built, the event fires on the
booking confirmation page, the QA log records two tests, and the lab gate passes
before traffic starts.

## Sources

- This engine's own handoff contract, aligned with `social-media-skills`
  skill `ad-to-site-journey-handoff` (read 2026-09-24).
- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe Media (Lioncrest imprint) — touchpoint consistency between
  advertising and destination (full procedure in [touchpoint consistency audit](touchpoint-consistency-audit.md)).
