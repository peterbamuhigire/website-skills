# Identity and register review

This reference records the smallest identity and language decision needed for a
French web surface. It is a review contract, not a user-profile schema or a
legal identity policy.

## Purpose and scope

Use this record when a name, address form, relationship term, pronunciation,
or locale crosses a page, form, campaign, support flow, or institutional
surface. The record separates what the audience should see from data that a
system might be able to store.

The default record is deliberately small:

```yaml
display_name: "Amina N."
locale: "fr-CD"
```

Add another field only when the purpose, jurisdiction, audience, and consent or
other lawful authority are recorded. A field that is merely convenient is not a
purpose.

| Field | Default | Add only when | Minimum evidence |
| --- | --- | --- | --- |
| `display_name` | allowed | the person or organisation needs a visible label | stated page or interaction purpose |
| `locale` | allowed | the surface has locale-sensitive content | approved locale map |
| `legal_name` | omit | a legal, statutory, payment, certificate, or identity check requires it | jurisdiction, actor, retention, and authority |
| `preferred_name` | omit | the user-facing address or personalisation needs a choice beyond `display_name` | user choice and display purpose |
| `pronunciation` | omit | audio, live support, or an explicitly requested pronunciation aid needs it | requested use, consent, and deletion boundary |
| `relationship` | omit | the social relationship changes meaning, access, or address | audience, meaning note, and reviewer |
| `original_script` / `transliteration` | omit | a mixed-script or pronunciation task requires it | locale, rendering need, and review |

Never silently convert a name to a presumed local form. If a field is not
needed, leave it out rather than storing an empty value. Do not use a legal name
as a marketing label by default.

## Record contract

Each decision record must state:

| Input | Required value |
| --- | --- |
| `purpose` | the user task or institutional action |
| `audience` | who reads, hears, or acts on the value |
| `market` and `locale` | named market where French conventions matter |
| `register` | `formal`, `neutral`, `conversational`, or `intimate`; also record `vous` or `tu` where applicable |
| `fields` | field name, visible use, and whether it is required or omitted |
| `consent_or_authority` | `not_needed`, `user_choice`, or a named authority; do not infer consent |
| `retention` | where the value lives, retention period, and deletion route; use `unknown` when unconfirmed |
| `review` | native-copy reviewer, domain reviewer where needed, date, and status |

Use the following outcome states:

- `PASS`: the minimum fields serve the recorded purpose and all required
  reviews are complete.
- `FAIL`: an unnecessary field is collected, a required field is missing, or
  the proposed use contradicts the stated purpose.
- `NOT_ASSESSED`: the copy, native review, jurisdiction, consent, retention,
  or rendered behaviour is unavailable. Do not turn an unknown into approval.

## Review procedure

1. State the page or interaction purpose and the audience before choosing a
   name or register.
2. Start with `display_name` and `locale`. For each additional field, write the
   necessity sentence: “This field is needed because …”.
3. Decide the market and register. Keep institutional, customer-facing, and
   conversational strings separate; do not average them into vague prose.
4. Record the visible label, storage boundary, retention/deletion boundary,
   consent or authority, and any locale-specific treatment.
5. Compare the proposed wording and identity use against the approved meaning.
   Route French copy through the native-copy review and route legal or regulated
   meaning to the relevant domain reviewer.
6. Record the outcome and the exact unresolved question. If the reviewer or
   authority is missing, stage the surface and mark it `NOT_ASSESSED`.

## Failure slices

| Finding | Outcome | Repair |
| --- | --- | --- |
| `legal_name` appears on a public profile with no legal task | `FAIL` | remove it or document the legal purpose, audience, authority, and retention |
| pronunciation is requested only because it might be useful | `FAIL` | omit it until a requested or evidenced use exists |
| `display_name` and `locale` are enough, but empty optional fields are persisted | `FAIL` | omit optional fields entirely |
| French register is chosen but no market or reviewer is named | `NOT_ASSESSED` | name the market and assign native review before release |
| legal effect or identity authority is ambiguous | `NOT_ASSESSED` | obtain the domain decision and preserve the source wording |

## Acceptance oracle

A reviewer must be able to answer, without guessing:

1. What is this identity value for?
2. Who will see or use it?
3. Why is every stored field necessary?
4. Where is it retained and how is deletion handled?
5. Which register and French market apply, and who reviewed them?

The synthetic cases in `fixtures/website-multilingual/identity-fixtures.json`
and `tests/test_kaizen_phase1.py` exercise the minimum-field pass and the
unnecessary-field failure. They are lab evidence only; they do not establish
consent, legal compliance, native quality, or production behaviour.

## References

- `../SKILL.md` for French market, register, meaning, and native-review gates.
- `../../../build/i18n/SKILL.md` for locale equivalence and missing-content policy.
- Action card `B11-A01` for the bounded action and its source limitations (local
  planning input; it is not a production authority).
