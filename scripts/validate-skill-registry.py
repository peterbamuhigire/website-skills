#!/usr/bin/env python3
"""Validate and optionally regenerate the website-skills registry.

Uses only the Python standard library so it works on Windows and Linux.
The manifest is JSON-formatted YAML: valid YAML 1.2 and directly parseable here.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MANIFEST = SKILLS / "manifest.yml"
VERIFIED = "2026-07-13"
ACK = "Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178."
LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([a-zA-Z_][\w-]*):\s*(.+?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip("'\"")
    return values


def discover() -> list[dict[str, object]]:
    entries = []
    for path in sorted(SKILLS.glob("*/*/SKILL.md")):
        meta = frontmatter(path)
        skill_id = meta.get("name", "")
        category = path.parent.parent.name
        entries.append({
            "id": skill_id,
            "category": category,
            "path": path.relative_to(ROOT).as_posix(),
            "owner": "website-skills-maintainers",
            "status": "active",
            "aliases": [],
            "dependencies": [],
            "inputs": ["project-context@1"],
            "outputs": [f"{skill_id}-output@1"],
            "last_verified": VERIFIED,
        })
    return entries


def generate() -> dict[str, object]:
    return {
        "schema_version": 1,
        "generated": VERIFIED,
        "canonical_count": len(discover()),
        "external_engines": {
            "design-system-skills": {"locator": "global-routing-table", "required_for": "visual-design"},
            "digital-research-skills": {"locator": "global-routing-table", "required_for": "live-research"},
        },
        "relocations": {
            "brand-alignment": "design-system-skills:brand-alignment",
            "brand-style-guide": "design-system-skills:brand-style-guide",
            "color-selection": "design-system-skills:color-selection",
            "form-ux-design": "design-system-skills:form-ux-design",
            "legal": "design-system-skills:legal-sector-ui-ux",
            "sector-strategies": "design-system-skills:sector-strategies",
            "ux-psychology": "design-system-skills:ux-psychology",
        },
        "skills": discover(),
    }


def validate(data: dict[str, object]) -> list[str]:
    errors: list[str] = []
    found = discover()
    registered = data.get("skills", [])
    if data.get("canonical_count") != len(found):
        errors.append(f"canonical_count is {data.get('canonical_count')}, expected {len(found)}")
    ids: set[str] = set()
    paths: set[str] = set()
    for item in registered if isinstance(registered, list) else []:
        skill_id = item.get("id", "")
        rel = item.get("path", "")
        if skill_id in ids:
            errors.append(f"duplicate skill id: {skill_id}")
        if rel in paths:
            errors.append(f"duplicate skill path: {rel}")
        ids.add(skill_id); paths.add(rel)
        if not (ROOT / rel).is_file():
            errors.append(f"missing registered file: {rel}")
    for entry in found:
        path = ROOT / str(entry["path"])
        text = path.read_text(encoding="utf-8-sig")
        if entry["id"] not in ids:
            errors.append(f"unregistered skill: {entry['id']}")
        heading = re.search(r"^# .+$", text, re.MULTILINE)
        if not heading or text[heading.end():].lstrip("\r\n").splitlines()[0] != ACK:
            errors.append(f"acknowledgement missing or misplaced: {entry['path']}")
        for raw in LINK.findall(text):
            target = raw.split("#", 1)[0].strip().strip("<>")
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"unresolved link in {entry['path']}: {raw}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="regenerate skills/manifest.yml")
    args = parser.parse_args()
    if args.write:
        MANIFEST.write_text(json.dumps(generate(), indent=2) + "\n", encoding="utf-8")
    if not MANIFEST.exists():
        print("ERROR: skills/manifest.yml is missing", file=sys.stderr); return 1
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print(f"registry valid: {data['canonical_count']} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
