# Research: Migration Decisions Lock-in

## Overview

This document resolves all five open questions identified in `../../old/docs/approach.md` by
reading the frozen legacy estate recorded in `../../old/docs/`. No runtime execution was performed;
all findings rest on static reading of the source files (Constitution Principle VI).

---

## Question 1 — What does 'Java(swift)' mean in the stated goal?

**Decision**: Spurious parenthetical. No Swift sources exist in the estate.

**Rationale**: `../../old/docs/overview.md` lists eight Java source files and one shell script
(`mvnw`). No `.swift` file appears in the inventory. `../../old/docs/approach.md` states
explicitly: "No Swift sources were seen in the estate." The reachable goal is a straight
Java-to-C# port.

**Alternatives considered**: (1) Swift as a secondary source base not provided — refuted by
the estate inventory; (2) 'Swift' as shorthand for SwiftUI on macOS — refuted by the stated
Windows target.

**Impact on downstream specs**: All 11 downstream specifications scope to Java-to-C# only.

---

## Question 2 — Which C# UI framework replaces Swing on Windows?

**Decision**: WinForms

**Rationale**: `MainFrame` uses five Swing widget types: `JFrame` (top-level window),
`JTabbedPane` (tabbed container), `JComboBox` (payment dropdown), `JRadioButton` (timing and
review radio buttons), `JOptionPane` (status update dialog). WinForms provides a named, structural
analogue for each. Source: `../../old/docs/overview.md` — "MainFrame is the Swing GUI entry point,
presenting a 700×500 tabbed window with four tabs."

**Widget mapping** (Swing → WinForms):

| Swing | WinForms |
|---|---|
| `JFrame` | `Form` |
| `JTabbedPane` | `TabControl` |
| `JComboBox` | `ComboBox` |
| `JRadioButton` | `RadioButton` |
| `JOptionPane` | `MessageBox` / `InputDialog` |

**Alternatives considered**: WPF — provides a richer binding model but is architecturally
further from Swing's imperative widget tree, increasing translation friction for a faithful port
(Constitution Principle V rationale). WinForms minimises that friction.

---

## Question 3 — Do both entry points (Main, MainFrame) survive?

**Decision**: Both entry points are in scope.

**Rationale**: Both carry verified rules in the inventory. `Main` has 8 verified rules (CLI flow,
input mapping, out-of-range defaults, Preparing→Served progression). `MainFrame` has 10 verified
rules (guards, defaults, widget behaviour). Dropping either would remove verified rules without an
explicit operator decision. Source: `../../old/docs/overview.md` — "Main is the CLI entry point";
"MainFrame is the Swing GUI entry point."

**Alternatives considered**: Drop CLI — no operator decision authorises this removal;
Drop GUI — same constraint.

---

## Question 4 — Are the four known Java defects preserved or corrected?

**Decision**: All four defects are **preserved verbatim** in the C# port.

**Rationale**: The operator chose the literal path (operator decision, 2026-11-17; Constitution
Principle III). A corrective port changes behaviour; that is an explicit opt-in requiring a new
operator decision and a spec amendment. Parity tests MUST assert the defective behaviour so the
code generator cannot accidentally correct it.

| Defect | Java identifier | Defective behaviour | Evidence |
|---|---|---|---|
| Constant order ID | `OrderPlacement.getOrderId` | Always returns `100` | "getOrderId always returns the hardcoded value 100 regardless of the orderId field supplied at construction" (`overview.md`) |
| Unconditional payment | `PaymentOptions.processPayment` | Sets `isPaymentComplete` to `true` with no validation | "No validation of the payment method value is performed" (`overview.md`) |
| Silent review overwrite | `CustomerReview.addReview` | Overwrites `orderId` and `review` without checking prior state | "No persistence or validation logic is present" (`overview.md`) |
| Unconstrained status | `OrderStatus.updateStatus` | Accepts any string | "can be updated to any string value via updateStatus" (`overview.md`) |

**Alternatives considered**: Correct defects during port — rejected; operator chose verbatim
preservation. Partial correction — rejected; no operator decision identifies which defects to
correct individually.

---

## Question 5 — What .NET version and packaging format is required?

**Decision**: .NET 8 LTS, self-contained single-file executable for Windows x64.

**Rationale**: Constitution Principle IV states this explicitly as a confirmed operator decision
(2026-11-17). `mvnw` and `module-info` are Java-specific build infrastructure with no C# analogue;
they are replaced wholesale by the .NET toolchain. No other .NET version or packaging format is in
scope without an amendment.

**Alternatives considered**: .NET 6 LTS — superseded by .NET 8 as the current LTS.
Framework-dependent executable — requires .NET runtime pre-installed; self-contained avoids that
dependency on a fresh Windows machine. MSI installer — out of scope without an explicit operator
decision.

---

## Runtime-Observation Gap

All findings above rest on static reading of `../../old/docs/`. The Java application was not
executed; 0 of 28 inventory items are execution-grounded. Rules phrased as "always",
"unconditionally", or "regardless" reflect the static reading only. Future work that executes the
Java application MUST reconcile any divergence before the port is declared complete (Constitution
Principle VI).
