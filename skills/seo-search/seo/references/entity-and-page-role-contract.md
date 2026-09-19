# Entity and page-role contract

Use this contract to connect a page's user job, entity facts, visible proof,
locale variant, metadata, and review trigger. It is a content and search
implementation record; it is not evidence of rankings, retrieval, or
recommendation.

## Page record

Every indexable page should have one record with:

| Field | Required decision |
| --- | --- |
| `route` and `locale` | canonical route and approved locale |
| `page_role` | `evergreen`, `current`, `deep-guide`, or `transactional` |
| `user_job` and `search_intent` | what the reader is trying to do |
| `primary_entity` | named organisation, person, place, service, product, or article |
| `entity_facts` | subject–predicate–object facts with source locators |
| `visible_proof` | evidence shown on the page; omit unsupported claims |
| `locale_variant` | equivalent, locale-specific, missing, or intentionally excluded |
| `canonical` / `alternates` | generated from the same approved route map |
| `metadata_and_schema` | title, description, headings, and only supported schema |
| `owner` / `reviewer` | responsible content and review roles |
| `review_trigger` / `review_date` | event or cadence that makes the page stale |
| `status` | `PASS`, `FAIL`, or `NOT_ASSESSED` |

## Page roles and review triggers

| Role | Information job | Review trigger |
| --- | --- | --- |
| `evergreen` | stable identity, explanation, or durable guidance | entity, offer, route, or policy change |
| `current` | fact that can change, such as availability or an active notice | named date, status change, or scheduled cadence |
| `deep-guide` | sourced explanation that needs maintained reasoning | source change, material contradiction, or scheduled review |
| `transactional` | action, requirements, eligibility, or offer completion | process, price, eligibility, owner, or integration change |

Do not make one page serve every role without stating which facts are stable,
which need dates, and which need sources and reasoning.

## Entity facts and visible proof

Write entity facts as plain subject–predicate–object statements, for example:

```text
[Entity] — [offers] — [verified service or product].
[Entity] — [serves] — [named audience or area, only when evidenced].
[Page] — [explains] — [the stated user job].
```

Each fact needs an owner, source locator, access or publication date when
relevant, locale treatment, and a review trigger. The visible page, metadata,
and schema must describe the same entity and facts. If a fact is not visible or
verified, omit it from schema and mark the record `NOT_ASSESSED` or `FAIL` as
appropriate.

## Review procedure

1. Assign the page role and user job before drafting metadata or schema.
2. Resolve the primary entity and facts from approved sources; record locale
   variants and genuine equivalents.
3. Map visible headings, proof, CTA, canonical, alternates, and schema to the
   record. Do not emit false alternates for missing or non-equivalent pages.
4. Set the owner, reviewer, review trigger, and date. A current page without a
   date or trigger is not release-ready.
5. Render or inspect the page and compare visible copy with metadata and schema.
   Static source inspection cannot establish rendered parity.

## Acceptance oracle and failure paths

`PASS` requires visible page role, owner, source, review date/trigger, and
entity facts; metadata and schema match visible content; locale links are true
equivalents. `FAIL` covers invented or contradictory facts, stale current data,
or conflicting metadata. `NOT_ASSESSED` covers missing render, source, native
review, or live crawl evidence.

| Finding | Outcome | Repair |
| --- | --- | --- |
| page has no role or user job | `FAIL` | assign the role and route owner before implementation |
| current fact has no date or review trigger | `FAIL` | add the trigger or remove the current claim |
| schema contains a fact absent from visible copy | `FAIL` | align visible content or omit the property |
| locale counterpart is missing or non-equivalent | `FAIL` | omit the alternate and record the gap |
| render or live crawl check was not run | `NOT_ASSESSED` | run the named check before release |

The synthetic page-role record in
`fixtures/website-multilingual/page-role-contract.json` and its tests show
normal and failing cases without claiming a real site outcome.

## References

- `../SKILL.md` for metadata, structured data, locale, and crawler contracts.
- `../../../build/i18n/SKILL.md` for route equivalence and missing alternates.
- `../../../content-copy/french-native-copy/SKILL.md` for native locale review.
