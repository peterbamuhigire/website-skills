#!/usr/bin/env python3
"""Content-link graph check for a built static site (M10-11-T11, GR-12).

Builds a directed graph over every *.html page in a built site (dist/) and reports:

- broken internal links: an href to a missing file, or to an anchor id the target page lacks;
- orphan pages: in-degree 0 (self-links ignored), excluding the home page and --entry pages;
- unreachable pages: not reachable from the home page by breadth-first search (an orphan
  cluster), excluding --entry pages;
- hub pages: in-degree at or above --hub-threshold (information only).

Treating links as "references" between documents follows the Graphify framing (idea only;
no Graphify code or package is used). Link resolution reuses local_target() and PageParser from
website_fixture_benchmark.py rather than duplicating them.

Determinism: pages are sorted by POSIX relative path, edges are de-duplicated, and the JSON is
written with sorted keys and no timestamps, so repeat runs are byte-identical.

Usage:
    python -X utf8 scripts/content_link_graph.py [dist] [--entry 404.html] [--hub-threshold N]
                                                  [--home index.html] [--out reports/content/link-graph.json]

Exit codes: 0 clean; 1 broken links, missing anchors, orphan or unreachable pages; 5 prerequisite
missing (no dist directory, no HTML pages, or no home page).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from website_fixture_benchmark import PageParser, local_target  # noqa: E402

IMPLICIT_ANCHORS = {"", "top"}


def rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def page_for(target: Path) -> Path:
    return target / "index.html" if target.is_dir() else target


def parse(page: Path) -> PageParser:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8", errors="replace"))
    return parser


def ids_of(parser: PageParser) -> set[str]:
    ids: set[str] = set()
    for tag, rows in parser.attrs.items():
        for attrs in rows:
            if attrs.get("id"):
                ids.add(attrs["id"])
            if tag == "a" and attrs.get("name"):
                ids.add(attrs["name"])
    return ids


def percentile(values: list[int], pct: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    rank = max(1, math.ceil(pct / 100 * len(ordered)))
    return ordered[rank - 1]


def build_graph(dist: Path, home: str, entries: list[str], hub_threshold: int | None) -> dict:
    root = dist.resolve()
    pages = sorted((p for p in root.rglob("*.html") if p.is_file()), key=lambda p: rel(p, root))
    names = [rel(p, root) for p in pages]
    parsed = {name: parse(page) for name, page in zip(names, pages)}
    anchors = {name: ids_of(parser) for name, parser in parsed.items()}

    edges: set[tuple[str, str]] = set()
    broken: set[tuple[str, str]] = set()
    missing_anchor: set[tuple[str, str]] = set()
    for name, page in zip(names, pages):
        for attrs in parsed[name].attrs.get("a", []) + parsed[name].attrs.get("area", []):
            href = attrs.get("href", "").strip()
            if not href:
                continue
            fragment = unquote(urlsplit(href).fragment)
            if href.startswith("#"):
                if fragment not in IMPLICIT_ANCHORS and fragment not in anchors[name]:
                    missing_anchor.add((name, href))
                continue
            target = local_target(page, href, root)
            if target is None:
                continue  # external, mailto:, tel: or javascript:
            if not target.is_relative_to(root):
                broken.add((name, href))
                continue
            target = page_for(target)
            if not target.is_file():
                broken.add((name, href))
                continue
            if target.suffix.lower() != ".html":
                continue  # a downloadable asset that exists; not a page edge
            target_name = rel(target, root)
            if fragment and fragment not in IMPLICIT_ANCHORS and fragment not in anchors.get(target_name, set()):
                missing_anchor.add((name, href))
            if target_name != name:
                edges.add((name, target_name))

    in_degree = {name: 0 for name in names}
    out_links: dict[str, list[str]] = {name: [] for name in names}
    for source, target in sorted(edges):
        in_degree[target] += 1
        out_links[source].append(target)

    allow = {home, *entries}
    orphans = [name for name in names if in_degree[name] == 0 and name not in allow]
    reached = {home}
    queue = deque([home])
    while queue:
        for target in out_links.get(queue.popleft(), []):
            if target not in reached:
                reached.add(target)
                queue.append(target)
    unreachable = [name for name in names if name not in reached and name not in allow]
    threshold = hub_threshold if hub_threshold is not None else max(2, percentile(list(in_degree.values()), 95))
    hubs = [{"page": name, "in_degree": in_degree[name]} for name in names if in_degree[name] >= threshold]

    failing = bool(broken or missing_anchor or orphans or unreachable)
    return {
        "tool": "content_link_graph",
        "schema_version": 1,
        "evidence_type": "static build graph (lab); not crawl or analytics data",
        "home": home,
        "entries": sorted(set(entries)),
        "pages": len(names),
        "edges": len(edges),
        "broken_links": [{"page": p, "href": h} for p, h in sorted(broken)],
        "missing_anchors": [{"page": p, "href": h} for p, h in sorted(missing_anchor)],
        "orphans": orphans,
        "unreachable_from_home": unreachable,
        "hubs": {"threshold": threshold, "pages": hubs, "note": "information only"},
        "in_degree": {name: in_degree[name] for name in names},
        "status": "FAIL" if failing else "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("dist", nargs="?", type=Path, default=Path("dist"))
    parser.add_argument("--home", default="index.html")
    parser.add_argument("--entry", action="append", default=[], help="page allowed to have no inbound link (repeatable), for example 404.html or a campaign landing page")
    parser.add_argument("--hub-threshold", type=int, default=None, help="in-degree at which a page is reported as a hub (default: 95th percentile, at least 2)")
    parser.add_argument("--out", type=Path, default=Path("reports/content/link-graph.json"))
    args = parser.parse_args()

    dist = args.dist
    if not dist.is_dir():
        print(f"content-link-graph: NOT_ASSESSED: dist directory not found at {dist}", file=sys.stderr)
        return 5
    if not (dist / args.home).is_file():
        print(f"content-link-graph: NOT_ASSESSED: home page {args.home} not found in {dist}", file=sys.stderr)
        return 5
    entries = list(args.entry)
    if (dist / "404.html").is_file() and "404.html" not in entries:
        entries.append("404.html")  # never linked by design
    report = build_graph(dist, args.home, entries, args.hub_threshold)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(
        f"content-link-graph: {report['status']}: {report['pages']} pages, {report['edges']} edges; "
        f"broken {len(report['broken_links'])}, missing anchors {len(report['missing_anchors'])}, "
        f"orphans {len(report['orphans'])}, unreachable {len(report['unreachable_from_home'])}, "
        f"hubs {len(report['hubs']['pages'])}; report {args.out.as_posix()}"
    )
    return 1 if report["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
