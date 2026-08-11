import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "website-kaizen"
BENCHMARK = ROOT / "scripts" / "website_fixture_benchmark.py"
ROLLBACK = ROOT / "scripts" / "rollback.sh"


def bash_executable() -> str:
    git_bash = Path(r"C:\Program Files\Git\bin\bash.exe")
    if git_bash.is_file():
        return str(git_bash)
    candidate = shutil.which("bash")
    if candidate:
        return candidate
    raise AssertionError("Git Bash or bash is required for the rollback shell tests")


def run_benchmark(fixture: Path, budgets: Path | None = None) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(BENCHMARK), "--fixture", str(fixture)]
    if budgets is not None:
        command.extend(["--budgets", str(budgets)])
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)


def test_drift_check_is_bounded_and_repeatable(tmp_path):
    wrapper = (ROOT / "scripts/drift-check.sh").read_text(encoding="utf-8")
    checker = (ROOT / "scripts/drift_check.py").read_text(encoding="utf-8")
    assert "drift_check.py" in wrapper
    assert "find " not in wrapper
    assert "MAX_MARKDOWN_FILES" in checker
    assert "MAX_TOTAL_BYTES" in checker
    assert '"git",\n        "ls-files"' in checker
    assert "date.today" not in checker

    report_dir = tmp_path / "reports"
    command = [
        sys.executable,
        str(ROOT / "scripts/drift_check.py"),
        "--root",
        str(ROOT),
        "--reports-dir",
        str(report_dir),
        "--as-of",
        "2026-08-11",
    ]
    first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    first_report = (report_dir / "drift-report.md").read_text(encoding="utf-8")
    second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    second_report = (report_dir / "drift-report.md").read_text(encoding="utf-8")
    assert first.returncode == 0, first.stdout + first.stderr
    assert second.returncode == 0, second.stdout + second.stderr
    assert first.stdout == second.stdout
    assert first_report == second_report


def test_fixture_mutations_fail_the_matching_lab_gate(tmp_path):
    mutated = tmp_path / "website-kaizen"
    shutil.copytree(FIXTURE, mutated)

    index = mutated / "index.html"
    index.write_text(index.read_text(encoding="utf-8").replace('href="about.html"', 'href="missing.html"', 1), encoding="utf-8")
    broken = run_benchmark(mutated)
    broken_result = json.loads(broken.stdout)
    assert broken.returncode == 1
    assert broken_result["status"] == "FAIL"
    assert broken_result["pages"][0]["links"]["status"] == "FAIL"
    assert "missing.html" in broken_result["pages"][0]["links"]["broken"]

    index.write_text(index.read_text(encoding="utf-8").replace('href="missing.html"', 'href="about.html"', 1).replace("<main>", "<section>", 1).replace("</main>", "</section>", 1), encoding="utf-8")
    semantics = run_benchmark(mutated)
    semantics_result = json.loads(semantics.stdout)
    assert semantics.returncode == 1
    assert semantics_result["pages"][0]["semantics"]["status"] == "FAIL"

    budgets = tmp_path / "budgets.json"
    budgets.write_text(json.dumps({"global": {"total_weight_kb": 0, "js_kb_gzip": 0, "css_kb_gzip": 0}}), encoding="utf-8")
    budget = run_benchmark(mutated, budgets)
    budget_result = json.loads(budget.stdout)
    assert budget.returncode == 1
    assert budget_result["performance_budget_inputs"]["status"] == "FAIL"


def rollback_environment(known_hosts: Path) -> dict[str, str]:
    return {
        "DEPLOY_HOST": "example.invalid",
        "DEPLOY_USER": "release",
        "DEPLOY_KEY": "test-only-key",
        "DEPLOY_PATH": "/srv/example/releases",
        "DEPLOY_KNOWN_HOSTS": str(known_hosts),
        "ROLLBACK_APPROVED": "yes",
        "ROLLBACK_TARGET": "/srv/example/releases",
        "ROLLBACK_REASON": "wave2 validation only",
        "RELOAD_SERVICE": "none",
        "ROLLBACK_VALIDATE_ONLY": "1",
    }


def run_rollback(environment: dict[str, str]) -> subprocess.CompletedProcess[str]:
    merged = os.environ.copy()
    merged.update(environment)
    return subprocess.run(
        [bash_executable(), str(ROLLBACK)],
        cwd=ROOT,
        env=merged,
        capture_output=True,
        text=True,
        check=False,
    )


def test_rollback_validation_and_static_safety_contract(tmp_path):
    script = ROLLBACK.read_text(encoding="utf-8")
    ci_template = (ROOT / "templates/ci/website.yml").read_text(encoding="utf-8")
    assert "ROLLBACK_APPROVED" in script
    assert "ROLLBACK_TARGET" in script
    assert '"$target"/releases/*' in script
    assert "LAST_SAFE_CURRENT" in script
    assert "LAST_SAFE_PREVIOUS" in script
    assert "recover_and_verify" in script
    assert '"$target"/.rollback.*' in script
    assert '"$target"/.rollback-recovery.*' in script
    assert "refusing unsafe rollback temporary path" in script
    assert "refusing unsafe rollback recovery temporary path" in script
    assert "StrictHostKeyChecking=yes" in script
    assert "UserKnownHostsFile" in script
    assert "sudo -- systemctl reload" in script
    assert "accept-new" not in script
    assert "$HOME/.ssh" not in script
    assert "ROLLBACK_VALIDATE_ONLY" in script
    for variable in ("DEPLOY_KNOWN_HOSTS", "ROLLBACK_APPROVED", "ROLLBACK_TARGET", "ROLLBACK_REASON", "RELOAD_SERVICE"):
        assert f"{variable}:" in ci_template

    known_hosts = tmp_path / "known_hosts"
    known_hosts.write_text("example.invalid ssh-ed25519 test-key\n", encoding="utf-8")
    valid = run_rollback(rollback_environment(known_hosts))
    assert valid.returncode == 0, valid.stdout + valid.stderr
    assert "remote state NOT ASSESSED" in valid.stdout

    missing_authority = rollback_environment(known_hosts)
    missing_authority.pop("ROLLBACK_APPROVED")
    assert run_rollback(missing_authority).returncode == 3

    mismatched_target = rollback_environment(known_hosts)
    mismatched_target["ROLLBACK_TARGET"] = "/srv/other"
    assert run_rollback(mismatched_target).returncode == 3

    escaped_target = rollback_environment(known_hosts)
    escaped_target["DEPLOY_PATH"] = "/srv/example/releases/../escape"
    escaped_target["ROLLBACK_TARGET"] = escaped_target["DEPLOY_PATH"]
    assert run_rollback(escaped_target).returncode == 3

    unapproved_service = rollback_environment(known_hosts)
    unapproved_service["RELOAD_SERVICE"] = "sh -c rm"
    assert run_rollback(unapproved_service).returncode == 3
