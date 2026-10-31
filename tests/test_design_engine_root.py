"""Design-engine sibling discovery is configurable and shared (WSK2-04).

The vendored-detector check used to look only at `../chwezi-design-engine`, so on a checkout that
sits beside `design-system-skills` its source comparison was NOT_ASSESSED by default. Both validators
now resolve the checkout through scripts/design_engine_root.py.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


FINDER = load("design_engine_root", "scripts/design_engine_root.py")
DETECTOR = load("check_vendored_detector", "scripts/check-vendored-detector.py")


def make_engine(path: Path, marker: str = "skills") -> Path:
    (path / marker).mkdir(parents=True)
    return path


def test_explicit_path_wins_over_everything(tmp_path):
    explicit = make_engine(tmp_path / "explicit")
    make_engine(tmp_path / "web" / "x")  # unrelated
    sibling = make_engine(tmp_path / "design-system-skills")
    env = {FINDER.ENV_ROOT: str(sibling)}
    assert FINDER.find_design_engine(tmp_path / "web", explicit=explicit, env=env) == explicit


def test_environment_root_beats_sibling_names(tmp_path):
    (tmp_path / "web").mkdir()
    make_engine(tmp_path / "design-system-skills")
    chosen = make_engine(tmp_path / "elsewhere" / "engine")
    env = {FINDER.ENV_ROOT: str(chosen)}
    assert FINDER.find_design_engine(tmp_path / "web", env=env) == chosen


def test_engines_root_variable_is_searched_for_both_names(tmp_path):
    (tmp_path / "web").mkdir()
    engines = tmp_path / "engines"
    chosen = make_engine(engines / "chwezi-design-engine")
    env = {FINDER.ENV_ENGINES_ROOT: str(engines)}
    assert FINDER.find_design_engine(tmp_path / "web", env=env) == chosen


def test_canonical_name_is_preferred_over_the_old_name(tmp_path):
    web = tmp_path / "web"
    web.mkdir()
    old = make_engine(tmp_path / "chwezi-design-engine")
    new = make_engine(tmp_path / "design-system-skills")
    assert FINDER.find_design_engine(web, env={}) == new
    assert old != new


def test_old_name_is_still_found_when_it_is_the_only_one(tmp_path):
    web = tmp_path / "web"
    web.mkdir()
    old = make_engine(tmp_path / "chwezi-design-engine")
    assert FINDER.find_design_engine(web, env={}) == old


def test_marker_must_exist_so_an_empty_folder_is_not_a_match(tmp_path):
    web = tmp_path / "web"
    web.mkdir()
    (tmp_path / "design-system-skills").mkdir()
    assert FINDER.find_design_engine(web, env={}) is None
    assert FINDER.find_design_engine(web, env={}, marker="tools/slop-detector") is None


def test_absent_engine_returns_none(tmp_path):
    (tmp_path / "web").mkdir()
    assert FINDER.find_design_engine(tmp_path / "web", env={}) is None


def vendor_copy(tmp_path: Path):
    """A tiny vendored set whose manifest matches, and a design engine holding identical files."""
    source = tmp_path / "design-system-skills"
    vendor = tmp_path / "vendor"
    files = {}
    for rel in DETECTOR.VENDORED_FILES:
        for base in (source, vendor):
            target = base / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f"// {rel}\n", encoding="utf-8")
        files[rel] = DETECTOR.sha256_norm(vendor / rel)
    manifest = {"files": files, "registry_sha256": files["tools/slop-detector/rules/registry.json"], "source_commit": "abc"}
    (vendor / "VENDOR.json").write_text(__import__("json").dumps(manifest), encoding="utf-8")
    return source, vendor


def run_check(vendor: Path, *args, env=None):
    import os

    full_env = {k: v for k, v in os.environ.items() if k not in {FINDER.ENV_ROOT, FINDER.ENV_ENGINES_ROOT}}
    full_env.update(env or {})
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(ROOT / "scripts/check-vendored-detector.py"), "--vendor-dir", str(vendor), *args],
        capture_output=True, text=True, env=full_env, cwd=vendor.parent,
    )


def test_check_uses_the_environment_root_and_compares(tmp_path):
    source, vendor = vendor_copy(tmp_path)
    result = run_check(vendor, env={FINDER.ENV_ROOT: str(source)})
    assert result.returncode == 0, result.stdout + result.stderr
    assert "source comparison PASS" in result.stdout


def test_check_reports_drift_found_through_the_environment_root(tmp_path):
    source, vendor = vendor_copy(tmp_path)
    (source / "tools/slop-detector/rules/registry.json").write_text("changed\n", encoding="utf-8")
    result = run_check(vendor, env={FINDER.ENV_ROOT: str(source)})
    assert result.returncode == 1
    assert "DRIFT" in result.stdout


def test_check_without_any_engine_is_not_assessed_and_says_how_to_fix_it(tmp_path):
    import contextlib
    import io

    _source, vendor = vendor_copy(tmp_path)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = DETECTOR.check(vendor, None, False)
    assert code == 0
    assert "source comparison NOT_ASSESSED" in out.getvalue()
    assert FINDER.ENV_ROOT in out.getvalue()


def test_disabled_comparison_is_labelled_differently_from_a_missing_engine(tmp_path):
    import contextlib
    import io

    _source, vendor = vendor_copy(tmp_path)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = DETECTOR.check(vendor, None, False, disabled=True)
    assert code == 0
    assert "comparison disabled" in out.getvalue()
