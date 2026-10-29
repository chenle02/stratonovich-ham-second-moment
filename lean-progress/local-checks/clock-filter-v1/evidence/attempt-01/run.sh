#!/bin/bash
set -u
export LEAN_PATH=./lean-progress/local-checks/clock-filter-v1/attempt-01/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
export LEAN_NUM_THREADS=3
${LEAN_BIN} -j1 -D Elab.async=false -R ./lean-progress/local-checks/clock-filter-v1/attempt-01/src -o ./lean-progress/local-checks/clock-filter-v1/attempt-01/out/StratonovichHAMAudit/ClockFilter.olean ./lean-progress/local-checks/clock-filter-v1/attempt-01/src/StratonovichHAMAudit/ClockFilter.lean > ./lean-progress/local-checks/clock-filter-v1/attempt-01/lean.log 2>&1
rc=$?
printf "%s\n" "$rc" > ./lean-progress/local-checks/clock-filter-v1/attempt-01/EXIT
exit "$rc"
