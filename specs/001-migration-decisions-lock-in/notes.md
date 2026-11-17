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

## T005

## T006

## T007

## T008

## T009
