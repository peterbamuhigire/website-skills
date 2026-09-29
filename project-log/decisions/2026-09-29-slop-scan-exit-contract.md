# Decision: slop-scan rebuilt over the vendored chwezi-slop detector; exit contract 0/1/5

- **Date:** 2026-09-29
- **Status:** Accepted by the orchestrator under Peter Bamuhigire's delegated authority (29 Sep 2026); Peter's ratification pending before merge
- **Phase:** my-10-kaizen M10-11 (IM-03), extending the K5 website adapter (`eb3b05e`) and the Phase-11 slop decision (2026-04-16)
- **Change class:** runtime-configuration (threshold and contract change)

## Summary

`scripts/slop-scan.sh` no longer carries its own regex set. It wraps the design
engine's `chwezi-slop` detector (M10-09, design-system-skills `3fe84a6`), which
travels here as a hash-checked vendored copy in `scripts/vendor/chwezi-slop/`
(`VENDOR.json`, `scripts/check-vendored-detector.py`). The website copy patterns
moved out of the script into the data pack `quality/slop-rules.website.json`,
built from `banned-patterns.md`.

## Contract change

| Exit | Before | After |
|---|---|---|
| 0 | clean | no blocking findings (advisory findings are reported only) |
| 1 | banned headline, filler or transition | any `block` or `warning` finding (the scan runs `--fail-on warning`) |
| 2 | gradient or pure black | retired |
| 3 | declared, never emitted | retired |
| 4 | trust row | retired |
| 5 | dist directory missing | `NOT_ASSESSED`: no dist directory, no Node 18 or later, a missing or tampered vendored detector, an invalid pack or a detector operational failure |

Outputs: `reports/design-quality/slop.json` (canonical, detector report shape) is
new; `reports/design-quality/slop-scan.md` keeps its path and is rendered from
the JSON.

## Why the retired codes are safe to remove

No consumer distinguishes codes 2-4. `visual-qa.sh` maps any non-zero slop exit
to its own exit 3; `design-quality-score.sh` fails (exit 2) on any non-zero;
`hooks/quality-gate.js` skips only design-quality-score's exit 5 (no dist). Both
scripts now print a distinct `NOT_ASSESSED` message for slop exit 5, and neither
treats it as a pass.

## Consequences

- Client CI enforces banned primary fonts for the first time (0 to 1 checks).
- The first run on an existing client site may fail on rules the old scan did
  not have; `slop-rules.md` carries a migration note and the waiver format.
- Node 18 or later becomes a prerequisite of the scan; the client pipeline
  already runs Node 22. Without Node the scan exits 5, never 0.
- Families 4 (low-information hero), 5 (icon overuse) and 10 (colour discipline)
  were relabelled from "automatic block" to "review gate (`human_review`)"
  because no detector rule enforces them as blocking. The doctrine ban is
  unchanged. This is a truthfulness correction for Peter's review.

## Rollback

Restore `scripts/slop-scan.sh` from the commit before this decision. The vendored
folder, the pack and `scripts/slop-scan-run.mjs` are inert without it.

## Re-vendoring

`python -X utf8 scripts/check-vendored-detector.py --sync-from ../design-system-skills`,
run by the orchestrator and committed after a hash review. Never automatic. The
same files are registered in byte mode in
`chwezi-engine-agents/catalog/shared-assets.yaml`.
