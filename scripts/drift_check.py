#!/usr/bin/env python3
"""Run the bounded, deterministic documentation drift check.

The checker reads only Markdown files known to Git (tracked or explicitly
untracked and not ignored), applies a fixed repository scope, and uses stable
sorting and stable report content. It does not inspect client project files,
network resources, generated reports, book extractions, or a submodule.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


MAX_MARKDOWN_FILES = 600
MAX_TOTAL_BYTES = 16 * 1024 * 1024
SCOPE_EXCLUDED_PARTS = {
    ".git",
    "book-extractions",
    "dist",
    "node_modules",
    "proposal-skills",
    "reports",
}
REQUIRED_FILES = (
    "glossary.md",
    "docs/doc-style-guide.md",
    "docs/deprecation-policy.md",
)
DEPRECATION_EXCLUSIONS = {"glossary.md", "docs/deprecation-policy.md"}
DATED_FRAMING = re.compile(
    r"as of 20[0-9]{2}|the next quarter|recently,|at the time of writing|currently,",
    re.IGNORECASE,
)
BANNED_TERMS = re.compile(
    r"\b(?:best-in-class|state of the art|cutting-edge|synergy|holistic|robust|"
    r"leverage\s+\w+)\b",
    re.IGNORECASE,
)
FORBIDDEN_CONSTRUCTIONS = re.compile(
    r"It is important to note that|Please be aware|As discussed above|utilise|facilitate ",
)
BANNED_EXCLUSIONS = {
    "glossary.md",
    "docs/doc-style-guide.md",
    "prompts/new-project-kickstart.md",
}
FORBIDDEN_EXCLUSIONS = {
    "docs/doc-style-guide.md",
    "skills/content-copy/blog-writer/references/editorial-standards.md",
}
DATED_EXCLUSIONS = {
    "certification/exam.md",
    "glossary.md",
}
LINK_PATTERN = re.compile(r"\]\(([^)\r\n]+)\)")
DEPRECATION_ROW = re.compile(
    r"^\|\s*`([^`]+)`\s*\|[^|]+\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*"
    r"(\d{4}-\d{2}-\d{2})\s*\|"
)


@dataclass(frozen=True)
class Scope:
    root: Path
    files: tuple[Path, ...]
    total_bytes: int


def relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def in_scope_path(path: str) -> bool:
    parts = set(Path(path).parts)
    return not parts.intersection(SCOPE_EXCLUDED_PARTS)


def git_markdown_files(root: Path) -> list[Path]:
    command = [
        "git",
        "ls-files",
        "--cached",
        "--others",
        "--exclude-standard",
        "-z",
        "--",
        "*.md",
    ]
    result = subprocess.run(command, cwd=root, capture_output=True, check=True)
    names = result.stdout.decode("utf-8", errors="strict").split("\0")
    paths = []
    for name in sorted(filter(None, names)):
        if not name.lower().endswith(".md") or not in_scope_path(name):
            continue
        path = (root / Path(name)).resolve()
        if path.is_file() and path.is_relative_to(root.resolve()):
            paths.append(path)
    return paths


def collect_scope(root: Path) -> Scope:
    files = git_markdown_files(root)
    total_bytes = sum(path.stat().st_size for path in files)
    return Scope(root=root, files=tuple(files), total_bytes=total_bytes)


def visible_lines(text: str) -> list[str]:
    """Return Markdown lines outside fenced code blocks."""

    visible: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            visible.append(line)
    return visible


def link_target(payload: str) -> str:
    value = payload.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    return value.split(maxsplit=1)[0]


def check_links(scope: Scope, texts: dict[Path, str]) -> list[str]:
    findings: list[str] = []
    root = scope.root.resolve()
    for path in scope.files:
        for line_number, line in enumerate(visible_lines(texts[path]), start=1):
            for match in LINK_PATTERN.finditer(line):
                target = link_target(match.group(1))
                parsed = urlsplit(target)
                if (
                    not target
                    or parsed.scheme
                    or parsed.netloc
                    or target.startswith(("#", "mailto:", "tel:", "javascript:"))
                ):
                    continue
                target_path = unquote(parsed.path)
                if not target_path:
                    continue
                candidate = root / target_path.lstrip("/") if target_path.startswith("/") else path.parent / target_path
                resolved = candidate.resolve()
                if not resolved.is_relative_to(root) or not resolved.exists():
                    findings.append(
                        f"- {relative_path(path, root)}:{line_number}: broken link -> {target}"
                    )
    return findings


def check_deprecations(scope: Scope, texts: dict[Path, str], as_of: date | None) -> list[str]:
    if as_of is None:
        return ["- temporal deprecation check: NOT ASSESSED (pass --as-of YYYY-MM-DD)"]
    policy = scope.root / "docs/deprecation-policy.md"
    entities: list[tuple[str, date]] = []
    for line in texts[policy].splitlines():
        match = DEPRECATION_ROW.match(line)
        if match:
            entities.append((match.group(1), date.fromisoformat(match.group(3))))
    findings: list[str] = []
    for entity, removal_on in entities:
        if as_of <= removal_on:
            continue
        for path in scope.files:
            rel = relative_path(path, scope.root)
            if rel in DEPRECATION_EXCLUSIONS or rel == entity:
                continue
            if entity in texts[path]:
                findings.append(
                    f"- {rel} references removed entity `{entity}` (removed {removal_on.isoformat()})"
                )
    return findings


def check_dated_framing(scope: Scope, texts: dict[Path, str]) -> list[str]:
    findings: list[str] = []
    for path in scope.files:
        rel = relative_path(path, scope.root)
        if (
            rel in DATED_EXCLUSIONS
            or rel.startswith("docs/plans/")
            or rel.startswith("project-log/")
            or rel.startswith("SESSION_")
        ):
            continue
        for line_number, line in enumerate(visible_lines(texts[path]), start=1):
            if DATED_FRAMING.search(line):
                findings.append(f"- {rel}:{line_number}")
    return findings


def check_banned_terms(scope: Scope, texts: dict[Path, str]) -> list[str]:
    findings: list[str] = []
    for path in scope.files:
        rel = relative_path(path, scope.root)
        if rel in BANNED_EXCLUSIONS:
            continue
        for line_number, line in enumerate(visible_lines(texts[path]), start=1):
            if BANNED_TERMS.search(line):
                findings.append(f"- {rel}:{line_number}")
    return findings


def check_skill_lengths(scope: Scope, texts: dict[Path, str]) -> list[str]:
    findings: list[str] = []
    for path in scope.files:
        if path.name == "SKILL.md":
            line_count = len(texts[path].splitlines())
            if line_count > 500:
                first_lines = "\n".join(texts[path].splitlines()[:5]).lower()
                if "justification" not in first_lines and "exceeds 500" not in first_lines:
                    findings.append(
                        f"- {relative_path(path, scope.root)} has {line_count} lines (limit 500)"
                    )
    return findings


def check_duplicate_windows(scope: Scope, texts: dict[Path, str]) -> list[str]:
    windows: dict[str, set[str]] = defaultdict(set)
    for path in scope.files:
        if "references" not in path.parts:
            continue
        lines = [line.strip() for line in visible_lines(texts[path]) if line.strip()]
        for index in range(max(0, len(lines) - 4)):
            window = "\n".join(lines[index : index + 5]).encode("utf-8")
            digest = hashlib.sha256(window).hexdigest()
            windows[digest].add(relative_path(path, scope.root))
    shared = sorted(
        (digest, sorted(paths))
        for digest, paths in windows.items()
        if len(paths) > 1
    )
    return [f"- {digest}: {', '.join(paths)}" for digest, paths in shared[:20]]


def check_forbidden_constructions(scope: Scope, texts: dict[Path, str]) -> list[str]:
    findings: list[str] = []
    for path in scope.files:
        rel = relative_path(path, scope.root)
        if rel in FORBIDDEN_EXCLUSIONS:
            continue
        for line_number, line in enumerate(visible_lines(texts[path]), start=1):
            if FORBIDDEN_CONSTRUCTIONS.search(line):
                findings.append(f"- {rel}:{line_number}")
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--as-of", type=date.fromisoformat, default=None)
    parser.add_argument("--strict", action="store_true", default=os.environ.get("DRIFT_STRICT") == "1")
    return parser.parse_args()


def render_section(title: str, findings: list[str]) -> list[str]:
    lines = [f"## {title}", ""]
    lines.extend(findings or ["No findings."])
    lines.append("")
    return lines


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    reports_dir = args.reports_dir.resolve()
    report_path = reports_dir / "drift-report.md"
    reports_dir.mkdir(parents=True, exist_ok=True)

    missing = [path for path in REQUIRED_FILES if not (root / path).is_file()]
    if missing:
        report_path.write_text(
            "# Drift-Check Report\n\n## Prerequisites\n\n"
            + "\n".join(f"- missing: {path}" for path in missing)
            + "\n",
            encoding="utf-8",
        )
        print(f"drift-check: prerequisite missing ({', '.join(missing)})", file=sys.stderr)
        return 8

    try:
        scope = collect_scope(root)
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        report_path.write_text(
            f"# Drift-Check Report\n\n## Prerequisites\n\n- {type(exc).__name__}: {exc}\n",
            encoding="utf-8",
        )
        print(f"drift-check: prerequisite error: {exc}", file=sys.stderr)
        return 8

    if len(scope.files) > MAX_MARKDOWN_FILES or scope.total_bytes > MAX_TOTAL_BYTES:
        report_path.write_text(
            "# Drift-Check Report\n\n## Bounded scope\n\n"
            f"- Markdown files: {len(scope.files)} (limit {MAX_MARKDOWN_FILES})\n"
            f"- Total bytes: {scope.total_bytes} (limit {MAX_TOTAL_BYTES})\n",
            encoding="utf-8",
        )
        print(
            f"drift-check: bounded scope exceeded ({len(scope.files)} files, {scope.total_bytes} bytes)",
            file=sys.stderr,
        )
        return 9

    try:
        texts = {path: path.read_text(encoding="utf-8") for path in scope.files}
    except (OSError, UnicodeDecodeError) as exc:
        print(f"drift-check: cannot read scoped Markdown: {exc}", file=sys.stderr)
        return 8

    dead_links = check_links(scope, texts)
    deprecations = check_deprecations(scope, texts, args.as_of)
    dated = check_dated_framing(scope, texts)
    banned = check_banned_terms(scope, texts)
    overlong = check_skill_lengths(scope, texts)
    duplicates = check_duplicate_windows(scope, texts)
    forbidden = check_forbidden_constructions(scope, texts)

    failures = 0
    if dead_links:
        failures |= 1
    if args.as_of is not None and deprecations:
        failures |= 2
    if dated:
        failures |= 4
    if args.strict and banned:
        failures |= 8
    if overlong:
        failures |= 16
    if args.strict and len(duplicates) >= 20:
        failures |= 32
    if args.strict and forbidden:
        failures |= 64

    lines = [
        "# Drift-Check Report",
        "",
        "Scope: Git-listed Markdown files only (tracked plus non-ignored working-tree files).",
        f"Markdown files: {len(scope.files)}",
        f"Total bytes: {scope.total_bytes}",
        f"As-of: {args.as_of.isoformat() if args.as_of else 'NOT ASSESSED'}",
        f"Strict mode: {'yes' if args.strict else 'no'}",
        "",
    ]
    lines.extend(render_section("1. Dead internal links", dead_links))
    lines.extend(render_section("2. Deprecated-entity references", deprecations))
    lines.extend(render_section("3. Dated framing", dated))
    lines.extend(render_section("4. Banned terms", banned))
    lines.extend(render_section("5. SKILL.md 500-line rule", overlong))
    lines.extend(render_section("6. Duplicated guidance", duplicates))
    lines.extend(render_section("7. Forbidden constructions", forbidden))
    lines.extend(
        [
            "## Summary",
            "",
            f"- Dead internal links: {len(dead_links)}",
            f"- Deprecated-entity references: {len(deprecations) if args.as_of else 'NOT ASSESSED'}",
            f"- Dated framing: {len(dated)}",
            f"- Banned terms: {len(banned)}",
            f"- SKILL.md over 500 lines: {len(overlong)}",
            f"- Duplicated guidance windows: {len(duplicates)}",
            f"- Forbidden constructions: {len(forbidden)}",
            f"- Status: {'FAIL' if failures else 'PASS'}",
            "",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")

    if dead_links:
        print(f"drift-check: FAIL - {len(dead_links)} dead internal link(s)")
    elif dated:
        print(f"drift-check: FAIL - {len(dated)} dated-framing instance(s)")
    elif overlong:
        print(f"drift-check: FAIL - {len(overlong)} SKILL.md file(s) over 500 lines")
    elif failures:
        print(f"drift-check: FAIL - exit bitmask {failures}")
    else:
        print(
            f"drift-check: PASS - {len(scope.files)} Markdown files; "
            f"as-of {args.as_of.isoformat() if args.as_of else 'NOT ASSESSED'}"
        )
    print("drift-check: report drift-report.md")
    for code in (1, 2, 4, 8, 16, 32, 64):
        if failures & code:
            return {1: 1, 2: 2, 4: 3, 8: 4, 16: 5, 32: 6, 64: 7}[code]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
