#!/usr/bin/env bash
# check-sri.sh — check external executable/style assets for SRI metadata.
# Usage: bash scripts/check-sri.sh <dist-dir> [allowlist-file]
set -euo pipefail

exec python3 "$(dirname "$0")/check_sri.py" "${1:-dist}" "${2:-.third-party-allowed}"
