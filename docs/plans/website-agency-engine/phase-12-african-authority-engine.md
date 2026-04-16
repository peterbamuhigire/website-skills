# Phase 12 - African Authority Engine

## Objective

Convert the now-enforced, now-disciplined engine into the recognised standard for premium
web design practice in Africa. Install the Africa-specific excellence layer the market
actually rewards, publish open-source benchmark sites and case studies that establish
authority in public, run an operator certification network, and contribute back to the
open-source ecosystem the engine depends on.

This is the phase that turns "world-class agency engine" from an internal property into
a continental reputation.

## Why This Phase Matters

The earlier phases produce excellence. This phase produces authority. The two are not
the same. Excellent agencies that do not publish, benchmark, or certify get hired by
the same clients forever and never reach the position of category leader.

For an Africa-based agency targeting premium positioning, two specific properties matter
that generic global agency frameworks ignore:

1. **Africa-realistic excellence** - the system must be visibly excellent on the
   bandwidth, devices, languages, payment systems, and trust contexts that African
   buyers and users actually live in. A Lighthouse score of 95 on a Stockholm fibre
   connection is irrelevant to a buyer whose customers shop on a 3G phone in Kampala.
2. **Public continental authority** - African studios buy from people they have read,
   seen speak, and seen ship. Authority compounds when the standards are open and the
   work is referenceable. Without published benchmarks, the agency competes on price
   with every freelancer in the LinkedIn search.

The 2026-04-12 evaluation does not name this phase explicitly because the evaluation is
internal. The market test is external. This phase passes the external test.

## Core Outcomes

- an Africa Excellence Layer that codifies low-bandwidth, mobile-money, multilingual,
  USSD-aware, and country-trust patterns as first-class skills
- a published open-source benchmark library: at least three reference sites covering
  different sectors and country contexts, public and indexed
- a published case-study corpus with at least eight real client outcomes
- a public quality scorecard updated quarterly
- an operator certification network with a published syllabus, exam, and inaugural cohort
- a knowledge commons: open or partially open licence on skills and references, public
  changelog, and at least one upstream open-source contribution
- a continental presence: at least one conference talk delivered, hosted, or invited

## Workstreams

### 1. Africa Excellence Layer

Codify the Africa-realistic patterns the engine already expects, but does not yet hold
as a single first-class skill.

Required scope:

- a new top-level `africa-excellence/SKILL.md` skill that owns the standards below
- low-bandwidth pattern reference at `africa-excellence/references/low-bandwidth-patterns.md`
  covering:
  - 3G and 4G as primary test connections (per the Phase 10 gate)
  - aggressive image compression beyond global defaults (AVIF first, WebP fallback,
    JPEG only when forced)
  - critical CSS inline; everything else lazy
  - font subsetting per language
  - no autoplay video; no preload of non-critical assets
  - service worker for offline-first content where it materially helps
  - data-saver mode detection (`Save-Data` header)
- mobile money UX reference at `africa-excellence/references/mobile-money-ux.md` covering:
  - M-Pesa (Kenya, Tanzania), MTN MoMo (Uganda, Rwanda, Ghana, Cameroon), Airtel Money
    (multi-country), Orange Money (West Africa, Cameroon), Wave (Senegal, Côte d'Ivoire),
    Flutterwave and Paystack (Nigeria-led, multi-country)
  - the STK push pattern, the USSD prompt pattern, the manual-paybill pattern
  - reconciliation, retry, and failure UX
  - currency formatting (UGX, KES, NGN, GHS, ZAR, RWF, TZS, XOF, XAF) without leading
    zero ambiguity
- USSD-aware design reference at `africa-excellence/references/ussd-aware-design.md`:
  when a feature must be reachable from a feature phone, design the web counterpart so
  it parallels and respects the USSD flow
- multilingual depth reference at `africa-excellence/references/african-language-pack.md`
  covering: English, French, Kiswahili, Luganda, Amharic, Yoruba, Hausa, Zulu, Twi,
  Wolof; including font support, expansion ratios, and RTL rules where they apply
  (Arabic for North Africa, Tifinagh for North-African Berber clients)
- country-trust-signals reference at `africa-excellence/references/africa-trust-signals.md`
  covering, per market: regulator badges, association memberships, payment provider
  badges, local certifications, name-display conventions, photo conventions, and
  case-study conventions
- cultural pattern reference at `africa-excellence/references/cultural-patterns.md`
  covering: hierarchy of testimonials (community before individual in many markets),
  family and community framing in conversion copy, photography conventions, and the
  difference between markets that respond to formality and markets that respond to warmth

Output: every shipped site is built and reviewed against this skill, not against generic
global defaults.

### 2. Open-Source Benchmark Library

Make the agency's standards visible by shipping reference sites under an open licence.

Required scope:

- at least three open-source benchmark sites covering different sectors and country
  contexts, for example:
  - a Ugandan SME services site
  - a Kenyan B2B technology site
  - a Nigerian fintech or healthtech site
- each benchmark site must:
  - pass every Phase 10 gate
  - meet every Africa Excellence Layer rule
  - score at least 9/10 on the design-quality rubric
  - include a published "how this site was built" walkthrough
  - be public, indexed, and licenced (Creative Commons content, MIT or Apache code)
- benchmark sites are republished or audited annually
- a public landing index lists every benchmark with its scorecard

Output: a sector studio anywhere in Africa can read, fork, and learn from work that
demonstrably meets the engine's standards.

### 3. Case-Study Corpus and Public Scorecard

Convert the Phase 7 case-study system into a public, continually-published authority asset.

Required scope:

- at least eight published case studies using the Phase 7 template, covering:
  - measurable client outcomes (revenue, leads, conversion, traffic)
  - the Africa-realistic constraints the project worked under
  - the gates and standards the project met
  - the experimentation results (where applicable, per Phase 11)
- a public quarterly scorecard at `dashboards/public-scorecard.md`:
  - aggregate Lighthouse, accessibility, and design-quality scores across all live
    client sites
  - aggregate uptime and incident metrics
  - aggregate experimentation outcomes
  - retention and expansion behaviour at the cohort level (anonymised)
- a published changelog of every material change to the engine
- the agency website itself is rebuilt to demonstrate the engine; it carries the same
  scorecard and the same standards as client work

Output: any prospective client or operator can see the actual outputs, the actual
methods, and the actual measured outcomes before making a decision.

### 4. Operator Certification Network

Take the Phase 11 certification programme and grow it into a network of certified
operators that the agency can hire from, partner with, and recommend.

Required scope:

- at least two cohorts run within 12 months of phase start
- a public certified-operators list (with consent) so clients can verify status
- a partnership tier for certified studios and freelancers in adjacent African markets
  who want to use the engine without joining the agency
- a recertification cycle of 12 months with a refreshed exam reflecting the latest
  engine state
- a published code of conduct and quality contract for certified operators
- a feedback loop: every certified operator submits a structured "engine feedback"
  document at recertification time that informs the next quarterly skill update

Output: when a client hires a certified operator, the agency's quality contract travels
with the operator.

### 5. Knowledge Commons and Upstream Contribution

Establish the engine as a contributor to, not just a consumer of, the open-source
ecosystem it depends on.

Required scope:

- a public licence on the open parts of the repository (MIT for code, CC BY for content
  is a sensible default; the agency must choose explicitly)
- a published "what is open and what is closed" matrix at `docs/licensing-matrix.md`
- at least one substantive upstream contribution per year to a project the engine
  depends on (Astro, Tailwind CSS, axe-core, Playwright, Lighthouse CI, GrowthBook,
  Sharp, or equivalent)
- a public roadmap (curated subset of this plan) at `docs/roadmap-public.md` so the
  community can see where the engine is going
- at least one published research note per year on an Africa-specific web design topic
  (low-bandwidth performance, mobile money UX, multilingual design at scale)

Output: the engine is visibly part of the global open-source web ecosystem on Africa-
specific terms.

### 6. Continental Presence

Make the agency's authority audible in the African design and developer community.

Required scope:

- at least one conference talk delivered or hosted within 12 months of phase start at
  a venue such as DevFest (Africa-wide), DroidConKE, PyCon Africa, ForLoop Africa,
  Africa Tech Summit, or a sector conference (UN-Habitat, AfricaCom, etc.)
- a hosted event option: a one-day workshop or a small invite-only summit where the
  engine, the certification programme, and the benchmark library are presented
- a publishing rhythm tied to Phase 7's editorial calendar:
  - one cornerstone authority piece per quarter on an Africa-specific topic
  - one open data point or benchmark release per quarter
  - one community guest contribution accepted per quarter
- relationships with at least three African design or developer media outlets
  (TechCabal, TechPoint Africa, WeeTracker, Disrupt Africa, Smashing Magazine for
  African contributors)

Output: the agency name appears in the same sentence as the standard it set.

## Repository Outputs Required

- `africa-excellence/SKILL.md` and the six supporting references named above
- `dashboards/public-scorecard.md` regenerated quarterly
- `docs/licensing-matrix.md` and the chosen open-source licence text
- `docs/roadmap-public.md`
- benchmark site repositories (separate Git repos, linked from this plan)
- case-study corpus published on the agency site and indexed
- certification cohort records under `certification/cohort-2026-XX.md`
- a new entry in `project-log/decisions/` per workstream
- update to `agency-positioning/SKILL.md` to reference the public scorecard, benchmark
  library, and certification network as part of premium positioning
- update to `they-ask-you-answer/SKILL.md` to integrate the publishing rhythm with the
  conference and media outreach plan

## Success Criteria

- A re-run of the `docs/evaluation/` framework moves the overall score to >= 9.5.
- At least three open-source benchmark sites are public, indexed, and pass every gate.
- At least eight case studies are published with measurable outcomes.
- The public scorecard is updated quarterly without operator narration.
- The certification programme has at least two cohorts within 12 months of phase start.
- At least one upstream open-source contribution per year is in evidence.
- At least one conference talk has been delivered or hosted.
- At least 12 African client projects have been shipped on the world-class engine
  within 12 months of phase completion.
- The agency is mentioned by at least one independent African design or developer
  publication as a reference for premium web design practice.

## Risks to Avoid

- Publishing benchmarks that do not actually pass the Phase 10 gates. The benchmark
  library is the highest-stakes asset; one weak benchmark damages credibility more
  than ten missing ones.
- Treating certification as a marketing badge. If it is not hard to earn, it is not
  worth holding.
- Letting the public scorecard become curated. The point is honest aggregate data; if
  bad numbers appear, fix the underlying work.
- Importing global frameworks unmodified into the Africa Excellence Layer. The point
  of this phase is that global defaults are not enough.
- Conference performance over substance. One talk that demonstrates the actual scorecard
  beats five talks that recycle generic agency theory.
- Closing the knowledge commons. Authority compounds when standards are public; closed
  systems compete on sales rather than on demonstrated quality.

## Reading Material To Buy And Provide At This Stage

- *Show Your Work!* by Austin Kleon: the operating philosophy of public knowledge
  commons. Required pre-reading for workstreams 2, 5, and 6.
- *Built to Sell* by John Warrillow: the operating philosophy of building an agency
  that does not depend on the founder, applied here to authority rather than only to
  delivery.
- *Authority* by Nathan Barry: the practical mechanics of publishing into authority
  in a niche.
- *The Brand Gap* by Marty Neumeier: the strategic frame for category leadership.
- *Made to Stick* by Chip Heath and Dan Heath: the framework for case-study writing
  that travels.
- *They Ask, You Answer* by Marcus Sheridan (re-read in the Phase 12 context): the
  publishing-as-trust frame applied to a continental rather than local market.
- *Africa's Business Revolution* by Acha Leke, Mutsa Chironga, and Georges Desvaux
  (McKinsey): market context for African premium positioning.
- *The Mobile Frontier* by Rachel Hinman: mobile-first thinking grounded in real
  global mobile constraints rather than US-fibre defaults.
- *Inclusive Design Patterns* by Heydon Pickering: re-read in the African multilingual
  and assistive-tech context.
- *Designing Across Cultures* (collected practitioner essays from Smashing Magazine
  and A List Apart): cross-cultural design literacy for the cultural-patterns reference.
- Academic and industry papers on M-Pesa UX (Mendoza-Denton et al., GSMA reports):
  primary-source grounding for the mobile money UX reference. Source via Google Scholar
  and the GSMA Mobile Money programme publications.
