"""M10-11 IM-03: slop-scan wrapper, vendored chwezi-slop detector and website pack.

Every family that slop-rules.md labels "automatic block" must be proved by the
fail fixture (its named rule fires with a failing severity and the scan exits 1)
and by the pass fixture (the rule does not fire and the scan exits 0).
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SLOP_RULES = ROOT / "skills/quality-gates/visual-qa/references/slop-rules.md"
PASS_DIST = ROOT / "tests/gates/pass/slop-dist"
FAIL_DIST = ROOT / "tests/gates/fail/slop-dist"
NODE = shutil.which("node")


def find_bash() -> str | None:
    if os.name == "nt":
        for candidate in (r"C:\Program Files\Git\bin\bash.exe", r"C:\Program Files (x86)\Git\bin\bash.exe"):
            if Path(candidate).is_file():
                return candidate
    return shutil.which("bash")


BASH = find_bash()
needs_node = pytest.mark.skipif(NODE is None, reason="Node.js unavailable: detector-backed checks NOT_ASSESSED")
needs_bash = pytest.mark.skipif(BASH is None or NODE is None, reason="bash or Node.js unavailable: slop-scan NOT_ASSESSED")


def scan(dist: Path, workdir: Path, engine: Path = ROOT, env_extra: dict | None = None) -> tuple[int, dict]:
    env = {**os.environ, "REPORTS_DIR": (workdir / "reports").as_posix()}
    env.pop("CHWEZI_SLOP_DETECTOR", None)
    env.update(env_extra or {})
    result = subprocess.run([BASH, (engine / "scripts/slop-scan.sh").as_posix(), dist.as_posix()], cwd=workdir, env=env,
                            capture_output=True, text=True)
    report_path = workdir / "reports/design-quality/slop.json"
    report = json.loads(report_path.read_text(encoding="utf-8")) if report_path.is_file() else {}
    return result.returncode, report


@pytest.fixture(scope="module")
def fail_run(tmp_path_factory):
    if BASH is None or NODE is None:
        pytest.skip("bash or Node.js unavailable")
    return scan(FAIL_DIST, tmp_path_factory.mktemp("fail"))


@pytest.fixture(scope="module")
def pass_run(tmp_path_factory):
    if BASH is None or NODE is None:
        pytest.skip("bash or Node.js unavailable")
    return scan(PASS_DIST, tmp_path_factory.mktemp("pass"))


def automatic_block_rows() -> list[tuple[str, str]]:
    rows = []
    for line in SLOP_RULES.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else []
        if len(cells) == 5 and cells[1].startswith("automatic block"):
            proof = re.findall(r"`([a-z0-9-]+)`", cells[4])
            rows.append((cells[0], proof[0] if proof else ""))
    return rows


AUTO_ROWS = automatic_block_rows()


def test_table_has_automatic_block_rows():
    assert len(AUTO_ROWS) >= 8
    assert all(rule for _family, rule in AUTO_ROWS), "every automatic block row names the rule its fail fixture proves"


def test_vendored_detector_hash_check_passes():
    result = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/check-vendored-detector.py")], cwd=ROOT,
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


def test_tampered_vendored_byte_fails_hash_check(tmp_path):
    vendor = tmp_path / "chwezi-slop"
    shutil.copytree(ROOT / "scripts/vendor/chwezi-slop", vendor)
    target = vendor / "tools/slop-detector/lib/util.mjs"
    data = bytearray(target.read_bytes())
    data[10] = (data[10] + 1) % 256
    target.write_bytes(bytes(data))
    result = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/check-vendored-detector.py"),
                             "--vendor-dir", str(vendor), "--no-source"], capture_output=True, text=True)
    assert result.returncode == 1
    assert "util.mjs" in result.stdout


@needs_node
def test_website_pack_validates():
    result = subprocess.run([NODE, str(ROOT / "scripts/validate-slop-pack.mjs")], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


def test_fail_fixture_exits_1(fail_run):
    code, report = fail_run
    assert code == 1
    assert report["exit_code"] == 2


def test_pass_fixture_exits_0(pass_run):
    code, report = pass_run
    assert code == 0
    assert report["summary"]["by_severity"]["block"] == 0
    assert report["summary"]["by_severity"]["warning"] == 0


@needs_bash
def test_missing_dist_exits_5_not_assessed(tmp_path):
    code, report = scan(tmp_path / "does-not-exist", tmp_path)
    assert code == 5
    assert report["status"] == "NOT_ASSESSED"


@pytest.mark.parametrize("run_name", ["fail_run", "pass_run"])
def test_report_has_detector_shape(run_name, request):
    _code, report = request.getfixturevalue(run_name)
    for key in ("tool", "version", "registry_sha256", "findings", "not_assessed", "waived", "errors", "summary", "exit_code"):
        assert key in report, key
    assert report["tool"] == "chwezi-slop"
    for finding in report["findings"]:
        for key in ("rule", "as_overlay", "severity", "evidence_mode", "file", "line", "message"):
            assert key in finding, key


@pytest.mark.parametrize("family,rule", AUTO_ROWS, ids=[f for f, _r in AUTO_ROWS])
def test_automatic_block_family_is_proved(family, rule, fail_run, pass_run):
    _code, fail_report = fail_run
    _code, pass_report = pass_run
    hits = [f for f in fail_report["findings"] if f["rule"] == rule]
    assert hits, f"{family}: {rule} did not fire on the fail fixture"
    assert any(f["severity"] in ("block", "warning") for f in hits), f"{family}: {rule} fired only as advisory"
    assert not [f for f in pass_report["findings"] if f["rule"] == rule], f"{family}: {rule} fired on the pass fixture"


@needs_bash
def test_tampered_vendored_detector_makes_scan_not_assessed(tmp_path):
    engine = tmp_path / "engine"
    (engine / "scripts").mkdir(parents=True)
    (engine / "quality").mkdir()
    for name in ("slop-scan.sh", "slop-scan-run.mjs"):
        shutil.copy2(ROOT / "scripts" / name, engine / "scripts" / name)
    shutil.copytree(ROOT / "scripts/vendor", engine / "scripts/vendor")
    shutil.copy2(ROOT / "quality/slop-rules.website.json", engine / "quality/slop-rules.website.json")
    registry = engine / "scripts/vendor/chwezi-slop/tools/slop-detector/rules/registry.json"
    registry.write_text(registry.read_text(encoding="utf-8").replace('"block"', '"advisory"', 1), encoding="utf-8")
    work = tmp_path / "work"
    work.mkdir()
    code, report = scan(FAIL_DIST, work, engine=engine)
    assert code == 5
    assert "tampered" in report["reason"]


@needs_bash
def test_visitor_mode_from_strategy_brief(tmp_path):
    brief = tmp_path / "strategy-brief.json"
    brief.write_text(json.dumps({"artifact": "strategy-brief", "version": 1, "project": "fixture", "owner": "strategy-lead",
                                 "status": "approved", "updated": "2026-09-29",
                                 "pages": [{"route": "/", "visitor_mode": "persuade"}]}), encoding="utf-8")
    code, report = scan(PASS_DIST, tmp_path, env_extra={"STRATEGY_BRIEF": str(brief)})
    assert code == 0
    modes = {run["mode"] for run in report["runs"]}
    assert "persuade" in modes
