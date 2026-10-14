---

description: "Dependency-ordered tasks for the written migration decision baseline"
---

# Tasks: Freeze Migration Decisions

**Input**: Design documents from `/specs/001-freeze-migration-decisions/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/downstream-specification-contract.md`, `quickstart.md`

**Tests**: This feature permits document inspection only. Validation tasks use the assertions in `quickstart.md`; no application code, project scaffolding, executable test project, build, or runtime test is created.

**Organization**: Tasks are grouped by user story so each documentation outcome can be completed and inspected independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel after its stated prerequisite because it changes a different file
- **[Story]**: Maps the task to a user story in `spec.md`
- Every task names the exact file or directory it reads, changes, or validates

## Phase 1: Setup (Documentation Boundary)

**Purpose**: Establish the documentation-only work area and authoritative inputs before editing the decision baseline.

- [x] T001 Confirm the feature artifact inventory, documentation-only structure, and deferred roadmap ownership in specs/001-freeze-migration-decisions/plan.md against ../../old/docs/README.md and ../../old/docs/roadmap.md

---

## Phase 2: Foundational (Decision and Traceability Model)

**Purpose**: Normalize the five decisions and the rules every user-story section must follow.

**⚠️ CRITICAL**: Complete this phase before editing the user-story deliverables so decision IDs, evidence roles, ambiguity, and supersession rules remain consistent.

- [x] T002 Consolidate the five frozen dispositions, rejected alternatives, legacy-evidence bases, governing constraints, and validation approach in specs/001-freeze-migration-decisions/research.md using only ../../old/docs/ and .specify/memory/constitution.md as applicable authorities
- [x] T003 Define the exactly-five-decision cardinality, evidence-reference rules, downstream-obligation links, `Unknown` ambiguity records for MDR-004 and MDR-005, and supersession validation in specs/001-freeze-migration-decisions/data-model.md

**Checkpoint**: The documentation model can represent every required decision without introducing application state, C# types, persistence, or executable tests.

---

## Phase 3: User Story 1 - Apply One Migration Baseline (Priority: P1) 🎯 MVP

**Goal**: Give later specification authors one authoritative baseline for the retained entry surfaces, .NET MAUI Windows graphical technology, and the fixed `1` and reported `100` identifier behaviors.

**Independent Test**: Read only `spec.md` and determine the required treatment of `Main`, `MainFrame`, `module-info`, `OrderPlacement.getOrderId()`, fixed identifier `1`, and the conditions for superseding preserved behavior without asking an implementer.

### Implementation for User Story 1

- [x] T004 [US1] Finalize MDR-001, MDR-004, and MDR-005 plus their consequences, exact identifier evidence, and preservation conditions in specs/001-freeze-migration-decisions/spec.md
- [x] T005 [P] [US1] Define the mandatory MDR citations and applied consequences for specifications 002, 003, 005, 009, 010, and 011 in specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md after T004
- [x] T006 [P] [US1] Add document-inspection assertions for exactly five MDR rows, .NET MAUI Windows selection, distinct entry surfaces, and the three exact identifier rule substrings in specs/001-freeze-migration-decisions/quickstart.md after T004

**Checkpoint**: User Story 1 is complete when a downstream author can apply the baseline and all US1 inspection assertions pass.

---

## Phase 4: User Story 2 - Audit Evidence and Judgment Separately (Priority: P2)

**Goal**: Make every legacy claim auditable while keeping documented facts, migration judgments, and unknown historical intent visibly separate.

**Independent Test**: Trace each legacy-behavior claim in `spec.md` to `../../old/docs/`, identify the governing basis for each migration choice, and confirm that neither `Java(swift)` nor JavaFX declarations nor the identifier behaviors receive unsupported intent.

### Implementation for User Story 2

- [x] T007 [US2] Finalize MDR-002 and MDR-003, the evidence-traceability table, and the evidence-versus-policy explanation for MDR-004 and MDR-005 in specs/001-freeze-migration-decisions/spec.md
- [x] T008 [P] [US2] Add conditional MDR-002 and MDR-003 citation rules plus conformance requirements that preserve `Unknown` identifier intent in specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md after T007
- [ ] T009 [P] [US2] Add document-inspection assertions for ambiguous `Java(swift)` wording, absent Swift behavior, dependency-only `module-info`, excluded JavaFX UI behavior, and unknown `1`/`100` intent in specs/001-freeze-migration-decisions/quickstart.md after T007

**Checkpoint**: User Story 2 is complete when every factual claim and migration judgment can be audited independently and all US2 inspection assertions pass.

---

## Phase 5: User Story 3 - Keep the Decision Work Bounded (Priority: P3)

**Goal**: Stop this feature at a written decision baseline and leave all project creation, ports, UI design, executable testing, and acceptance execution with roadmap specifications 002 through 011.

**Independent Test**: Inspect the feature directory and confirm it contains only Markdown decision, design, contract, checklist, and task artifacts, with no source, project, test, build-output, or unrelated roadmap deliverable.

### Implementation for User Story 3

- [ ] T010 [US3] Finalize the in-scope and out-of-scope boundaries, edge-case routing, and prohibition on work owned by specifications 002 through 011 in specs/001-freeze-migration-decisions/spec.md
- [ ] T011 [P] [US3] Add rejection conditions for silent MDR overrides, merged or dropped entry surfaces, inferred Swift or JavaFX behavior, and undocumented identifier changes in specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md after T010
- [ ] T012 [P] [US3] Add filesystem inspection assertions that reject non-Markdown files and source, test, bin, or obj directories under specs/001-freeze-migration-decisions/ in specs/001-freeze-migration-decisions/quickstart.md after T010

**Checkpoint**: User Story 3 is complete when the directory remains documentation-only and all out-of-scope topics are still assigned to their roadmap owners.

---

## Phase 6: Polish & Cross-Cutting Validation

**Purpose**: Reconcile the complete written baseline and prove it meets the feature-wide success criteria.

- [ ] T013 Reconcile MDR-001 through MDR-005, exact legacy identifiers, `Unknown` intent wording, and downstream obligations across specs/001-freeze-migration-decisions/spec.md, specs/001-freeze-migration-decisions/research.md, specs/001-freeze-migration-decisions/data-model.md, and specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md
- [ ] T014 Execute every document-inspection command in specs/001-freeze-migration-decisions/quickstart.md and correct any failing Markdown artifact under specs/001-freeze-migration-decisions/
- [ ] T015 Recheck all acceptance scenarios and success criteria against specs/001-freeze-migration-decisions/spec.md and record the completed requirements review in specs/001-freeze-migration-decisions/checklists/requirements.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; begin with T001.
- **Foundational (Phase 2)**: T002 depends on T001; T003 depends on T002 and blocks all user-story work.
- **User Story 1 (Phase 3)**: T004 depends on T003; T005 and T006 can run in parallel after T004.
- **User Story 2 (Phase 4)**: T007 depends on T003. Because it edits the shared `spec.md`, execute it after T004 when working in one checkout; T008 and T009 can run in parallel after T007.
- **User Story 3 (Phase 5)**: T010 depends on T003. Because it edits the shared `spec.md`, execute it after T004 and T007 when working in one checkout; T011 and T012 can run in parallel after T010.
- **Polish (Phase 6)**: T013 depends on all selected user stories; T014 depends on T013; T015 depends on T014.

### User Story Dependencies

- **User Story 1 (P1)**: Starts after Foundational and has no semantic dependency on another story; it is the suggested MVP.
- **User Story 2 (P2)**: Starts after Foundational and is independently testable, but its shared-file edit to `spec.md` must be coordinated with US1.
- **User Story 3 (P3)**: Starts after Foundational and is independently testable, but its shared-file edit to `spec.md` must be coordinated with US1 and US2.

### Within Each User Story

- Finalize the applicable decisions or boundaries in `spec.md` first.
- Update the downstream contract and quickstart assertions in parallel only after the applicable `spec.md` task completes.
- Run the relevant quickstart inspection assertions before declaring the story complete.
- Do not create executable tests, source code, projects, or build artifacts.

### Parallel Opportunities

- After T004, run T005 and T006 in parallel because they modify separate files.
- After T007, run T008 and T009 in parallel because they modify separate files.
- After T010, run T011 and T012 in parallel because they modify separate files.
- US1, US2, and US3 are semantically independent after T003, but edits to their shared Markdown files must be serialized or explicitly coordinated.

---

## Parallel Example: User Story 1

```text
After T004 completes:
Task T005: Define mandatory downstream citations in specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md
Task T006: Add US1 inspection assertions in specs/001-freeze-migration-decisions/quickstart.md
```

## Parallel Example: User Story 2

```text
After T007 completes:
Task T008: Add conditional citations and audit conformance rules in specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md
Task T009: Add US2 inspection assertions in specs/001-freeze-migration-decisions/quickstart.md
```

## Parallel Example: User Story 3

```text
After T010 completes:
Task T011: Add scope-protecting rejection conditions in specs/001-freeze-migration-decisions/contracts/downstream-specification-contract.md
Task T012: Add documentation-only filesystem assertions in specs/001-freeze-migration-decisions/quickstart.md
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational.
3. Complete T004, then T005 and T006.
4. Run the US1 assertions in `quickstart.md` and stop for an independent review.

### Incremental Delivery

1. Complete Setup and Foundational to stabilize the decision model.
2. Complete US1 to make the core migration baseline usable.
3. Complete US2 to make evidence and judgment independently auditable.
4. Complete US3 to prove that the feature stayed within its roadmap boundary.
5. Complete cross-cutting reconciliation and the full quickstart inspection.

### Parallel Team Strategy

1. Complete T001 through T003 sequentially.
2. Assign the applicable `spec.md` task to one editor.
3. After that task completes, update the contract and quickstart in parallel.
4. Repeat for each selected story, then complete T013 through T015 sequentially.

---

## Notes

- `[P]` tasks change different files and have no dependency on another incomplete task at that point.
- `[US1]`, `[US2]`, and `[US3]` map directly to the prioritized stories in `spec.md`.
- All legacy-behavior evidence comes from `../../old/docs/`; constitution rules govern migration judgments but are not legacy evidence.
- Preserve `Main`, `MainFrame`, `module-info`, `OrderPlacement.getOrderId()`, `return 100;`, and both identifier-`1` constructor expressions verbatim when cited.
- Historical intent for identifiers `1` and `100` remains `Unknown` unless new evidence is explicitly admitted through a scope change.
- Stop at documentation; implementation begins only in the later roadmap specifications that own it.
