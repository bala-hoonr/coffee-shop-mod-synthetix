# Quickstart: Validate the Written Decision Baseline

## Prerequisites

- Run from the repository root.
- Use a POSIX-compatible shell with `rg`, `find`, and `test` available.
- Do not install an SDK or workload; this validation inspects documentation only.

## 1. Confirm all Phase 0 and Phase 1 artifacts exist

```sh
FEATURE_DIR=specs/001-freeze-migration-decisions

for file in plan.md research.md data-model.md quickstart.md \
  contracts/downstream-specification-contract.md; do
  test -f "$FEATURE_DIR/$file" || exit 1
done
```

Expected outcome: exit status `0`.

## 2. Confirm exactly five numbered decisions

```sh
SPEC_FILE="$FEATURE_DIR/spec.md"

test "$(rg -c '^\| \*\*MDR-00[1-5]\*\* \|' "$SPEC_FILE")" -eq 5
for id in MDR-001 MDR-002 MDR-003 MDR-004 MDR-005; do
  rg -q "^\| \*\*$id\*\* \|" "$SPEC_FILE" || exit 1
done
```

Expected outcome: exit status `0`; all five identifiers occur as decision rows.

## 3. Confirm exact identifier evidence

```sh
rg -Fq 'return 100;' "$SPEC_FILE"
rg -Fq 'OrderPlacement order = new OrderPlacement(1, chosenItems, timingPreference);' "$SPEC_FILE"
rg -Fq 'order = new OrderPlacement(1, chosenItems, timingPreference);' "$SPEC_FILE"
```

Expected outcome: exit status `0`; the three exact rule substrings remain present.

## 4. Confirm frozen choices and unknown intent

```sh
rg -q 'MDR-001.*`Main`.*distinct.*`MainFrame`.*distinct' "$SPEC_FILE"
rg -q 'MDR-001.*\.NET MAUI.*Windows' "$SPEC_FILE"
rg -q 'MDR-002.*Swift' "$SPEC_FILE"
rg -q 'MDR-003.*JavaFX' "$SPEC_FILE"
rg -q 'MDR-004.*Do not classify.*bug.*intended domain rule' "$SPEC_FILE"
rg -q 'MDR-005.*Do not classify.*bug.*intended domain rule' "$SPEC_FILE"
```

Expected outcome: exit status `0`; distinct entry surfaces, selected technology, source/scope
interpretation, and ambiguity treatment are all inspectable from the decision table.

## 5. Confirm the downstream citation contract

```sh
CONTRACT_FILE="$FEATURE_DIR/contracts/downstream-specification-contract.md"

for id in MDR-001 MDR-002 MDR-003 MDR-004 MDR-005; do
  rg -q "$id" "$CONTRACT_FILE" || exit 1
done
rg -Fq 'separately approved behavior-change specification' "$CONTRACT_FILE"
rg -Fq 'explicit acceptance criteria' "$CONTRACT_FILE"
```

Expected outcome: exit status `0`; all decisions have a consumption rule and overrides are explicit.

## 6. Confirm the feature remains documentation-only

```sh
test -z "$(find "$FEATURE_DIR" -type f ! -name '*.md' -print)"
test -z "$(find "$FEATURE_DIR" -type d \
  \( -name src -o -name tests -o -name bin -o -name obj \) -print)"
```

Expected outcome: exit status `0`; the feature contains no application source, project scaffold,
generated output, or executable tests.

## Completion Signal

All commands exit with status `0`. No build, runtime, scaffold, application-code, or executable-test
command is needed or permitted for this feature.
