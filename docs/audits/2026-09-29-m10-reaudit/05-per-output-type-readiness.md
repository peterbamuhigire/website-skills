# Per-output-type readiness

All scores judged. Bar: a premium agency deliverable a discerning client would
accept without rework. Rendered, field and conversion outcomes are
`NOT_ASSESSED` for every type; no type has a complete worked deliverable in the
repository.

## Ranked table

| Rank | Output type | Score | Owning skills |
|---:|---|---:|---|
| 1 | Marketing / company website | 60 | website-builder, premium-website-product, page-builder, design-system, seo, deploy, the gates |
| 2 | Blog | 58 | blog-writer, blog-idea-generator, premium-commercial-writing, seo |
| 3 | Client intake brief | 57 | website-builder references (intake questionnaire, strategy brief), premium-sales-conversation |
| 4 | Deployment / hand-over pack | 56 | deploy, website-builder (asset ownership register), observability |
| 5 | Landing page | 55 | page-builder, long-form-sales-copy, sales-copywriting, launch-campaigns, cro-audit |
| 5 | Performance and SEO audit reports | 55 | seo-audit, deploy (legacy-site-performance-audit, lab-to-field), cro-audit |
| 7 | Multilingual / African-language site | 52 | i18n, language-standards, french-native-copy, swahili-native-copy, east-african-english, africa-excellence |
| 8 | E-commerce-lite / catalogue | 45 | ecommerce, ecommerce-checkout, ecommerce-funnel, ecommerce-analytics, retail-commerce-operating-system |

**Output-type readiness (mean): 54.75, reported as 55.**

## Detail

### Marketing / company website — 60
Strongest path: a ten-gate build contract in `website-builder`, a 15-step CI
template, the slop-scan gate, a fixture benchmark that passes. Gaps: the only
fixture sites are two-page lab fixtures (`fixtures/website-kaizen`,
`website-basic`); `examples/service-page-journey` is a single page; no retained
render evidence. Lift: one complete reference site with render, a11y and
performance reports committed as a worked example.

### Blog — 58
Three-wave research requirement and claim-and-source map are above typical
practice. Gaps: no sample article with its source register; the new-tab rule for
internal links is contestable; the research dependency means degraded mode
leaves only a narrow draft. Lift: a worked article plus its source register and
publishing hand-off.

### Client intake brief — 57
A 255-line intake questionnaire, a 213-line strategy brief template, an owner
decision register and `PROJECT.md` handling. Gaps: no intake skill (routes to the
orchestrator); no filled example brief; no routing fixture for an intake-only
request. Lift: a thin `client-intake` skill or a declared route with fixtures,
plus a completed example brief.

### Deployment / hand-over pack — 56
`deploy` is among the deepest skills (release decision record, rollback
preconditions, 7- and 30-day reviews). Gaps: the hand-over pack is described in
several places but has no single template; no sample release evidence bundle;
live deployment and rollback `NOT_ASSESSED`. Lift: `templates/handover-pack.md`
and a worked evidence bundle from a fixture deploy.

### Landing page — 55
Copy depth is good (long-form, direct-response, channel-to-site hand-off
receiving). Gaps: no landing-page owner; message-match and single-goal rules are
spread across four skills; no worked page. Lift: a landing-page reference under
`page-builder` with a worked example and fixtures.

### Performance and SEO audit reports — 55
`seo-audit` defines a findings register with evidence, impact, confidence and
retest; `legacy-site-performance-audit.md` and lab-to-field calibration exist;
the Africa stress profile is labelled a floor, not a median. Gaps: no sample
report; field Core Web Vitals `NOT_ASSESSED`; the 3G profile's market figures are
partly `NOT_ASSESSED` per the engine's own register. Lift: a worked audit report
against a fixture site.

### Multilingual / African-language site — 52
`i18n` enforces one route-equivalence map for switcher, canonical, hreflang and
sitemap; French and Kiswahili native-copy skills are deep; bilingual identity
fixtures exist. Gaps: the language pack declares ten first-class African
languages (Luganda, Amharic, Yoruba, Hausa, Zulu, Twi, Wolof, Arabic, Tifinagh
besides Kiswahili) with fonts and expansion ratios but no native-copy route or
review procedure; speaker counts are unsourced; RTL is handled only in the pack.
Lift: either add native-copy routes (Luganda first for the home market) or
reclassify those languages as "layout-supported, copy not assessed".

### E-commerce-lite / catalogue — 45
Commerce skills are sound on strategy and truthful urgency, but assume a store
with checkout, OMS or POS. Gaps: nothing for a static catalogue with enquiry,
WhatsApp or mobile-money ordering; `retail-commerce-operating-system` has no
references; `fixtures/website-commerce` is a single JSON file. Lift: a
`catalogue-lite` skill with product schema, price-truth rules, ordering
hand-off patterns and a worked catalogue.
