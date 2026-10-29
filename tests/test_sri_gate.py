from __future__ import annotations

import base64
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
    digest = base64.b64encode(bytes(48)).decode("ascii")
    parser.feed(f'<link rel="stylesheet" href="https://cdn.test/site.css" integrity="sha384-{digest}" crossorigin="anonymous">')
    assert parser.findings == []


def test_external_asset_without_crossorigin_fails():
    parser = check_sri.AssetParser("https://example.test/")
    parser.feed('<script src="https://cdn.test/app.js" integrity="sha384-YWJj"></script>')
    assert ("https://cdn.test/app.js", "missing crossorigin") in parser.findings


def test_wrong_length_sri_digest_fails():
    parser = check_sri.AssetParser("https://example.test/")
    parser.feed('<script src="https://cdn.test/app.js" integrity="sha384-YWJj" crossorigin="anonymous"></script>')
    assert ("https://cdn.test/app.js", "missing or invalid integrity") in parser.findings


def test_canonical_url_does_not_exempt_asset_from_sri_audit(tmp_path):
    page = tmp_path / "index.html"
    page.write_text('''<link rel="canonical" href="https://cdn.test/page">
<script src="https://cdn.test/app.js"></script>''', encoding="utf-8")
    assert ("https://cdn.test/app.js", "missing or invalid integrity") in check_sri.audit(page)


def test_protocol_relative_external_asset_is_audited():
    parser = check_sri.AssetParser("https://site.test/page")
    parser.feed('<script src="//cdn.test/app.js"></script>')
    assert ("//cdn.test/app.js", "missing or invalid integrity") in parser.findings


def test_explicit_served_origin_exempts_same_origin_asset():
    parser = check_sri.AssetParser("https://site.test/page")
    parser.feed('<script src="https://site.test/app.js"></script>')
    assert parser.findings == []


def test_protocol_relative_asset_matching_explicit_served_origin_is_same_origin():
    parser = check_sri.AssetParser("https://cdn.test/page")
    parser.feed('<script src="//cdn.test/app.js"></script>')
    assert parser.findings == []


def test_malformed_network_asset_fails_closed():
    parser = check_sri.AssetParser(None)
    parser.feed('<script src="https://cdn.test:not-a-port/app.js"></script>')
    assert ("https://cdn.test:not-a-port/app.js", "invalid network asset URL") in parser.findings
