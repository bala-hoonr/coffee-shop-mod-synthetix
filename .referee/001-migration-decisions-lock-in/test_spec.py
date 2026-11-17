"""
Acceptance tests for spec 001 — Migration Decisions Lock-in.

These tests verify that:
    coffee-shop-mod-synthetix/specs/001-migration-decisions-lock-in/spec.md

satisfies every functional requirement (FR-001–FR-007), success criterion
(SC-001–SC-005), and user story (US1–US5) stated in the referee spec.

The deliverable is a documentation artifact only; no code is tested.  Each
test reads spec.md and asserts a required piece of content is present (or
absent, where the spec forbids it).

Run explicitly (recursive discovery skips this dotted folder):
    PYTHONPATH=/tmp/pypkgs python3 -m pytest \
        .referee/001-migration-decisions-lock-in/ -v
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Path resolution — locates spec.md relative to this test file
# ---------------------------------------------------------------------------

_WORKSPACE = Path(__file__).resolve().parent.parent.parent.parent
_SPEC_PATH = (
    _WORKSPACE
    / "coffee-shop-mod-synthetix"
    / "specs"
    / "001-migration-decisions-lock-in"
    / "spec.md"
)


def _spec() -> str:
    assert _SPEC_PATH.exists(), (
        f"spec.md not found at {_SPEC_PATH}.\n"
        f"Workspace root resolved to: {_WORKSPACE}"
    )
    return _SPEC_PATH.read_text(encoding="utf-8")


def _decision_record(text: str) -> str:
    """Return only the Decision Record section (from '## Decision Record' onwards)."""
    idx = text.find("## Decision Record")
    assert idx != -1, "spec.md must contain a '## Decision Record' section"
    return text[idx:]


# ===========================================================================
# FR-006 — Runtime-observation gap notice
# ===========================================================================


def test_fr006_gap_notice_present():
    """spec.md must carry the runtime-observation gap notice (FR-006)."""
    s = _spec()
    assert re.search(r"[Rr]untime-observation gap", s), (
        "Must carry a runtime-observation gap notice (FR-006)"
    )


def test_fr006_zero_of_28_execution_grounded():
    """Gap notice must state that 0 of 28 inventory items are execution-grounded (FR-006)."""
    s = _spec()
    assert "0 of 28" in s, (
        "Gap notice must state '0 of 28 inventory items are execution-grounded' (FR-006)"
    )


def test_fr006_static_reading_qualifier_words():
    """Gap notice must name the qualifier words 'always', 'unconditionally', and 'regardless'
    as resting on static reading only (FR-006)."""
    s = _spec()
    qualifiers = ["always", "unconditionally", "regardless"]
    present = [q for q in qualifiers if q in s]
    assert len(present) >= 2, (
        f"Gap notice must reference rules phrased as 'always', 'unconditionally', or "
        f"'regardless'; only found: {present} (FR-006)"
    )


def test_fr006_static_reading_phrase_in_gap_notice():
    """Gap notice must use the phrase 'static reading' (FR-006)."""
    s = _spec()
    assert "static reading" in s, (
        "Gap notice must state rules rest on static reading (FR-006)"
    )


# ===========================================================================
# FR-001 / US3 — WinForms as C# UI framework
# ===========================================================================


def test_fr001_winforms_named_as_ui_framework():
    """Decision 2 must name WinForms as the confirmed C# UI framework (FR-001, US3)."""
    s = _spec()
    assert "WinForms" in s, "Must name WinForms as the C# UI framework (FR-001)"


def test_fr001_winforms_in_decision_record():
    """WinForms must appear in the Decision Record section, not only in requirements (FR-001)."""
    dr = _decision_record(_spec())
    assert "WinForms" in dr, (
        "Decision Record must name WinForms as the confirmed C# UI framework (FR-001)"
    )


def test_fr001_widget_mapping_jframe_to_form():
    """Widget mapping table must map JFrame to Form (FR-001, US3 scenario 2, SC-004)."""
    s = _spec()
    assert re.search(r"JFrame\b.*\bForm\b", s), (
        "Must map JFrame → Form in the widget mapping table (FR-001)"
    )


def test_fr001_widget_mapping_jtabbedpane_to_tabcontrol():
    """Widget mapping table must map JTabbedPane to TabControl (FR-001, SC-004)."""
    s = _spec()
    assert re.search(r"JTabbedPane\b.*\bTabControl\b", s), (
        "Must map JTabbedPane → TabControl in the widget mapping table (FR-001)"
    )


def test_fr001_widget_mapping_jcombobox_to_combobox():
    """Widget mapping table must map JComboBox to ComboBox (FR-001, SC-004)."""
    s = _spec()
    assert re.search(r"JComboBox\b.*\bComboBox\b", s), (
        "Must map JComboBox → ComboBox in the widget mapping table (FR-001)"
    )


def test_fr001_widget_mapping_jradiobutton_to_radiobutton():
    """Widget mapping table must map JRadioButton to RadioButton (FR-001, SC-004)."""
    s = _spec()
    assert re.search(r"JRadioButton\b.*\bRadioButton\b", s), (
        "Must map JRadioButton → RadioButton in the widget mapping table (FR-001)"
    )


def test_fr001_widget_mapping_joptionpane_to_messagebox():
    """Widget mapping table must map JOptionPane to MessageBox or InputDialog (FR-001, SC-004)."""
    s = _spec()
    assert re.search(r"JOptionPane\b.*\b(MessageBox|InputDialog)\b", s), (
        "Must map JOptionPane → MessageBox / InputDialog in the widget mapping table (FR-001)"
    )


def test_sc004_widget_mapping_covers_all_five_swing_widgets():
    """Widget mapping table must cover all five Swing widget types used in MainFrame (SC-004)."""
    s = _spec()
    required = ["JFrame", "JTabbedPane", "JComboBox", "JRadioButton", "JOptionPane"]
    missing = [w for w in required if w not in s]
    assert not missing, (
        f"Widget mapping table missing entries for: {missing} (SC-004)"
    )


# ===========================================================================
# FR-002 / US4 — Both entry points in scope
# ===========================================================================


def test_fr002_main_cli_in_scope():
    """Decision 3 must record that the CLI entry point (Main) is in scope (FR-002, US4)."""
    dr = _decision_record(_spec())
    assert re.search(r"\bMain\b", dr), (
        "Decision Record must name 'Main' as a CLI entry point (FR-002)"
    )
    assert re.search(
        r"(Main.*in scope|both.*in scope|Main.*ported|both entry points)",
        dr, re.IGNORECASE
    ), "Decision Record must state Main is in scope (FR-002)"


def test_fr002_mainframe_gui_in_scope():
    """Decision 3 must record that the GUI entry point (MainFrame) is in scope (FR-002, US4)."""
    dr = _decision_record(_spec())
    assert re.search(r"\bMainFrame\b", dr), (
        "Decision Record must name 'MainFrame' as a GUI entry point (FR-002)"
    )
    assert re.search(
        r"(MainFrame.*in scope|both.*in scope|MainFrame.*ported|both entry points)",
        dr, re.IGNORECASE
    ), "Decision Record must state MainFrame is in scope (FR-002)"


def test_fr002_both_entry_points_ported_and_covered_by_parity_tests():
    """Decision 3 must state both entry points are ported and covered by parity tests (FR-002)."""
    s = _spec()
    assert re.search(r"both.*ported.*parity|parity.*both.*ported|both.*covered.*parity", s, re.IGNORECASE) or \
        re.search(r"both entry points are.*ported|both.*covered by parity", s, re.IGNORECASE), (
        "Must state both entry points are ported and covered by parity tests (FR-002)"
    )


# ===========================================================================
# FR-003 / US2 / SC-003 — Defect dispositions
# ===========================================================================


def test_fr003_defects_preserved_verbatim():
    """Decision 4 must state all four defects are preserved verbatim in the C# port (FR-003)."""
    s = _spec()
    assert re.search(r"preserved verbatim", s, re.IGNORECASE), (
        "Must state defects are 'preserved verbatim' in the C# port (FR-003)"
    )


def test_fr003_all_four_defect_identifiers_present():
    """Decision 4 must name all four known Java defects by their identifiers (FR-003)."""
    s = _spec()
    defect_ids = ["getOrderId", "processPayment", "addReview", "updateStatus"]
    missing = [d for d in defect_ids if d not in s]
    assert not missing, (
        f"Decision 4 is missing entries for: {missing} (FR-003)"
    )


def test_fr003_getorderid_returns_100():
    """Decision 4 must state getOrderId always returns 100 (FR-003)."""
    s = _spec()
    assert re.search(r"getOrderId.*\b100\b|\b100\b.*getOrderId", s), (
        "Must connect getOrderId to the constant return value 100 (FR-003)"
    )


def test_fr003_getorderid_parity_assertion_any_constructor_input():
    """Parity test assertion for getOrderId must specify return value == 100 for any
    constructor input (FR-003, US2 scenario 1, SC-003)."""
    s = _spec()
    assert re.search(
        r"(any constructor input|regardless.*orderId|any.*input.*\b100\b|\b100\b.*any.*input)",
        s, re.IGNORECASE
    ), (
        "Parity test assertion must specify return value == 100 for any constructor input "
        "(FR-003, SC-003)"
    )


def test_fr003_processpayment_sets_ispaymentcomplete_true():
    """Decision 4 must state processPayment unconditionally sets isPaymentComplete to true (FR-003)."""
    s = _spec()
    assert "isPaymentComplete" in s, "Must mention isPaymentComplete (FR-003)"
    assert re.search(r"isPaymentComplete.*true|true.*isPaymentComplete", s, re.IGNORECASE), (
        "Must state isPaymentComplete is set to true (FR-003)"
    )


def test_fr003_processpayment_parity_any_method_string_including_invalid():
    """Parity assertion for processPayment must cover any method string including
    invalid/empty values (FR-003, US2 scenario 2, SC-003)."""
    s = _spec()
    assert re.search(
        r"(any method string|any.*method.*value|invalid.*empty|empty.*invalid)",
        s, re.IGNORECASE
    ), (
        "Parity assertion must specify isPaymentComplete == true for any method string "
        "including invalid/empty values (FR-003, SC-003)"
    )


def test_fr003_addreview_overwrites_prior_state():
    """Decision 4 must state CustomerReview.addReview overwrites prior state (FR-003)."""
    s = _spec()
    assert "addReview" in s or "CustomerReview" in s, (
        "Must name addReview / CustomerReview in defect dispositions (FR-003)"
    )
    assert re.search(r"overwrite", s, re.IGNORECASE), (
        "Must describe the overwrite behaviour of addReview (FR-003)"
    )


def test_fr003_addreview_parity_second_call_overwrites_first():
    """Parity assertion for addReview must specify a second call overwrites the first
    (FR-003, US2 scenario 3, SC-003)."""
    s = _spec()
    assert re.search(
        r"(second call overwrites|second.*overwrites|overwrites.*first call|overwrites.*prior)",
        s, re.IGNORECASE
    ), (
        "Parity assertion must specify second call overwrites values written by the first call "
        "(FR-003, SC-003)"
    )


def test_fr003_updatestatus_accepts_any_string():
    """Decision 4 must state updateStatus accepts any string with no validation (FR-003)."""
    s = _spec()
    assert "updateStatus" in s, "Must mention updateStatus (FR-003)"
    assert re.search(r"(any string|no validation|arbitrary string)", s, re.IGNORECASE), (
        "Must state updateStatus accepts any string with no validation (FR-003)"
    )


def test_fr003_updatestatus_parity_arbitrary_strings_accepted_without_error():
    """Parity assertion for updateStatus must specify arbitrary strings are accepted
    without error (FR-003, US2 scenario 4, SC-003)."""
    s = _spec()
    assert re.search(
        r"(arbitrary strings.*accepted|arbitrary.*without error|empty.*null-like|out-of-domain)",
        s, re.IGNORECASE
    ), (
        "Parity assertion must specify arbitrary strings (empty, null-like, out-of-domain) "
        "are accepted without error (FR-003, SC-003)"
    )


def test_sc003_parity_assertions_in_decision_record():
    """SC-003: parity test assertions for all four defects must appear in the Decision Record
    section so spec 003 authors need no other source."""
    dr = _decision_record(_spec())
    defect_ids = ["getOrderId", "processPayment", "addReview", "updateStatus"]
    missing = [d for d in defect_ids if d not in dr]
    assert not missing, (
        f"Decision Record section is missing parity assertion entries for: {missing} (SC-003)"
    )


# ===========================================================================
# FR-004 / US1 — .NET 8 LTS target and packaging
# ===========================================================================


def test_fr004_dotnet8_lts_stated():
    """.NET 8 LTS must be stated as the confirmed target version (FR-004, US1 scenario 1)."""
    s = _spec()
    assert re.search(r"\.NET 8 LTS", s), (
        "Must state '.NET 8 LTS' as the confirmed target (FR-004)"
    )


def test_fr004_self_contained_single_file_executable():
    """Self-contained single-file executable must be stated as the packaging format (FR-004, US1)."""
    s = _spec()
    assert re.search(r"self.contained single.file executable", s, re.IGNORECASE), (
        "Must state 'self-contained single-file executable' (FR-004)"
    )


def test_fr004_windows_x64_target_platform():
    """Windows x64 must be stated as the target platform (FR-004, US1)."""
    s = _spec()
    assert re.search(r"Windows x64", s), (
        "Must state 'Windows x64' as the target platform (FR-004)"
    )


def test_fr004_no_other_dotnet_version_in_scope():
    """Must state no other .NET version or packaging format is in scope without an amendment (FR-004)."""
    s = _spec()
    assert re.search(
        r"(No other.*version|no other.*packaging|not in scope.*without.*amendment|"
        r"without.*amendment.*not in scope)",
        s, re.IGNORECASE
    ), "Must state no other .NET version or packaging format is in scope without amendment (FR-004)"


def test_fr004_dotnet_target_in_decision_record():
    """.NET 8 LTS must appear inside the Decision Record section itself (FR-004)."""
    dr = _decision_record(_spec())
    assert ".NET 8 LTS" in dr, (
        "'.NET 8 LTS' must appear in the Decision Record section (FR-004)"
    )


# ===========================================================================
# FR-007 / US1 — mvnw and module-info are Java-specific, not ported
# ===========================================================================


def test_fr007_mvnw_identified_as_java_specific():
    """Must record mvnw as Java-specific build infrastructure (FR-007, US1 scenario 2)."""
    s = _spec()
    assert "mvnw" in s, "Must mention mvnw (FR-007)"
    assert re.search(r"(Java.specific|no C# analogue|Java bootstrapping)", s, re.IGNORECASE), (
        "Must describe mvnw as Java-specific with no C# analogue (FR-007)"
    )


def test_fr007_mvnw_replaced_wholesale_by_dotnet_toolchain():
    """Must state mvnw is replaced wholesale by the .NET toolchain (FR-007, US1)."""
    s = _spec()
    assert re.search(
        r"replaced.*\.NET toolchain|\.NET toolchain.*replaces|replaced wholesale",
        s, re.IGNORECASE
    ), "Must state mvnw is replaced wholesale by the .NET toolchain (FR-007)"


def test_fr007_mvnw_rules_must_not_be_ported():
    """Must state mvnw rules must NOT be carried into C# specifications (FR-007)."""
    s = _spec()
    assert re.search(
        r"(MUST NOT.*C#|must not.*ported|not.*carried into C#|must not.*carry.*C#)",
        s, re.IGNORECASE
    ), "Must state mvnw rules must NOT be carried into C# specifications (FR-007)"


def test_fr007_module_info_also_identified():
    """Must also identify module-info as Java-specific with no C# analogue (FR-007)."""
    s = _spec()
    assert "module-info" in s, (
        "Must mention module-info as Java-specific infrastructure (FR-007)"
    )


# ===========================================================================
# FR-005 / US5 — Java(swift) spurious parenthetical
# ===========================================================================


def test_fr005_java_swift_spurious_parenthetical():
    """Must record 'Java(swift)' as a spurious parenthetical (FR-005, US5 scenario 1)."""
    s = _spec()
    assert re.search(r"spurious parenthetical", s, re.IGNORECASE), (
        "Must describe 'Java(swift)' as a spurious parenthetical (FR-005)"
    )


def test_fr005_no_swift_sources_in_estate():
    """Must state no Swift sources exist in the estate (FR-005, US5 scenario 1)."""
    s = _spec()
    assert re.search(r"[Nn]o Swift sources", s), (
        "Must state 'no Swift sources exist in the estate' (FR-005)"
    )


def test_fr005_pure_java_to_csharp_migration():
    """Must state the migration is a pure Java-to-C# port (FR-005, US5 scenario 2)."""
    s = _spec()
    assert re.search(r"pure Java.to.C#|Java-to-C#", s, re.IGNORECASE), (
        "Must state the migration is a pure Java-to-C# port (FR-005)"
    )


def test_fr005_java_swift_decision_in_decision_record():
    """Decision 1 about Java(swift) must appear in the Decision Record section (FR-005)."""
    dr = _decision_record(_spec())
    assert re.search(r"[Jj]ava\(swift\)|spurious parenthetical|[Nn]o Swift", dr), (
        "Decision Record must contain the Java(swift) disposition (FR-005)"
    )


# ===========================================================================
# SC-001 — Exactly five numbered decisions, no unresolved entries
# ===========================================================================


def test_sc001_exactly_five_numbered_decisions():
    """Decision Record must contain exactly five numbered decision headings (SC-001)."""
    s = _spec()
    decisions = re.findall(r"^#{2,4}\s+Decision\s+\d+\b", s, re.MULTILINE | re.IGNORECASE)
    assert len(decisions) == 5, (
        f"Expected exactly 5 numbered Decision headings, found {len(decisions)}: "
        f"{decisions} (SC-001)"
    )


def test_sc001_no_tbd_in_decision_cells():
    """No Decision cell value in the Decision Record tables must be 'TBD' (SC-001)."""
    s = _spec()
    assert not re.search(r"\|\s*\*\*Decision\*\*\s*\|\s*TBD\s*\|", s, re.IGNORECASE), (
        "A Decision cell must not contain 'TBD' (SC-001)"
    )


def test_sc001_no_open_questions_section():
    """The Open Questions section must be absent or resolved — not unresolved (SC-001)."""
    s = _spec()
    # An "Open Questions" heading with content below it would indicate unresolved items.
    # The constitution sync note says this section is dropped after all five are resolved.
    if re.search(r"^#+\s*Open Questions\s*$", s, re.MULTILINE | re.IGNORECASE):
        # If the heading exists, it must have no TBD or unresolved entries under it
        assert not re.search(r"Open Questions[\s\S]{0,500}TBD", s, re.IGNORECASE), (
            "Open Questions section must not contain unresolved (TBD) entries (SC-001)"
        )


# ===========================================================================
# SC-002 — Each decision is self-contained and unambiguous
# ===========================================================================


def test_sc002_four_standard_decisions_have_question_field():
    """Decisions 1, 2, 3, and 5 must each have a Question field row in their Key/Value table.
    Decision 4 uses a defect-matrix format and is checked separately (SC-002)."""
    s = _spec()
    question_rows = re.findall(r"\|\s*\*\*Question\*\*\s*\|", s)
    assert len(question_rows) >= 4, (
        f"Expected at least 4 '| **Question** |' table rows (Decisions 1–3 and 5), "
        f"found {len(question_rows)} (SC-002)"
    )


def test_sc002_four_standard_decisions_have_decision_field():
    """Decisions 1, 2, 3, and 5 must each have a Decision field row in their Key/Value table.
    Decision 4 states its answer in prose and is checked separately (SC-002)."""
    s = _spec()
    decision_rows = re.findall(r"\|\s*\*\*Decision\*\*\s*\|", s)
    assert len(decision_rows) >= 4, (
        f"Expected at least 4 '| **Decision** |' table rows (Decisions 1–3 and 5), "
        f"found {len(decision_rows)} (SC-002)"
    )


def test_sc002_decision4_states_answer_in_prose():
    """Decision 4 must state its answer ('preserved verbatim') in prose since it uses a
    defect-matrix format rather than a Key/Value table (SC-002)."""
    s = _spec()
    # Extract Decision 4 section
    m = re.search(r"(^#{2,4}\s+Decision\s+4\b.*?)(?=^#{2,4}\s+Decision\s+\d+\b|\Z)",
                  s, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    assert m, "Must have a 'Decision 4' heading (SC-002)"
    d4 = m.group(1)
    assert re.search(r"preserved verbatim", d4, re.IGNORECASE), (
        "Decision 4 must state the answer ('preserved verbatim') in its section (SC-002)"
    )
    # Must also carry evidence anchors
    assert re.search(r"(overview\.md|Evidence anchor|\.\./\.\./old/docs/)", d4), (
        "Decision 4 must carry evidence anchors in its section (SC-002, Principle I)"
    )


def test_sc002_decision_dates_recorded():
    """Each decision must carry an operator decision date of 2026-11-17 (SC-002)."""
    s = _spec()
    # The date should appear in the Decision Record section
    dr = _decision_record(s)
    date_entries = re.findall(r"2026-11-17", dr)
    assert len(date_entries) >= 1, (
        "Decision Record must record operator decision date 2026-11-17 (SC-002)"
    )


def test_sc002_four_standard_decisions_have_evidence_field():
    """Decisions 1, 2, 3, and 5 must each have an Evidence field row in their Key/Value table.
    Decision 4 carries evidence in prose and is checked separately (SC-002, Principle I)."""
    s = _spec()
    evidence_rows = re.findall(r"\|\s*\*\*Evidence\*\*\s*\|", s)
    assert len(evidence_rows) >= 4, (
        f"Expected at least 4 '| **Evidence** |' table rows (Decisions 1–3 and 5), "
        f"found {len(evidence_rows)} (SC-002, Principle I)"
    )


# ===========================================================================
# SC-005 — Constitution consistency (Constitution v1.1.0)
# ===========================================================================


def test_sc005_no_alternative_dotnet_version_as_confirmed_target():
    """Spec must not name a .NET version other than 8 as the confirmed target (SC-005, Principle IV)."""
    s = _spec()
    # Reject any Decision cell that names .NET 6/7/9 as the confirmed target
    assert not re.search(r"\*\*Decision\*\*.*\.NET\s+(6|7|9|10)\b", s, re.IGNORECASE), (
        "Spec must not confirm a .NET version other than 8 as the target (SC-005)"
    )


def test_sc005_no_alternative_ui_framework_confirmed():
    """Spec must not confirm an alternative UI framework in place of WinForms (SC-005, Principle V)."""
    s = _spec()
    competing = ["WPF", "MAUI", "Avalonia", "Blazor"]
    for fw in competing:
        # Reject only if named in a **Decision** cell
        assert not re.search(rf"\*\*Decision\*\*.*\b{fw}\b", s, re.IGNORECASE), (
            f"Spec must not confirm {fw} as the UI framework — must be WinForms (SC-005)"
        )


def test_sc005_defects_not_stated_as_corrected():
    """Decision 4 must not state that defects are corrected (SC-005, Principle III)."""
    s = _spec()
    assert not re.search(
        r"\*\*Decision\*\*.*\bcorrect(ed)?\b.*defect|\*\*Decision\*\*.*defect.*\bcorrect(ed)?\b",
        s, re.IGNORECASE
    ), "Decision 4 must not state defects are corrected — must be preserved verbatim (SC-005)"


def test_sc005_evidence_anchors_reference_old_docs():
    """Every Evidence field must cite ../../old/docs/ as a source (SC-005, Principle I)."""
    s = _spec()
    assert re.search(r"\.\./\.\./old/docs/", s), (
        "Evidence fields must cite ../../old/docs/ (SC-005, Constitution Principle I)"
    )


def test_sc005_approach_md_cited_for_java_swift_decision():
    """Decision 1 (Java(swift)) must cite approach.md as evidence (SC-005, Principle I)."""
    s = _spec()
    assert re.search(r"approach\.md", s), (
        "Decision 1 must cite approach.md for the spurious parenthetical finding "
        "(SC-005, Constitution Principle I)"
    )


def test_sc005_overview_md_cited_for_defects_and_widgets():
    """Decisions 2 and 4 must cite overview.md as evidence (SC-005, Principle I)."""
    s = _spec()
    assert re.search(r"overview\.md", s), (
        "Decisions must cite overview.md for Swing widget and defect evidence "
        "(SC-005, Constitution Principle I)"
    )


# ===========================================================================
# US1 quick-read acceptance — spec.md alone answers the scaffolding questions
# ===========================================================================


def test_us1_decision_record_states_dotnet8_lts_self_contained_windows_x64():
    """US1: the Decision Record section alone must answer the scaffolding question
    (.NET 8 LTS, self-contained single-file executable, Windows x64)."""
    dr = _decision_record(_spec())
    assert ".NET 8 LTS" in dr, "Decision Record must state .NET 8 LTS (US1)"
    assert re.search(r"single.file executable", dr, re.IGNORECASE), (
        "Decision Record must state single-file executable (US1)"
    )
    assert "Windows x64" in dr, "Decision Record must state Windows x64 (US1)"


def test_us1_decision_record_states_mvnw_replaced_by_dotnet():
    """US1: the Decision Record section must state mvnw is replaced by the .NET toolchain."""
    dr = _decision_record(_spec())
    assert "mvnw" in dr, "Decision Record must name mvnw (US1)"
    assert re.search(r"replaced.*\.NET|\.NET.*replac", dr, re.IGNORECASE), (
        "Decision Record must state mvnw is replaced by the .NET toolchain (US1)"
    )


# ===========================================================================
# US3 quick-read acceptance — widget mapping answers the analogue question
# ===========================================================================


def test_us3_decision_record_contains_winforms_and_jframe_form_mapping():
    """US3: Decision Record must state WinForms and the JFrame → Form mapping."""
    dr = _decision_record(_spec())
    assert "WinForms" in dr, "Decision Record must name WinForms (US3)"
    assert re.search(r"JFrame.*\bForm\b", dr), (
        "Decision Record must map JFrame → Form (US3 scenario 2)"
    )


# ===========================================================================
# US4 quick-read acceptance — entry-point scope unambiguous from Decision Record
# ===========================================================================


def test_us4_decision_record_names_both_main_and_mainframe():
    """US4: Decision Record must name both Main and MainFrame as in-scope entry points."""
    dr = _decision_record(_spec())
    assert re.search(r"\bMain\b", dr), "Decision Record must mention Main (US4)"
    assert re.search(r"\bMainFrame\b", dr), "Decision Record must mention MainFrame (US4)"


# ===========================================================================
# US5 quick-read acceptance — Java(swift) resolved in Decision Record
# ===========================================================================


def test_us5_decision_record_resolves_java_swift_wording():
    """US5: Decision Record must resolve the Java(swift) wording as a spurious parenthetical."""
    dr = _decision_record(_spec())
    assert re.search(r"spurious parenthetical|[Nn]o Swift sources", dr), (
        "Decision Record must resolve Java(swift) as a spurious parenthetical (US5)"
    )
