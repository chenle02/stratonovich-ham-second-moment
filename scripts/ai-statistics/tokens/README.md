# Token and cost totals for Appendix E

`token_totals.py` reads three local log stores on the worker machine
(read-only) and writes totals only, with no paths, prompts or message text, to
`token-totals.json`. The logs themselves are not in the repository, so this
snapshot is the record; the script documents exactly how it was made.

    python3 scripts/ai-statistics/tokens/token_totals.py

What is counted: this repository and its subfolders, and its review
workspaces under `~/.local/state/Le-AI-Lab/stratonovich-*` and
`~/.local/state/tmp/stratonovich-*`. The separate Lean-companion and video
projects are not counted.

Snapshot (see `snapshot_utc` in the JSON):

- Codex worker (GPT family): 52 sessions, 2026-10-27 to 2026-11-11 UTC;
  about 10.98 billion input tokens (98.7% read from cache), 36.1 million
  output tokens (21.7 million of them reasoning). Model per session is the
  last one named in it (gpt-6-astra 32, gpt-6.1-sol 20).
- Claude Code (Opus 5.5): about 5,350 API calls, 10.2 million output tokens,
  1.36 billion cache reads. Includes coordination and editing sessions as
  well as reviews; the logs keep a rolling window.
- OpenCode, DeepSeek V4 Pro: 122 sessions, 55.5 million input, 171.7 million
  cache reads, 1.41 million output, 3.84 million reasoning tokens; cost
  $50.83 as computed by OpenCode.

Codex, Claude and Kimi were used on subscriptions, so no dollar figure
exists for them. Kimi token counts were not recorded. These numbers agree
with an independent one-pass parse by a read-only subagent (Codex sessions
and tokens, DeepSeek sessions and cost identical).
