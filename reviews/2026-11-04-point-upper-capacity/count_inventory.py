#!/usr/bin/env python3
"""Local public-tokenizer audit; no provider/config/carrier mutations."""
import ast
import hashlib
import json
from pathlib import Path
import sys
import tokenizers

OUT = Path(__file__).resolve().parent
STATE = OUT.parent
inventory_root = Path(sys.argv[1])
source = inventory_root / 'build_inventory.py'
code = source.read_bytes()
tree = ast.parse(code)
prefix = []
for node in tree.body:
  if isinstance(node, ast.FunctionDef) and node.name == 'js':
    continue
  if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
      and isinstance(node.value.func, ast.Name) and node.value.func.id == 'js'):
    break
  prefix.append(node)
else:
  raise AssertionError('No explicit writer boundary found')
module = ast.Module(body=prefix, type_ignores=[])
for node in ast.walk(module):
  if isinstance(node, ast.Call):
    func = node.func
    name = func.attr if isinstance(func, ast.Attribute) else func.id if isinstance(func, ast.Name) else ''
    assert name not in {'js','write_text','write_bytes','mkdir','open','unlink','rename','replace','system','run','Popen','urlopen'}, name
env = {'__file__': str(source), '__name__': 'READ_ONLY_NO_WRITERS'}
exec(compile(module, str(source), 'exec'), env)
saved = json.loads((inventory_root / 'complete-capacity-inventory.json').read_text())
assert env['inventory'] == saved
prompt = bytes(env['prompt'])
assert hashlib.sha256(prompt).hexdigest() == saved['prospective_prompt_sha256']

tokenizer_file = OUT / 'DeepSeek-V4-Pro/tokenizer.json'
raw = tokenizer_file.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '8f9f37ca37fdc4f5fd36d5cf4d3b0e8392edb4e894fd10cc0d70b4957c8633cf'
spec = json.loads(raw)
added_count = len(spec['added_tokens'])
spec['added_tokens'] = []
tok = tokenizers.Tokenizer.from_str(json.dumps(spec))
tok.no_truncation()
tok.no_padding()
def count(b):
  return len(tok.encode(b.decode('utf-8'), add_special_tokens=False).ids)

messages = env['ex']['messages']
text = [ ''.join(p['text'] for p in m['parts'] if p.get('type') == 'text').encode() for m in messages ]
assert text[0] == env['oldprompt']
original = json.loads((STATE / 'stratonovich-af97-intrinsic-core-packet-v2/native/collection.json').read_text())
native_original_input = original['usage']['input'] + original['usage']['cache']['read']
historical = {
  'original_user_plain_tokens': count(text[0]),
  'original_actual_full_input': native_original_input,
  'factual_first_three_messages_plain_tokens': sum(count(t) for t in text[:3]),
  'factual_actual_full_input': saved['baseline_input_including_cache'],
  'factual_last_public_plain_tokens': count(text[3]),
  'factual_actual_public_output': saved['last_public_output'],
}
historical['original_native_minus_plain'] = native_original_input - historical['original_user_plain_tokens']
historical['factual_native_minus_plain'] = historical['factual_actual_full_input'] - historical['factual_first_three_messages_plain_tokens']
overhead = max(0,historical['original_native_minus_plain'],historical['factual_native_minus_plain'])
candidate = count(prompt)
extra = sum(count(env['enc'](env[k])) for k in ['config','agent','runtime']) + count(env['agenttext'].encode())
guard = saved['newcharges']['actual_future_guard_runtime_UTF8_allowance']
total = candidate + overhead + extra + guard + saved['combined_output'] + saved['boundary'] + saved['system']
result = {
  'status': 'LOCAL_OFFICIAL_TEXT_TOKENIZER_CONDITIONAL_PLAN_NOT_NATIVE_ADMISSION',
  'inventory_root_name': inventory_root.name,
  'inventory_sha256': hashlib.sha256((inventory_root/'complete-capacity-inventory.json').read_bytes()).hexdigest(),
  'producer_script_sha256': hashlib.sha256(code).hexdigest(),
  'tokenizers_python_version': tokenizers.__version__,
  'tokenizer_sha256': hashlib.sha256(raw).hexdigest(),
  'plaintext_special_token_handling': 'added_tokens removed in memory; no special-token interpretation of user content; no truncation/padding/automatic BOS/EOS',
  'removed_added_vocabulary_entries': added_count,
  'historical_actual_comparison': historical,
  'candidate_prompt_bytes': len(prompt),
  'candidate_prompt_sha256': hashlib.sha256(prompt).hexdigest(),
  'candidate_plain_text_tokens': candidate,
  'conservative_measured_historical_overhead': overhead,
  'entire_new_config_agent_runtime_and_agenttext_extra_tokens': extra,
  'full_future_guard_UTF8_allowance': guard,
  'combined_reasoning_public_output_reserved': saved['combined_output'],
  'boundary_reserved': saved['boundary'],
  'system_reserved': saved['system'],
  'conditional_total': total,
  'context': saved['context'],
  'conditional_headroom': saved['context'] - total,
  'all_source_mathematics_retained': True,
  'native_provider_or_account_probe': False,
  'producer_or_carrier_or_config_mutations': False,
  'caveat': 'Exact count for these text bytes with the pinned public tokenizer. Actual provider alias/template/system may differ. Historical native discrepancies and all prior output/boundary/system/future-runtime reserves are retained. Not a scientific depth or confidence certificate.'
}
path = OUT / (inventory_root.name + '-local-tokenizer-count.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
