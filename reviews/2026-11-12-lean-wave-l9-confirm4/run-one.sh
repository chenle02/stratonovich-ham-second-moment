#!/bin/bash
# run one wave-L9 re-confirmation review; retry once only if the attempt did not complete as a review (tool failure)
d=$1; LC=e2c50b55cc6faf63e9da85391608fb3e4c93b293
for a in 01 02; do
  echo "$(date -u +%FT%TZ) start attempt-$a" >> $d/driver.log
  CODEX_HOME=$d/codex-home subscription-review-cli run codex --model gpt-6.1-sol --effort high \
    --packet $d/packet --target candidate/statement-ledger.md --prompt-file $d/contract.txt \
    --source-revision $LC --out $d/attempt-$a --min-confidence high --timeout 10800 > $d/run-$a.log 2>&1
  rc=$?
  st=$(grep -m1 '^Status:' $d/attempt-$a/STATUS.md 2>/dev/null)
  echo "$(date -u +%FT%TZ) attempt-$a exit=$rc $st" >> $d/driver.log
  case "$st" in *review-complete*) break;; esac
  [ $a = 02 ] || echo "$(date -u +%FT%TZ) attempt-$a TOOL FAILURE (not review-complete); retrying once" >> $d/driver.log
done
echo "$(date -u +%FT%TZ) done" >> $d/driver.log
