"""M10-11-T11 (GR-12): content-link graph over a built site."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/content_link_graph.py"


def run(site: Path, out: Path, *extra: str) -> tuple[int, dict]:
    result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), str(site), "--out", str(out), *extra],
                            cwd=ROOT, capture_output=True, text=True)
    report = json.loads(out.read_text(encoding="utf-8")) if out.is_file() else {}
    return result.returncode, report


def test_fixture_reports_exactly_the_seeded_findings(tmp_path):
    code, report = run(ROOT / "fixtures/website-link-graph", tmp_path / "graph.json")
    assert code == 1
    assert report["orphans"] == ["orphan.html"]
    assert report["broken_links"] == [{"page": "index.html", "href": "contact.html"}]
    assert report["missing_anchors"] == [{"page": "services.html", "href": "services.html#faq"}]
    assert report["unreachable_from_home"] == ["orphan.html"]


def test_repeat_runs_are_byte_identical(tmp_path):
    run(ROOT / "fixtures/website-link-graph", tmp_path / "a.json")
    run(ROOT / "fixtures/website-link-graph", tmp_path / "b.json")
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(tmp_path / "a.json") == digest(tmp_path / "b.json")


def test_kaizen_fixture_is_clean(tmp_path):
    code, report = run(ROOT / "fixtures/website-kaizen", tmp_path / "graph.json")
    assert code == 0 and report["status"] == "PASS"


def test_entry_allowlist_excludes_a_campaign_landing(tmp_path):
    site = tmp_path / "site"
    shutil.copytree(ROOT / "fixtures/website-link-graph", site)
    (site / "index.html").write_text((site / "index.html").read_text(encoding="utf-8").replace('href="contact.html"', 'href="/services.html"'), encoding="utf-8")
    (site / "services.html").write_text((site / "services.html").read_text(encoding="utf-8").replace("services.html#faq", "services.html#prices"), encoding="utf-8")
    code, report = run(site, tmp_path / "graph.json", "--entry", "orphan.html")
    assert code == 0, report
    assert report["orphans"] == [] and report["unreachable_from_home"] == []


def test_missing_dist_is_not_assessed(tmp_path):
    code, _report = run(tmp_path / "missing", tmp_path / "graph.json")
    assert code == 5
