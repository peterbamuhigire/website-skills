#!/usr/bin/env bash
# rollback.sh - authority-bound rollback hook for the canonical CI pipeline.
#
# The caller binds approval to the exact target path and supplies a
# pre-provisioned known-hosts file. This helper never writes a private key
# under the operator's SSH directory and never accepts an unknown host key.
#
# Required environment:
#   DEPLOY_HOST, DEPLOY_USER, DEPLOY_KEY, DEPLOY_PATH
#   DEPLOY_KNOWN_HOSTS - existing runner-managed SSH known-hosts file
#   ROLLBACK_APPROVED=yes - explicit mutation authority
#   ROLLBACK_TARGET - must exactly equal DEPLOY_PATH
#   ROLLBACK_REASON - recorded in the local evidence log
#
# Optional environment:
#   RELOAD_SERVICE - nginx, apache2, httpd, or none (default: nginx)
#   SSH_CONNECT_TIMEOUT - positive integer seconds (default: 15)
#   ROLLBACK_VALIDATE_ONLY=1 - validate local inputs without remote access
#
# Exit codes:
#   0 - rollback succeeded or local validation passed
#   1 - rollback or recovery failed
#   3 - prerequisite, authority, or target validation failed

set -Eeuo pipefail

fail_prerequisite() {
    echo "rollback: $*" >&2
    exit 3
}

require_env() {
    local name="$1"
    [[ -n "${!name:-}" ]] || fail_prerequisite "$name missing"
}

for required in \
    DEPLOY_HOST DEPLOY_USER DEPLOY_KEY DEPLOY_PATH DEPLOY_KNOWN_HOSTS \
    ROLLBACK_APPROVED ROLLBACK_TARGET ROLLBACK_REASON; do
    require_env "$required"
done

[[ "$ROLLBACK_APPROVED" == "yes" ]] || fail_prerequisite "ROLLBACK_APPROVED must be exactly yes"
[[ "$ROLLBACK_TARGET" == "$DEPLOY_PATH" ]] || fail_prerequisite "ROLLBACK_TARGET must exactly equal DEPLOY_PATH"
[[ -r "$DEPLOY_KNOWN_HOSTS" ]] || fail_prerequisite "DEPLOY_KNOWN_HOSTS must name a readable existing file"

[[ "$DEPLOY_HOST" =~ ^[A-Za-z0-9._:-]+$ ]] || fail_prerequisite "DEPLOY_HOST contains unsupported characters"
[[ "$DEPLOY_USER" =~ ^[A-Za-z0-9._-]+$ ]] || fail_prerequisite "DEPLOY_USER contains unsupported characters"
[[ "$DEPLOY_PATH" =~ ^/([A-Za-z0-9._-]+/)*[A-Za-z0-9._-]+$ ]] || fail_prerequisite "DEPLOY_PATH must be an absolute, simple path"
case "$DEPLOY_PATH" in
    */../*|*/..|../*|..|*/./*|*/.|./*|.) fail_prerequisite "DEPLOY_PATH contains an unsafe path segment" ;;
esac
[[ "$DEPLOY_PATH" != "/" ]] || fail_prerequisite "DEPLOY_PATH may not be the filesystem root"
ROLLBACK_REASON_PATTERN='^[A-Za-z0-9][A-Za-z0-9._:/ -]{0,159}$'
[[ "$ROLLBACK_REASON" =~ $ROLLBACK_REASON_PATTERN ]] || fail_prerequisite "ROLLBACK_REASON contains unsupported characters"

RELOAD_SERVICE="${RELOAD_SERVICE:-nginx}"
case "$RELOAD_SERVICE" in
    nginx|apache2|httpd|none) ;;
    *) fail_prerequisite "RELOAD_SERVICE must be nginx, apache2, httpd, or none" ;;
esac

SSH_CONNECT_TIMEOUT="${SSH_CONNECT_TIMEOUT:-15}"
[[ "$SSH_CONNECT_TIMEOUT" =~ ^[1-9][0-9]*$ ]] || fail_prerequisite "SSH_CONNECT_TIMEOUT must be a positive integer"

if [[ "${ROLLBACK_VALIDATE_ONLY:-0}" == "1" ]]; then
    echo "rollback validation: PASS (authority and target inputs accepted; remote state NOT ASSESSED)"
    exit 0
fi
[[ "${ROLLBACK_VALIDATE_ONLY:-0}" == "0" ]] || fail_prerequisite "ROLLBACK_VALIDATE_ONLY must be 0 or 1"

LOG_DIR="reports/deploy"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/rollback-$(date -u +%Y%m%dT%H%M%SZ).log"

umask 077
KEY_FILE="$(mktemp "${TMPDIR:-/tmp}/website-rollback-key.XXXXXX")"
cleanup_key() {
    rm -f -- "$KEY_FILE"
}
trap cleanup_key EXIT
printf '%s\n' "$DEPLOY_KEY" > "$KEY_FILE"
chmod 600 "$KEY_FILE"

SSH=(
    ssh
    -o BatchMode=yes
    -o ConnectTimeout="$SSH_CONNECT_TIMEOUT"
    -o StrictHostKeyChecking=yes
    -o UserKnownHostsFile="$DEPLOY_KNOWN_HOSTS"
    -i "$KEY_FILE"
    -- "$DEPLOY_USER@$DEPLOY_HOST"
)

echo "rollback: starting target=$DEPLOY_PATH reason=$ROLLBACK_REASON" | tee "$LOG"

if ! PROBE="$("${SSH[@]}" bash -s -- "$DEPLOY_PATH" 2>>"$LOG" <<'REMOTE'
set -euo pipefail
target=$1

[ -d "$target" ] || { echo "target directory missing: $target" >&2; exit 1; }
[ -d "$target/releases" ] || { echo "release directory missing: $target/releases" >&2; exit 1; }
[ -L "$target/current" ] || { echo "current symlink missing: $target/current" >&2; exit 1; }
[ -L "$target/previous" ] || { echo "previous symlink missing: $target/previous" >&2; exit 1; }

resolve_release() {
    link=$1
    value=$(readlink -- "$link")
    if [[ "$value" = /* ]]; then
        candidate=$value
    else
        candidate=$target/$value
    fi
    resolved=$(readlink -f -- "$candidate")
    case "$resolved" in
        "$target"/releases/*) ;;
        *) echo "symlink escapes release root: $link -> $value" >&2; exit 1 ;;
    esac
    case "$resolved" in
        *[!A-Za-z0-9_./:-]*) echo "release target contains unsupported characters" >&2; exit 1 ;;
    esac
    [ -d "$resolved" ] || { echo "release target missing: $resolved" >&2; exit 1; }
    printf '%s\n' "$resolved"
}

current=$(resolve_release "$target/current")
previous=$(resolve_release "$target/previous")
[ "$current" != "$previous" ] || { echo "current and previous release are identical" >&2; exit 1; }
printf 'current=%s\nprevious=%s\n' "$current" "$previous"
REMOTE
)"; then
    echo "rollback: FAIL - remote target preflight failed; no mutation attempted" | tee -a "$LOG" >&2
    exit 1
fi

CURRENT_TARGET="$(printf '%s\n' "$PROBE" | sed -n 's/^current=//p')"
PREV_TARGET="$(printf '%s\n' "$PROBE" | sed -n 's/^previous=//p')"
[[ -n "$CURRENT_TARGET" && -n "$PREV_TARGET" ]] || {
    echo "rollback: FAIL - preflight returned incomplete release targets" | tee -a "$LOG" >&2
    exit 1
}
echo "rollback: current=$CURRENT_TARGET previous=$PREV_TARGET" | tee -a "$LOG"
LAST_SAFE_CURRENT="$CURRENT_TARGET"
LAST_SAFE_PREVIOUS="$PREV_TARGET"
echo "rollback: last-safe-current=$LAST_SAFE_CURRENT last-safe-previous=$LAST_SAFE_PREVIOUS" | tee -a "$LOG"

if ! "${SSH[@]}" bash -s -- "$DEPLOY_PATH" "$CURRENT_TARGET" "$PREV_TARGET" 2>>"$LOG" <<'REMOTE'
set -Eeuo pipefail
target=$1
current=$2
previous=$3
tmp=$(mktemp -d "$target/.rollback.XXXXXX")
swapped=0

restore() {
    status=$?
    if [ "$swapped" -eq 0 ]; then
        set +e
        ln -s -- "$current" "$tmp/restore-current" && mv -Tf -- "$tmp/restore-current" "$target/current"
        ln -s -- "$previous" "$tmp/restore-previous" && mv -Tf -- "$tmp/restore-previous" "$target/previous"
        set -e
    fi
    case "$tmp" in
        "$target"/.rollback.*) rm -rf -- "$tmp" ;;
        *) echo "refusing unsafe rollback temporary path: $tmp" >&2; status=1 ;;
    esac
    exit "$status"
}
trap restore EXIT

ln -s -- "$previous" "$tmp/current"
ln -s -- "$current" "$tmp/previous"
mv -Tf -- "$tmp/current" "$target/current"
mv -Tf -- "$tmp/previous" "$target/previous"
swapped=1
REMOTE
then
    echo "rollback: FAIL - symlink swap failed; recovery was attempted" | tee -a "$LOG" >&2
    exit 1
fi

verify_current() {
    "${SSH[@]}" bash -s -- "$DEPLOY_PATH" "$1" "$2" <<'REMOTE'
set -euo pipefail
target=$1
expected_current=$2
expected_previous=$3
actual_current=$(readlink -f -- "$target/current")
actual_previous=$(readlink -f -- "$target/previous")
[ "$actual_current" = "$expected_current" ]
[ "$actual_previous" = "$expected_previous" ]
REMOTE
}

recover_original() {
    "${SSH[@]}" bash -s -- "$DEPLOY_PATH" "$LAST_SAFE_CURRENT" "$LAST_SAFE_PREVIOUS" <<'REMOTE'
set -euo pipefail
target=$1
current=$2
previous=$3
tmp=$(mktemp -d "$target/.rollback-recovery.XXXXXX")
cleanup() {
    status=$?
    case "$tmp" in
        "$target"/.rollback-recovery.*) rm -rf -- "$tmp" ;;
        *) echo "refusing unsafe rollback recovery temporary path: $tmp" >&2; status=1 ;;
    esac
    exit "$status"
}
trap cleanup EXIT
ln -s -- "$current" "$tmp/current"
ln -s -- "$previous" "$tmp/previous"
mv -Tf -- "$tmp/current" "$target/current"
mv -Tf -- "$tmp/previous" "$target/previous"
REMOTE
}

recover_and_verify() {
    if ! recover_original 2>>"$LOG"; then
        echo "rollback: recovery FAILED - operator intervention required; last-safe state was current=$LAST_SAFE_CURRENT previous=$LAST_SAFE_PREVIOUS" | tee -a "$LOG" >&2
        return 1
    fi
    if ! verify_current "$LAST_SAFE_CURRENT" "$LAST_SAFE_PREVIOUS" 2>>"$LOG"; then
        echo "rollback: recovery verification FAILED - operator intervention required" | tee -a "$LOG" >&2
        return 1
    fi
    echo "rollback: recovery PASS - restored last-safe state current=$LAST_SAFE_CURRENT previous=$LAST_SAFE_PREVIOUS" | tee -a "$LOG"
}

if ! verify_current "$PREV_TARGET" "$CURRENT_TARGET" 2>>"$LOG"; then
    echo "rollback: FAIL - post-swap verification failed; restoring original symlinks" | tee -a "$LOG" >&2
    recover_and_verify || exit 1
    exit 1
fi

if [[ "$RELOAD_SERVICE" != "none" ]]; then
    if ! "${SSH[@]}" sudo -- systemctl reload "$RELOAD_SERVICE" 2>>"$LOG"; then
        echo "rollback: FAIL - service reload failed; restoring original symlinks" | tee -a "$LOG" >&2
        recover_and_verify || exit 1
        exit 1
    fi
else
    echo "rollback: service reload skipped by explicit RELOAD_SERVICE=none" | tee -a "$LOG"
fi

echo "rollback: PASS - current now points to $PREV_TARGET; see $LOG" | tee -a "$LOG"
