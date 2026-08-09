---
name: swahili-native-copy
description: Use when Kiswahili web, marketing, product, email, or metadata copy must read naturally for a named East African market; use `language-standards` for cross-language policy and `i18n` for routing.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Swahili Native Copy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Author Kiswahili from meaning with correct noun-class concord, register, idiom, and market conventions.

## Target Markets (Standard)

Kiswahili content from this engine targets East and Central Africa. The primary markets are:

**Primary:** Kenya, Tanzania (mainland and Zanzibar)
**Secondary:** DR Congo (Kiswahili-speaking eastern provinces and Kinshasa growing market)
**Tertiary:** Uganda (limited Kiswahili readership — do not assume Ugandan readers), Rwanda, Burundi, Mozambique (Kiswahili-speaking communities)

The reader is an educated professional with advanced Kiswahili comprehension. They expect standard Kiswahili (Kiswahili sanifu) — respectful, formal, and clear. Many read Kiswahili as L1 (Tanzania, coastal Kenya) or as a strong L2 (inland Kenya, DRC).

**Default to respectful standard Kiswahili.** Avoid Sheng (Nairobi street slang), avoid Mombasa dialect features, avoid Zanzibari historical variants. When a market-specific term differs between Kenya and Tanzania, record the decision and use the term most widely understood.

<!-- dual-compat-start -->
## Use When

- Writing or revising Kiswahili pages, CTAs, microcopy, emails, or metadata.
- Adapting approved source meaning into native Kiswahili rather than literal translation.
- Reviewing concord, register, idiom, spelling, numbers, dates, or search phrasing.

## Do Not Use When

- The task is locale routing, hreflang, slugs, or sitemap structure; use `i18n`.
- The task is cross-language parity; use `language-standards`.
- The copy is English or French; use the matching native-language skill.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| Approved meaning, facts, and offer | Source copy, brief, or client notes | yes | Stop and request the missing source of truth. |
| Target market: Tanzania, Kenya, or regional | Project brief | yes | Use respectful `Kiswahili sanifu` provisionally and flag localisation unresolved. |
| Brand register and code-switching boundary | Brand owner | conditional | Default to respectful standard and avoid slang. |
| Page goal, proof, SEO target, and constraints | Content/SEO owner | conditional | Preserve meaning and label search or conversion choices provisional. |

## Workflow

1. Fix the market, audience, and register using [register and greetings](references/register-and-greetings.md).
2. Stop if the source meaning, time, price, or regulated claim is ambiguous.
3. Write from meaning, not English order; handle loanwords through [loanwords and anglicisms](references/loanwords-and-anglicisms.md).
4. Audit noun classes and agreement using [noun classes and concord](references/noun-classes-and-concord.md).
5. Check verb structure, tense, negatives, imperative, subjunctive, and politeness using [verb system and politeness](references/verb-system-and-politeness.md).
6. Improve natural collocations and culturally appropriate language with [idiom and cultural guidance](references/idiom-and-cultural.md).
7. Localise numbers, dates, prices, opening hours, and the Swahili clock with [numbers, time, and dates](references/numbers-time-dates.md).
8. Research search phrasing natively when network access and SEO scope allow.
9. Run [the revision checklist](references/revision-checklist.md), including concord and meaning comparison.
10. If competent native verification is unavailable, mark it `not assessed` and return a focused review brief.

Recovery: repair meaning, concord, or register findings, then rerun the native-copy checklist.

## Quality Standards

- Noun-class agreement is correct across adjectives, possessives, demonstratives, numbers, and verbs.
- Register is respectful and consistent, with no unapproved slide into slang or another dialect.
- Loanwords and technical terms follow the named market's normal usage.
- Spelling, dates, prices, and times are unambiguous and locally correct.
- Search terms are researched in Kiswahili when SEO claims are made.
- Back-comparison preserves every material fact and next step.

## Anti-Patterns

- Translating English word order directly. Fix: rebuild the sentence around Kiswahili syntax.
- Applying default M-/WA- concord to every noun. Fix: identify the noun class and audit all agreement.
- Leaving avoidable bare English terms. Fix: use established Kiswahili or an approved market term.
- Mixing Kenyan, Tanzanian, and Sheng conventions silently. Fix: record the market and code-switching boundary.
- Mishandling the Swahili clock. Fix: state and verify the intended civil time.
- Transposing English keywords. Fix: research how the target reader expresses the intent.
- Certifying native quality without review. Fix: mark it `not assessed` and request review.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Native Kiswahili copy | Page, campaign, or product owner | Meaning, concord, register, idiom, and localisation pass the checklist. |
| Market and register note | Future writers | Market, audience, voice, terminology, and code-switching decisions are recorded. |
| Review findings | Author or approver | Each issue shows the original, correction, reason, and severity. |

## References

- [Noun classes and concord](references/noun-classes-and-concord.md)
- [Verb system and politeness](references/verb-system-and-politeness.md)
- [Register and greetings](references/register-and-greetings.md)
- [Idiom and cultural guidance](references/idiom-and-cultural.md)
- [Loanwords and anglicisms](references/loanwords-and-anglicisms.md)
- [Numbers, time, and dates](references/numbers-time-dates.md)
- [Revision checklist](references/revision-checklist.md)
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Locale and register record | Short note | Market, voice, terminology, and provisional choices are explicit. |
| Native-copy review | Checklist or issue table | Concord, meaning, idiom, localisation, and unassessed checks are visible. |

## Capability Contract

Read access to source meaning and Kiswahili copy is required. Review defaults to read-only; editing requires explicit authority. Network access may verify current market and search usage. Native-speaker review cannot be claimed unless it occurred.

## Degraded Mode

Without market context, network research, fonts/rendering, or a competent native review, return respectful provisional `Kiswahili sanifu` and name each unassessed dimension. Never treat unavailable native or visual verification as passed.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Mixed or unspecified East African audience | Use respectful standard provisionally | Slang or country-specific exclusion |
| Named market has established usage | Localise terminology and formats | Artificial textbook copy |
| Youth-slang voice is explicitly approved | Define the exact boundary | Uncontrolled register drift |
| Meaning, time, or claim is ambiguous | Stop and clarify | Material mistranslation |

## Worked Example

Source intent: advertise a shop opening at 8:00 a.m. civil time in Dar es Salaam. The copy records Tanzania as the market, verifies how the displayed time will be understood, and avoids an unreviewed Swahili-clock conversion.

## Read Next

- `language-standards` for cross-language parity.
- `i18n` for technical locale routing.
- `africa-excellence` for wider East African delivery patterns.
