---
name: africa-excellence
description: Use when a website must work credibly in African markets across constrained bandwidth, mobile-first use, mobile money, USSD-aware journeys, local languages, trust, and cultural context; use deploy for release execution.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Africa Excellence
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Apply Africa-realistic product and delivery constraints without flattening diverse markets into stereotypes.

<!-- dual-compat-start -->
## Use When

- Users face expensive or unstable data
- mobile money or USSD shapes conversion
- local trust, address, language, or device conditions affect the experience.

## Do Not Use When

- Use as a substitute for country and audience research, or for deployment execution owned by `deploy`.

## Required Inputs

| Artefact | Source or provider | Required? | Purpose | If absent |
|---|---|---:|---|---|
| Target countries, audience evidence, device and network profile, payment channels, language plan, and trust requirements | Research, analytics, client operations, and project brief | yes | Calibrate patterns to a real market | Stop when the market is described only as 'Africa' without country evidence |

## Workflow

1. Name countries, audiences, evidence, and constraints
2. Choose bandwidth, device, payment, language, trust, and offline-continuity patterns
3. Integrate requirements into content, design, commerce, and measurement
4. Stop on stereotype or unverified infrastructure claims, recover through research or qualified assumptions, then test on the agreed constrained profile.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Africa excellence requirements and acceptance matrix | Website-builder, design-system, commerce, and deploy | Each market constraint maps to an implementation owner and observable test |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Country evidence register and constrained-profile results | Product and release owners | Sources are locatable and unavailable tests are marked `not assessed` |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required. Planning is read-only by default; implementation and network tests require authority. Live payments, USSD sessions, user contact, spending, and publication require explicit permission.

## Degraded Mode

Without device, network, payment, or country evidence, return the narrowest qualified risk matrix, mark those checks `not assessed`, and do not generalise a pass across Africa.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Save-Data or constrained 3G is material | Serve a lighter media and motion path | Exclusion through data cost |
| Mobile money is a primary payment rail | Design explicit pending, failed, reversed, and receipt states | Payment ambiguity |

## Quality Standards

- Name the market and evidence; meet the repository's Africa-calibrated performance budget; support payment, language, trust, and recovery states relevant to the chosen country.

## Anti-Patterns

- Treating Africa as one market. Fix: name countries, segments, and evidence.
- Adding flags and patterns as cultural localisation. Fix: adapt language, trust, payment, and service reality.
- Assuming continuous broadband. Fix: test constrained profiles and Save-Data behaviour.
- Showing mobile-money success only. Fix: cover pending, failed, reversed, duplicate, and receipt states.
- Certifying a country without local evidence. Fix: mark it unassessed and commission research or testing.

## Worked Example

For Uganda, test the 350 KB target on the agreed 3G profile, expose MTN MoMo and Airtel Money pending/reversal states, and label any untested USSD handoff rather than claiming nationwide readiness.

## References

- [Website Skills authoring standard](../../../docs/skill-authoring-standard.md)


## Preserved Domain Use Guidance
- Any project for an African client, regardless of which African market.
- Any project whose primary audience uses African mobile-money rails,
  3G networks, African languages, or lives in an African trust
  ecosystem.
- When reviewing a built site against Africa-calibrated standards before
  launch.
- When auditing a site that was built against global defaults and needs
  an Africa-specific upgrade.

## Preserved Domain Exclusions
- The project's primary audience is not in an African market and will
  not encounter African mobile-money, USSD, or language contexts. Use
  sector-strategies and design-system defaults instead.
- Working on infrastructure that is shared globally and Africa
  calibration is already applied (the Phase 10 3G performance profile
  is an example — that is owned by `deploy/references/africa-calibration.md`
  and does not need duplication here).

## Core contract

Every site in scope is built and reviewed against six standards owned
by this skill:

1. **Low-bandwidth performance** — beyond the global defaults; AVIF
   first, font-subsetting per language, aggressive critical-CSS,
   Save-Data honouring. See `references/low-bandwidth-patterns.md`.
2. **Mobile-money UX** — if the site takes money, it meets the regional
   mobile-money provider patterns (M-Pesa, MoMo, Airtel Money, Orange
   Money, Wave, Flutterwave, Paystack) and formats currency without
   ambiguity. See `references/mobile-money-ux.md`.
3. **USSD-aware design** — where a feature has a USSD counterpart for
   feature-phone users, the web flow parallels and respects the USSD
   flow. See `references/ussd-aware-design.md`.
4. **Multilingual depth** — beyond "English + French"; Kiswahili,
   Luganda, Amharic, Yoruba, Hausa, Zulu, Twi, Wolof, Arabic, and
   Tifinagh are treated as first-class when the market requires. See
   `references/african-language-pack.md`.
5. **Country-specific trust signals** — regulator badges, association
   memberships, payment provider badges, and local certifications per
   market. See `references/africa-trust-signals.md`.
6. **Cultural patterns** — hierarchy of testimonials, family/community
   framing, photography conventions, and market-specific formality vs
   warmth. See `references/cultural-patterns.md`.

## Preserved Domain Workflow
1. **Classify the market.** Identify the primary country and any
   secondary markets. Record in the strategy brief.
2. **Apply the six standards** to the design-system, page-build, SEO,
   and deploy work. Each reference states how the standard flows into
   the respective build skill.
3. **Review against references** at visual-QA and design-quality-score
   time. The rubric's category 6 (trust-signal placement) and category
   7 (section originality) take their Africa-specific instantiation
   from this skill.
4. **Verify at launch** on a real throttled 3G device or emulated
   profile in at least one African market on a local mobile-money
   provider rail (where payments are in scope).
5. **Document variance.** Where a client requires deviation from an
   Africa-excellence pattern (e.g. a global SaaS targeting African
   enterprise buyers who use cards, not mobile money), record the
   deviation in a decision entry.

## Preserved Domain Inputs
- Primary and secondary African markets.
- Payment rails in scope.
- Primary and secondary languages.
- Feature-phone relevance (does a USSD counterpart exist?).
- Client's sector and regulatory posture.

## Preserved Domain Quality Guidance
- 3G-throttled profile loads the primary route under the 350 KB budget
  and LCP ≤ 2.5 s. The Phase 10 performance gate enforces this; this
  skill raises the bar where the gate permits.
- AVIF is the first image format; WebP the fallback; JPEG only when
  forced.
- Critical CSS is inlined; all other CSS is lazy.
- Fonts are subsetted per language actually shipped on the site.
- Currency formatting uses the ISO-4217 code (UGX, KES, NGN, GHS, ZAR,
  RWF, TZS, XOF, XAF) with no leading-zero ambiguity.
- Mobile-money UX surfaces provider choice before payment prompt and
  handles STK push, USSD prompt, and manual paybill flows distinctly.
- Trust badges are real and current; regulator badges link to the
  regulator.
- Testimonials prefer community framing where the market responds to
  community over individual testimony.

## Preserved Domain Anti-Patterns
- Using global SaaS visual defaults (purple-to-blue gradient,
  diverse-office-stock photos) for African clients. These fail the
  design-quality rubric's originality category.
- Shipping a mobile-money-enabled flow that only covers one provider
  when the market has several large providers.
- Assuming "English" is sufficient language coverage in markets where
  the buyer or end-user primarily operates in another language at home
  or at work.
- Ignoring feature-phone users in markets where smartphone penetration
  is < 70%. The site may not reach them, but the flow should not break
  when a feature-phone user is on the call with a smartphone user.
- Copy-pasting a Kenyan-market site into a Ugandan-market site without
  revisiting trust signals and currency.
- Applying a Lagos cultural-tone template to a Kampala build or vice
  versa without verification.

## Preserved Domain Outputs
- Every primary template reviewed against the six references before
  launch.
- A recorded Africa-excellence audit line in the project's launch log.
- A decision entry for any deviation from the references.
- Inputs to the design-quality-score rubric categories 6 and 7
  (trust-signal placement, section originality) that reflect the
  market.

## Preserved Domain References
- `references/low-bandwidth-patterns.md` — performance patterns beyond
  the global defaults.
- `references/mobile-money-ux.md` — regional mobile-money providers,
  STK push / USSD / manual flows, reconciliation UX, currency
  formatting.
- `references/ussd-aware-design.md` — when and how the web flow must
  respect a USSD counterpart.
- `references/african-language-pack.md` — the 10 first-class African
  languages: font support, expansion ratios, RTL rules.
- `references/africa-trust-signals.md` — regulator, association,
  payment-provider, and cultural trust signals per market.
- `references/cultural-patterns.md` — testimony hierarchy, photography
  conventions, formality vs warmth by market.

## Notes

- This skill composes with `sector-strategies` (sector rules) and
  `design-system` (visual tokens), not instead of them. Global defaults
  still apply; this skill adds and sometimes overrides.
- The Phase 10 performance gate and this skill share a heritage but
  have different scopes: the gate enforces a numeric threshold; this
  skill defines pattern practice.
- The benchmark library (Phase 12) will include at least one site per
  major African sub-region against this skill.
