"""The maintained five-page worked example keeps passing its own gates (WSK2-02).

`examples/service-site-five-page/` is a complete synthetic deliverable: brief, five pages, a release
record and a rollback plan. This test runs every gate the release record claims, against the real
scripts, and checks that the recorded outcome is what happens. It then injects one defect per gate into
a copy of the site and requires the matching gate to fail, so the example also shows the gates are
sensitive and not only that they pass on clean input. Gates that need a browser, a locked toolchain or a
deployment target are recorded as not assessed in the release record and are not run here.
"""

from __future__ import annotations

import json
import os
import random
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "service-site-five-page"
SITE = EXAMPLE / "site"
EVIDENCE = json.loads((EXAMPLE / "release-evidence.json").read_text(encoding="utf-8"))
README = (EXAMPLE / "README.md").read_text(encoding="utf-8")
SCHEMA = json.loads((ROOT / "templates/project-artifacts/core-artifacts.schema.json").read_text(encoding="utf-8"))
ROUTES = ["/", "/services/", "/about/", "/contact/", "/privacy/"]
GATES = {gate["gate"]: gate for gate in EVIDENCE["gates"]}


def have(tool: str) -> bool:
    return shutil.which(tool) is not None


def build_budgets(path: Path) -> Path:
    """The engine's own global budgets and route overrides, applied to the five example routes."""
    budgets = json.loads((ROOT / "performance-budgets.json").read_text(encoding="utf-8"))
    routes = {route: budgets["routes"].get(route, {}) for route in ROUTES}
    path.write_text(json.dumps({"global": budgets["global"], "routes": routes}), encoding="utf-8")
    return path


def argv_for(command: str, site: Path, budgets: Path) -> list[str]:
    parts = shlex.split(command.format(site=site, budgets=budgets))
    parts = [sys.executable if p == "python3" else p for p in parts]
    return [str(ROOT / p) if p.startswith("scripts/") else p for p in parts]


def run_gate(gate_id: str, site: Path, workdir: Path):
    gate = GATES[gate_id]
    tool = shlex.split(gate["command"])[0]
    if not have("bash" if tool == "bash" else tool) and tool != "python3":
        pytest.skip(f"{tool} unavailable: {gate_id} NOT_ASSESSED")
    budgets = build_budgets(workdir / "budgets.json")
    cwd = workdir
    if gate_id == "secrets-scan":
        if not have("git"):
            pytest.skip("git unavailable: secrets-scan NOT_ASSESSED")
        cwd = workdir / "scratch-repo"
        if cwd.exists():
            shutil.rmtree(cwd)
        shutil.copytree(site, cwd)
        subprocess.run(["git", "init", "-q"], cwd=cwd, check=True)
        subprocess.run(["git", "add", "."], cwd=cwd, check=True)
    env = {**os.environ, "REPORT": str(workdir / "report.txt")}
    return subprocess.run(argv_for(gate["command"], site, budgets), cwd=cwd, capture_output=True, text=True, env=env, timeout=120)


# --- the release record is well formed and honest ------------------------------------------------


def test_release_record_has_the_engine_artefact_header():
    header = SCHEMA["$defs"]["header"]
    assert [key for key in header["required"] if key not in EVIDENCE] == []
    assert EVIDENCE["version"] == header["properties"]["version"]["const"]
    assert EVIDENCE["status"] in header["properties"]["status"]["enum"]


def test_a_synthetic_site_with_a_blocking_gate_or_unrun_gates_is_never_recorded_as_released():
    blocking = [g for g in EVIDENCE["gates"] if g.get("blocks_release")]
    assert EVIDENCE["synthetic"] is True
    assert (blocking or EVIDENCE["not_assessed"]) and EVIDENCE["release"]["decision"] == "BLOCKED"
    assert EVIDENCE["waivers"] == []


def test_every_recorded_status_matches_its_expected_exit_and_every_gap_has_a_reason():
    for gate in EVIDENCE["gates"]:
        assert gate["status"] in {"pass", "fail"}
        assert (gate["status"] == "pass") == (gate["expected_exit"] == 0), gate["gate"]
        if gate["status"] == "fail":
            assert gate.get("blocks_release") is True and gate.get("failing_checks")
    for gap in EVIDENCE["not_assessed"]:
        assert gap["reason"].strip() and "command" not in gap


def test_the_readme_names_every_gate_in_the_release_record():
    names = [g["gate"] for g in EVIDENCE["gates"]] + [g["gate"] for g in EVIDENCE["not_assessed"]]
    assert [name for name in names if name not in README] == []


def test_the_site_is_five_pages_with_the_expected_routes():
    pages = sorted(p.relative_to(SITE).as_posix() for p in SITE.rglob("*.html"))
    assert pages == ["about/index.html", "contact/index.html", "index.html", "privacy/index.html", "services/index.html"]


# --- every recorded gate really behaves as recorded ----------------------------------------------


@pytest.mark.parametrize("gate_id", sorted(GATES))
def test_recorded_gate_outcome_is_what_the_real_script_returns(gate_id, tmp_path):
    result = run_gate(gate_id, SITE, tmp_path)
    assert result.returncode == GATES[gate_id]["expected_exit"], result.stdout + result.stderr


def test_the_security_txt_gate_fails_only_on_the_placeholder_domain(tmp_path):
    result = run_gate("security-txt", SITE, tmp_path)
    failures = [line for line in result.stdout.splitlines() if line.startswith("FAIL")]
    assert failures == ["FAIL placeholder value found"], result.stdout


# --- the gates are sensitive: one injected defect per gate ---------------------------------------


def mutated_copy(tmp_path: Path, edit) -> Path:
    site = tmp_path / "mutant"
    if site.exists():
        shutil.rmtree(site)
    shutil.copytree(SITE, site)
    edit(site)
    return site


def replace_in(path: str, old: str, new: str):
    def edit(site: Path):
        target = site / path
        text = target.read_text(encoding="utf-8")
        assert old in text, f"{old!r} not in {path}"
        target.write_text(text.replace(old, new, 1), encoding="utf-8")
    return edit


def add_big_image(site: Path):
    (site / "assets" / "big.jpg").write_bytes(bytes(random.Random(3).getrandbits(8) for _ in range(300 * 1024)))
    target = site / "index.html"
    target.write_text(target.read_text(encoding="utf-8").replace("<main", '<img src="/assets/big.jpg" width="1200" height="600" alt="" fetchpriority="high"><main', 1), encoding="utf-8")


# (gate, injected defect, edit, expected failure exit, text the gate must print). Pinning the exit code and
# the message means a crash or a usage error cannot pass for a catch.
MUTATIONS = [
    ("html-perf-lint", "an image without dimensions", replace_in("index.html", "<main", '<img src="/assets/og-card.png" alt=""><main'), 1, "HPL-002"),
    ("html-perf-lint", "a render-blocking head script", replace_in("index.html", "</head>", '<script src="/app.js"></script></head>'), 1, "HPL-001"),
    ("route-weight-budget", "a 300 KB above-the-fold image", add_big_image, 2, "above_fold_image_kb"),
    ("metadata-audit", "a page without html lang", replace_in("services/index.html", '<html lang="en-GB">', "<html>"), 1, "<html lang>"),
    ("metadata-audit", "a viewport that blocks zoom", replace_in("about/index.html", "initial-scale=1", "initial-scale=1, user-scalable=no"), 1, "blocks zoom"),
    ("metadata-audit", "a page without a canonical link", replace_in("contact/index.html", '<link rel="canonical" href="https://example.com/contact/">', ""), 1, "rel=canonical"),
    ("banned-phrase-scan", "a filler phrase", replace_in("index.html", "Bicycle repairs, quoted before we start", "Welcome to our cutting-edge workshop"), 1, "matches /cutting"),
    ("content-link-graph", "a broken internal link", replace_in("about/index.html", 'href="/contact/">contact page', 'href="/gone/">contact page'), 1, "broken 1"),
    ("sri", "an external script without integrity", replace_in("index.html", "</head>", '<script src="https://cdn.example.net/x.js" defer></script></head>'), 1, "missing or invalid integrity"),
    ("slop-scan", "a banned primary font", replace_in("styles.css", '"Public Sans", system-ui', "Inter, system-ui"), 1, "block 1"),
    ("secrets-scan", "a credential-shaped string", replace_in("privacy/index.html", "<h1>", "<!-- AKIA" + "IOSFODNN7EXAMPLE --><h1>"), 1, "aws-access-key"),
]


@pytest.mark.parametrize("gate_id,defect,edit,exit_code,marker", MUTATIONS, ids=[f"{m[0]}: {m[1]}" for m in MUTATIONS])
def test_each_gate_fails_when_its_defect_is_injected(gate_id, defect, edit, exit_code, marker, tmp_path):
    site = mutated_copy(tmp_path, edit)
    result = run_gate(gate_id, site, tmp_path)
    output = result.stdout + result.stderr
    assert result.returncode == exit_code, f"{gate_id} did not catch {defect}\n{output}"
    assert marker in output, f"{gate_id} failed for another reason than {defect}\n{output}"


# --- the rollback helper's local validation, named in the README ---------------------------------


def test_rollback_helper_accepts_only_an_authorised_exact_target(tmp_path):
    if not have("bash"):
        pytest.skip("bash unavailable: rollback validation NOT_ASSESSED")
    (tmp_path / "known_hosts").write_text("", encoding="utf-8")
    base = {
        **os.environ,
        "DEPLOY_HOST": "host.invalid", "DEPLOY_USER": "deploy", "DEPLOY_KEY": "not-a-key",
        "DEPLOY_PATH": "/srv/site", "DEPLOY_KNOWN_HOSTS": str(tmp_path / "known_hosts"),
        "ROLLBACK_VALIDATE_ONLY": "1",
    }
    script = str(ROOT / "scripts" / "rollback.sh")

    def run(**extra):
        env = {k: v for k, v in base.items() if k not in {"ROLLBACK_APPROVED", "ROLLBACK_TARGET", "ROLLBACK_REASON"}}
        env.update(extra)
        return subprocess.run(["bash", script], capture_output=True, text=True, env=env, cwd=tmp_path)

    assert run().returncode == 3
    assert run(ROLLBACK_APPROVED="yes", ROLLBACK_TARGET="/srv/other", ROLLBACK_REASON="example drill").returncode == 3
    ok = run(ROLLBACK_APPROVED="yes", ROLLBACK_TARGET="/srv/site", ROLLBACK_REASON="example drill")
    assert ok.returncode == 0 and "remote state NOT ASSESSED" in ok.stdout
