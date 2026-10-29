#!/bin/bash
set -u
cd .
<HOME>/.local/bin/uv run --with mpmath python ./reviews/2026-10-29-interaction-driver/checks.py > ${LOCAL_RAW}/stratonovich-interaction-driver-numerics-v1/driver.txt 2>&1
rc=$?
printf "%s\n" "$rc" > ${LOCAL_RAW}/stratonovich-interaction-driver-numerics-v1/EXIT
exit "$rc"
