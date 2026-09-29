#!/usr/bin/env python3
"""Hash-check the vendored chwezi-slop detector (M10-11-T01).

The website client pipeline checks out only this engine, so the design engine's
deterministic slop detector (chwezi-design-engine/tools/slop-detector, M10-09)
travels here as a vendored copy under scripts/vendor/chwezi-slop/. The copy keeps
the design engine's relative layout (tools/slop-detector/, hooks/lib/,
doctrine/references/) because the detector resolves font-matcher.js and the
banned-font JSON relative to itself.

Checks, in order:
1. every file listed in VENDOR.json exists and its SHA-256 (after CRLF
   normalisation) matches the manifest; any mismatch exits 1;
2. when the sibling checkout ../chwezi-design-engine exists, every vendored file
   matches the source file; drift exits 1. When the sibling is absent the
   comparison is NOT_ASSESSED, which is reported and is never a pass for that
   comparison (the manifest check still decides the exit code).

Updating the copy is a deliberate, reviewed step that the orchestrator runs and
commits; it is never run automatically:

    python -X utf8 scripts/check-vendored-detector.py --sync-from ../chwezi-design-engine

Exit codes: 0 clean; 1 tampered, missing or drifted; 5 manifest unreadable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VENDOR = ROOT / "scripts" / "vendor" / "chwezi-slop"
DEFAULT_SOURCE = ROOT.parent / "chwezi-design-engine"
SOURCE_REPO = "https://github.com/peterbamuhigire/chwezi-design-engine"

# Paths relative to the design engine root; the vendored copy keeps them.
# Static tier, registry and banned-font JSON. browser.mjs is carried so the
# optional browser tier resolves, but it installs nothing and stays inert
# without the client project's own locked Playwright.
VENDORED_FILES = (
    "tools/slop-detector/cli.mjs",
    "tools/slop-detector/lib/browser-rules.mjs",
    "tools/slop-detector/lib/browser.mjs",
    "tools/slop-detector/lib/checks.mjs",
    "tools/slop-detector/lib/colour.mjs",
    "tools/slop-detector/lib/detector.mjs",
    "tools/slop-detector/lib/doctrine-consistency.mjs",
    "tools/slop-detector/lib/document.mjs",
    "tools/slop-detector/lib/drift.mjs",
    "tools/slop-detector/lib/parse-css.mjs",
    "tools/slop-detector/lib/parse-html.mjs",
    "tools/slop-detector/lib/registry.mjs",
    "tools/slop-detector/lib/schema.mjs",
    "tools/slop-detector/lib/tailwind.mjs",
    "tools/slop-detector/lib/util.mjs",
    "tools/slop-detector/lib/waivers.mjs",
    "tools/slop-detector/rules/registry.json",
    "tools/slop-detector/rules/registry.schema.json",
    "hooks/lib/font-matcher.js",
    "doctrine/references/ai-slop-banned-fonts.json",
)


def normalised_bytes(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n")


def sha256_norm(path: Path) -> str:
    return hashlib.sha256(normalised_bytes(path)).hexdigest()


def git_head(repo: Path) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip() or None


def git_dirty(repo: Path, paths: tuple[str, ...]) -> list[str]:
    try:
        out = subprocess.run(["git", "-C", str(repo), "status", "--porcelain", "--", *paths], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return []
    return sorted(line[3:] for line in out.stdout.splitlines() if line.strip())


def sync(source: Path, vendor: Path) -> int:
    missing = [rel for rel in VENDORED_FILES if not (source / rel).is_file()]
    if missing:
        print(f"FAIL: source files missing under {source}: {', '.join(missing)}")
        return 1
    dirty = git_dirty(source, VENDORED_FILES)
    if dirty:
        print("FAIL: source files have uncommitted changes; commit them in the design engine first: " + ", ".join(dirty))
        return 1
    files = {}
    for rel in VENDORED_FILES:
        target = vendor / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(normalised_bytes(source / rel))
        files[rel] = sha256_norm(target)
    manifest = {
        "schema_version": 1,
        "tool": "chwezi-slop",
        "source_repo": SOURCE_REPO,
        "source_path": "tools/slop-detector",
        "source_commit": git_head(source),
        "registry_sha256": files["tools/slop-detector/rules/registry.json"],
        "hash_mode": "sha256 after CRLF normalisation",
        "update_command": "python -X utf8 scripts/check-vendored-detector.py --sync-from ../chwezi-design-engine",
        "files": files,
    }
    (vendor / "VENDOR.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"synced {len(files)} files from {source} at {manifest['source_commit']}")
    return 0


def check(vendor: Path, source: Path | None, as_json: bool) -> int:
    manifest_path = vendor / "VENDOR.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        files = manifest["files"]
    except (OSError, ValueError, KeyError) as exc:
        print(f"NOT_ASSESSED: vendored detector manifest unreadable ({exc})")
        return 5
    findings: list[str] = []
    if sorted(files) != sorted(VENDORED_FILES):
        findings.append("manifest file list differs from the vendored set in check-vendored-detector.py")
    for rel, want in sorted(files.items()):
        path = vendor / rel
        if not path.is_file():
            findings.append(f"missing: {rel}")
        elif sha256_norm(path) != want:
            findings.append(f"hash mismatch (tampered or edited in place): {rel}")
    if files.get("tools/slop-detector/rules/registry.json") != manifest.get("registry_sha256"):
        findings.append("registry_sha256 does not match the registry.json file hash")

    source_status = "NOT_ASSESSED (sibling ../chwezi-design-engine absent)"
    drift: list[str] = []
    if source is not None and (source / "tools" / "slop-detector").is_dir():
        for rel in sorted(files):
            src = source / rel
            if not src.is_file():
                drift.append(f"absent in source: {rel}")
            elif (vendor / rel).is_file() and sha256_norm(src) != sha256_norm(vendor / rel):
                drift.append(f"differs from source: {rel}")
        source_status = "PASS" if not drift else "DRIFT"
    elif source is None:
        source_status = "NOT_ASSESSED (source comparison disabled)"

    result = {
        "vendored_files": len(files),
        "source_commit": manifest.get("source_commit"),
        "manifest": "PASS" if not findings else "FAIL",
        "manifest_findings": findings,
        "source_comparison": source_status,
        "source_drift": drift,
    }
    if as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for item in findings:
            print(f"FAIL {item}")
        for item in drift:
            print(f"DRIFT {item} (re-vendor with --sync-from and review the diff)")
        print(f"vendored detector: manifest {result['manifest']} ({len(files)} files, source commit {result['source_commit']}); source comparison {source_status}")
    return 1 if findings or drift else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vendor-dir", type=Path, default=DEFAULT_VENDOR)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="chwezi-design-engine checkout to compare with")
    parser.add_argument("--no-source", action="store_true", help="skip the source comparison (reported as NOT_ASSESSED)")
    parser.add_argument("--sync-from", type=Path, help="copy the vendored set from this chwezi-design-engine checkout and rewrite VENDOR.json")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.sync_from:
        return sync(args.sync_from.resolve(), args.vendor_dir.resolve())
    return check(args.vendor_dir.resolve(), None if args.no_source else args.source.resolve(), args.json)


if __name__ == "__main__":
    sys.exit(main())
