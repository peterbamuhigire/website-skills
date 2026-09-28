import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_manifest_and_current_documentation_counts_match_filesystem():
    manifest = json.loads((ROOT / "skills/manifest.yml").read_text(encoding="utf-8"))
    skills = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
    counts = Counter(path.parent.parent.name for path in skills)
    assert manifest["canonical_count"] == len(skills)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    # The 2026-09-28 README states the total in prose and the categories in a table; the older
    # tree form is still accepted. Either way the numbers must match the filesystem.
    total = re.search(r"Current skill count:\s*(\d+)", readme) or re.search(r"\bIts (\d+) active skills\b", readme)
    assert total and int(total.group(1)) == len(skills)
    readme_counts = {
        category: int(count)
        for category, count in re.findall(r"(?:\|--|`--)\s+([a-z-]+)/[^\n]*\((\d+) skills\)", readme)
    }
    readme_counts.update({
        category: int(count)
        for category, count in re.findall(r"^\|\s*`([a-z-]+)`\s*\|\s*(\d+)\s*\|", readme, re.MULTILINE)
    })
    assert readme_counts == dict(counts)
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    assert {
        category: int(count)
        for category, count in re.findall(r"\*\*`([a-z-]+)/`\*\*\s*\((\d+)\)", claude)
    } == dict(counts)


def test_relocation_map_is_the_manifest_route_contract():
    manifest = json.loads((ROOT / "skills/manifest.yml").read_text(encoding="utf-8"))
    relocation_map = (ROOT / "docs/relocation-map.md").read_text(encoding="utf-8")
    for old_name, destination in manifest["relocations"].items():
        assert f"| `{old_name}` | `{destination}` |" in relocation_map
        assert destination.startswith("design-system-skills:")


def test_quarantined_provenance_has_no_active_library_metadata():
    register = (ROOT / "skills/orchestration/premium-ui-ux-design/references/source-register.md").read_text(encoding="utf-8").lower()
    assert "active provenance" in register
    assert "quarantined provenance" in register
    assert "z-library" not in register
    assert "z-lib" not in register


def test_rollback_helper_has_authority_target_and_recovery_boundaries():
    script = (ROOT / "scripts/rollback.sh").read_text(encoding="utf-8")
    assert "ROLLBACK_APPROVED" in script
    assert "ROLLBACK_TARGET" in script
    assert "UserKnownHostsFile" in script
    assert "StrictHostKeyChecking=yes" in script
    assert "mktemp" in script
    assert "recover_original" in script
    assert "accept-new" not in script
    assert "$HOME/.ssh" not in script
