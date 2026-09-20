# Meaning-first institutional French handoff

This handoff converts an approved institutional or workflow meaning into
reviewable French copy. It keeps the official term available while giving the
reader a plain account of status, next step, owner, and escalation. It does
not interpret law or change an official decision.

## Handoff record

Record one row per label, status, notice, or workflow step:

| Field | Required content |
| --- | --- |
| `source_label` | official source wording and source locator |
| `plain_meaning` | what happened in reader language |
| `status` | current state and its evidence |
| `next_step` | what the reader should do, or state that no action is needed |
| `owner` | team or named role responsible for the next step |
| `escalation` | approved contact or condition for help |
| `legal_effect` | preserved effect, limitation, or `domain review required` |
| `market` / `locale` / `audience` | named French market and reader |
| `register` | `vous` or `tu`, plus institutional/formal/neutral choice |
| `native_review` | reviewer, date, findings, and status |
| `domain_review` | reviewer for legal, regulated, or policy meaning |
| `back_comparison` | facts, actor, action, timing, and consequence preserved |

If any required meaning or owner is missing, stage the copy and mark the
handoff `NOT_ASSESSED`.

## Procedure

1. Capture the official label and its source. Do not rewrite an unclear source
   before the domain owner confirms what it means.
2. Identify the actor, action, affected person, status, timing, consequence,
   and available recovery path.
3. Write a plain-language explanation in the named market and register. Pair
   it with the official label in a controlled details or glossary element when
   the label must remain visible.
4. State the next step, owner, and escalation route. If there is no next step,
   say so explicitly.
5. Run the French native-copy review for grammar, idiom, typography, and
   register. Run domain review whenever simplification could affect legal or
   policy effect.
6. Back-compare the reviewed text with the source. Record every omitted,
   added, softened, or ambiguous point and repair before release.

## Synthetic pattern

```yaml
source_label: "[official status label]"
plain_meaning: "[what this status means to the reader]"
status: "[current state]"
next_step: "[action or no action required]"
owner: "[responsible role]"
escalation: "[approved support route]"
legal_effect: "[preserved source meaning; domain review required if unclear]"
market: "fr-CD"
locale: "fr-CD"
audience: "service user"
register: "vous / institutionnel"
native_review: "NOT_ASSESSED"
domain_review: "NOT_ASSESSED"
```

The placeholders are intentional. Do not present a fabricated official label,
contact, deadline, or legal conclusion as a production example.

## Acceptance oracle

A task reviewer can state what happened, what to do next, when or under what
condition it will happen, who owns it, and where to ask for help. The official
meaning, actor, consequence, and limitations remain unchanged. Native or domain
review that has not occurred is visible as `NOT_ASSESSED`.

## Failure paths

| Finding | Outcome | Repair |
| --- | --- | --- |
| plain copy hides the official status or changes its effect | `FAIL` | retain the official label and obtain domain review |
| next step or owner is absent | `FAIL` | obtain the workflow owner or state that no action is required |
| French draft is literal, mixed-register, or unreviewed | `NOT_ASSESSED` | rewrite from meaning and assign native review |
| source meaning is ambiguous | `NOT_ASSESSED` | stop and resolve the source with the responsible domain owner |

## References

- `../SKILL.md` for market, register, native drafting, and back-comparison.
- `../../../build/i18n/SKILL.md` for locale routing and missing-content states.
- `C:/wamp64/www/chwezi-dev-engine/skills/frontend-ux/ux-content-strategy/SKILL.md`
  for status, error, and recovery content ownership.
