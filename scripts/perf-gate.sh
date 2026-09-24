#!/usr/bin/env bash
# perf-gate.sh — canonical performance gate for the website-skills engine.
#
# Runs Lighthouse CI against every primary route on a built static preview,
# asserts the thresholds in lighthouserc.json, checks route-level weight
# budgets in performance-budgets.json (every category, via
# scripts/route-weight-budget.mjs), and emits reports under reports/.
#
# Usage: SKILLS_DIR=/path/to/website-skills bash /path/to/website-skills/scripts/perf-gate.sh
#
# Exit codes:
#   0  — all gates passed
#   1  — Lighthouse threshold failure
#   2  — route weight budget exceeded, or a budgeted route was not built (NOT_ASSESSED blocks)
#   3  — tool prerequisite missing
#   4  — no built output to serve
#   5  — static HTML performance lint failed (scripts/html-perf-lint.mjs)
#
# Prerequisites (install once per project):
#   npm i -D @lhci/cli   (Node 18+ required for the weight walker and HTML lint)
#
# Lab profile: lighthouserc.json uses a deliberate low-end STRESS profile
# (WebPageTest '3G' network values, 300 ms RTT). It is not a median. INP is
# not measurable in Lighthouse navigation mode; TBT is the lab proxy and INP
# is enforced from field/RUM data (see skills/launch-ops/observability).

set -euo pipefail

ROOT="$(pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SKILLS_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
LHCI_CONFIG="${LHCI_CONFIG:-$SKILLS_DIR/lighthouserc.json}"
BUDGETS_FILE="${BUDGETS_FILE:-$SKILLS_DIR/performance-budgets.json}"
DIST_DIR="${DIST_DIR:-$ROOT/dist}"
REPORTS_DIR="${REPORTS_DIR:-$ROOT/reports}"
# PORT is only the placeholder host port in the generated Lighthouse CI URLs; LHCI serves DIST_DIR itself.
PORT="${PERF_GATE_PORT:-4321}"

command -v npx >/dev/null 2>&1 || { echo "perf-gate: npx not found" >&2; exit 3; }
command -v node >/dev/null 2>&1 || { echo "perf-gate: node not found" >&2; exit 3; }

[ -d "$DIST_DIR" ] || { echo "perf-gate: $DIST_DIR not found. Run the project build first." >&2; exit 4; }
[ -f "$LHCI_CONFIG" ] || { echo "perf-gate: lighthouserc.json missing at $LHCI_CONFIG" >&2; exit 3; }
[ -f "$BUDGETS_FILE" ] || { echo "perf-gate: performance-budgets.json missing at $BUDGETS_FILE" >&2; exit 3; }

mkdir -p "$REPORTS_DIR/lighthouse" "$REPORTS_DIR/bundle"

echo "perf-gate: running static HTML performance lint"
LINT_EXIT=0
node "$SKILLS_DIR/scripts/html-perf-lint.mjs" "$DIST_DIR" --report "$REPORTS_DIR/bundle/html-perf-lint.json" || LINT_EXIT=$?
if [ "$LINT_EXIT" -eq 3 ]; then echo "perf-gate: html-perf-lint usage error" >&2; exit 3; fi

# One node call resolves every budgeted route (templates such as /blog/[slug]/ use a
# representative built page), enforces each weight category, and writes the Lighthouse CI
# configuration for exactly those pages: staticDistDir = $DIST_DIR, one URL per route, and a
# per-route total-byte-weight assertion equal to the route budget.
GENERATED_CONFIG="$REPORTS_DIR/lighthouse/lighthouserc.generated.json"
echo "perf-gate: validating route weight budgets (HTML, CSS, JS, fonts, images, third-party scripts)"
BUDGET_EXIT=0
node "$SKILLS_DIR/scripts/route-weight-budget.mjs" \
    --dist "$DIST_DIR" \
    --budgets "$BUDGETS_FILE" \
    --allow "${THIRD_PARTY_ALLOWLIST:-$ROOT/.third-party-allowed}" \
    --report "$REPORTS_DIR/bundle/route-weight.json" \
    --emit-lhci-config "$GENERATED_CONFIG" \
    --lhci-base "$LHCI_CONFIG" \
    --port "$PORT" || BUDGET_EXIT=$?
case "$BUDGET_EXIT" in
    0|2|4) ;;
    *) echo "perf-gate: route-weight-budget prerequisite or budget-file error (exit $BUDGET_EXIT)" >&2; exit 3 ;;
esac

echo "perf-gate: running Lighthouse CI against $DIST_DIR"
LHCI_EXIT=0
npx --yes @lhci/cli autorun --config="$GENERATED_CONFIG" || LHCI_EXIT=$?

if [ "$LHCI_EXIT" -ne 0 ]; then
    echo "perf-gate: FAIL — Lighthouse thresholds not met. See $REPORTS_DIR/lighthouse/" >&2
    exit 1
fi
if [ "$BUDGET_EXIT" -eq 2 ]; then
    echo "perf-gate: FAIL — route weight budget exceeded." >&2
    exit 2
fi
if [ "$BUDGET_EXIT" -eq 4 ]; then
    echo "perf-gate: FAIL — a budgeted route was NOT_ASSESSED (not built); NOT_ASSESSED blocks release." >&2
    exit 2
fi
if [ "$LINT_EXIT" -ne 0 ]; then
    echo "perf-gate: FAIL — HTML performance lint findings. See $REPORTS_DIR/bundle/html-perf-lint.json" >&2
    exit 5
fi

echo "perf-gate: PASS — all routes within Lighthouse thresholds and weight budgets."
