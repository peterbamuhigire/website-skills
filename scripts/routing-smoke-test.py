#!/usr/bin/env python3
"""Run deterministic top-three routing checks against active skill text.

Lexical proxy; not live routing (see addyosmani/agent-skills issue #620).

Checks (M10-03):
- positives: the expected skill ranks within ``top_k``; precision@1 and precision@3 are printed;
- owned negatives (``negatives`` in the fixture file): the negative's skill must not rank first
  with a non-zero score, and its ``owner`` must rank strictly above it with a non-zero score. An
  owner written ``<engine-id>/<skill>`` belongs to another engine and is NOT_ASSESSED here (it is
  evaluated in union mode by chwezi-engine-agents);
- ``forbidden_top1`` on a positive is still honoured for backwards compatibility;
- ``--min-rank1 <pct>``: fail when precision@1 falls below the ratchet floor;
- ``--lint-fixtures``: a prompt must not contain its expected slug as a phrase and its word-trigram
  overlap with the expected description must stay below 0.6.

The owner-outranks-self rule is adapted from addyosmani/agent-skills (MIT,
https://github.com/addyosmani/agent-skills, commit 2686b62), ``scripts/run-evals.js``; paraphrased.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = ROOT / "tests/routing/fixtures.json"
WORD = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?")
STOP = {"a","an","and","as","at","be","before","by","for","from","in","into","is","it","of","on","or","the","this","through","to","with","without"}
TRIGRAM_LIMIT = 0.6


def tokens(text: str) -> list[str]:
    return [word for word in WORD.findall(text.lower()) if word not in STOP and len(word) > 1]


def read_skills() -> dict[str, dict]:
    skills = {}
    for path in sorted((ROOT / "skills").glob("*/*/SKILL.md")):
        raw = path.read_text(encoding="utf-8-sig")
        front = raw.split("---", 2)[1]
        meta = yaml.safe_load(front)
        skills[meta["name"]] = {"meta": meta, "raw": raw}
    return skills


def corpus(skills: dict[str, dict] | None = None) -> dict[str, Counter[str]]:
    skills = skills if skills is not None else read_skills()
    result = {}
    for name, item in skills.items():
        raw, meta = item["raw"], item["meta"]
        use = re.search(r"^##\s+Use When\s*$([\s\S]*?)(?=^##\s|\Z)", raw, re.M | re.I)
        do_not = re.search(r"^##\s+Do Not Use When\s*$([\s\S]*?)(?=^##\s|\Z)", raw, re.M | re.I)
        positive = f"{meta['name']} {meta.get('description','')} {use.group(1) if use else ''}"
        negative = tokens(do_not.group(1) if do_not else "")
        counts = Counter(tokens(positive))
        for term in negative:
            counts[term] -= 0.15
        result[name] = counts
    return result


def score_all(prompt: str, documents: dict[str, Counter[str]]) -> dict[str, float]:
    query = Counter(tokens(prompt))
    document_frequency = Counter(term for counts in documents.values() for term in counts if counts[term] > 0)
    scores = {}
    for name, counts in documents.items():
        score = 0.0
        for term, q_count in query.items():
            tf = max(0.0, counts.get(term, 0.0))
            if tf:
                score += (1.0 + math.log(tf)) * math.log((len(documents) + 1) / (document_frequency[term] + 1)) * q_count
        name_terms = set(tokens(name.replace("-", " ")))
        score += 2.5 * len(name_terms & set(query))
        scores[name] = score
    return scores


def rank(prompt: str, documents: dict[str, Counter[str]]) -> list[str]:
    scores = score_all(prompt, documents)
    return sorted(scores, key=lambda item: (-scores[item], item))


def check_negative(negative: dict, documents: dict[str, Counter[str]]) -> tuple[str, str]:
    """Return (status, message); status is PASS, FAIL or NOT_ASSESSED."""
    skill, owner, prompt = negative["skill"], negative.get("owner"), negative["prompt"]
    if owner and "/" in owner:
        return "NOT_ASSESSED", f"cross-engine owner {owner} is checked in union mode"
    if skill not in documents:
        return "FAIL", f"negative skill {skill} is not active"
    scores = score_all(prompt, documents)
    ranked = sorted(scores, key=lambda item: (-scores[item], item))
    if ranked[0] == skill and scores[skill] > 0:
        return "FAIL", f"{skill} ranks first ({scores[skill]:.2f})"
    if not owner:
        return "PASS", "skill is not rank 1"
    if owner not in documents:
        return "FAIL", f"owner {owner} is not active"
    if scores[owner] <= 0 or ranked.index(owner) >= ranked.index(skill):
        return "FAIL", f"owner {owner} (rank {ranked.index(owner) + 1}, {scores[owner]:.2f}) does not outrank {skill} (rank {ranked.index(skill) + 1}, {scores[skill]:.2f})"
    return "PASS", "owner outranks skill"


def normalise(text: str) -> str:
    return " " + re.sub(r"[^a-z0-9]+", " ", text.lower()).strip() + " "


def trigrams(text: str) -> set[tuple[str, ...]]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(words[i:i + 3]) for i in range(len(words) - 2)}


def lint_prompt(prompt: str, slug: str, description: str) -> list[str]:
    findings = []
    phrase = re.sub(r"^\d+-", "", slug.lower()).replace("-", " ").strip()
    if phrase and f" {phrase} " in normalise(prompt):
        findings.append(f"slug-in-prompt '{phrase}'")
    grams = trigrams(prompt)
    if grams:
        overlap = len(grams & trigrams(description)) / len(grams)
        if overlap >= TRIGRAM_LIMIT:
            findings.append(f"description-copy trigram overlap {overlap:.2f}")
    return findings


def run(fixture_path: Path, min_rank1: float | None, lint: bool) -> int:
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    skills = read_skills()
    docs = corpus(skills)
    top_k = data["top_k"]
    failures = []
    hits = rank1 = 0
    for fixture in data["fixtures"]:
        ranked = rank(fixture["prompt"], docs)
        if ranked[0] == fixture["expected"]:
            rank1 += 1
        if fixture["expected"] in ranked[:top_k]:
            hits += 1
        else:
            failures.append(f"{fixture['id']}: expected {fixture['expected']} in {ranked[:top_k]}")
        forbidden = fixture.get("forbidden_top1")
        if forbidden and ranked[0] == forbidden:
            failures.append(f"{fixture['id']}: forbidden top-one route {forbidden}")
    total = len(data["fixtures"])
    negatives = data.get("negatives", [])
    outcome = Counter()
    for negative in negatives:
        status, message = check_negative(negative, docs)
        outcome[status] += 1
        if status == "FAIL":
            failures.append(f"negative {negative.get('id', negative['skill'])}: {message}")
    p1 = 100.0 * rank1 / total if total else 0.0
    p3 = 100.0 * hits / total if total else 0.0
    print(f"routing-smoke: {hits}/{total} top-{top_k} hits ({hits / total:.1%}); lexical proxy, not live routing")
    print(f"- precision@1: {rank1}/{total} ({p1:.1f}%)")
    print(f"- precision@3: {hits}/{total} ({p3:.1f}%)")
    owned = sum(1 for negative in negatives if negative.get("owner"))
    print(f"- owned negatives: {owned} (pass {outcome['PASS']}, fail {outcome['FAIL']}, not assessed {outcome['NOT_ASSESSED']})")
    if min_rank1 is not None:
        print(f"- rank-1 floor: {min_rank1:.1f}%")
        if p1 < min_rank1:
            failures.append(f"precision@1 {p1:.1f}% is below the ratchet floor {min_rank1:.1f}%")
    if lint:
        lint_findings = []
        for fixture in data["fixtures"]:
            meta = skills.get(fixture["expected"], {}).get("meta", {})
            for finding in lint_prompt(fixture["prompt"], fixture["expected"], str(meta.get("description", ""))):
                lint_findings.append(f"{fixture['id']}: {finding}")
        print(f"- fixture lint findings: {len(lint_findings)}")
        failures.extend(f"lint {item}" for item in lint_findings)
    for failure in failures:
        print(f"ERROR: {failure}")
    return 1 if failures or hits != total else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fixtures", type=Path, default=DEFAULT_FIXTURES)
    parser.add_argument("--min-rank1", type=float, default=None, help="Fail when precision@1 (percent) is below this floor.")
    parser.add_argument("--lint-fixtures", action="store_true", help="Fail on slug-bearing or description-copying prompts.")
    args = parser.parse_args()
    return run(args.fixtures, args.min_rank1, args.lint_fixtures)


if __name__ == "__main__":
    raise SystemExit(main())
