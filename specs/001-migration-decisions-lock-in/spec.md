# Feature Specification: Migration Decisions Lock-in

**Feature Branch**: `001-migration-decisions-lock-in`

**Created**: 2026-11-17

**Status**: Draft

**Input**: User description: "Captures and freezes the decisions the operator left open: the C# UI
framework replacing Swing on Windows, whether both the CLI entry and the Swing GUI entry survive
the port or one is dropped, whether known Java defects (such as getOrderId returning a constant,
addReview overwriting without checking prior state, processPayment unconditionally marking
complete) are preserved verbatim or corrected, the target .NET version and packaging format, and
the intended reading of the 'Java(swift)' wording in the stated goal. Delivers a written decision
record only; does not port any code or write tests."

> **Runtime-observation gap** (Constitution Principle VI): Every rule in this document was derived
> from static reading of the legacy Java estate as recorded in `../../old/docs/`. The Java
> application was not executed; 0 of 28 inventory items are execution-grounded. Rules phrased as
> "always", "unconditionally", or "regardless" reflect the static reading only. Future work that
> executes the Java application against the same scripted inputs used by the parity test suite
> MUST reconcile any divergence into either a corrected rule or a known-difference note before
> declaring the port complete.

---

## User Scenarios & Testing *(mandatory)*

This specification is consumed by the engineers and tools that author the eleven downstream
migration specifications. The "users" are those authors; the value delivered is the removal of
ambiguity that would otherwise block every later wave.

### User Story 1 - Read decision record to begin .NET scaffolding (Priority: P1)

An engineer authoring spec 002 (Target .NET Scaffolding) needs to know the confirmed .NET target
version and packaging format before writing a single scaffolding requirement. Without this record,
spec 002 cannot fix its requirements to a concrete deliverable.

**Why this priority**: Spec 002 depends on spec 001 and no scaffolding requirement can be written
without the .NET version and packaging format being fixed. It unblocks the entire wave chain.

**Independent Test**: Reviewer reads this document and can state, without consulting any other
source, the exact .NET version, the packaging format, and the target platform for the Windows
deliverable.

**Acceptance Scenarios**:

1. **Given** this document is the only source consulted, **When** an engineer asks "what .NET
   version and packaging format is required?", **Then** the answer is unambiguously .NET 8 LTS,
   self-contained single-file executable for Windows x64.
2. **Given** this document is the only source consulted, **When** an engineer asks "what replaces
   the mvnw bootstrap?", **Then** the document states that mvnw is replaced wholesale by the
   .NET toolchain and no mvnw rule crosses into the C# deliverable.

---

### User Story 2 - Read defect dispositions to write parity tests (Priority: P1)

An engineer authoring specs 007–009 (OrderPlacement, PaymentOptions, CustomerReview ports) needs
to know whether the four known Java defects are preserved verbatim or corrected so that parity
test expectations can be written correctly and unambiguously.

**Why this priority**: Parity tests (spec 003) gate every domain port. A wrong or absent defect
decision causes the parity test expectations to be written incorrectly, invalidating the entire
test harness.

**Independent Test**: Reviewer reads this document and can state, for each of the four named
defects, the exact decision (preserve or correct) and the specific assertion the parity test
MUST make.

**Acceptance Scenarios**:

1. **Given** the `OrderPlacement.getOrderId` defect, **When** an engineer reads the decision,
   **Then** they know to write the parity test asserting the return value is `100` regardless of
   the `orderId` supplied at construction.
2. **Given** the `PaymentOptions.processPayment` defect, **When** an engineer reads the decision,
   **Then** they know to assert that any payment method value results in
   `isPaymentComplete == true`.
3. **Given** the `CustomerReview.addReview` defect, **When** an engineer reads the decision,
   **Then** they know to assert the overwrite behaviour: a second call overwrites `orderId` and
   `review` without checking prior state.
4. **Given** the `OrderStatus.updateStatus` defect, **When** an engineer reads the decision,
   **Then** they know to assert that arbitrary strings are accepted as a status value.

---

### User Story 3 - Read UI framework decision to begin GUI and adapter specs (Priority: P1)

An engineer authoring spec 004 (Swing-Affordance C# Adapters) or spec 011 (GUI Entry Window Port)
needs the confirmed C# UI framework before mapping any Swing widget to its C# analogue. Without
this decision, no widget mapping table can be written and no GUI porting requirement can be stated.

**Why this priority**: Spec 004 and spec 011 both depend on spec 001. Blocking them blocks the
entire GUI port wave.

**Independent Test**: Reviewer reads this document and can state the confirmed C# UI framework and
the widget mapping table for the five Swing widgets used in `MainFrame`.

**Acceptance Scenarios**:

1. **Given** this document, **When** an engineer asks "which C# UI framework replaces Swing?",
   **Then** the answer is WinForms.
2. **Given** this document, **When** an engineer asks "what is the C# analogue of JFrame?",
   **Then** the answer is Form.
3. **Given** the five Swing widget types (`JFrame`, `JTabbedPane`, `JComboBox`, `JRadioButton`,
   `JOptionPane`), **When** an engineer reads the widget mapping table, **Then** each maps to
   exactly one named WinForms widget.

---

### User Story 4 - Read entry-point scope to bound the port (Priority: P1)

An engineer authoring spec 010 (Console Entry Flow Port) or spec 011 (GUI Entry Window Port) needs
to know whether both entry points (`Main` and `MainFrame`) survive the port, or whether one is
dropped, before scoping either specification.

**Why this priority**: Dropping an entry point eliminates an entire specification; keeping both
doubles the scope of specs 010 and 011. The decision must precede any scoping work.

**Independent Test**: Reviewer reads this document and can state whether spec 010 delivers a C#
console port or a deprecation record, and likewise for spec 011.

**Acceptance Scenarios**:

1. **Given** this document, **When** an engineer asks "does the CLI entry point (Main) survive?",
   **Then** the answer is yes — both entry points are in scope.
2. **Given** this document, **When** an engineer asks "does the GUI entry point (MainFrame)
   survive?", **Then** the answer is yes — both entry points are in scope.

---

### User Story 5 - Resolve the 'Java(swift)' wording in the stated goal (Priority: P2)

An engineer reading the stated goal ("migrate from Java(swift) to csharp(windows) application")
needs to know whether Swift sources exist in the estate and must be treated as an additional
migration source.

**Why this priority**: A live Swift source base would expand the scope of every specification.
Confirming the absence of Swift source lets all specifications ignore it without risk.

**Independent Test**: Reviewer reads this document and can confirm that no Swift sources exist in
the estate and the port is a pure Java-to-C# migration.

**Acceptance Scenarios**:

1. **Given** this document, **When** an engineer asks "is there a Swift source base to migrate?",
   **Then** the answer is no — 'Java(swift)' is a spurious parenthetical; no Swift sources are
   present in the estate.
2. **Given** this document, **When** an engineer asks "what is the full scope of source
   languages?", **Then** the answer is Java only.

---

### Edge Cases

- What if a future operator decision amends one of these frozen decisions? The constitution
  requires a written rationale, a version bump to the constitution, and an amendment to this
  specification before any downstream spec is updated.
- What if the running Java application, when observed, exhibits behaviour that contradicts a rule
  recorded here? The runtime-observation gap notice at the top of this document applies; the
  divergence must be resolved by a corrected rule or a known-difference note before the port is
  declared complete.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: This document MUST record the C# UI framework confirmed as the replacement for
  Swing on Windows as WinForms, with a widget mapping table covering `JFrame`, `JTabbedPane`,
  `JComboBox`, `JRadioButton`, and `JOptionPane`.
  *Evidence anchor*: `MainFrame` — "presenting a 700×500 tabbed window with four tabs: Menu
  (checkbox item selection), Order Details (timing radio buttons), Payment (dropdown), and Review
  (rating radio buttons)" (`../../old/docs/overview.md`).

- **FR-002**: This document MUST record that both entry points are in scope: the CLI entry point
  (`Main`) and the GUI entry point (`MainFrame`) are both ported and both covered by parity tests.
  *Evidence anchor*: `Main` — "Main is the CLI entry point"; `MainFrame` — "MainFrame is the
  Swing GUI entry point" (`../../old/docs/overview.md`).

- **FR-003**: This document MUST record the disposition of each of the four known Java defects as
  **preserved verbatim** in the C# port, and MUST state the exact assertion the parity test for
  each defect MUST make:

  - `OrderPlacement.getOrderId` always returns `100` regardless of the `orderId` field supplied
    at construction. Parity test MUST assert the return value is `100`.
    *Evidence anchor*: "Notably, getOrderId always returns the hardcoded value 100 regardless of
    the orderId field supplied at construction" (`../../old/docs/overview.md`).

  - `PaymentOptions.processPayment` unconditionally sets `isPaymentComplete` to `true` with no
    validation of the payment method value. Parity test MUST assert that any payment method value
    results in `isPaymentComplete == true`.
    *Evidence anchor*: "processPayment accepts a method string, stores it, sets isPaymentComplete
    to true, and prints a confirmation. No validation of the payment method value is performed"
    (`../../old/docs/overview.md`).

  - `CustomerReview.addReview` (the setter pair) overwrites any previously stored `orderId` and
    `review` on the same instance without checking prior state. Parity test MUST assert the
    overwrite behaviour.
    *Evidence anchor*: `CustomerReview` — "It holds two fields (orderId and review) and exposes
    one method to record a review. No persistence or validation logic is present"
    (`../../old/docs/overview.md`).

  - `OrderStatus.updateStatus` accepts any string with no validation. Parity test MUST assert
    that arbitrary strings are accepted as a status value.
    *Evidence anchor*: "can be updated to any string value via updateStatus"
    (`../../old/docs/overview.md`).

- **FR-004**: This document MUST record the confirmed target as .NET 8 LTS, self-contained
  single-file executable for Windows x64. No other .NET version or packaging format is in scope
  unless a subsequent operator decision amends this specification and the constitution.
  *Evidence anchor*: Constitution Principle IV — "Confirmed replacement target (operator decision,
  2026-11-17): .NET 8 LTS, self-contained single-file executable for Windows x64."

- **FR-005**: This document MUST record that the 'Java(swift)' wording in the stated goal is a
  spurious parenthetical: no Swift sources exist in the estate; the migration is a pure
  Java-to-C# port.
  *Evidence anchor*: Constitution Migration Constraints — "The Java(swift) wording in the stated
  goal is confirmed as a spurious parenthetical: no Swift sources exist in the estate; the
  migration is a pure Java-to-C# port (operator decision, 2026-11-17; corroborated by
  `../../old/docs/approach.md`)."

- **FR-006**: This document MUST carry the runtime-observation gap notice (Constitution Principle
  VI) stating that all rules were derived from static reading with 0% execution-grounded coverage,
  and that any rule phrased as "always", "unconditionally", or "regardless" rests on static
  reading, not on a live trace.

- **FR-007**: This document MUST record that `mvnw` and `module-info` are Java-specific build
  and module infrastructure with no C# analogue; their verified rules describe Java bootstrapping
  concerns only and MUST NOT be carried into C# specifications as requirements. They are replaced
  wholesale by the .NET toolchain (Constitution Principle IV).
  *Evidence anchor*: `mvnw` — "bootstraps Maven builds without requiring a pre-installed Maven";
  `module-info` — "declares dependencies on javafx.controls, javafx.fxml, and java.desktop"
  (`../../old/docs/overview.md`).

### Key Entities

- **Decision Record**: A frozen, evidence-backed statement of an operator choice that blocks one
  or more downstream specifications. Each decision record contains: the question resolved, the
  answer chosen, the operator decision date (2026-11-17), and the verbatim evidence anchors
  supporting it.

- **Known Defect**: A behaviour in the Java estate that is demonstrably incorrect (returns a
  constant regardless of input, sets a flag unconditionally, overwrites without guard, accepts
  invalid values without validation) but is recorded verbatim in the inventory. Each defect has
  an associated disposition decision (preserve or correct) and a required parity test assertion.

---

## Decision Record

This section is the normative output of this specification. It enumerates each decision in a
form directly usable by downstream specifications and by the parity test harness.

### Decision 1 — Java(swift) wording

| Field | Value |
|---|---|
| **Question** | What does 'Java(swift)' mean in the stated goal? |
| **Decision** | Spurious parenthetical. No Swift sources exist in the estate. The migration is a pure Java-to-C# port. |
| **Date** | 2026-11-17 |
| **Evidence** | `../../old/docs/approach.md` — "No Swift sources were seen in the estate"; `../../old/docs/overview.md` lists eight Java source files and one shell script with no Swift files. |
| **Impact** | All 11 downstream specifications scope to Java-to-C# only. No Swift source is treated as in-scope. |

### Decision 2 — C# UI framework

| Field | Value |
|---|---|
| **Question** | Which C# UI framework replaces Swing on the Windows target? |
| **Decision** | WinForms |
| **Date** | 2026-11-17 |
| **Evidence** | `MainFrame` uses: `JFrame` (top-level window), `JTabbedPane` (tabbed container), `JComboBox` (payment dropdown), `JRadioButton` (timing and review radio buttons), `JOptionPane` (status update dialog). WinForms provides a structural analogue for each. (`../../old/docs/overview.md`) |
| **Impact** | Spec 004 (Swing-Affordance Adapters) and spec 011 (GUI Entry Window Port) MUST use the WinForms widget vocabulary. |

**Widget mapping table** (Swing → WinForms):

| Swing widget | WinForms analogue |
|---|---|
| `JFrame` | `Form` |
| `JTabbedPane` | `TabControl` |
| `JComboBox` | `ComboBox` |
| `JRadioButton` | `RadioButton` |
| `JOptionPane` | `MessageBox` / `InputDialog` |

### Decision 3 — Entry-point scope

| Field | Value |
|---|---|
| **Question** | Do both CLI (`Main`) and GUI (`MainFrame`) entry points survive the port, or is one dropped? |
| **Decision** | Both entry points are in scope. `Main` (CLI) and `MainFrame` (GUI) are both ported and both covered by parity tests. |
| **Date** | 2026-11-17 |
| **Evidence** | `Main` — "Main is the CLI entry point for the coffee shop application"; `MainFrame` — "MainFrame is the Swing GUI entry point, presenting a 700×500 tabbed window" (`../../old/docs/overview.md`). Both carry verified rules. |
| **Impact** | Spec 010 (Console Entry Flow Port) delivers a C# console port, not a deprecation record. Spec 011 (GUI Entry Window Port) delivers a WinForms port, not a deprecation record. |

### Decision 4 — Known defect dispositions

All four defects are **preserved verbatim** in the C# port. The parity test for each defect MUST
assert the defective behaviour so the code generator cannot accidentally correct it.

> *Rationale*: A literal port reproduces defects; a corrective port changes behaviour. The
> operator chose the literal path so the parity test suite pins the Java-identical behaviour.
> Future correction is an explicit opt-in requiring a new operator decision and a spec amendment.

| Defect | Java identifier | Defective behaviour | Parity test assertion |
|---|---|---|---|
| Constant order ID | `OrderPlacement.getOrderId` | Always returns `100` regardless of `orderId` supplied at construction | Assert return value == `100` for any constructor input |
| Unconditional payment | `PaymentOptions.processPayment` | Sets `isPaymentComplete` to `true` with no validation of the payment method value | Assert `isPaymentComplete == true` for any method string including invalid/empty values |
| Silent review overwrite | `CustomerReview.addReview` (setter pair) | Overwrites `orderId` and `review` on the same instance without checking prior state | Assert that a second call overwrites the values written by the first call |
| Unconstrained status | `OrderStatus.updateStatus` | Accepts any string with no validation | Assert that arbitrary strings (empty, null-like, out-of-domain) are accepted without error |

*Evidence anchors*: `../../old/docs/overview.md` — `OrderPlacement`: "getOrderId always returns
the hardcoded value 100 regardless of the orderId field supplied at construction";
`PaymentOptions`: "No validation of the payment method value is performed";
`CustomerReview`: "No persistence or validation logic is present"; `OrderStatus`: "can be updated
to any string value via updateStatus".

### Decision 5 — Target .NET version and packaging

| Field | Value |
|---|---|
| **Question** | What .NET version and packaging format does the Windows deliverable target? |
| **Decision** | .NET 8 LTS, self-contained single-file executable for Windows x64 |
| **Date** | 2026-11-17 |
| **Evidence** | `mvnw` and `module-info` are Java-specific build infrastructure with no C# analogue (`../../old/docs/overview.md`). The confirmed replacement target is .NET 8 LTS per Constitution Principle IV. |
| **Impact** | Spec 002 (Target .NET Scaffolding) MUST target .NET 8 LTS and produce a self-contained single-file executable for Windows x64. No other version or packaging format is in scope without an amendment. `mvnw` rules MUST NOT be ported; they are replaced wholesale by the .NET toolchain. |

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All five open questions from `../../old/docs/approach.md` are answered and recorded
  as frozen, evidence-backed decisions in this document, with no question left unresolved.

- **SC-002**: Each of the eleven downstream specifications (specs 002–011) can be authored without
  returning to this document for clarification — the decisions recorded here are unambiguous and
  self-contained for the purpose of scoping and requirement writing.

- **SC-003**: The parity test harness (spec 003) can encode the correct expected value for each
  of the four known defects by reading the Decision 4 table in this document, without consulting
  any other source.

- **SC-004**: The widget mapping table in Decision 2 covers every Swing widget type present in
  `MainFrame` (five widget types: `JFrame`, `JTabbedPane`, `JComboBox`, `JRadioButton`,
  `JOptionPane`), leaving no widget unmapped.

- **SC-005**: This document is internally consistent with the Migration Constitution v1.1.0 — no
  decision recorded here contradicts a principle or migration constraint stated in the
  constitution.

---

## Assumptions

- The five open questions enumerated in `../../old/docs/approach.md` are the complete set of
  blocking decisions for this migration. No additional blocking decisions are known at the time
  of this writing.
- The operator decisions recorded here were made on 2026-11-17 and are reflected in the
  Migration Constitution v1.1.0 (`../../old/docs/` — this workspace's constitution file).
- The Java estate as recorded in `../../old/docs/` is frozen — no additional Java source files
  will be added to the estate after this specification is written.
- Making the fixed five-item menu (`Cappuccino`, `Latte`, `Matcha Latte`, `Cold Brew`,
  `Hot Chocolate`) data-driven is out of scope unless the Migration Decisions specification is
  amended with an explicit operator approval (Constitution Migration Constraints).
- The forced `Preparing` → `Served` status progression after CLI order placement is verified
  behaviour from `Main` and is preserved verbatim per Decision 4 (preserve all defects/behaviours
  verbatim). Evidence: `Main` — "Order status is also demonstrated by transitioning through
  Preparing and Served" (`../../old/docs/overview.md`).
- No runtime execution of the Java application was performed; all rules are derived from static
  reading with 0% execution-grounded coverage (Constitution Principle VI).
