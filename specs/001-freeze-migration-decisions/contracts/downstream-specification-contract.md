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
| Deviation reference | `None`, or a separately approved scope- or behavior-change specification as required by the cited decision |

A prose section or table is acceptable if all four fields are unambiguous.
When preserved behavior changes, the deviation reference must identify a
separately approved behavior-change specification with explicit acceptance criteria.

## Mandatory Consumers

Every row below is mandatory. Each consumer must record the cited decision and the applied
consequence in its Required Citation Block; one row does not replace another row for the same
consumer.

| Consumer specification | Mandatory decision citation | Required applied consequence |
|---|---|---|
| 002 · C# project skeleton | MDR-001 | Retain `Main` and `MainFrame` as distinct console and graphical entry surfaces in the project shell, and apply .NET MAUI with Windows support to the graphical surface. |
| 003 · Acceptance checklist from rules | MDR-004 | Include externally reported identifier `100` as baseline behavior, preserve its exact rule evidence `return 100;`, and record `Intent: Unknown`. |
| 003 · Acceptance checklist from rules | MDR-005 | Include fixed construction identifier `1` in both entry flows, preserve `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and `order = new OrderPlacement(1, chosenItems, timingPreference);`, and record `Intent: Unknown`. |
| 005 · Port OrderPlacement | MDR-004 | Preserve the `OrderPlacement.getOrderId()` behavior evidenced by `return 100;` and retain `Intent: Unknown`. |
| 009 · Port MainFrame desktop UI | MDR-001 | Retain `MainFrame` as the distinct graphical entry surface and implement its equivalent with .NET MAUI and Windows support. |
| 009 · Port MainFrame desktop UI | MDR-005 | Preserve the window-flow behavior evidenced by `order = new OrderPlacement(1, chosenItems, timingPreference);` and retain `Intent: Unknown`. |
| 010 · Port Main console flow | MDR-001 | Retain `Main` as the distinct console entry surface; do not merge it with or replace it by the `MainFrame` graphical surface. |
| 010 · Port Main console flow | MDR-005 | Preserve the console-flow behavior evidenced by `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);` and retain `Intent: Unknown`. |
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
   behavior as a bug or defect, an intended domain rule, or a temporary shortcut, and does not treat
   selection of a replacement behavior as evidence of historical intent; and
7. records any override as a separate approved scope- or behavior-change specification, as required
   by the cited decision, that identifies the affected legacy surface or behavior and supplies
   explicit acceptance criteria.

## Rejection Conditions

A consuming specification fails this contract if any of the following conditions applies. A failed
citation or deviation does not supersede the frozen decision or any linked downstream obligation.

1. **Silent MDR override**: The specification omits the exact applicable `MDR-*` identifier,
   paraphrases or contradicts the decision while recording no deviation, or otherwise changes an
   applied consequence without the separate approved scope- or behavior-change specification
   required by that decision. Replacing .NET MAUI or removing Windows support also requires an
   already-adopted constitutional amendment.
2. **Merged or dropped entry surface**: The specification merges `Main` and `MainFrame`, drops
   either one, or treats one as a replacement for the other without a separately approved scope-change
   specification that cites MDR-001 and supplies explicit acceptance criteria.
3. **Inferred Swift or JavaFX behavior**: The specification derives a Swift component or behavior
   from `Java(swift)`, claims that “swift” meant Swing, or derives an executable JavaFX screen,
   journey, entry surface, or behavior from `module-info` without newly admitted evidence and an
   explicit scope change citing MDR-002 or MDR-003 as applicable.
4. **Undocumented identifier change**: The specification changes the behavior evidenced by
   `return 100;`, `OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);`, or
   `order = new OrderPlacement(1, chosenItems, timingPreference);` without a separately approved
   behavior-change specification that cites MDR-004 or MDR-005 as applicable, identifies every
   affected verbatim rule substring, and supplies explicit acceptance criteria. Labeling `1` or
   `100` as correct, a bug or defect, an intended domain rule, or a temporary shortcut, or changing
   `Intent: Unknown` by inference, also fails this contract.
