#!/usr/bin/env python3
"""Check external script/style asset tags for Subresource Integrity metadata."""
from __future__ import annotations

import base64
import datetime as dt
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

HASH = re.compile(r"^sha(256|384|512)-([A-Za-z0-9+/]+={0,2})$")


def origin(url: str, default_scheme: str | None = None) -> tuple[str, str, int | None] | None:
    try:
        parsed = urlsplit(url)
        hostname = parsed.hostname
        port = parsed.port
    except ValueError:
        return None
    scheme = parsed.scheme.lower()
    if not scheme and parsed.netloc:
        scheme = default_scheme or "https"
    if scheme not in {"http", "https"} or not hostname:
        return None
    default_port = 443 if scheme == "https" else 80
    return (scheme, hostname.lower(), port or default_port)


def valid_integrity(value: str) -> bool:
    for token in value.split():
        match = HASH.fullmatch(token.split("?", 1)[0])
        if not match:
            continue
        try:
            digest = base64.b64decode(match.group(2), validate=True)
            if len(digest) == {"256": 32, "384": 48, "512": 64}[match.group(1)]:
                return True
        except ValueError:
            continue
    return False


class AssetParser(HTMLParser):
    def __init__(self, document_url: str | None):
        super().__init__(convert_charrefs=True)
        self.document_origin = origin(document_url) if document_url else None
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

        document_scheme = self.document_origin[0] if self.document_origin else "https"
        asset_origin = origin(url, default_scheme=document_scheme)
        if asset_origin is None:
            if url.lower().startswith(("http://", "https://", "//")):
                self.findings.append((url, "invalid network asset URL"))
            return
        if self.document_origin is not None and asset_origin == self.document_origin:
            return
        if not valid_integrity(values.get("integrity", "")):
            self.findings.append((url, "missing or invalid integrity"))
        if values.get("crossorigin", "").lower() not in {"", "anonymous", "use-credentials"}:
            self.findings.append((url, "invalid crossorigin value"))
        elif values.get("crossorigin", "").lower() == "":
            self.findings.append((url, "missing crossorigin"))


def audit(path: Path, document_url: str | None = None) -> list[tuple[str, str]]:
    # Canonical metadata is not proof of the origin serving this document.
    # Without an explicit document URL, absolute assets are checked conservatively.
    parser = AssetParser(document_url)
    text = path.read_text(encoding="utf-8", errors="replace")
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
    document_url = os.environ.get("SRI_DOCUMENT_ORIGIN")
    if document_url and origin(document_url) is None:
        print("check-sri: SRI_DOCUMENT_ORIGIN must be an absolute HTTP(S) origin", file=sys.stderr)
        return 3
    report = Path("reports/security/sri.txt")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"SRI audit — {dt.datetime.now(dt.timezone.utc).isoformat()}", "---"]
    for page in files:
        for url, reason in audit(page, document_url):
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
