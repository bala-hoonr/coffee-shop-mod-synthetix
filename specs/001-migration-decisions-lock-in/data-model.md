# Data Model: Migration Decisions Lock-in

This feature produces a documentation artifact, not executable code. The entities below describe
the logical structure of the decision record as written in `spec.md`.

---

## Entity: DecisionRecord

A frozen, evidence-backed statement of an operator choice that blocks one or more downstream
specifications.

| Field | Type | Description |
|---|---|---|
| `id` | integer | Sequential identifier (Decision 1 … Decision 5) |
| `question` | string | The unresolved question that was blocking downstream work |
| `decision` | string | The frozen answer (operator-approved, 2026-11-17) |
| `date` | date | Date the decision was recorded (2026-11-17 for all five) |
| `evidenceAnchors` | string[] | Verbatim substrings from `../../old/docs/` that support the decision |
| `impact` | string | Which downstream specifications are unblocked and how |

**Validation rules**:
- `evidenceAnchors` MUST NOT be empty; every decision requires at least one verbatim anchor.
- `decision` MUST be unambiguous — readable in isolation, without reference to any other document.
- `date` MUST match the constitution ratification date (2026-11-17) or a later amendment date.

**State transitions**: None. A DecisionRecord is frozen at creation. Amendment requires a new
operator decision, a constitution version bump, and a spec amendment (Constitution Governance).

**Instances** (the five decisions in `spec.md`):

| id | question (summary) |
|---|---|
| 1 | What does 'Java(swift)' mean? |
| 2 | Which C# UI framework replaces Swing? |
| 3 | Do both CLI and GUI entry points survive? |
| 4 | Are the four known Java defects preserved or corrected? |
| 5 | What .NET version and packaging format is required? |

---

## Entity: KnownDefect

A behaviour in the Java estate that is demonstrably incorrect, recorded verbatim in the inventory,
with an explicit disposition decision and a required parity test assertion.

| Field | Type | Description |
|---|---|---|
| `javaIdentifier` | string | Verbatim class and method name from the Java estate |
| `defectiveBehaviour` | string | Static-read description of the incorrect behaviour |
| `disposition` | enum `{preserve, correct}` | Operator choice for the C# port |
| `parityTestAssertion` | string | Exact assertion the parity test MUST make |
| `evidenceAnchor` | string | Verbatim substring from `../../old/docs/overview.md` |

**Validation rules**:
- `disposition` MUST be explicitly recorded; "unknown" is not a valid state.
- `parityTestAssertion` MUST be specific enough to write as an executable C# test without
  additional interpretation.
- `evidenceAnchor` MUST be a verbatim substring (Constitution Principle I).

**Instances** (all four defects, all with `disposition = preserve`):

| javaIdentifier | defectiveBehaviour | parityTestAssertion |
|---|---|---|
| `OrderPlacement.getOrderId` | Always returns `100` regardless of `orderId` supplied at construction | Assert return value == `100` for any constructor input |
| `PaymentOptions.processPayment` | Sets `isPaymentComplete` to `true` with no validation of the payment method value | Assert `isPaymentComplete == true` for any method string including invalid/empty values |
| `CustomerReview.addReview` | Overwrites `orderId` and `review` without checking prior state | Assert that a second call overwrites the values written by the first call |
| `OrderStatus.updateStatus` | Accepts any string with no validation | Assert that arbitrary strings (empty, null-like, out-of-domain) are accepted without error |

---

## Entity: WidgetMapping

A one-to-one mapping from a Swing widget type to its WinForms analogue, covering every widget
present in `MainFrame`.

| Field | Type | Description |
|---|---|---|
| `swingWidget` | string | Verbatim Swing class name |
| `winFormsAnalogue` | string | Confirmed WinForms class or static method name |

**Validation rule**: The table MUST cover every Swing widget type present in `MainFrame` (SC-004).
No widget may be left unmapped.

**Instances**:

| swingWidget | winFormsAnalogue |
|---|---|
| `JFrame` | `Form` |
| `JTabbedPane` | `TabControl` |
| `JComboBox` | `ComboBox` |
| `JRadioButton` | `RadioButton` |
| `JOptionPane` | `MessageBox` / `InputDialog` |

---

## Relationships

```
DecisionRecord(2) ──contains──► WidgetMapping (5 entries)
DecisionRecord(4) ──contains──► KnownDefect (4 entries)
```

Decision 2 (UI framework) owns the widget mapping table. Decision 4 (defect dispositions) owns
the four KnownDefect entries. The other three decisions (1, 3, 5) have no sub-entities.
