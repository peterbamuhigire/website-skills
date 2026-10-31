"""Source-register expiry validator (WSK2-06).

Only the search register was machine-checked for expired review dates; the standards table in
`docs/standards-register.md` and the two performance registers were read by hand, so six rows went
overdue unnoticed. `scripts/validate-source-registers.py` checks the standards table and every JSON
register under `docs/source-registers/`. A review date can only move forward when a verification date
backs it, and the gap between the two may not exceed what the row's cadence allows.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_source_registers", ROOT / "scripts/validate-source-registers.py")
CHECK = importlib.util.module_from_spec(SPEC)
sys.modules["validate_source_registers"] = CHECK
SPEC.loader.exec_module(CHECK)

AS_OF = date(2026, 10, 31)

HEADER = "| Standard | Current controlled basis | Applies to | Owner | Cadence | Last verified | Next review |\n|---|---|---|---|---|---|---|\n"


def table(*rows: str) -> str:
    return "# Standards Register\n\nIntro text.\n\n" + HEADER + "\n".join(rows) + "\n\n## Legal boundary\n\nProse.\n"


def row(name="WCAG", cadence="Quarterly", verified="2026-10-31", review="2027-01-31") -> str:
    return f"| {name} | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Accessibility | accessibility-audit | {cadence} | {verified} | {review} |"


def errors_for(text: str, as_of: date = AS_OF) -> list[str]:
    return CHECK.check_standards_table(text, as_of)


def register(claims=None, sources=None, review="2026-12-31") -> dict:
    return {
        "register_id": "r",
        "review_date": review,
        "sources": sources if sources is not None else [{"source_id": "S1", "url": "https://example.com", "access_date": "2026-10-31"}],
        "claims": claims if claims is not None else [{"claim_id": "C1", "claim": "x", "source_ids": ["S1"], "review_date": "2026-12-31", "support_review": {"state": "supported"}}],
    }


# --- the markdown standards table ----------------------------------------------------------------


def test_a_current_row_passes():
    assert errors_for(table(row())) == []


def test_an_overdue_row_fails():
    assert any("overdue" in e for e in errors_for(table(row(verified="2026-07-01", review="2026-10-01"))))


def test_a_review_date_today_is_not_overdue():
    assert errors_for(table(row(verified="2026-10-01", review="2026-10-31"))) == []


def test_a_missing_or_unparseable_date_fails():
    assert errors_for(table(row(review="soon")))
    assert errors_for(table(row(verified="")))


def test_a_review_date_pushed_beyond_the_cadence_window_fails():
    quarterly_too_far = row(cadence="Quarterly", verified="2026-10-31", review="2027-10-31")
    monthly_too_far = row(cadence="Monthly", verified="2026-10-31", review="2027-01-31")
    assert any("cadence" in e for e in errors_for(table(quarterly_too_far)))
    assert any("cadence" in e for e in errors_for(table(monthly_too_far)))


def test_each_cadence_accepts_its_normal_window():
    assert errors_for(table(row(cadence="Monthly", verified="2026-10-31", review="2026-11-30"))) == []
    assert errors_for(table(row(cadence="Quarterly", verified="2026-10-31", review="2027-01-31"))) == []
    assert errors_for(table(row(cadence="Annual", verified="2026-10-31", review="2027-10-31"))) == []


def test_a_verification_date_in_the_future_fails():
    assert any("future" in e for e in errors_for(table(row(verified="2026-12-01", review="2027-01-31"))))


def test_an_unknown_cadence_fails():
    assert any("cadence" in e for e in errors_for(table(row(cadence="Whenever"))))


def test_a_file_without_the_table_fails_rather_than_passing_empty():
    assert errors_for("# Standards Register\n\nNo table here.\n")


# --- the JSON registers --------------------------------------------------------------------------


def test_a_current_register_passes():
    assert CHECK.check_register_data(register(), "r.json", AS_OF) == []


def test_an_overdue_claim_fails():
    claim = {"claim_id": "C1", "claim": "x", "source_ids": ["S1"], "review_date": "2026-10-30", "support_review": {"state": "supported"}}
    assert any("overdue" in e for e in CHECK.check_register_data(register(claims=[claim]), "r.json", AS_OF))


def test_a_claim_citing_an_unknown_source_fails():
    claim = {"claim_id": "C1", "claim": "x", "source_ids": ["NOPE"], "review_date": "2026-12-31", "support_review": {"state": "supported"}}
    assert any("unknown source" in e for e in CHECK.check_register_data(register(claims=[claim]), "r.json", AS_OF))


def test_a_source_recorded_in_another_register_of_the_folder_is_accepted(tmp_path):
    folder = tmp_path / "docs" / "source-registers"
    folder.mkdir(parents=True)
    (tmp_path / "docs" / "standards-register.md").write_text(table(row()), encoding="utf-8")
    early = register()
    late = register(claims=[{"claim_id": "C9", "claim": "y", "source_ids": ["S1"], "review_date": "2026-12-31", "support_review": {"state": "supported"}}], sources=[{"source_id": "S2", "url": "https://example.com", "access_date": "2026-10-31"}])
    (folder / "a.json").write_text(json.dumps(early), encoding="utf-8")
    (folder / "b.json").write_text(json.dumps(late), encoding="utf-8")
    assert CHECK.check_tree(tmp_path, AS_OF) == []
    (folder / "a.json").unlink()
    assert any("unknown source S1" in e for e in CHECK.check_tree(tmp_path, AS_OF))


def test_a_claim_with_no_sources_fails():
    claim = {"claim_id": "C1", "claim": "x", "source_ids": [], "review_date": "2026-12-31", "support_review": {"state": "supported"}}
    assert any("no source" in e for e in CHECK.check_register_data(register(claims=[claim]), "r.json", AS_OF))


def test_a_source_accessed_in_the_future_fails():
    source = {"source_id": "S1", "url": "https://example.com", "access_date": "2026-12-01"}
    assert any("future" in e for e in CHECK.check_register_data(register(sources=[source]), "r.json", AS_OF))


def test_duplicate_claim_ids_fail():
    claim = {"claim_id": "C1", "claim": "x", "source_ids": ["S1"], "review_date": "2026-12-31", "support_review": {"state": "supported"}}
    assert any("duplicate" in e for e in CHECK.check_register_data(register(claims=[claim, dict(claim)]), "r.json", AS_OF))


def test_an_unknown_support_state_fails_but_not_assessed_is_allowed():
    bad = {"claim_id": "C1", "claim": "x", "source_ids": ["S1"], "review_date": "2026-12-31", "support_review": {"state": "looks fine"}}
    good = {"claim_id": "C2", "claim": "y", "source_ids": ["S1"], "review_date": "2026-12-31", "support_review": {"state": "not_assessed"}}
    assert any("support state" in e for e in CHECK.check_register_data(register(claims=[bad]), "r.json", AS_OF))
    assert CHECK.check_register_data(register(claims=[good]), "r.json", AS_OF) == []


def test_a_register_with_no_claims_fails():
    assert CHECK.check_register_data(register(claims=[]), "r.json", AS_OF)


# --- command line and the live tree --------------------------------------------------------------


def test_cli_reports_overdue_rows_with_exit_1(tmp_path):
    docs = tmp_path / "docs"
    (docs / "source-registers").mkdir(parents=True)
    (docs / "standards-register.md").write_text(table(row(verified="2026-07-01", review="2026-10-01")), encoding="utf-8")
    (docs / "source-registers" / "r.json").write_text(json.dumps(register()), encoding="utf-8")
    result = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/validate-source-registers.py"), "--root", str(tmp_path), "--as-of", "2026-10-31"], capture_output=True, text=True)
    assert result.returncode == 1
    assert "overdue" in result.stdout


def test_cli_passes_a_clean_tree_and_rejects_a_bad_date_argument(tmp_path):
    docs = tmp_path / "docs"
    (docs / "source-registers").mkdir(parents=True)
    (docs / "standards-register.md").write_text(table(row()), encoding="utf-8")
    (docs / "source-registers" / "r.json").write_text(json.dumps(register()), encoding="utf-8")
    cmd = [sys.executable, "-X", "utf8", str(ROOT / "scripts/validate-source-registers.py"), "--root", str(tmp_path)]
    ok = subprocess.run(cmd + ["--as-of", "2026-10-31"], capture_output=True, text=True)
    assert ok.returncode == 0 and "PASS" in ok.stdout
    assert subprocess.run(cmd + ["--as-of", "tomorrow"], capture_output=True, text=True).returncode == 5


def test_the_live_registers_have_no_expired_or_malformed_records():
    errors = CHECK.check_tree(ROOT, date.today())
    assert errors == [], errors[:5]
