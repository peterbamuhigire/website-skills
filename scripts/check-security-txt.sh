#!/usr/bin/env bash
# check-security-txt.sh - validates RFC 9116 security.txt in a built site.
#
# Usage:
#   bash .claude/skills/scripts/check-security-txt.sh <dist-dir>
#
# Exit codes:
#   0 - security.txt exists and passes the engine baseline
#   1 - missing or invalid security.txt
#   3 - prerequisite missing

set -euo pipefail

DIST_DIR="${1:-dist}"
FILE="$DIST_DIR/.well-known/security.txt"
REPORT="reports/security/security-txt.txt"
mkdir -p "$(dirname "$REPORT")"

[ -d "$DIST_DIR" ] || { echo "check-security-txt: $DIST_DIR not found" >&2; exit 3; }

FAIL=0
WARN=0

log() { echo "$1" | tee -a "$REPORT"; }
fail() { log "FAIL $1"; FAIL=1; }
warn() { log "WARN $1"; WARN=1; }
pass() { log "PASS $1"; }

: > "$REPORT"
log "# security.txt audit - $(date -u +%Y-%m-%dT%H:%M:%SZ)"
log "File: $FILE"

if [ ! -f "$FILE" ]; then
    fail "missing /.well-known/security.txt"
    echo "check-security-txt: FAIL - see $REPORT" >&2
    exit 1
fi

if grep -qiE '(\{[^}]+\}|TODO|TBD|example\.com|your-domain|yourdomain|security@example)' "$FILE"; then
    fail "placeholder value found"
fi

CONTACT_COUNT=$(grep -ciE '^Contact:[[:space:]]*[^[:space:]]+' "$FILE" || true)
if [ "$CONTACT_COUNT" -lt 1 ]; then
    fail "Contact field is required"
else
    pass "Contact field present ($CONTACT_COUNT)"
fi

while IFS= read -r contact; do
    value="${contact#Contact:}"
    value="$(echo "$value" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
    if ! echo "$value" | grep -qE '^(mailto:|https://|tel:)'; then
        fail "Contact must be a URI using mailto:, https://, or tel: ($value)"
    fi
done < <(grep -iE '^Contact:' "$FILE" || true)

EXPIRES_COUNT=$(grep -ciE '^Expires:[[:space:]]*[^[:space:]]+' "$FILE" || true)
if [ "$EXPIRES_COUNT" -ne 1 ]; then
    fail "Expires field must appear exactly once"
else
    EXPIRES_VALUE=$(grep -iE '^Expires:' "$FILE" | head -1 | sed 's/^[^:]*:[[:space:]]*//; s/[[:space:]]*$//')
    if ! echo "$EXPIRES_VALUE" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}[Tt][0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?[Zz]$'; then
        fail "Expires must be RFC3339 UTC format, e.g. 2026-12-31T23:59:00Z"
    else
        if date -u -d "$EXPIRES_VALUE" +%s >/tmp/security-txt-expires.$$ 2>/dev/null; then
            EXPIRES_EPOCH=$(cat /tmp/security-txt-expires.$$)
            rm -f /tmp/security-txt-expires.$$
            NOW_EPOCH=$(date -u +%s)
            MAX_EPOCH=$(( NOW_EPOCH + 366 * 24 * 60 * 60 ))
            if [ "$EXPIRES_EPOCH" -le "$NOW_EPOCH" ]; then
                fail "Expires is in the past ($EXPIRES_VALUE)"
            elif [ "$EXPIRES_EPOCH" -gt "$MAX_EPOCH" ]; then
                warn "Expires is more than 366 days in the future; refresh annually"
                pass "Expires is valid and future"
            else
                pass "Expires is valid and future"
            fi
        else
            fail "Expires could not be parsed by system date ($EXPIRES_VALUE)"
        fi
    fi
fi

if grep -qiE '^Canonical:' "$FILE"; then
    while IFS= read -r canonical; do
        value="${canonical#Canonical:}"
        value="$(echo "$value" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
        if ! echo "$value" | grep -qE '^https://[^[:space:]]+/.well-known/security\.txt$'; then
            fail "Canonical must be an https URL ending in /.well-known/security.txt ($value)"
        fi
    done < <(grep -iE '^Canonical:' "$FILE" || true)
    pass "Canonical field checked"
else
    warn "Canonical field missing; include it for multi-host clarity"
fi

for field in Policy Encryption Acknowledgments Hiring; do
    if grep -qiE "^$field:" "$FILE"; then
        while IFS= read -r line; do
            value="${line#*:}"
            value="$(echo "$value" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
            if ! echo "$value" | grep -qE '^https://[^[:space:]]+$'; then
                fail "$field must be an https URL ($value)"
            fi
        done < <(grep -iE "^$field:" "$FILE" || true)
        pass "$field field checked"
    fi
done

if grep -qiE '^Policy:' "$FILE"; then
    pass "Policy field present"
else
    fail "Policy field is required by this engine so researchers see disclosure scope"
fi

if [ "$FAIL" -ne 0 ]; then
    echo "check-security-txt: FAIL - see $REPORT" >&2
    exit 1
fi

if [ "$WARN" -ne 0 ]; then
    echo "check-security-txt: PASS with warnings - see $REPORT"
else
    echo "check-security-txt: PASS"
fi
