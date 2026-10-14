# Phase 0 Research: Freeze Migration Decisions

This research resolves the planning questions for a written decision baseline. Legacy-behavior
findings come only from `../../old/docs/`. Technology versions come from constitution requirements
and current Microsoft support information and are not claims about the legacy estate.

## Entry surfaces and graphical technology

**Decision**: Preserve two distinct entry surfaces mirroring `Main` and `MainFrame`. Retain `Main` as
the console flow and make the `MainFrame` equivalent a .NET MAUI graphical client with Windows as a
required supported target.

**Rationale**: `../../old/docs/overview.md` documents `Main` as the complete console ordering flow and
`MainFrame` as the Swing ordering workflow. Constitution Principle II mandates C#, .NET MAUI, and
Windows support for the graphical application. This is frozen as MDR-001.

**Alternatives considered**: WinForms and WPF were migration-analysis options but conflict with the
constitution's selected graphical framework. Console-only and graphical-only shapes would each drop
a documented entry surface.

## Meaning of `Java(swift)`

**Decision**: Treat `Java(swift)` as ambiguous operator wording, not evidence of a Swift component.
Describe the frozen estate as Java with the documented `Main` console and Swing `MainFrame` surfaces.

**Rationale**: `../../old/docs/approach.md` records the declared and detected source as Java and says
the material shows a Java Swing console/desktop application with no Swift. `../../old/docs/overview.md`
declares Java and documents `Main`, `MainFrame`, and the other Java components. No Swift component or
behavior appears in the frozen material. This is frozen as MDR-002.

**Alternatives considered**: Treating “swift” as proof of a hidden Swift client is unsupported.
Treating it definitively as a typo for Swing would also invent intent. New executable evidence would
require an explicit scope change.

## JavaFX declaration scope

**Decision**: Treat `module-info` as dependency and scope evidence only. Do not define or port a
separate JavaFX user-interface surface; the documented executable surfaces are Swing `MainFrame` and
console `Main`.

**Rationale**: `../../old/docs/overview.md` says `module-info` declares JavaFX controls, JavaFX FXML,
and Java Desktop dependencies and opens/exports the application package, but “contains no executable
business behavior.” A dependency declaration alone does not establish a user journey or screen. This
is frozen as MDR-003.

**Alternatives considered**: Adding a JavaFX user interface merely because JavaFX is declared would
invent behavior absent from the frozen evidence. Later executable JavaFX evidence would require an
explicit scope change.

## Externally reported identifier `100`

**Decision**: Preserve `OrderPlacement.getOrderId()` returning `100`; classify its historical intent
as unknown rather than calling it either a defect or an intended domain rule.

**Rationale**: `../../old/docs/prd.md` FR-047 records the behavior and the verbatim rule evidence
`return 100;`. `../../old/docs/roadmap.md` states that the material did not measure intent.
Constitution Principle I requires preserved documented behavior unless an intentional change is
separately specified with explicit acceptance criteria. This is frozen as MDR-004.

**Alternatives considered**: Returning the identifier stored at construction might appear more
conventional, but it would be a behavior change. It may be proposed only in a separate approved
behavior-change specification.

## Fixed construction identifier `1`

**Decision**: Preserve fixed order identifier `1` in both entry flows; classify its historical intent
as unknown rather than calling it either a defect or an intended domain rule.

**Rationale**: `../../old/docs/prd.md` FR-009 records
`OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);`, and FR-039 records
`order = new OrderPlacement(1, chosenItems, timingPreference);`. `../../old/docs/roadmap.md` says intent
was not measured. Constitution Principle I supplies the preservation policy. This is frozen as
MDR-005. The frozen FR-039 citation is retained as written even though its recorded source metadata
names `Main.java`; this feature does not silently repair frozen evidence.

**Alternatives considered**: Generating identifiers or supplying another identifier would change
verified behavior and therefore requires a separate approved behavior-change specification.

## Supported downstream technology baseline

**Decision**: Pin later implementation planning to C# 14 targeting `net10.0`, .NET SDK `10.0.402`, and
.NET MAUI workload `10.0.110`. Specification 002 owns writing project/global configuration and
installing workloads; this feature records only the constraint.

**Rationale**: Constitution Principle II requires the implementation plan to pin supported .NET and
.NET MAUI versions. As of 2026-10-14, [.NET 10 is an active LTS release](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core),
and [.NET MAUI 10.0.110 is the supported stable servicing level](https://dotnet.microsoft.com/en-us/platform/support/policy/maui).
The standard [.NET MAUI Windows target uses WinUI 3](https://learn.microsoft.com/en-us/dotnet/maui/supported-platforms?view=net-maui-10.0).
These are proposed migration constraints, not legacy evidence.

**Alternatives considered**: .NET 11 and its MAUI line are prerelease as of the plan date. Older MAUI
lines are out of support. The experimental .NET MAUI WPF backend is not the constitution-selected
standard Windows target.

## Validation approach

**Decision**: Validate feature 001 by deterministic Markdown inspection on any host. Defer native
Windows build, unit, integration, launch, and navigation validation until the corresponding later
specifications create executable artifacts.

**Rationale**: FR-001 and FR-015 prohibit code, scaffolding, ports, and executable tests here. The
constitution's testing principles apply when behavior and workflows are implemented. Document
inspection can prove completeness, exact evidence, bounded scope, and downstream citation rules now.

**Alternatives considered**: Creating a C# test project, MAUI project, or Windows smoke test would
absorb roadmap specifications 002, 009, 010, or 011 and violate this feature's boundary.
