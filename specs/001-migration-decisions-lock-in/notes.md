# Task Evidence Notes

## T001

## T002

**Task**: Verify that the runtime-observation gap notice (FR-006) in `spec.md` states: (1) all
rules derived from static reading, (2) 0 of 28 inventory items are execution-grounded, and
(3) rules phrased as "always", "unconditionally", or "regardless" rest on static reading only.

**Findings**: PASS — all three required statements are present in the gap notice at the top of
`specs/001-migration-decisions-lock-in/spec.md` (lines immediately after the preamble block),
under the heading `> **Runtime-observation gap** (Constitution Principle VI)`.

Verbatim substrings verified:

1. **Static reading**: "Every rule in this document was derived from static reading of the legacy
   Java estate as recorded in `../../old/docs/`."

2. **0 of 28 execution-grounded**: "The Java application was not executed; 0 of 28 inventory
   items are execution-grounded."

3. **Keyword phrases on static reading only**: "Rules phrased as 'always', 'unconditionally', or
   'regardless' reflect the static reading only."

All three conditions required by FR-006 are satisfied. The gap notice also includes a forward
obligation — future work executing the Java application MUST reconcile divergence before declaring
the port complete — which is consistent with Constitution Principle VI.

**Result**: FR-006 VERIFIED.

## T003

**Task**: Read `specs/001-migration-decisions-lock-in/spec.md` and `.specify/memory/constitution.md`
and verify no decision in the Decision Record contradicts any principle in constitution v1.1.0
(SC-005). Record which principles were checked and any conflict identified.

**Principles checked** (constitution v1.1.0, all six core principles plus Migration Constraints):

| Principle | Description | Decision(s) checked | Result |
|---|---|---|---|
| I. Evidence-First Description | Every rule traceable to verbatim substring of `../../old/docs/`; symbols reproduced verbatim | All five decisions | PASS |
| II. Parity Testing is Mandatory | Every carried rule must have a passing C# test; tests written before/alongside | Decision 4 (defect parity test assertions) | PASS |
| III. Decide-Before-Drift (Known Defects) | All four defects preserved verbatim; parity tests MUST assert defective behaviour | Decision 4 | PASS |
| IV. Infrastructure is Replaced, Not Ported | mvnw / module-info not ported; .NET 8 LTS self-contained single-file for Windows x64 | Decision 5 | PASS |
| V. UI Framework and Entry-Point Scope | WinForms; both Main (CLI) and MainFrame (GUI) in scope | Decisions 2 and 3 | PASS |
| VI. Runtime-Observation Gap | Specs encoding "always"/"unconditionally"/"regardless" rules MUST carry a gap notice | spec.md preamble gap notice + Decision 4 defect descriptions | PASS |
| Migration Constraints | Java(swift) is spurious parenthetical; .NET 8 LTS Windows x64; five-item menu; etc. | Decision 1, Decision 5 | PASS |

**Detailed findings per decision**:

- **Decision 1 — Java(swift) wording**: Records "Spurious parenthetical. No Swift sources exist
  in the estate. The migration is a pure Java-to-C# port." Evidence cites
  `../../old/docs/approach.md` — "No Swift sources were seen in the estate" and the eight-file
  Java inventory from `../../old/docs/overview.md`. This is identical to the Migration Constraints
  entry in the constitution and satisfies Principle I (verbatim evidence anchors). **No conflict.**

- **Decision 2 — C# UI framework**: Records WinForms with widget mapping table: JFrame → Form,
  JTabbedPane → TabControl, JComboBox → ComboBox, JRadioButton → RadioButton,
  JOptionPane → MessageBox / InputDialog. This matches Principle V verbatim ("Widget mapping:
  JFrame → Form, JTabbedPane → TabControl, JComboBox → ComboBox, JRadioButton → RadioButton,
  JOptionPane → MessageBox / InputDialog"). Evidence cites `../../old/docs/overview.md`. **No conflict.**

- **Decision 3 — Entry-point scope**: Records "Both entry points are in scope. Main (CLI) and
  MainFrame (GUI) are both ported and both covered by parity tests." This matches Principle V
  verbatim ("both entry points are in scope — the CLI entry point (Main) and the GUI entry point
  (MainFrame) are both ported and both covered by parity tests"). Evidence cites verbatim
  substrings from `../../old/docs/overview.md`. **No conflict.**

- **Decision 4 — Known defect dispositions**: Records all four defects as "preserved verbatim"
  with parity test assertions:
  - `OrderPlacement.getOrderId`: assert return value == `100` for any constructor input — matches
    Principle III exactly.
  - `PaymentOptions.processPayment`: assert `isPaymentComplete == true` for any method string
    including invalid/empty values — matches Principle III exactly.
  - `CustomerReview.addReview`: assert that a second call overwrites the values written by the
    first call — matches Principle III exactly.
  - `OrderStatus.updateStatus`: assert arbitrary strings are accepted without error — matches
    Principle III exactly.
  Rationale in Decision 4 ("A literal port reproduces defects … operator chose the literal path")
  is identical to the Principle III rationale. Evidence anchors cite verbatim substrings from
  `../../old/docs/overview.md` satisfying Principle I. **No conflict.**

- **Decision 5 — Target .NET version and packaging**: Records ".NET 8 LTS, self-contained
  single-file executable for Windows x64." This matches Principle IV ("Confirmed replacement
  target (operator decision, 2026-11-17): .NET 8 LTS, self-contained single-file executable for
  Windows x64") and the Migration Constraints ("The confirmed C# deliverable is .NET 8 LTS,
  self-contained single-file executable for Windows x64") verbatim. Records that mvnw and
  module-info are Java-specific with no C# analogue and are replaced wholesale by the .NET
  toolchain, consistent with Principle IV. Evidence cites `../../old/docs/overview.md`. **No conflict.**

- **Runtime-observation gap notice** (preamble): spec.md opens with the gap notice mandated by
  Principle VI. Decision 4 uses the phrases "always", "unconditionally", "regardless" — all
  covered by the preamble notice. **No conflict.**

**Conflicts identified**: None.

**Result**: SC-005 VERIFIED — the Decision Record is internally consistent with constitution
v1.1.0. No decision contradicts any principle or migration constraint.

## T004

**Task**: Read `specs/001-migration-decisions-lock-in/spec.md` Decision 5 and verify it records:
(1) .NET 8 LTS, self-contained single-file executable for Windows x64 as the confirmed target
(FR-004); (2) no other .NET version or packaging format is in scope without an amendment; and
(3) `mvnw` and `module-info` are Java-specific with no C# analogue and are replaced wholesale by
the .NET toolchain (FR-007). Verify evidence anchors cite verbatim substrings from
`../../old/docs/` (Constitution Principle I).

**Findings**:

**FR-004 — Confirmed target (.NET 8 LTS, self-contained single-file for Windows x64)**

Decision 5 Decision field states verbatim: ".NET 8 LTS, self-contained single-file executable for
Windows x64". The Impact field states: "Spec 002 (Target .NET Scaffolding) MUST target .NET 8 LTS
and produce a self-contained single-file executable for Windows x64. No other version or packaging
format is in scope without an amendment." Both required statements are present. ✅

Evidence anchor for the .NET 8 LTS target cites Constitution Principle IV:
"Confirmed replacement target (operator decision, 2026-11-17): .NET 8 LTS, self-contained
single-file executable for Windows x64." This is an operator decision, not derivable from the
Java estate, so citing the constitution is appropriate — Constitution Principle I covers rules
derived from the estate; the target platform is an operator choice. ✅

**FR-007 — `mvnw` and `module-info` are Java-specific with no C# analogue**

Decision 5 Evidence field states: "`mvnw` and `module-info` are Java-specific build infrastructure
with no C# analogue (`../../old/docs/overview.md`)." The Impact field states: "`mvnw` rules MUST
NOT be ported; they are replaced wholesale by the .NET toolchain." The Requirements section
(FR-007) states both `mvnw` and `module-info` rules "MUST NOT be carried into C# specifications
as requirements. They are replaced wholesale by the .NET toolchain (Constitution Principle IV)."

All three clauses required by FR-007 are present across Decision 5 and FR-007 in the
Requirements section. ✅

**Constitution Principle I — Evidence anchors verified against `../../old/docs/overview.md`**

FR-007 evidence anchor: `mvnw` — "bootstraps Maven builds without requiring a pre-installed
Maven". Confirmed verbatim in `../../old/docs/overview.md`: "The Maven Wrapper shell script (mvnw)
bootstraps Maven builds without requiring a pre-installed Maven." ✅

FR-007 evidence anchor: `module-info` — "declares dependencies on javafx.controls, javafx.fxml,
and java.desktop". Confirmed verbatim in `../../old/docs/overview.md`: "The Java module descriptor
for com.example.coffeeshopapplication declares dependencies on javafx.controls, javafx.fxml, and
java.desktop." ✅

**Amendment scope**

Decision 5 Impact field states: "No other version or packaging format is in scope without an
amendment." Required clause is present. ✅

**Summary table**:

| Check | Required text | Present in spec.md | Verbatim anchor confirmed |
|---|---|---|---|
| FR-004: target | ".NET 8 LTS, self-contained single-file executable for Windows x64" | Decision 5 Decision field | Operator decision (constitution Principle IV) |
| FR-004: amendment scope | "No other version or packaging format is in scope without an amendment" | Decision 5 Impact field | N/A — normative rule |
| FR-007: mvnw Java-specific | "`mvnw` … Java-specific … no C# analogue" | Decision 5 Evidence field | "bootstraps Maven builds without requiring a pre-installed Maven" in `../../old/docs/overview.md` |
| FR-007: module-info Java-specific | "`module-info` … Java-specific … no C# analogue" | Decision 5 Evidence field + FR-007 | "declares dependencies on javafx.controls, javafx.fxml, and java.desktop" in `../../old/docs/overview.md` |
| FR-007: replaced by .NET toolchain | "replaced wholesale by the .NET toolchain" | Decision 5 Impact field + FR-007 | N/A — normative rule |

**Result**: FR-004 VERIFIED. FR-007 VERIFIED. Constitution Principle I VERIFIED for all evidence
anchors referencing `../../old/docs/`.

## T005

## T006

## T007

## T008

## T009
