<!--
Sync Impact Report
- Version change: none -> 1.0.0
- Modified principles: none (initial adoption)
- Added principles:
  - I. Evidence-Preserving Migration
  - II. C# and .NET MAUI Architecture
  - III. SOLID, DRY, and Clean Code
  - IV. Unit-Tested Behavior
  - V. Integration-Tested Workflows
- Added sections:
  - Technology and Evidence Constraints
  - Spec-First Delivery and Quality Gates
- Removed sections: none
- Follow-up TODOs: none
-->
# Coffee Shop C# Migration Constitution

## Core Principles

### I. Evidence-Preserving Migration

Every requirement, design decision, task, implementation behavior, and test expectation MUST trace
to the frozen legacy documentation under `../../old/docs/` or to an explicit requirement supplied
after that documentation was produced. Verbatim legacy identifiers and rule evidence MUST remain
verbatim wherever they are cited. The migration MUST report and reproduce documented behavior; it
MUST NOT infer behavior from the migration goal, platform conventions, or desired product features.
Any intentional behavior change MUST be specified separately, identify the documented legacy
behavior it changes, and receive an explicit acceptance criterion before implementation. This keeps
the C# rebuild auditable when runtime execution evidence is absent.

### II. C# and .NET MAUI Architecture

Application code MUST be written in C# and the graphical application MUST use .NET MAUI with
Windows as a supported target. Domain behavior MUST remain independent of MAUI views and platform
APIs. Presentation, application orchestration, domain logic, and infrastructure concerns MUST have
explicit boundaries, and dependencies MUST point toward the domain. Platform-specific code MUST be
isolated behind narrow abstractions when it is required. The selected supported .NET and .NET MAUI
versions MUST be pinned in the implementation plan. These rules preserve portability and make the
documented behavior testable without a graphical runtime.

### III. SOLID, DRY, and Clean Code

Production code and test code MUST apply SOLID principles, remove knowledge duplication, and use
clear C# naming and small cohesive units. Each type or member MUST have one focused reason to change;
dependencies on variable behavior or external effects MUST be injected through appropriately narrow
contracts. Repeated business rules MUST have one authoritative implementation, while coincidentally
similar code MUST NOT be abstracted without a demonstrated shared concept. Public APIs MUST be kept
minimal, mutable state MUST be constrained, and failures MUST be explicit. Reviewers MUST reject
unnecessary indirection, speculative abstractions, hidden side effects, and dead code. Clean design
is required to make the migration maintainable without obscuring legacy rule traceability.

### IV. Unit-Tested Behavior

Every implemented business rule, default, validation boundary, mapping, and state transition MUST
have deterministic unit tests at the narrowest practical layer. A behavior change MUST begin with a
test that fails for the expected reason, followed by the minimum implementation needed to pass and
then refactoring with the suite green. Unit tests MUST isolate platform UI and external effects,
cover normal, boundary, and documented fallback paths, and name the rule being verified. Tests MUST
not duplicate production algorithms or depend on execution order, network access, wall-clock time,
or shared mutable state. A task is incomplete while its required unit tests fail or are absent.

### V. Integration-Tested Workflows

Each documented user workflow and every boundary between presentation, orchestration, domain, and
infrastructure code MUST be covered by integration tests proportional to its risk. Integration tests
MUST verify real component composition, navigation or command flow, dependency registration, state
transfer, and platform adapters where those behaviors exist. UI automation MAY supplement but MUST
not replace integration coverage of application and domain boundaries. Tests MUST remain repeatable
and MUST identify any Windows-only execution prerequisite. No workflow task is complete until both
its unit tests and applicable integration tests pass together.

## Technology and Evidence Constraints

- The implementation language is C#; the graphical client framework is .NET MAUI and Windows is a
  required supported target.
- `../../old/docs/` is the authoritative description of the legacy Java estate for this work unit.
  Workspace code or repositories outside this working tree MUST NOT be used as behavioral evidence.
- Plans and specifications MUST distinguish documented legacy behavior from proposed changes. A
  desired capability that is absent from the evidence MUST be recorded as a new requirement, never
  presented as existing behavior.
- Legacy component and symbol names MUST be quoted exactly when used as traceability evidence. C#
  names MAY follow established .NET conventions only when an explicit mapping to the legacy symbol
  is maintained in the specification or plan.
- The solution MUST build with warnings treated as errors for project-owned code. Nullable reference
  type analysis and the repository's agreed C# formatting and static-analysis rules MUST be enabled.
- Secrets, credentials, generated build output, and machine-specific configuration MUST NOT be
  committed. Dependencies MUST be justified by a requirement and centrally versioned where the
  solution structure permits it.

## Spec-First Delivery and Quality Gates

Work MUST proceed in this order: specification, implementation plan, dependency-ordered tasks, then
implementation. The specification MUST contain testable acceptance criteria and trace each retained
legacy behavior to frozen documentation. The plan MUST record architectural boundaries, C#/.NET
MAUI versions, the Windows validation strategy, and explicit decisions for every intended deviation.
Tasks MUST identify their relevant unit and integration tests and MUST preserve dependency order.

Before implementation begins, the specification, plan, and tasks MUST be checked for unresolved
contradictions and unexplained behavior. During implementation, each task MUST satisfy the applicable
principles and leave the solution buildable. Before a task or feature is declared complete, reviewers
MUST confirm traceability, a clean warning-free build, passing unit tests, passing applicable
integration tests, and no undocumented behavior changes. Exceptions MUST be documented with scope,
rationale, risk, owner, and a removal or review condition; convenience alone is not justification.

## Governance

This constitution is the highest-authority development policy for this work unit. Specifications,
plans, tasks, implementation, and reviews MUST demonstrate compliance. Where another local practice
conflicts with this constitution, this constitution prevails unless it is formally amended.

An amendment MUST be proposed as a documented change that states its rationale, affected principles,
migration impact, and required changes to active feature artifacts. Adoption requires explicit owner
approval and an updated Sync Impact Report. Amendments MUST use semantic versioning: MAJOR for
removing or incompatibly redefining governance, MINOR for adding a principle or materially expanding
mandatory guidance, and PATCH for non-semantic clarification or correction. The ratification date
MUST remain the original adoption date; the last-amended date MUST change on every adopted amendment.

Every specification and plan review MUST include a constitution check. Every implementation review
MUST verify its quality gates with recorded build and test evidence. A compliance review MUST also
occur before a feature is presented for acceptance. Unresolved violations block completion; approved
temporary exceptions MUST satisfy the exception record required by the delivery section.

**Version**: 1.0.0 | **Ratified**: 2026-10-14 | **Last Amended**: 2026-10-14
