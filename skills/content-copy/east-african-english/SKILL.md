---
name: east-african-english
description: Use when English website copy must sound natural, clear, respectful, and professionally East African; use `language-standards` for multilingual policy and `content-writing` for message structure.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# East African English
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

Apply an East African, British-influenced English register without caricature, imported slang, or blanket regional assumptions.

<!-- dual-compat-start -->
## Use When

- Drafting or reviewing English copy for audiences in Uganda, Kenya, Tanzania, or the wider region.
- A site needs courteous, credible language that reflects local commercial communication.
- Imported US copy, slang, or idiom sounds foreign to the intended reader.

## Do Not Use When

- The task is French or Kiswahili execution; use the matching native-copy skill.
- The task is multilingual governance; use `language-standards`.
- The message hierarchy or conversion argument is broken; fix it with `content-writing` before polishing register.

## Required Inputs

| Artefact | Source or provider | Required? | When missing |
|---|---|---:|---|
| English draft or content brief | Project owner | yes | Return a short style brief if no draft exists. |
| Target country, audience, and context | Brand or market brief | yes | Use neutral international British English and label regional choices unresolved. |
| Brand voice and required terminology | Brand guidance or client | conditional | Preserve established terminology; flag conflicts rather than silently replacing it. |

## Workflow

1. Identify the country, audience, channel, and level of formality.
2. Stop and request context when a local term could change meaning, trust, or legal interpretation.
3. Preserve the author's meaning and business facts while correcting spelling, idiom, courtesy, and rhythm.
4. Replace imported slang or forced regionalisms with plain language unless evidence shows the audience uses them.
5. Check dates, currency, addresses, phone formats, and institutional terms against the target market.
6. Read the result aloud for natural cadence and review every material change.
7. If country-specific verification is unavailable, revert to neutral British English and disclose the limitation.

Recovery: repair disputed terminology with the owner, then rerun the regional and meaning review.

## Quality Standards

- British spelling is consistent unless the client's established house style requires otherwise.
- Language is direct and respectful, not stiff, patronising, or artificially "local".
- Regional terms are used only when they improve comprehension for the named audience.
- Facts, names, prices, dates, and quotations remain unchanged unless correction is evidenced.
- Review findings identify exact wording and a usable correction.

## Anti-Patterns

- Adding "kindly" to every instruction. Fix: use it only where courtesy genuinely requires it.
- Treating East Africa as one uniform dialect. Fix: name the country and audience or use neutral English.
- Replacing clear English with slang to sound local. Fix: prefer familiar professional language.
- Converting British spelling inconsistently. Fix: apply one project-wide spelling standard.
- Editing facts while editing tone. Fix: preserve claims and flag factual issues separately.
- Calling a phrase wrong because it differs from US usage. Fix: judge it against audience comprehension and the agreed regional standard.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Revised English copy | Page or content owner | Meaning is preserved and regional, spelling, and courtesy choices are consistent. |
| Language review notes | Author or approver | Each material issue includes the original, correction, and reason. |
| Regional style decision | Future writers | Country, register, spelling, and unresolved terminology are recorded. |

## References

- [Legacy detailed guidance](references/legacy-guidance.md) for the preserved regional language standard and examples.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Change log | Inline notes or tracked list | Material register and terminology edits are traceable. |
| Regional decision note | Short record | Target market and any neutral-language fallback are explicit. |

## Capability Contract

Read access to the draft and market context is required. Review defaults to read-only. Editing the source requires explicit authority. Network access may verify current institutional or market terminology; it is not required for basic prose review.

## Degraded Mode

When country context or verification is unavailable, use neutral international British English, retain uncertain local terms, and list them for confirmation. Never label an unverified regional expression as correct.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| One named national audience | Apply verified local conventions | Generic regional stereotyping |
| Mixed East African audience | Prefer widely understood neutral forms | Country-specific wording confusing other readers |
| Established brand term conflicts with preference | Preserve and flag | Unauthorised voice drift |
| Meaning changes under a proposed edit | Stop and ask | Tone editing that changes the offer or claim |

## Worked Example

Input: a Kenyan service page says "Schedule your free consult today" for a formal procurement audience. Revision: "Book an initial consultation"; the note records the formal register choice and does not add Kenyan slang.

## Read Next

- `language-standards` governs cross-language consistency.
- `content-writing` fixes message hierarchy and page purpose.
- `premium-commercial-writing` supplies the commercial editorial gate.
