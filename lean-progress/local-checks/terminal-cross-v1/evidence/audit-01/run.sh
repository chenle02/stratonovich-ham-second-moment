#!/bin/bash
set -u
export LEAN_NUM_THREADS=3
export LEAN_PATH=${LOCAL_RAW}/stratonovich-terminal-cross-lean-dev-03/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/Audit.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/Audit.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/Audit.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongPrefactor.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongPrefactor.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongPrefactor.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongRate.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongRate.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongRate.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/StrictEndpoint.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/StrictEndpoint.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/StrictEndpoint.exit
${LEAN_BIN} -j1 -D Elab.async=false ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongPolySign.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongPolySign.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/WrongPolySign.exit
export LEAN_PATH=${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/out:${DEPENDENCY_ROOT}/.lake/packages/mathlib/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/plausible/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/LeanSearchClient/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/importGraph/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/proofwidgets/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/aesop/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/Qq/.lake/build/lib/lean:${DEPENDENCY_ROOT}/.lake/packages/batteries/.lake/build/lib/lean
${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/src -o ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/out/StratonovichHAMAudit/TerminalCross.olean ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/src/StratonovichHAMAudit/TerminalCross.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/TerminalCross.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/TerminalCross.exit
${LEAN_BIN} -j1 -D Elab.async=false -R ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/src ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/src/Audit.lean > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/Audit.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-terminal-cross-lean-audit-01/replay/Audit.exit
exit 0
