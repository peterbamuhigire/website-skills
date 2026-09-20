#!/usr/bin/env bash
# banned-phrase-scan.sh — code-enforced banned-phrase gate for DRAFT copy.
#
# Scans a file or directory of draft text (markdown, plain text, HTML —
# anything before a `dist/` build exists) for the regex-checkable phrases
# catalogued in
#   skills/content-copy/brand-voice/references/banned-phrases.md
# under its "## Regex-checkable phrases" section. That file is the single
# source of truth for the phrase list; this script parses it rather than
# hardcoding a separate copy, so the two cannot drift apart.
#
# This is the pre-build counterpart to scripts/slop-scan.sh, which enforces
# an overlapping (not identical) list against RENDERED dist/ HTML as part
# of the design-quality gate. Run this one on drafts before a build exists;
# slop-scan.sh still runs post-build as the final floor.
#
# Usage:
#   bash scripts/banned-phrase-scan.sh <file-or-dir> [file-or-dir ...]
#
# Exit codes:
#   0 — no banned phrases found
#   1 — one or more banned phrases found
#   2 — prerequisite missing (target not found, phrase list not found)

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SKILLS_DIR:-$(cd -- "$SCRIPT_DIR/.." && pwd)}"
PHRASE_FILE="${BANNED_PHRASE_FILE:-$SKILLS_DIR/skills/content-copy/brand-voice/references/banned-phrases.md}"

if [[ $# -eq 0 ]]; then
  echo "banned-phrase-scan: usage: bash scripts/banned-phrase-scan.sh <file-or-dir> [...]" >&2
  exit 2
fi

[[ -f "$PHRASE_FILE" ]] || { echo "banned-phrase-scan: phrase list not found at $PHRASE_FILE" >&2; exit 2; }

for target in "$@"; do
  [[ -e "$target" ]] || { echo "banned-phrase-scan: target not found: $target" >&2; exit 2; }
done

# Extract regex patterns from the "## Regex-checkable phrases" section only
# (stop before "## Judgment-only patterns"). Each entry is a top-level
# bullet whose pattern is the first backtick-delimited span on the line:
#   - `pattern here` — description
PATTERNS=()
in_section=0
while IFS= read -r line; do
  if [[ "$line" == "## Regex-checkable phrases" ]]; then
    in_section=1
    continue
  fi
  if [[ $in_section -eq 1 && "$line" == "## "* ]]; then
    break
  fi
  if [[ $in_section -eq 1 && "$line" =~ ^-\ \`([^\`]+)\` ]]; then
    PATTERNS+=("${BASH_REMATCH[1]}")
  fi
done < "$PHRASE_FILE"

if [[ ${#PATTERNS[@]} -eq 0 ]]; then
  echo "banned-phrase-scan: no patterns parsed from $PHRASE_FILE — refusing to run an empty scan" >&2
  exit 2
fi

FAIL=0
HITS=0
for target in "$@"; do
  # Build the file list: the target itself if it's a file, or every
  # .md/.txt/.html file under it if it's a directory.
  if [[ -f "$target" ]]; then
    files=("$target")
  else
    mapfile -t files < <(find "$target" -type f \( -name '*.md' -o -name '*.txt' -o -name '*.html' -o -name '*.htm' \) 2>/dev/null)
  fi

  for f in "${files[@]}"; do
    for pattern in "${PATTERNS[@]}"; do
      while IFS=: read -r lineno match; do
        echo "FAIL $f:$lineno — matches /$pattern/i — \"$match\""
        HITS=$((HITS+1))
        FAIL=1
      done < <(grep -nEi "$pattern" "$f" 2>/dev/null | sed -E "s/^([0-9]+):(.*)$/\1:\2/" || true)
    done
  done
done

if [[ $FAIL -ne 0 ]]; then
  echo "banned-phrase-scan: FAIL — $HITS banned-phrase hit(s). See skills/content-copy/brand-voice/references/banned-phrases.md" >&2
  exit 1
fi
echo "banned-phrase-scan: PASS — 0 hits across ${#PATTERNS[@]} pattern(s)."
