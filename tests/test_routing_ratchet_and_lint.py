"""M10-03 tests: owned negatives, rank-1 ratchet, fixture lint and Tier-1 lint refinements."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


ROUTING = _load("website_routing", "scripts/routing-smoke-test.py")
CONTRACTS = _load("website_contracts", "scripts/validate-skill-contracts.py")


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/routing-smoke-test.py"), *args], capture_output=True, text=True, encoding="utf-8")


def _fixture_copy(tmp_path: Path, mutate) -> Path:
    data = json.loads((ROOT / "tests/routing/fixtures.json").read_text(encoding="utf-8"))
    mutate(data)
    path = tmp_path / "fixtures.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_live_fixtures_pass_with_floor_and_lint():
    result = _run("--min-rank1", "92", "--lint-fixtures")
    assert result.returncode == 0, result.stdout
    assert "owned negatives:" in result.stdout


def test_floor_above_measured_fails():
    result = _run("--min-rank1", "100")
    assert result.returncode == 1
    assert "below the ratchet floor" in result.stdout


def test_owner_ranked_below_self_fails(tmp_path):
    # Seeded regression: deploy is the true owner of this prompt, so declaring it a negative of
    # deploy owned by observability must fail.
    def mutate(data):
        data["negatives"] = [{"id": "seeded", "skill": "deploy", "prompt": "Publish the built site to production hosting, run smoke checks afterwards and prove rollback readiness", "owner": "observability"}]
    result = _run("--fixtures", str(_fixture_copy(tmp_path, mutate)))
    assert result.returncode == 1
    assert "negative seeded" in result.stdout


def test_cross_engine_owner_is_not_assessed():
    docs = ROUTING.corpus()
    status, _ = ROUTING.check_negative({"skill": "seo-audit", "prompt": "Pick the typeface for the invoice PDF", "owner": "chwezi-design-engine/font-selection-and-pairing"}, docs)
    assert status == "NOT_ASSESSED"


def test_slug_lint_catches_slug_bearing_prompt():
    assert ROUTING.lint_prompt("Run the accessibility audit now", "accessibility-audit", "")
    assert ROUTING.lint_prompt("Use the 02-seo-audit skill", "02-seo-audit", "")
    assert ROUTING.lint_prompt("alpha beta gamma delta", "x", "alpha beta gamma delta")
    assert ROUTING.lint_prompt("Check keyboard focus on the live site", "accessibility-audit", "Use when auditing") == []


def test_fence_stripping_hides_headings_inside_code():
    text = "## Use When\nreal\n```md\n## Workflow\n```\n~~~~\n## Outputs\n~~~\n~~~~\n"
    stripped = CONTRACTS.strip_fences(text)
    assert "## Workflow" not in stripped and "## Outputs" not in stripped
    assert "## Use When" in stripped


def test_negated_triggers_are_stripped_globally():
    assert CONTRACTS.has_positive_trigger("Use when building pages; do not use when auditing.")
    assert not CONTRACTS.has_positive_trigger("Do not use when auditing a site; never use for SEO.")


def test_host_strict_yaml_subset():
    assert CONTRACTS.host_strict_yaml("name: ok\n\tdescription: tab")
    assert CONTRACTS.host_strict_yaml('name: ok\ndescription: "unclosed')
    assert CONTRACTS.host_strict_yaml("name: ok\ndescription: Use when a: b")
    assert CONTRACTS.host_strict_yaml("name: ok\ndescription: Use when building.\nmetadata:\n  portable: true") == []


def test_frontmatter_exemption_is_rejected(tmp_path):
    folder = tmp_path / "example"
    folder.mkdir()
    skill = folder / "SKILL.md"
    skill.write_text("---\nname: example\ndescription: Use when testing.\nmetadata:\n  lint_exempt: true\n---\n# Example\n", encoding="utf-8")
    findings = CONTRACTS.validate_skill(skill, 500, 350)
    assert any(code == "frontmatter_exemption" for code, _, _ in findings)


def test_exemptions_are_validator_owned(tmp_path, monkeypatch):
    folder = tmp_path / "example"
    folder.mkdir()
    skill = folder / "SKILL.md"
    skill.write_text("---\nname: example\ndescription: Use when testing.\n---\n# Example\n", encoding="utf-8")
    before = {code for code, _, _ in CONTRACTS.validate_skill(skill, 500, 350)}
    assert "missing_workflow" in before
    monkeypatch.setattr(CONTRACTS, "EXEMPTIONS", {"missing_workflow": {"example": "test reason"}})
    after = {code for code, _, _ in CONTRACTS.validate_skill(skill, 500, 350)}
    assert "missing_workflow" not in after
