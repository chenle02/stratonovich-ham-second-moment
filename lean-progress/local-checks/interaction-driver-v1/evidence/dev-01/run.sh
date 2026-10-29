#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/compile-time.txt ${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/src -o ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/out/StratonovichHAMAudit/InteractionDriver.olean ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/src/StratonovichHAMAudit/InteractionDriver.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/compile.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/compile.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/Audit.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/compile-audit.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/compile-audit.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
export LEAN_PATH=${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
/usr/bin/time -v -o ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay-time.txt ${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay/src -o ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay/out/StratonovichHAMAudit/InteractionDriver.olean ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay/src/StratonovichHAMAudit/InteractionDriver.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/Audit.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay-audit.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/replay-audit.exit
if [ "$rc" -ne 0 ]; then exit "$rc"; fi
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/WrongHolderThreshold.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/WrongHolderThreshold.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/WrongHolderThreshold.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/MissingSpatialCount.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/MissingSpatialCount.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/MissingSpatialCount.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/WrongGaussianExponent.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/WrongGaussianExponent.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/WrongGaussianExponent.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/NegativeLogFactor.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/NegativeLogFactor.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/NegativeLogFactor.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/MissingGaussianNormalization.lean > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/MissingGaussianNormalization.txt 2>&1
rc=$?; printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/MissingGaussianNormalization.exit
printf "0\n" > ${LOCAL_RAW}/stratonovich-interaction-driver-lean-v1/EXIT
exit 0
