#!/usr/bin/env bash
# test-banned-phrase-scan.sh — repeatable test for banned-phrase-scan.sh
# against real dirty and clean text fixtures.
#
# Run: bash scripts/test-banned-phrase-scan.sh

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SCAN="$SCRIPT_DIR/banned-phrase-scan.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

PASS_COUNT=0
FAIL_COUNT=0

check() {
  local name="$1" expected="$2" actual="$3"
  if [[ "$actual" == "$expected" ]]; then
    echo "PASS — $name (expected exit $expected, got $actual)"
    PASS_COUNT=$((PASS_COUNT+1))
  else
    echo "FAIL — $name (expected exit $expected, got $actual)"
    FAIL_COUNT=$((FAIL_COUNT+1))
  fi
}

cat > "$TMP/dirty.md" <<'EOF'
# Welcome to our Agency

In today's fast-paced digital world, businesses need a game-changer.
We're passionate about cutting-edge, world-class solutions.
No fluff, just results — Excited to share our revolutionary approach.
EOF

cat > "$TMP/clean.md" <<'EOF'
# Bookkeeping for Kampala retailers

We reconcile your till receipts against your bank statement every Friday.
Fixed fee, no surprise invoices at month end. Ask about our onboarding call.
EOF

set +e
bash "$SCAN" "$TMP/dirty.md" >/dev/null 2>&1
dirty_code=$?
bash "$SCAN" "$TMP/clean.md" >/dev/null 2>&1
clean_code=$?
bash "$SCAN" "$TMP" >/dev/null 2>&1
dir_code=$?
bash "$SCAN" "$TMP/does-not-exist.md" >/dev/null 2>&1
missing_code=$?
bash "$SCAN" >/dev/null 2>&1
no_args_code=$?
set -e

check "real AI-slop draft — FAIL (exit 1)" 1 "$dirty_code"
check "real clean client-specific draft — PASS (exit 0)" 0 "$clean_code"
check "directory mode finds the dirty file — FAIL (exit 1)" 1 "$dir_code"
check "missing target — prerequisite error (exit 2)" 2 "$missing_code"
check "no arguments — usage error (exit 2)" 2 "$no_args_code"

# Confirm actual hit count on the dirty fixture is non-trivial (>=5), so
# this isn't passing by accident on a near-empty pattern list.
hit_count=$(bash "$SCAN" "$TMP/dirty.md" 2>/dev/null | grep -c '^FAIL ' || true)
if [[ "$hit_count" -ge 5 ]]; then
  echo "PASS — dirty fixture produces >=5 hits (got $hit_count)"
  PASS_COUNT=$((PASS_COUNT+1))
else
  echo "FAIL — dirty fixture produced only $hit_count hits, expected >=5"
  FAIL_COUNT=$((FAIL_COUNT+1))
fi

echo ""
echo "$PASS_COUNT/$((PASS_COUNT+FAIL_COUNT)) passed"
[[ $FAIL_COUNT -eq 0 ]]
