"""The African language pack claims only what the engine can produce (WSK2-09).

The pack called ten languages "first-class" while only Kiswahili (and French and English, outside the table)
have native-copy skills, and its speaker counts cited no source. A language is first-class only when a
native-copy skill exists; the rest are layout-supported and need a named native writer and reviewer. Every
speaker figure carries its unsourced status in the column header, so none can be quoted by accident.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "skills/orchestration/africa-excellence/references/african-language-pack.md"
ROUTER = ROOT / "skills/orchestration/africa-excellence/SKILL.md"
SKILL_NAMES = {p.parent.name for p in (ROOT / "skills").glob("*/*/SKILL.md")}


def support_table() -> list[list[str]]:
    lines = PACK.read_text(encoding="utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Language |") and "Copy route" in line)
    rows = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def header() -> list[str]:
    lines = PACK.read_text(encoding="utf-8").splitlines()
    line = next(line for line in lines if line.startswith("| Language |") and "Copy route" in line)
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def test_the_pack_no_longer_calls_ten_languages_first_class():
    text = PACK.read_text(encoding="utf-8")
    assert not re.search(r"\b10 first-class\b|\bten first-class\b", text, re.I)
    assert "## First-class languages" not in text


def test_the_router_does_not_call_the_layout_only_languages_first_class_either():
    text = ROUTER.read_text(encoding="utf-8")
    assert not re.search(r"10 first-class African", text)
    assert not re.search(r"Tifinagh are treated as first-class", text)


def test_every_copy_route_names_a_skill_that_exists_or_says_none():
    rows = support_table()
    assert len(rows) == 10
    for row in rows:
        route = row[header().index("Copy route")]
        names = re.findall(r"`([a-z0-9-]+)`", route)
        if names:
            assert all(name in SKILL_NAMES for name in names), (row[0], names)
        else:
            assert route.lower().startswith("none"), (row[0], route)


def test_only_languages_with_a_native_copy_skill_have_a_copy_route():
    routed = [row[0] for row in support_table() if re.search(r"`[a-z0-9-]+`", row[header().index("Copy route")])]
    assert routed == ["Kiswahili"]
    assert "swahili-native-copy" in SKILL_NAMES


def test_the_speaker_column_is_marked_unsourced_in_its_header():
    column = next(cell for cell in header() if cell.lower().startswith("speakers"))
    assert "not_assessed" in column.lower() and "do not quote" in column.lower()


def test_no_figure_was_deleted_the_estimates_are_still_there_for_the_owner_to_source():
    figures = [row[header().index(next(c for c in header() if c.lower().startswith("speakers")))] for row in support_table()]
    assert all(re.search(r"\d", figure) for figure in figures)
