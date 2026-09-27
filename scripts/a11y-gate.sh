#!/usr/bin/env bash
# a11y-gate.sh — canonical accessibility gate.
#
# Runs axe-core against every primary route on a built static preview.
# Fails on any "serious" or "critical" violation. Writes full results to
# reports/a11y/. Intended to be called from the canonical CI pipeline and
# from any operator's local machine.
#
# Usage from a client project:
#   SKILLS_DIR=/path/to/website-skills bash /path/to/website-skills/scripts/a11y-gate.sh
#
# Exit codes:
#   0 — no serious or critical violations
#   1 — serious or critical violations found
#   3 — prerequisite missing
#   4 — no built output to serve

set -euo pipefail

ROOT="$(pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SKILLS_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
DIST_DIR="${DIST_DIR:-$ROOT/dist}"
REPORTS_DIR="${REPORTS_DIR:-$ROOT/reports}/a11y"
PORT="${A11Y_PORT:-4321}"
ROUTES_FILE="${ROUTES_FILE:-$SKILLS_DIR/performance-budgets.json}"

node "$SKILLS_DIR/scripts/require-locked-qa-tools.mjs" 'serve=serve' '@playwright/test=playwright' '@axe-core/playwright=-' || exit 3
SERVE_BIN="$ROOT/node_modules/.bin/serve"

[ -d "$DIST_DIR" ] || { echo "a11y-gate: $DIST_DIR not found. Build first." >&2; exit 4; }
[ -f "$ROUTES_FILE" ] || { echo "a11y-gate: $ROUTES_FILE not found" >&2; exit 3; }

mkdir -p "$REPORTS_DIR"

# Preview
echo "a11y-gate: starting preview on :$PORT"
"$SERVE_BIN" "$DIST_DIR" -l "$PORT" >"$REPORTS_DIR/preview.log" 2>&1 &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null || true' EXIT

for _ in $(seq 1 30); do
    if curl -sSf "http://localhost:$PORT/" >/dev/null 2>&1; then break; fi
    sleep 0.5
done

A11Y_BASE_URL="http://localhost:$PORT" \
ROUTES_FILE="$ROUTES_FILE" \
REPORTS_DIR="$REPORTS_DIR" \
node "$SKILLS_DIR/scripts/a11y-gate-runner.mjs"
