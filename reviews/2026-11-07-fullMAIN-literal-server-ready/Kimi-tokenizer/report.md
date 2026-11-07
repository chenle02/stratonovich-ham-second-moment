# Public K3 tokenizer evidence — conditional capacity, no dispatch authority

The official MoonshotAI Kimi-K3 repository provides a usable offline tokenizer at commit `f831ab66814297da540d832a5235f8e904f29d06`. This is new positive evidence for conditional K3 counting, comparable in status to an official openweight counter plus declared framing allowance. It is not proof of deployed managed-OAuth tokenizer equality.

## Vendor/model binding

The actual historical native requests declare model alias `kimi-code/k3`, outgoing model `k3`, OpenAI protocol and max effort. The official Kimi Code subscription documentation lists `k3` among its accepted model IDs. The official K3 model README recommends Kimi Code's K3 selection, but names the separately hosted platform API model `kimi-k3`. These establish vendor/product/model-family correspondence. No inspected official document binds the managed subscription deployment to this HF commit, tokenizer hash, server template revision or unchanged vocabulary. This remaining distinction should be labeled conditional, not treated as an absolute-proof standard different from DeepSeek.

Sources: [official pinned tokenizer](https://huggingface.co/moonshotai/Kimi-K3/tree/f831ab66814297da540d832a5235f8e904f29d06), [official subscription API overview](https://www.kimi.com/code/docs/en/), [official model README](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/README.md).

## Actual offline results

The rank file contains 163584 mergeable tokens and every one-byte value. Its ordinary-text byte BPE therefore has token count at most UTF8 byte count: initialization uses bytes, and merges reduce their number. Protective text splitting preserves that inequality. This proves a bound for this pinned encoding, not for undocumented provider preprocessing. It does not bound arbitrary tools/chat wrappers, nor prove a 65536-token native next-Read guarantee.

Using the exact AST-extracted official regex, pinned ranks and already cached tiktoken (no remote code execution):

- All 222 required whole target payloads: **1836006 ordinary tokens**, sum of individually encoded full files.
- Root's unchanged 83 whole fresh targets: **573316 ordinary tokens**, same method.
- Actual 74 historical Read outputs: **660518 ordinary tokens**; including native notes: **664222**.
- Largest actual single output plus note: **33804** conditional tokens. Historical maximum does not certify future reads.

No fields, characters or source bodies were removed. The totals exclude chat framing and are not full-input admission counts. The complete cumulative corpus cannot fit one 737280-token request under this conditional encoding; the 83-source sum alone leaves 163964 before other context/framing. Staging/compaction still needs charged genuine synthesis and preserved source debt. No new source selection or provider authority follows.

## Historical 35-request calibration

`conditional-counts.json` compares all 35 measured cache-inclusive inputs to accumulated actual public Read text. At final request measured input is 681572, versus 664222 conditional Read-text tokens, difference 17350. This is consistent with a close practical tokenizer lead but cannot identify tokenizer equality: the difference also contains system/tools, user messages, assistant history and formatting.

Root additionally authorized counting private assistant strings strictly opaquely. `opaque-calibration35.json` counts every recoverable archived message component, system string and tool schema without emitting/interpreting their contents. Native request metadata does not contain serialized HTTP messages. Agent-message records flush late; request message counts select archived chronological prefixes and separately recorded extra user context. The diagnostic canonical JSON is explicitly not native serialization. The exact missing layer is native typed-message conversion plus deployed server chat preprocessing/template and revision. At the last request the opaque string-value sum is **675995**, against measured **681572** (difference **5577**). Across all35, the measured-minus-string-sum range is **671 to 5577**. Canonical JSON instead counts748581 at the last request: its escaping/syntax overhead makes clear why JSON serialization is not the provider template. Thus calibration is evidence, not an exact error margin or guaranteed future allowance.

## Counting controls and API boundary

Official Kimi Code configuration documentation explicitly distinguishes displayed `token_counting` strategy from internal compaction/budget/overflow logic, which continues using measured usage plus estimates. Selecting `measured` is not a pre-request counter. [Official configuration reference](https://moonshotai.github.io/kimi-code/en/configuration/config-files).

The inspected official subscription overview documents Messages/Chat/Responses compatibility, but supplies no inspected `messages/count_tokens` endpoint contract, subscription entitlement or OAuth permission for it. Official-site searches did not produce such documentation. Anthropic compatibility alone does not prove endpoint support; third-party proxy claims are not used. This report does not conclude the endpoint is absent. No count endpoint, authentication, provider/native request, global configuration, credential or model operation was attempted.

## Reproduction and limits

`count_public.py` and `calibrate_opaque.py` use only local pinned sources and the existing cached Python3.14/tiktoken. No Transformers remote code was executed. `encoding_k3.py` is retained as public source: it renders XTML segments, marks user/tool text ordinary, and separates structural special tokens. The README requires preserved thinking history; tool0 delivery cannot simply discard it when assessing later requests.

The smallest next action is Root's explicit conditional policy decision: whether this official K3 family binding, calibration and conservative charged framing are sufficient for a bounded route, with actual every-request usage checked and overflows refused. An exact deployed-tokenizer claim or future native next-tool guarantee remains unsupported. Existing 311296 allowance, original 222 cumulative targets, Root83 fresh policy, 215 proofs/241 roles/13 joins, and all source debts remain unchanged.
