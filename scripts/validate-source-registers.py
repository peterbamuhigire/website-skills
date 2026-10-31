#!/usr/bin/env python3
"""Fail on expired or malformed source records (WSK2-06).

Checks, using only the standard library:

1. `docs/standards-register.md`: every row of the standards table has a parseable `Last verified` and
   `Next review` date, a cadence of Monthly, Quarterly or Annual, a review date that is not in the past,
   a verification date that is not in the future, and a gap between the two that the cadence allows
   (45, 100 and 400 days). A review date therefore cannot be pushed out without a verification behind it.
2. Every `docs/source-registers/*.json`: the register and each claim carry a review date that is not in
   the past; every claim cites at least one source that exists in a register of the folder (a later
   register may cite a source recorded in an earlier one); claim identifiers are unique; the support state is one the engine uses; no source was accessed in the future.

This checks metadata only. It does not verify that a claim is true; that needs a source check recorded in
the register. Usage:

    python scripts/validate-source-registers.py [--root DIR] [--as-of YYYY-MM-DD]

Exit codes: 0 clean; 1 expired or malformed records; 5 unusable argument or unreadable file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STANDARDS_TABLE = "docs/standards-register.md"
REGISTER_GLOB = "docs/source-registers/*.json"
CADENCE_WINDOW_DAYS = {"monthly": 45, "quarterly": 100, "annual": 400}
SUPPORT_STATES = {"supported", "partially_supported", "unsupported", "synthesis", "inference", "no-source", "not_assessed"}
REQUIRED_COLUMNS = ("standard", "cadence", "last verified", "next review")


def parse_date(value) -> date | None:
    try:
        return date.fromisoformat(str(value).strip())
    except ValueError:
        return None


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def check_standards_table(text: str, as_of: date) -> list[str]:
    lines = text.splitlines()
    header_index = next((i for i, line in enumerate(lines) if line.lstrip().startswith("|") and "next review" in line.lower()), None)
    if header_index is None:
        return [f"{STANDARDS_TABLE}: no standards table with a 'Next review' column found"]
    columns = [cell.lower() for cell in split_row(lines[header_index])]
    missing = [name for name in REQUIRED_COLUMNS if name not in columns]
    if missing:
        return [f"{STANDARDS_TABLE}: table lacks the column(s) {', '.join(missing)}"]
    position = {name: columns.index(name) for name in REQUIRED_COLUMNS}
    errors: list[str] = []
    rows = 0
    for line in lines[header_index + 2 :]:
        if not line.lstrip().startswith("|"):
            break
        cells = split_row(line)
        if len(cells) < len(columns):
            errors.append(f"{STANDARDS_TABLE}: row has {len(cells)} cells, expected {len(columns)}: {cells[0] if cells else line}")
            continue
        rows += 1
        name = cells[position["standard"]]
        cadence = cells[position["cadence"]].lower()
        verified = parse_date(cells[position["last verified"]])
        review = parse_date(cells[position["next review"]])
        if cadence not in CADENCE_WINDOW_DAYS:
            errors.append(f"{STANDARDS_TABLE}: {name}: cadence '{cells[position['cadence']]}' is not Monthly, Quarterly or Annual")
        if verified is None:
            errors.append(f"{STANDARDS_TABLE}: {name}: 'Last verified' is missing or not an ISO date")
        if review is None:
            errors.append(f"{STANDARDS_TABLE}: {name}: 'Next review' is missing or not an ISO date")
        if verified is None or review is None:
            continue
        if review < as_of:
            errors.append(f"{STANDARDS_TABLE}: {name}: review overdue ({review}, as of {as_of})")
        if verified > as_of:
            errors.append(f"{STANDARDS_TABLE}: {name}: verification date {verified} is in the future")
        window = CADENCE_WINDOW_DAYS.get(cadence)
        if window is not None and (review - verified).days > window:
            errors.append(f"{STANDARDS_TABLE}: {name}: next review {review} is more than {window} days after verification {verified}, beyond the {cells[position['cadence']]} cadence")
    if rows == 0:
        errors.append(f"{STANDARDS_TABLE}: the standards table has no rows")
    return errors


def check_register_data(data: dict, name: str, as_of: date, known_source_ids: frozenset[str] = frozenset()) -> list[str]:
    errors: list[str] = []
    review = parse_date(data.get("review_date"))
    if review is None:
        errors.append(f"{name}: register review_date is missing or not an ISO date")
    elif review < as_of:
        errors.append(f"{name}: register review overdue ({review})")
    sources = data.get("sources")
    claims = data.get("claims")
    if not isinstance(sources, list) or not sources:
        errors.append(f"{name}: needs a non-empty sources list")
        sources = []
    if not isinstance(claims, list) or not claims:
        errors.append(f"{name}: needs a non-empty claims list")
        claims = []
    source_ids: set[str] = set()
    for source in sources:
        source_id = source.get("source_id") if isinstance(source, dict) else None
        if not source_id:
            errors.append(f"{name}: a source has no source_id")
            continue
        source_ids.add(source_id)
        accessed = parse_date(source.get("access_date"))
        if accessed is None:
            errors.append(f"{name}: source {source_id} has no valid access_date")
        elif accessed > as_of:
            errors.append(f"{name}: source {source_id} access_date {accessed} is in the future")
    seen: set[str] = set()
    for claim in claims:
        claim_id = claim.get("claim_id") if isinstance(claim, dict) else None
        if not claim_id:
            errors.append(f"{name}: a claim has no claim_id")
            continue
        if claim_id in seen:
            errors.append(f"{name}: duplicate claim_id {claim_id}")
        seen.add(claim_id)
        refs = claim.get("source_ids")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{name}: claim {claim_id} has no source_ids (no source)")
        else:
            for ref in refs:
                if ref not in source_ids and ref not in known_source_ids:
                    errors.append(f"{name}: claim {claim_id} cites unknown source {ref}")
        claim_review = parse_date(claim.get("review_date"))
        if claim_review is None:
            errors.append(f"{name}: claim {claim_id} review_date is missing or not an ISO date")
        elif claim_review < as_of:
            errors.append(f"{name}: claim {claim_id} review overdue ({claim_review})")
        state = (claim.get("support_review") or {}).get("state") if isinstance(claim.get("support_review"), dict) else None
        if state not in SUPPORT_STATES:
            errors.append(f"{name}: claim {claim_id} has an unknown support state {state!r}")
    return errors


def check_tree(root: Path, as_of: date) -> list[str]:
    errors: list[str] = []
    table = root / STANDARDS_TABLE
    if not table.is_file():
        errors.append(f"{STANDARDS_TABLE}: missing")
    else:
        errors.extend(check_standards_table(table.read_text(encoding="utf-8-sig"), as_of))
    loaded: list[tuple[str, dict]] = []
    for path in sorted(root.glob(REGISTER_GLOB)):
        rel = path.relative_to(root).as_posix()
        try:
            loaded.append((rel, json.loads(path.read_text(encoding="utf-8"))))
        except (OSError, ValueError) as exc:
            errors.append(f"{rel}: unreadable ({exc})")
    known = frozenset(
        source["source_id"]
        for _rel, data in loaded
        for source in (data.get("sources") if isinstance(data.get("sources"), list) else [])
        if isinstance(source, dict) and source.get("source_id")
    )
    for rel, data in loaded:
        errors.extend(check_register_data(data, rel, as_of, known))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--as-of", default=None, help="date to judge expiry against (default: today)")
    args = parser.parse_args()
    as_of = date.today() if args.as_of is None else parse_date(args.as_of)
    if as_of is None:
        print(f"validate-source-registers: --as-of must be an ISO date, got {args.as_of!r}", file=sys.stderr)
        return 5
    errors = check_tree(args.root, as_of)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"validate-source-registers: FAIL ({len(errors)} findings, as of {as_of})")
        return 1
    registers = sorted(args.root.glob(REGISTER_GLOB))
    claims = sum(len(json.loads(p.read_text(encoding='utf-8')).get("claims", [])) for p in registers)
    print(f"validate-source-registers: PASS ({len(registers)} registers, {claims} claims, standards table current as of {as_of})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
