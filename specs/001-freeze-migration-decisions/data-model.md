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

## Relationships

- One `MigrationDecisionRecord` contains exactly five `MigrationDecision` entities.
- Each `MigrationDecision` has at least one evidence or governing-basis reference.
- Each legacy-behavior claim has at least one `EvidenceReference` to `../../old/docs/`.
- Each migration judgment has at least one `GoverningConstraint`.
- MDR-004 and MDR-005 each have exactly one `AmbiguityRecord`.
- One `MigrationDecision` may create multiple `DownstreamObligation` entities.
- Every `DownstreamObligation.decision_id` resolves to a decision in the same record.

## Validation Rules

1. Decision IDs are unique and complete from MDR-001 through MDR-005.
2. `Main` and `MainFrame` remain distinct entry surfaces.
3. MDR-001 selects .NET MAUI with Windows support; WinForms and WPF remain unselected.
4. MDR-002 does not infer a Swift component or claim what “swift” originally meant.
5. MDR-003 does not infer executable JavaFX behavior from `module-info`.
6. MDR-004 preserves the exact behavior evidenced by `return 100;`.
7. MDR-005 preserves both constructor expressions containing identifier `1`.
8. MDR-004 and MDR-005 classify intent as `Unknown`, never as intended behavior or a defect.
9. A downstream override names the affected legacy behavior and has its own explicit acceptance criteria.
10. No entity represents application state, runtime persistence, C# project structure, a ported component, or executable test code.

## State Transitions

There are no application state transitions in this feature. The only governance transition is:

```text
Frozen baseline ──separately approved specification──> Superseded baseline
```

Supersession requires citation of the affected `MDR-*` decision, identification of the documented
legacy behavior being changed, and explicit acceptance criteria. `Intent: Unknown` cannot change by
inference; newly supplied evidence requires explicit scope review.
