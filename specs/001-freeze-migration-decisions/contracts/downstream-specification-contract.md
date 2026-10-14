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

| Consumer specification | Required decision citations |
|---|---|
| 002 · C# project skeleton | MDR-001 |
| 003 · Acceptance checklist from rules | MDR-004, MDR-005 |
| 005 · Port OrderPlacement | MDR-004 |
| 009 · Port MainFrame desktop UI | MDR-001, MDR-005 |
| 010 · Port Main console flow | MDR-001, MDR-005 |
| 011 · Acceptance against frozen rules | MDR-004, MDR-005 |

## Conditional Consumers

- Cite MDR-002 whenever a later specification discusses source language, the operator phrase
  `Java(swift)`, or possible Swift scope.
- Cite MDR-003 whenever a later specification discusses graphical surfaces, JavaFX, `module-info`,
  or dependency scope.
- Cite any additional MDR decision whenever its consequence applies, even if the consumer is not
  named in the mandatory table.

## Conformance Rules

A consuming specification conforms only when it:

1. uses the exact applicable `MDR-*` identifier;
2. keeps `Main` and `MainFrame` as distinct retained entry surfaces where MDR-001 applies;
3. does not infer a Swift component or additional JavaFX user interface from absent behavior;
4. preserves fixed identifier `1` and reported identifier `100` wherever MDR-004 or MDR-005 applies;
5. keeps the historical intent of `1` and `100` unknown; and
6. records any override as a separate approved behavior-change specification that identifies the
   legacy behavior being changed and supplies explicit acceptance criteria.

## Rejection Conditions

The citation fails this contract if it silently overrides a decision, paraphrases a decision without
its identifier, merges or drops an entry surface, labels `1` or `100` as correct or defective,
introduces Swift or JavaFX behavior without new evidence and an explicit scope change, or replaces
.NET MAUI without an adopted constitutional amendment.
