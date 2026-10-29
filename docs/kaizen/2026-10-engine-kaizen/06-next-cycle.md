# Next cycle

The October fixes are complete within scope. The following work remains open and should be scheduled as separate evidence-backed changes.

| Priority | Remaining work | Entry condition / proof needed |
|---|---|---|
| P0 | Remediate and re-audit the Lighthouse CI dependency tree without force-upgrading into an unsupported range. | Maintainer-supported compatible versions or a reviewed alternative; exact lockfile audit must pass before release. Current official advisories and affected ranges must be rechecked at implementation time. |
| P0 | Optimize the five-page fixture to satisfy the unchanged 2,000 ms lab LCP assertion. | Controlled variants show custom-font use is required to reproduce the miss: font-free CSS passes, font-preloaded fallback remains over budget, and the full font-styled fixture is slower. Profile the font/render path and repeat the same configured profile; keep field CWV separate. |
| P1 | Add maintained visual structure/capture specs. | Deterministic local visual test must pass clean pages and detect a deliberate visual defect, with reports kept outside the checkout. |
| P1 | Verify response security headers on a staging edge. | Authorized staging URL and evidence for each configured header; local preview is not deployment proof. |
| P1 | Finish complete worked-example coverage and portfolio link/path audit. | Maintained full output type per routed workflow and automated scan for broken local references and machine-specific paths. Existing link/path portfolio baseline is NOT_ASSESSED. |
| P1 | Review privacy and policy references for the jurisdictions and processing actually in scope. | Claim-by-claim official legal sources and qualified counsel review. Do not treat the current identifier lookup as a compliance review. |
| P2 | Reassess model and runtime availability. | Official model release, active account/runtime catalogue and task-specific quality/cost/latency evidence; retain model-agnostic skills unless evidence supports change. |
| P2 | Re-run full routing and marketplace proof after any routing or manifest change. | Live runner routing remains NOT_ASSESSED; current lexical smoke and local native install/load are bounded evidence only. |

The executable immutable size gate now enforces 5,000 entries for both the full checkout and package-oriented distribution and verifies manifest parity, unreadable-directory failure, and symlink containment. Do not delete user content to meet it; additions require the same full-checkout and package count method.
