#!/usr/bin/env bash
# slop-scan.sh: design-quality slop scan of a built site (M10-11-T02).
#
# A thin wrapper over the design engine's chwezi-slop detector. The website
# engine keeps no rule engine of its own: the detector's registry supplies the
# font, colour, motion and layout rules, and quality/slop-rules.website.json
# supplies the website copy patterns from
#   skills/quality-gates/design-quality-score/references/banned-patterns.md
# (so a pattern added there is enforced once it is added to the pack).
#
# The detector is the hash-checked copy in scripts/vendor/chwezi-slop/
# (VENDOR.json). CHWEZI_SLOP_DETECTOR may point at a local chwezi-design-engine
# checkout instead; the vendored hash check is then skipped and recorded.
#
# Runs:
#   node <detector>/cli.mjs --json --tier deep --fail-on warning \
#        --extra-rules quality/slop-rules.website.json <dist>
# plus one --mode run per visitor mode when the strategy-brief artefact
# declares per-page visitor_mode (STRATEGY_BRIEF, default
# project-artifacts/strategy-brief.json).
#
# Usage:
#   bash scripts/slop-scan.sh [dist-dir]
#
# Outputs (under $REPORTS_DIR/design-quality, default ./reports/design-quality):
#   slop.json      canonical JSON report (detector report shape)
#   slop-scan.md   Markdown rendering of slop.json
#
# Exit codes:
#   0  no blocking findings (advisory findings never block)
#   1  blocking findings (block or warning severity)
#   5  prerequisite missing or NOT_ASSESSED: no dist directory, no Node >= 18,
#      vendored detector missing or tampered, invalid pack, or a detector
#      operational failure. Never treated as clean.
# The former per-family codes 2-4 are retired (decision record
# project-log/decisions/2026-09-29-slop-scan-exit-contract.md).

set -uo pipefail

ROOT="$(pwd)"
ENGINE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="${1:-$ROOT/dist}"
REPORTS_DIR="${REPORTS_DIR:-$ROOT/reports}/design-quality"
mkdir -p "$REPORTS_DIR"

not_assessed() {
  local reason="$1"
  local json_reason="${reason//\\/\\\\}"
  json_reason="${json_reason//\"/\\\"}"
  printf '{\n  "tool": "chwezi-slop",\n  "wrapper": "website-skills scripts/slop-scan.sh",\n  "status": "NOT_ASSESSED",\n  "reason": "%s",\n  "findings": [],\n  "exit_code": 5\n}\n' "$json_reason" > "$REPORTS_DIR/slop.json"
  {
    echo "# Slop-Scan Report"
    echo ""
    echo "Scanned: $DIST_DIR"
    echo ""
    echo "## Status"
    echo ""
    echo "**NOT_ASSESSED** (exit 5): $reason"
    echo ""
    echo "This is not a pass. Fix the prerequisite and re-run."
  } > "$REPORTS_DIR/slop-scan.md"
  echo "slop-scan: NOT_ASSESSED: $reason" >&2
  exit 5
}

if [[ ! -d "$DIST_DIR" ]]; then
  not_assessed "dist directory not found at $DIST_DIR"
fi

if ! command -v node >/dev/null 2>&1; then
  not_assessed "Node.js is not installed (the chwezi-slop detector needs Node 18 or later)"
fi
NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]' 2>/dev/null || echo 0)"
if (( NODE_MAJOR < 18 )); then
  not_assessed "Node.js $NODE_MAJOR is too old (the chwezi-slop detector needs Node 18 or later)"
fi

node "$ENGINE_DIR/scripts/slop-scan-run.mjs" "$DIST_DIR" "$REPORTS_DIR"
CODE=$?
case "$CODE" in
  0) echo "slop-scan: PASS. Report: $REPORTS_DIR/slop-scan.md" ;;
  1) echo "slop-scan: FAIL (blocking findings). Report: $REPORTS_DIR/slop-scan.md" ;;
  5) echo "slop-scan: NOT_ASSESSED. Report: $REPORTS_DIR/slop-scan.md" ;;
  *) echo "slop-scan: unexpected exit $CODE from slop-scan-run.mjs; treated as NOT_ASSESSED" >&2; CODE=5 ;;
esac
exit "$CODE"
