#!/usr/bin/env python3
"""Validate current search and AI-discoverability doctrine."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "quality" / "search-doctrine-policy.json"
SOURCE_FIELDS = {
    "source_id",
    "title",
    "url",
    "publisher",
    "source_tier",
    "publication_or_version_date",
    "access_date",
    "freshness_class",
    "support_status",
    "confidence",
    "scope_and_limit",
}
CLAIM_FIELDS = {
    "claim_id",
    "claim",
    "source_ids",
    "support_review",
    "freshness_class",
    "review_date",
    "confidence",
}
SUPPORT_STATES = {"supported", "unsupported", "synthesis", "inference", "no-source"}


def fail(findings: list[str], message: str) -> None:
    findings.append(message)


def validate_register(path: Path, findings: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(findings, f"currentness register unreadable: {exc}")
        return

    sources = data.get("sources")
    claims = data.get("claims")
    if not isinstance(sources, list) or not sources:
        fail(findings, "currentness register needs a non-empty sources list")
        return
    if not isinstance(claims, list) or not claims:
        fail(findings, "currentness register needs a non-empty claims list")
        return

    source_ids: set[str] = set()
    for item in sources:
        missing = SOURCE_FIELDS - set(item) if isinstance(item, dict) else SOURCE_FIELDS
        if missing:
            fail(findings, f"source missing fields: {sorted(missing)}")
            continue
        source_id = item["source_id"]
        if source_id in source_ids:
            fail(findings, f"duplicate source_id: {source_id}")
        source_ids.add(source_id)
        if item["source_tier"] not in {1, 2, 3, 4, 5}:
            fail(findings, f"invalid source tier: {source_id}")

    today = date.today()
    claim_ids: set[str] = set()
    for item in claims:
        missing = CLAIM_FIELDS - set(item) if isinstance(item, dict) else CLAIM_FIELDS
        if missing:
            fail(findings, f"claim missing fields: {sorted(missing)}")
            continue
        claim_id = item["claim_id"]
        if claim_id in claim_ids:
            fail(findings, f"duplicate claim_id: {claim_id}")
        claim_ids.add(claim_id)
        refs = item["source_ids"]
        if not isinstance(refs, list) or not refs:
            fail(findings, f"claim has no source_ids: {claim_id}")
        for source_id in refs:
            if source_id not in source_ids:
                fail(findings, f"claim {claim_id} references unknown source {source_id}")
        review = item["support_review"]
        if not isinstance(review, dict) or review.get("state") not in SUPPORT_STATES:
            fail(findings, f"claim has invalid support_review: {claim_id}")
        try:
            review_date = date.fromisoformat(item["review_date"])
        except (TypeError, ValueError):
            fail(findings, f"claim has invalid review_date: {claim_id}")
        else:
            if review_date < today:
                fail(findings, f"claim review overdue: {claim_id} ({review_date})")


def main() -> int:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    findings: list[str] = []
    texts: dict[str, str] = {}

    for relative in policy["canonical_files"]:
        path = ROOT / relative
        if not path.is_file():
            fail(findings, f"missing canonical file: {relative}")
            continue
        texts[relative] = path.read_text(encoding="utf-8-sig", errors="replace")

    for rule in policy["forbidden_patterns"]:
        pattern = re.compile(rule["pattern"], re.IGNORECASE | re.DOTALL)
        for relative, text in texts.items():
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                fail(findings, f"{relative}:{line}: {rule['reason']}")

    for relative, snippets in policy["required_snippets"].items():
        text = texts.get(relative, "")
        for snippet in snippets:
            if snippet.casefold() not in text.casefold():
                fail(findings, f"{relative}: missing doctrine anchor {snippet!r}")

    validate_register(ROOT / policy["currentness_register"], findings)

    if findings:
        for finding in findings:
            print(f"ERROR: {finding}")
        print(f"search-doctrine: FAIL ({len(findings)} findings)")
        return 1
    print(f"search-doctrine: PASS ({len(texts)} canonical files, currentness verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
