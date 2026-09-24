#!/usr/bin/env python3
"""Reject raw books and likely reconstructive full-text conversions."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


LARGE_BOOK_TEXT_BYTES = 80_000
RAW_BOOK_EXTENSIONS = {".epub", ".mobi", ".azw", ".azw3"}
SOURCE_TEXT_EXTENSIONS = {".md", ".txt", ".rst", ".html", ".htm"}
BOOK_SOURCE_PATH_RE = re.compile(
    r"(?:^|/)(?:book-extractions?|book-dumps?|raw-books?|source-books?)(?:/|$)",
    re.IGNORECASE,
)
BOOK_SUMMARY_NAME_RE = re.compile(
    r"(?:^|[-_.])(?:book[-_]?extraction|book[-_]?summary|extraction)(?:[-_.]|$)",
    re.IGNORECASE,
)
# Content-aware digest markers (owner rule 2026-09-24): a book digest is rejected wherever it is stored,
# including under skills/*/references/. Each pattern is applied to Markdown/text files.
QUOTE_SECTION_RE = re.compile(r"^#{1,6}\s*(?:direct|key|notable|selected|memorable)\s+quotes?\b", re.IGNORECASE | re.MULTILINE)
EXTRACTED_FROM_RE = re.compile(
    r"^\s*(?:>\s*)?(?:\*\*)?(?:source:?\*{0,2}\s*)?(?:this (?:file|document|reference) extracts\b|extracted from\b|distilled from the full text of\b)",
    re.IGNORECASE | re.MULTILINE,
)
LOCAL_BOOK_PATH_RE = re.compile(
    r"(?:[A-Za-z]:[\\/]+(?:temp|tmp)[\\/]+books|\.claude[\\/]+skills[\\/]+book|_book_extracts|z-lib(?:rary)?\b|libgen)",
    re.IGNORECASE,
)
# One book's chapter/part sequence: headings such as "## Part IV: ..." or "### 3.2 ... (Author, Chapter 5)".
CHAPTER_HEADING_RE = re.compile(
    r"^#{2,4}\s+(?:(?:Part|Chapter|Ch\.?)\s+(?:[0-9]+|[IVXLC]+)\b|.*\((?:[^)]*,\s*)?(?:Chapter|Ch\.)\s*[0-9]+)",
    re.IGNORECASE | re.MULTILINE,
)
CHAPTER_HEADING_LIMIT = 3
SINGLE_SOURCE_HEADER_RE = re.compile(
    r"^(?:#\s+.*\u2014.*extraction.*|\*\*source:\*\*\s+.*(?:\u00a9|isbn|publisher).*)$",
    re.IGNORECASE | re.MULTILINE,
)
CONTENT_RULE_EXEMPT = {
    # The retirement record and rule statements name these patterns by design.
    "docs/continuous-improvement/book-source-retirement-2026-09-24.md",
}
FULL_TEXT_MARKERS = {
    "isbn": re.compile(r"\bISBN(?:-1[03])?\s*:?\s*[\dXx][\dXx\-\s]{8,}"),
    "copyright": re.compile(r"\bcopyright\s+(?:\u00a9|\(c\)|&copy;|[12]\d{3})", re.IGNORECASE),
    "rights-reserved": re.compile(r"\ball rights reserved\b", re.IGNORECASE),
    "reproduction-notice": re.compile(
        r"\bno part of this (?:book|publication|work) may be reproduced\b",
        re.IGNORECASE,
    ),
    "ebook-conversion": re.compile(
        r"(?:\[\]\{#[^}\n]*\.xhtml|calibre\d*|index_split_\d+\.html)",
        re.IGNORECASE,
    ),
}
EXCLUDED_PARTS = {".git", ".venv", "__pycache__", "node_modules"}


@dataclass(frozen=True)
class Finding:
    code: str
    path: Path
    message: str

    def format(self) -> str:
        return f"[ERROR] {self.code}: {self.path} {self.message}"


def scan_content(relative: Path, text: str) -> list[Finding]:
    """Content rules for a Markdown or text file. Returns findings for book-digest markers."""
    if relative.as_posix() in CONTENT_RULE_EXEMPT:
        return []
    findings: list[Finding] = []
    if QUOTE_SECTION_RE.search(text):
        findings.append(Finding("book-quote-section", relative, 'has a "Direct quotes"/"Key quotes" section; quote sections are never stored'))
    if EXTRACTED_FROM_RE.search(text):
        findings.append(Finding("book-extracted-from", relative, 'says it is "extracted from" a source or that it "extracts" one; write a task-oriented reference instead'))
    if LOCAL_BOOK_PATH_RE.search(text):
        findings.append(Finding("book-local-path", relative, "names a local book-file path or a pirate-library source"))
    chapters = CHAPTER_HEADING_RE.findall(text)
    if len(chapters) > CHAPTER_HEADING_LIMIT:
        findings.append(Finding("book-chapter-sequence", relative, f"{len(chapters)} chapter/part headings follow one book's sequence; reorganise by task"))
    if SINGLE_SOURCE_HEADER_RE.search("\n".join(text.splitlines()[:12])):
        findings.append(Finding("book-single-source-header", relative, "opens with a single-source extraction header"))
    return findings


def scan(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue

        suffix = path.suffix.lower()
        if suffix in RAW_BOOK_EXTENSIONS:
            findings.append(
                Finding(
                    "raw-book-source",
                    relative,
                    "raw ebook source files are temporary inputs and must not be stored in the repository",
                )
            )
            continue

        in_book_source_path = BOOK_SOURCE_PATH_RE.search(relative.as_posix()) is not None
        size = path.stat().st_size
        if in_book_source_path or BOOK_SUMMARY_NAME_RE.search(path.name):
            # Owner rule (2026-09-24): book extractions and book summaries are never stored
            # in this repository, whatever their size. Knowledge must live in task-oriented
            # skill references with a brief citation instead.
            findings.append(
                Finding(
                    "book-extraction-stored",
                    relative,
                    "book extractions and book summaries must never be stored in the repository; "
                    "convert the method into a task-oriented skill reference",
                )
            )
            continue
        if suffix == ".pdf" and in_book_source_path:
            findings.append(
                Finding(
                    "raw-book-source",
                    relative,
                    "PDFs under book/source-extraction paths must stay outside the repository",
                )
            )
            continue
        if suffix not in SOURCE_TEXT_EXTENSIONS:
            continue

        if in_book_source_path and size >= LARGE_BOOK_TEXT_BYTES:
            findings.append(
                Finding(
                    "source-fulltext-path",
                    relative,
                    f"{size} bytes under a book-extraction path; retain concise synthesis, not source text",
                )
            )

        try:
            text_for_rules = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            text_for_rules = ""
        findings.extend(scan_content(relative, text_for_rules))

        if size < 30_000:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        markers = sorted(name for name, pattern in FULL_TEXT_MARKERS.items() if pattern.search(content))
        if len(markers) >= 3:
            findings.append(
                Finding(
                    "source-fulltext-markers",
                    relative,
                    "likely reconstructive book text; matched markers: " + ", ".join(markers),
                )
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings = scan(args.root)
    print(f"source-ingestion-guardrail: {args.root.resolve()}")
    print(f"findings: {len(findings)}")
    for finding in findings:
        print(finding.format())
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
