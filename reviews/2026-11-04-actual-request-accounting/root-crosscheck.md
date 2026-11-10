# Root independent request-accounting cross-check

Root read the actual closed B21 native driver and the new accounting program,
without executing either. Independently rechecked the exact exported single
user text against the prompt, native collection/export usage, current CLI
binary identity and every bounded source-code excerpt, private program hashes
and their absence from both the user text and effective agent prompt.

The inspected driver passes only prompt bytes through stdin to the native run.
The request preparation code uses the effective agent prompt and prepared
messages, and selects tool definitions separately. The local guard, preflight,
run supervisor and projection programs are not explicit message payloads in
this inspected path. Their private code-byte charge is not a measured model
input. Full configuration JSON objects likewise are not forwarded wholesale;
the agent prompt is model-visible and options/tool transformations still count
where actually delivered. The prior export records 824374 input tokens with
zero cache, versus 823859 public-tokenizer plain tokens: a net difference of
515. That observation is historical and does not guarantee future overhead.

No exact final HTTP-body capture is present. This cross-check does not infer
that every builtin system/tool transformation is absent, select a future
allowance, remove an inherited floor, lower any hard reserve, or certify a
new request fits. Complete readable mathematical retention and actual future
request construction/counting remain necessary before any new review.
