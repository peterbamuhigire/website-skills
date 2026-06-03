---
name: french-native-copy
description: Native-quality French copywriting standard for the website engine. Produces French web, marketing, and product copy that reads as if written by an educated native speaker — correct register (tu/vous), idiomatic phrasing, French typography, and zero machine-translation artefacts. Use whenever French copy is written, adapted, or reviewed; do not rely on raw translation of English source copy.
---

# French Native Copy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- Writing any French-language page, section, microcopy, CTA, email, or metadata for a site the engine builds.
- Adapting approved English copy into French where the French must stand on its own as native copy, not a translation.
- Reviewing French copy (human, translated, or AI-generated) for register, idiom, grammar, and typography before it ships.
- Producing French SEO/GEO copy where the target keyword and phrasing must be researched natively, not transposed from English.

## Do not use when
- The language routing, URL structure, hreflang, or sitemap question is the task — that belongs to `i18n`.
- The cross-language tone policy or three-language consistency question is the task — that belongs to `language-standards`.
- The copy is English or Kiswahili. For Kiswahili use `swahili-native-copy`.

## Required inputs
- The source material the French copy must convey: the approved English copy, the brand brief, or the raw client facts.
- The audience and market: France, francophone Africa (and which country), Canada, or a mixed francophone audience. This sets vocabulary, register defaults, and currency/date conventions.
- The register decision for the brand: `vous` (default for commerce and services) or `tu` (youth, lifestyle, peer-to-peer brands). If unspecified, default to `vous`.
- The page goal and any conversion or SEO targets the copy must hit.

## Workflow
1. Fix the register and audience first. Choose `vous` or `tu` and the francophone market, then hold that choice across the whole page. Mixed register inside one experience is the clearest tell of amateur copy. See `references/register-and-address.md`.
2. Write the French from the meaning, not the English words. Express the idea as a French speaker would frame it, then check it carries every required fact. Translating word-for-word produces calques; see `references/anglicisms-to-avoid.md`.
3. Apply the grammar that machine translation gets wrong as you write: partitive articles, gender and adjective agreement, negation scope, pronoun placement, relative pronouns, and verb-preposition collocations. See `references/grammar-pitfalls.md`.
4. Raise it from correct to native: idiomatic connectors, natural collocations, French CTA verbs, and rhythm. See `references/idiom-and-flow.md`.
5. Apply French typography: narrow non-breaking space before `; : ! ?`, guillemets `« »`, decimal comma, `€` after the number, lowercase days/months/nationalities. See `references/typography-and-formatting.md`.
6. Run the revision checklist and the back-translation test before sign-off. See `references/revision-checklist.md`.

## Quality standards
- A French native reader finds nothing that signals translation: no calques, no anglicisms, no English word order, no English punctuation spacing.
- Register is consistent end to end. Where `vous` is chosen, every verb, pronoun, and possessive agrees with it; the same for `tu`.
- Every adjective agrees in gender and number with its noun; every partitive (`du`, `de la`, `de l'`, `des`) is correct and collapses to `de` after negation and quantity.
- Typography follows French rules, not English: `Découvrir nos services` carries the correct spacing and punctuation; prices read `1 250,00 €`, not `€1,250.00`.
- SEO terms are researched in French, not transposed: the slug and target phrase are what a French speaker actually searches, per `i18n` slug rules.
- The copy passes the back-translation test: translating the French back to English reproduces the intended meaning without distortion.

## Anti-patterns
- Running English copy through translation and lightly editing the output. Write from meaning.
- Mixing `tu` and `vous`, or switching gender of address mid-page.
- Calques such as `Nous offrons des solutions`, `pour plus d'informations cliquez ici`, or `réalisez votre potentiel` where idiomatic French differs. See the anglicism table.
- English punctuation spacing (`Bonjour!` with no space, straight quotes `"..."`, `€50`, `3.50`).
- Inventing French marketing adjectives banned by `glossary.md#banned-terms` in their French equivalents.
- Keeping English slugs or English keyword phrasing on French pages without research.

## Outputs
- Native-quality French copy for the requested artefact (page, section, CTA, email, metadata).
- A short register-and-audience note recording the `tu`/`vous` and market decision so downstream copy stays consistent.
- Review findings with concrete corrections when the task is a review rather than fresh authoring.

## References
- `references/register-and-address.md` — tu vs vous, politeness, conditional softening, formal commercial register.
- `references/grammar-pitfalls.md` — partitive articles, gender and agreement, negation, pronouns, relative pronouns, verb-preposition collocations, multiple-pronoun order, subjunctive triggers, country prepositions, tense/mood for CTAs, past-participle agreement, and the MT smell-test.
- `references/vocabulary-by-theme.md` — native business, finance, tech, hospitality, retail, and health vocabulary with gender, and sector calque traps.
- `references/idiom-and-flow.md` — connectors, collocations, CTA verbs, sensory and premium language, sentence rhythm, native craft tells, and warm story-driven phrasing.
- `references/anglicisms-to-avoid.md` — calques and anglicisms with native French alternatives.
- `references/typography-and-formatting.md` — spacing, guillemets, numbers, currency, dates, capitalisation.
- `references/revision-checklist.md` — native-speaker QA checklist, concord audit, and back-translation test.

## Notes
- This skill is the French execution layer under `language-standards`, which owns the cross-language tone policy. Read `language-standards` for the three-language consistency rules, then apply this skill for French.
- Pair with `i18n` for routing and localized slugs, and with `seo`/`google-ai-search` for French keyword research.
- Source material distilled from: Sylvie Poisson-Quinton, *French Grammar in 44 Lessons* (Level A1); *2000 French Phrases* and *50 Most Used French Verbs* (French Hacking); *Conversational French Dialogues* (Touri Language Learning); and *Read & Think French, Premium* (Think French magazine). Upgraded in 2026 with: Annie Heminway, *Practice Makes Perfect — Complete French Grammar*; Boulares & Frérot, *Grammaire progressive du français — Niveau avancé*; *Learn French II — Parallel Text*; and the *French–English Bilingual Visual Dictionary* (DK). See `book-extractions/french-language-books-extraction-2026.md`.
