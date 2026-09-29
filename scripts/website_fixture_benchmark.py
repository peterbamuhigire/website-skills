#!/usr/bin/env python3
"""Run a deterministic, local-only website fixture benchmark.

The benchmark proves only repository-local link, semantic, accessibility-input,
and performance-budget-input checks. It does not measure browser performance,
Core Web Vitals, production traffic, or field accessibility outcomes.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "fixtures" / "website-kaizen"
DEFAULT_BUDGETS = ROOT / "performance-budgets.json"
DEFAULT_PICKERS = ROOT / "quality" / "picker-libraries.json"
# Same shape as the chwezi-slop waiver reason: "<who>: <evidence>".
WAIVER_REASON = re.compile(r"^[^:\n]{2,80}: \S.{9,}$")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []
        self.attrs: dict[str, list[dict[str, str]]] = {}
        self.headings: list[int] = []
        self.title_text: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalised = {key: value or "" for key, value in attrs}
        self.tags.append(tag)
        self.attrs.setdefault(tag, []).append(normalised)
        if tag == "title":
            self.in_title = True
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_text.append(data)


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
    has_description = any(attrs.get("name") == "description" and attrs.get("content", "").strip() for attrs in parser.attrs.get("meta", []))
    title_value = re.sub(r"<!--.*?-->", "", "".join(parser.title_text), flags=re.DOTALL).strip()
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
        "metadata": {"status": "PASS" if title_value and has_description else "FAIL"},
    }


def load_pickers(path: Path = DEFAULT_PICKERS) -> list[dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    libraries = data.get("libraries") if isinstance(data, dict) else None
    if not isinstance(libraries, list) or not libraries:
        raise ValueError("picker-libraries.json must list libraries")
    return libraries


def dependency_minimalism(pages: list[Path], fixture: Path, pickers: list[dict[str, object]]) -> dict[str, object]:
    """PT-10: fail a known picker library unless the page records why a native control is insufficient."""
    findings: list[dict[str, str]] = []
    waivers: list[dict[str, str]] = []
    invalid_waivers: list[dict[str, str]] = []
    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for tag_attrs in parser.attrs.values():
            for attrs in tag_attrs:
                if "data-native-insufficient" in attrs:
                    reason = attrs["data-native-insufficient"].strip()
                    target = waivers if WAIVER_REASON.match(reason) else invalid_waivers
                    target.append({"page": page.name, "reason": reason})
        for tag, key in (("script", "src"), ("link", "href")):
            for attrs in parser.attrs.get(tag, []):
                url = attrs.get(key, "")
                for library in pickers:
                    if url and re.search(str(library["asset_pattern"]), url, re.IGNORECASE):
                        findings.append({"page": page.name, "library": str(library["name"]), "via": f"{tag} {key}={url}"})
    package = fixture / "package.json"
    if package.is_file():
        manifest = json.loads(package.read_text(encoding="utf-8"))
        declared = {**manifest.get("dependencies", {}), **manifest.get("devDependencies", {})}
        for library in pickers:
            for name in library.get("packages", []):
                if name in declared:
                    findings.append({"page": "package.json", "library": str(library["name"]), "via": f"dependency {name}"})
    waived = bool(findings) and bool(waivers) and not invalid_waivers
    status = "PASS" if not findings or waived else "FAIL"
    return {"status": status, "findings": findings, "waivers": waivers, "invalid_waivers": invalid_waivers,
            "rule": "native control first; a picker library needs data-native-insufficient=\"<who>: <evidence>\" on the control"}


def run_benchmark(fixture: Path = DEFAULT_FIXTURE, budgets: Path = DEFAULT_BUDGETS, pickers: Path = DEFAULT_PICKERS) -> dict[str, object]:
    fixture = fixture.resolve()
    config = json.loads((fixture / "fixture.json").read_text(encoding="utf-8"))
    budget_data = json.loads(budgets.read_text(encoding="utf-8"))
    names = config.get("pages") if isinstance(config, dict) else None
    if not isinstance(names, list) or not names:
        raise ValueError("pages must be a non-empty list")
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError("page names must be non-empty strings")
    pages = [(fixture / name).resolve() for name in names]
    if len(set(pages)) != len(pages):
        raise ValueError("pages must have unique resolved paths")
    if any(not page.is_relative_to(fixture) or not page.is_file() for page in pages):
        raise ValueError("pages must be existing files within the fixture")
    page_results = [check_page(page, fixture) for page in pages]
    minimalism = dependency_minimalism(pages, fixture, load_pickers(pickers))
    required_budget_keys = {"total_weight_kb", "js_kb_gzip", "css_kb_gzip"}
    global_budget = budget_data.get("global") if isinstance(budget_data, dict) else None
    if not isinstance(global_budget, dict):
        raise ValueError("global budgets must be an object")
    available_keys = required_budget_keys.issubset(global_budget)
    try:
        if available_keys and any(type(global_budget[key]) not in (int, float)
                                  or not math.isfinite(global_budget[key]) or global_budget[key] < 0
                                  for key in required_budget_keys):
            raise ValueError("required budgets must be finite non-negative numbers")
        raw_ceiling = int(global_budget["total_weight_kb"] * 1024) if available_keys else 0
    except OverflowError as exc:
        raise ValueError("required budgets exceed numeric conversion range") from exc
    assets = [path for path in fixture.rglob("*") if path.is_file() and path != fixture / "fixture.json"]
    if any(not path.resolve().is_relative_to(fixture) for path in assets):
        raise ValueError("fixture assets must stay within the fixture")
    asset_bytes = sum(path.stat().st_size for path in assets)
    checks = {
        "links": all(result["links"]["status"] == "PASS" for result in page_results),
        "semantics": all(result["semantics"]["status"] == "PASS" for result in page_results),
        "metadata": all(result["metadata"]["status"] == "PASS" for result in page_results),
        "accessibility_inputs": all(result["accessibility_inputs"]["status"] == "PASS" for result in page_results),
        "performance_budget_inputs": available_keys and asset_bytes <= raw_ceiling,
        "dependency_minimalism": minimalism["status"] == "PASS",
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
        "dependency_minimalism": minimalism,
        "field_core_web_vitals": "NOT ASSESSED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--budgets", type=Path, default=DEFAULT_BUDGETS)
    args = parser.parse_args()
    try:
        result = run_benchmark(args.fixture.resolve(), args.budgets.resolve())
    except (OSError, UnicodeError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc), "evidence_type": "lab fixture only"}))
        return 1
    print(json.dumps(result, indent=2))
    print(f"dependency_minimalism: {result['dependency_minimalism']['status']}", file=sys.stderr)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
