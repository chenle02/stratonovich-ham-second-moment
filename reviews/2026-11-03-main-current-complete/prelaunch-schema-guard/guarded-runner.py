from pathlib import Path
import datetime, hashlib, json, os, subprocess, time

base = Path(__file__).resolve().parent
carrier = base / 'carrier'
native = base / 'native'
frozen = json.loads((base / 'carrier-freeze.json').read_text())
sha = lambda b: hashlib.sha256(b).hexdigest()
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
assert frozen['root_explicit_one_invocation_authorization'] is True
assert not native.exists(), 'An immutable native attempt already exists; no automatic retry.'
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=carrier, text=True).strip()
assert head == frozen['carrier_head']
assert subprocess.check_output(['git', 'status', '--porcelain'], cwd=carrier) == b''
for name, expected in frozen['files'].items():
  assert sha((carrier / name).read_bytes()) == expected, name
prompt = (base / 'proposed-prompt.txt').read_bytes()
assert sha(prompt) == frozen['prompt_sha256'] == 'df702b5118887c1bd9b2420e0c35259d664620f7ceda14effa92a54c42f90916'
agent = json.loads((base / 'agent-preflight.json').read_text())
assert agent['model'] == {'providerID': 'deepseek', 'modelID': 'deepseek-v4-pro'}
assert agent['tools'] and all(v is False for v in agent['tools'].values())
native.mkdir()
(native / 'prompt.txt').write_bytes(prompt)
argv = ['<HOME>/.opencode/bin/opencode', 'run', '--pure', '--dir', str(carrier), '--agent', 'reviewer', '--model', 'deepseek/deepseek-v4-pro', '--format', 'json']
env = os.environ.copy()
env['OPENCODE_PERMISSION'] = '{"*":"deny"}'
env['OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX'] = '131072'
launch = {'started_utc': now(), 'argv': argv, 'source_commit': frozen['source_commit'], 'carrier_head': head, 'initial_carrier_clean': True, 'model_requested': 'deepseek/deepseek-v4-pro', 'category': 'paper-review-deepseek', 'prompt_sha256': sha(prompt), 'prompt_bytes': len(prompt), 'task_local_config_sha256': frozen['config_sha256'], 'permission_env': env['OPENCODE_PERMISSION'], 'output_token_budget': 131072, 'prior_project_reports_supplied': False, 'confidence_requested': True, 'is_cold_read': False, 'automatic_retry': False, 'automatic_continuation': False, 'scope': 'Fresh whole-current MAIN214ownproofs240statements28TeX at8ce03ae with fourteen complete mathematical families full semantic and primary-source applications; actual unforced verdict/confidence and per214depth; not finalcold, no image/render/Kimi/projectclosure'}
(native / 'launch.json').write_text(json.dumps(launch, indent=2) + '\n')
start = time.monotonic()
with (native / 'events.jsonl').open('xb') as stdout, (native / 'stderr.txt').open('xb') as stderr:
  child = subprocess.Popen(argv, cwd=carrier, env=env, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr)
  pid = {'pid': child.pid, 'supervisor_pid': os.getpid(), 'proc_start_ticks': Path('/proc/' + str(child.pid) + '/stat').read_text().split()[21], 'started_utc': launch['started_utc']}
  (native / 'pid.json').write_text(json.dumps(pid, indent=2) + '\n')
  print(json.dumps({'status': 'running', **pid, 'carrier_head': head, 'prompt_sha256': sha(prompt)}), flush=True)
  child.communicate(prompt)
exit_receipt = {'exit_code': child.returncode, 'elapsed_seconds': time.monotonic() - start, 'finished_utc': now(), 'carrier_head_unchanged': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=carrier, text=True).strip() == head, 'carrier_clean': subprocess.check_output(['git', 'status', '--porcelain'], cwd=carrier) == b'', 'events_sha256': sha((native / 'events.jsonl').read_bytes()), 'stderr_sha256': sha((native / 'stderr.txt').read_bytes())}
(native / 'exit.json').write_text(json.dumps(exit_receipt, indent=2) + '\n')
print(json.dumps({'status': 'terminal', **exit_receipt}), flush=True)
