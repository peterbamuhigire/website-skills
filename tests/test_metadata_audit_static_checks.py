"""Static language and zoom checks in metadata-audit.sh (WSK2-07), and honest gate fixtures.

`<html lang>` (WCAG 3.1.1) and a viewport that does not block zoom (WCAG 1.4.4) used to be caught only
by the browser-based axe gate, which many hosts cannot run. These tests execute the real script against
temporary build folders. The viewport rule mirrors axe's `meta-viewport`: fail on `user-scalable=no` (or 0)
and on `maximum-scale` below 2.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "metadata-audit.sh"
BASH = shutil.which("bash")

pytestmark = pytest.mark.skipif(BASH is None, reason="bash is required: metadata-audit checks NOT_ASSESSED")

DESCRIPTION = "A description that is comfortably longer than fifty characters for the audit."


def page(html_open='<html lang="en-GB">', viewport='<meta name="viewport" content="width=device-width, initial-scale=1">', title="Home page"):
    return f"""<!doctype html>
{html_open}
<head>
<meta charset="utf-8">
{viewport}
<title>{title}</title>
<meta name="description" content="{DESCRIPTION}">
<link rel="canonical" href="https://example.com/">
<meta property="og:title" content="{title}">
<meta property="og:image" content="https://example.com/card.png">
</head>
<body><main><h1>{title}</h1></main></body>
</html>
"""


def audit(tmp_path: Path, html: str):
    dist = tmp_path / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(html, encoding="utf-8")
    return subprocess.run(
        [BASH, str(SCRIPT), str(dist)],
        cwd=tmp_path,
        env={"PATH": "/usr/bin:/bin", "REPORT": str(tmp_path / "report.txt")},
        capture_output=True,
        text=True,
    )


def test_a_complete_page_passes(tmp_path):
    result = audit(tmp_path, page())
    assert result.returncode == 0, result.stdout + result.stderr
    assert "metadata-audit: PASS" in result.stdout


@pytest.mark.parametrize("html_open", ["<html>", '<html lang="">', '<html class="no-js">', '<html lang=" ">'])
def test_missing_or_empty_lang_fails(tmp_path, html_open):
    result = audit(tmp_path, page(html_open=html_open))
    assert result.returncode == 1, result.stdout + result.stderr
    assert "<html lang>" in result.stdout


def test_lang_on_a_multi_attribute_or_multi_line_tag_is_found(tmp_path):
    result = audit(tmp_path, page(html_open='<html class="a"\n      lang="sw">'))
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize(
    "content",
    [
        "width=device-width, initial-scale=1, user-scalable=no",
        "width=device-width, user-scalable=0",
        "width=device-width, initial-scale=1, maximum-scale=1",
        "width=device-width, maximum-scale=1.5",
        "user-scalable = no, width=device-width",
    ],
)
def test_viewport_that_blocks_zoom_fails(tmp_path, content):
    result = audit(tmp_path, page(viewport=f'<meta name="viewport" content="{content}">'))
    assert result.returncode == 1, result.stdout + result.stderr
    assert "zoom" in result.stdout


@pytest.mark.parametrize(
    "content",
    [
        "width=device-width, initial-scale=1, maximum-scale=2",
        "width=device-width, initial-scale=1, maximum-scale=5",
        "width=device-width, initial-scale=1, user-scalable=yes",
        "width=device-width, initial-scale=1, minimum-scale=1",
    ],
)
def test_viewport_that_allows_zoom_passes(tmp_path, content):
    result = audit(tmp_path, page(viewport=f'<meta name="viewport" content="{content}">'))
    assert result.returncode == 0, result.stdout + result.stderr


def test_viewport_with_content_before_name_is_still_checked(tmp_path):
    result = audit(tmp_path, page(viewport='<meta content="width=device-width, user-scalable=no" name="viewport">'))
    assert result.returncode == 1
    assert "zoom" in result.stdout


def test_existing_checks_are_unchanged(tmp_path):
    html = page().replace('<link rel="canonical" href="https://example.com/">', "")
    result = audit(tmp_path, html)
    assert result.returncode == 1
    assert "canonical" in result.stdout


def test_declared_metadata_gate_fixtures_really_pass_and_fail():
    """tests/gates/cases.json names a pass and a fail fixture for the metadata gate; run both for real."""
    case = next(c for c in json.loads((ROOT / "tests/gates/cases.json").read_text(encoding="utf-8"))["cases"] if c["gate"] == "metadata")
    outcomes = {}
    for label in ("pass", "fail"):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            dist.mkdir()
            shutil.copy(ROOT / "tests/gates" / case[label], dist / "index.html")
            outcomes[label] = subprocess.run(
                [BASH, str(SCRIPT), str(dist)], cwd=tmp, env={"PATH": "/usr/bin:/bin", "REPORT": str(Path(tmp) / "r.txt")}, capture_output=True, text=True
            ).returncode
    assert outcomes == {"pass": 0, "fail": 1}
