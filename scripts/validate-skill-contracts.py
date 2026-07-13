#!/usr/bin/env python3
"""Validate the website-skills July 2026 authoring contract."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CI installs PyYAML
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
ACK = "Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178."
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
COMPATIBILITY = ["claude-code", "codex"]
MOJIBAKE = ("Ã", "Â", "â€", "â†", "âœ", "ðŸ", "\ufffd")
LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
FM = re.compile(r"^\ufeff?---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
AUDIT_WORDS = re.compile(r"\b(audit|review|critique|analysis|assessment)\b", re.I)


def section(text: str, *names: str) -> str | None:
    choices = "|".join(re.escape(name) for name in names)
    match = re.search(rf"^##\s+(?:{choices})\s*$([\s\S]*?)(?=^##\s|\Z)", text, re.M | re.I)
    return match.group(1).strip() if match else None


def parse(path: Path) -> tuple[dict, str, list[str]]:
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    match = FM.match(raw)
    if not match:
        return {}, raw, ["frontmatter"]
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}, raw[match.end():], ["frontmatter_yaml"]
    if not isinstance(data, dict):
        return {}, raw[match.end():], ["frontmatter_type"]
    return data, raw[match.end():], []


def add(findings: list[tuple[str, str, str]], code: str, path: Path, detail: str) -> None:
    findings.append((code, path.relative_to(ROOT).as_posix(), detail))


def validate_skill(path: Path, max_lines: int, max_desc: int) -> list[tuple[str, str, str]]:
    fm, body, errors = parse(path)
    findings: list[tuple[str, str, str]] = []
    for error in errors:
        add(findings, error, path, error.replace("_", " "))
    if errors:
        return findings
    name = fm.get("name")
    desc = fm.get("description")
    if name != path.parent.name:
        add(findings, "name_mismatch", path, f"{name!r} != {path.parent.name!r}")
    if not isinstance(desc, str) or not desc.startswith("Use when") or "\n" in desc or len(desc) > max_desc:
        add(findings, "description", path, "description must be one line, start 'Use when', and meet the length limit")
    unsupported = sorted(set(fm) - ALLOWED_KEYS)
    if unsupported:
        add(findings, "unsupported_frontmatter", path, ", ".join(unsupported))
    metadata = fm.get("metadata")
    if not isinstance(metadata, dict) or metadata.get("portable") is not True or metadata.get("compatible_with") != COMPATIBILITY:
        add(findings, "portable_metadata", path, "metadata portability contract missing")
    required_sections = {
        "use_when": ("Use When",), "do_not_use_when": ("Do Not Use When",),
        "inputs": ("Inputs", "Required Inputs"), "workflow": ("Workflow",),
        "outputs": ("Outputs",), "evidence": ("Evidence Produced",),
        "capability": ("Capability Contract", "Capability and Permission Boundaries"),
        "degraded_mode": ("Degraded Mode",), "decision_rules": ("Decision Rules",),
        "quality": ("Quality Standards",), "anti_patterns": ("Anti-Patterns",),
        "worked_example": ("Worked Example", "Worked Examples"),
        "references": ("References",),
    }
    for required, aliases in required_sections.items():
        content = section(body, *aliases)
        if content is None or not content:
            add(findings, f"missing_{required}", path, f"missing or empty {'/'.join(aliases)}")
        exact_count = sum(len(re.findall(rf"^##\s+{re.escape(alias)}\s*$", body, re.M | re.I)) for alias in aliases)
        if exact_count > 1:
            add(findings, "duplicate_contract_section", path, "/".join(aliases))
    inputs = section(body, "Inputs", "Required Inputs") or ""
    if "None" not in inputs and ("|" not in inputs or not re.search(r"if absent|when missing|absent", inputs, re.I)):
        add(findings, "input_contract", path, "input table must state missing-input behaviour")
    workflow = section(body, "Workflow") or ""
    if not re.search(r"^\s*(?:\d+\.|- )", workflow, re.M) or not re.search(r"stop|block", workflow, re.I) or not re.search(r"recover|repair|retry|rerun|retest|rescore|recheck|fallback", workflow, re.I):
        add(findings, "workflow_contract", path, "workflow needs order, stop condition, and recovery")
    outputs = section(body, "Outputs") or ""
    if "|" not in outputs or not re.search(r"consumer", outputs, re.I) or not re.search(r"acceptance", outputs, re.I):
        add(findings, "output_contract", path, "output table needs consumer and acceptance condition")
    evidence = section(body, "Evidence Produced") or ""
    if "|" not in evidence or not re.search(r"acceptance|format|condition", evidence, re.I):
        add(findings, "evidence_contract", path, "evidence table needs an observable format or acceptance condition")
    capability = section(body, "Capability Contract", "Capability and Permission Boundaries") or ""
    if not re.search(r"read|search", capability, re.I) or not re.search(r"authori|permission|explicit", capability, re.I):
        add(findings, "capability_contract", path, "minimum capability and authority boundary missing")
    if AUDIT_WORDS.search(str(name)) and not re.search(r"read-only", capability, re.I):
        add(findings, "audit_not_read_only", path, "audit/review/analysis skill must default to read-only")
    degraded = section(body, "Degraded Mode") or ""
    if not re.search(r"not assessed|unavailable|narrowest|qualified", degraded, re.I):
        add(findings, "degraded_mode", path, "degraded result must qualify unavailable checks")
    decisions = section(body, "Decision Rules") or ""
    if decisions.count("|") < 6 or not re.search(r"failure|risk|avoided", decisions, re.I):
        add(findings, "decision_contract", path, "decision table needs action and failure/risk avoided")
    if any(line.startswith("|") and not line.rstrip().endswith("|") for line in body.splitlines()):
        add(findings, "malformed_table", path, "Markdown table row does not end with a pipe")
    anti = section(body, "Anti-Patterns") or ""
    items = re.findall(r"^\s*[-*]\s+", anti, re.M)
    if len(items) < 5 or len(re.findall(r"\bFix:", anti, re.I)) < 5:
        add(findings, "anti_patterns", path, "five concrete anti-patterns with Fix: corrections required")
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    if len(raw.splitlines()) > max_lines:
        add(findings, "line_limit", path, f"{len(raw.splitlines())} lines")
    if any(marker in raw for marker in MOJIBAKE):
        add(findings, "encoding_noise", path, "mojibake marker present")
    first_heading = re.search(r"^# .+$", body, re.M)
    if not first_heading or body[first_heading.end():].lstrip("\r\n").splitlines()[:1] != [ACK]:
        add(findings, "acknowledgement", path, "acknowledgement missing or misplaced")
    for raw_link in LINK.findall(body):
        target = raw_link.split("#", 1)[0].strip().strip("<>")
        if target and not (path.parent / target).resolve().exists():
            add(findings, "broken_link", path, raw_link)
    if re.search(r"\b(?:Task|Grep|Glob|apply_patch) tool\b|\bClaude Code must\b|\bCodex must\b", body):
        add(findings, "runner_specific", path, "runner-specific instruction in portable body")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--details", action="store_true")
    args = parser.parse_args()
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    active_root = ROOT / baseline["active_root"]
    files = sorted(active_root.glob("*/*/SKILL.md"))
    templates = sorted((ROOT / "templates" / "skill").glob("SKILL.md"))
    findings: list[tuple[str, str, str]] = []
    names: defaultdict[str, list[str]] = defaultdict(list)
    for path in files:
        fm, _, _ = parse(path)
        if fm.get("name"):
            names[str(fm["name"])].append(path.relative_to(ROOT).as_posix())
        findings.extend(validate_skill(path, baseline["max_skill_lines"], baseline["max_description_characters"]))
    for name, paths in names.items():
        if len(paths) > 1:
            findings.append(("duplicate_name", ", ".join(paths), name))
    if len(files) != baseline["expected_active_skills"]:
        findings.append(("active_count", baseline["active_root"], f"{len(files)} != {baseline['expected_active_skills']}"))
    if len(templates) != baseline["expected_templates"]:
        findings.append(("template_count", "templates/skill", f"{len(templates)} != {baseline['expected_templates']}"))
    mandatory = (
        "skills/manifest.yml", "docs/skill-authoring-standard.md", "templates/skill/SKILL.md",
        "quality/skill-contract-baseline.json", "tests/routing/fixtures.json",
        "scripts/routing-smoke-test.py", ".github/workflows/skill-engine-quality.yml",
    )
    for relative in mandatory:
        if not (ROOT / relative).is_file():
            findings.append(("mandatory_resource", relative, "missing"))
    routing = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "routing-smoke-test.py")],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
    )
    if routing.returncode:
        detail = " | ".join(line for line in routing.stdout.splitlines() if line.startswith("ERROR:"))
        findings.append(("routing_failure", "tests/routing/fixtures.json", detail or "routing smoke failed"))
    counts = Counter(code for code, _, _ in findings)
    expected = baseline.get("failure_counts", {})
    print(f"skill-contracts: {len(files)} active skills, {len(templates)} templates")
    print(json.dumps(dict(sorted(counts.items())), indent=2))
    if args.details:
        for code, path, detail in findings:
            print(f"{code}: {path}: {detail}")
    if dict(counts) != expected:
        print(f"ERROR: findings differ from zero-debt baseline {expected}", file=sys.stderr)
        return 1
    print("skill-contracts: zero debt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
