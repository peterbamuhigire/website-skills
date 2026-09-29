# Coverage and taxonomy

**Taxonomy & structure: 55 / 100 (judged).**

## Current structure

| Category | Skills | Assessment |
|---|---:|---|
| agency-ops | 14 | Grab-bag: agency commerce (positioning, sales, referral, retention) sits beside site artefacts (`policy-pages`, `email-sender`) and a marketing channel (`social-media`) |
| brand | 2 | Orphan-sized; brand visual identity lives in the design engine |
| build | 6 | Coherent; carries the core pipeline |
| commerce | 5 | Coherent but skewed to full-store and omnichannel scope |
| content-copy | 11 | Coherent; largest craft group |
| launch-ops | 4 | Coherent |
| meta | 3 | Not a domain group; two of three duplicate dev-engine skills |
| orchestration | 6 | Mixes the orchestrator, a product layer, a sector skill (hospitality) and a regional pattern layer (africa-excellence) |
| quality-gates | 6 | Coherent except `kaizen-engine-and-product-improvement`, which is an improvement loop, not a gate |
| seo-search | 3 | Coherent |
| ux-conversion | 2 | Orphan-sized |

Counts match `AGENTS.md` and `README.md` (62). `validate-skill-registry.py` passes.

## Named deficiencies

1. **Imbalance.** One group holds 23 % of skills (agency-ops, 14) while two hold
   two each. The 14-skill group is not mutually exclusive with `build`
   (`policy-pages`, `email-sender` produce site artefacts) or with the
   social-media engine (`social-media`).
2. **Missing first-class entry points for named output types.** Client intake
   exists only as `website-builder/references/intake-questionnaire-template.md`
   (255 lines) and `website-strategy-brief-template.md`; there is no intake skill,
   so an intake request routes to the full orchestrator. Landing pages have no
   owning skill (they route across `page-builder`, `long-form-sales-copy`,
   `launch-campaigns`). The hand-over pack has no single owner or template.
3. **No catalogue-commerce skill.** Nothing covers a static product catalogue with
   enquiry, WhatsApp or mobile-money ordering and no cart, which is a common
   East African small-business requirement. `mobile-money-ux.md` exists only as an
   africa-excellence reference.
4. **Sector coverage is one skill.** `hospitality-website-product` is the only
   sector product skill; other sectors are delegated to
   `design-system-skills:sector-strategies`, which covers presentation, not
   content, schema and conversion for the sector.
5. **Language coverage is asymmetric.** Native-copy skills exist for French and
   Kiswahili (plus `east-african-english`); the africa-excellence language pack
   names ten "first-class" African languages without native-copy routes.
6. **Router and taxonomy drift.** `AGENTS.md` lists `brand-style-guide` and
   `color-selection` among on-demand support skills without the
   `design-system-skills:` prefix used elsewhere; its "Phase 10/11/12" sections
   organise skills by history rather than by category.

## Proposed revised structure (judged)

- Split `agency-ops` into `agency-commercial` (positioning, offers, sales,
  referral, retention, local acquisition, monthly report) and move `policy-pages`
  and `email-sender` to `build`.
- Merge `brand` and `ux-conversion` into a `strategy-conversion` group, or keep
  them and add the missing intake and landing-page skills there.
- Move `kaizen-engine-and-product-improvement` to `launch-ops` (post-launch loop).
- Add `commerce/catalogue-lite` and `orchestration/client-intake` (or declare
  intake routes explicitly in fixtures).
- Reduce local `meta/skill-safety-audit` to a pointer stub, as already done for
  `meta/skill-writing`, since the dev engine's `skill-engine-audit` now carries the
  skill safety gate (`references/skill-safety-gate.md`, absorbed from the retired
  dev-engine `skill-safety-audit`).
