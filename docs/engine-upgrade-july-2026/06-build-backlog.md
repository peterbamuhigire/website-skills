# Concrete Build Backlog

| # | Artefact | Purpose | Acceptance criteria | Effort |
|---:|---|---|---|---|
| 1 | `skills/manifest.yml` | Canonical registry | Contains every skill, owner, category, dependencies, aliases, status, inputs/outputs and verification date; generated count is 59. | M |
| 2 | `scripts/validate-skill-registry.py` | Prevent routing drift | Fails on missing files, stale aliases, duplicate IDs, malformed frontmatter, absent acknowledgement and unresolved local links. | M |
| 3 | `templates/ci/website.yml` + `scripts/install-canonical-ci.sh` | Repair portability | Engine location is an explicit input; deploy runner path exists; workflow uses least privilege; fixture CI passes. | M |
| 4 | `fixtures/website-basic/` | Prove baseline flow | Builds and passes every gate locally/CI; includes intentional failure variants. | L |
| 5 | `fixtures/website-multilingual/` | Prove language flow | en/fr/sw route, hreflang, localized slugs, native-review records and screenshot baselines pass. | L |
| 6 | `fixtures/website-commerce/` | Prove commerce flow | Catalogue/cart/checkout mock, schema, analytics, security and performance evidence pass. | L |
| 7 | `docs/standards-register.md` | Currency governance | Every normative source has owner, scope, version, link, review cadence and next date. | S |
| 8 | `docs/relocation-map.md` | Resolve migrated design routing | Every old name maps to an external-engine locator or successor; all active references validate. | S |
| 9 | `templates/project-artifacts/` | Typed handoffs | Versioned templates/schemas for six core artifacts; each fixture consumes them. | M |
| 10 | `tests/gates/` | Validate gate behaviour | Pass/fail fixtures and report snapshots for all seven executable gates. | L |
| 11 | `docs/benchmark-programme.md` | Independent proof plan | Reviewer roles, score calibration, consent, publication and refresh rules defined. | M |
| 12 | `skills/*/*/examples/` | Worked outputs | Every skill has at least one realistic completed output or points to a shared fixture. | L |

Remove the committed `.pyc` in the same change as an ignore rule; record the removal normally. Do not bulk-rewrite legacy historical plans—label them historic and repair only active routes.

## Master ranking appendix

| Rank | Engine | Capped score | Verdict |
|---:|---|---:|---|
| 1/1 | website-skills | 65/100 | Prioritise contract integrity and fixtures before further topical expansion. |
