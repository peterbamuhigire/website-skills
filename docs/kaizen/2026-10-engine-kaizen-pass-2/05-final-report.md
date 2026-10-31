# Final report (pass 2)

## What changed

This pass found and fixed one critical defect, built the first maintained end-to-end worked deliverable, and added three validators so that the defects it found cannot return unnoticed. Nine backlog items were kept and none was reverted. Each is one commit. No file was deleted, no other engine was edited, and nothing was pushed.

The critical defect: the security gate's dependency-audit step failed open. When npm could not audit (no lockfile, registry unreachable) the gate printed `npm audit high=0 critical=0` and carried on. It now stops with exit 6, and nine tests run the real script against a stub `npm` to prove both the real outcomes and the five did-not-complete cases.

## Scores

Fresh judgement **(synthesis)** with the same ten dimensions as the frozen baseline. The 29 October final is shown for comparison; the baseline was lower than that final because the fresh observation found defects the previous pass had not measured, not because anything regressed.

| Dimension | 29 Oct final | Baseline (this pass) | Final | Reason for movement from baseline |
|---|---:|---:|---:|---|
| Doctrine | 70 | 70 | 72 | The router no longer carries machine paths; two release rules (portable references, source registers) are written into it and enforced in CI. No doctrine changed. |
| Taxonomy and routing | 50 | 48 | 54 | Precision at one 92.5% to 93.2%; the whole-site prompt reaches `website-builder` (rank 3 of 62); skills with three positives and two owned negatives 2 to 4. The copy-review prompt still routes to `launch-campaigns` and 30 skills have no positive fixture. |
| Skill depth | 65 | 62 | 64 | The security gate's failure behaviour and the language tiers are now specified. The static-catalogue page pattern is still missing. |
| Applied proof | 25 | 25 | 40 | A maintained five-page deliverable with brief, release record, rollback plan and a test that injects eleven defects. Still no maintained catalogue, bilingual or blog example, and no browser gate has passed on a real toolchain. |
| Standards currency | 60 | 52 | 66 | Every standards row re-verified with dated, stateful claims; a validator makes expiry fail CI. Privacy statutes are partial, one OWASP date is not assessed, the vendored detector now drifts, and the Lighthouse CI tree is unresolved. |
| Output readiness | 65 | 58 | 62 | The security gate cannot pass an audit that did not run; two static accessibility checks and a quieter hero lint. Browser gates, LCP and the dependency audit remain blockers. |
| Accessibility and inclusion | 55 | 50 | 56 | Static `lang` and zoom checks; the language claim now matches the engine. No assistive-technology or native-language review. |
| Production and handoff | 65 | 65 | 68 | A complete rollback plan that follows the real helper, with its local validation tested. No rehearsal, staging or hand-over pack. |
| Hygiene | 80 | 72 | 83 | 25 active machine paths removed and guarded; 0 of 624 relative links broken; expiry validator; the metadata gate's own pass fixture made honest. 47 history-document paths remain at ceilings; the vendored copy needs a re-sync. |
| Safety and integrity | 65 | 55 | 64 | The critical fail-open is fixed and tested. Dependency-audit, legal-review and mirror-sourced e-book provenance items remain open. |

Baseline raw = **55.7/100** (sum 557); capped `min(raw, 65)` = **55.7**. Final raw = **62.9/100** (sum 629); capped `min(raw, 65)` = **62.9**. The 29 October final was 60.0. No dimension is lower than its baseline. The 95 target is not met and is not claimed. These scores do not override blocked release gates.

## Kept changes

| ID | Commit | Change | Evidence |
|---|---|---|---|
| WSK2-01 (critical) | `f548bb3` | Security gate fails closed when npm audit does not complete | 5 of 9 new tests failed before; 9/9 after; real npm confirmed |
| WSK2-04 | `38c9bb1`, `bd71a48` | Design engine found by a configurable root; hash test made hermetic | 11 tests; default check now compares and reports drift |
| WSK2-07 | `0a28183` | Static `html lang` and zoom-safe viewport checks; honest pass fixture | 11 of 18 failed before; 18/18 after |
| WSK2-08 | `f936529` | Small marks are not hero candidates | 2 of 8 failed before; five warnings to none on the example |
| WSK2-05 | `0b29417` | Portable-reference validator and 25 path fixes | 27 tests; active findings 25 to 0; design routes checked 8 to 15 |
| WSK2-02 | `a63a05b` | Maintained five-page example with release record and rollback plan | 27 tests; 11 injected defects all caught, pinned to exit code and message |
| WSK2-03 | `af0ad1e` | Whole-site trigger and routing fixtures | precision at one 92.5% to 93.2%; full-coverage skills 2 to 4 |
| WSK2-06 | `e52de53` | Source-register expiry validator and standards re-verification | 21 tests; six overdue rows fixed; three stale facts corrected |
| WSK2-09 | `51931d2` | Language pack claims only what the engine can produce | 6/6 failed before; 6/6 after |

Evidence commits: `a62e078` (frozen baseline), `7133724` (backlog), then the experiment log, validation record, this report and the next-cycle file. Reverted: none.

## New automated checks

Four guards against recurrence, all in CI and the engine manifest or the suite: `scripts/check_portable_references.py`, `scripts/validate-source-registers.py`, `tests/test_security_gate_audit.py` (the real gate against a stub `npm`), and `tests/test_worked_service_site.py` (every recorded gate run for real, with injected defects).

## Release state

The worked example is **BLOCKED for release** on purpose: its `security.txt` gate fails on the placeholder domain, eight further gates are recorded as not assessed with reasons, and no owner, host, legal review or rollback rehearsal exists for a fictional business. For the engine itself the standing blockers from 29 October are unchanged: the Lighthouse CI dependency tree (15 high-severity package records, not re-audited), the 2,000 ms lab LCP of a font-using site, visual capture specs, staging-edge headers, and counsel review of privacy wording.

## Residual risk

- **Vendored detector drift (new, real).** The design engine committed new rules at 16:27 on 2026-10-31 (`7582bbf`). The default `check-vendored-detector.py` now exits 1 with `DRIFT` on three files on this host. CI has no sibling and reports `NOT_ASSESSED`. The copy needs a reviewed re-sync by the orchestrator after the design engine's cycle ends.
- **Legal and privacy.** The five statute checks are identifier-level; three rest on search summaries. The Nigeria NDPR naming is inconsistent across five files and is not edited.
- **Provenance.** One register record, `LOCAL_CARTER_EPUB_2026`, cites a local e-book file whose name carries a download-mirror marker and whose provenance the register already calls unresolved. Only the user-profile directory was removed from its locator; the filename was kept. The owner should decide whether that source stays.
- **Test host.** Real pytest and every browser gate could not run here; the 280 passing cases are under a documented stand-in and `unittest`.
- **Lexical routing.** Routing gains are a proxy, not live-model evidence.

## Branches

The repository started on `kaizen/2026-10` (18 commits ahead of `origin/main`, never pushed). This pass worked on `kaizen/2026-10-pass2`, created from that HEAD. The two uncommitted 29 October evidence files were left byte-identical throughout (blob hashes `71b11469bf8c294e1d871e424afd07e4b1f90c1a` and `12c49b5e0a4ba852a585676fd2d1bcac9dc5fda7`) and are in no commit of this pass. The last step of the pass switches the checkout back to `kaizen/2026-10`. Whether that succeeded is reported in the hand-off message, because it happens after this file is committed; the uncommitted files carry across the switch. Nothing was pushed, tagged or released.
