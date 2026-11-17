# Implementation Plan: Migration Decisions Lock-in

**Branch**: `001-migration-decisions-lock-in` | **Date**: 2026-11-17 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-migration-decisions-lock-in/spec.md`

## Summary

Produce a written decision record that freezes the five operator choices that would otherwise block
every downstream migration specification: Java(swift) wording, C# UI framework, entry-point scope,
known Java defect dispositions, and target .NET version and packaging format. The deliverable is a
document only — no code is written, no tests are executed, and no Java source is modified.

## Technical Context

**Language/Version**: N/A — deliverable is a documentation artifact (Markdown)

**Primary Dependencies**: N/A

**Storage**: N/A

**Testing**: Manual review — a human reviewer reads the completed document and can answer each of
the five decision questions without consulting any other source (see Quickstart)

**Target Platform**: N/A — the deliverable is consumed by engineers authoring specs 002–011

**Project Type**: Decision record (documentation only)

**Performance Goals**: N/A

**Constraints**: Every decision entry MUST include a verbatim evidence anchor from
`../../old/docs/`. No decision may rest on inference or memory (Constitution Principle I).

**Scale/Scope**: 5 decisions, 4 defect disposition entries, 1 widget mapping table

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|---|---|---|
| I. Evidence-First | Every decision MUST cite a verbatim substring from `../../old/docs/` | PASS — all 5 decisions in spec.md carry evidence anchors traceable to `overview.md` or `approach.md` |
| II. Parity Testing | No C# code produced by this spec; parity test assertions it records are consumed by spec 003 | PASS — no parity tests due from this spec |
| III. Decide-Before-Drift | All 4 defect dispositions recorded; each has an exact parity test assertion | PASS — Decision 4 covers all four defects verbatim |
| IV. Infrastructure Replaced | `mvnw` and `module-info` explicitly scoped out; .NET 8 LTS confirmed | PASS — FR-007 and Decision 5 state this |
| V. UI Framework/Entry-Point Locked | WinForms confirmed; both `Main` and `MainFrame` confirmed in scope | PASS — Decisions 2 and 3 record this |
| VI. Runtime-Observation Gap | Gap notice present at top of spec; 0% execution-grounded coverage stated | PASS — FR-006 and opening notice cover this |

**Post-design re-check**: All six gates still pass after Phase 1 design artifacts are written.
No complexity tracking entry is required (no violations).

## Project Structure

### Documentation (this feature)

```text
specs/001-migration-decisions-lock-in/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command — NOT created by /speckit-plan)
```

No `contracts/` directory is created: this feature has no external interfaces. The decision record
is consumed by human authors, not by any system boundary.

### Source Code

None. This specification produces documentation only; no source tree is created or modified.

## Complexity Tracking

No constitution violations were identified. No entries required.
