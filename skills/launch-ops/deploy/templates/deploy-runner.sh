#!/usr/bin/env bash
set -euo pipefail

: "${DEPLOY_HOST:?DEPLOY_HOST is required}"
: "${DEPLOY_USER:?DEPLOY_USER is required}"
: "${DEPLOY_PATH:?DEPLOY_PATH is required}"
: "${DEPLOY_KEY:?DEPLOY_KEY is required}"

test -d dist || { echo "deploy-runner: dist/ missing" >&2; exit 2; }
key_file=$(mktemp)
trap 'rm -f "$key_file"' EXIT
chmod 600 "$key_file"
printf '%s\n' "$DEPLOY_KEY" > "$key_file"
rsync -az --delete -e "ssh -i $key_file -o StrictHostKeyChecking=yes" dist/ "$DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PATH/"
