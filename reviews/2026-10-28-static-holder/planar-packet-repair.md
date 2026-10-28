# Post-hook packet repair

No reviewer was dispatched against the preparation at56aa356. Its pre-commit
formatter rewrote60line-leading indentations after source/PDF hashes were
recorded. The commit was already pushed when the mismatch was caught; it
remains immutable history, not an accepted freeze. Earlier worker checks were
true for their recorded pre-hook source, not the post-hook commit.

The exact pre-hook source326e1508 was recovered from its staged Git blob
6cb9c4f2250496f0e4d4d70e5b7daa77d5d0848e and retained losslessly as
pre-hook-source.tex.gz. Every line is identical after stripping leading ASCII
spaces; no internal character, mathematical token or line count changed.
No verbatim/space-catcode construct exists in these notes. The actual
post-hook source was rebuilt with the canonical command; all required gates
pass and the complete extracted PDF text is byte-identical to the pre-hook PDF.
See hook-source-change.json and post-hook-binding.json for exact hashes.

The original byte-preservation statement applies to the worker-delivered
source. Current canonical source preserves all prior content up to the
recorded leading-indent normalization; it is not literally byte-identical.
This correction is explicit rather than retroactively rewriting worker evidence.

Use planar-packet-v2 and planar-replay-packet-v2 only. TeX reading excerpts are
now plain text snapshots with exact canonical line/byte bindings, so a source
formatter cannot rewrite them as if they were editable compilation units.
The full canonical TeX is already formatter-idempotent and the rebuilt PDF
is included. Raw pinned source PDFs are available for optional page checks.
All committed packet bytes must pass the manifest check before any dispatch.
No hook, global configuration or acceptance threshold was changed or bypassed.
