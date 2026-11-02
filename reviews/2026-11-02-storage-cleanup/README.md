# Storage cleanup and candidate recovery

Two duplicate local checkouts and their merged-tip branches were removed.
The clean retired production clone and merged remote branch were removed
on <HUB>. The production tip remains an ancestor of the active branch.
Only master and the active research branch remain locally.

The temporary review branch had no unique commits. Its three edited TeX
files, rebuilt263-page PDF, complete binary patch, index intent and build
logs are preserved in candidate-wip-recovery.tar.gz, independently rehashed.
The same exact files remain in external stratonovich-cleanup-rescue-20261102;
full frozen source candidate v2 and its98-member capsule remain intact.
Use the exact base and manifest to restore a minimal review checkout or
create a source-only review carrier. Do not recreate a full duplicate
checkout solely to review these six proof changes.

The unreviewed candidate is not production source. ACTIVE's scientific
source remainsb4b6efc. All native reviews remain terminal; no new provider
call occurred. Git was compacted with --no-prune and connectivity passed.
