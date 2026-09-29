# Roadmap to world-class

Current: published 55.2, Readiness 59.6. Targets are measured-constrained
overall scores; the published number stays capped at 65 until the portfolio
craft standard's acceptance evidence exists.

## P0 — applied proof and routing coverage (target about 59; Readiness about 62.7)

1. **Routing fixture coverage.** Add three positives and two owned negatives for the
   20 most-used skills in `tests/routing/fixtures.json` (starting with
   website-builder, page-builder, seo, seo-audit, deploy, i18n, blog-writer,
   accessibility-audit, design-quality-score, ecommerce). T2_cov 1/62 → 20/62 lifts
   the T2 mean from 0.7405 to about 0.817 and Readiness from 59.6 to about 62.7.
   Add at least one positive for each of the 32 skills with none.
2. **Declare the real validator set.** `chwezi-engine-agents/catalog/engines.yaml`
   declares three validators; the engine's own CI runs seven checks plus hook tests
   and pytest. Add `validate-skill-contracts.py`, `validate-search-doctrine.py`,
   `check-vendored-detector.py` and `validate-slop-pack.mjs` so T1 measures what
   the engine actually gates (engine-agents change; owner approval required).
3. **Worked artefacts for every output type** under `examples/`: a multi-page
   reference site with committed render, a11y and performance reports; a filled
   intake brief; a sample SEO and performance audit report; a hand-over pack; a
   worked blog article with its source register; a landing page; a bilingual
   English/Kiswahili route set; a catalogue page. Link each from its owning
   skill's `## Worked Example`.
4. **Finish normalisation.** Remove the `## Preserved Domain …` sections from the
   15 skills that still carry them (fold any unique rule into the contract or a
   reference); replace the generic "The task matches this domain" trigger in the
   10 affected skills, beginning with `skills/agency-ops/monthly-report/SKILL.md`.

## P1 — close the output-type gaps (target about 63–65)

5. **New skill `commerce/catalogue-lite`** (P1): static catalogue, product schema
   truth rules, enquiry/WhatsApp/mobile-money ordering hand-offs, stock and price
   disclaimers, with fixtures and a worked catalogue.
6. **Client intake entry point** (P1): a thin `orchestration/client-intake` skill
   over the existing questionnaire and strategy-brief templates, or explicit
   intake fixtures routing to `website-builder`.
7. **Hand-over pack template** (P1): `templates/handover-pack.md` consolidating the
   asset ownership register, credentials transfer (names only), runbooks,
   measurement baseline and support terms; referenced from `deploy` and
   `website-builder`.
8. **Language claim** (P1): in
   `skills/orchestration/africa-excellence/references/african-language-pack.md`,
   either add a Luganda native-copy route and review procedure or reclassify the
   eight languages without copy routes as layout-supported only; source or remove
   the speaker counts.
9. **Review the new-tab rule** (P1) in `skills/content-copy/blog-writer/SKILL.md`
   against the accessibility gate; if retained, require a visible and
   programmatic "opens in a new tab" cue.
10. **References for reference-less skills** (P1): `hospitality-website-product`
    (schema and booking-fallback templates), `retail-commerce-operating-system`,
    `cross-page-design-consistency-audit`.
11. **Currentness registers** (P1) for accessibility (WCAG version status) and
    tooling defaults (A/B, RUM, QA tool pins) under `docs/source-registers/`.

## P2 — hygiene and evidence beyond the cap (target above 65 only with evidence)

12. Move root session and audit files into `docs/` history, remove
    `static-website-starter.zip` from the root or document it; trim `AGENTS.md`
    phase history into `docs/`.
13. Rebalance taxonomy per `02-coverage-and-taxonomy.md`; declare or deduplicate
    the cross-engine near-pairs (`blog-writer`, native-copy skills,
    `update-claude-documentation`) in `evals/routing/ownership.yaml`.
14. Retire the 32 `legacy-guidance.md` files once their unique content is migrated.
15. Tier 3 behavioural runs for the eight output types when spend is authorised;
    these, not further prose, are what can move Readiness past its 70 ceiling and
    the published score past 65.
16. Correct the portfolio routing table's statement that this engine embeds
    `proposal-skills` (no submodule exists at HEAD), or restore the submodule.
