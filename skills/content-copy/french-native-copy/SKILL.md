---
name: french-native-copy
description: Use when French web, marketing, product, email, or metadata copy must read as native for a named francophone market; use `language-standards` for cross-language policy and `i18n` for routing.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# French Native Copy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Author French from meaning rather than English syntax, with a deliberate market, register, terminology, and typography decision.

## Target Markets (Standard)

French content from this engine targets **francophone Africa**, not France. The primary markets are:

**Central Africa:** DRC, Congo-Brazzaville, Cameroon, Gabon, Central African Republic, Chad, Equatorial Guinea
**West Africa:** Senegal, Mali, Côte d'Ivoire, Togo, Benin, Burkina Faso, Niger, Guinea, Guinea-Bissau, Mauritania
**Indian Ocean:** Madagascar, Djibouti, Comoros
**East Africa:** Burundi, Rwanda (francophone communities)

The reader is an educated professional with advanced French comprehension, often reading French as L2 or L3 alongside local languages. They understand formal business French and expect professional register.

**Never assume the reader is in France.** Reference OHADA, BCEAO/BEAC, FCFA, and institutions relevant across francophone Africa. Use vocabulary understood across West and Central Africa — not France-specific, not Québécois, not Belgian.

<!-- dual-compat-start -->
## Use When

- Writing or revising any French page, CTA, microcopy, email, or metadata.
- Adapting approved source meaning into native French rather than literal translation.
- Reviewing French for register, idiom, grammar, typography, or search phrasing.

## Do Not Use When

- The task is locale routing, hreflang, slugs, or sitemap structure; use `i18n`.
- The task is cross-language parity or shared terminology policy; use `language-standards`.
- The copy is English or Kiswahili; use the matching native-language skill.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Approved meaning, facts, and offer | Source copy, brief, or client notes | yes | Stop translation and request the missing source of truth. |
| Francophone market and audience | Project brief | yes | Use neutral professional French provisionally and flag localisation unresolved. |
| Register decision: `vous` or `tu` | Brand owner | conditional | Default to `vous` for commerce and services and record the assumption. |
| Page goal, proof, SEO target, and constraints | Content/SEO owner | conditional | Preserve meaning; mark conversion and search choices provisional. |

## Workflow

1. Fix the target market, audience, and `vous`/`tu` register using [register and address](references/register-and-address.md).
2. Stop if regulated, commercial, or factual source meaning is ambiguous.
3. Write from intended meaning, then compare against the source facts; avoid word-for-word calques using [anglicisms to avoid](references/anglicisms-to-avoid.md).
4. Audit agreement, articles, negation, pronouns, prepositions, tense, and mood with [grammar pitfalls](references/grammar-pitfalls.md).
5. Improve collocations, connectors, CTA verbs, and rhythm using [idiom and flow](references/idiom-and-flow.md).
6. Apply French punctuation, spacing, guillemets, dates, numbers, currency, and capitalisation from [typography and formatting](references/typography-and-formatting.md).
7. Research search phrasing natively when network access and SEO scope allow; do not transpose English keywords.
8. Run [the revision checklist](references/revision-checklist.md), including meaning comparison and register consistency.
9. If native verification is unavailable, mark native quality `not assessed` and return a focused review brief.

Recovery: repair meaning, register, or grammar findings, then rerun the native-copy checklist.

## Quality Standards

- A French reader encounters no English word order, calque, or punctuation convention.
- Address and register remain consistent across verbs, pronouns, possessives, and CTA language.
- Grammar and agreement are correct throughout.
- Numbers, dates, currency, and typography match the named market.
- Search terms are researched in French when SEO claims are made.
- Back-comparison preserves every material fact, limitation, and next step.

## Anti-Patterns

- Lightly editing machine translation. Fix: rewrite from meaning.
- Mixing `tu` and `vous`. Fix: record one register and audit every address form.
- Using calques such as a literal English CTA. Fix: choose an idiomatic French action verb.
- Applying France-only conventions to francophone Africa without a market decision. Fix: name and research the audience.
- Keeping English punctuation, number, or currency formatting. Fix: apply the locale convention.
- Transposing English keywords. Fix: research how French speakers express the intent.
- Certifying native quality without a competent review. Fix: mark it `not assessed` and request review.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Native French copy | Page, campaign, or product owner | Meaning, register, grammar, idiom, and typography pass the checklist. |
| Register and market note | Future writers | Market, audience, `tu`/`vous`, and terminology decisions are recorded. |
| Review findings | Author or approver | Each issue shows the original, correction, reason, and severity. |

## References

- [Register and address](references/register-and-address.md)
- [Grammar pitfalls](references/grammar-pitfalls.md)
- [Vocabulary by theme](references/vocabulary-by-theme.md)
- [Idiom and flow](references/idiom-and-flow.md)
- [Anglicisms to avoid](references/anglicisms-to-avoid.md)
- [Typography and formatting](references/typography-and-formatting.md)
- [Revision checklist](references/revision-checklist.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Locale and register record | Short note | Market, audience, register, and provisional choices are explicit. |
| Native-copy review | Checklist or issue table | Meaning, concord, idiom, typography, and unassessed checks are visible. |

## Capability Contract

Read access to source meaning and French copy is required. Review defaults to read-only; editing requires explicit authority. Network access may verify current market and search usage. Native-speaker review cannot be claimed unless it occurred.

## Degraded Mode

Without market context, network research, fonts/rendering, or a competent native review, return neutral provisional French and name each unassessed dimension. Never turn unavailable native or visual verification into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Professional commerce with no register choice | Use `vous` provisionally | Accidental over-familiarity |
| Youth or peer brand with approved voice | Use `tu` consistently | Register drift |
| Market convention differs | Localise terminology and formats | France-centric copy |
| Meaning or regulated claim is ambiguous | Stop and clarify | Material mistranslation |

## Worked Example

Source intent: invite a Dakar business owner to request an initial assessment, not promise a free consultation. The French CTA reflects that qualification step, uses `vous`, and records Senegal as the market; it does not copy the English button word for word.

## Read Next

- `language-standards` for cross-language parity.
- `i18n` for technical locale routing.
- `premium-commercial-writing` for premium commercial editorial quality.
