#!/usr/bin/env bash
# drift-check.sh - bounded documentation drift gate wrapper.
#
# The deterministic implementation lives in drift_check.py so the same
# file-list, parsing, and exit semantics run on Git Bash and CI Linux.
#
# Usage:
#   bash scripts/drift-check.sh [--strict]
#   DRIFT_AS_OF=YYYY-MM-DD bash scripts/drift-check.sh
#
# Exit codes:
#   0 - no blocking drift
#   1 - dead internal link
#   2 - removed deprecated entity reference
#   3 - dated framing
#   4 - banned term in strict mode
#   5 - SKILL.md over 500 lines
#   6 - duplicated guidance in strict mode
#   7 - forbidden construction in strict mode
#   8 - prerequisite or runner error
#   9 - bounded scope exceeded
#
# Optional environment:
#   SKILLS_DIR - engine root when called from a client project
#   REPORTS_DIR - report root (defaults to the current project's reports/)
#   DRIFT_AS_OF - explicit date for the deprecation-removal check

set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ENGINE_ROOT="${SKILLS_DIR:-$(cd -- "$SCRIPT_DIR/.." && pwd)}"
REPORT_ROOT="${REPORTS_DIR:-$(pwd)/reports}/drift"
PYTHON_BIN="${PYTHON_BIN:-python3}"
AS_OF_ARGS=()
if [[ -n "${DRIFT_AS_OF:-}" ]]; then
  AS_OF_ARGS=(--as-of "$DRIFT_AS_OF")
fi

exec "$PYTHON_BIN" "$SCRIPT_DIR/drift_check.py" \
  --root "$ENGINE_ROOT" \
  --reports-dir "$REPORT_ROOT" \
  "${AS_OF_ARGS[@]}" \
  "$@"
