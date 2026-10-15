"""Acceptance tests for specification 001's documentation-only deliverable.

Run explicitly from the repository root with:

    pytest .referee/001-freeze-migration-decisions/

The feature deliberately has no executable product behavior.  These tests therefore
inspect the decision record and its supporting Markdown artifacts without importing,
building, or executing implementation code.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
FEATURE_DIR = REPO_ROOT / "specs" / "001-freeze-migration-decisions"

EXPECTED_ARTIFACTS = {
    Path("spec.md"),
    Path("plan.md"),
    Path("tasks.md"),
    Path("research.md"),
    Path("data-model.md"),
    Path("quickstart.md"),
    Path("contracts/downstream-specification-contract.md"),
    Path("checklists/requirements.md"),
}


def read_artifact(relative_path: str) -> str:
    path = FEATURE_DIR / relative_path
    assert path.is_file(), f"required documentation artifact is missing: {path}"
    return path.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def spec() -> str:
    return read_artifact("spec.md")


def section(document: str, heading: str, level: int = 2) -> str:
    """Return a Markdown section through (but not including) its next peer."""

    marks = "#" * level
    match = re.search(
        rf"(?ms)^{re.escape(marks)}\s+{re.escape(heading)}"
        rf"(?:\s+\*[^\n]*\*)?\s*$\n"
        rf"(.*?)(?=^{re.escape(marks)}\s+|\Z)",
        document,
    )
    assert match, f"missing Markdown section: {marks} {heading}"
    return match.group(1)


def assert_contains(text: str, *terms: str) -> None:
    folded = text.casefold()
    missing = [term for term in terms if term.casefold() not in folded]
    assert not missing, f"missing required content: {missing}"


def mdr_rows(decision_section: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in decision_section.splitlines():
        match = re.match(r"^\|\s*\**(MDR-\d{3})\**\s*\|", line)
        if match:
            assert match.group(1) not in rows, f"duplicate decision row: {match.group(1)}"
            rows[match.group(1)] = line
    return rows


def fenced_shell(document: str) -> str:
    blocks = re.findall(r"```(?:sh|bash|shell)?\s*\n(.*?)```", document, re.S | re.I)
    return "\n".join(blocks)


def test_feature_has_exactly_the_documentation_only_artifact_inventory() -> None:
    assert FEATURE_DIR.is_dir(), f"feature directory is missing: {FEATURE_DIR}"

    actual_files = {
        path.relative_to(FEATURE_DIR)
        for path in FEATURE_DIR.rglob("*")
        if path.is_file()
    }
    assert actual_files == EXPECTED_ARTIFACTS, (
        "specification 001 must contain exactly its decision/design Markdown artifacts; "
        f"missing={sorted(EXPECTED_ARTIFACTS - actual_files, key=str)}, "
        f"unexpected={sorted(actual_files - EXPECTED_ARTIFACTS, key=str)}"
    )
    assert all(path.suffix.casefold() == ".md" for path in actual_files)

    forbidden_directories = {
        "src",
        "source",
        "test",
        "tests",
        "bin",
        "obj",
        "build",
        "dist",
        "generated",
    }
    present_directories = {
        path.name.casefold() for path in FEATURE_DIR.rglob("*") if path.is_dir()
    }
    assert forbidden_directories.isdisjoint(present_directories), (
        "application, test, or generated-output directories are outside this work order"
    )


def test_decision_record_contains_exactly_five_final_mdr_rows(spec: str) -> None:
    decisions = section(spec, "Migration Decision Record", level=3)
    rows = mdr_rows(decisions)

    assert set(rows) == {f"MDR-{number:03d}" for number in range(1, 6)}
    assert len(rows) == 5
    assert not re.search(
        r"(?i)\b(?:TODO|TBD|TBC|FIXME|NEEDS?\s+CLARIFICATION|UNRESOLVED)\b|\?{3,}",
        decisions,
    ), "the frozen decision record still contains an unresolved marker"


def test_mdr_001_freezes_both_entry_surfaces_and_maui_windows(spec: str) -> None:
    row = mdr_rows(section(spec, "Migration Decision Record", level=3))["MDR-001"]
    assert_contains(row, "Main", "MainFrame", ".NET MAUI", "Windows")
    assert re.search(r"(?i)(?:distinct|separate|split|both).*(?:Main|entry)", row)

    whole_record = section(spec, "Requirements")
    assert_contains(whole_record, "WinForms", "WPF", "constitution")
    assert re.search(
        r"(?is)(?:WinForms.{0,100}WPF|WPF.{0,100}WinForms).{0,180}"
        r"(?:not selected|not selectable|exclude|mandat(?:e|es|ed)|\.NET MAUI)",
        whole_record,
    ), "WinForms and WPF must be explicitly rejected in favor of constitution-mandated MAUI"


def test_mdr_002_treats_java_swift_as_ambiguous_not_as_swift_evidence(spec: str) -> None:
    row = mdr_rows(section(spec, "Migration Decision Record", level=3))["MDR-002"]
    assert_contains(row, "Java(swift)", "ambiguous", "Java", "Swing", "console", "Swift")
    assert re.search(
        r"(?i)(?:no|not|absent|without).{0,80}(?:Swift|evidence)|"
        r"Swift.{0,80}(?:no|not|absent|without)",
        row,
    ), "MDR-002 must say that frozen evidence does not establish a Swift component"


def test_mdr_003_limits_module_info_to_dependency_evidence(spec: str) -> None:
    row = mdr_rows(section(spec, "Migration Decision Record", level=3))["MDR-003"]
    assert_contains(row, "module-info", "JavaFX", "dependency", "business behavior")
    assert re.search(
        r"(?i)(?:no|not|do not|exclude).{0,100}(?:separate|additional)?.{0,30}JavaFX.{0,30}"
        r"(?:UI|user-interface|user interface|surface)|"
        r"JavaFX.{0,100}(?:no|not|do not|exclude)",
        row,
    ), "JavaFX declarations must not create another UI surface"

    evidence = section(spec, "Evidence Traceability", level=3)
    assert_contains(
        evidence,
        "module-info",
        "contains no executable business behavior",
    )
    assert_contains(
        section(spec, "Requirements"),
        "JavaFX controls",
        "JavaFX FXML",
        "Java Desktop",
    )


def test_mdr_004_and_005_preserve_both_observed_identifier_behaviors(spec: str) -> None:
    decisions = mdr_rows(section(spec, "Migration Decision Record", level=3))
    assert_contains(
        decisions["MDR-004"],
        "OrderPlacement.getOrderId()",
        "100",
        "preserve",
        "intent",
    )
    assert_contains(
        decisions["MDR-005"],
        "1",
        "Main",
        "MainFrame",
        "preserve",
        "intent",
    )

    evidence = section(spec, "Evidence Traceability", level=3)
    assert_contains(
        evidence,
        "../../old/docs/prd.md",
        "FR-009",
        "FR-039",
        "FR-047",
        "OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);",
        "order = new OrderPlacement(1, chosenItems, timingPreference);",
        "return 100;",
    )


def test_identifier_evidence_is_separate_from_preservation_policy_and_unknown_intent(
    spec: str,
) -> None:
    requirements = section(spec, "Requirements")
    assert re.search(
        r"(?is)(?:does not measure|unknown|not (?:known|measured|classified)).{0,180}"
        r"(?:intended|intent|defect|bug|shortcut)|"
        r"(?:intent|intended|defect|bug|shortcut).{0,180}"
        r"(?:does not measure|unknown|not (?:known|measured|classified))",
        requirements,
    ), "the record must not invent an explanation for identifier values 1 and 100"
    assert re.search(
        r"(?is)(?:evidence|verified|documented).{0,220}(?:policy|preserv)|"
        r"(?:policy|preserv).{0,220}(?:evidence|verified|documented)",
        requirements,
    ), "observed identifier evidence and the migration preservation decision must be distinct"
    assert_contains(requirements, "separate behavior-change specification", "acceptance criteria")

    data_model = read_artifact("data-model.md")
    assert_contains(data_model, "MDR-004", "MDR-005", "Unknown", "evidence", "supers")
    for decision_id in ("MDR-004", "MDR-005"):
        assert re.search(
            rf"(?is){decision_id}.{{0,500}}\bUnknown\b|\bUnknown\b.{{0,500}}{decision_id}",
            data_model,
        ), f"{decision_id} must carry an explicit Unknown ambiguity state"


def test_every_required_legacy_claim_has_frozen_source_traceability(spec: str) -> None:
    evidence = section(spec, "Evidence Traceability", level=3)
    for claim_token in (
        "Main",
        "MainFrame",
        "Swing",
        "module-info",
        "OrderPlacement",
        "getOrderId",
        "return 100;",
    ):
        assert claim_token in evidence

    source_rows = [
        line
        for line in evidence.splitlines()
        if line.startswith("|") and "../../old/docs/" in line
    ]
    assert len(source_rows) >= 7, "each listed legacy-behavior claim needs its own frozen source row"
    assert all(re.search(r"\.\./\.\./old/docs/[\w.-]+\.md", row) for row in source_rows)
    assert_contains(evidence, "overview.md", "prd.md", "roadmap.md")


def test_research_records_evidence_judgment_and_rejected_alternatives_separately() -> None:
    research = read_artifact("research.md")
    for decision_id in ("MDR-001", "MDR-002", "MDR-003", "MDR-004", "MDR-005"):
        assert decision_id in research
    assert_contains(
        research,
        "../../old/docs/",
        "constitution",
        "evidence",
        "decision",
        "WinForms",
        "WPF",
        "Swift",
        "JavaFX",
        "Unknown",
    )
    assert re.search(r"(?i)alternatives?\s+(?:considered|rejected)|rejected alternatives?", research)


def test_downstream_contract_assigns_every_unconditional_mdr_citation() -> None:
    contract = read_artifact("contracts/downstream-specification-contract.md")
    expected = {
        "MDR-001": ("002", "009", "010"),
        "MDR-004": ("003", "005", "011"),
        "MDR-005": ("003", "009", "010", "011"),
    }
    for decision_id, downstream_specs in expected.items():
        assert decision_id in contract
        for spec_number in downstream_specs:
            assert re.search(
                rf"(?is){decision_id}.{{0,700}}(?:spec(?:ification)?\s*)?{spec_number}\b|"
                rf"(?:spec(?:ification)?\s*)?{spec_number}\b.{{0,700}}{decision_id}",
                contract,
            ), f"the downstream contract must bind specification {spec_number} to {decision_id}"

    assert_contains(contract, "MDR-002", "MDR-003", "Swift", "JavaFX", "Unknown")
    assert re.search(r"(?i)(?:conditional|when|if).{0,180}MDR-002|MDR-002.{0,180}(?:conditional|when|if)", contract)
    assert re.search(r"(?i)(?:conditional|when|if).{0,180}MDR-003|MDR-003.{0,180}(?:conditional|when|if)", contract)


def test_downstream_contract_rejects_silent_or_out_of_scope_changes() -> None:
    contract = read_artifact("contracts/downstream-specification-contract.md")
    assert_contains(
        contract,
        "Main",
        "MainFrame",
        "Swift",
        "JavaFX",
        "identifier",
        "acceptance criteria",
    )
    rejection_words = re.findall(r"(?i)\b(?:reject|nonconform|must not|invalid|fail)\w*\b", contract)
    assert len(rejection_words) >= 4, "the contract needs explicit rejection/nonconformance rules"
    assert re.search(r"(?is)(?:silent|without).{0,100}(?:override|supersed|change)", contract)


def test_quickstart_is_deterministic_document_inspection_not_a_build_or_runtime_suite() -> None:
    quickstart = read_artifact("quickstart.md")
    commands = fenced_shell(quickstart)
    assert commands.strip(), "quickstart.md must contain runnable inspection commands"
    assert_contains(commands, "rg", "find", "MDR-", "specs/001-freeze-migration-decisions")
    assert re.search(r"(?m)^\s*(?:test|\[\[|if\b|find\b|rg\b)", commands), (
        "quickstart must contain shell assertions, not only illustrative searches"
    )
    assert not re.search(
        r"(?im)^\s*(?:dotnet|msbuild|npm|yarn|pnpm|mvn|gradle|pytest|go\s+test)\b",
        commands,
    ), "building applications or running executable suites is deferred to later specifications"


def test_scope_boundaries_defer_roadmap_002_through_011(spec: str) -> None:
    boundaries = section(spec, "Scope Boundaries", level=3)
    assert_contains(
        boundaries,
        "Out of scope",
        "C# source",
        "project",
        "implementation",
        "domain component",
        "entry-flow port",
        "acceptance execution",
        "roadmap item",
        "specification 001",
    )

    requirements = section(spec, "Requirements")
    assert re.search(r"(?i)002\s+(?:through|[-–—])\s*011", requirements)
    assert_contains(requirements, "project skeleton", "component ports", "user-interface ports")


def test_requirements_checklist_records_a_completed_review() -> None:
    checklist = read_artifact("checklists/requirements.md")
    checkbox_lines = [line for line in checklist.splitlines() if re.match(r"^\s*-\s*\[[ xX]\]", line)]
    assert checkbox_lines, "requirements checklist must contain review items"
    incomplete = [line for line in checkbox_lines if not re.match(r"^\s*-\s*\[[xX]\]", line)]
    assert not incomplete, f"requirements review contains incomplete items: {incomplete}"
    assert_contains(checklist, "acceptance", "MDR-001", "MDR-005", "scope")
