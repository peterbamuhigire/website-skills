import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "fixtures" / "website-multilingual"


def load(name):
    return json.loads((FIXTURE_ROOT / name).read_text(encoding="utf-8"))


def test_identity_minimum_fields_pass_and_unnecessary_field_fails():
    records = {record["id"]: record for record in load("identity-fixtures.json")["records"]}
    minimum = records["minimum-display-name-locale"]
    unnecessary = records["unnecessary-legal-name"]
    assert set(minimum["fields"]) == {"display_name", "locale"}
    assert minimum["decision_status"] == "PASS"
    assert minimum["native_review_status"] == "NOT_ASSESSED"
    assert "legal_name" in unnecessary["fields"]
    assert unnecessary["decision_status"] == "FAIL"


def test_identity_optional_fields_have_explicit_omission_or_purpose():
    for record in load("identity-fixtures.json")["records"]:
        fields = record["fields"]
        optional = {"legal_name", "preferred_name", "pronunciation", "relationship", "transliteration"}
        assert record["consent_or_authority"] in {"not_needed", "user_choice"}
        assert record["retention"]
        for field in optional & set(fields):
            assert field == "transliteration" or record["purpose"]
        assert record["optional_fields_omitted"] or record["kind"] == "intentional-omission"


def test_mixed_language_fixture_cases_cover_required_shapes():
    records = load("identity-fixtures.json")["records"]
    kinds = {record["kind"] for record in records}
    assert {"original-script", "transliteration", "kinship", "mixed-script", "intentional-omission"} <= kinds
    for record in records:
        assert record["source_text"]
        assert record["source_locale"] and record["target_locale"]
        assert record["expected"]
        assert record["decision_status"] in {"PASS", "FAIL", "NOT_ASSESSED"}
        assert record["native_review_status"] in {"PASS", "FAIL", "NOT_ASSESSED"}
    assert next(r for r in records if r["kind"] == "mixed-script")["bidi_isolation"] is True


def test_page_role_contract_has_normal_and_failure_paths():
    records = {record["id"]: record for record in load("page-role-contract.json")["records"]}
    passing = records["current-service-page"]
    failing = records["schema-invisible-fact"]
    assert passing["page_role"] == "current"
    assert passing["owner"] and passing["reviewer"] and passing["review_date"]
    assert passing["status"] == "PASS"
    assert failing["metadata_and_schema"] != "matches-visible-content"
    assert failing["status"] == "FAIL"
    assert not failing["review_date"]


def test_question_mark_scan_audit_preserves_static_and_unassessed_states():
    records = {record["id"]: record for record in load("question-mark-scan.json")["records"]}
    clear = records["clear-service-route"]
    ambiguous = records["ambiguous-primary-action"]
    unavailable = records["browser-evidence-unavailable"]
    assert clear["status"] == "PASS" and clear["findings"] == []
    assert ambiguous["status"] == "FAIL"
    assert ambiguous["findings"][0]["owner"] and ambiguous["findings"][0]["locator"]
    assert unavailable["status"] == "NOT_ASSESSED"
    assert unavailable["evidence_type"] == "NOT_ASSESSED"
    assert all(value == "NOT_ASSESSED" for key, value in unavailable.items() if key in {
        "purpose", "information_scent", "labels_and_affordance", "hierarchy",
        "scan_path", "recovery", "noise", "privacy_friction"
    })
