# Feature Specification: Freeze Migration Decisions

**Feature Branch**: `refactor/rebuild`

**Created**: 2026-10-14

**Status**: Draft

**Input**: User description: "Freeze the Windows UI, source-phrase, JavaFX scope, and order-identifier migration decisions before any port; produce a written decision record only."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Apply One Migration Baseline (Priority: P1)

As an author of a later migration specification, I need one authoritative record of the target entry surfaces, graphical client technology, and identifier behavior so that I can specify a port without reopening foundational choices.

**Why this priority**: Every later project-shell, domain, and user-interface specification depends on a stable interpretation of these choices.

**Independent Test**: A reviewer can read only this specification and determine the required treatment of `Main`, `MainFrame`, `module-info`, `OrderPlacement.getOrderId()`, and the fixed identifier `1` without consulting an implementer.

**Acceptance Scenarios**:

1. **Given** a later specification for the graphical ordering flow, **When** its author consults this record, **Then** the author finds that the `MainFrame` equivalent is a .NET MAUI graphical client with Windows as a supported target.
2. **Given** a later specification for the application entry flows, **When** its author consults this record, **Then** the author finds that both the `Main` console flow and the `MainFrame` desktop flow are retained as distinct entry surfaces.
3. **Given** a later specification involving order identifiers, **When** its author consults this record, **Then** the author finds that both the fixed construction identifier `1` and the externally reported identifier `100` are preserved unless a separately approved behavior-change specification supersedes this record.

---

### User Story 2 - Audit Evidence and Judgment Separately (Priority: P2)

As a migration reviewer, I need each decision to distinguish frozen legacy evidence from migration judgment so that unsupported intent is never presented as a fact about the legacy estate.

**Why this priority**: The material verifies the identifier behaviors but does not measure why they exist, and the operator's phrase `Java(swift)` is ambiguous.

**Independent Test**: A reviewer can trace every legacy-behavior claim to `../../old/docs/`, identify the governing constraint behind each migration choice, and see an explicit statement wherever intent is unknown.

**Acceptance Scenarios**:

1. **Given** the `100` and `1` behaviors, **When** a reviewer checks their rationale, **Then** the record says that the behaviors are verified, their intent is unknown, and preservation follows the evidence-preserving migration policy rather than a claim that they are correct.
2. **Given** the phrase `Java(swift)`, **When** a reviewer checks its interpretation, **Then** the record identifies Java as the documented source language, Swing and console as the documented executable surfaces, and Swift as absent from the frozen evidence.
3. **Given** the JavaFX declarations in `module-info`, **When** a reviewer checks their treatment, **Then** the record distinguishes declared dependencies from executable business behavior and excludes an additional JavaFX user interface from this migration scope.

---

### User Story 3 - Keep the Decision Work Bounded (Priority: P3)

As the migration owner, I need this feature to stop at a written decision baseline so that no code, project scaffolding, component port, or acceptance execution is pulled forward from the roadmap.

**Why this priority**: A narrow decision artifact lets dependent specifications proceed in order without mixing policy with implementation.

**Independent Test**: An artifact review finds the specification and its quality checklist, but no application code, project skeleton, ported behavior, test implementation, or content belonging to roadmap specifications 002 through 011.

**Acceptance Scenarios**:

1. **Given** the completed feature artifacts, **When** their contents are reviewed, **Then** they contain decisions, evidence, consequences, assumptions, and acceptance criteria only.
2. **Given** an unresolved topic outside the four decision areas, **When** it is encountered, **Then** it remains assigned to its existing roadmap specification rather than being decided or implemented here.
3. **Given** a proposed deliverable owned by specifications 002 through 011, **When** it is encountered during this feature, **Then** this record may identify its owner and applicable `MDR-*` constraint but does not specify, design, create, port, test, or execute that deliverable.

### Edge Cases

- If an option in the migration analysis conflicts with the constitution, the constitution governs; therefore WinForms and WPF are not selectable alternatives to the mandated .NET MAUI graphical client.
- If later evidence reveals executable Swift or JavaFX behavior, that evidence requires an explicit scope change; it does not retroactively turn the currently absent behavior into part of this baseline.
- If a stakeholder later wants `OrderPlacement.getOrderId()` to return the stored identifier or wants generated order identifiers, the change requires its own documented legacy deviation and explicit acceptance criteria before implementation.
- The fixed construction identifier `1` and the externally reported identifier `100` can coexist even though they appear inconsistent. This feature preserves and traces both; it does not invent intent or reconcile them.
- The presence of JavaFX declarations in `module-info` alone does not establish a JavaFX user journey, screen, or behavior to port.
- `../../old/docs/edge_cases.md` reports that its edge-case search was unavailable. That is not evidence that the estate has no other edge cases, so this feature MUST NOT invent, resolve, or silently discard any unmeasured case.
- An edge case that changes one of MDR-001 through MDR-005 follows that decision's explicit scope-change or behavior-change path. Any other edge case remains with its roadmap owner: project or host setup with specification 002, rule capture with specification 003, component behavior with specifications 004 through 008, graphical-flow behavior with specification 009, console-flow behavior with specification 010, and executable cross-cutting validation with specification 011.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The feature MUST produce one written migration decision record and MUST NOT produce application code, project scaffolding, ported components, or executable tests.
- **FR-002**: The record MUST retain two distinct user entry surfaces: the console flow represented by `Main` and the desktop graphical flow represented by `MainFrame`.
- **FR-003**: The record MUST designate .NET MAUI as the graphical client technology, with Windows as a required supported target, in accordance with the project constitution.
- **FR-004**: The record MUST state that WinForms and WPF are not selected because the governing constitution already mandates .NET MAUI.
- **FR-005**: The record MUST interpret the documented migration source as Java and MUST state that `Java(swift)` does not establish a Swift component because no Swift behavior or component appears in the frozen material.
- **FR-006**: The record MUST place the documented Swing `MainFrame` flow and console `Main` flow in migration scope.
- **FR-007**: The record MUST treat `module-info` as evidence of declared JavaFX controls, JavaFX FXML, and Java Desktop dependencies, while stating that it contains no executable business behavior.
- **FR-008**: The record MUST exclude an additional JavaFX user-interface surface from the migration baseline because none is documented in the frozen behavior set.
- **FR-009**: The record MUST preserve the verified `OrderPlacement.getOrderId()` behavior whose verbatim rule evidence is `return 100;`.
- **FR-010**: The record MUST preserve the fixed order identifier `1` in both documented entry flows, traced to `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and `order = new OrderPlacement(1, chosenItems, timingPreference);`.
- **FR-011**: The record MUST state that the material does not measure whether the `100` and `1` behaviors are intended, defects, or temporary shortcuts.
- **FR-012**: The record MUST distinguish the evidence that the identifier behaviors exist from the policy decision to preserve them during an evidence-preserving migration.
- **FR-013**: The record MUST require later specifications that depend on these choices to cite the applicable decision identifiers defined in this specification.
- **FR-014**: The record MUST require any proposed change to a preserved identifier behavior to identify the documented legacy behavior being changed and provide explicit acceptance criteria in a separate behavior-change specification.
- **FR-015**: The feature MUST NOT decide or describe implementation work assigned to roadmap specifications 002 through 011, including the project skeleton, rule checklist, component ports, user-interface ports, or final acceptance execution.

### Migration Decision Record

| ID | Decision | Basis | Consequence for later specifications |
|---|---|---|---|
| **MDR-001** | Preserve `Main` as a distinct console entry surface and `MainFrame` as a distinct graphical entry surface; do not merge or drop either surface. The `MainFrame` equivalent MUST use .NET MAUI and MUST support Windows. | `../../old/docs/overview.md` separately describes the `Main` console flow and the Swing `MainFrame` flow. Constitution Principles I and II require preservation of both documented surfaces and mandate C#, .NET MAUI, and Windows support for the target graphical application. | Spec 002 MUST retain distinct console and graphical entry surfaces in the project shell. Spec 009 MUST retain the `MainFrame` graphical surface and apply .NET MAUI with Windows support. Spec 010 MUST retain the `Main` console surface. |
| **MDR-002** | Treat `Java(swift)` as ambiguous operator wording, not as evidence of Swift scope. Describe the frozen estate as Java with the documented console `Main` and Swing `MainFrame` surfaces. Do not claim that a Swift component exists or that “swift” was intended to mean Swing. | `../../old/docs/overview.md` identifies the estate language as `java` and documents `Main` and `MainFrame`. `../../old/docs/approach.md` records the operator phrase and reports that the supplied material shows Java and no Swift; it is migration-analysis context, not evidence of hidden behavior or operator intent. Constitution Principle I prohibits inference from the migration goal. | Later specifications MUST NOT claim or port a Swift component unless newly admitted evidence and an explicit scope change establish that scope. They MUST keep the original meaning of “swift” unresolved unless new evidence establishes it. |
| **MDR-003** | Treat `module-info` as dependency and scope evidence only, not as an executable entry surface. Do not define or port a separate JavaFX user-interface surface; the documented executable surfaces remain console `Main` and Swing `MainFrame`. | `../../old/docs/overview.md` states that `module-info` declares JavaFX controls, JavaFX FXML, and Java Desktop dependencies and “contains no executable business behavior.” Constitution Principle I prohibits inferring behavior from a dependency declaration. | Later behavior and UI specifications MUST cover the documented Swing `MainFrame` and console `Main` flows. The JavaFX declarations create no additional screen, journey, entry-surface, or behavior requirement unless newly admitted evidence and an explicit scope change establish one. |
| **MDR-004** | Preserve `OrderPlacement.getOrderId()` returning the externally reported identifier `100`, exactly as evidenced by `return 100;`. Intent is `Unknown`. Do not classify the behavior as a bug, an intended domain rule, or a temporary shortcut. | `../../old/docs/prd.md` FR-047 states that the externally reported identifier is always `100` regardless of the stored identifier and provides the verbatim rule evidence `return 100;`. `../../old/docs/roadmap.md` states that intent was not measured. Constitution Principle I supplies the preservation policy. | Spec 003 MUST include reported identifier `100` as baseline behavior with `Unknown` intent. Spec 005 MUST preserve `return 100;`. Spec 011 MUST validate reported identifier `100` and retain the `Unknown` intent classification. |
| **MDR-005** | Preserve fixed order identifier `1` in both documented entry flows, exactly as evidenced by `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and `order = new OrderPlacement(1, chosenItems, timingPreference);`. Intent is `Unknown`. Do not classify the behavior as a bug, an intended domain rule, or a temporary shortcut. | `../../old/docs/prd.md` FR-009 and FR-039 provide the two verbatim constructor expressions. `../../old/docs/roadmap.md` states that intent was not measured. Constitution Principle I supplies the preservation policy. | Spec 003 MUST include fixed identifier `1` in both entry flows with `Unknown` intent. Spec 009 MUST preserve the window-flow expression. Spec 010 MUST preserve the console-flow expression. Spec 011 MUST validate both fixed-identifier behaviors and retain the `Unknown` intent classification. |

### Applied Consequences and Preservation Conditions

- **MDR-001**: `Main` and `MainFrame` remain separate retained entry surfaces for specs 002, 009,
  and 010. A downstream omission, merge, rename without an explicit traceability mapping, or
  conflicting statement does not supersede this decision. Supersession requires a separate,
  explicitly approved scope-change specification that cites MDR-001, identifies the affected
  documented surface, supplies explicit testable acceptance criteria, and updates every affected
  downstream obligation. Replacing .NET MAUI or removing Windows support additionally requires an
  already-adopted constitutional amendment.
- **MDR-002**: Any later specification that discusses source language, `Java(swift)`, or possible
  Swift scope MUST cite MDR-002, describe Java as the documented source language, and keep the
  original meaning of “swift” unresolved. A Swift component or behavior may enter scope only
  through newly admitted evidence and an explicit scope change; the operator phrase alone is not
  evidence of that behavior.
- **MDR-003**: Any later specification that discusses graphical surfaces, JavaFX, `module-info`, or
  dependency scope MUST cite MDR-003 and keep dependency declarations separate from executable
  behavior. It MUST NOT derive an additional JavaFX user interface from `module-info`; newly
  admitted executable evidence and an explicit scope change are required to add such a surface.
- **MDR-004**: The frozen identifier is `OrderPlacement.getOrderId()` and its exact rule evidence is
  `return 100;` from `../../old/docs/prd.md` FR-047. Specs 003, 005, and 011 MUST preserve or validate
  that externally reported value and MUST keep `Intent: Unknown`. A replacement is valid only in a
  separate, explicitly approved behavior-change specification that cites MDR-004, identifies
  `return 100;` as the behavior being changed, supplies explicit testable acceptance criteria, and
  updates every affected downstream obligation.
- **MDR-005**: The exact console-flow evidence from `../../old/docs/prd.md` FR-009 is
  `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);`; the exact
  window-flow evidence from FR-039 is
  `order = new OrderPlacement(1, chosenItems, timingPreference);`. Specs 003, 009, 010, and 011 MUST
  preserve or validate the applicable fixed-identifier behavior and MUST keep `Intent: Unknown`.
  Replacing either expression's behavior requires a separate, explicitly approved behavior-change
  specification that cites MDR-005, identifies every affected verbatim rule substring, supplies
  explicit testable acceptance criteria, and updates every affected downstream obligation.

For MDR-004 and MDR-005, choosing a replacement behavior does not establish why the legacy behavior
existed. `Intent: Unknown` can change only when newly admitted evidence is reviewed through an
explicit scope change. If any required supersession condition is absent, the frozen decision and
all of its downstream obligations remain in force.

### Evidence Traceability

| Decision | Supported claim | Frozen source and locator | Verbatim identifier or rule evidence | Evidence role |
|---|---|---|---|---|
| MDR-001 | A console entry flow is documented. | `../../old/docs/overview.md`, `Main` component description | `Main` | Legacy evidence |
| MDR-001 | A distinct Swing graphical entry flow is documented. | `../../old/docs/overview.md`, `MainFrame` component description | `MainFrame` | Legacy evidence |
| MDR-002 | The supplied estate is identified as Java and documents the two executable surfaces. | `../../old/docs/overview.md`, language and component descriptions | `java`, `Main`, `MainFrame` | Legacy evidence |
| MDR-002 | The migration analysis records the operator phrase as ambiguous and reports that the supplied material shows Java and no Swift. | `../../old/docs/approach.md`, goal and feasibility analysis | `Java(swift)` | Migration-analysis context; not executable-behavior or operator-intent evidence |
| MDR-003 | The module descriptor declares JavaFX controls, JavaFX FXML, and Java Desktop dependencies and contains no executable business behavior. | `../../old/docs/overview.md`, `module-info` component description | `module-info`; “contains no executable business behavior” | Legacy evidence |
| MDR-004 | The externally reported order identifier is always `100`, regardless of the identifier stored at construction. | `../../old/docs/prd.md`, FR-047 | `OrderPlacement`, `getOrderId`, `return 100;` | Legacy evidence |
| MDR-004 | Historical intent for the identifier behavior was not measured. | `../../old/docs/roadmap.md`, specification 001 rationale | — | Migration-analysis context; not executable-behavior evidence |
| MDR-005 | The console flow constructs an order with identifier `1`. | `../../old/docs/prd.md`, FR-009 | `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` | Legacy evidence |
| MDR-005 | The window flow constructs an order with identifier `1`. | `../../old/docs/prd.md`, FR-039 | `order = new OrderPlacement(1, chosenItems, timingPreference);` | Legacy evidence |
| MDR-005 | Historical intent for the identifier behavior was not measured. | `../../old/docs/roadmap.md`, specification 001 rationale | — | Migration-analysis context; not executable-behavior evidence |

### Evidence Versus Migration Policy for MDR-004 and MDR-005

The frozen evidence establishes only the observable identifier behaviors: FR-047 contains
`return 100;`, while FR-009 and FR-039 contain the two constructor expressions using identifier
`1`. The roadmap supplies migration-analysis context that historical intent was not measured.
Neither source establishes that `100` or `1` is correct, defective, an intended domain rule, or a
temporary shortcut. Accordingly, both decisions retain `Intent: Unknown`.

Preserving those verified behaviors is a migration-policy judgment supplied by Constitution
Principle I, not a fact asserted by the legacy evidence. The policy requires documented behavior to
be reproduced unless an intentional change is separately specified, identifies the documented
legacy behavior it changes, and receives explicit acceptance criteria. Therefore MDR-004 and
MDR-005 freeze `100` and `1` for the migration baseline without claiming why the legacy system used
them; selecting a replacement behavior would not, by itself, resolve their historical intent.

### Scope Boundaries

**In scope**:

- The five written dispositions MDR-001 through MDR-005 covering graphical technology and entry-surface shape, interpretation of `Java(swift)`, JavaFX-versus-Swing scope, and preservation of fixed identifier `1` and externally reported identifier `100` with `Intent: Unknown`.
- Frozen-evidence citations, governing migration constraints, consequences, supersession conditions, and traceability instructions needed for later specifications to consume those five decisions.
- Routing an out-of-scope question to its existing roadmap owner without deciding, designing, implementing, testing, or accepting that owner's work.

**Out of scope**:

- Any source or test code, C# solution or project, framework setup, package or workload change, build or runtime command, generated output, user-interface design, component port, executable test, or acceptance result.
- Any implementation, correction, reconciliation, or replacement of the fixed identifier `1` or externally reported identifier `100` behaviors.
- Any inference of Swift or JavaFX behavior absent from the frozen documentation, and any resolution of an edge case that was not measured by that documentation.
- Any requirement, design, artifact, implementation, test, or execution result owned by roadmap specifications 002 through 011. This feature may state an applicable frozen constraint or citation obligation, but MUST NOT absorb the downstream work described below.

| Roadmap owner | Work prohibited in specification 001 and retained by that owner |
|---|---|
| Specification 002 | Create the C# solution and projects, configure the framework and Windows-capable hosts, add console and graphical build/run entry points, or create user-interface placeholders. |
| Specification 003 | Produce the rule-derived acceptance checklist or turn the frozen rules into executable tests. |
| Specification 004 | Port, design, or test `CoffeeShopMenu`. |
| Specification 005 | Port, design, or test `OrderPlacement`, including executable identifier behavior. |
| Specification 006 | Port, design, or test `OrderStatus`. |
| Specification 007 | Port, design, or test `PaymentOptions`. |
| Specification 008 | Port, design, or test `CustomerReview`. |
| Specification 009 | Design, port, or test the `MainFrame` graphical workflow or its .NET MAUI user interface. |
| Specification 010 | Design, port, or test the `Main` console workflow. |
| Specification 011 | Execute the acceptance checklist, produce pass/fail results, or perform cross-cutting acceptance against the ported application. |

Encountering any item in this table does not expand specification 001. The item remains deferred to
the named owner, subject to the applicable `MDR-*` decisions and the downstream citation contract.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: One decision record contains all five numbered decisions, with zero unresolved clarification markers and zero undecided alternatives.
- **SC-002**: 100% of legacy-behavior claims in the decision record identify a frozen source under `../../old/docs/` and retain verbatim identifiers or rule evidence where cited.
- **SC-003**: A downstream specification author can determine the selected graphical technology, supported entry surfaces, `Java(swift)` interpretation, JavaFX scope, and treatment of both identifier behaviors from this record with zero additional migration-decision questions.
- **SC-004**: A review of the feature artifacts finds zero application-code, project-scaffolding, port, or executable-test deliverables and zero requirements absorbed from roadmap specifications 002 through 011.
- **SC-005**: All acceptance scenarios can be verified by document inspection, and each later specification named in the decision table can trace its applicable choice to an `MDR-*` identifier.
- **SC-006**: Reviewers can identify the intent of the `1` and `100` behaviors as unknown in 100% of the places where this specification explains their preservation.

## Assumptions

- `../../old/docs/` remains the authoritative description of the legacy estate for this work unit.
- The current constitution is authoritative over the migration analysis when technology options conflict; therefore .NET MAUI supersedes the earlier WinForms-versus-WPF option set.
- No executable Swift component or JavaFX user-interface behavior exists within the frozen evidence supplied to this specification.
- Preservation of the `1` and `100` behaviors is a reversible migration baseline, not a finding about their original intent or product correctness.
- Later specifications will cite this record by `MDR-*` identifier and will not silently override it.
