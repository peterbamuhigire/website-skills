"""Project-artefact contract checks (M10-11-T13).

Standard library only: checks the example artefacts against the header contract in
templates/project-artifacts/core-artifacts.schema.json, and the optional per-page
visitor_mode field of the strategy brief.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "templates/project-artifacts"
SCHEMA = json.loads((ARTIFACTS / "core-artifacts.schema.json").read_text(encoding="utf-8"))
DEFS = SCHEMA["$defs"]


def header_errors(doc: dict) -> list[str]:
    header = DEFS["header"]
    errors = [f"missing {key}" for key in header["required"] if key not in doc]
    if doc.get("version") != header["properties"]["version"]["const"]:
        errors.append("version must be 1")
    if doc.get("status") not in header["properties"]["status"]["enum"]:
        errors.append("status not allowed")
    return errors


def strategy_brief_errors(doc: dict) -> list[str]:
    errors = header_errors(doc)
    if doc.get("artifact") != "strategy-brief":
        errors.append("artifact must be strategy-brief")
    pages = doc.get("pages", [])
    if not isinstance(pages, list):
        return errors + ["pages must be a list"]
    modes = DEFS["visitorMode"]["enum"]
    for page in pages:
        for key in DEFS["strategyBriefPage"]["required"]:
            if key not in page:
                errors.append(f"page missing {key}")
        if "visitor_mode" in page and page["visitor_mode"] not in modes:
            errors.append(f"page {page.get('route')}: visitor_mode {page['visitor_mode']!r} not in {modes}")
    return errors


@pytest.mark.parametrize("path", sorted(ARTIFACTS.glob("*.example.json")), ids=lambda p: p.name)
def test_example_artifacts_carry_the_header(path):
    assert header_errors(json.loads(path.read_text(encoding="utf-8"))) == []


def test_visitor_mode_vocabulary_matches_the_detector():
    assert DEFS["visitorMode"]["enum"] == ["persuade", "operate", "read", "experience"]


def test_strategy_brief_example_validates_without_visitor_mode():
    brief = json.loads((ARTIFACTS / "strategy-brief.example.json").read_text(encoding="utf-8"))
    assert "pages" not in brief or all("visitor_mode" not in page for page in brief["pages"])
    assert strategy_brief_errors(brief) == []


def test_strategy_brief_example_validates_with_visitor_mode():
    brief = copy.deepcopy(json.loads((ARTIFACTS / "strategy-brief.example.json").read_text(encoding="utf-8")))
    brief["pages"] = [{"route": "/", "visitor_mode": "persuade"}, {"route": "/fees/", "visitor_mode": "read"}, {"route": "/contact/"}]
    assert strategy_brief_errors(brief) == []


def test_unknown_visitor_mode_is_rejected():
    brief = json.loads((ARTIFACTS / "strategy-brief.example.json").read_text(encoding="utf-8"))
    brief["pages"] = [{"route": "/", "visitor_mode": "sell"}]
    assert strategy_brief_errors(brief)
