# Downstream Specification Decision Contract

## Purpose

This documentation contract implements FR-013 and FR-014. It defines how later migration
specifications consume the frozen decisions in `spec.md`. It is not an application API, command,
endpoint, file format, or runtime interface.

## Required Citation Block

Every consuming specification must include the following information for each applicable decision:

| Field | Requirement |
|---|---|
| Decision ID | Exact applicable `MDR-*` identifier |
| Applicability | Why the decision affects the consuming specification |
| Applied consequence | How the specification preserves or applies the frozen baseline |
| Deviation reference | `None`, or a separately approved behavior-change specification |

A prose section or table is acceptable if all four fields are unambiguous.

## Mandatory Consumers

Every row below is mandatory. Each consumer must record the cited decision and the applied
consequence in its Required Citation Block; one row does not replace another row for the same
consumer.

| Consumer specification | Mandatory decision citation | Required applied consequence |
|---|---|---|
| 002 · C# project skeleton | MDR-001 | Retain `Main` and `MainFrame` as distinct console and graphical entry surfaces in the project shell, and apply .NET MAUI with Windows support to the graphical surface. |
| 003 · Acceptance checklist from rules | MDR-004 | Include externally reported identifier `100` as baseline behavior, preserve its exact rule evidence `return 100;`, and record `Intent: Unknown`. |
| 003 · Acceptance checklist from rules | MDR-005 | Include fixed construction identifier `1` in both entry flows, preserve `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and `order = new OrderPlacement(1, chosenItems, timingPreference);`, and record `Intent: Unknown`. |
| 005 · Port OrderPlacement | MDR-004 | Preserve the `OrderPlacement.getOrderId()` behavior evidenced by `return 100;` and do not infer its historical intent. |
| 009 · Port MainFrame desktop UI | MDR-001 | Retain `MainFrame` as the distinct graphical entry surface and implement its equivalent with .NET MAUI and Windows support. |
| 009 · Port MainFrame desktop UI | MDR-005 | Preserve the window-flow behavior evidenced by `order = new OrderPlacement(1, chosenItems, timingPreference);` and do not infer its historical intent. |
| 010 · Port Main console flow | MDR-001 | Retain `Main` as the distinct console entry surface; do not merge it with or replace it by the `MainFrame` graphical surface. |
| 010 · Port Main console flow | MDR-005 | Preserve the console-flow behavior evidenced by `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and do not infer its historical intent. |
| 011 · Acceptance against frozen rules | MDR-004 | Validate externally reported identifier `100`, including the behavior evidenced by `return 100;`, and retain `Intent: Unknown`. |
| 011 · Acceptance against frozen rules | MDR-005 | Validate fixed construction identifier `1` in both entry flows against both exact constructor expressions and retain `Intent: Unknown`. |

## Conditional Consumers

- Cite MDR-002 whenever a later specification discusses source language, the operator phrase
  `Java(swift)`, or possible Swift scope. The Required Citation Block MUST describe Java as the
  documented source language, keep the original meaning of “swift” unresolved, and MUST NOT claim
  a Swift component or behavior unless newly admitted evidence and an explicit scope change
  establish that scope.
- Cite MDR-003 whenever a later specification discusses graphical surfaces, JavaFX, `module-info`,
  or dependency scope. The Required Citation Block MUST treat `module-info` as dependency and scope
  evidence only, keep dependency declarations separate from executable behavior, and MUST NOT
  derive an additional JavaFX user interface unless newly admitted executable evidence and an
  explicit scope change establish that surface.
- Cite any additional MDR decision whenever its consequence applies, even if the consumer is not
  named in the mandatory table.

## Conformance Rules

A consuming specification conforms only when it:

1. uses the exact applicable `MDR-*` identifier;
2. keeps `Main` and `MainFrame` as distinct retained entry surfaces where MDR-001 applies;
3. applies MDR-002 by describing Java as the documented source language, preserving
   `Java(swift)` as ambiguous wording, and neither inferring a Swift component nor claiming that
   “swift” was intended to mean Swing;
4. applies MDR-003 by treating `module-info` as dependency and scope evidence only, separating its
   declarations from executable behavior, and not inferring an additional JavaFX user interface;
5. preserves fixed identifier `1` and reported identifier `100` wherever MDR-004 or MDR-005 applies;
6. records `Intent: Unknown` for both identifier behaviors, retains that classification unless
   newly admitted evidence is reviewed through an explicit scope change, does not classify either
   behavior as an intended domain rule, defect, or temporary shortcut, and does not treat selection
   of a replacement behavior as evidence of historical intent; and
7. records any override as a separate approved behavior-change specification that identifies the
   legacy behavior being changed and supplies explicit acceptance criteria.

## Rejection Conditions

The citation fails this contract if it silently overrides a decision, paraphrases a decision without
its identifier, merges or drops an entry surface, labels `1` or `100` as correct or defective,
introduces Swift or JavaFX behavior without new evidence and an explicit scope change, or replaces
.NET MAUI without an adopted constitutional amendment.
