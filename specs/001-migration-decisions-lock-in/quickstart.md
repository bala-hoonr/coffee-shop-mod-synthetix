# Quickstart Validation Guide: Migration Decisions Lock-in

This guide describes how to validate that `spec.md` meets its acceptance criteria. The deliverable
is a document; validation is performed by a reviewer reading the document and checking each scenario
below. No build, install, or runtime execution step is required.

---

## Prerequisites

- Access to `specs/001-migration-decisions-lock-in/spec.md` (the document under review).
- No other source may be consulted for the validation checks below — each scenario is designed to
  be answerable from `spec.md` alone.

---

## Validation Scenarios

### SC-001 — All five open questions are answered

Open `spec.md` and read the **Decision Record** section. Confirm that it contains exactly five
numbered decisions:

1. Decision 1 — Java(swift) wording
2. Decision 2 — C# UI framework
3. Decision 3 — Entry-point scope
4. Decision 4 — Known defect dispositions
5. Decision 5 — Target .NET version and packaging

**Expected**: All five are present, each with a **Question**, **Decision**, **Date**, **Evidence**,
and **Impact** row. No decision is left as "TBD" or unresolved.

---

### SC-002 — Decisions are self-contained for downstream spec authors

For each of the five decisions, confirm that the **Decision** cell contains a complete,
unambiguous answer (not a reference to another document or a conditional statement).

**Check list**:
- Decision 1: States "No Swift sources exist" and "pure Java-to-C# port".
- Decision 2: States "WinForms" and includes the five-row widget mapping table.
- Decision 3: States "both entry points are in scope" naming `Main` and `MainFrame`.
- Decision 4: Contains the four-row defect table with `preserve` disposition for each row.
- Decision 5: States ".NET 8 LTS, self-contained single-file executable for Windows x64".

**Expected**: A reviewer can state the answer to each question after reading only `spec.md`.

---

### SC-003 — Parity test assertions are specific enough to be written as C# tests

Read the **Decision 4** table in `spec.md`. For each of the four defects, confirm the
**Parity test assertion** column contains a concrete, executable assertion:

| Row | Required assertion text |
|---|---|
| `OrderPlacement.getOrderId` | "Assert return value == `100` for any constructor input" |
| `PaymentOptions.processPayment` | "Assert `isPaymentComplete == true` for any method string including invalid/empty values" |
| `CustomerReview.addReview` | "Assert that a second call overwrites the values written by the first call" |
| `OrderStatus.updateStatus` | "Assert that arbitrary strings (empty, null-like, out-of-domain) are accepted without error" |

**Expected**: Each assertion is present and specific. No row says "TBD" or requires additional
interpretation.

---

### SC-004 — Widget mapping table covers all five Swing widgets

Read the **Decision 2** widget mapping table in `spec.md`. Confirm it contains exactly these five
rows and no widget is unmapped:

| Swing widget | Expected WinForms analogue |
|---|---|
| `JFrame` | `Form` |
| `JTabbedPane` | `TabControl` |
| `JComboBox` | `ComboBox` |
| `JRadioButton` | `RadioButton` |
| `JOptionPane` | `MessageBox` / `InputDialog` |

**Expected**: All five rows present, all five WinForms analogues named.

---

### SC-005 — Document is consistent with the Migration Constitution v1.1.0

Read the opening **Runtime-observation gap notice** in `spec.md`. Confirm it states:
- All rules derived from static reading.
- 0 of 28 inventory items are execution-grounded.
- Rules phrased as "always", "unconditionally", or "regardless" rest on static reading only.

Then verify that no decision in the Decision Record contradicts a principle in
`.specify/memory/constitution.md` v1.1.0.

**Expected**: No conflict between `spec.md` and the constitution. The gap notice is present and
accurate.

---

## Done When

- [ ] All five decisions are present and unambiguous (SC-001, SC-002)
- [ ] All four parity test assertions are specific and executable (SC-003)
- [ ] Widget mapping table covers all five Swing widget types (SC-004)
- [ ] Runtime-observation gap notice is present; no conflict with the constitution (SC-005)
