"""Collect a terminal cold read; verify evidence, never grade mathematics."""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import subprocess

ROUND = Path(__file__).resolve().parent
ROOT = ROUND.parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def validate(execution, session, prompt, head, session_id):
    assert execution['status'] == 'terminal', 'Attempt not normally terminal'
    assert execution['exit_code'] == 0, 'Native transport failed'
    assert execution['model_requested'] == 'deepseek/deepseek-v4-pro'
    assert execution['head_held'] and execution['workspace_bytes_unchanged']
    assert execution['source_revision'] == head, 'Held source HEAD differs'
    assert sha(prompt.encode()) == execution['prompt_sha256'], 'Prompt binding differs'
    info = session['info']
    assert info['id'] == session_id, 'Export is from another session'
    workspace = Path(execution['cwd']).resolve()
    assert Path(info['directory']).resolve() == workspace
    messages = session['messages']
    users = [m for m in messages if m['info']['role'] == 'user']
    assert len(users) == 1, 'Fresh cold read must have exactly one user message'
    delivered = ''.join(p['text'] for p in users[0]['parts'] if p['type'] == 'text')
    assert delivered == prompt, 'Complete initial prompt differs'
    assistants = [m for m in messages if m['info']['role'] == 'assistant']
    assert assistants, 'No assistant messages'
    for m in assistants:
        assert m['info']['providerID'] == 'deepseek'
        assert m['info']['modelID'] == 'deepseek-v4-pro', 'Actual model differs'
        assert not m['info'].get('error'), 'Native assistant error'
    final = assistants[-1]
    assert final['info']['finish'] == 'stop', 'Incomplete final answer'
    report = '\n'.join(p['text'] for p in final['parts'] if p['type'] == 'text')
    assert report.strip(), 'Empty final report'
    tools = []
    for m in assistants:
        for p in m['parts']:
            if p['type'] != 'tool':
                continue
            assert p['tool'] in {'read', 'grep', 'glob'}, 'Unexpected tool'
            state = p['state']
            inputs = state.get('input', {})
            if p['tool'] == 'read':
                assert isinstance(inputs.get('filePath'), str), 'Missing read target'
            if p['tool'] == 'glob':
                pattern = Path(inputs['pattern'])
                assert not pattern.is_absolute() and '..' not in pattern.parts, 'External glob pattern'
            target = inputs.get('filePath', inputs.get('path', str(workspace)))
            target = Path(target)
            if not target.is_absolute():
                target = workspace / target
            assert target.resolve().is_relative_to(workspace), 'External tool target'
            output = state.get('output', '')
            tools.append({'tool': p['tool'], 'status': state['status'],
                          'input': inputs, 'target_relative': str(target.resolve().relative_to(workspace)),
                          'output_sha256': sha(output.encode()), 'output_bytes': len(output.encode())})
    return report, tools


def self_check():
    """Replay a completed predecessor, plus deliberately corrupted evidence."""
    prior = ROUND.parent / '2026-10-29-full-upper-cold-v4'
    execution = json.loads((prior / 'cold-v1-execution.json').read_text())
    session = json.loads((prior / 'cold-v1-session-final.json').read_text())
    prompt = (prior / 'prompt-v1.txt').read_text()
    head = execution['source_revision']
    sid = session['info']['id']
    report, tools = validate(execution, session, prompt, head, sid)
    assert report.strip() == (prior / 'cold-v1-report.txt').read_text().strip()
    assert len(tools) == 15
    controls = []
    variants = ['prompt', 'model', 'head', 'session', 'external_target', 'incomplete', 'second_user']
    for name in variants:
        e, s, p, h, i = copy.deepcopy(execution), copy.deepcopy(session), prompt, head, sid
        if name == 'prompt':
            p += 'corruption'
        elif name == 'model':
            next(m for m in s['messages'] if m['info']['role'] == 'assistant')['info']['modelID'] = 'wrong-model'
        elif name == 'head':
            h = 'wrong-source'
        elif name == 'session':
            i = 'wrong-session'
        elif name == 'external_target':
            next(p for m in s['messages'] for p in m['parts'] if p['type'] == 'tool')['state']['input']['path'] = '/outside-packet'
        elif name == 'incomplete':
            [m for m in s['messages'] if m['info']['role'] == 'assistant'][-1]['info']['finish'] = 'length'
        elif name == 'second_user':
            s['messages'].append(copy.deepcopy(s['messages'][0]))
        try:
            validate(e, s, p, h, i)
        except AssertionError:
            controls.append(name)
        else:
            raise AssertionError('Corrupted evidence incorrectly accepted: ' + name)
    result = {'completed_predecessor_replay': 'PASS', 'report_byte_content_equal': True,
              'tool_calls': len(tools), 'negative_controls_refused': controls,
              'scope': 'Collection evidence only;not mathematics,source-proof coverage or a verdict'}
    (ROUND / 'collector-check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


def collect():
    native = ROUND / 'native-v1'
    execution = json.loads((native / 'execution.json').read_text())
    assert execution.get('status') == 'terminal', 'Wait on the existing live handle'
    assert not (ROUND / 'collection-binding.json').exists(), 'Already collected;do not overwrite'
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    preflight = json.loads((ROUND / 'committed-preflight-v1.json').read_text())
    assert preflight['commit'] == head == execution['source_revision']
    manifest = json.loads((ROUND / 'manifest-v1.json').read_text())
    assert manifest == execution['input_hashes']
    for name, digest in manifest.items():
        assert sha((ROUND / 'packet-v1' / name).read_bytes()) == digest
        assert sha((Path(execution['cwd']) / name).read_bytes()) == digest
    events = [json.loads(x) for x in (native / 'events.jsonl').read_text().splitlines() if x.strip()]
    session_ids = {e['sessionID'] for e in events if 'sessionID' in e}
    assert len(session_ids) == 1, 'Native stream has no unique session'
    session_id = next(iter(session_ids))
    # A pipe-captured OpenCode export can exit0 before its large JSON is complete.
    # Use regular files and require a complete parse;never salvage a JSON prefix.
    export_path = native / 'session-final.json'
    with export_path.open('x') as output, (native / 'export-stderr.txt').open('x') as error:
        subprocess.run(['opencode', 'export', '--pure', session_id], cwd=execution['cwd'],
                       stdout=output, stderr=error, text=True, check=True)
    exported_text = export_path.read_text()
    session = json.loads(exported_text)
    prompt = (ROUND / 'prompt-v1.txt').read_text()
    report, tools = validate(execution, session, prompt, head, session_id)
    for target, content in [('cold-v1-report.txt', report.rstrip() + '\n'),
                            ('cold-v1-session-final.json', exported_text),
                            ('cold-v1-execution.json', (native / 'execution.json').read_text()),
                            ('source-tool-coverage.json', json.dumps(tools, indent=2) + '\n')]:
        assert not (ROUND / target).exists(), 'Refusing evidence overwrite'
        (ROUND / target).write_text(content)
    result = {'status': 'COLLECTED;scientific adjudication pending', 'source_revision': head,
              'session_id': session_id, 'actual_model': 'deepseek/deepseek-v4-pro',
              'elapsed_seconds': execution['elapsed_seconds'], 'head_held': True,
              'complete_initial_prompt_verified': True, 'input_hashes_verified': True,
              'all_tool_targets_inside_isolated_workspace': True, 'tool_calls': len(tools),
              'failed_tool_calls': sum(t['status'] != 'completed' for t in tools),
              'confidence_grade_requested': False,
              'native_events_sha256': sha((native / 'events.jsonl').read_bytes()),
              'session_export_sha256': sha(exported_text.encode()),
              'report_sha256': sha((ROUND / 'cold-v1-report.txt').read_bytes()),
              'does_not_prove': 'Mathematical acceptance,full-source proof audit,novelty,formal or circulation clearance'}
    (ROUND / 'collection-binding.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-check', action='store_true')
    args = parser.parse_args()
    self_check() if args.self_check else collect()
