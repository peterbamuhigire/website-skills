#!/usr/bin/env bash
# security-gate.sh - canonical security + compliance gate.
#
# Orchestrates:
#   1. npm audit (dependency vulnerabilities)
#   2. check-security-headers.sh (HSTS, CSP, etc.)
#   3. check-security-txt.sh (public vulnerability disclosure route)
#   4. check-sri.sh (third-party asset integrity)
#   5. scan-secrets.sh (leaked credentials)
#   6. supply-chain-check.sh (lockfile, install scripts, typosquats)
#
# Usage:
#   bash .claude/skills/scripts/security-gate.sh
#
# Exit codes:
#   0 - all checks pass
#   1 - npm audit high/critical
#   2 - security header missing or misconfigured
#   3 - security.txt failure
#   4 - SRI failure
#   5 - secret detected
#   6 - prerequisite missing
#   7 - supply-chain failure

set -euo pipefail

ROOT="$(pwd)"
SKILLS_DIR="${SKILLS_DIR:-$ROOT/.claude/skills}"
DIST_DIR="${DIST_DIR:-$ROOT/dist}"
REPORTS_DIR="${REPORTS_DIR:-$ROOT/reports}/security"
mkdir -p "$REPORTS_DIR"

command -v jq >/dev/null 2>&1 || { echo "security-gate: jq required" >&2; exit 6; }

# 1. npm audit
echo "security-gate: npm audit"
AUDIT_JSON="$REPORTS_DIR/audit.json"
AUDIT_EXIT=0
npm audit --audit-level=high --json > "$AUDIT_JSON" || AUDIT_EXIT=$?
HIGH=$(jq '[.vulnerabilities[]?|select(.severity=="high")]|length' "$AUDIT_JSON" 2>/dev/null || echo 0)
CRIT=$(jq '[.vulnerabilities[]?|select(.severity=="critical")]|length' "$AUDIT_JSON" 2>/dev/null || echo 0)
echo "security-gate: npm audit high=$HIGH critical=$CRIT"
# Apply suppressions
SUPPRESSIONS_FILE="$ROOT/.audit-suppress.json"
if [ -f "$SUPPRESSIONS_FILE" ]; then
    IGNORED=$(jq --slurpfile sup "$SUPPRESSIONS_FILE" \
        '[.vulnerabilities[]?|select(.severity=="high" or .severity=="critical")
          |select([.via[]?.url] as $urls
                  | any($sup[][]; .id as $id | $urls|any(contains($id))))]|length' \
        "$AUDIT_JSON" 2>/dev/null || echo 0)
    HIGH=$(( HIGH - IGNORED > 0 ? HIGH - IGNORED : 0 ))
fi
if [ "$HIGH" -gt 0 ] || [ "$CRIT" -gt 0 ]; then
    echo "security-gate: FAIL - $CRIT critical, $HIGH high vulnerabilities" >&2
    exit 1
fi

# 2. Security headers (against preview for marketing sites; against staging for
# edge-configured headers, run separately)
echo "security-gate: security headers"
if [ -f "$SKILLS_DIR/scripts/check-security-headers.sh" ]; then
    bash "$SKILLS_DIR/scripts/check-security-headers.sh" "$DIST_DIR" || exit 2
fi

# 3. security.txt
echo "security-gate: security.txt"
if [ -f "$SKILLS_DIR/scripts/check-security-txt.sh" ]; then
    bash "$SKILLS_DIR/scripts/check-security-txt.sh" "$DIST_DIR" || exit 3
fi

# 4. SRI
echo "security-gate: SRI"
if [ -f "$SKILLS_DIR/scripts/check-sri.sh" ]; then
    bash "$SKILLS_DIR/scripts/check-sri.sh" "$DIST_DIR" "$ROOT/.third-party-allowed" || exit 4
fi

# 5. Secrets
echo "security-gate: secrets"
bash "$SKILLS_DIR/scripts/scan-secrets.sh" || exit 5

# 6. Supply chain
echo "security-gate: supply chain"
bash "$SKILLS_DIR/scripts/supply-chain-check.sh" || exit 7

{
    echo "# Security Gate Summary"
    echo ""
    echo "Run: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo ""
    echo "- npm audit: PASS (high=$HIGH critical=$CRIT)"
    echo "- Security headers: PASS"
    echo "- security.txt: PASS"
    echo "- SRI: PASS"
    echo "- Secrets scan: PASS"
    echo "- Supply chain: PASS"
} > "$REPORTS_DIR/summary.md"

echo "security-gate: PASS"
