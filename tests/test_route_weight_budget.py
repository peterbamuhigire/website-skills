"""Tests for scripts/route-weight-budget.mjs (perf-gate weight walker).

The walker replaced a check that measured raw HTML bytes only; these tests prove
that JS, CSS, font, image and third-party budgets are now enforced.
"""

from __future__ import annotations

import json
import os
import pathlib
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "route-weight-budget.mjs"
NODE = shutil.which("node")

pytestmark = pytest.mark.skipif(NODE is None, reason="node is not installed")

BUDGETS = {
    "global": {
        "total_weight_kb": 350,
        "html_kb_gzip": 30,
        "js_kb_gzip": 80,
        "css_kb_gzip": 30,
        "font_kb_total": 80,
        "above_fold_image_kb": 200,
        "third_party_js_kb": 0,
    },
    "routes": {"/": {"js_kb_gzip": 60}, "/about/": {}, "/blog/[slug]/": {}},
}


def incompressible(size: int) -> bytes:
    return os.urandom(size)


def build_site(root: Path, *, js_bytes: int = 2_000, hero_bytes: int = 50_000,
               extra_head: str = "", lazy_bytes: int = 0, font_bytes: int = 20_000,
               with_blog_post: bool = True) -> Path:
    dist = root / "dist"
    (dist / "assets").mkdir(parents=True)
    (dist / "about").mkdir()
    (dist / "assets" / "site.css").write_text(
        "@font-face{font-family:Body;src:url('/assets/body.woff2') format('woff2');font-display:swap}"
        "body{font-family:Body,serif}", encoding="utf-8")
    (dist / "assets" / "body.woff2").write_bytes(incompressible(font_bytes))
    # Hex-encoded random data compresses to roughly half; use raw bytes in a comment-free file.
    (dist / "assets" / "app.js").write_bytes(incompressible(js_bytes))
    (dist / "assets" / "hero-800.avif").write_bytes(incompressible(hero_bytes))
    (dist / "assets" / "hero-1600.avif").write_bytes(incompressible(hero_bytes * 3))
    lazy = ""
    if lazy_bytes:
        (dist / "assets" / "gallery.avif").write_bytes(incompressible(lazy_bytes))
        lazy = '<img src="/assets/gallery.avif" loading="lazy" width="400" height="300" alt="">'
    page = (
        "<!doctype html><html lang=en><head><meta charset=utf-8><title>T</title>"
        '<link rel="stylesheet" href="/assets/site.css">'
        f"{extra_head}</head><body>"
        '<img src="/assets/hero-800.avif" srcset="/assets/hero-800.avif 800w, /assets/hero-1600.avif 1600w" '
        'fetchpriority="high" width="800" height="500" alt="Hero">'
        f"{lazy}"
        '<script type="module" src="/assets/app.js"></script></body></html>'
    )
    (dist / "index.html").write_text(page, encoding="utf-8")
    (dist / "about" / "index.html").write_text(page, encoding="utf-8")
    if with_blog_post:
        (dist / "blog" / "hello").mkdir(parents=True)
        (dist / "blog" / "hello" / "index.html").write_text(page, encoding="utf-8")
    return dist


def run(tmp_path: Path, dist: Path, allow: str | None = None) -> tuple[int, dict]:
    budgets = tmp_path / "budgets.json"
    budgets.write_text(json.dumps(BUDGETS), encoding="utf-8")
    report = tmp_path / "report.json"
    args = [NODE, str(SCRIPT), "--dist", str(dist), "--budgets", str(budgets), "--report", str(report)]
    allow_file = tmp_path / "allow.txt"
    allow_file.write_text(allow or "", encoding="utf-8")
    args += ["--allow", str(allow_file)]
    result = subprocess.run(args, capture_output=True, text=True, cwd=tmp_path)
    data = json.loads(report.read_text(encoding="utf-8")) if report.exists() else {}
    return result.returncode, data


def route(data: dict, name: str) -> dict:
    return next(r for r in data["routes"] if r["route"] == name)


def test_small_site_passes_and_measures_every_category(tmp_path):
    code, data = run(tmp_path, build_site(tmp_path))
    assert code == 0, data
    home = route(data, "/")
    assert home["status"] == "PASS"
    measured = home["measured"]
    assert measured["font_kb_total"] > 15
    assert measured["js_kb_gzip"] > 1
    assert 45 < measured["above_fold_image_kb"] < 60  # 800w candidate chosen, not 1600w
    assert measured["total_weight_kb"] >= measured["above_fold_image_kb"] + measured["font_kb_total"]


def test_javascript_over_budget_fails_even_when_html_is_tiny(tmp_path):
    code, data = run(tmp_path, build_site(tmp_path, js_bytes=70_000))
    assert code == 2
    home = route(data, "/")
    assert home["status"] == "FAIL"
    assert any(f.startswith("js_kb_gzip") for f in home["failures"])
    # /about/ inherits the global 80 KB JS budget, so 70 KB passes there.
    assert route(data, "/about/")["status"] == "PASS"


def test_hero_image_over_budget_fails(tmp_path):
    code, data = run(tmp_path, build_site(tmp_path, hero_bytes=230_000))
    assert code == 2
    assert any(f.startswith("above_fold_image_kb") for f in route(data, "/")["failures"])


def test_lazy_images_do_not_count_towards_first_load(tmp_path):
    code, data = run(tmp_path, build_site(tmp_path, lazy_bytes=400_000))
    assert code == 0
    assert route(data, "/")["measured"]["total_weight_kb"] < 350


def test_font_budget_enforced(tmp_path):
    code, data = run(tmp_path, build_site(tmp_path, font_bytes=90_000))
    assert code == 2
    assert any(f.startswith("font_kb_total") for f in route(data, "/")["failures"])


def test_third_party_script_fails_zero_budget_unless_allowlisted(tmp_path):
    head = '<script async src="https://widgets.example.net/chat.js"></script>'
    code, data = run(tmp_path, build_site(tmp_path, extra_head=head))
    assert code == 2
    assert any("third_party_js_kb" in f for f in route(data, "/")["failures"])

    other = tmp_path / "second"
    other.mkdir()
    code, data = run(other, build_site(other, extra_head=head), allow="https://widgets.example.net  # approved chat, decision 2026-09-23\n")
    assert code == 0
    assert any("NOT_ASSESSED" in limit for limit in route(data, "/")["limits"])


def test_missing_referenced_asset_fails(tmp_path):
    dist = build_site(tmp_path)
    (dist / "assets" / "app.js").unlink()
    code, data = run(tmp_path, dist)
    assert code == 2
    assert any("missing" in f for f in route(data, "/")["failures"])


def test_no_budgeted_route_built_is_not_assessed(tmp_path):
    dist = tmp_path / "dist"
    dist.mkdir()
    code, data = run(tmp_path, dist)
    assert code == 4
    assert data["status"] == "NOT_ASSESSED"


def test_canonical_config_has_no_desktop_preset_and_no_lab_inp_assertion():
    config = json.loads((ROOT / "lighthouserc.json").read_text(encoding="utf-8"))
    settings = config["ci"]["collect"]["settings"]
    assert settings.get("preset") != "desktop"
    assert settings["formFactor"] == "mobile"
    assert "emulatedFormFactor" not in settings
    assertions = config["ci"]["assert"]["assertions"]
    assert "interaction-to-next-paint" not in assertions
    assert assertions["total-blocking-time"][0] == "error"
    budgets = json.loads((ROOT / "performance-budgets.json").read_text(encoding="utf-8"))
    assert budgets["network_profile"]["is_median"] is False
    assert "stress" in budgets["network_profile"]["name"]


LINT = ROOT / "scripts" / "html-perf-lint.mjs"


def lint(tmp_path: Path, html: str) -> tuple[int, dict]:
    dist = tmp_path / "lintdist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(html, encoding="utf-8")
    report = tmp_path / "lint.json"
    result = subprocess.run([NODE, str(LINT), str(dist), "--report", str(report)],
                            capture_output=True, text=True)
    return result.returncode, json.loads(report.read_text(encoding="utf-8"))


GOOD = ('<!doctype html><html><head><script type="module" src="/a.js"></script>'
        '<script defer src="/b.js"></script></head><body>'
        '<img src="/h.avif" width="800" height="500" fetchpriority="high" alt="">'
        '<img src="/g.avif" width="400" height="300" loading="lazy" alt="">'
        '<iframe src="/m.html" width="600" height="400" loading="lazy" title="m"></iframe></body></html>')


def codes(data: dict) -> set[str]:
    return {f["code"] for f in data["findings"]}


def test_lint_passes_clean_page(tmp_path):
    code, data = lint(tmp_path, GOOD)
    assert code == 0 and data["errors"] == 0, data


@pytest.mark.parametrize("html,expected", [
    (GOOD.replace('<script defer src="/b.js">', '<script src="/b.js">'), "HPL-001"),
    (GOOD.replace(' width="400" height="300"', ''), "HPL-002"),
    (GOOD.replace(' width="600" height="400"', ''), "HPL-002"),
    (GOOD.replace('fetchpriority="high"', 'fetchpriority="high" loading="lazy"'), "HPL-003"),
    (GOOD.replace('</body>', '<script>document.write("x")</script></body>'), "HPL-004"),
], ids=["blocking-head-script", "img-no-dims", "iframe-no-dims", "lazy-hero", "document-write"])
def test_lint_fails_each_rule(tmp_path, html, expected):
    code, data = lint(tmp_path, html)
    assert code == 1
    assert expected in codes(data)


def test_lint_warns_without_failing_on_missing_fetchpriority(tmp_path):
    code, data = lint(tmp_path, GOOD.replace(' fetchpriority="high"', ''))
    assert code == 0
    assert "HPL-101" in codes(data)


def run_with(tmp_path: Path, dist: Path, budgets: dict, extra: list[str] | None = None) -> tuple[int, str]:
    path = tmp_path / "custom-budgets.json"
    path.write_text(json.dumps(budgets), encoding="utf-8")
    allow = tmp_path / "allow-custom.txt"
    allow.write_text("", encoding="utf-8")
    result = subprocess.run([NODE, str(SCRIPT), "--dist", str(dist), "--budgets", str(path), "--allow", str(allow)]
                            + (extra or []), capture_output=True, text=True, cwd=tmp_path)
    return result.returncode, result.stdout + result.stderr


def test_missing_template_page_is_not_assessed_and_blocks(tmp_path):
    dist = build_site(tmp_path, with_blog_post=False)
    code, data = run(tmp_path, dist)
    assert code == 4
    blog = route(data, "/blog/[slug]/")
    assert blog["status"] == "NOT_ASSESSED"
    assert data["status"] == "NOT_ASSESSED"


def test_optional_missing_route_does_not_block(tmp_path):
    dist = build_site(tmp_path, with_blog_post=False)
    budgets = json.loads(json.dumps(BUDGETS))
    budgets["routes"]["/blog/[slug]/"] = {"optional": True}
    code, _ = run_with(tmp_path, dist, budgets)
    assert code == 0


def test_template_resolves_to_a_representative_built_page(tmp_path):
    dist = build_site(tmp_path)
    (dist / "blog" / "zeta").mkdir()
    (dist / "blog" / "zeta" / "index.html").write_text((dist / "index.html").read_text(encoding="utf-8"), encoding="utf-8")
    code, data = run(tmp_path, dist)
    assert code == 0
    blog = next(r for r in data["routes"] if r.get("representative_of") == "/blog/[slug]/")
    assert blog["route"] == "/blog/hello/"

    budgets = json.loads(json.dumps(BUDGETS))
    budgets["routes"]["/blog/[slug]/"] = {"representative": "/blog/zeta/"}
    code, out = run_with(tmp_path, dist, budgets, ["--report", str(tmp_path / "r2.json")])
    assert code == 0
    assert '/blog/zeta/' in (tmp_path / "r2.json").read_text(encoding="utf-8")


def test_route_budget_above_global_total_is_invalid_without_exception(tmp_path):
    dist = build_site(tmp_path)
    budgets = json.loads(json.dumps(BUDGETS))
    budgets["routes"]["/about/"] = {"total_weight_kb": 400}
    code, out = run_with(tmp_path, dist, budgets)
    assert code == 3 and "exceeds the global" in out
    budgets["routes"]["/about/"]["exception_decision"] = "project-log/decisions/2026-09-24-about.md"
    code, _ = run_with(tmp_path, dist, budgets)
    assert code == 0


def test_generated_lighthouse_config_covers_templates_and_honours_dist_dir(tmp_path):
    dist = build_site(tmp_path)
    base = tmp_path / "base-rc.json"
    base.write_text(json.dumps({"ci": {"collect": {"staticDistDir": "./dist", "url": ["http://localhost:4321/"]},
        "assert": {"preset": "lighthouse:recommended", "assertions": {
            "total-byte-weight": ["error", {"maxNumericValue": 358400}], "cumulative-layout-shift": ["error", {"maxNumericValue": 0.1}]}}}}),
        encoding="utf-8")
    out = tmp_path / "generated.json"
    code, _ = run_with(tmp_path, dist, BUDGETS, ["--emit-lhci-config", str(out), "--lhci-base", str(base), "--port", "4321"])
    assert code == 0
    cfg = json.loads(out.read_text(encoding="utf-8"))
    collect = cfg["ci"]["collect"]
    assert pathlib.Path(collect["staticDistDir"]) == dist.resolve()
    assert "http://localhost:4321/blog/hello/" in collect["url"]
    matrix = cfg["ci"]["assert"]["assertMatrix"]
    assert "total-byte-weight" not in matrix[0]["assertions"]
    blog = next(m for m in matrix if "blog/hello" in m["matchingUrlPattern"])
    assert blog["assertions"]["total-byte-weight"][1]["maxNumericValue"] == 350 * 1024


def test_repository_budgets_are_consistent_with_global_total():
    budgets = json.loads((ROOT / "performance-budgets.json").read_text(encoding="utf-8"))
    total = budgets["global"]["total_weight_kb"]
    for name, cfg in budgets["routes"].items():
        assert cfg.get("total_weight_kb", total) <= total or cfg.get("exception_decision"), name


HERO_PAGE = ('<!doctype html><html><head></head><body>'
             '<img src="/logo.svg" width="40" height="40" loading="lazy" alt="Logo">'
             '<img src="/hero.avif" width="1200" height="600" alt="Hero">'
             '</body></html>')


def test_lint_hero_is_the_largest_image_not_the_first(tmp_path):
    code, data = lint(tmp_path, HERO_PAGE)
    assert code == 0, data
    assert "HPL-003" not in codes(data)
    assert "HPL-101" in codes(data)


def test_lint_lazy_largest_image_fails(tmp_path):
    code, data = lint(tmp_path, HERO_PAGE.replace('width="1200" height="600"', 'width="1200" height="600" loading="lazy"'))
    assert code == 1
    assert "HPL-003" in codes(data)


def test_lint_data_hero_marker_wins_and_silences_warning(tmp_path):
    page = HERO_PAGE.replace('<img src="/logo.svg" width="40" height="40" loading="lazy"', '<img src="/logo.svg" width="40" height="40" data-hero')
    code, data = lint(tmp_path, page)
    assert code == 0
    assert "HPL-101" not in codes(data)
