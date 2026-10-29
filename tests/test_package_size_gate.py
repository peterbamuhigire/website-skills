from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_size_gate", ROOT / "scripts/validate-checkout-size.py")
GATE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(GATE)


def fixture_root(tmp_path: Path) -> Path:
    root = tmp_path / "engine"
    skills = root / "skills"
    plugin_dir = root / ".claude-plugin"
    plugin_dir.mkdir(parents=True)
    rows = []
    plugin_paths = []
    for category, name in [("alpha", "one"), ("beta", "two")]:
        folder = skills / category / name
        folder.mkdir(parents=True)
        rel = f"skills/{category}/{name}/SKILL.md"
        (folder / "SKILL.md").write_text(f"---\nname: {name}\n---\n# {name}\n", encoding="utf-8")
        rows.append({"id": name, "path": rel, "status": "active"})
        plugin_paths.append(f"./skills/{category}/{name}/")
    (skills / "manifest.yml").write_text(json.dumps({"canonical_count": 2, "skills": rows}), encoding="utf-8")
    (plugin_dir / "plugin.json").write_text(json.dumps({"name": "website", "version": "1.1.0", "skills": plugin_paths}), encoding="utf-8")
    (plugin_dir / "marketplace.json").write_text(json.dumps({"name": "chwezi-website", "plugins": [{"name": "website", "version": "1.1.0", "source": "./"}]}), encoding="utf-8")
    return root


def test_valid_manifests_have_exact_identity_and_path_parity(tmp_path):
    root = fixture_root(tmp_path)
    assert GATE.validate_manifests(root) == []


def test_extra_plugin_path_fails_exact_parity(tmp_path):
    root = fixture_root(tmp_path)
    extra = root / "skills/extra/ghost"
    extra.mkdir(parents=True)
    (extra / "SKILL.md").write_text("---\nname: ghost\n---\n# Ghost\n", encoding="utf-8")
    path = root / ".claude-plugin/plugin.json"
    data = json.loads(path.read_text())
    data["skills"].append("./skills/extra/ghost/")
    path.write_text(json.dumps(data))
    assert any("exactly match" in finding for finding in GATE.validate_manifests(root))


def test_registry_identity_mismatch_fails(tmp_path):
    root = fixture_root(tmp_path)
    path = root / "skills/manifest.yml"
    data = json.loads(path.read_text())
    data["skills"][0]["id"] = "wrong-name"
    path.write_text(json.dumps(data))
    assert any("identity mismatch" in finding for finding in GATE.validate_manifests(root))


def test_marketplace_identity_mismatch_fails(tmp_path):
    root = fixture_root(tmp_path)
    path = root / ".claude-plugin/marketplace.json"
    data = json.loads(path.read_text())
    data["plugins"][0]["version"] = "9.9.9"
    path.write_text(json.dumps(data))
    assert any("identity/version" in finding for finding in GATE.validate_manifests(root))


def test_symlink_escape_fails_closed(tmp_path):
    root = fixture_root(tmp_path)
    outside = tmp_path / "outside"
    outside.write_text("outside", encoding="utf-8")
    (root / "escape").symlink_to(outside)
    with pytest.raises(GATE.GateError, match="escapes checkout"):
        GATE.count_entries(root)


def test_external_manifest_symlink_is_rejected_before_manifest_read(tmp_path):
    root = fixture_root(tmp_path)
    external = tmp_path / "external-plugin.json"
    external.write_text(json.dumps({"name": "outside", "version": "1", "skills": []}), encoding="utf-8")
    plugin = root / ".claude-plugin/plugin.json"
    plugin.unlink()
    plugin.symlink_to(external)
    with pytest.raises(GATE.GateError, match="escapes checkout"):
        GATE.run(root)


def test_broken_symlink_fails_closed(tmp_path):
    root = fixture_root(tmp_path)
    (root / "broken").symlink_to(root / "missing")
    with pytest.raises(GATE.GateError, match="broken or unreadable symlink"):
        GATE.count_entries(root)


def test_unreadable_directory_fails_closed(tmp_path, monkeypatch):
    root = fixture_root(tmp_path)
    real_scandir = os.scandir

    def denied(path):
        if Path(path) == root.resolve():
            raise PermissionError("fixture unreadable")
        return real_scandir(path)

    monkeypatch.setattr(GATE.os, "scandir", denied)
    with pytest.raises(GATE.GateError, match="cannot read directory"):
        GATE.count_entries(root)


def test_both_hard_caps_fail_closed(tmp_path, monkeypatch):
    root = fixture_root(tmp_path)
    monkeypatch.setattr(GATE, "MAX_CHECKOUT_ENTRIES", 1)
    monkeypatch.setattr(GATE, "MAX_PACKAGE_ENTRIES", 1)
    errors, full, package, _, _ = GATE.run(root)
    assert full > 1 and package > 1
    assert any("full checkout entries" in finding for finding in errors)
    assert any("package entries" in finding for finding in errors)
