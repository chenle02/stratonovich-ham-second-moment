#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongZeroShift.lean > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongZeroShift.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongZeroShift.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongPrefactor.lean > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongPrefactor.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongPrefactor.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongEndpoint.lean > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongEndpoint.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongEndpoint.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongInverse.lean > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongInverse.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongInverse.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongNumeratorSign.lean > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongNumeratorSign.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-consumer-controls-v2/WrongNumeratorSign.exit
exit 0
