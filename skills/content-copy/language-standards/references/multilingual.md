# Multilingual Consistency and Language Routing

**Purpose**: Define how the engine keeps one brand voice across English, French, and Kiswahili, and route each language to its native-copy execution skill so non-English copy is written natively, never machine-translated.

**Read this when**: A project ships in more than one language, you are deciding which skill writes which language, or you are checking that the three language versions stay consistent in meaning, tone, and trust.

## The three supported languages

The engine supports three first-class languages (see `i18n`):

- **English** — British-influenced East African English. Owner: `east-african-english` (standard) with `content-writing` and `premium-commercial-writing` for structure and persuasion.
- **French** — Francophone (France, francophone Africa, or Canada per audience). Owner: `french-native-copy`.
- **Kiswahili** — `Kiswahili sanifu` for Tanzania, Kenya, and the wider East African region. Owner: `swahili-native-copy`.

## Mandatory routing

Each non-English language has a dedicated native-copy skill. Using it is not optional:

- Write French through `french-native-copy`. Do not produce French by translating English and editing the output.
- Write Kiswahili through `swahili-native-copy`. Do not produce Kiswahili by translating English and editing the output.
- `language-standards` (this skill) owns the cross-language tone policy and consistency; the native-copy skills own correctness and idiom within each language.

The order is: agree the message and tone in `language-standards` → write each language version with its native-copy skill → reconcile the versions for consistency (below).

## What stays consistent across languages

- **Meaning and claims**: every language version states the same facts, offers, prices, and guarantees. A promise in one language exists in all.
- **Brand voice and positioning**: warmth, formality level, and personality carry across, even though the grammatical means differ (French `vous`, Swahili honorifics, English courtesy).
- **Structure and conversion intent**: the same page goal, the same call to action intent, the same trust signals — though the exact wording is native to each language, not parallel-translated.
- **Names and proper nouns**: brand names, product names, and legal entities stay identical unless a localized name is deliberately adopted.

## What is allowed to differ

- **Wording and idiom**: each version is written natively, so phrasing, idioms, and sentence shape differ. Parallel word-for-word versions are a failure, not a goal.
- **Register mechanics**: French chooses `tu`/`vous`; Swahili chooses singular-personal vs plural-respectful and honorifics; English uses courtesy and modality. Each is set per language to produce the same felt tone.
- **Examples and cultural references**: localize examples, names, currency, dates, and proverbs to the audience. A Swahili `methali` has no French equivalent and need not.
- **Length**: French commonly runs ~15–20% longer than English; Swahili verb morphology can compress or expand. Design and layout must absorb expansion (see `i18n` and `design-system`).

## Routing into the build

- **Slugs and URLs**: localize per language; never swap only the language prefix. See `i18n` slug rules.
- **SEO/GEO terms**: research keywords natively in each language; do not transpose the English phrase. Coordinate with `seo` and `google-ai-search`.
- **Metadata**: title and description are written natively per language within length limits, not truncated translations.
- **Microcopy, forms, errors, emails**: all of it routes through the native-copy skill for its language — not just the marketing pages.

## Consistency check before sign-off

1. Claims parity: every fact, price, offer, and guarantee appears in all shipped languages.
2. Tone parity: each version produces the same brand feeling, verified by a native reader per language.
3. Native quality: each non-English version passes its own revision checklist (`french-native-copy`/`references/revision-checklist.md`, `swahili-native-copy`/`references/revision-checklist.md`).
4. No translation artefacts: no calques, no English word order, no English punctuation or number formatting in the non-English versions.
5. Routing integrity: slugs, `hreflang`, and canonical resolve so a language switch lands on the matching page.

## Source

Routing and consistency policy for the engine's three-language model; native-language correctness is owned by `french-native-copy` and `swahili-native-copy`, which cite their own primary-source language references.
