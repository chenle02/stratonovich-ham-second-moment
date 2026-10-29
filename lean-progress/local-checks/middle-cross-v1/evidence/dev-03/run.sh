#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/time.txt ${LEAN_BIN} --profile -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/src -o ${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/out/StratonovichHAMAudit/MiddleCross.olean ${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/src/StratonovichHAMAudit/MiddleCross.lean > ${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/lean.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-middle-cross-lean-dev-03/EXIT
exit "$rc"
