#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/Audit.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/Audit.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/Audit.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongZeroShift.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongZeroShift.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongZeroShift.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongPrefactor.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongPrefactor.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongPrefactor.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongEndpoint.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongEndpoint.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongEndpoint.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongInverse.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongInverse.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongInverse.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongNumeratorSign.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongNumeratorSign.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/WrongNumeratorSign.exit
export LEAN_PATH=${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/src -o ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/out/StratonovichHAMAudit/MiddleCross.olean ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/src/StratonovichHAMAudit/MiddleCross.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/MiddleCross.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/MiddleCross.exit
${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/src ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/src/Audit.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/Audit.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-audit-01/replay/Audit.exit
exit 0
