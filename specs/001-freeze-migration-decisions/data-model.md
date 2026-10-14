# Documentation Data Model: Migration Decision Record

This is a model of the written governance artifact. It is not a coffee-shop application model,
database schema, C# type design, or persistence design.

## Entities

### MigrationDecisionRecord

| Field | Type | Rules |
|---|---|---|
| `feature` | String | Exactly `001-freeze-migration-decisions` |
| `authority` | Reference set | Includes `spec.md`, `.specify/memory/constitution.md`, and frozen evidence under `../../old/docs/` |
| `decisions` | MigrationDecision list | Exactly five, with IDs MDR-001 through MDR-005 |
| `in_scope` | Statement set | Only the four decision areas and their traceability obligations |
| `out_of_scope` | Statement set | All application code and roadmap specifications 002–011 implementation work |

### MigrationDecision

| Field | Type | Rules |
|---|---|---|
| `decision_id` | Identifier | Unique; one of MDR-001 through MDR-005 |
| `subject` | String | UI/entry shape, source interpretation, dependency scope, or preserved identifier behavior |
| `decision_statement` | String | One frozen, unambiguous disposition |
| `decision_type` | Enum | `TargetShape`, `SourceInterpretation`, `DependencyScope`, or `PreservedBehavior` |
| `legacy_evidence` | EvidenceReference list | Required for every legacy-behavior claim |
| `governing_constraints` | GoverningConstraint list | Required for migration judgments not established by legacy behavior |
| `downstream_obligations` | DownstreamObligation list | Records consuming specification or an applicability condition |
| `intent_classification` | Enum | `NotApplicable` or `Unknown`; must be `Unknown` for MDR-004 and MDR-005 |
| `supersession_condition` | String | Separate approved scope/behavior-change specification with explicit acceptance criteria |

### EvidenceReference

| Field | Type | Rules |
|---|---|---|
| `source_path` | Project-relative path | Legacy evidence must be under `../../old/docs/` |
| `locator` | String | Heading or requirement ID, such as FR-047 |
| `supported_claim` | String | Must not exceed what the source states |
| `verbatim_evidence` | String | Exact identifier or rule substring when cited |
| `role` | Enum | `LegacyEvidence` or `MigrationAnalysisContext` |

### GoverningConstraint

| Field | Type | Rules |
|---|---|---|
| `source` | Reference | Constitution principle or explicit feature requirement |
| `constraint` | String | The rule that governs the migration judgment |
| `governs` | Decision reference | One or more MDR identifiers |

### DownstreamObligation

| Field | Type | Rules |
|---|---|---|
| `consumer` | String | Named downstream specification or an applicability condition |
| `decision_id` | Decision reference | Exact applicable MDR identifier |
| `required_treatment` | String | How the consumer preserves or applies the baseline |
| `deviation_reference` | Optional reference | `None` or a separately approved behavior-change specification |

### AmbiguityRecord

| Field | Type | Rules |
|---|---|---|
| `subject` | Decision reference | MDR-004 or MDR-005 |
| `verified_fact` | String | The exact behavior shown by frozen evidence |
| `intent` | Enum | Exactly `Unknown` |
| `prohibited_inference` | String | Must prohibit classification as intended rule or defect |
| `resolution_path` | String | New evidence plus explicit scope change, or an approved behavior-change specification |

## Required Decision Instances

The record cardinality is closed, not extensible: `decisions` contains exactly the following five
rows. Each ID occurs once, no ID outside this set is valid, and omission, duplication, or addition
invalidates the record.

| Decision ID | Subject | Decision type | Intent classification |
|---|---|---|---|
| MDR-001 | Retained `Main` and `MainFrame` entry surfaces and the target graphical technology | `TargetShape` | `NotApplicable` |
| MDR-002 | Interpretation of the operator wording `Java(swift)` | `SourceInterpretation` | `NotApplicable` |
| MDR-003 | Scope meaning of the `module-info` declarations | `DependencyScope` | `NotApplicable` |
| MDR-004 | Externally reported identifier from `OrderPlacement.getOrderId()` | `PreservedBehavior` | `Unknown` |
| MDR-005 | Fixed construction identifier `1` in both documented entry flows | `PreservedBehavior` | `Unknown` |

## Evidence-Reference Rules

1. Every statement presented as legacy behavior has at least one `EvidenceReference` whose
   `source_path` is under `../../old/docs/`, whose `locator` identifies the relevant heading or
   requirement, and whose `supported_claim` says no more than that source states.
2. A cited legacy symbol or rule substring is copied exactly into `verbatim_evidence`; normalization,
   inferred renaming, and silent repair are invalid. A reference that does not quote a symbol or
   rule may leave `verbatim_evidence` empty only when its `supported_claim` is still directly stated
   by the source.
3. `LegacyEvidence` supports a fact about the estate. `MigrationAnalysisContext` may describe an
   earlier analysis, an unmeasured question, or roadmap ownership, but cannot establish executable
   behavior or historical intent.
4. A constitution principle or explicit feature requirement is represented as a
   `GoverningConstraint`, never as legacy evidence. Conversely, a target migration judgment cannot
   be attributed to frozen legacy evidence unless that evidence actually states it.
5. Evidence references are attached to the decision whose claim they support; a path-only citation
   without a locator and supported claim is invalid.

The minimum evidence links required by the five instances are:

| Decision ID | Source and locator | Supported claim | Required verbatim evidence | Role |
|---|---|---|---|---|
| MDR-001 | `../../old/docs/overview.md`, `Main` component description | A console entry flow is documented. | `Main` | `LegacyEvidence` |
| MDR-001 | `../../old/docs/overview.md`, `MainFrame` component description | A distinct Swing graphical entry flow is documented. | `MainFrame` | `LegacyEvidence` |
| MDR-002 | `../../old/docs/overview.md`, system/component descriptions | The supplied estate is Java and documents `Main` and `MainFrame`. | `java`, `Main`, `MainFrame` | `LegacyEvidence` |
| MDR-002 | `../../old/docs/approach.md`, source-language analysis | The supplied material reports Java and no Swift component. | `Java(swift)` | `MigrationAnalysisContext` |
| MDR-003 | `../../old/docs/overview.md`, `module-info` component description | JavaFX controls, JavaFX FXML, and Java Desktop are declared dependencies, with no executable business behavior. | `module-info` | `LegacyEvidence` |
| MDR-004 | `../../old/docs/prd.md`, FR-047 | The externally reported order identifier is always `100`. | `return 100;` | `LegacyEvidence` |
| MDR-004 | `../../old/docs/roadmap.md`, specification 001 rationale | Historical intent for the identifier behavior was not measured. | — | `MigrationAnalysisContext` |
| MDR-005 | `../../old/docs/prd.md`, FR-009 | The console flow constructs an order with identifier `1`. | `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` | `LegacyEvidence` |
| MDR-005 | `../../old/docs/prd.md`, FR-039 | The window flow constructs an order with identifier `1`. | `order = new OrderPlacement(1, chosenItems, timingPreference);` | `LegacyEvidence` |
| MDR-005 | `../../old/docs/roadmap.md`, specification 001 rationale | Historical intent for the identifier behavior was not measured. | — | `MigrationAnalysisContext` |

## Required Downstream-Obligation Links

Each row is a `DownstreamObligation` whose `decision_id` resolves to the required decision instance.
The named links are mandatory; conditional links are created whenever their applicability condition
is met.

| Consumer or applicability condition | Decision ID | Required treatment |
|---|---|---|
| Specification 002 · C# project skeleton | MDR-001 | Retain the distinct console and graphical entry surfaces and apply the selected target shape. |
| Specification 003 · acceptance checklist from rules | MDR-004 | Include the externally reported identifier `100` as baseline behavior and keep its intent `Unknown`. |
| Specification 003 · acceptance checklist from rules | MDR-005 | Include fixed construction identifier `1` in both entry flows and keep its intent `Unknown`. |
| Specification 005 · port `OrderPlacement` | MDR-004 | Preserve the behavior evidenced by `return 100;`. |
| Specification 009 · port `MainFrame` desktop UI | MDR-001 | Retain `MainFrame` as the distinct graphical entry surface and apply the selected graphical technology. |
| Specification 009 · port `MainFrame` desktop UI | MDR-005 | Preserve `order = new OrderPlacement(1, chosenItems, timingPreference);`. |
| Specification 010 · port `Main` console flow | MDR-001 | Retain `Main` as the distinct console entry surface. |
| Specification 010 · port `Main` console flow | MDR-005 | Preserve `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);`. |
| Specification 011 · acceptance against frozen rules | MDR-004 | Validate reported identifier `100` and retain the `Unknown` intent classification. |
| Specification 011 · acceptance against frozen rules | MDR-005 | Validate fixed identifier `1` in both flows and retain the `Unknown` intent classification. |
| Any specification discussing source language, `Java(swift)`, or possible Swift scope | MDR-002 | Treat the wording as ambiguous and do not infer Swift behavior without newly admitted evidence and an explicit scope change. |
| Any specification discussing graphical surfaces, JavaFX, `module-info`, or dependency scope | MDR-003 | Treat `module-info` as dependency evidence and do not infer an additional executable JavaFX surface. |

## Required Ambiguity Records

Exactly these two `AmbiguityRecord` instances exist:

| Subject | Verified fact | Intent | Prohibited inference | Resolution path |
|---|---|---|---|---|
| MDR-004 | `OrderPlacement.getOrderId()` has the verified rule evidence `return 100;`. | `Unknown` | Do not classify `100` as an intended domain rule, defect, or temporary shortcut. | Newly admitted evidence plus explicit scope review may establish historical intent; changing the behavior instead requires a separately approved behavior-change specification. |
| MDR-005 | The two documented flows use `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and `order = new OrderPlacement(1, chosenItems, timingPreference);`. | `Unknown` | Do not classify fixed identifier `1` as an intended domain rule, defect, or temporary shortcut. | Newly admitted evidence plus explicit scope review may establish historical intent; changing either behavior instead requires a separately approved behavior-change specification. |

## Relationships

- One `MigrationDecisionRecord` contains exactly five `MigrationDecision` entities.
- Each `MigrationDecision` has at least one evidence or governing-basis reference.
- Each legacy-behavior claim has at least one `EvidenceReference` to `../../old/docs/`.
- Each migration judgment has at least one `GoverningConstraint`.
- MDR-004 and MDR-005 each have exactly one `AmbiguityRecord`.
- One `MigrationDecision` may create multiple `DownstreamObligation` entities.
- Every `DownstreamObligation.decision_id` resolves to a decision in the same record.
- Every mandatory consumer/decision pair in the required downstream-obligation table exists exactly
  once; applicable conditional pairs exist at least once and do not replace mandatory pairs.
- An `AmbiguityRecord` does not change verified behavior; it records the separation between the
  verified fact and unknown historical intent.

## Validation Rules

1. Decision IDs are unique and complete from MDR-001 through MDR-005.
2. `Main` and `MainFrame` remain distinct entry surfaces.
3. MDR-001 selects .NET MAUI with Windows support; WinForms and WPF remain unselected.
4. MDR-002 does not infer a Swift component or claim what “swift” originally meant.
5. MDR-003 does not infer executable JavaFX behavior from `module-info`.
6. MDR-004 preserves the exact behavior evidenced by `return 100;`.
7. MDR-005 preserves both constructor expressions containing identifier `1`.
8. MDR-004 and MDR-005 classify intent as `Unknown`, never as intended behavior or a defect.
9. A downstream override passes every supersession check defined below; otherwise the frozen
   decision remains authoritative.
10. No entity represents application state, runtime persistence, C# project structure, a ported component, or executable test code.

## Supersession Validation

A proposed supersession is valid only when all of these checks pass:

1. The proposal is a separate, explicitly approved scope or behavior-change specification; an edit,
   paraphrase, omission, or conflicting downstream statement is not a supersession.
2. Its `deviation_reference` is not `None`, resolves to that approved specification, and cites the
   exact affected `MDR-*` identifier in this record.
3. It identifies the documented legacy behavior being changed, including every affected verbatim
   rule substring when MDR-004 or MDR-005 is involved.
4. It supplies explicit, testable acceptance criteria for the replacement behavior and updates each
   affected downstream obligation rather than silently dropping a consumer link.
5. It does not change `Unknown` historical intent by inference. Reclassification of intent requires
   newly admitted evidence and explicit scope review; choosing a replacement behavior alone does not
   establish why the legacy behavior existed.
6. If the proposal conflicts with a constitutional mandate, the applicable constitution amendment
   must already be adopted; a behavior-change specification cannot supersede the constitution.

Failure of any check leaves the frozen decision and all linked downstream obligations in force.

## State Transitions

There are no application state transitions in this feature. The only governance transition is:

```text
Frozen baseline ──separately approved specification──> Superseded baseline
```

The transition occurs only after all supersession validation checks pass. `Intent: Unknown` cannot
change by inference; newly supplied evidence requires explicit scope review.
