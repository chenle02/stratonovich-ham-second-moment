#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-local-flow-lean-v1/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/compile-time.txt ${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/src -o ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/out/StratonovichHAMAudit/LocalFlow.olean ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/src/StratonovichHAMAudit/LocalFlow.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/compile.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/compile.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/Audit.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/compile-audit.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/compile-audit.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
export LEAN_PATH=${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay-time.txt ${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay/src -o ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay/out/StratonovichHAMAudit/LocalFlow.olean ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay/src/StratonovichHAMAudit/LocalFlow.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/Audit.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay-audit.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/replay-audit.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongMaskEndpoint.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongMaskEndpoint.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongMaskEndpoint.exit
if [ "$rc" -eq 0 ]; then exit 10; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongWhiteWitness.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongWhiteWitness.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongWhiteWitness.exit
if [ "$rc" -eq 0 ]; then exit 10; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongSchurCancellation.lean > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongSchurCancellation.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/WrongSchurCancellation.exit
if [ "$rc" -eq 0 ]; then exit 10; fi
printf "0\n" > ${LOCAL_RAW}/stratonovich-local-flow-lean-v1/EXIT
exit 0
