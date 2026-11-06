# Independent audit of actual constructor image delivery and Root v1 checker

Actual snapshot delivery: PASS — all17required source/candidate PNGs are byte-identical and wholeRGBA-identical to the frozen originals. Actual calls are all assistant/function, unique, correctly paired and request full_resolution=true. This is delivery/fidelity evidence only, not attention, mathematical correctness, source-print clarity, confidence or acceptance.

Standalone Root v1 verifier: one bounded role/type provenance repair is needed before future standalone use. The actual frozen data is correct; the malformed cases below exist ONLY in owned sanitized public-tool fixtures. Root's checker/snapshot remain unchanged, and no native restart/source failure is inferred.

## Exact inputs and recomputation

Reviewed frozen check_images.py SHA8a2de934f5e2003fedb13f61d23fd4603cea5b8edd9ba13a694fc882db82bdde and snapshot-20261106T200023017085Z. Root confirmed both frozen before this audit. Both snapshot files and checker were hashed before/after with no change.

The immutable DATA manifest479e8a3e… authenticates the pixel-plan leaf and each original PNG leaf; original row lengths/hashes and actual workspace images agree. Independent audit manifestc1dfad7b… authenticates its minimum leaf; its17pixel set exactly equals the image plan. Thus a mutable plan plus mutable PNG/workspace cannot silently replace the original selected images.

The actual saved event prefix5,953,354bytes/SHA68b9949e05cecf1542fbcec4663eb624a0d16525206df484ff3b59064d10afd4 was independently reread and matched to the frozen snapshot. Only public call fields and role=tool returns were accessed; assistant content/reasoning fields were not read or retained. All17actual media call envelopes are roleassistant/typefunction, with exact native call keys{id,type,function}; each function has{name,arguments}. All paths resolve inside the existing workspace and cover precisely the17required paths once each.

Every paired media return has the actual native three-block schema [text,image_url.imageUrl.url,text]. Its data URI is exactly PNG/base64; strict base64 decoding reproduces the ENTIRE frozen original PNG bytes, not merely a reencoded/cropped region. PIL independently loads actualPNG format/dimensions and verifies wholeRGBA pixels. All17row sizes/hashes/call-event hashes/return offsets match Root's saved result. The exact concatenated public-tool result JSON lines match Root's tool-only custody file. This is stronger than the prior three-image clipped-region/full-pixel-union primitive, but it establishes only this actual17-image delivery.

The executed frozen Root source uses literal LF for events. Its earlier unexecuted splitlines draft is not treated as an executed failure or as evidence against current results. No source/packet/live stream was edited, and no final terminal status is inferred while exec12071is still Root-monitored.

## Pure controls and precise v1 guard gap

The unchanged Root verify_return helper was source-byte loaded and applied to all17actual public returns. Eleven additional helper controls refuse false/nonboolean full-resolution flags, metadata-only claims, duplicate image blocks, malformed base64, wrong MIME, altered PNG bytes, a cross-image source and an unexpected region argument. Aggregate fixtures refuse a missing required image, cross-image content and a changed frozen plan leaf.

The Root main extraction loop, however, consumes any row.tool_calls with function.name ReadMediaFile without checking that the calling row role is assistant or that call.type is function. In NEW owned public-only fixtures, the real call IDs/arguments/results were sanitized into minimal events with no assistant content/reasoning. The positive fixture passes. Changing ONLY the first call row's role to meta still passes17images; changing ONLY its call.type to not-function also passes17images. These are reproducible prospective provenance false positives. They do not falsify the actual snapshot, whose17call roles/types were independently checked correct.

Root agreed to a separate bounded v2 adding role/type guards and controls, preserving frozen v1. This audit does not modify Root code or approve that successor sight unseen. No broad format, schema, scientific or confidence change is needed to fix this specific engineering gap.

## Isolation, privacy and scope

All process/shell/exec/spawn/fork routes were denied. Root main was invoked ONLY with in-memory sanitized event fixtures and its output HERE rebound to a new owned directory; actual event reads were intercepted by BytesIO, and all writes were confined to this independent audit directory. The real frozen source PNGs were read only. Original Root checker/snapshot, source packet, actual workspace and native session remained unchanged. No model, native/export/config/doctor, Git, Lean or network action occurred. No private assistant content/reasoning was accessed or retained, and fixture outputs are clearly labelled not actual native data.

The actual seventeen-image byte/pixel PASS remains valid with the independently strengthened role/type checks. It does not interpret G(t,x), repair a source display, certify a constructor proof, upgrade old calibration/report confidence, grant full267-page visual clearance or complete the research goal. Root retains separate final transport, scientific adjudication and any future verifier-use decisions.

Artifacts: result.json records17independent actual rows, helper/aggregate refusals and the two isolated false positives; audit.py reproduces with a NEW empty audit output root. Owned fixture result files preserve the injected-meta/type findings separately. Input pins in result.json bind the exact frozen Root inputs.
