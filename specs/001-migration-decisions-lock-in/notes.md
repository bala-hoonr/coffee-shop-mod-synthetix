# Task Evidence Notes

## T001

## T002

**Task**: Verify that the runtime-observation gap notice (FR-006) in `spec.md` states: (1) all
rules derived from static reading, (2) 0 of 28 inventory items are execution-grounded, and
(3) rules phrased as "always", "unconditionally", or "regardless" rest on static reading only.

**Findings**: PASS — all three required statements are present in the gap notice at the top of
`specs/001-migration-decisions-lock-in/spec.md` (lines immediately after the preamble block),
under the heading `> **Runtime-observation gap** (Constitution Principle VI)`.

Verbatim substrings verified:

1. **Static reading**: "Every rule in this document was derived from static reading of the legacy
   Java estate as recorded in `../../old/docs/`."

2. **0 of 28 execution-grounded**: "The Java application was not executed; 0 of 28 inventory
   items are execution-grounded."

3. **Keyword phrases on static reading only**: "Rules phrased as 'always', 'unconditionally', or
   'regardless' reflect the static reading only."

All three conditions required by FR-006 are satisfied. The gap notice also includes a forward
obligation — future work executing the Java application MUST reconcile divergence before declaring
the port complete — which is consistent with Constitution Principle VI.

**Result**: FR-006 VERIFIED.

## T003

## T004

## T005

## T006

## T007

## T008

## T009
