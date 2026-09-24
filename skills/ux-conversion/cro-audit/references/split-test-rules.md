# Split-Test Rules Reference

Parent skill: [cro-audit](../SKILL.md). Read when generating test hypotheses for a page, funnel or campaign.

Every rule below is a hypothesis to test, not a proven fact. Effect sizes vary by market, traffic source, device and offer, and none is quoted here. Run each test on your own traffic, with a stated success metric, a fixed run time and enough conversions to read the result. Prioritise by likely impact, ease and traffic volume.

Test order of priority: offer, then headline, then CTA presence and timing, then price and payment structure, then layout and visuals.

## Headlines

**H1. Specific figures over round ones.** Hypothesis: "Join 1,148 Kampala shop owners" is more credible than "Join over 1,000". Round numbers can read as guesses. Use only true, current counts.

**H2. Present tense.** Hypothesis: copy describing what happens now ("Your stock count updates on every sale") outperforms the future conditional ("will update") and the past tense. Test by rewriting headline and CTA copy in the present.

**H3. Headline colour contrast.** Hypothesis: a high-contrast, warm-coloured headline may draw more attention on a sales page than a brand-neutral one. Test one colour change at a time; check accessibility contrast before shipping any winner.

**H4. Anchor claims in a concrete event.** Hypothesis: a headline tied to something specific and verifiable ("How our Jinja depot cut stock-outs in one quarter") beats a generic claim. Use only true events you can evidence.

**H5. Keep faces from competing with the headline.** Hypothesis: a face beside a headline pulls the eye from the copy. Test a soft background image, or a subject looking toward the text, against a face beside the headline.

## CTAs and Buttons

**C1. Show the buy button early.** Hypothesis: visitors ready to act should never wait for it (for example, on a video page where the button appears only after a delay). Test immediate display against any delayed reveal, including on upsell pages.

**C2. Say "free" where it is true.** Hypothesis: a short note beside a free opt-in button ("Free, no card needed") reduces hesitation. Test with and without.

**C3. Benefit-action copy over urgency-only copy.** Hypothesis: "Get the stock template" beats "Limited time offer" as the line above a button. Test action-plus-outcome wording against urgency wording. Never use false urgency.

**C4. Button below the video, not beside it.** Hypothesis: a side-placed CTA is overlooked next to a video. Test below-video against side placement, and test above-video for highly engaged audiences.

**C5. Top-of-page CTA on long free-trial pages.** Hypothesis: low-commitment visitors want the action immediately. Test a prominent button at the top of a long page.

## Forms

**F1. Micro-commitment before the email field.** Hypothesis: a one-tap question ("How did you hear about us?") before the email field makes the second step feel natural. Always include an "Other" option so no visitor is stuck. Test against a plain email form.

**F2. Inline order form.** Hypothesis: keeping the order form on the sales page preserves buying momentum better than a redirect. Test inline against redirect.

**F3. Two-step order form.** Hypothesis: collect name, email and phone first and payment second; this captures leads who abandon at payment, whom you can follow up (with consent). Compare completed orders plus recovered leads against a one-step form.

**F4. Card field position.** Hypothesis: field order and side placement affect completion. Test layouts using your payment provider's compliant components; never alter security handling to test layout.

**F5. HTTPS everywhere.** Not a test: it is a baseline. Serve every page over HTTPS and confirm no mixed content.

**F6. Alternatives to social sign-in.** Hypothesis: offering email sign-up beside social login reduces drop-out. Test, and check data-protection requirements for each login method.

## Trust Signals

**T1. Testimonials at the top of the order form.** Hypothesis: anxiety peaks at the form, so proof placed before the offer recap helps. Test proof first against recap first.

**T2. Video testimonials below the sales video under a proof heading.** Hypothesis: varied voices let more visitors find someone like themselves. Test against no testimonials.

**T3. Present testimonials honestly.** Show plain attributed quotes with real name, role and photo, or a genuine social post shown natively with a link and the author's consent. Never restyle a testimonial to look like a post it never was: that misrepresents its origin and can breach consumer and endorsement rules.

**T4. Trust seals only on payment pages.** Hypothesis: security badges on non-payment pages introduce doubt that was not there. Test badge and no-badge on registration pages; keep them on checkout.

**T5. Fill empty form space.** Hypothesis: short testimonials in blank areas of an order form maintain persuasion through completion. Test against a bare form.

## Pricing and Offers

**P1. Payment plans on higher-ticket offers.** Hypothesis: an instalment option (for example three monthly payments of UGX 120,000 against one payment of UGX 330,000) removes the barrier for price-sensitive buyers. Test plan counts and amounts, and pre-select whichever option you want to anchor. State total cost clearly.

**P2. Discounts as currency amounts.** Hypothesis: "UGX 20,000 off" is easier to process than "10% off" when the currency amount is small relative to the price. Test per price band; for large prices, percentages may win.

**P3. Fewer price options with an anchor.** Hypothesis: one high-priced anchor plus one primary offer beats three tiers that split attention. Test removing the middle option.

**P4. Lead with the recurring product.** Hypothesis: selling the membership as the main offer and including the low-price item as a bonus retains more recurring customers than selling the low-price item first and upselling. Compare recurring accounts and revenue per visitor.

**P5. Free trial without a card.** Hypothesis: asking for a card lowers sign-ups but raises trial quality. Test sign-ups, paid conversions and support load together.

## Layout

**L1. Fewer choices.** Hypothesis: cutting clickable options above the fold to a handful speeds decisions. Test a stripped page.

**L2. Direct images toward the copy.** Hypothesis: subjects looking toward the message pull the eye to it. Test gaze direction on images near CTAs.

**L3. Remove sections that do not advance the decision.** Hypothesis: extra blocks can create doubt. Test a shorter version before adding anything.

**L4. Timed pop-up for engaged readers.** Hypothesis: a pop-up triggered by dwell time or scroll depth on content pages adds sign-ups without hurting the main opt-in. Show it only to non-subscribers; check whether your site rules and accessibility standards allow it; avoid landing pages.

**L5. Plain beats expensive.** Hypothesis: a simple page can convert as well as a heavily designed one, and shorter copy can beat longer on low-commitment offers. Test a plain version.

## Default Control Blueprint

Use as a starting point for a new funnel page, then test each element.

**Landing page:** curiosity-led headline that hints at the outcome; optional three-step header for warm traffic only (remove for cold traffic); final step labelled with the reward ("Get your access"); micro-survey with a closing "Other" option.

**Sales video page:** high-contrast headline above the video; button visible from load; inline order form; a short box under the video listing three to five points it covers (test whether previewing lifts completion); video controls limited only where you can justify it and accessibility allows (never disable captions or pause).

**Order form:** short attributed testimonials at the top; offer recap; card fields per provider guidance; trust seals here only; no blank space.

## Trial-Close Technique

Insert short agreement questions through a presentation, video or long page so the reader says "yes" repeatedly before the final ask. Mechanism: commitment and consistency.

Where to place them:
- Opening: two or three questions confirming the reader wants the outcome.
- After each testimonial.
- After each feature or benefit.
- Before the price reveal.
- Directly before the CTA.

Slots: "Can you see how [feature] would save you [time or cost]?" / "Would [outcome] matter to your business this quarter?" / "Is that worth [price] to you?"

Procedure: write 20 to 30 varied closes on cards; place several after every testimonial; measure revenue per lead or per registrant before and after. Keep them honest and unpushy; if the audience finds them formulaic, reduce frequency.

## Sources

- Brunson, R. (2013) *108 Proven Split Test Winners*, DotComSecrets Labs: informed the hypothesis areas (headlines, CTAs, forms, trust, pricing, layout); no figures or cases are reproduced here.
- Cialdini, R. (2007) *Influence*, Collins; Nahai, N. (2012) *Webs of Influence*, Pearson: informed the commitment-and-consistency rationale for trial closes.
