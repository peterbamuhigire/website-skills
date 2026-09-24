"""The owner rule (2026-09-24): book extractions and book summaries are never stored."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("guardrail", ROOT / "scripts" / "source_ingestion_guardrail.py")
guardrail = importlib.util.module_from_spec(spec)
sys.modules["guardrail"] = guardrail
spec.loader.exec_module(guardrail)


def codes(tmp_path: Path) -> list[str]:
    return [finding.code for finding in guardrail.scan(tmp_path)]


def test_small_file_in_book_extractions_folder_is_rejected(tmp_path):
    (tmp_path / "book-extractions").mkdir()
    (tmp_path / "book-extractions" / "notes.md").write_text("short", encoding="utf-8")
    assert codes(tmp_path) == ["book-extraction-stored"]


def test_book_summary_file_name_is_rejected_anywhere(tmp_path):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "levy-ux-strategy-extraction.md").write_text("short", encoding="utf-8")
    (tmp_path / "docs" / "some-book-summary.md").write_text("short", encoding="utf-8")
    assert codes(tmp_path) == ["book-extraction-stored", "book-extraction-stored"]


def test_task_oriented_reference_is_allowed(tmp_path):
    (tmp_path / "skills").mkdir()
    (tmp_path / "skills" / "pricing-page-choice-architecture.md").write_text("# Pricing", encoding="utf-8")
    assert codes(tmp_path) == []


def test_repository_is_clean():
    assert guardrail.scan(ROOT) == []


def write(tmp_path: Path, name: str, text: str) -> None:
    target = tmp_path / "skills" / "x" / "references" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def test_quote_section_is_rejected(tmp_path):
    write(tmp_path, "a.md", "# Title\n\n## Direct quotes\n\n- a line\n")
    assert codes(tmp_path) == ["book-quote-section"]
    write(tmp_path, "b.md", "# Title\n\n### Key quotes\n")
    assert codes(tmp_path).count("book-quote-section") == 2


def test_extracted_from_and_local_paths_are_rejected(tmp_path):
    write(tmp_path, "a.md", "# Title\n**Source:** Extracted from `some-book.md`.\n")
    write(tmp_path, "b.md", "# Title\n\nThis file extracts the method.\n")
    write(tmp_path, "c.md", "# Title\n\nRead C:/temp/books/original.epub first.\n")
    assert sorted(codes(tmp_path)) == ["book-extracted-from", "book-extracted-from", "book-local-path"]


def test_book_chapter_sequence_is_rejected_but_task_headings_pass(tmp_path):
    chapters = "# T\n\n" + "".join(f"## Part {n}: Topic\n\ntext\n\n" for n in ("I", "II", "III", "IV"))
    write(tmp_path, "a.md", chapters)
    assert codes(tmp_path) == ["book-chapter-sequence"]
    write(tmp_path, "b.md", "# T\n\n## Decide the offer\n\n## Test the page\n\n## Extract text from a PDF\n")
    assert codes(tmp_path) == ["book-chapter-sequence"]


def test_ordinary_use_of_extract_is_allowed(tmp_path):
    write(tmp_path, "a.md", "# Tips\n\nExtract the text with a parser. Sources are extracted from the database.\n")
    assert codes(tmp_path) == []
