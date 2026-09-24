# Touchpoint Consistency Audit (Pre-Launch Gate)

Parent skill: [launch-campaigns](../SKILL.md). Read before any paid traffic, email or WhatsApp broadcast is pointed at the site, and whenever a campaign produces clicks but few enquiries. The audit checks that every place a buyer meets the brand tells the same story as the advertising, so that money is not spent sending people to a page, a phone call or a reply that contradicts the ad.

The receiving-side handoff with the marketing engine (landing-page brief, message-match table, UTM and event definitions) is covered in [channel-to-site handoff: receiving side](channel-to-site-handoff-receiving.md). This file is the consistency gate that runs after that package is accepted and before launch.

## 1. The principle

A brand is every slice of the buyer's experience: the ad, the landing page, the home page, the photographs, the WhatsApp reply, the phone greeting, the reviews, the proposal. Advertising that works can still fail if one slice contradicts it. A strong ad pointed at a text-heavy page that is hard to read on a phone, or at a reply that arrives two days late, loses the lead.

## 2. Inputs

| Input | Source | If missing |
|---|---|---|
| Two or three value themes the campaign will stress | Campaign strategy (marketing engine) or `brand-strategy` | Stop; the audit has nothing to test against |
| Message-match table (ad promise to page element) | Channel-to-site handoff package | Build a provisional table from the live ads and mark it provisional |
| Ad creative and copy for every variant | Marketing engine | Audit only the variants supplied; list the rest as not assessed |
| Proof inventory (reviews, case studies, certificates) with consent status | Client and `agency-positioning` proof library | Treat unconsented proof as absent |
| Contact scripts and quick replies | Client front desk or sales lead | Request them; the audit cannot pass without them |

## 3. Slice inventory

List every touchpoint the campaign's buyer will meet in the first week.

| Slice | Examples |
|---|---|
| Advertising | Each ad variant, search ad text, WhatsApp click-to-chat greeting |
| Landing page | The campaign page and its thank-you or confirmation state |
| Supporting pages | Home, service, pricing, About, contact pages a buyer is likely to open |
| Search presence | Google Business Profile description, photos, hours, review replies |
| Human contact | WhatsApp quick replies, phone greeting, call script, email auto-reply, response time |
| People and place | Founder and staff photographs, uniforms, vehicles, signage, premises from the road |
| Documents | Price sheet, proposal template, brochure PDF |
| After conversion | Confirmation message, onboarding email, follow-up, review request |

## 4. The audit table

Score each slice against each check. Use pass, fail, or not assessed; never record an unchecked item as passed.

| Slice | Theme 1 visible | Theme 2 visible | Theme 3 visible | Matches ad promise | Trust proof where the buyer first looks | Works on a phone | Contact route and reply time stated | Result |
|---|---|---|---|---|---|---|---|---|

Check definitions:

1. **Theme visible**: the value theme appears in words or imagery a first-time visitor would notice, not only deep in the page.
2. **Matches ad promise**: every promise in the ad is answered truthfully on this slice, in the same terms. A price, deadline or offer in the ad is identical on the page and in the reply script.
3. **Trust proof where the buyer first looks**: on the landing page, a real, consented, dated proof element (a named review with its source, a case result, a registration or certificate) sits within the first screen on a phone, next to the main claim.
4. **Works on a phone**: see section 5.
5. **Contact route and reply time**: a visible human route (tap-to-call, WhatsApp link) with a reply time the team actually meets.

## 5. Mobile check (run on a real mid-range Android phone)

- The first screen shows the offer, the proof element and a next step, not only a large photograph.
- Text is readable without zooming; buttons can be tapped with a thumb.
- The form works with the phone keyboard and asks only for what sales uses.
- Tap-to-call and WhatsApp links open the right number with a prefilled greeting that matches the ad.
- The page passes this engine's performance gate on its stress profile; use the performance-gate references in `launch-ops/deploy` for thresholds (Core Web Vitals targets are recorded in register CW-01).
- Accessibility follows WCAG 2.2 AA (register CW-05).

## 6. People and imagery standard

Faces and premises are slices too. Set the requirement here and route the visual decisions (art direction, crop, colour treatment, casting) to `design-system-skills`.

- Photographs of founders and staff are real, current and consented; stock images are never presented as staff or customers.
- The treatment is consistent across the ad and the site, so a visitor recognises the same people and place.
- Dress, setting and expression fit the value themes (a firm selling calm reliability does not use casual party photos on its About page).
- People shown as customers have given written consent; no one is shown only as a recipient of help.

## 7. Human-contact alignment

1. Rewrite quick replies, call greeting and first-response email so each repeats the campaign's value themes and the exact offer.
2. State and meet a reply time. Test it: send a message and make a call as a buyer on a weekday and at the weekend, and record the times.
3. Give the front desk a short sheet: the offer, its real conditions, the three most likely questions and their approved answers.

## 8. Gate rules

- **Blocking** (no paid traffic until fixed): the landing page fails "matches ad promise"; no consented proof on the first phone screen; the page fails the mobile check or the performance gate; no monitored contact route; the reply script contradicts the offer; any fabricated or unconsented proof anywhere in the campaign.
- **Fix within the first week**: supporting pages or the business profile missing a theme; imagery inconsistent between ad and site; after-conversion messages not yet aligned.
- **Log and schedule**: documents (price sheet, brochure) out of date but not contradicting the offer.

Record the result with the date, the tester and the evidence (screenshots, test-call times) in the release checklist required by the parent skill.

## 9. Ethics and compliance checks

- Reviews and testimonials are genuine, attributed as agreed, and never bought or written by the business. (In the United States, fake and bought reviews are banned outright by the FTC rule recorded in register AD-09; treat that as the minimum standard everywhere.)
- Urgency and scarcity in the ad are real, and the page states the real reason.
- Any comparison with a competitor is truthful and has had legal review; prefer comparing with a category behaviour rather than a named rival.
- The privacy notice covers any tracking the campaign relies on and the contact data the form collects (Uganda register PL-01; Kenya register PL-02); route changes to `policy-pages`.

## 10. After launch

Re-run the audit table for the landing page and human contact weekly during the first month, and whenever the ad creative, offer or price changes. Feed lead-quality notes from sales back to the marketing engine through the handoff channel.

## 11. Worked example (illustrative)

A Kampala fumigation firm's new ads stress three themes: safe for children and pets, uniformed and locally owned, and a quarterly plan with termite checks included. The audit finds the landing page leads with "50% OFF" (fails theme and ad match), the only review is an unattributed quotation (fails proof), the WhatsApp quick reply quotes a different price (blocking), and the About page shows the founders in a casual photograph in front of a car (imagery, fix within a week). Paid traffic is held. The team replaces the discount banner with the quarterly plan and its price, adds two named reviews with the customers' written consent, rewrites the quick replies, and books a staff photo session in uniform. The re-audit passes and the campaign starts four days later.

One practitioner reports a campaign that produced 237 leads but only 8 sales because the client never fixed a site that contradicted the ads. The figure is an unaudited anecdote; the lesson is the gate.

## Sources

- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe Media (Lioncrest imprint; publisher inferred from ISBN) — the brand as every "slice", the slice audit as a condition for launching paid media, trust proof where the buyer first looks, rewriting call scripts to repeat the value themes, and the anecdote cited in section 11.
- Currentness register of 2026-09-23, claims CW-01, CW-05, AD-09, PL-01 and PL-02.
