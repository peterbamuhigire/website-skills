# Decision: Go-to-market skills (local acquisition, referrals, niche, delivery automation)

- **Date:** 2026-06-13
- **Status:** Accepted
- **Phase:** Post-roadmap (operational capability addition)
- **Driver:** A Reddit post on modern web-design-studio go-to-market was mapped
  against the engine; 6 of 10 themes were already covered, 4 were gaps. Closed
  the gaps with researched skills.

## Summary

Ran a 4-cohort digital-research-engine wave (sources retained in the research
report) and built the agency-ops go-to-market layer the engine lacked:

- New skill `local-in-person-acquisition` (the "go in person" channel).
- New skill `referral-program` (generous, systematic client referrals).
- New skill `delivery-automation` (own tooling / productized delivery).
- Enhanced `agency-positioning` with a niche-down selection rubric.

## Deliverables

- `skills/agency-ops/local-in-person-acquisition/` — SKILL.md + 5 references.
- `skills/agency-ops/referral-program/` — SKILL.md + 5 references.
- `skills/agency-ops/delivery-automation/` — SKILL.md + 5 references.
- `skills/agency-ops/agency-positioning/references/niche-selection-rubric.md` and
  `niche-positioning-sources.md`; SKILL.md workflow/use/reference updates.
- Research report: `docs/plans/2026-06-13-reddit-webdesign-gtm-research-report.md`.
- Updated `CLAUDE.md` (agency-ops 11→14), `glossary.md`, `AGENTS.md`.

## Rationale

- Niche-down was added to `agency-positioning` rather than a new skill because
  positioning already lives there; sector-strategies stays the design-side half.
- Each skill carries a `sources.md` with attribution and explicit UNVERIFIED
  flags per the digital-research-engine mandate.

## Risks

- Many GTM statistics are vendor-blog "industry-reported" claims, not primary
  research; flagged as UNVERIFIED so operators don't quote them as fact.
- AI-speed optimism in the source post contradicts the strongest 2025 evidence
  (METR, Faros, Stack Overflow). `delivery-automation` states this plainly rather
  than repeating the hype — a deliberate, defensible stance.

## Follow-up

- Optional Wave 2 gap-fill if a client engagement needs deeper local-market data.
- Re-run `skill-safety-audit` if these skills change materially (this build passed).
