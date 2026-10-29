#!/usr/bin/env python3
"""Check external script/style asset tags for Subresource Integrity metadata."""
from __future__ import annotations

import base64
import datetime as dt
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

HASH = re.compile(r"^sha(256|384|512)-([A-Za-z0-9+/]+={0,2})$")


def origin(url: str) -> tuple[str, str, int | None] | None:
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return None
    default_port = 443 if parsed.scheme == "https" else 80
    return (parsed.scheme.lower(), parsed.hostname.lower(), parsed.port or default_port)


def valid_integrity(value: str) -> bool:
    for token in value.split():
        match = HASH.fullmatch(token.split("?", 1)[0])
        if not match:
            continue
        try:
            base64.b64decode(match.group(2), validate=True)
            return True
        except ValueError:
            continue
    return False


class AssetParser(HTMLParser):
    def __init__(self, canonical: str | None):
        super().__init__(convert_charrefs=True)
        self.canonical_origin = origin(canonical) if canonical else None
        self.findings: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        rels = set(values.get("rel", "").lower().split())
        asset = False
        url = ""
        if tag == "script" and values.get("src"):
            asset, url = True, values["src"]
        elif tag == "link" and values.get("href"):
            as_type = values.get("as", "").lower()
            asset = bool(rels & {"stylesheet", "modulepreload"}) or ("preload" in rels and as_type in {"script", "style"})
            url = values["href"]
        if not asset:
            return

        asset_origin = origin(url)
        if asset_origin is None or (self.canonical_origin is not None and asset_origin == self.canonical_origin):
            return
        if asset_origin[1] == "localhost" or asset_origin[1] == "127.0.0.1":
            return
        if not valid_integrity(values.get("integrity", "")):
            self.findings.append((url, "missing or invalid integrity"))
        if values.get("crossorigin", "").lower() not in {"", "anonymous", "use-credentials"}:
            self.findings.append((url, "invalid crossorigin value"))
        elif values.get("crossorigin", "").lower() == "":
            self.findings.append((url, "missing crossorigin"))


def audit(path: Path) -> list[tuple[str, str]]:
    parser = AssetParser(None)
    text = path.read_text(encoding="utf-8", errors="replace")
    for tag in re.finditer(r"<link\b[^>]*\brel\s*=\s*(['\"]?)canonical\1[^>]*>", text, re.I):
        href = re.search(r"\bhref\s*=\s*(['\"])(.*?)\1", tag.group(0), re.I)
        if href:
            parser.canonical_origin = origin(href.group(2))
            break
    parser.feed(text)
    return parser.findings


def main() -> int:
    if len(sys.argv) < 2:
        print("check-sri: usage: check_sri.py <dist-dir> [allowlist-file]", file=sys.stderr)
        return 3
    dist = Path(sys.argv[1])
    if not dist.is_dir():
        print(f"check-sri: {dist} not found", file=sys.stderr)
        return 3
    files = sorted(dist.rglob("*.html"))
    report = Path("reports/security/sri.txt")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"SRI audit — {dt.datetime.now(dt.timezone.utc).isoformat()}", "---"]
    for page in files:
        for url, reason in audit(page):
            lines.append(f"FAIL {page.relative_to(dist)}: {url} {reason}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(report.read_text(encoding="utf-8"), end="")
    if len(lines) > 2:
        print(f"check-sri: FAIL — see {report}", file=sys.stderr)
        return 1
    print("check-sri: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
