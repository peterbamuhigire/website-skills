#!/usr/bin/env python3
r"""Fail on machine-specific absolute paths and on broken Markdown relative links (WSK2-05).

Two checks over the engine checkout, using only the standard library:

1. Machine-specific absolute paths are findings: a user-profile path (`X:\Users\<name>`,
   `/Users/<name>/`, `/home/<user>/`) or the local web-server folder name `wamp64`. Conventional
   system paths used as examples or test data (`C:\Program Files\...`, `C:\temp\...`) are not. Active content (everything not listed as history) may carry
   none. History documents and client prompts keep their wording, but each file is held to a
   no-increase ceiling in `quality/portable-references-policy.json`, so the count can only fall.
   A line containing the marker `portable-ok` is skipped, for the rare line that must quote a path.
2. Every Markdown relative link and image must resolve to a file or folder inside the checkout.
   Links that leave the checkout (a relative link into a sibling engine) are findings, because a
   client project checks out this engine alone. Fenced code, inline code, URLs, anchors, `mailto:`
   and template placeholders are not links.

Cross-engine references are written as skill names resolved through the engine-routing table
(for example `chwezi-design-engine:form-ux-design`), never as paths.

Usage:
    python scripts/check_portable_references.py [--root DIR] [--policy FILE] [--measure]

`--measure` prints the current per-file counts for history files as JSON, to maintain the ceilings;
it never edits the policy. Exit codes: 0 clean; 1 findings; 5 policy unreadable.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLICY = ROOT / "quality" / "portable-references-policy.json"
ALLOW_MARKER = "portable-ok"
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".mjs", ".js", ".sh", ".ps1", ".html", ".css", ".txt", ".toml", ".cfg", ".ini"}
ALWAYS_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache", ".lighthouseci"}

# A user-profile path on a Windows drive (the letter is not the tail of a longer word, so `https://`
# and `Note:/` are not paths), a POSIX home folder, or the local web-server folder name.
PATH_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s\"'`]+"  # portable-ok
    r"|/home/[A-Za-z0-9._-]+/"  # portable-ok
    r"|/Users/[A-Za-z0-9._-]+/"  # portable-ok
    r"|wamp64",  # portable-ok
    re.IGNORECASE,
)
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")
NOT_A_FILE = re.compile(r"^(?:[A-Za-z][A-Za-z0-9+.-]*:|#|//)")
PLACEHOLDER = re.compile(r"[{}<>$*]")


def find_path_hits(text: str) -> list[tuple[int, str, str]]:
    """Return (line, kind, snippet) for each machine-specific path in the text."""
    hits = []
    for number, line in enumerate(text.splitlines(), 1):
        if ALLOW_MARKER in line:
            continue
        match = PATH_PATTERN.search(line)
        if match:
            start = max(0, match.start() - 20)
            hits.append((number, "machine-path", line[start : match.end() + 30].strip()))
    return hits


def find_link_problems(path: Path, text: str, root: Path) -> list[tuple[int, str, str]]:
    """Return (line, target, reason) for each Markdown relative link that does not resolve."""
    problems = []
    in_fence = False
    root = root.resolve()
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        scrubbed = re.sub(r"`[^`]*`", "", line)
        for match in LINK_PATTERN.finditer(scrubbed):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if not target or NOT_A_FILE.match(target) or PLACEHOLDER.search(target):
                continue
            file_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not file_part:
                continue
            resolved = (root / file_part.lstrip("/")) if file_part.startswith("/") else (path.parent / file_part)
            resolved = Path(os.path.normpath(resolved))
            if root != resolved and root not in resolved.parents:
                problems.append((number, target, "relative link leaves the checkout"))
            elif not resolved.exists():
                problems.append((number, target, "relative link does not resolve"))
    return problems


def is_history(rel: str, policy: dict) -> bool:
    return any(rel.startswith(prefix) for prefix in policy.get("history_prefixes", [])) or rel in policy.get("history_files", [])


def iter_files(root: Path, policy: dict):
    skip_prefixes = tuple(policy.get("skip_prefixes", []))
    skip_files = set(policy.get("skip_files", []))
    for directory, names, files in os.walk(root):
        names[:] = sorted(name for name in names if name not in ALWAYS_SKIP_DIRS)
        for name in sorted(files):
            path = Path(directory) / name
            rel = path.relative_to(root).as_posix()
            if rel.startswith(skip_prefixes) or rel in skip_files or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            yield rel, path


def scan(root: Path, policy: dict) -> dict:
    """Scan the checkout. Returns violations and the measured history counts."""
    root = root.resolve()
    violations: list[dict] = []
    history: dict[str, int] = {}
    ceilings = policy.get("history_ceilings", {})
    for rel, path in iter_files(root, policy):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (UnicodeDecodeError, OSError):
            continue
        hits = find_path_hits(text)
        if is_history(rel, policy):
            if hits:
                history[rel] = len(hits)
            ceiling = ceilings.get(rel, 0)
            if len(hits) > ceiling:
                violations.append({"file": rel, "line": hits[ceiling][0], "kind": "history-ceiling", "detail": f"{len(hits)} machine-specific paths exceed the recorded ceiling of {ceiling}: {hits[ceiling][2]}"})
        else:
            for line, kind, snippet in hits:
                violations.append({"file": rel, "line": line, "kind": kind, "detail": snippet})
        if path.suffix.lower() == ".md":
            for line, target, reason in find_link_problems(path, text, root):
                violations.append({"file": rel, "line": line, "kind": "broken-link", "detail": f"{reason}: {target}"})
    return {"violations": violations, "history": history}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--measure", action="store_true", help="print current history counts as JSON and exit 0")
    args = parser.parse_args()
    try:
        policy = json.loads(args.policy.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"portable-references: policy unreadable ({exc})", file=sys.stderr)
        return 5
    result = scan(args.root, policy)
    if args.measure:
        print(json.dumps(dict(sorted(result["history"].items())), indent=2))
        return 0
    for item in result["violations"]:
        print(f"{item['file']}:{item['line']}: {item['kind']}: {item['detail']}")
    history_total = sum(result["history"].values())
    if result["violations"]:
        print(f"portable-references: FAIL ({len(result['violations'])} findings)")
        return 1
    print(f"portable-references: PASS (no active machine paths, no broken links; {history_total} history-document paths held at their ceilings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
