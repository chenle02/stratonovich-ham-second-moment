# Decision: native recovery or strict one-attempt hold

**Proposal only; no model calls are authorized by this file.**

The installed approved OpenCode route has a hardcoded native SessionRetry
policy that cannot be disabled per run. It caused the three recorded replay
incidents; earlier-stream usage and aggregate cost/cap remain unknown. A
corrected custom one-shot client is still being prepared and has not passed
its offline code review or been approved for live use.

Two concrete choices remain:

1. Keep the strict single-provider-attempt requirement and keep new calls
   held until the corrected one-shot client and its exact route/scope are
   reviewed and approved. No live client change is implied by this choice.
2. Explicitly amend the native execution plan prospectively: use the SAME
   configured DeepSeek V4Pro route/profile/scientific inputs for the remaining
   21 frozen scopes (153 proof pairs), maximum3 simultaneous processes,
   one process per scope and3,600seconds per process. Native transport
   recovery is knowingly allowed under the installed policy; aggregate
   usage/cost/cap may remainunknown and will be disclosed rather thanestimated.
   Per-generation caps stay65,536 ordinary/98,304 main. There are no
   coordinator relaunches, confidence-based retries, tools or fallback.
   This choice also explicitly permits ONE separate budget-repair process for
   the failedRP007 scaling proof, same exact source/prompt,98,304 per generation.
   Its old failure remains; no aggregate131,072-token guarantee is claimed
   when native recovery is allowed. No further repeat is authorized.

SCOPE.json names every remaining source/prompt/profile/cap. Choice2 changes
execution policy, not mathematical scope or requested model. It does not
retroactively accept the three old protocol incidents, complete the three
partial mathematical reconstructions, upgrade any grade, or authorize R/F,
push, public release or arXiv. The prior PU exception is not automatically
extended. The existing hold remains unless the user explicitly chooses2.
