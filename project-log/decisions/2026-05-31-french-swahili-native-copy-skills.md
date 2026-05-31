# Native-quality French and Kiswahili copy skills

- **Date**: 2026-05-31
- **Status**: Accepted
- **Phase**: Not phase-bound (content-copy layer expansion)
- **Driver**: Founder

## Summary

The engine's multilingual support listed English, French, and Kiswahili, but
only English had a dedicated language-quality skill (`east-african-english`,
plus `content-writing` and `premium-commercial-writing`). French and Kiswahili
relied on `language-standards` policy alone, leaving the actual copy exposed to
machine-translation artefacts: calques, broken French agreement and typography,
and broken Kiswahili noun-class concord.

Two dedicated execution skills were added under `skills/content-copy/` so that
French and Kiswahili copy is written natively rather than translated:

- `french-native-copy`
- `swahili-native-copy`

Both sit under `language-standards`, which now explicitly owns the
cross-language consistency policy and routes each non-English language to its
native-copy skill.

## Deliverables

- `skills/content-copy/french-native-copy/SKILL.md` and six references:
  `register-and-address.md`, `grammar-pitfalls.md`, `idiom-and-flow.md`,
  `anglicisms-to-avoid.md`, `typography-and-formatting.md`,
  `revision-checklist.md`.
- `skills/content-copy/swahili-native-copy/SKILL.md` and seven references:
  `noun-classes-and-concord.md`, `verb-system-and-politeness.md`,
  `register-and-greetings.md`, `idiom-and-cultural.md`,
  `loanwords-and-anglicisms.md`, `numbers-time-dates.md`,
  `revision-checklist.md`.
- New `skills/content-copy/language-standards/references/multilingual.md` —
  three-language consistency rules and routing into the native-copy skills.
- `language-standards/SKILL.md` updated to route French and Kiswahili to the
  native-copy skills and to forbid raw-translation output for those languages.
- `glossary.md`, `CLAUDE.md`, `README.md`, and `AGENTS.md` updated: new
  canonical skill names, content-copy count raised from 8 to 10, and routing
  entries.

## Rationale

- French and Kiswahili each have specific failure modes that generic policy
  cannot prevent. French needs register discipline (tu/vous), partitive and
  agreement correctness, and French typography. Kiswahili needs noun-class
  concord across every dependent word — the dominant failure of translated
  Swahili — plus correct verb mood and the Swahili-clock conversion.
- Encoding these as execution skills with deep references makes native quality
  repeatable and reviewable, and gives each language a blocking revision
  checklist with a back-translation test.
- Reference material was distilled from primary language sources: Poisson-Quinton
  *French Grammar in 44 Lessons*; *2000 French Phrases* and *50 Most Used French
  Verbs* (French Hacking); *Conversational French Dialogues* (Touri); *Read &
  Think French, Premium*; Almasi/Fallon *Swahili Grammar (Sarufi ya Kiswahili)*;
  Russell *Swahili (Teach Yourself)*; Marten & McGrath *Colloquial Swahili*;
  *Swahili (Spoken World)* (Living Language).

## Risks

- Native-quality review still requires a native reader per language; the skills
  raise the floor and define acceptance criteria but do not replace a final
  native check. The revision checklists make this explicit.
- Raw extraction notes from the source books contained errors; all language
  examples in the shipped references were verified and corrected against
  standard usage before inclusion (for example, `barua pepe` not a literal
  coinage; correct negative subject prefixes; correct imperative/subjunctive
  forms).

## Follow-up

- Run `skill-safety-audit` on both new skills.
- Run `drift-check.sh` to confirm glossary, links, and banned-term compliance.
- Consider a future Kiswahili and French keyword-research note co-owned with
  `seo`/`google-ai-search` once a live francophone or East African project
  needs it.
