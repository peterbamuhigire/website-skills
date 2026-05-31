---
name: swahili-native-copy
description: Native-quality Kiswahili copywriting standard for the website engine. Produces Swahili web, marketing, and product copy that reads as if written by an educated East African native speaker — correct noun-class concord, idiomatic phrasing, respectful register, and zero machine-translation artefacts. Use whenever Kiswahili copy is written, adapted, or reviewed; do not rely on raw translation of English source copy.
---

# Swahili Native Copy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- Writing any Kiswahili page, section, microcopy, CTA, email, or metadata for a site the engine builds.
- Adapting approved English copy into Kiswahili where the Swahili must stand on its own as native copy, not a translation.
- Reviewing Kiswahili copy (human, translated, or AI-generated) for concord, register, idiom, and spelling before it ships.
- Producing Kiswahili SEO/GEO copy where the target phrasing must be researched natively, not transposed from English.

## Do not use when
- The language routing, URL structure, hreflang, or sitemap question is the task — that belongs to `i18n`.
- The cross-language tone policy or three-language consistency question is the task — that belongs to `language-standards`.
- The copy is English or French. For French use `french-native-copy`.

## Required inputs
- The source material the Kiswahili copy must convey: the approved English copy, the brand brief, or the raw client facts.
- The audience and market: Tanzania, Kenya, or a wider East African / regional audience. This sets vocabulary depth, code-switching tolerance, and trust conventions.
- The register for the brand: standard respectful `Kiswahili sanifu` (default for commerce and services), or a warmer peer voice. If unspecified, default to respectful standard.
- The page goal and any conversion or SEO targets the copy must hit.

## Workflow
1. Write in `Kiswahili sanifu` (standard Swahili), the register taught in schools and used in media across Tanzania and Kenya. Avoid `Sheng` and street slang unless the brief explicitly targets a youth-slang voice. See `references/register-and-greetings.md`.
2. Write from meaning, not English words. Frame the idea as an East African speaker would, then confirm it carries every required fact. See `references/loanwords-and-anglicisms.md`.
3. Get noun-class concord right as you write. Every adjective, possessive, demonstrative, number, and verb agreement must match the noun's class (`ngeli`). This is the single biggest failure of machine translation. See `references/noun-classes-and-concord.md`.
4. Build verbs correctly and choose the right mood: subjunctive (`-e`) with `tafadhali` for soft CTAs, imperative for direct ones, correct negatives. See `references/verb-system-and-politeness.md`.
5. Raise it to native: greetings in the right register, respectful address, idiom and the occasional `methali` (proverb), natural collocations. See `references/idiom-and-cultural.md`.
6. Localize numbers, dates, prices, and any time references; handle the Swahili clock carefully. See `references/numbers-time-dates.md`.
7. Run the revision checklist, including a concord audit and back-translation test. See `references/revision-checklist.md`.

## Quality standards
- Concord is correct everywhere: `kitabu kizuri`, `vitabu vizuri`, `huduma bora`, `bidhaa zetu`, `mtoto wetu` agree by class, with no English-word-order or default-class errors.
- Register is respectful and consistent: greetings, address, and CTAs match `Kiswahili sanifu`; no accidental slip into slang or into another dialect mid-page.
- Loanwords follow native norms: integrated Arabic loans used freely (`asante`, `karibu`, `safari`), English handled the native way (`barua pepe` for email, `tovuti` for website, `simu ya mkononi` for mobile), bare English avoided.
- Spelling and orthography are standard: correct use of `ng'` (with apostrophe), `ny`, `ch`, `dh`, `gh`, `th`; no English-influenced spellings.
- SEO terms are researched in Kiswahili, not transposed; the slug and target phrase are what an East African actually searches, per `i18n` slug rules.
- The copy passes the back-translation test: translating back to English reproduces the intended meaning without distortion.

## Anti-patterns
- Translating English word-for-word and producing broken concord (`kubwa nyumba` instead of `nyumba kubwa`; `letu duka` instead of `duka letu`).
- Default-class agreement: forcing M-/WA- (human) concord onto non-human nouns, or ignoring the N-class behaviour of family terms (`dada yangu`, not `dada wangu`).
- Calques such as `Karibu kwa tovuti` for "Welcome to the website", or bare `email`, `online`, `website` left untranslated.
- Mixing Tanzanian and Kenyan conventions or sliding into `Sheng` in copy meant to be standard.
- Mishandling the Swahili clock so opening hours or times are six hours off.
- Inventing marketing adjectives banned by `glossary.md#banned-terms` in their Swahili equivalents.

## Outputs
- Native-quality Kiswahili copy for the requested artefact (page, section, CTA, email, metadata).
- A short register-and-audience note recording the market (Tanzania/Kenya/regional) and voice decision so downstream copy stays consistent.
- Review findings with concrete corrections when the task is a review rather than fresh authoring.

## References
- `references/noun-classes-and-concord.md` — the `ngeli` system and agreement across adjectives, possessives, demonstratives, numbers, and verbs.
- `references/verb-system-and-politeness.md` — verb structure, tenses, negatives, imperative and subjunctive, `tafadhali`, polite requests.
- `references/register-and-greetings.md` — `Kiswahili sanifu`, greetings by register, honorifics, plural-of-respect, dialect and slang lines.
- `references/idiom-and-cultural.md` — collocations, trust language, `methali`, and East African cultural conventions for copy.
- `references/loanwords-and-anglicisms.md` — Arabic loans, English-word handling, calques to avoid, Tanzania vs Kenya usage.
- `references/numbers-time-dates.md` — numbers with concord, the Swahili clock, days, months, dates, and currency.
- `references/revision-checklist.md` — native-speaker QA checklist, concord audit, and back-translation test.

## Notes
- This skill is the Kiswahili execution layer under `language-standards`, which owns the cross-language tone policy. Read `language-standards` for the three-language consistency rules, then apply this skill for Kiswahili.
- Pair with `i18n` for routing and localized slugs, with `africa-excellence` for low-bandwidth and East African trust patterns, and with `seo`/`google-ai-search` for Kiswahili keyword research.
- Source material distilled from: Oswald Almasi, Michael David Fallon et al., *Swahili Grammar for Introductory and Intermediate Levels (Sarufi ya Kiswahili)*; Joan Russell, *Swahili (Teach Yourself)*; Lutz Marten & Donovan Lee McGrath, *Colloquial Swahili*; and *Swahili (Spoken World)* (Living Language).
