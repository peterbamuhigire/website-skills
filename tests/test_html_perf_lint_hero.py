"""html-perf-lint hero detection ignores small marks (WSK2-08).

HPL-101 used to name a 40 px decorative header mark as the "hero image" on every page whose only image
was that mark, a warning nobody can act on. An image whose declared width and height are both 64 or less
is now a mark or icon and cannot be the hero; it still gets the dimension and `document.write` checks.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
LINT = ROOT / "scripts" / "html-perf-lint.mjs"
NODE = shutil.which("node")

pytestmark = pytest.mark.skipif(NODE is None, reason="Node.js is required: html-perf-lint checks NOT_ASSESSED")

MARK = '<img src="/mark.svg" width="40" height="40" alt="">'


def lint(tmp_path: Path, body: str):
    dist = tmp_path / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(f"<!doctype html><html lang=\"en\"><head><title>t</title></head><body>{body}</body></html>", encoding="utf-8")
    result = subprocess.run([NODE, str(LINT), str(dist)], capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr


def test_a_page_whose_only_image_is_a_small_mark_has_no_hero_warning(tmp_path):
    code, out = lint(tmp_path, f"<header>{MARK}</header><main><h1>Text hero</h1></main>")
    assert code == 0, out
    assert "HPL-101" not in out


def test_the_large_image_is_the_hero_not_the_mark(tmp_path):
    code, out = lint(tmp_path, f'{MARK}<img src="/big.jpg" width="1200" height="600" alt="A workshop bench">')
    assert code == 0, out
    assert "HPL-101" in out and "/big.jpg" in out
    assert "/mark.svg" not in out


def test_lazy_loading_on_the_large_image_is_still_an_error(tmp_path):
    code, out = lint(tmp_path, f'{MARK}<img src="/big.jpg" width="1200" height="600" alt="x" loading="lazy">')
    assert code == 1
    assert "HPL-003" in out and "/big.jpg" in out


def test_a_mark_without_dimensions_still_fails_the_dimension_check(tmp_path):
    code, out = lint(tmp_path, '<img src="/mark.svg" alt="">')
    assert code == 1
    assert "HPL-002" in out


def test_boundary_64_by_64_is_a_mark_and_65_by_64_can_be_the_hero(tmp_path):
    code, out = lint(tmp_path, '<img src="/a.png" width="64" height="64" alt="">')
    assert code == 0 and "HPL-101" not in out, out
    code, out = lint(tmp_path, '<img src="/a.png" width="65" height="64" alt="">')
    assert code == 0 and "HPL-101" in out, out


def test_a_wide_short_image_is_not_treated_as_a_mark(tmp_path):
    code, out = lint(tmp_path, '<img src="/banner.png" width="800" height="40" alt="">')
    assert code == 0 and "HPL-101" in out, out


def test_an_explicit_hero_marker_is_unchanged(tmp_path):
    code, out = lint(tmp_path, f'{MARK}<img src="/big.jpg" width="1200" height="600" alt="x" fetchpriority="high">')
    assert code == 0, out
    assert "HPL-101" not in out


def test_a_single_unmarked_content_image_still_warns(tmp_path):
    code, out = lint(tmp_path, '<img src="/photo.jpg" width="300" height="200" alt="A bicycle">')
    assert code == 0
    assert "HPL-101" in out and "/photo.jpg" in out
