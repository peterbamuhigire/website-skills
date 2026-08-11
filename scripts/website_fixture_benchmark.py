#!/usr/bin/env python3
"""Run a deterministic, local-only website fixture benchmark.

The benchmark proves only repository-local link, semantic, accessibility-input,
and performance-budget-input checks. It does not measure browser performance,
Core Web Vitals, production traffic, or field accessibility outcomes.
"""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "fixtures" / "website-kaizen"
DEFAULT_BUDGETS = ROOT / "performance-budgets.json"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []
        self.attrs: dict[str, list[dict[str, str]]] = {}
        self.headings: list[int] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalised = {key: value or "" for key, value in attrs}
        self.tags.append(tag)
        self.attrs.setdefault(tag, []).append(normalised)
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))


def local_target(page: Path, href: str, fixture: Path) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    value = parsed.path or "index.html"
    if value.startswith("/"):
        target = fixture / value.lstrip("/")
    else:
        target = page.parent / value
    return target.resolve()


def check_page(page: Path, fixture: Path) -> dict[str, object]:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    broken: list[str] = []
    for attrs in parser.attrs.get("a", []) + parser.attrs.get("link", []):
        href = attrs.get("href", "")
        target = local_target(page, href, fixture)
        if target is not None and (not target.is_relative_to(fixture.resolve()) or not target.is_file()):
            broken.append(href)
    html_attrs = parser.attrs.get("html", [{}])[0]
    images_without_alt = sum("alt" not in attrs for attrs in parser.attrs.get("img", []))
    missing_form_labels = sum(
        "id" not in attrs or not any(attrs.get("id") == label.get("for") for label in parser.attrs.get("label", []))
        for attrs in parser.attrs.get("input", [])
    )
    headings_ok = all(next_level - level <= 1 for level, next_level in zip(parser.headings, parser.headings[1:]))
    has_description = any(attrs.get("name") == "description" and attrs.get("content") for attrs in parser.attrs.get("meta", []))
    return {
        "page": page.name,
        "links": {"status": "PASS" if not broken else "FAIL", "broken": broken},
        "semantics": {
            "status": "PASS" if len(parser.attrs.get("main", [])) == 1 and len(parser.attrs.get("h1", [])) == 1 and headings_ok else "FAIL",
            "lang": html_attrs.get("lang", ""),
            "main_count": len(parser.attrs.get("main", [])),
            "h1_count": len(parser.attrs.get("h1", [])),
            "nav_count": len(parser.attrs.get("nav", [])),
            "heading_order": "PASS" if headings_ok else "FAIL",
        },
        "accessibility_inputs": {
            "status": "PASS" if html_attrs.get("lang") and images_without_alt == 0 and missing_form_labels == 0 and len(parser.attrs.get("nav", [])) > 0 else "FAIL",
            "images_without_alt": images_without_alt,
            "inputs_without_labels": missing_form_labels,
        },
        "metadata": {"status": "PASS" if parser.attrs.get("title") and has_description else "FAIL"},
    }


def run_benchmark(fixture: Path = DEFAULT_FIXTURE, budgets: Path = DEFAULT_BUDGETS) -> dict[str, object]:
    config = json.loads((fixture / "fixture.json").read_text(encoding="utf-8"))
    budget_data = json.loads(budgets.read_text(encoding="utf-8"))
    pages = [fixture / name for name in config["pages"]]
    page_results = [check_page(page, fixture) for page in pages]
    required_budget_keys = {"total_weight_kb", "js_kb_gzip", "css_kb_gzip"}
    available_keys = required_budget_keys.issubset(budget_data.get("global", {}))
    asset_bytes = sum(path.stat().st_size for path in fixture.iterdir() if path.is_file() and path.name != "fixture.json")
    raw_ceiling = int(budget_data["global"]["total_weight_kb"] * 1024) if available_keys else 0
    checks = {
        "links": all(result["links"]["status"] == "PASS" for result in page_results),
        "semantics": all(result["semantics"]["status"] == "PASS" for result in page_results),
        "accessibility_inputs": all(result["accessibility_inputs"]["status"] == "PASS" for result in page_results),
        "performance_budget_inputs": available_keys and asset_bytes <= raw_ceiling,
    }
    return {
        "id": config["id"],
        "status": "PASS" if all(checks.values()) else "FAIL",
        "evidence_type": "lab fixture only",
        "pages": page_results,
        "performance_budget_inputs": {
            "status": "PASS" if checks["performance_budget_inputs"] else "FAIL",
            "budget_file": str(budgets.relative_to(ROOT).as_posix()) if budgets.is_relative_to(ROOT) else str(budgets),
            "total_weight_budget_kb": budget_data.get("global", {}).get("total_weight_kb"),
            "fixture_asset_bytes": asset_bytes,
            "raw_ceiling_check": "PASS" if checks["performance_budget_inputs"] else "FAIL",
        },
        "field_core_web_vitals": "NOT ASSESSED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--budgets", type=Path, default=DEFAULT_BUDGETS)
    args = parser.parse_args()
    result = run_benchmark(args.fixture.resolve(), args.budgets.resolve())
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
