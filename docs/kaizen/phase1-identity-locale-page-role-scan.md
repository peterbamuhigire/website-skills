# Phase 1 website Kaizen slice: identity, locale, page role, and scan

Status: IMPLEMENTED CONTRACTS AND SYNTHETIC FIXTURES. Date: 19 September
2026. Scope is limited to B11-A01, B11-A02, B11-A03, B14-A02, and B21-A01 in
the book-study action cards.

## Scope decision

The owning website skills already existed, so this slice extends references and
adds fixture-level checks. No new skill, route implementation, production
content, browser automation, native-language certification, or cross-repository
write was needed. The identity contract starts with `display_name` and
`locale`; `legal_name`, `preferred_name`, `pronunciation`, relationship, and
script metadata remain conditional on purpose, jurisdiction, audience, and
consent or recorded authority.

## Action mapping

| Action | Implemented surface | Evidence |
| --- | --- | --- |
| B11-A01 | `skills/content-copy/french-native-copy/references/identity-and-register-review.md` | minimum identity record, privacy minimisation, register, retention, review states |
| B11-A02 | `skills/build/i18n/references/bilingual-identity-fixtures.md` and `fixtures/website-multilingual/identity-fixtures.json` | original script, transliteration, kinship, mixed script, and intentional omission cases |
| B11-A03 | `skills/content-copy/french-native-copy/references/meaning-first-institutional-copy.md` | official label paired with plain meaning, status, next step, owner, escalation, and back-comparison |
| B14-A02 | `skills/seo-search/seo/references/entity-and-page-role-contract.md` and `fixtures/website-multilingual/page-role-contract.json` | page role, entity facts, visible proof, locale variant, review trigger, and metadata/schema parity |
| B21-A01 | `skills/quality-gates/accessibility-audit/references/question-mark-and-scan-audit.md` and `fixtures/website-multilingual/question-mark-scan.json` | purpose, scan, affordance, hierarchy, recovery, privacy friction, locator, owner, and retest question |

## Evidence status

Observation: the focused fixture tests pass when the records have the required
shape and fail or remain unassessed for the declared negative cases.

Inference: the contracts make the requested review decisions explicit and
reusable by the existing skills; they do not demonstrate a production site's
behaviour.

Not assessed: native-speaker and domain review, consent and jurisdictional
compliance, rendered browser layout, screen-reader pronunciation, live crawl or
schema validation, user observation, conversion, accessibility conformance,
and production retention/deletion controls. The fixture records preserve these
as `NOT_ASSESSED` rather than implying approval.

## Rollback and handoff

The slice is additive. A maintainer can remove the new reference links and
fixture/test files while preserving all prior skill and route behaviour. The
designated root agent owns final diff review, integration, and any decision to
promote the contracts beyond fixture/shadow mode.
