# Bilingual identity fixtures

Use these synthetic fixtures to check that identity-bearing and mixed-language
strings keep their meaning when they cross locales. They test data shape and
rendering decisions; they do not certify a language, culture, or screen-reader
experience.

## Fixture record

Every fixture should state:

| Field | Meaning |
| --- | --- |
| `id` | stable test identifier |
| `kind` | `original-script`, `transliteration`, `kinship`, `mixed-script`, or `intentional-omission` |
| `source_locale` / `target_locale` | locale and market context |
| `source_text` | approved source string; synthetic text is preferred in the lab |
| `transliteration` | optional pronunciation aid; omit unless the task needs it |
| `gloss` | short meaning for the reviewer, not replacement copy |
| `context` / `register` | where the string appears and how it addresses the audience |
| `direction` | `ltr`, `rtl`, or `auto` |
| `bidi_isolation` | whether `<bdi>`, `unicode-bidi: isolate`, or equivalent is required |
| `expected` | meaning, punctuation, and omission rule that must survive |
| `review` | native reviewer, date, and `PASS`, `FAIL`, or `NOT_ASSESSED` |

Do not put a long literary passage in a fixture. One short phrase or name is
enough to expose a data or rendering error.

## Required fixture cases

1. **Original-script name:** preserve the approved source spelling; do not
   silently normalise it into the target language.
2. **Transliteration:** include it only when requested or needed for the
   stated task, and keep the original script as the identity source.
3. **Kinship or address term:** record the social function and register. A
   generic equivalent is not automatically faithful.
4. **Mixed-script run:** isolate a name, URL, number, or foreign phrase inside
   surrounding copy so punctuation and order remain stable.
5. **Intentional omission:** prove that an unnecessary legal, preferred, or
   pronunciation field is omitted rather than stored as a blank.

## Review procedure

1. Start from the approved source meaning and locale map.
2. Mark whether the target is a translation, transliteration, retained term,
   gloss, or deliberate omission.
3. Check punctuation, bidi isolation, line wrapping, and register using the
   longest realistic string available.
4. Compare the source and target for actor, relationship, action, and
   consequence. Record an issue rather than guessing where equivalence is
   uncertain.
5. Require a competent native review for release. Without that review, keep
   the result `NOT_ASSESSED` even when static checks pass.

## Acceptance and failure evidence

`PASS` means the expected meaning and omission rule are preserved and the
record contains the required locale and review fields. `FAIL` means an
identity field was silently changed, punctuation/order is corrupted, a mixed
script is not isolated when needed, or an unnecessary field appears. Use
`NOT_ASSESSED` for missing native review, rendering, or assistive-technology
evidence.

The fixture pack at
`fixtures/website-multilingual/identity-fixtures.json` covers all five cases.
The associated tests are deterministic and synthetic; they are not a native
speaker sign-off or a live browser result.

## Boundaries

- `display_name` plus `locale` is sufficient when no legal, pronunciation, or
  relationship purpose exists.
- `legal_name`, `preferred_name`, `pronunciation`, relationship, and script
  metadata remain conditional on purpose, jurisdiction, audience, and consent
  or other recorded authority.
- A fixture cannot prove font coverage, screen-reader pronunciation, or visual
  layout without a rendered run; those checks remain `NOT_ASSESSED` here.
