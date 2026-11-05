# C native transport anomaly — bounded metadata/source audit

**Diagnosis:** native stream re-entry is evidenced independently of the duplicate stdout pattern. The available application log has two LLM.run stream invocations for the same run/session/model, but one outer prompt-loop and one processor-process entry. The pinned CLI contains a processor retry path that can produce the observed two distinct step starts and abandoned empty reasoning part. That path is a source-supported explanation, not a captured error/attempt-index record. The specific trigger, low-level HTTP-attempt count and first-attempt usage/framing remain unknown.

The original collector result MUST remain **incomplete=true**, with fresh_generation_sequence refusal. This audit does not waive that contract, repair a harness/report, approve a retry, or give a new mathematical grade. One explicit supervisor CLI invocation is consistent with native internal re-execution; automatic_retry=false in the wrapper is not proof that the CLI/SDK made only one underlying attempt.

## Independently verifiable final record

The original native directory is stratonovich-af97-unitC-main-runtime-v1-20261105/native-unitC. Its complete JSON export SHA04e46c834b16512328b4340364e528918f565c6c05db6564475925da199cc792 parses as exactly one user and one assistant in SIDses_e542af140ffeWfpX23U02ddwZ6. Session title is Stratonovich Unit C MAIN af97; CLI version1.18.31; project/cwd/root identify the held C carrier. The assistant's parentID is that actual user; both agent fields are reviewer and the observed user/assistant provider/model are deepseek/deepseek-v4-pro. There is no extra user instruction or second assistant/public assessment in the exported conversation.

The sole user TEXT part is exactly1804522 bytes/SHA26af20407ffff0df0126a9e555efd4b9b7c70555770b6130c93fdffd8afa02ab, equal to held C input. The sole completed public TEXT part is24671 bytes/SHAa7db8a136e22a1e9a79a9f52a0f957025008312942096e8e9c2acfdcf10c04eb, equal to BOTH public.raw.txt andpublic.md. It has278 logical lines/277LF and no terminalLF. These are independently checked actual public-record facts, not invented public output or private reasoning used as proof. Root's mathematical reading/claimed scoped confidence is separate from this transport audit.

Actual assistant parts are step-start,reasoning,step-start,reasoning,text,step-finish, all on the same assistant message. The two step-start IDs are different and both persist in the export with the same held tree snapshot. Thus this is not merely printing the same step-start part twice. There are no tool parts. The first reasoning part has text length0 and only a start timestamp. The second has32411UTF8 bytes and start/end timestamps. I inspected only these types/IDs/times/lengths, not the reasoning content or mathematical meaning.

The original CLI exits0 with finish=stop, elapsed788.943459978s and the wrapper records immutable_inputs_unchanged=true. Root separately reports its149-authority/source/HEAD terminal verification; this audit binds that Root-owned observation without pretending to repeat all149 checks. The collector's event sequence is step_start,step_start,text,step_finish and its strict_event_error_count is1. The exact frozen run_native.py requires a single start/text/finish sequence; its incomplete predicate therefore stays true even though the final public text and export parse successfully.

## Actual allowlisted logs, not a guessed retry from timing

I located the existing application log and selected only metadata for the exact run/session. No raw log, request/header/configuration or unknown message content was copied. The evidence sidecar binds byte offsets, lengths and line hashes, with only timestamp/level and allowlisted identifiers/stream labels retained.

The relevant positive records are:

*13:10:29.855Z: one SessionPrompt loop entry.
*13:10:30.555Z: one SessionProcessor process entry for the final assistant ID.
*13:10:30.557Z: LLM stream invocation, sameSID/deepseek/deepseek-v4-pro;13:10:30.571Z selects ai-sdk.
*13:18:06.616Z: a second LLM stream invocation with the same run/SID/provider/model;13:18:06.618Z again selects ai-sdk.

The stdout step-start timestamps are13:10:33.623Z and13:18:09.885Z, followed by completed public text/final stop. Timing is reported only as metadata. It does not establish a timeout, rate limit, lost connection or any specific provider failure. The inspected run has no captured warning/error or retry-status record. Lack of such a record in the available log is not proof that no internal error occurred elsewhere.

This log establishes at least TWO native LLM.run invocations, beyond the stdout/export pattern. It does NOT by itself count every HTTP request, prove the first request reached the provider, or identify its exact transmitted body. Both observed stream entries name the requested model; no model fallback is evidenced. No server/API trace or account probe was obtained.

## Pinned source mechanism and its limits

CLI SHA is the actual f9dab32248695e9ebd56b16a1921798fd85112cf5a69c7dfd0cabc1e17be4a11. Bounded exact public-code excerpts and offsets are retained in pinned-source-evidence.json:

*At byte96726162, the unique LLM.run stream-log site executes before Qo.prepare. Repeated entries therefore evidence re-entering this native LLM service, not merely a repeated frontend update. The surrounding stream adapter calls LLM.run and adapts its full stream; it is not itself a log-printing loop.
*SessionProcessor.process logs process outside its inner streamed effect. Inside that effect it resets currentText/reasoningMap, then executes stream(c), wrapped in native retry(policy). Its retry handler sets a separate session.status record; that is distinct from a terminal session.error.
*On EACH received step-start it persists a NEW part ID on the current assistant. Reasoning-start persists an empty part; reasoning-delta appends text and reasoning-end closes it. Resetting the map on re-execution can leave an earlier stored empty/start-only part unclosed, while the eventual current reasoning part is completed.
*CLI JSON stdout forwards message.part.updated step-start/finish and completed text. It does not forward a non-idle session.status retry as its own JSON event. Absence of a retry event in these four stdout lines therefore cannot exclude the source retry path.
*At step-finish, assistantMessage.tokens is ASSIGNED from that step's usage. It is not an all-failed-attempt accumulation. The SDK call also exposes an optional retries parameter with a default0, but no per-attempt request trace proves all effective lower-level behavior in this run.

With one process/loop entry and two LLM.run entries, processor-level retry/re-execution is strongly source-supported. A direct recorded retry status/attempt index/error is absent, so I do not promote that explanation to a verified trigger or exact attempt accounting. Another unlogged native/adapter mechanism cannot be excluded solely from the public export. The empty reasoning part is compatible with reset/re-entry, but is not proof that the backend did zero work.

## Final usage versus unknown abandoned-attempt usage

The final assistant and final step-finish agree on:

 input1 + cache.read517376 + cache.write0 =517377 final full input;
 public8393 + reasoning11897 =20290 final combined output;
 final reported total=537667.

That final full input is within the Root-bound517809 request component; final combined output is below131072. Those inequalities apply to the recorded COMPLETED step. They do not establish the first stream's input/cache/reasoning/output/charge, nor an aggregate all-attempt FULLTURN. The original field name actual_FULLTURN537667 remains untouched and must be read with this abandoned-attempt limitation. No first step-finish/usage record exists in the export. A zero-byte first reasoning part cannot substitute for one, and the final cache-read count does not recover its source or amount.

Source retry uses the processor's input c again, supporting continuity of the requested task. The final exported user/agent/model/root identities are exact. Nevertheless there is no independently captured first transmitted prompt/system/framing or response usage. Held source/carrier/context facts and the final accepted input do not turn that missing per-attempt evidence into a direct measurement. I neither assume a framing/cap violation nor certify a first-attempt budget that was not observed. No token count is inferred from private reasoning text.

## Disposition boundary

The final completed assistant/public record is real, unique and independently bound to the held C input and requested observed route; it can be inspected as that immutable actual public evidence. It is NOT a clean pass of the frozen single-start transport contract and is not a second independent vote. Its mathematics, confidence and scope still require Root adjudication. Internal native re-entry and unknown first-attempt facts remain attached to any use of that record.

No source or mathematical counterexample is asserted by this operational anomaly. No original file, collector flag, native public text, eligibility rule, harness or authority was changed. No new export/CLI/model/API/account call, supplement, automatic retry, patch or protocol is proposed. The existing C fence remains spent; Root's original incomplete record and all unknowns are preserved. Only this new external bounded audit data was written. The final readback rehashes original native/code inputs; it supplies no run or scientific acceptance authority.
