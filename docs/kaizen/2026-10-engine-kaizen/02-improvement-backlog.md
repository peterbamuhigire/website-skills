# Improvement backlog

Changes are limited to small, testable fixes supported by the baseline. The sequence starts with a committed evidence baseline; each accepted implementation item will be committed separately. The cycle is capped at ten kept changes.

| ID | Priority | Evidence-backed change | Acceptance evidence | Status |
|---|---|---|---|---|
| WSK-01 | P0 | Change the accessibility runner to create a browser context and page using the Playwright browser-context API, and close the context on success and error. | Unit regression tests for normal and thrown-error paths; exact locked a11y gate scans the clean and deliberately defective fixtures. | Planned |
| WSK-02 | P0 | Make SRI inspection parse HTML asset references so canonical URLs are not treated as executable/style assets; preserve failure for external scripts/styles without integrity metadata. | Isolated pass/fail parser fixtures; security SRI subcheck against the clean sample site. | Planned |
| WSK-03 | P1 | Add bounded guidance for a static catalogue with seller-mediated enquiry and manual settlement, including explicit seller-owned destinations and evidence needed before enabling contact/payment. | Three positive and two owned-negative ecommerce routing fixtures; route smoke and tests. | Planned |
| WSK-04 | P1 | Refresh the overdue Google AI Search claim only to the scope stated by the current official Google Search guide. | Currentness validator passes; source URL, access date, claim scope, and next review recorded. | Planned |
| WSK-05 | P1 | Refresh the overdue model-currentness entry using official Anthropic model/deprecation sources and separately record the Codex assignment check. | Currentness records identify model IDs, dates, current assignment, availability limits and retain/change decision; no policy is changed. | Planned |
| WSK-06 | P2 | Re-run normal, failure, full-suite and registered marketplace checks; record release blockers and size counts. | Full validators and practitioner flows recorded; 5,000-entry cap preserved; remaining NOT_ASSESSED evidence explicit. | Planned |

## Out of scope and retained blockers

- Do not force-upgrade locked QA dependencies. The exact available Lighthouse CI version remains 0.15.1 and its tree reports high advisories. Registry metadata and GitHub advisory pages were checked; an upstream-compatible path is not established. The security release gate remains blocked until a compatible, supported dependency set is available and scanned.
- Do not weaken the configured 2,000 ms lab LCP budget to match field CWV thresholds. Optimize the fixture or retain the measured lab failure. Field Core Web Vitals remain NOT_ASSESSED.
- Do not claim edge headers from local preview checks. A staging/edge verification is unavailable; keep that release gate open.
- Do not claim visual QA passed; required capture/structure specs are absent.
- Do not rewrite privacy/legal text without jurisdiction-specific legal review and a clause-by-clause source check.
- Do not add live contacts, prices, payment providers, product stock, or business claims to synthetic tasks.
- No design doctrine, broad refactor, cross-engine edits, deletion, public marketplace submission, deployment, or push.
