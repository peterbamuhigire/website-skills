#!/usr/bin/env python3
"""Run deterministic top-three routing checks against active skill text."""
from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORD = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?")
STOP = {"a","an","and","as","at","be","before","by","for","from","in","into","is","it","of","on","or","the","this","through","to","with","without"}


def tokens(text: str) -> list[str]:
    return [word for word in WORD.findall(text.lower()) if word not in STOP and len(word) > 1]


def corpus() -> dict[str, Counter[str]]:
    result = {}
    for path in sorted((ROOT / "skills").glob("*/*/SKILL.md")):
        raw = path.read_text(encoding="utf-8-sig")
        front = raw.split("---", 2)[1]
        meta = yaml.safe_load(front)
        use = re.search(r"^##\s+Use When\s*$([\s\S]*?)(?=^##\s|\Z)", raw, re.M | re.I)
        do_not = re.search(r"^##\s+Do Not Use When\s*$([\s\S]*?)(?=^##\s|\Z)", raw, re.M | re.I)
        positive = f"{meta['name']} {meta.get('description','')} {use.group(1) if use else ''}"
        negative = tokens(do_not.group(1) if do_not else "")
        counts = Counter(tokens(positive))
        for term in negative:
            counts[term] -= 0.15
        result[meta["name"]] = counts
    return result


def rank(prompt: str, documents: dict[str, Counter[str]]) -> list[str]:
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
    return sorted(scores, key=lambda item: (-scores[item], item))


def main() -> int:
    data = json.loads((ROOT / "tests/routing/fixtures.json").read_text(encoding="utf-8"))
    docs = corpus()
    top_k = data["top_k"]
    failures = []
    hits = 0
    for fixture in data["fixtures"]:
        ranked = rank(fixture["prompt"], docs)
        top = ranked[:top_k]
        if fixture["expected"] in top:
            hits += 1
        else:
            failures.append(f"{fixture['id']}: expected {fixture['expected']} in {top}")
        forbidden = fixture.get("forbidden_top1")
        if forbidden and ranked[0] == forbidden:
            failures.append(f"{fixture['id']}: forbidden top-one route {forbidden}")
    precision = hits / len(data["fixtures"])
    print(f"routing-smoke: {hits}/{len(data['fixtures'])} top-{top_k} hits ({precision:.1%})")
    for failure in failures:
        print(f"ERROR: {failure}")
    return 1 if failures or hits != len(data["fixtures"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
