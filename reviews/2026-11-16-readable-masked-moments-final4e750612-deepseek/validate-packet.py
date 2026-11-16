from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((p/'MANIFEST.json').read_text());raw=(p/'INPUT.txt').read_bytes()
assert sha(raw)==m['prompt_sha256'] and len(raw)==m['prompt_bytes']
spec=json.loads((p/'PACKET-SPEC.json').read_text());capacity=json.loads((p/'CAPACITY.json').read_text())
assert m['combined_reasoning_public_output_cap']==spec['combined_reasoning_public_output_cap']==capacity['combined_reasoning_public_cap']>=65536
assert capacity['conditional_total']==capacity['framed_prompt_tokens_under_retained_tokenizer']+capacity['agent_prompt_tokens']+capacity['combined_reasoning_public_cap']+capacity['conditional_runtime_reserve']
assert capacity['conditional_headroom']==capacity['advertised_context']-capacity['conditional_total']>0
for f,fr in zip(m['input_files'],m['embedded_frames']):
 data=(p/f['path']).read_bytes();offset=fr['payload_byte_offset'];assert raw[offset:offset+len(data)]==data
 assert sha(data)==f['sha256']==fr['payload_sha256'];assert len(data)==f['bytes']==fr['payload_bytes']
 name=Path(f['path']).name;assert raw[:offset].endswith(b'===== RAW UTF8 SOURCE =====\n')
 assert raw[offset+len(data):].startswith(('\n===== END '+name+' =====\n\n').encode())
for f in p.rglob('*'):
 if f.is_file():assert bytes([47,104,111,109,101,47]) not in f.read_bytes(),f
assert not any((p/name).exists() for name in ['LAUNCH.json','SAFE-PREFLIGHT.json','EXIT.json','PUBLIC-REPORT.md','LAUNCH-ONCE.lock','native-events.jsonl'])
checks=json.loads((p/'PREPARATION-CHECKS.json').read_text())
checks.update(second_pass_raw_frame_header_endmarkers=True,serialized_absolute_machine_paths_absent=True,launch_runtime_files_absent=True)
(p/'PREPARATION-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
m['preparation_checks_sha256']=sha((p/'PREPARATION-CHECKS.json').read_bytes())
m['validation_script_sha256']=sha(Path(__file__).read_bytes())
(p/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n')
entries=[]
for f in sorted(p.rglob('*')):
 if f.is_file() and f.name!='SHA256SUMS':entries.append(sha(f.read_bytes())+'  '+str(f.relative_to(p)))
(p/'SHA256SUMS').write_text('\n'.join(entries)+'\n')
print(json.dumps({'offline_structural_validation':True,'frames':len(m['embedded_frames']),'files_hashed':len(entries),'input_sha256':sha(raw),'manifest_sha256':sha((p/'MANIFEST.json').read_bytes()),'checksum_manifest_sha256':sha((p/'SHA256SUMS').read_bytes()),'provider_calls':0,'preflight_performed':False,'launch_performed':False},indent=2))
