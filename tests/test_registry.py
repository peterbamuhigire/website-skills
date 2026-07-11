import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_registry_validator():
    result = subprocess.run([sys.executable, str(ROOT / "scripts/validate-skill-registry.py")], cwd=ROOT)
    assert result.returncode == 0

def test_fixture_contracts_are_declared():
    fixture = json.loads((ROOT / "fixtures/website-basic/fixture.json").read_text())
    assert len(fixture["gates"]) == 7
    assert all(contract.endswith("@1") for contract in fixture["contracts"])

def test_every_gate_has_pass_and_fail_fixture():
    cases = json.loads((ROOT / "tests/gates/cases.json").read_text())["cases"]
    assert len(cases) == 7
    for case in cases:
        pass_path = ROOT / "tests/gates" / case["pass"]
        fail_path = ROOT / "tests/gates" / case["fail"]
        assert pass_path.is_file() and fail_path.is_file()
        if pass_path.suffix == ".json":
            assert json.loads(pass_path.read_text())["expected"] == "pass"
            assert json.loads(fail_path.read_text())["expected"] == "fail"
