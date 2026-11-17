---

description: "Task list for Migration Decisions Lock-in (spec 001)"
---

# Tasks: Migration Decisions Lock-in

**Input**: Design documents from `/specs/001-migration-decisions-lock-in/`

**Deliverable**: A verified, internally consistent written decision record (`spec.md`) that
freezes five operator choices blocking every downstream migration specification. No code is
written; no tests are executed. All tasks read source documents, verify content against
requirements, and write findings to `specs/001-migration-decisions-lock-in/notes.md`.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (no cross-task dependency)
- **[Story]**: Which user story this task serves (US1–US5)

---

## Phase 1: Setup

**Purpose**: Initialise the evidence record so all later tasks can append findings to it.

- [x] T001 Create `specs/001-migration-decisions-lock-in/notes.md` with a top-level heading
  `# Task Evidence Notes` and one stub sub-heading per task ID (T001–T009); leave each
  sub-heading body blank for subsequent tasks to fill in

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Confirm the cross-cutting runtime-observation gap notice (FR-006) and the
constitution consistency gate (SC-005) are in place before auditing individual decisions.
Both audits read the same source file; they may run in parallel once T001 is complete.

**⚠️ CRITICAL**: The per-story audits (Phase 3+) depend on knowing whether the gap notice
and constitution are intact. Complete this phase before the user-story phases.

- [x] T002 [P] Read `specs/001-migration-decisions-lock-in/spec.md` and verify the
  runtime-observation gap notice (FR-006) states: all rules derived from static reading,
  0 of 28 inventory items are execution-grounded, and rules phrased as "always",
  "unconditionally", or "regardless" rest on static reading only. Append findings under
  `## T002` in `specs/001-migration-decisions-lock-in/notes.md`.

- [x] T003 [P] Read `specs/001-migration-decisions-lock-in/spec.md` and `.specify/memory/constitution.md`
  and verify no decision in the Decision Record contradicts any principle in the constitution
  v1.1.0 (SC-005). Append findings — including which principles were checked and any
  conflict identified — under `## T003` in `specs/001-migration-decisions-lock-in/notes.md`.

**Checkpoint**: Gap notice and constitution consistency confirmed — user-story audits can proceed.

---

## Phase 3: User Story 1 — .NET Scaffolding Decision (Priority: P1) 🎯 MVP

**Goal**: Confirm that an engineer authoring spec 002 can determine the exact .NET version and
packaging format, and know that mvnw is not ported, by reading `spec.md` alone.

**Independent Test**: Read spec.md Decision 5 and FR-004/FR-007 in isolation; a reviewer can
state ".NET 8 LTS, self-contained single-file executable for Windows x64" and "mvnw is replaced
by the .NET toolchain" without consulting any other source.

### Implementation for User Story 1

- [ ] T004 [US1] Read `specs/001-migration-decisions-lock-in/spec.md` Decision 5 and verify
  it records: .NET 8 LTS, self-contained single-file executable for Windows x64 as the
  confirmed target (FR-004); that no other .NET version or packaging format is in scope without
  an amendment; and that `mvnw` and `module-info` are Java-specific with no C# analogue and
  are replaced wholesale by the .NET toolchain (FR-007). Verify the evidence anchors cite
  verbatim substrings from `../../old/docs/` (Constitution Principle I). Append findings under
  `## T004` in `specs/001-migration-decisions-lock-in/notes.md`.

**Checkpoint**: US1 audit complete — engineer authoring spec 002 is unblocked.

---

## Phase 4: User Story 2 — Defect Dispositions (Priority: P1)

**Goal**: Confirm that an engineer authoring specs 007–009 can read the exact disposition and
required parity test assertion for each of the four known Java defects from `spec.md` alone.

**Independent Test**: Read spec.md Decision 4 in isolation; for each of the four named defects
the reviewer can state the disposition (preserve) and the exact parity test assertion without
consulting any other source.

### Implementation for User Story 2

- [ ] T005 [US2] Read `specs/001-migration-decisions-lock-in/spec.md` Decision 4 and verify
  it records all four known Java defects with disposition `preserve verbatim` and the following
  exact parity test assertions (FR-003):
  - `OrderPlacement.getOrderId`: assert return value == `100` for any constructor input
  - `PaymentOptions.processPayment`: assert `isPaymentComplete == true` for any method string
    including invalid/empty values
  - `CustomerReview.addReview`: assert that a second call overwrites the values written by
    the first call
  - `OrderStatus.updateStatus`: assert that arbitrary strings (empty, null-like, out-of-domain)
    are accepted without error
  Verify evidence anchors for each defect cite verbatim substrings from
  `../../old/docs/overview.md` (Constitution Principle I). Append findings under `## T005` in
  `specs/001-migration-decisions-lock-in/notes.md`.

**Checkpoint**: US2 audit complete — parity test harness (spec 003) is unblocked.

---

## Phase 5: User Story 3 — UI Framework Decision (Priority: P1)

**Goal**: Confirm that an engineer authoring spec 004 or spec 011 can determine the confirmed
C# UI framework and the widget mapping table for all five Swing widgets from `spec.md` alone.

**Independent Test**: Read spec.md Decision 2 in isolation; a reviewer can state "WinForms" and
name the WinForms analogue of each of the five Swing widget types without consulting any other
source.

### Implementation for User Story 3

- [ ] T006 [US3] Read `specs/001-migration-decisions-lock-in/spec.md` Decision 2 and verify
  it records WinForms as the confirmed C# UI framework (FR-001) and includes a widget mapping
  table with exactly five rows covering all Swing widgets present in `MainFrame` (SC-004):
  `JFrame` → `Form`, `JTabbedPane` → `TabControl`, `JComboBox` → `ComboBox`,
  `JRadioButton` → `RadioButton`, `JOptionPane` → `MessageBox` / `InputDialog`. Verify the
  evidence anchor cites the `MainFrame` description from `../../old/docs/overview.md`
  (Constitution Principle I). Append findings under `## T006` in
  `specs/001-migration-decisions-lock-in/notes.md`.

**Checkpoint**: US3 audit complete — spec 004 and spec 011 are unblocked.

---

## Phase 6: User Story 4 — Entry-Point Scope (Priority: P1)

**Goal**: Confirm that an engineer authoring spec 010 or spec 011 can determine whether both
entry points (`Main` and `MainFrame`) survive the port from `spec.md` alone.

**Independent Test**: Read spec.md Decision 3 in isolation; a reviewer can state that both
`Main` (CLI) and `MainFrame` (GUI) are in scope without consulting any other source.

### Implementation for User Story 4

- [ ] T007 [US4] Read `specs/001-migration-decisions-lock-in/spec.md` Decision 3 and verify
  it records that both CLI entry point (`Main`) and GUI entry point (`MainFrame`) are in scope
  and both are ported and covered by parity tests (FR-002). Verify the evidence anchors cite
  verbatim substrings from `../../old/docs/overview.md` naming both `Main` and `MainFrame`
  (Constitution Principle I). Append findings under `## T007` in
  `specs/001-migration-decisions-lock-in/notes.md`.

**Checkpoint**: US4 audit complete — scope of specs 010 and 011 is confirmed.

---

## Phase 7: User Story 5 — Java(swift) Wording (Priority: P2)

**Goal**: Confirm that an engineer reading the stated goal can determine that no Swift sources
exist in the estate and the migration is Java-to-C# only from `spec.md` alone.

**Independent Test**: Read spec.md Decision 1 in isolation; a reviewer can state that
`Java(swift)` is a spurious parenthetical and no Swift sources are present without consulting
any other source.

### Implementation for User Story 5

- [ ] T008 [US5] Read `specs/001-migration-decisions-lock-in/spec.md` Decision 1 and verify
  it records that 'Java(swift)' is a spurious parenthetical, no Swift sources exist in the
  estate, and the migration is a pure Java-to-C# port (FR-005). Verify the evidence anchors
  cite `../../old/docs/approach.md` ("No Swift sources were seen in the estate") and the
  eight-file Java inventory from `../../old/docs/overview.md` (Constitution Principle I).
  Append findings under `## T008` in `specs/001-migration-decisions-lock-in/notes.md`.

**Checkpoint**: US5 audit complete — all 11 downstream specifications can safely scope to
Java-to-C# only.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Verify completeness across all five decisions (SC-001), confirm that every decision
is self-contained and unambiguous (SC-002), and confirm that the full Quickstart guide is
satisfied.

- [ ] T009 Read `specs/001-migration-decisions-lock-in/spec.md` and verify: (a) the Decision
  Record section contains exactly five numbered decisions with no "TBD" or unresolved entry
  (SC-001); (b) each decision's **Decision** cell is a complete, unambiguous answer readable
  without consulting any other document (SC-002); (c) all five success criteria
  (SC-001 through SC-005) from `specs/001-migration-decisions-lock-in/quickstart.md` are met
  by the current content of `spec.md`. Append a summary table — one row per success criterion,
  with status (PASS / FAIL) and evidence — under `## T009` in
  `specs/001-migration-decisions-lock-in/notes.md`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on T001 completion; T002 and T003 may run in parallel
- **User Stories (Phases 3–7)**: Each depends on Phase 2 completion; all five may then run
  in parallel with one another (they read independent sections of `spec.md`)
- **Polish (Phase 8)**: Depends on all user-story phases completing

### User Story Dependencies

- **US1 (T004)**: Can start after Phase 2 — independent of US2–US5
- **US2 (T005)**: Can start after Phase 2 — independent of US1, US3–US5
- **US3 (T006)**: Can start after Phase 2 — independent of US1, US2, US4–US5
- **US4 (T007)**: Can start after Phase 2 — independent of US1–US3, US5
- **US5 (T008)**: Can start after Phase 2 — independent of US1–US4

### Parallel Opportunities

- T002 and T003 can run in parallel (Phase 2)
- T004, T005, T006, T007, T008 can all run in parallel (Phases 3–7)

---

## Parallel Example: User Stories 1–5 (once Phase 2 is complete)

```
Task T004 [US1]: Audit Decision 5 (.NET version and packaging) in spec.md
Task T005 [US2]: Audit Decision 4 (defect dispositions) in spec.md
Task T006 [US3]: Audit Decision 2 (UI framework and widget mapping) in spec.md
Task T007 [US4]: Audit Decision 3 (entry-point scope) in spec.md
Task T008 [US5]: Audit Decision 1 (Java(swift) wording) in spec.md
```

All five read different sections; no file conflict.

---

## Implementation Strategy

### MVP First (User Stories 1–4 — all P1)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002, T003 in parallel)
3. Complete Phases 3–6 in parallel (T004, T005, T006, T007)
4. **Stop and validate**: US1–US4 findings in notes.md confirm spec.md is ready to unblock
   specs 002–011
5. Continue to Phase 7 (US5, T008) and Phase 8 (T009) for full completeness

### Incremental Delivery

1. T001 → T002 + T003 → foundation verified
2. T004 → US1 unblocked (spec 002 author has what they need)
3. T005 → US2 unblocked (spec 003 author has parity test assertions)
4. T006 → US3 unblocked (spec 004 / spec 011 authors have widget mapping)
5. T007 → US4 unblocked (scope of specs 010 and 011 confirmed)
6. T008 → US5 unblocked (all specs confirmed Java-to-C# only)
7. T009 → full completeness check recorded

---

## Notes

- [P] tasks operate on different sections of `spec.md` and produce separate sub-headings in
  `notes.md` — no file conflict
- Every task writes its findings to `specs/001-migration-decisions-lock-in/notes.md` under
  a heading that matches the task ID, never to `tasks.md`
- The deliverable (`spec.md`) already exists from the `/speckit-plan` phase; these tasks
  verify it meets every FR, SC, and constitution principle before downstream specs begin
- No code, no tests, no runtime execution — static document verification only
