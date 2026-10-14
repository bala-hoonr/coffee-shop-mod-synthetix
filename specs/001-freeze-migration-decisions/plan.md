# Implementation Plan: Freeze Migration Decisions

**Branch**: `001-freeze-migration-decisions` | **Date**: 2026-10-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-freeze-migration-decisions/spec.md`

## Summary

Produce a documentation-only migration baseline that freezes five decisions before any port: retain
the distinct `Main` console and `MainFrame` graphical entry surfaces, use .NET MAUI for the graphical
surface with Windows support, treat `Java(swift)` as ambiguous wording rather than Swift evidence,
treat `module-info` as dependency evidence rather than a separate JavaFX user interface, and preserve
the fixed identifier `1` and `OrderPlacement.getOrderId()` result `100` without inventing their intent.
The design models decisions, evidence, ambiguity, and downstream citation obligations; it creates no
application code, project skeleton, component design, or executable test.

## Technical Context

**Language/Version**: Markdown/CommonMark for this feature's artifacts. Downstream implementation
baseline pinned by the constitution to C# 14, `net10.0`, .NET SDK `10.0.402`, and .NET MAUI workload
`10.0.110`; specification 002 owns materializing those pins in project files.

**Primary Dependencies**: None for this documentation-only feature. .NET MAUI is a frozen downstream
technology constraint, not an installed dependency or legacy-estate claim in this feature.

**Storage**: N/A; the record is version-controlled Markdown and defines no runtime persistence.

**Testing**: Deterministic document inspection with `rg`, `find`, and shell assertions as described in
`quickstart.md`; no build, executable test suite, or application run is in scope.

**Target Platform**: Documentation validation is OS-independent. The downstream graphical client
must support Windows through the standard .NET MAUI Windows target; native Windows build and workflow
validation begins only after the relevant later specifications create an application.

**Project Type**: Documentation-only migration decision record consumed by later specifications.

**Performance Goals**: N/A; no runtime behavior is produced.

**Constraints**: Use only frozen legacy documentation under `../../old/docs/` for legacy claims;
preserve verbatim identifiers and rule evidence; distinguish observations from migration judgment;
leave identifier intent unknown; contain exactly five `MDR-*` decisions; create no application code,
scaffolding, component ports, or executable tests; absorb no work from roadmap specifications 002–011.

**Scale/Scope**: One record containing five decisions across four decision areas, with downstream
citation obligations for specifications 002, 003, 005, 009, 010, and 011 and conditional obligations
where later specifications discuss Swift, JavaFX, source language, or UI scope.

## Constitution Check

*GATE: Passed before Phase 0 research and re-checked after Phase 1 design.*

| Gate | Pre-design evaluation | Post-design re-check |
|---|---|---|
| I. Evidence-Preserving Migration | PASS — every legacy-behavior claim is traceable to `../../old/docs/`; `1`, `100`, and all legacy identifiers remain verbatim. Preservation is migration policy, not a claim of original intent. | PASS — `research.md`, `data-model.md`, the downstream contract, and `quickstart.md` keep legacy evidence separate from governance and research decisions. |
| II. C# and .NET MAUI Architecture | PASS — MDR-001 retains both entry surfaces and selects constitution-mandated .NET MAUI with Windows support. The stable downstream baseline is pinned to C# 14, `net10.0`, SDK `10.0.402`, and MAUI `10.0.110`; no project is created here. | PASS — the artifacts state the downstream constraint without selecting project topology or implementing presentation, orchestration, domain, infrastructure, or platform-adapter types. |
| III. SOLID, DRY, and Clean Code | PASS (not applicable to production/test code) — no code is authorized. The documentation design gives each decision, evidence reference, ambiguity, and downstream obligation one clear role. | PASS — the documentation model avoids duplicated authority and speculative implementation abstractions. |
| IV. Unit-Tested Behavior | PASS (not applicable) — no behavior is implemented, and FR-001 prohibits executable tests. Document inspection validates this record; later implementation remains subject to unit-test requirements. | PASS — `quickstart.md` contains record-inspection assertions only and creates no test project or production behavior. |
| V. Integration-Tested Workflows | PASS (not applicable) — no workflow is implemented. Later specifications must validate composition and record Windows-only prerequisites when code exists. | PASS — no integration or UI automation is pulled forward; the downstream Windows strategy remains explicit. |
| Technology and Evidence Constraints | PASS — .NET MAUI/Windows is identified as governance, not legacy evidence; no secrets, dependencies, generated output, or machine configuration are introduced. | PASS — all generated files are Markdown under the feature directory and no implementation dependency is added. |
| Spec-First Delivery and Quality Gates | PASS — specification precedes plan; no tasks or implementation are performed by this workflow. All decision questions have a frozen disposition. | PASS — Phase 0 and Phase 1 artifacts contain no unresolved decision, contradiction, code, build result, or test claim. |

**Windows validation strategy for later implementation**: after specifications 002, 009, and 010
create the relevant hosts, validate on native Windows by restoring and building the console and .NET
MAUI Windows hosts with warnings treated as errors, running headless unit and integration coverage for
their boundaries, and performing graphical build/launch/navigation smoke validation. The exact
commands, host names, target OS floor, and prerequisites belong to those later specifications and to
the final acceptance work in specification 011.

No constitution violation or temporary exception is required.

## Project Structure

### Documentation (this feature)

```text
specs/001-freeze-migration-decisions/
├── analysis.md
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── tasks.md
├── contracts/
│   └── downstream-specification-contract.md
└── checklists/
    └── requirements.md
```

### Source Code (repository root)

```text
No source-code, test-code, project, package, or generated-output directories are created or modified
by this feature.
```

**Structure Decision**: Keep every deliverable under
`specs/001-freeze-migration-decisions/`. The contract is a documentation interface for downstream
specification authors, not an application API. T001 confirmed this inventory against
`../../old/docs/README.md`, which identifies the frozen legacy-document set, and
`../../old/docs/roadmap.md`, which assigns specification 001 only the written decision record. The
current inventory contains Markdown specification, planning, research, data-model, contract,
inspection, checklist, analysis, and task artifacts only. It contains no application source,
project scaffold, executable test, package, or generated output.

### Deferred Roadmap Ownership

| Roadmap specification | Work retained by that specification |
|---|---|
| 002 | C# solution, projects, framework setup, console host, and build/run entry points |
| 003 | Rule-derived acceptance checklist |
| 004–008 | Ports of `CoffeeShopMenu`, `OrderPlacement`, `OrderStatus`, `PaymentOptions`, and `CustomerReview` |
| 009 | `MainFrame` desktop user-interface port |
| 010 | `Main` console-flow port |
| 011 | Execution of acceptance against the frozen rules |

Specification 001 may record constraints and downstream citation obligations for that work, but it
does not create, design, implement, or execute any of these deferred deliverables.

## Complexity Tracking

No constitution violations require justification.
