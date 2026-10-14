# Phase 0 Research: Freeze Migration Decisions

This research consolidates exactly five frozen migration dispositions before any port begins. Legacy
facts and rule evidence come only from `../../old/docs/`; migration policy comes only from
`.specify/memory/constitution.md`. The operator phrase `Java(swift)` supplies context but does not
establish a Swift component, behavior, or historical intent. Analysis in `approach.md` and
`roadmap.md` is used only in its stated role as migration-analysis context, not as executable
legacy evidence.

## MDR-001 — Retain both entry surfaces and use .NET MAUI on Windows

**Frozen disposition**: Preserve two distinct entry surfaces mirroring `Main` and `MainFrame`.
Retain `Main` as the console flow and make the `MainFrame` equivalent a .NET MAUI graphical client
with Windows as a required supported target.

**Legacy-evidence basis**:

- `../../old/docs/overview.md` describes `Main` as the complete console ordering flow.
- `../../old/docs/overview.md` describes `MainFrame` as the Swing ordering workflow.
- `../../old/docs/approach.md` identifies the Windows UI choice and the console-plus-desktop split
  as a migration decision; it does not establish the target technology as a legacy fact.

**Governing constraints**: Constitution Principle I prohibits dropping documented behavior based on
the migration goal. Principle II mandates C#, .NET MAUI for the graphical application, and Windows
as a supported target. The documented entry surfaces therefore supply the retained shape, while the
constitution supplies the target graphical technology.

**Rejected alternatives**:

- WinForms and WPF are not selectable because they conflict with the constitution-mandated
  graphical framework.
- Console-only and graphical-only shapes are rejected because each drops one documented entry
  surface.
- Merging `Main` and `MainFrame` into one undifferentiated entry surface is rejected because the
  frozen evidence describes distinct console and Swing workflows.

**Validation**: Document inspection must find `Main`, `MainFrame`, `.NET MAUI`, and `Windows` in this
disposition and must keep the two entry surfaces distinct. No project, host, or graphical client is
created or run by this feature.

## MDR-002 — Treat `Java(swift)` as ambiguous wording, not Swift evidence

**Frozen disposition**: Describe the frozen estate as Java with the documented console `Main` and
Swing `MainFrame` surfaces. Treat `Java(swift)` as ambiguous operator wording; do not use it as
evidence of a Swift component or behavior and do not claim that “swift” was intended to mean Swing.

**Legacy-evidence basis**:

- `../../old/docs/overview.md` identifies the estate language as `java` and documents the Java
  components `Main` and `MainFrame`.
- `../../old/docs/approach.md` records both declared and detected source as Java and reports that the
  supplied material shows a Java Swing console/desktop application and no Swift.

**Governing constraints**: Constitution Principle I requires every legacy claim to trace to frozen
documentation and prohibits inference from the migration goal. The constitution's Technology and
Evidence Constraints require desired but absent capability to be recorded as a new requirement,
not presented as existing behavior.

**Rejected alternatives**:

- Treating “swift” as proof of an undiscovered Swift client is unsupported by the frozen material.
- Treating “swift” definitively as a typo for Swing invents operator intent.
- Adding Swift scope without newly admitted evidence and an explicit requirement would present
  absent behavior as legacy behavior.

**Validation**: Document inspection must identify Java as the documented source language, retain
`Java(swift)` as ambiguous wording, and find no assertion that a Swift component exists or that the
operator's intended meaning is known.

## MDR-003 — Treat `module-info` as dependency evidence only

**Frozen disposition**: Retain `module-info` as dependency and scope evidence, not as an executable
entry surface. Do not define or port an additional JavaFX user interface; the documented executable
surfaces remain Swing `MainFrame` and console `Main`.

**Legacy-evidence basis**:

- `../../old/docs/overview.md` states that `module-info` declares dependencies on JavaFX controls,
  JavaFX FXML, and Java Desktop, opens the application package to JavaFX FXML, and exports it.
- The same `module-info` description states that it “contains no executable business behavior.”
- `../../old/docs/overview.md` separately describes the executable console `Main` and Swing
  `MainFrame` workflows.

**Governing constraints**: Constitution Principle I prohibits inferring behavior from a dependency
declaration or desired target shape. Principle II governs the target graphical framework but does
not convert a legacy dependency declaration into a documented user journey.

**Rejected alternatives**:

- Treating the JavaFX declarations as proof of a separate screen, user journey, or entry surface is
  rejected because none is documented in the frozen behavior set.
- Porting a JavaFX user interface merely because the dependencies are declared would invent
  behavior.
- Ignoring `module-info` entirely is rejected because its dependency declarations remain relevant
  evidence about the legacy estate even though they add no executable behavior.

**Validation**: Document inspection must preserve the exact identifier `module-info`, distinguish
dependency declarations from executable behavior, and add no JavaFX user-interface requirement.

## MDR-004 — Preserve the externally reported identifier `100`

**Frozen disposition**: Preserve `OrderPlacement.getOrderId()` returning `100`. Its historical
intent is `Unknown`; do not classify the behavior as either a defect or an intended domain rule.

**Legacy-evidence basis**:

- `../../old/docs/prd.md` FR-047 states that the externally reported order identifier is always
  `100`, regardless of the identifier stored at construction, and gives the verbatim rule evidence
  `return 100;`.
- `../../old/docs/overview.md` states that the `OrderPlacement` identifier accessor does not return
  the stored identifier and always returns `100`.
- `../../old/docs/roadmap.md` states that the material did not measure whether the identifier
  behaviors were intended.

**Governing constraints**: Constitution Principle I requires documented behavior to be reproduced
unless an intentional change is separately specified, identifies the documented legacy behavior it
changes, and receives an explicit acceptance criterion. Preservation is therefore migration policy,
not evidence that `100` is correct or intended.

**Rejected alternatives**:

- Returning the identifier supplied at construction is rejected for this baseline because it would
  change the verified `return 100;` behavior.
- Labeling the behavior a bug, intended rule, or temporary shortcut is rejected because historical
  intent was not measured.
- Silently choosing a conventional identifier design is rejected because platform conventions are
  not legacy evidence.

**Validation**: Document inspection must find `OrderPlacement.getOrderId()`, `return 100;`, and
`Intent: Unknown`. Any future replacement must be separately specified with the affected behavior
and explicit acceptance criteria; this feature performs no executable test.

## MDR-005 — Preserve fixed construction identifier `1`

**Frozen disposition**: Preserve fixed order identifier `1` in both documented entry flows. Its
historical intent is `Unknown`; do not classify the behavior as either a defect or an intended
domain rule.

**Legacy-evidence basis**:

- `../../old/docs/prd.md` FR-009 records the console-flow rule with the verbatim evidence
  `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);`.
- `../../old/docs/prd.md` FR-039 records the window-flow rule with the verbatim evidence
  `order = new OrderPlacement(1, chosenItems, timingPreference);`.
- `../../old/docs/roadmap.md` states that the material did not measure whether the identifier
  behaviors were intended.

FR-039's frozen source metadata names `Main.java`; this record retains that citation as written and
does not silently repair frozen evidence.

**Governing constraints**: Constitution Principle I requires the two documented constructor
behaviors to be preserved unless a separately specified intentional change identifies them and has
explicit acceptance criteria. Preservation does not establish why identifier `1` was used.

**Rejected alternatives**:

- Generating identifiers, using a different constant, or reconciling `1` with the reported `100`
  is rejected for this baseline because each would change verified behavior.
- Labeling fixed identifier `1` a bug, intended rule, or temporary shortcut is rejected because
  historical intent was not measured.
- Correcting FR-039's frozen source metadata without new admitted evidence is rejected because it
  would alter the supplied evidence record.

**Validation**: Document inspection must find both constructor expressions verbatim and
`Intent: Unknown`. A later behavior change must identify each affected expression and supply
explicit acceptance criteria in a separate specification.

## Validation approach

Feature 001 is validated by deterministic inspection of its Markdown record. This is consistent
with `../../old/docs/roadmap.md`, which assigns this specification a written decision record and
assigns project creation, ports, rule-checklist production, and acceptance execution to later
specifications. It also avoids claiming execution evidence that `../../old/docs/approach.md` says was
not measured.

Inspection must confirm all of the following:

1. Exactly five frozen dispositions exist, identified as MDR-001 through MDR-005.
2. Every legacy claim cites a source under `../../old/docs/`, and every migration judgment names its
   constitutional basis.
3. `Main`, `MainFrame`, and `module-info` remain verbatim and keep their distinct evidence roles.
4. `return 100;` and both identifier-`1` constructor expressions remain verbatim.
5. The intent of the `100` and `1` behaviors remains `Unknown`, with no defect or intended-rule
   inference.
6. WinForms, WPF, hidden Swift behavior, an additional JavaFX UI, stored or generated replacement
   identifiers, and silent evidence repair remain rejected alternatives rather than selected work.
7. No source code, project scaffold, ported component, executable test, build result, or acceptance
   result is produced by this feature.

The constitution's unit- and integration-testing gates apply when later specifications implement
behavior and workflows. Native Windows build, launch, navigation, and executable acceptance evidence
therefore remain deferred until the corresponding downstream artifacts exist.
