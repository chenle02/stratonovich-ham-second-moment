# Source-read ledger v2: bounded immutable-source authentication repair

The v1 standalone collector's leaf authority was incomplete: it checked the frozen DATA manifest file hash, but then trusted mutable plan rows and a mutable independent-minimum file without authenticating their manifest membership. A consistent plan/packet/workspace change could satisfy those old source-binding conditions. This is a verifier provenance defect, not evidence that any actual source or reading was wrong. Root separately verified the actual originals.

V1's complete40-member directory and manifest0a0d5fd1548ba1528773bd90583df4939ec4d354e0ee6b95632fc15daeffcead remain byte-identical. This separate v2 directory contains only the bounded authentication successor and new safe snapshots. No live packet, workspace, session, plan, native report, grade or Root authority was modified.

## Exact authority chain

1. Authenticate original constructor DATA manifest479e8a3e… . From its immutable member table, authenticate required-text-ranges-and-roles.json as EXACT52044bytes/SHA883f3249ee2fa338ca4dbc7eeb573a5473135acfdc4b10814a077f5f7c5af9a9 before using any rowSHA/range/path.
2. Authenticate the independent DATA-audit manifestc1dfad7b632a063f09cf54e88584b0191580ea0111efd71b49fb08f57c7e56eb and its independent-minimum.json member, EXACT27572bytes/SHAa83695a775bb828e02361f09e7d70fa18115f987718657fcb4cb17da82b03878, before trusting its scientific required set.
3. Require the original64 paths to equal that immutable independent minimum. Authenticate each packet/<required-path> directly by its immutable DATA-manifest member length/hash, also requiring the original plan row to match that same member.
4. Compare each actual workspace leaf byte-for-byte to that authenticated frozen packet leaf. source-authority.json records every64member identity and exact original plan/minimum binding.

Manifest member paths/duplicates/lengths/hashes are checked. None of the source-data manifests is regenerated or treated as self-approving mutable metadata. The original4677primary range and every full-file role remain unchanged.

## Consistent mutation controls

Six in-memory controls preserve the ORIGINAL manifest JSON while changing coherent lower-level data. The relevant v1 source-binding conditions were reproduced as accepting (a) a changed plan row plus packet/workspace leaf and (b) a mutually consistent64-path minimum/plan replacement that demotes a needed white proof to available metadata. V2 refuses both before event-ledger interpretation. Additional controls refuse packet+workspace change with unchanged plan, workspace-only change, minimum-only change and a changed independent manifest JSON. No actual source/minimum/plan/manifest was changed by the tests.

AST comparison verifies that only existing main changed to call the new authentication boundary and save its authority evidence. The only new functions are manifest_members,authenticated_inputs,authority_controls. Every existing LF model, numbered-Read parser, FF/byte bijection, event-prefix capture/privacy filter, text ledger, image-pending logic and exact source/FF controls is AST-identical to v1. No format, scientific acceptance, confidence or image rule was broadened.

## New safe evidence snapshot

Snapshot preterminal-v2-20261106T195627956331Z binds5,587,407bytes of a stable complete event prefix,82public tool calls/results. All64actual LF text contents are now present. Images remain PENDING separate actual pixel evidence; their presence in a tool-call list does not grant delivery/semantic credit.

The primary direct return still reconstructs exactly284666bytes/SHA5a6eff…29a2, including64FFand4614LFrows. The original4677LFendpoint is STILL refused, with undefined4615–4677recorded in its separate strict-original-coordinate-refusal.json. The independent contiguous4677virtual-segment byte bijection still explains complete original source delivery as separate evidence, with Root adjudication pending. No numeric range was clipped, repaired, waived or relabelled passed. The prior11FF/source/mapping/transport controls remain unchanged and pass.

All retained custody remains exact needed tool returns, minimal calls and allowlisted public metadata only; private assistant content/reasoning is neither accessed nor persisted. There was no model, native CLI, restart, doctor, Lean, Git or network call. The original source reading and frozen packet remain intact.

Reproduce into another new timestamped snapshot here:

    PYTHONDONTWRITEBYTECODE=1 python3 check_reads.py --label later-readback-v2

This is a transparent engineering successor, not a scientific/source defect claim or report regrade. Root remains responsible for final native monitoring, coordinate adjudication, actual17pixel checking and scientific findings.
