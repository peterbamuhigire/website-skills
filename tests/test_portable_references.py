"""Portable-reference validator (WSK2-05).

Machine-specific absolute paths and relative links that do not resolve were a hand check. The validator
`scripts/check_portable_references.py` fails on them in active content, holds history documents and client
prompts to a no-increase ceiling, and checks every Markdown relative link. This file quotes the patterns
it detects, so it is listed under `skip_files` in `quality/portable-references-policy.json`.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_portable_references", ROOT / "scripts/check_portable_references.py")
CHECK = importlib.util.module_from_spec(SPEC)
sys.modules["check_portable_references"] = CHECK
SPEC.loader.exec_module(CHECK)

POLICY = {
    "schema_version": 1,
    "history_prefixes": ["docs/history/", "prompts/"],
    "history_ceilings": {},
    "skip_prefixes": ["scripts/vendor/", "node_modules/"],
    "skip_files": [],
}


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def kinds(text: str):
    return [kind for _line, kind, _snippet in CHECK.find_path_hits(text)]


# --- path patterns -------------------------------------------------------------------------------


def test_windows_user_profile_and_server_folder_paths_are_found_with_either_slash():
    assert kinds("see C:\\wamp64\\www\\engine") == ["machine-path"]
    assert kinds("see C:/wamp64/www/engine") == ["machine-path"]
    assert kinds("D:\\Users\\Someone\\Downloads") == ["machine-path"]
    assert kinds("e:/users/someone/x") == ["machine-path"]
    assert kinds('"C:\\\\Users\\\\Someone\\\\file"') == ["machine-path"]


def test_conventional_system_paths_used_as_examples_are_not_machine_specific():
    text = "\n".join(["C:\\Program Files\\Git\\bin\\bash.exe", "Remove-Item C:\\temp\\cache", "git -C C:\\repo status", "C:/Windows/System32"])
    assert kinds(text) == []


def test_posix_home_paths_are_found():
    assert kinds("cd /home/someone/project") == ["machine-path"]
    assert kinds("open /Users/Someone/Downloads/x") == ["machine-path"]


def test_a_bare_wamp64_folder_name_is_found():
    assert kinds("the wamp64 folder") == ["machine-path"]


def test_urls_times_and_ordinary_text_are_not_paths():
    text = "\n".join(
        [
            "https://example.com/a/b",
            "ftp://host/dir and http://localhost:8080/x",
            "Open 09:00/17:00 on weekdays",
            "Note:/ a slash after a colon in prose",
            "Use ~/notes and ./local and ../up and /var/www/html",
            "a/b/c.md",
        ]
    )
    assert kinds(text) == []


def test_line_numbers_are_one_based_and_snippets_are_trimmed():
    hits = CHECK.find_path_hits("clean\nbad C:\\wamp64\\x here\nclean")
    assert hits[0][0] == 2
    assert "C:" in hits[0][2]


def test_the_allow_marker_skips_only_its_own_line():
    text = "C:\\wamp64\\a portable-ok\nC:\\wamp64\\b"
    assert [line for line, _k, _s in CHECK.find_path_hits(text)] == [2]


# --- links ---------------------------------------------------------------------------------------


def test_a_broken_relative_link_is_reported(tmp_path):
    write(tmp_path, "docs/a.md", "[x](missing.md)\n")
    problems = CHECK.find_link_problems(tmp_path / "docs/a.md", (tmp_path / "docs/a.md").read_text(), tmp_path)
    assert [(line, target) for line, target, _why in problems] == [(1, "missing.md")]


def test_working_links_anchors_urls_and_images_are_not_reported(tmp_path):
    write(tmp_path, "docs/b.md", "")
    write(tmp_path, "docs/img.png", "")
    text = "[a](b.md) [b](b.md#section) [c](#top) [d](https://example.com) [e](mailto:x@y.z) ![i](img.png) [f](<b.md>)\n"
    write(tmp_path, "docs/a.md", text)
    assert CHECK.find_link_problems(tmp_path / "docs/a.md", text, tmp_path) == []


def test_a_broken_image_is_reported(tmp_path):
    text = "![alt](gone.png)\n"
    write(tmp_path, "a.md", text)
    assert [t for _l, t, _w in CHECK.find_link_problems(tmp_path / "a.md", text, tmp_path)] == ["gone.png"]


def test_a_link_that_leaves_the_checkout_is_reported_even_when_the_target_exists(tmp_path):
    outside = tmp_path / "sibling.md"
    outside.write_text("x", encoding="utf-8")
    root = tmp_path / "engine"
    text = "[s](../sibling.md)\n"
    write(root, "a.md", text)
    problems = CHECK.find_link_problems(root / "a.md", text, root)
    assert len(problems) == 1 and "leaves the checkout" in problems[0][2]


def test_links_in_fenced_code_and_inline_code_are_ignored(tmp_path):
    text = "```\n[x](missing.md)\n```\n~~~\n[y](missing.md)\n~~~\nUse `[z](missing.md)` literally.\n"
    write(tmp_path, "a.md", text)
    assert CHECK.find_link_problems(tmp_path / "a.md", text, tmp_path) == []


def test_template_placeholders_in_link_targets_are_ignored(tmp_path):
    text = "[a]({{ url }}) [c](${HOME}/x) [d](*.md) [e]({{url}})\n"
    write(tmp_path, "a.md", text)
    assert CHECK.find_link_problems(tmp_path / "a.md", text, tmp_path) == []


def test_encoded_names_and_titles_resolve(tmp_path):
    write(tmp_path, "docs/my file.md", "")
    text = '[a](my%20file.md) [b](my%20file.md "A title")\n'
    write(tmp_path, "docs/a.md", text)
    assert CHECK.find_link_problems(tmp_path / "docs/a.md", text, tmp_path) == []


def test_a_root_relative_link_resolves_against_the_checkout(tmp_path):
    write(tmp_path, "docs/target.md", "")
    text = "[ok](/docs/target.md) [bad](/docs/nope.md)\n"
    write(tmp_path, "a.md", text)
    assert [t for _l, t, _w in CHECK.find_link_problems(tmp_path / "a.md", text, tmp_path)] == ["/docs/nope.md"]


# --- scope, ceilings, skips ----------------------------------------------------------------------


def test_active_content_allows_no_machine_path(tmp_path):
    write(tmp_path, "skills/x/SKILL.md", "uses C:\\wamp64\\www\\y\n")
    result = CHECK.scan(tmp_path, POLICY)
    assert [v["file"] for v in result["violations"]] == ["skills/x/SKILL.md"]
    assert result["violations"][0]["kind"] == "machine-path"


def test_history_files_are_held_to_a_ceiling_not_to_zero(tmp_path):
    write(tmp_path, "prompts/client.md", "C:\\wamp64\\a\nC:\\wamp64\\b\n")
    policy = {**POLICY, "history_ceilings": {"prompts/client.md": 2}}
    result = CHECK.scan(tmp_path, policy)
    assert result["violations"] == []
    assert result["history"] == {"prompts/client.md": 2}


def test_history_files_may_not_grow_past_their_ceiling(tmp_path):
    write(tmp_path, "prompts/client.md", "C:\\wamp64\\a\nC:\\wamp64\\b\nC:\\wamp64\\c\n")
    policy = {**POLICY, "history_ceilings": {"prompts/client.md": 2}}
    violations = CHECK.scan(tmp_path, policy)["violations"]
    assert len(violations) == 1 and violations[0]["kind"] == "history-ceiling"


def test_a_new_history_file_with_a_path_fails_because_its_ceiling_is_zero(tmp_path):
    write(tmp_path, "docs/history/new.md", "C:\\wamp64\\a\n")
    violations = CHECK.scan(tmp_path, POLICY)["violations"]
    assert [v["kind"] for v in violations] == ["history-ceiling"]


def test_a_history_file_below_its_ceiling_is_fine_and_reported(tmp_path):
    write(tmp_path, "prompts/client.md", "clean\n")
    policy = {**POLICY, "history_ceilings": {"prompts/client.md": 5}}
    assert CHECK.scan(tmp_path, policy)["violations"] == []


def test_skipped_prefixes_and_files_are_not_scanned(tmp_path):
    write(tmp_path, "scripts/vendor/x.js", "C:\\wamp64\\a\n")
    write(tmp_path, "tools/quotes.md", "C:\\wamp64\\a\n")
    policy = {**POLICY, "skip_files": ["tools/quotes.md"]}
    assert CHECK.scan(tmp_path, policy)["violations"] == []


def test_links_are_checked_in_history_documents_too(tmp_path):
    write(tmp_path, "docs/history/old.md", "[x](gone.md)\n")
    violations = CHECK.scan(tmp_path, POLICY)["violations"]
    assert [v["kind"] for v in violations] == ["broken-link"]


def test_binary_and_undecodable_files_are_skipped_without_error(tmp_path):
    path = tmp_path / "skills" / "blob.md"
    path.parent.mkdir(parents=True)
    path.write_bytes(b"\xff\xfe\x00\x01 C:\\wamp64\\x \x80\x81")
    (tmp_path / "skills" / "pic.png").write_bytes(b"C:\\wamp64\\x")
    assert CHECK.scan(tmp_path, POLICY)["violations"] == []


# --- command line --------------------------------------------------------------------------------


def run_cli(*args):
    return subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/check_portable_references.py"), *args], capture_output=True, text=True)


def test_cli_exit_codes_and_messages(tmp_path):
    write(tmp_path, "skills/x/SKILL.md", "uses C:\\wamp64\\www\\y\n")
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps(POLICY), encoding="utf-8")
    bad = run_cli("--root", str(tmp_path), "--policy", str(policy))
    assert bad.returncode == 1
    assert "skills/x/SKILL.md:1" in bad.stdout and "machine-path" in bad.stdout
    (tmp_path / "skills/x/SKILL.md").write_text("clean\n", encoding="utf-8")
    good = run_cli("--root", str(tmp_path), "--policy", str(policy))
    assert good.returncode == 0 and "PASS" in good.stdout


def test_cli_measure_prints_history_ceilings_without_failing(tmp_path):
    write(tmp_path, "prompts/client.md", "C:\\wamp64\\a\nC:\\wamp64\\b\n")
    policy = tmp_path / "policy.json"
    policy.write_text(json.dumps(POLICY), encoding="utf-8")
    result = run_cli("--root", str(tmp_path), "--policy", str(policy), "--measure")
    assert result.returncode == 0
    assert json.loads(result.stdout) == {"prompts/client.md": 2}


def test_cli_missing_policy_is_a_prerequisite_error(tmp_path):
    result = run_cli("--root", str(tmp_path), "--policy", str(tmp_path / "nope.json"))
    assert result.returncode == 5


# --- the live tree -------------------------------------------------------------------------------


def test_the_live_engine_has_no_active_machine_paths_or_broken_links():
    policy = json.loads((ROOT / "quality/portable-references-policy.json").read_text(encoding="utf-8"))
    result = CHECK.scan(ROOT, policy)
    assert result["violations"] == [], result["violations"][:5]
