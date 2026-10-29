#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/compile-time.txt ${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/src -o ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/out/StratonovichHAMAudit/ProjectionResidual.olean ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/src/StratonovichHAMAudit/ProjectionResidual.lean > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/compile.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/compile.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/Audit.lean > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/compile-audit.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/compile-audit.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
export LEAN_PATH=${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay-time.txt ${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay/src -o ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay/out/StratonovichHAMAudit/ProjectionResidual.olean ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay/src/StratonovichHAMAudit/ProjectionResidual.lean > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/Audit.lean > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay-audit.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/replay-audit.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/WrongParentSign.lean > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/WrongParentSign.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/WrongParentSign.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/WrongTiltDirection.lean > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/WrongTiltDirection.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/WrongTiltDirection.exit
printf "0\n" > ${LOCAL_RAW}/stratonovich-projection-residual-lean-v2/EXIT
exit 0
