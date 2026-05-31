# French Copy Revision Checklist

**Purpose**: A final pass that catches the errors that survive drafting. Run it on every piece of French copy before sign-off, whether authored fresh or adapted from English.

**Read this when**: The French draft exists and you need to verify it is native-quality before it ships, or you are reviewing someone else's French copy.

## How to use

Work top to bottom. Any failure is a blocking edit, not a suggestion. Record the register/audience decision at the top so the next writer inherits it.

## 1. Register and consistency

- One address throughout: `vous` (default) or `tu` (declared brand choice). No mid-page switch.
- Brand voice consistent: `nous` (or `on` only in `tu` voice) for the company; never a stray `je` unless the page is a named person speaking.
- Honorifics correct where used: `Madame, Monsieur`; no `Cher client` opener.

## 2. Grammar audit (see grammar-pitfalls.md)

- Every adjective agrees in gender and number with its noun.
- Partitives correct (`du`/`de la`/`des`), collapsing to `de` after negation and after quantity words.
- Negation complete in writing: `ne … pas` present (not dropped).
- Object pronouns before the verb (after, hyphenated, only in affirmative imperative).
- `qui`/`que`/`dont`/`où` chosen by grammatical role, not by meaning.
- Verb-preposition pairs correct (`bénéficier de`, `répondre à`, `attendre` + no prep).
- `c'est` vs `il est` correct; profession after `être` takes no article.

## 3. Idiom and flow (see idiom-and-flow.md)

- Connectors present and correct (`en effet` vs `en fait`, `ainsi`, `par ailleurs`).
- Verb-noun collocations native (`proposer`/`assurer`/`garantir`, not `offrir des solutions`).
- CTA buttons use the infinitive (`Découvrir`, `Demander un devis`); link text names its destination, never `Cliquez ici`.
- Sentence rhythm varied; not chopped into translated-English fragments.

## 4. Anglicism sweep (see anglicisms-to-avoid.md)

- No calques from the table (`pour plus d'informations cliquez ici`, `centré sur le client`, etc.).
- No false friends misused (`actuellement`, `éventuellement`, `assister à`, `sensible`).
- Borrowed English words replaced where a better French term exists (`assistance` not `support`, `numérique` not `digital` in quality copy); Québec audience → anglicisms removed (`courriel`).
- No English noun stacks, possessive `'s`, or `-ing` progressives carried over.

## 5. Typography (see typography-and-formatting.md)

- Narrow non-breaking space before `; : ! ?` and inside `« »`.
- Guillemets `« »`, curly apostrophes — no straight quotes.
- Decimal comma, space thousands, space before `%`, `€` after the amount.
- Sentence-case headings; lowercase days, months, nationalities; accents on capitals (`À propos`).
- Page is UTF-8 and the font renders every accent, including `œ`.

## 6. Back-translation test

Translate the finished French back into English in your head (or literally on paper). The result must reproduce the intended meaning with no distortion, no missing fact, and no accidental change of register. If the back-translation drifts from the brief, the French is wrong even if it "sounds nice".

## 7. Read-aloud test

Read the French aloud. Stumbling, an unnatural pause, or a phrase a native would not say marks a calque or a rhythm problem. Rewrite from meaning, not by patching words.

## 8. SEO and slug check (with i18n and seo)

- Target keyword is what a French speaker actually searches, researched in French — not a transposed English phrase.
- Slug is localized per `i18n` rules; `hreflang` and canonical resolve to the matching French page.
- Metadata title and description are native French within length limits, not truncated translations.

## Acceptance criteria

The copy ships only when sections 1–8 pass. A reviewer who is a French native speaker should read the page and find nothing that betrays it was produced for a multilingual build rather than written in French from the start.

## Source

Checklist synthesised from the French native-copy reference set; grammar and idiom items trace to Sylvie Poisson-Quinton, *French Grammar in 44 Lessons* (Level A1), *2000 French Phrases* (French Hacking), and *Read & Think French, Premium* (Think French magazine).
