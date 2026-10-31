# Date-gated checks

Two currentness validators fail once a recorded review date passes. This page lists the dates on which each one will start failing unless the sources behind it are re-verified. The README gives the short version in "Quality and improvement".

## How the dates work

- Moving a date needs a source check behind it. The register validator also rejects a review date that sits further from its verification date than the cadence allows: 45, 100 and 400 days for monthly, quarterly and annual rows.
- The dates below were read from the registers. Each was confirmed by running `validate-source-registers.py --as-of` on the day before and the day after; the error count steps up on the day shown.
- `validate-search-doctrine.py` has no `--as-of` option. Its date was confirmed by running it with a substituted current date.
- Re-checked on 2026-10-31 for the first row: `--as-of 2026-11-30` exits 0, and `--as-of 2026-12-01` exits 1 with 8 findings.

## Calendar

| First failing day | Records that reach their review date the day before | Validator |
|---|---|---|
| 2026-12-01 | `standards-currentness-2026-10-31.json` (the register and three claims) and four standards-table rows: Search, Lab tooling, Structured data, Data-protection statutes (2026-11-30) | `validate-source-registers.py` |
| 2026-12-06 | Seven claims in `search-ai-currentness-2026-09-05.json` (2026-12-05) | `validate-search-doctrine.py` and `validate-source-registers.py` |
| 2026-12-13 to 2026-12-26 | That register (2026-12-12), four of its claims (2026-12-14), six standards claims (2026-12-15), `performance-currentness-2026-09-23.json` (2026-12-23) and the claims of `performance-currentness-2026-09-25.json` (2026-12-25); each day-after run adds the records listed | `validate-source-registers.py` |
| 2027-01-30 | `performance-currentness-2026-09-25.json` (its register, 2027-01-29) | `validate-source-registers.py` |
| 2027-02-01 | Fourteen records (2027-01-31): seven quarterly standards-table rows (WCAG, WAI-ARIA, Application verification, Web risk awareness, Workflow security, Core Web Vitals, Privacy risk) and seven claims | `validate-source-registers.py` |
| 2027-03-24, 2027-09-06, 2027-09-24 | Four, one and one claims in the performance and search registers | `validate-source-registers.py` |
| 2027-11-01 | The annual RFC 9116 row and one standards claim (2027-10-31) | `validate-source-registers.py` |

## Other scheduled reviews

The next-cycle file, [`06-next-cycle.md`](kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md), also sets a monthly backlog review on 2026-11-30 and a full engine audit with the 65 cap on 2027-01-31.
