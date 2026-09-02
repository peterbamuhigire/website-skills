---
name: language-standards
description: Use when a multilingual website needs cross-language tone, terminology, locale ownership, and consistency rules; use `french-native-copy`, `swahili-native-copy`, or `east-african-english` for language-specific execution.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Language Standards
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Govern meaning and tone across English, French, and Kiswahili while routing native writing to the language-specific skill.

## Target Audiences (Standard)

Every multilingual output from this engine targets these audiences. Do not deviate unless the project brief explicitly names different markets.

| Locale | Primary Markets | Secondary Markets | Reader Profile | Register |
|--------|----------------|-------------------|----------------|----------|
| **English** | East Africa (Uganda, Kenya, Tanzania, Rwanda) | All English-speaking Africa and global English speakers | Advanced comprehension; educated professionals reading fluently in English (often L2/L3) | British-influenced East African professional English; clear, direct, respectful; globally readable |
| **French** | DRC, Congo-Brazzaville, Burundi, Senegal, Mali, Côte d'Ivoire, Togo, Cameroon, Gabon, Madagascar | All francophone Africa (Bénin, Burkina Faso, Niger, Guinea, Djibouti, Comoros, Chad, Central African Republic) | Advanced comprehension; educated professionals reading fluently in French (often L2/L3) | Formal vous; francophone African professional French; never France-centric, never Québécois |
| **Kiswahili** | Kenya, Tanzania, DR Congo | Uganda (limited), Rwanda, Burundi, Mozambique (Kiswahili speakers) | Advanced comprehension; educated professionals reading standard Kiswahili | Respectful Kiswahili sanifu; no slang, no Sheng, no regional dialect drift |

### Rules
1. **English must be globally readable.** An English speaker in London, Lagos, or Nairobi must understand every sentence. Use East African warmth and courtesy but avoid local slang or references only Ugandans would understand.
2. **French targets francophone Africa, not France.** Reference OHADA, BCEAO/BEAC, FCFA, and institutions relevant across West and Central Africa. Never assume the reader is in Paris.
3. **Kiswahili targets Kenya and Tanzania first.** DR Congo is the secondary growth market. Uganda has limited Kiswahili readership — do not assume Ugandan readers for Swahili content.
4. **Advanced reader assumption.** Do not simplify vocabulary, over-explain concepts, or use patronising language. The audience reads at an advanced level in their chosen language.
5. **No raw translation.** Each language is authored from meaning. The French and Kiswahili outputs must read as if originally written in that language by a professional from the target market.

<!-- dual-compat-start -->
## Use When

- A site needs a language policy, terminology register, or cross-language review.
- English, French, and Kiswahili versions must communicate the same offer without literal translation.
- Teams need to decide which content is shared and which is locale-specific.

## Do Not Use When

- The task is native French, Kiswahili, or East African English writing; use the relevant execution skill.
- The task is URL routing, hreflang, sitemap, or locale architecture; use `i18n`.
- Only one sentence in one language needs routine editing and no cross-language decision is involved.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Approved source meaning and business facts | Content owner | yes | Stop comparison and identify the missing source of truth. |
| Locale list, market, and audience per language | Project or research brief | yes | Do not assume France equals francophone Africa or that one Kiswahili register fits every market. |
| Brand voice and terminology | Brand owner | conditional | Create a provisional register and flag it for approval. |
| Existing locale copy | Project files | conditional | Produce policy and handoff rules rather than a completed consistency audit. |

## Workflow

1. Name each locale, target market, audience, and native-copy owner.
2. Establish the source-of-truth meaning, facts, offer, proof, and CTA.
3. Classify fields as shared, locale-adapted, or locale-specific using [multilingual rules](references/multilingual.md).
4. Build a terminology register for brand names, services, regulated terms, dates, numbers, and currencies.
5. Route execution to the matching native-copy skill; do not raw-translate the English structure.
6. Compare versions for meaning, claim strength, omissions, CTA commitment, and tone rather than sentence symmetry.
7. Stop and resolve any legal, commercial, or factual mismatch before release.
8. If a native reviewer or locale evidence is unavailable, mark that locale provisional and return the exact review needed.

Recovery: repair the source meaning or locale decision, then rerun the parity review across all affected languages.

## Quality Standards

- Every locale has a named market and language owner.
- Facts, prices, dates, claim strength, and offer boundaries remain consistent unless localisation is approved.
- Register and terminology remain consistent within each locale.
- French and Kiswahili are authored natively rather than produced by raw translation.
- Cross-language review records intentional differences and unresolved issues.

## Anti-Patterns

- Treating English as a sentence-by-sentence template. Fix: preserve meaning while allowing native structure.
- Using one generic "French" market. Fix: name the francophone audience and conventions.
- Mixing Kenyan and Tanzanian Kiswahili choices without a decision. Fix: set the market and register.
- Translating brand or regulated terms inconsistently. Fix: maintain an approved terminology register.
- Declaring parity because paragraph counts match. Fix: compare claims, proof, actions, and omissions.
- Silently weakening or strengthening a claim in one locale. Fix: record and approve the variation.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Language policy | Content, design, and implementation teams | Locales, markets, ownership, source language, and adaptation rules are explicit. |
| Terminology register | Native writers and reviewers | Each controlled term has approved forms and prohibited or unresolved variants. |
| Cross-language consistency review | Release owner | Material mismatches and intentional differences are recorded by locale. |

## References

- [Multilingual rules](references/multilingual.md) for shared and locale-specific policy.
- [Advanced business English](references/business-english-advanced.md) for professional English decisions.
- [Legacy detailed guidance](references/legacy-guidance.md) for preserved tone and terminology conventions.
<!-- dual-compat-end -->

## Human-English overlay

Load [`human-english-craft-synthesis-2026.md`](../../../book-extractions/human-english-craft-synthesis-2026.md) for English copy, headings, CTAs, and microcopy. Apply its reader/purpose, genre/spine, evidence, sentence, and proof passes. Preserve correct regional usage; do not make copy sound “human” through errors, forced slang, or fake warmth.

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Locale decision register | Table | Market, register, owner, and approval status exist for every locale. |
| Parity review | Checklist or issue list | Claims, facts, proof, CTAs, and missing content were compared. |

## Capability Contract

Read access to all compared locale content is required. Review defaults to read-only. Editing requires explicit authority and native execution through the relevant skill. Network research is optional; publication and routing changes require separate authority.

## Degraded Mode

If a locale, native reviewer, or market evidence is unavailable, assess only the accessible meaning and structure, mark native quality `not assessed`, and provide the smallest review brief. Never count an unreviewed locale as passed.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Meaning is universal but expression differs | Adapt natively | Translation artefacts |
| Offer, law, currency, or convention differs | Create locale-specific content | Materially wrong local copy |
| No native quality evidence | Mark provisional and require review | False certification |
| URL or hreflang issue dominates | Hand off to `i18n` | Mixing content governance with routing |

## Worked Example

An English CTA says "Book a consultation". The French and Kiswahili writers may choose different natural verbs, but the review confirms that all three promise the same meeting type, qualification step, and response expectation.

## Read Next

- `french-native-copy` for French execution.
- `swahili-native-copy` for Kiswahili execution.
- `east-african-english` for regional English execution.
- `i18n` for technical locale architecture.
## English collocation and lexical-precision overlay

Load [`english-collocations-and-lexical-precision-2026-09-02.md`](references/english-collocations-and-lexical-precision-2026-09-02.md) alongside this standard. It strengthens exact word choice, natural collocations, register, idiom restraint, grammar, and human-quality revision.
