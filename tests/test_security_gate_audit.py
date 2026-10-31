"""The security gate's dependency-audit step must fail closed (WSK2-01).

`npm audit` exits non-zero both when it finds vulnerabilities and when it cannot audit at all
(no lockfile, registry unreachable). The gate used to read counts from whatever JSON came back, so
an error document produced `high=0 critical=0` and the gate carried on. These tests run the real
`scripts/security-gate.sh` against a stub `npm` on PATH, so no network and no lockfile are needed.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "security-gate.sh"
BASH = shutil.which("bash")
JQ = shutil.which("jq")

pytestmark = pytest.mark.skipif(BASH is None or JQ is None, reason="bash and jq are required: security-gate audit checks NOT_ASSESSED")

STUB = textwrap.dedent(
    """\
    #!/usr/bin/env bash
    # Stub npm: behaviour chosen by STUB_NPM_MODE. Only `npm audit` is expected.
    case "${STUB_NPM_MODE:-}" in
      clean)       echo '{"auditReportVersion":2,"vulnerabilities":{},"metadata":{"vulnerabilities":{"high":0,"critical":0}}}'; exit 0 ;;
      moderate)    echo '{"auditReportVersion":2,"vulnerabilities":{"pkg":{"name":"pkg","severity":"moderate","via":[]}},"metadata":{}}'; exit 0 ;;
      high)        echo '{"auditReportVersion":2,"vulnerabilities":{"pkg":{"name":"pkg","severity":"high","via":[]}},"metadata":{}}'; exit 1 ;;
      critical)    echo '{"auditReportVersion":2,"vulnerabilities":{"pkg":{"name":"pkg","severity":"critical","via":[]}},"metadata":{}}'; exit 1 ;;
      enolock)     echo '{"error":{"code":"ENOLOCK","summary":"This command requires an existing lockfile."}}'; echo "npm error code ENOLOCK" >&2; exit 1 ;;
      unreachable) echo '{"error":{"code":"ENOTFOUND","summary":"request to the registry failed"}}'; exit 1 ;;
      empty)       exit 1 ;;
      garbage)     echo 'this is not json'; exit 0 ;;
      noversion)   echo '{"vulnerabilities":{}}'; exit 0 ;;
    esac
    echo "stub npm: unknown mode" >&2
    exit 99
    """
)


def run_gate(tmp_path: Path, mode: str) -> subprocess.CompletedProcess:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    npm = bin_dir / "npm"
    npm.write_text(STUB, encoding="utf-8")
    npm.chmod(0o755)
    project = tmp_path / "project"
    project.mkdir(exist_ok=True)
    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}", "STUB_NPM_MODE": mode}
    env.pop("DIST_DIR", None)
    env.pop("REPORTS_DIR", None)
    return subprocess.run([BASH, str(GATE)], cwd=project, env=env, capture_output=True, text=True, timeout=60)


# The gate reaches its second step ("security headers") only when the audit step passed.
PASSED_AUDIT = "security-gate: security headers"


@pytest.mark.parametrize("mode", ["clean", "moderate"])
def test_completed_audit_without_blocking_findings_proceeds(tmp_path, mode):
    result = run_gate(tmp_path, mode)
    assert PASSED_AUDIT in result.stdout, result.stdout + result.stderr
    assert "npm audit high=0 critical=0" in result.stdout


@pytest.mark.parametrize("mode,expected", [("high", "0 critical, 1 high"), ("critical", "1 critical, 0 high")])
def test_completed_audit_with_blocking_findings_exits_1(tmp_path, mode, expected):
    result = run_gate(tmp_path, mode)
    assert result.returncode == 1, result.stdout + result.stderr
    assert expected in result.stderr
    assert PASSED_AUDIT not in result.stdout


@pytest.mark.parametrize("mode", ["enolock", "unreachable", "empty", "garbage", "noversion"])
def test_audit_that_did_not_complete_is_a_failure_not_a_pass(tmp_path, mode):
    result = run_gate(tmp_path, mode)
    assert result.returncode == 6, result.stdout + result.stderr
    assert "npm audit did not complete" in result.stderr
    assert PASSED_AUDIT not in result.stdout
    assert "high=0 critical=0" not in result.stdout
