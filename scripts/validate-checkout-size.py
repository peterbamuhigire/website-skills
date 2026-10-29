#!/usr/bin/env python3
"""Fail-closed package-size and marketplace-manifest integrity gate."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import stat
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_CHECKOUT_ENTRIES = 5_000
MAX_PACKAGE_ENTRIES = 5_000
PACKAGE_EXCLUSIONS = {".git", ".cache", ".venv", "venv", "node_modules", "__pycache__"}
NAME_RE = re.compile(r"^name:\s*['\"]?([A-Za-z0-9][A-Za-z0-9._-]*)['\"]?\s*$", re.MULTILINE)


class GateError(RuntimeError):
    pass


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def count_entries(root: Path, excluded_dirs: set[str] | None = None) -> tuple[int, int]:
    """Count regular files and symlink entries; never follow links or ignore scan errors."""
    try:
        resolved_root = root.resolve(strict=True)
    except OSError as exc:
        raise GateError(f"cannot resolve root {root}: {exc}") from exc
    if not resolved_root.is_dir():
        raise GateError(f"root is not a directory: {root}")

    exclusions = excluded_dirs or set()
    count = 0
    symlinks = 0

    def walk(directory: Path, relative: Path) -> None:
        nonlocal count, symlinks
        try:
            with os.scandir(directory) as iterator:
                entries = sorted(iterator, key=lambda entry: entry.name)
        except OSError as exc:
            raise GateError(f"cannot read directory {relative.as_posix() or '.'}: {exc}") from exc

        for entry in entries:
            rel = relative / entry.name
            try:
                if entry.is_symlink():
                    symlinks += 1
                    try:
                        target = Path(entry.path).resolve(strict=True)
                    except OSError as exc:
                        raise GateError(f"broken or unreadable symlink {rel.as_posix()}: {exc}") from exc
                    if not _is_within(target, resolved_root):
                        raise GateError(f"symlink escapes checkout: {rel.as_posix()} -> {target}")
                    if not any(part in exclusions for part in rel.parts):
                        count += 1
                    continue

                if entry.is_dir(follow_symlinks=False):
                    if entry.name in exclusions:
                        continue
                    walk(Path(entry.path), rel)
                    continue

                mode = entry.stat(follow_symlinks=False).st_mode
                if not stat.S_ISREG(mode):
                    raise GateError(f"unsupported filesystem entry {rel.as_posix()}")
                if not any(part in exclusions for part in rel.parts):
                    count += 1
            except OSError as exc:
                raise GateError(f"cannot inspect {rel.as_posix()}: {exc}") from exc

    walk(resolved_root, Path())
    return count, symlinks


def _read_json(path: Path, label: str, errors: list[str]) -> dict | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label} unreadable: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return None
    return value


def validate_manifests(root: Path) -> list[str]:
    errors: list[str] = []
    registry = _read_json(root / "skills/manifest.yml", "skills manifest", errors)
    plugin = _read_json(root / ".claude-plugin/plugin.json", "plugin manifest", errors)
    marketplace = _read_json(root / ".claude-plugin/marketplace.json", "marketplace manifest", errors)
    if registry is None or plugin is None or marketplace is None:
        return errors

    rows = registry.get("skills")
    if not isinstance(rows, list):
        errors.append("skills manifest: skills must be a list")
        return errors
    active: dict[str, str] = {}
    ids: set[str] = set()
    for row in rows:
        if not isinstance(row, dict) or row.get("status") != "active":
            continue
        skill_id, rel = row.get("id"), row.get("path")
        if not isinstance(skill_id, str) or not isinstance(rel, str):
            errors.append("skills manifest: active row lacks string id/path")
            continue
        if skill_id in ids:
            errors.append(f"skills manifest: duplicate id {skill_id}")
        if rel in active.values():
            errors.append(f"skills manifest: duplicate path {rel}")
        ids.add(skill_id)
        active[skill_id] = rel
        candidate = (root / rel).resolve()
        if not rel.startswith("skills/") or not _is_within(candidate, root.resolve()) or not candidate.is_file():
            errors.append(f"skills manifest: unsafe or missing skill path {rel}")
            continue
        try:
            text = candidate.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"skills manifest: cannot read {rel}: {exc}")
            continue
        match = NAME_RE.search(text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else "")
        if not match or match.group(1) != skill_id:
            errors.append(f"skills manifest: identity mismatch for {rel}; expected {skill_id}")

    if registry.get("canonical_count") != len(active):
        errors.append(f"skills manifest: canonical_count {registry.get('canonical_count')} != active rows {len(active)}")

    found: dict[str, str] = {}
    skills_root = root / "skills"
    try:
        for path in sorted(skills_root.rglob("SKILL.md")):
            if any(part in {".git", "node_modules", "__pycache__", "_TEMPLATE"} for part in path.relative_to(root).parts):
                continue
            candidate = path.resolve(strict=True)
            if not _is_within(candidate, root.resolve()):
                errors.append(f"filesystem skill path escapes checkout: {path.relative_to(root).as_posix()}")
                continue
            try:
                text = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError) as exc:
                errors.append(f"cannot read skill file {path.relative_to(root).as_posix()}: {exc}")
                continue
            match = NAME_RE.search(text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else "")
            rel = path.relative_to(root).as_posix()
            if not match:
                errors.append(f"skill file lacks a valid frontmatter name: {rel}")
                continue
            skill_id = match.group(1)
            if skill_id in found:
                errors.append(f"filesystem skill identity duplicated: {skill_id}")
            found[skill_id] = rel
    except OSError as exc:
        errors.append(f"cannot enumerate skills directory: {exc}")

    if found != active:
        for skill_id in sorted(found.keys() - active.keys()):
            errors.append(f"skills manifest missing filesystem skill: {skill_id} ({found[skill_id]})")
        for skill_id in sorted(active.keys() - found.keys()):
            errors.append(f"skills manifest has missing filesystem skill: {skill_id} ({active[skill_id]})")
        for skill_id in sorted(found.keys() & active.keys()):
            if found[skill_id] != active[skill_id]:
                errors.append(f"skills manifest path mismatch for {skill_id}: {active[skill_id]} != {found[skill_id]}")

    plugin_name = plugin.get("name")
    plugin_version = plugin.get("version")
    plugin_paths = plugin.get("skills")
    if not isinstance(plugin_name, str) or not isinstance(plugin_version, str) or not isinstance(plugin_paths, list):
        errors.append("plugin manifest lacks name/version/skills list")
        plugin_paths = []
    dirs: list[str] = []
    for raw in plugin_paths:
        if not isinstance(raw, str) or not raw.startswith("./skills/") or not raw.endswith("/"):
            errors.append(f"plugin manifest has invalid skill path: {raw!r}")
            continue
        rel_dir = raw[2:-1]
        resolved = (root / rel_dir).resolve()
        if not _is_within(resolved, root.resolve()) or not (resolved / "SKILL.md").is_file():
            errors.append(f"plugin manifest has unsafe or missing skill path: {raw}")
            continue
        dirs.append(rel_dir + "/SKILL.md")
    expected_dirs = {rel for rel in active.values()}
    if len(dirs) != len(set(dirs)):
        errors.append("plugin manifest contains duplicate skill paths")
    if set(dirs) != expected_dirs:
        errors.append("plugin manifest skill paths do not exactly match active registry paths")

    marketplace_rows = marketplace.get("plugins")
    if not isinstance(marketplace_rows, list):
        errors.append("marketplace manifest: plugins must be a list")
        marketplace_rows = []
    root_plugins = [row for row in marketplace_rows if isinstance(row, dict) and row.get("source") in {"./", "."}]
    if len(root_plugins) != 1:
        errors.append("marketplace manifest must identify exactly one root plugin with source './'")
    else:
        row = root_plugins[0]
        if row.get("name") != plugin_name or row.get("version") != plugin_version:
            errors.append("marketplace root plugin identity/version does not match plugin manifest")
    return errors


def run(root: Path) -> tuple[list[str], int, int, int, int]:
    # Inspect every tree entry before reading manifests so an escaping manifest
    # symlink is rejected before it can cause an out-of-checkout read.
    full, full_symlinks = count_entries(root)
    package, package_symlinks = count_entries(root, PACKAGE_EXCLUSIONS)
    errors = validate_manifests(root)
    if full > MAX_CHECKOUT_ENTRIES:
        errors.append(f"full checkout entries {full} exceed immutable cap {MAX_CHECKOUT_ENTRIES}")
    if package > MAX_PACKAGE_ENTRIES:
        errors.append(f"package entries {package} exceed immutable cap {MAX_PACKAGE_ENTRIES}")
    return errors, full, package, full_symlinks, package_symlinks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        errors, full, package, full_symlinks, package_symlinks = run(args.root)
    except (GateError, OSError, RuntimeError) as exc:
        print(f"package-size: FAIL closed: {exc}", file=sys.stderr)
        return 2
    print(f"package-size: full={full}/{MAX_CHECKOUT_ENTRIES} entries, symlinks={full_symlinks}")
    print(f"package-size: package={package}/{MAX_PACKAGE_ENTRIES} entries, symlinks={package_symlinks}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"package-size: FAIL ({len(errors)} findings)", file=sys.stderr)
        return 1
    print("package-size: PASS (manifest identity/path parity and immutable entry caps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
