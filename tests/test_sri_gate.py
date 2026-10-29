from __future__ import annotations

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_sri.py"
SPEC = importlib.util.spec_from_file_location("check_sri", MODULE_PATH)
check_sri = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(check_sri)


def test_canonical_absolute_link_is_not_an_asset():
    html = '''<link rel="canonical" href="https://example.test/page">
<link rel="stylesheet" href="/site.css"><script src="/site.js"></script>'''
    parser = check_sri.AssetParser(None)
    parser.feed(html)
    assert parser.findings == []


def test_external_script_without_integrity_fails():
    parser = check_sri.AssetParser("https://example.test/")
    parser.feed('<script src="https://cdn.test/app.js"></script>')
    assert ("https://cdn.test/app.js", "missing or invalid integrity") in parser.findings


def test_external_stylesheet_with_valid_integrity_and_crossorigin_passes():
    parser = check_sri.AssetParser("https://example.test/")
    parser.feed('<link rel="stylesheet" href="https://cdn.test/site.css" integrity="sha384-YWJj" crossorigin="anonymous">')
    assert parser.findings == []


def test_external_asset_without_crossorigin_fails():
    parser = check_sri.AssetParser("https://example.test/")
    parser.feed('<script src="https://cdn.test/app.js" integrity="sha384-YWJj"></script>')
    assert ("https://cdn.test/app.js", "missing crossorigin") in parser.findings
