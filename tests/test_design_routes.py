import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_skill_registry", ROOT / "scripts/validate-skill-registry.py")
REGISTRY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REGISTRY)


def make_design_engine(root: Path, *names: str) -> Path:
    for name in names:
        skill = root / "skills" / "01-group" / name
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")
    return root


def test_dangling_design_route_fails(tmp_path):
    website = tmp_path / "website"
    website.mkdir()
    (website / "AGENTS.md").write_text(
        "- `design-system-skills:brand-visual-identity`\n- `design-system-skills:no-such-skill`\n"
        "<!-- design-system-skills:trigger v2 -->\n",
        encoding="utf-8",
    )
    design = make_design_engine(tmp_path / "design", "brand-visual-identity")
    status, errors = REGISTRY.check_design_routes(website, design)
    assert status == "FAIL"
    assert len(errors) == 1 and "no-such-skill" in errors[0]


def test_history_files_are_not_live_routes(tmp_path):
    website = tmp_path / "website"
    (website / "docs" / "engine-upgrade-july-2026").mkdir(parents=True)
    (website / "docs" / "engine-upgrade-july-2026" / "plan.md").write_text("design-system-skills:brand-alignment\n", encoding="utf-8")
    design = make_design_engine(tmp_path / "design", "brand-visual-identity")
    assert REGISTRY.check_design_routes(website, design) == ("PASS", [])


def test_missing_design_engine_is_not_assessed(tmp_path):
    status, messages = REGISTRY.check_design_routes(tmp_path, tmp_path / "absent")
    assert status == "NOT_ASSESSED"
    assert messages


def test_live_tree_design_routes_resolve():
    status, errors = REGISTRY.check_design_routes()
    assert status in {"PASS", "NOT_ASSESSED"}
    assert errors == [] or status == "NOT_ASSESSED"
