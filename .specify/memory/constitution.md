<!--
SYNC IMPACT REPORT
==================
Version change: 1.0.0 → 1.1.0 (MINOR — operator answers recorded; five open questions resolved
  and removed; Principles III, IV, V, and Migration Constraints materially updated)
Modified principles:
  - III. Decide-Before-Drift (Known Defects): decision recorded as "preserve verbatim" for all
    four defects; parity tests MUST assert defective behaviour.
  - IV. Infrastructure is Replaced, Not Ported: .NET 8 LTS, self-contained single-file executable
    for Windows x64 added as the confirmed replacement target.
  - V. UI Framework and Entry-Point Scope are Locked Before Porting: WinForms confirmed as the
    target framework; both CLI (Main) and GUI (MainFrame) confirmed as in scope.
Modified sections:
  - Migration Constraints: Java(swift) entry updated to "resolved"; platform/packaging constraint
    updated with confirmed .NET 8 / single-file decision.
  - Open Questions: all five questions resolved and removed; section dropped.
Added sections: (none)
Removed sections: Open Questions (all resolved)
Follow-up TODOs: none — no placeholders deferred.
-->

# Coffee Shop Ordering System — Migration Constitution

## Core Principles

### I. Evidence-First Description

Every behaviour, rule, and constraint described in any specification MUST be traceable to a
verbatim substring of the legacy source (as recorded in `../../old/docs/`). A behaviour the
documents do not contain is absent from scope, regardless of what the migration goal implies it
should do. Symbols and identifiers MUST be reproduced verbatim as they appear in the source
(`CoffeeShopMenu`, `OrderPlacement`, `getOrderId`, `isPaymentComplete`, etc.); paraphrases or
renames are not acceptable as evidence anchors.

**Rationale**: The inventory was not execution-grounded (0 of 28 items). Static reading is the
only evidence available; treating it as the authority prevents scope drift and unverified
assumptions from entering specifications.

### II. Parity Testing is Mandatory

Every verified business rule carried from the Java estate into the C# port MUST have a
corresponding passing C# test in the parity test harness before the porting task that owns that
rule is declared complete. No domain component port is complete without its parity tests passing.
Tests MUST be written before or alongside implementation — never after.

**Rationale**: Because runtime behaviour of the Java application was not observed, the parity test
suite is the only objective gate between "copied the structure" and "reproduced the behaviour." A
port without tests cannot be distinguished from a port that silently changes a rule.

### III. Decide-Before-Drift (Known Defects)

Each known defect in the Java estate has an explicit operator-recorded decision: **all four
defects are preserved verbatim in the C# port**. The parity test for each defect MUST assert the
defective behaviour so the code generator cannot accidentally correct it.

Defects preserved verbatim (operator decision, 2026-11-17; sources: `../../old/docs/overview.md`,
`../../old/docs/approach.md`):

- `OrderPlacement.getOrderId` always returns the constant `100` regardless of the `orderId`
  supplied at construction. The C# port MUST reproduce this; the parity test MUST assert the
  return value is `100`.
- `PaymentOptions.processPayment` unconditionally sets `isPaymentComplete` to `true` with no
  validation of the payment method value. The C# port MUST reproduce this; the parity test MUST
  assert that any payment method value results in `isPaymentComplete == true`.
- `CustomerReview.addReview` (the setter pair) overwrites any previously stored `orderId` and
  `review` on the same instance without checking prior state. The C# port MUST reproduce this;
  the parity test MUST assert the overwrite behaviour.
- `OrderStatus.updateStatus` accepts any string with no validation. The C# port MUST reproduce
  this; the parity test MUST assert that arbitrary strings are accepted.

**Rationale**: A literal port reproduces defects; a corrective port changes behaviour. The
operator chose the literal path so the parity test suite pins the Java-identical behaviour. Future
correction is an explicit opt-in requiring a new operator decision and a spec amendment.

### IV. Infrastructure is Replaced, Not Ported

`mvnw` and `module-info` are Java-specific build and module infrastructure with no C# analogue.
Their verified rules describe Java bootstrapping concerns (JAVA_HOME resolution, wrapper jar
download, platform-specific paths, Maven base directory lookup, mavenrc loading, module
dependency declarations for `javafx.controls`, `javafx.fxml`, `java.desktop`). These rules MUST
NOT be carried into C# specifications as requirements. They are replaced wholesale by the confirmed
.NET toolchain.

**Confirmed replacement target** (operator decision, 2026-11-17): .NET 8 LTS, self-contained
single-file executable for Windows x64. The scaffolding specification (spec 002) MUST target this
exactly. No other .NET version or packaging format is in scope unless a subsequent operator
decision amends this constitution.

**Rationale**: Porting infrastructure rules produces dead or misleading C# code. The equivalent
C# story (project file, build invocation, packaging) is chosen fresh in spec 002.

### V. UI Framework and Entry-Point Scope are Locked Before Porting

**Confirmed decisions** (operator decisions, 2026-11-17):

1. **UI framework**: WinForms — the structural analogue to Swing on Windows. Widget mapping:
   JFrame → Form, JTabbedPane → TabControl, JComboBox → ComboBox, JRadioButton → RadioButton,
   JOptionPane → MessageBox / InputDialog.
2. **Entry-point scope**: both entry points are in scope — the CLI entry point (`Main`) and the
   GUI entry point (`MainFrame`) are both ported and both covered by parity tests.

No GUI or CLI porting task MUST begin until these decisions are recorded in the Migration
Decisions specification (spec 001). Both are now recorded; spec 001 MUST carry them verbatim.

Swing-specific affordances (tabbed 700×500 window, checkbox group with 1-based display indices,
radio-group pre-selected defaults, modal input dialog with cancel-returns-null semantics) MUST be
mapped to the corresponding WinForms widget vocabulary before any GUI porting task is accepted.

**Rationale**: The GUI port cannot be specified without knowing the target widget toolkit.
WinForms provides the most direct structural mapping to Swing's widget set, minimising translation
friction for a faithful port. Keeping both entry points avoids silent scope reduction; both have
verified rules in the Java estate.

### VI. Runtime-Observation Gap is Explicitly Recorded

Every specification that encodes a rule phrased as "always", "unconditionally", or "regardless"
MUST carry a note stating that this rule was derived from static reading and was not confirmed by
observing the running Java application. No specification MUST claim execution-grounded parity; the
harness is pinned to verified rules only.

**Rationale**: The inventory has 0% execution-grounded coverage. Rules that read as absolute on
static inspection may hide runtime behaviour (input exceptions, null paths, Swing threading
quirks). Honest labelling lets a future executor reconcile any divergence against a live Java
trace rather than silently accepting the static reading as final.

## Migration Constraints

The following constraints are derived directly from the frozen Discover artifacts and govern
every specification in this migration.

- The menu is fixed at exactly five items: `Cappuccino`, `Latte`, `Matcha Latte`, `Cold Brew`,
  `Hot Chocolate` (source: `CoffeeShopMenu`). Making the menu data-driven is out of scope unless
  the Migration Decisions specification records an explicit operator approval.
- Status values offered for manual GUI update are `"Preparing"` and `"Served"` only
  (source: `MainFrame`). The initial status at construction is `"Pending"` (source: `OrderStatus`).
- The GUI MUST enforce the guard: an order cannot be placed if no menu items are selected
  (FR-020). The GUI MUST enforce the guard: order status cannot be updated unless an order has
  already been placed (FR-021).
- Default values in the GUI are: timing `"Immediate"` (pre-selected radio button), payment
  `"Cash"` (combo box default), review `"Good"` (field default) with `"Very Good"` pre-selected
  as the radio button (sources: FR-023 through FR-027).
- The CLI maps numeric input to fixed option strings: timing 1→`Immediate`,
  2→`Bring after 5 minutes`, 3→`Keep bringing in a break of 30 minutes`, else→`Immediate`;
  payment 1→`UPI`, 2→`Cash`, 3→`Card`, 4→`Coupon`, else→`Cash`; review 1→`Very Good`,
  2→`Good`, 3→`Okish`, 4→`Bad`, 5→`Worst`, else→`Good` (source: `Main`).
- After CLI order placement, order status is progressed unconditionally through `Preparing` then
  `Served` (source: `Main`). Whether this progression survives in the C# CLI port is governed by
  Principle III (preserved verbatim per operator decision).
- The `Java(swift)` wording in the stated goal is confirmed as a spurious parenthetical: no Swift
  sources exist in the estate; the migration is a pure Java-to-C# port
  (operator decision, 2026-11-17; corroborated by `../../old/docs/approach.md`).
- The target platform is Windows. The confirmed C# deliverable is .NET 8 LTS, self-contained
  single-file executable for Windows x64 (operator decision, 2026-11-17; see Principle IV).

## Development Workflow

1. **Specification first**: every porting task MUST have an accepted specification before
   implementation begins. No code is written to infer missing specifications.
2. **Wave order**: specifications MUST be executed in the order defined in
   `../../old/docs/roadmap.md` — decisions lock-in (001), scaffolding (002), parity harness (003),
   Swing adapters (004), domain types (005+), entry points last — because later waves depend on
   earlier deliverables.
3. **Parity test gate**: a component port is not marked complete until its parity tests pass in
   CI.
4. **No push, merge, or deploy**: this workspace produces specifications, plans, and task lists.
   The referee and the platform's gates rule on what is accepted. Nothing is pushed, merged, or
   deployed from within this workspace.
5. **Write only within this workspace**: never write outside
   `/synthetix/new/coffee-shop-mod-synthetix/`. The legacy estate under `../../old/` and
   `../../evolve/` is read-only.

## Governance

This constitution supersedes any conflicting guidance in lower-precedence documents for this work
unit. Amendments require:

1. A written rationale explaining what changed and why.
2. A version bump following semantic versioning:
   - **MAJOR**: backward-incompatible removal or redefinition of a principle.
   - **MINOR**: new principle or section added, or materially expanded guidance.
   - **PATCH**: clarification, wording correction, or non-semantic refinement.
3. `LAST_AMENDED_DATE` updated to the amendment date.

All specifications MUST verify compliance with the principles above before acceptance. Complexity
beyond what the verified rules require MUST be justified explicitly. Use `../../old/docs/` as the
runtime reference for rule evidence; never cite memory or inference as a rule source.

**Version**: 1.1.0 | **Ratified**: 2026-11-17 | **Last Amended**: 2026-11-17
