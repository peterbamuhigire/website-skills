#!/usr/bin/env bash
# install-canonical-ci.sh — bootstrap the canonical CI pipeline into a client project.
#
# Copies the canonical workflow and the canonical npm scripts into a project
# using an explicitly resolved engine checkout. Running this is the one-time setup step
# that signs the project up for the engine's enforcement gates.
#
# Usage:
#   bash /path/to/website-skills/scripts/install-canonical-ci.sh <project-path> [engine-path]
#
# Idempotent. Re-running is safe; existing files are backed up to
# .engine-backup-<timestamp>/ before being overwritten.
#
# Exit codes:
#   0 — install complete
#   1 — project path invalid
#   2 — engine path is invalid
#   3 — user declined to overwrite existing workflow

set -euo pipefail

PROJECT="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ENGINE="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS="${2:-$DEFAULT_ENGINE}"
if [ -z "$PROJECT" ] || [ ! -d "$PROJECT" ]; then
    echo "usage: install-canonical-ci.sh <project-path>" >&2
    exit 1
fi

if [ ! -f "$SKILLS/skills/manifest.yml" ] || [ ! -f "$SKILLS/templates/ci/website.yml" ]; then
    echo "install-canonical-ci: invalid engine path: $SKILLS" >&2
    exit 2
fi

TS=$(date -u +%Y%m%d-%H%M%S)
BACKUP="$PROJECT/.engine-backup-$TS"

backup_if_present() {
    local src="$1"
    if [ -e "$src" ]; then
        mkdir -p "$BACKUP"
        cp -R "$src" "$BACKUP/"
        echo "install-canonical-ci: backed up $src → $BACKUP/"
    fi
}

# 1. Workflow
mkdir -p "$PROJECT/.github/workflows"
backup_if_present "$PROJECT/.github/workflows/website.yml"
cp "$SKILLS/templates/ci/website.yml" "$PROJECT/.github/workflows/website.yml"
python "$SKILLS/scripts/validate-skill-registry.py"
echo "install-canonical-ci: workflow installed at .github/workflows/website.yml"

# 2. Lighthouse config
backup_if_present "$PROJECT/lighthouserc.json"
cp "$SKILLS/lighthouserc.json" "$PROJECT/lighthouserc.json"

# 3. Performance budgets
backup_if_present "$PROJECT/performance-budgets.json"
cp "$SKILLS/performance-budgets.json" "$PROJECT/performance-budgets.json"

# 4. Visual baseline stubs (directory contract only; actual baselines captured per project)
mkdir -p "$PROJECT/tests/visual"
cp -n "$SKILLS/tests/visual/baseline/README.md" "$PROJECT/tests/visual/baseline/README.md" 2>/dev/null || true
mkdir -p "$PROJECT/tests/visual/baseline"

# 5. Third-party allowlist (empty by default)
if [ ! -f "$PROJECT/.third-party-allowed" ]; then
    cat > "$PROJECT/.third-party-allowed" <<'EOF'
# Third-party asset allowlist.
# One origin per line. Add a hash-delimited one-line reason.
# The default is to ship with zero third-party runtime assets.
#
# Example:
# https://plausible.example.com  # self-hosted Plausible analytics
EOF
fi

# 6. security.txt starter (required by security-gate; replace placeholders)
mkdir -p "$PROJECT/public/.well-known"
if [ ! -f "$PROJECT/public/.well-known/security.txt" ]; then
    cp "$SKILLS/templates/security.txt" "$PROJECT/public/.well-known/security.txt"
fi
if [ ! -f "$PROJECT/docs/security-policy.md" ]; then
    mkdir -p "$PROJECT/docs"
    cp "$SKILLS/templates/security-policy.md" "$PROJECT/docs/security-policy.md"
fi

# 7. package.json scripts — if jq is present, merge; otherwise print instructions.
if command -v jq >/dev/null 2>&1 && [ -f "$PROJECT/package.json" ]; then
    TMP=$(mktemp)
    jq '.scripts += {
        "perf-gate": "bash ${WEBSITE_SKILLS_DIR}/scripts/perf-gate.sh",
        "a11y-gate": "bash ${WEBSITE_SKILLS_DIR}/scripts/a11y-gate.sh",
        "visual-qa": "bash ${WEBSITE_SKILLS_DIR}/scripts/visual-qa.sh",
        "security-gate": "bash ${WEBSITE_SKILLS_DIR}/scripts/security-gate.sh",
        "drift-check": "bash ${WEBSITE_SKILLS_DIR}/scripts/drift-check.sh",
        "design-score": "bash ${WEBSITE_SKILLS_DIR}/scripts/design-quality-score.sh",
        "engine-gates": "npm run perf-gate && npm run a11y-gate && npm run visual-qa && npm run security-gate"
    }' "$PROJECT/package.json" > "$TMP"
    backup_if_present "$PROJECT/package.json"
    mv "$TMP" "$PROJECT/package.json"
    echo "install-canonical-ci: package.json scripts merged"
else
    echo "install-canonical-ci: jq not found or no package.json — add these scripts manually:" >&2
    echo '  Set WEBSITE_SKILLS_DIR and call $WEBSITE_SKILLS_DIR/scripts/<gate>.sh.' >&2
    echo '  "engine-gates": "npm run perf-gate && npm run a11y-gate && npm run visual-qa && npm run security-gate"' >&2
fi

# 8. .gitignore additions
if [ -f "$PROJECT/.gitignore" ]; then
    for entry in 'reports/' '.engine-backup-*' '.lighthouseci/'; do
        grep -qxF "$entry" "$PROJECT/.gitignore" || echo "$entry" >> "$PROJECT/.gitignore"
    done
fi

cat <<EOF

install-canonical-ci: done.

Next steps in this project:
  1. npm i -D @lhci/cli @axe-core/cli @playwright/test serve jq
  2. Capture initial visual baselines once the first template is designed:
     npx playwright test --update-snapshots tests/visual/capture.spec.ts
  3. Replace placeholders in public/.well-known/security.txt and docs/security-policy.md.
  4. Commit .github/workflows/website.yml, lighthouserc.json, performance-budgets.json,
     .third-party-allowed, public/.well-known/security.txt, docs/security-policy.md,
     and any backup folder after reviewing.
  5. Configure GitHub secrets: DEPLOY_HOST, DEPLOY_USER, DEPLOY_KEY.
  6. Configure GitHub variables: DEPLOY_PATH, PRODUCTION_URL.
  7. Trigger the workflow and verify every gate runs.

Set the GitHub variable WEBSITE_SKILLS_DIR to the repository-relative engine checkout.
See skills/launch-ops/deploy/references/ci-troubleshooting.md for common issues.
EOF
