import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_local_website_fixture_benchmark_is_deterministic():
    command = [sys.executable, str(ROOT / "scripts/website_fixture_benchmark.py")]
    first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    assert json.loads(first.stdout) == json.loads(second.stdout)
    result = json.loads(first.stdout)
    assert result["status"] == "PASS"
    assert result["evidence_type"] == "lab fixture only"
    assert result["field_core_web_vitals"] == "NOT ASSESSED"
