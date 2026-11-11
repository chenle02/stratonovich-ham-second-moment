#!/usr/bin/env python3
"""Count AI review RUNS recorded under reviews/ of Article-Stratonovich-HAM-Second-Moment.

Read-only: archives are read in memory, nothing is extracted or modified.
Usage:
    python3 -I count_reviews.py <repo-root> <out-dir>
Writes <out-dir>/review-stats.json, <out-dir>/runs.tsv, <out-dir>/unclassified.txt.

The evidence base is every regular file under reviews/ PLUS every member of every .tar/.tar.gz/
.tar.xz archive under reviews/ (members are addressed as "<archive>::<member>"; a member's
"directory" is "<archive>::<member dir>"). Full definitions: review-stats.md, "Definitions".

A RUN is one dispatch of one review task to one reviewer model (a model call was made or
attempted), whether or not it produced a report. Identity (merge key) by evidence format:
  K1 CLI receipt      : JSON object (top level or under "data") with provider + a status from the
                        subscription-review-cli vocabulary. Key = (family, session_id or started_utc).
                        All copies (packet copies, archive copies, original/recovered re-validations
                        of one session) merge into one run; the highest-ranked status is used.
                        Statuses blocked-*-preflight and dry-run made no model call: not runs
                        (counted separately as preflight refusals).
  K2 opencode session : one fresh opencode session id "ses_..." (the DeepSeek route). Sessions seen
                        only in preflight files are not reviews. Persistent sessions -> K3.
  K3 persistent turn  : one request-safe/completed-safe turn of a persistent opencode session,
                        key = (sid, request_sha256 or turn path). kind=="prompt" is a run;
                        kind=="summary" (context compaction) is not.
  K4 Kimi ACP turn    : one transport receipt (schema subscription-review-acp-transport/1) of a
                        persistent Kimi ACP session, key = (session, turn label). Compaction/usage
                        commands and availability probes are not runs; a "format-repair"
                        continuation is merged into the turn it repairs.
  K5 Kimi CLI session : a "session_<uuid>" with a structured status record and no K1 receipt.
  K6 launch only      : a launch record naming DeepSeek/Kimi in a top-level folder with no other
                        run of that family; key = (folder, started_utc).
  K7 legacy summary   : *summary*.json with model_actual + status in a folder with no other run
                        of the same family.
"""
import collections
import datetime as dt
import fnmatch
import gzip
import json
import os
import re
import sys
import tarfile

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
OUT = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else '.')
REV = os.path.join(ROOT, 'reviews')
MAX_MEMBER = 4_000_000
TEXT_EXT = ('.json', '.jsonl', '.md', '.txt', '.log')

VERDICTS = ['PASS_WITH_NOTES', 'PASS', 'FAIL', 'INCONCLUSIVE', 'PARTIAL']
CLI_STATUS = {'review-complete', 'review-complete-recovered', 'invalid-report',
              'blocked-provider', 'timeout', 'error'}
NO_CALL_STATUS = re.compile(r'^(blocked-.*preflight|dry-run)$')
SES_RE = re.compile(r'ses_[A-Za-z0-9]{26}')
KSES_RE = re.compile(r'session_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
PREFLIGHT_NAME = re.compile(r'preflight|(^|/|::)health/|probe', re.I)  # matched against the full virtual path
AGGREGATE_NAME = re.compile(r'^(depth-ledger|proof-index)', re.I)
PROVIDER_FAMILY = {'claude': 'Claude', 'codex': 'GPT/Codex', 'openai': 'GPT/Codex',
                   'kimi': 'Kimi', 'deepseek': 'DeepSeek'}
FAMS = ['Claude', 'GPT/Codex', 'DeepSeek', 'Kimi', 'other']

# ----------------------------------------------------------------- virtual file system
FILES = {}       # vpath -> text
ARCHIVES = []
errors = []


def vrel(p):
    return os.path.relpath(p, ROOT)


for dp, dn, fn in os.walk(REV):
    dn.sort()
    for f in sorted(fn):
        p = os.path.join(dp, f)
        rp = vrel(p)
        if re.search(r'\.(tar|tar\.gz|tgz|tar\.xz)$', f):
            ARCHIVES.append(p)
            continue
        try:
            if f.endswith(TEXT_EXT):
                FILES[rp] = open(p, encoding='utf-8', errors='ignore').read()
            elif f.endswith(('.txt.gz', '.md.gz', '.json.gz')):
                FILES[rp[:-3]] = gzip.open(p, 'rt', encoding='utf-8', errors='ignore').read()
        except Exception as e:
            errors.append((rp, str(e)[:100]))
for a in ARCHIVES:
    ra = vrel(a)
    try:
        with tarfile.open(a) as tf:
            for m in tf:
                if not m.isfile() or m.size > MAX_MEMBER or not m.name.endswith(TEXT_EXT):
                    continue
                name = m.name.lstrip('./')
                FILES[ra + '::' + name] = tf.extractfile(m).read().decode('utf-8', 'ignore')
    except Exception as e:
        errors.append((ra, str(e)[:100]))

JSON = {}
for p, t in FILES.items():
    if p.endswith('.json'):
        try:
            JSON[p] = json.loads(t)
        except Exception:
            pass

def vdirname(p):
    if '::' in p:
        a, m = p.split('::', 1)
        return a + '::' + (m.rsplit('/', 1)[0] if '/' in m else '')
    return p.rsplit('/', 1)[0]


DIR_INDEX = collections.defaultdict(list)
for p in FILES:
    DIR_INDEX[vdirname(p)].append(p)


def vbase(p):
    return p.split('::')[-1].rsplit('/', 1)[-1]


def vglob(d, pattern):
    return sorted(p for p in DIR_INDEX.get(d, []) if fnmatch.fnmatch(vbase(p), pattern))


def folder_of(p):
    return p.split('/')[1]


def unwrap(d):
    if isinstance(d, dict) and isinstance(d.get('data'), dict) and 'original_sha256' in d:
        return d['data']
    return d


def family(model):
    if not model:
        return None
    m = str(model).lower()
    if 'deepseek' in m:
        return 'DeepSeek'
    if 'kimi' in m or m == 'k3':
        return 'Kimi'
    if 'claude' in m or 'opus' in m:
        return 'Claude'
    if 'gpt' in m or 'codex' in m:
        return 'GPT/Codex'
    return None


def norm_verdict(v):
    if v is None:
        return 'missing'
    if v in ('not_requested', 'free_text_unparsed'):
        return v
    s = str(v).strip().upper()
    return s if s in VERDICTS else 'other'


def norm_conf(c):
    if c is None:
        return 'missing'
    s = str(c).strip().lower()
    return s.upper() if s in ('high', 'medium', 'low') else 'other'


def harvest(obj, keys, depth=2):
    if not isinstance(obj, dict):
        return None
    for k in keys:
        if k in obj and obj[k] not in (None, '') and not isinstance(obj[k], (dict, list)):
            return obj[k]
    if depth > 0:
        for v in obj.values():
            if isinstance(v, dict):
                r = harvest(v, keys, depth - 1)
                if r is not None:
                    return r
    return None


VERDICT_KEYS = ['verdict', 'actual_verdict', 'literal_verdict', 'reported_verdict', 'raw_verdict',
                'scientific_verdict', 'visible_literal_verdict', 'raw_mathematical_verdict']
CONF_KEYS = ['confidence', 'actual_confidence', 'literal_confidence', 'reported_confidence',
             'raw_confidence', 'visible_literal_confidence', 'raw_mathematical_confidence']
MODEL_KEYS = ['model_actual', 'actual_model', 'model', 'model_requested', 'actual_model_alias']


def iso_date(s):
    try:
        return dt.datetime.fromisoformat(str(s).replace('Z', '+00:00')).astimezone(dt.timezone.utc).date().isoformat()
    except Exception:
        return None


def ses_time(sid):
    """opencode descending id -> UTC time; offset calibrated on launch.json started_utc (+-1 s)."""
    v = (~int(sid[4:16], 16)) & ((1 << 48) - 1)
    return dt.datetime.fromtimestamp((v // 4096 + 26 * (1 << 36)) / 1000, dt.timezone.utc)


def tokens_from(obj, depth=1):
    if not isinstance(obj, dict):
        return None
    u = obj.get('usage')
    if isinstance(u, dict) and ('input_tokens' in u or 'output_tokens' in u):
        return {'input': (u.get('input_tokens') or 0) + (u.get('cache_creation_input_tokens') or 0)
                + (u.get('cache_read_input_tokens') or 0), 'output': u.get('output_tokens') or 0}
    for k in ('usage_verbatim', 'actual_token_metadata', 'actual_tokens', 'actual_usage_metadata'):
        u = obj.get(k)
        if isinstance(u, dict) and ('input' in u or 'output' in u):
            cache = u.get('cache') if isinstance(u.get('cache'), dict) else {}
            return {'input': (u.get('input') or 0) + (cache.get('read') or 0) + (cache.get('write') or 0),
                    'output': (u.get('output') or 0) + (u.get('reasoning') or 0)}
    u = obj.get('usage')
    if isinstance(u, list) and u and isinstance(u[0], dict) and 'FULLTURN' in u[0]:
        return {'input': sum((x.get('input_with_cache') or x.get('actual_input_including_cache') or 0) for x in u),
                'output': sum((x.get('output_plus_reasoning') or x.get('combined_output_reasoning') or 0) for x in u)}
    if depth > 0:
        for v in obj.values():
            if isinstance(v, dict):
                r = tokens_from(v, depth - 1)
                if r:
                    return r
    return None


V_RE = re.compile(r'(?i:verdict)[^\n]{0,60}?\b(PASS_WITH_NOTES|PASS|FAIL|INCONCLUSIVE|PARTIAL)\b')
C_RE = re.compile(r'(?i:confidence)[^\n]{0,40}?\b(HIGH|MEDIUM|LOW|high|medium|low)\b')


def verdict_from_text(t):
    v, c = V_RE.search(t), C_RE.search(t)
    return (v.group(1) if v else None, c.group(1).lower() if c else None)


def public_json_valid(t):
    try:
        d = json.loads(t.strip())
        return isinstance(d, dict) and 'verdict' in d
    except Exception:
        return False


runs, unclassified, claimed = [], [], set()
preflight_refusals = collections.Counter()


def new_run(**kw):
    r = dict(run_id=None, family=None, model=None, source_kind=None, folder=None, evidence=[],
             start_utc=None, date=None, date_source=None, outcome=None, verdict='missing',
             confidence='missing', accepted='unknown', accepted_source=None, contract_met=None,
             elapsed_seconds=None, input_tokens=None, output_tokens=None, format_repaired=False, notes=[])
    r.update(kw)
    r['notes'] = list(r['notes'])
    return r


def ev(lst, n=None):
    return sorted(set(lst))


def ev_out(lst, n=15):
    lst = sorted(set(lst))
    return lst[:n] + (['... +%d more' % (len(lst) - n)] if len(lst) > n else [])


# ----------------------------------------------------------------- K1 CLI receipts
STATUS_RANK = {'review-complete-recovered': 6, 'review-complete': 5, 'invalid-report': 3,
               'timeout': 2, 'blocked-provider': 1, 'error': 1}
k1 = collections.defaultdict(list)
for p, d in JSON.items():
    x = unwrap(d)
    if not isinstance(x, dict):
        continue
    prov, st = x.get('provider'), x.get('status')
    if not isinstance(prov, str) or prov not in PROVIDER_FAMILY or not isinstance(st, str) or not (x.get('session_id') or x.get('started_utc')):
        continue
    if NO_CALL_STATUS.match(st):
        preflight_refusals[(PROVIDER_FAMILY[prov], st, x.get('started_utc'))] += 1
        continue
    if st in CLI_STATUS:
        k1[(PROVIDER_FAMILY[prov], x.get('session_id') or x.get('started_utc'))].append((p, x))
K1_FOLLOW = []
for key, lst in k1.items():
    starts = sorted({q.get('started_utc') or '' for _, q in lst})
    if len(starts) > 1:  # same session dispatched more than once (resume/continuation)
        final = [t for t in lst if (t[1].get('started_utc') or '') == starts[-1]]
        for stx in starts[1:]:
            K1_FOLLOW.append({'family': key[0], 'session': key[1], 'start_utc': stx, 'folder': folder_of(lst[0][0]),
                              'evidence': [q for q, y in lst if (y.get('started_utc') or '') == stx], 'kind': 'same-session-resume'})
        total_el = sum(max((y.get('elapsed_seconds') or 0) for _, y in lst if (y.get('started_utc') or '') == stx) for stx in starts)
        first_status = sorted({y['status'] for _, y in lst if (y.get('started_utc') or '') == starts[0]})
    else:
        final, total_el, first_status = lst, None, None
    final.sort(key=lambda t: (STATUS_RANK.get(t[1]['status'], 0), 'recover' in vbase(t[0]), '::' not in t[0], -len(t[0])), reverse=True)
    p, x = final[0]
    st = x['status']
    loose = [q for q, _ in lst if '::' not in q]
    tok = tokens_from(x)
    r = new_run(run_id='K1:%s:%s' % key, family=key[0], model=x.get('model_actual') or x.get('model_requested'),
                source_kind='K1-cli-receipt', folder=folder_of(sorted(loose or [q for q, _ in lst])[0]),
                evidence=ev(q for q, _ in lst), start_utc=x.get('started_utc'), date=iso_date(x.get('started_utc')),
                date_source='started_utc',
                outcome={'review-complete': 'completed', 'review-complete-recovered': 'completed',
                         'invalid-report': 'invalid-report'}.get(st, 'blocked/quota/timeout'),
                verdict=norm_verdict(x.get('scientific_verdict')), confidence=norm_conf(x.get('confidence')),
                accepted={True: 'yes', False: 'no'}.get(x.get('accepted'), 'unknown'),
                accepted_source='receipt.accepted' if 'accepted' in x else None,
                elapsed_seconds=x.get('elapsed_seconds'),
                input_tokens=tok['input'] if tok else None, output_tokens=tok['output'] if tok else None,
                format_repaired=(st == 'review-complete-recovered'))
    if total_el is not None:
        r['elapsed_seconds'] = total_el
        r['start_utc'], r['date'] = starts[0], iso_date(starts[0])
        r['notes'].append('session dispatched %d times; outcome = last dispatch, elapsed = sum; first dispatch status %s' % (len(starts), first_status))
    sts = sorted(set(q['status'] for _, q in lst))
    if len(sts) > 1:
        r['notes'].append('merged copies with statuses %s; kept %s' % (sts, st))
    if not loose:
        r['notes'].append('receipt found only inside an archive')
    runs.append(r)
    claimed.update(q for q, _ in lst)
k1_sessions = {k[1] for k in k1}

# ----------------------------------------------------------------- session id index
ses_files = collections.defaultdict(set)
kses_files = collections.defaultdict(set)
for p, t in FILES.items():
    for m in set(SES_RE.findall(t)):
        ses_files[m].add(p)
    for m in set(KSES_RE.findall(t)):
        kses_files[m].add(p)

persistent_ses = set()
for p, d in JSON.items():
    x = unwrap(d)
    if 'request-safe' in vbase(p) and isinstance(x, dict) and x.get('sid'):
        persistent_ses.add(x['sid'])

# ----------------------------------------------------------------- K3 persistent DeepSeek turns
turns = {}
for p, d in JSON.items():
    b = vbase(p)
    if 'request-safe' in b or 'completed-safe' in b:
        prefix = b.split('request-safe' if 'request-safe' in b else 'completed-safe')[0]
        turns.setdefault((vdirname(p), prefix), {})['req' if 'request-safe' in b else 'done'] = (p, unwrap(d))
k3 = {}
for (dpath, prefix), recs in sorted(turns.items(), key=lambda kv: ('::' in kv[0][0], kv[0])):
    req, done = recs.get('req'), recs.get('done')
    kind = req[1].get('kind') if req else None
    sid = req[1].get('sid') if req else None
    inferred = kind is None
    if inferred:
        kind = 'summary' if re.search(r'comp|summary', prefix + dpath.rsplit('/', 1)[-1], re.I) else 'prompt'
    claimed.update(q for q, _ in recs.values())
    key = (sid, req[1].get('request_sha256')) if req else ('?', (done[1].get('assistant_id') if done else dpath))
    if kind != 'prompt':
        continue
    if key in k3:
        k3[key]['evidence'] += [q for q, _ in recs.values()]
        continue
    pub = vglob(dpath, prefix + '*public*.raw.txt')
    t = FILES.get(pub[0], '') if pub else ''
    v, c = verdict_from_text(t) if t else (None, None)
    if t and not v:
        v = 'not_requested'
    tok = tokens_from(done[1]) if done else None
    r = new_run(run_id='K3:%s' % (dpath + '/' + prefix).rstrip('/'), family='DeepSeek', model='deepseek/deepseek-v4-pro',
                source_kind='K3-persistent-opencode-turn', folder=folder_of(dpath),
                evidence=[q for q, _ in recs.values()] + pub, date=folder_of(dpath)[:10], date_source='folder-name',
                outcome='completed' if (done and t) else ('completed-no-public-text' if done else 'no-terminal-record'),
                verdict=norm_verdict(v), confidence=norm_conf(c),
                input_tokens=tok['input'] if tok else None, output_tokens=tok['output'] if tok else None)
    r['notes'].append('persistent session %s; family per Progress.md ("sameDScompactor"); verdict = raw model text' % (sid or '?'))
    if v == 'not_requested':
        r['notes'].append('ungraded working/stage turn (no verdict token in public text)')
    if inferred:
        r['notes'].append('kind inferred from name (no request-safe record): prompt')
    claimed.update(pub)
    k3[key] = r
runs += list(k3.values())

# ----------------------------------------------------------------- K4 Kimi ACP turns
acp = [(p, unwrap(d)) for p, d in JSON.items()
       if isinstance(unwrap(d), dict) and unwrap(d).get('schema') == 'subscription-review-acp-transport/1']
acp_sessions = {x.get('session_id') for _, x in acp}
NONREVIEW = re.compile(r'(compact|command|usage|probe|initial)', re.I)
acp_turns = collections.defaultdict(list)
for p, x in acp:
    b = vbase(p)
    claimed.add(p)
    if NONREVIEW.search(b):
        continue
    label = re.sub(r'(-format-repair)?-transport(-receipt)?(-relative)?\.json$', '', b)
    n = len(((x.get('accounting') or {}).get('prompt_usage')) or [])
    acp_turns[(x.get('session_id'), label)].append((n, p, 'format-repair' in b))
for (sid, label), lst in sorted(acp_turns.items()):
    lst.sort()
    pubs = set()
    for _, p, _ in lst:
        pubs.update(vglob(vdirname(p), label + '*public*.raw.txt'))
    pubs.update(q for q in FILES if vbase(q) == label + '-public.raw.txt')
    if not pubs:
        for _, p, _ in lst:
            d0 = vdirname(p)
            if sum(1 for k in acp_turns if any(vdirname(pp) == d0 for _, pp, _ in acp_turns[k])) == 1:
                pubs.update(vglob(d0, 'public.raw.txt'))
    pubs = sorted(pubs)
    reps = [q for q in pubs if 'format-repair' in vbase(q)]
    firsts = [q for q in pubs if 'format-repair' not in vbase(q)]
    final_pub = (reps or firsts or [None])[0]
    t = FILES.get(final_pub, '') if final_pub else ''
    v, c = verdict_from_text(t) if t else (None, None)
    if final_pub is None:
        outcome = 'no-terminal-record'
    elif not t.strip():
        outcome = 'empty-report'
    elif public_json_valid(t):
        outcome = 'completed'
    elif not label.startswith('pixel') and not v:
        outcome, v = 'completed', 'not_requested'
    else:
        outcome = 'invalid-report'
    first_valid = public_json_valid(FILES.get(firsts[0], '')) if firsts else False
    r = new_run(run_id='K4:%s:%s' % (sid[-12:], label), family='Kimi', model='kimi-code/k3',
                source_kind='K4-kimi-acp-turn', folder=folder_of(lst[0][1]), evidence=[p for _, p, _ in lst] + pubs,
                date=folder_of(lst[0][1])[:10], date_source='folder-name', outcome=outcome,
                verdict=norm_verdict(v), confidence=norm_conf(c),
                format_repaired=bool(reps) and not first_valid)
    r['notes'].append('ACP session %s prompt#%d; verdict/confidence = raw model JSON' % (sid[-12:], lst[0][0]))
    if v == 'not_requested':
        r['notes'].append('ungraded working/source-reading turn (no report JSON requested)')
    if reps:
        r['notes'].append('format-repair continuation merged; original report schema-valid=%s' % first_valid)
    claimed.update(pubs)
    runs.append(r)

# ----------------------------------------------------------------- K2 fresh opencode sessions
for sid, files in sorted(ses_files.items()):
    if sid in persistent_ses:
        continue
    nonpre = [p for p in files if not PREFLIGHT_NAME.search(p.split('/', 2)[2])]
    if not nonpre:
        preflight_refusals[('DeepSeek', 'preflight-only-session', sid)] += 1
        continue
    own = [p for p in files if p in JSON and not AGGREGATE_NAME.search(vbase(p))
           and not PREFLIGHT_NAME.search(p.split('/', 2)[2]) and len(set(SES_RE.findall(FILES[p]))) == 1]
    # home = where the session's own execution evidence lives (launch/terminal/collection/export)
    execf = [p for p in own if re.search(r'launch|terminal|collection|session-export|session-final|execution|technical-result|completion', vbase(p))]
    home = sorted(execf or own or nonpre, key=lambda q: ('::' in q, q))[0]
    hdir = vdirname(home)
    votes = collections.Counter()
    for p in own:
        x = unwrap(JSON[p])
        m = harvest(x, MODEL_KEYS) if isinstance(x, dict) else None
        if not family(m) and isinstance(x, dict):
            mm = re.search(r'--model\s+(\S+)', ' '.join(map(str, x.get('argv') or x.get('command_without_prompt') or [])))
            m = mm.group(1) if mm else None
        if family(m):
            votes[m] += 1
    model = votes.most_common(1)[0][0] if votes else None
    if len({family(m) for m in votes}) > 1:
        unclassified.append(('mixed-model-fields', sid, 'model fields disagree across session files: %s (majority used)' % dict(votes)))
    if not model:
        for p in vglob(hdir, '*.json'):
            m = harvest(unwrap(JSON.get(p)), MODEL_KEYS, depth=1)
            if family(m):
                model = m
                break
    fam = family(model)
    note_model = None
    if not fam:
        fam = 'DeepSeek'
        note_model = 'no model named in structured fields; attributed DeepSeek (only opencode reviewer route: paper-review-deepseek)'
    if fam != 'DeepSeek':
        note_model = 'opencode session with non-DeepSeek model field %s' % model
    v = c = el = tok = st = finish = contract_ok = None
    for p in sorted(own, key=lambda q: ('terminal-checks' not in q, '::' in q, q)):
        x = unwrap(JSON[p])
        if not isinstance(x, dict):
            continue
        v = v or harvest(x, VERDICT_KEYS)
        c = c or harvest(x, CONF_KEYS)
        el = el or harvest(x, ['elapsed_seconds'])
        tok = tok or tokens_from(x)
        st = st or harvest(x, ['started_utc'], 0)
        finish = finish or x.get('finish')
        if isinstance(x.get('contract'), dict) and contract_ok is None:
            contract_ok = str(x['contract'].get('contract_ok')).lower() == 'true'
    reports = [q for q in DIR_INDEX.get(hdir, []) if re.search(r'(report|public)', vbase(q), re.I)
               and vbase(q).endswith(('.md', '.txt', '.json'))]
    if not v:
        for q in sorted(reports):
            vv, cc = verdict_from_text(FILES[q])
            if vv:
                v, c = vv, c or cc
                break
    cold = None
    for p in own:
        x = unwrap(JSON[p])
        if isinstance(x, dict) and isinstance(x.get('status'), str) and re.match(r'(NOT )?CLEAR', x['status']):
            cold = x['status'].split(';')[0]
            el = el or x.get('elapsed_seconds')
    if not cold and (vglob(hdir, 'cold-v1-execution.json') or any(
            isinstance(unwrap(JSON.get(q)), dict) and unwrap(JSON.get(q)).get('is_cold_read') is True
            for q in vglob(hdir, '*launch*.json'))):
        cold = 'cold read'
    if not st:
        for p in vglob(hdir, '*launch*.json'):
            x = unwrap(JSON.get(p))
            if isinstance(x, dict) and x.get('started_utc'):
                st = x['started_utc']
                break
    t0 = ses_time(sid)
    if finish == 'length' or contract_ok is False:
        outcome = 'invalid-report'
    elif cold:
        outcome, v, c = 'completed', 'not_requested', None
    elif v:
        outcome = 'completed'
    elif any('technical-result' in vbase(p) for p in own):
        outcome, v = 'completed', 'not_requested'
    elif reports:
        outcome, v = 'completed', 'free_text_unparsed'
    else:
        outcome = 'unknown'
    r = new_run(run_id='K2:%s' % sid, family=fam, model=model or 'deepseek/deepseek-v4-pro (attributed)',
                source_kind='K2-opencode-session', folder=folder_of(home), evidence=ev(files),
                start_utc=st or t0.isoformat(), date=iso_date(st) or t0.date().isoformat(),
                date_source='started_utc' if st else 'session-id-timestamp', outcome=outcome,
                verdict=norm_verdict(v), confidence=norm_conf(c), elapsed_seconds=el,
                input_tokens=tok['input'] if tok else None, output_tokens=tok['output'] if tok else None)
    r['ses_time'] = t0.isoformat()
    if cold:
        r['notes'].append('cold read; grade not requested (status: %s)' % cold)
    if note_model:
        r['notes'].append(note_model)
    if finish == 'length':
        r['notes'].append('finish=length (truncated report)')
    if all('::' in p for p in files):
        r['notes'].append('session id found only inside archives')
    runs.append(r)
    claimed.update(own)

# ----------------------------------------------------------------- K5 Kimi CLI sessions (non-ACP)
for sid, files in sorted(kses_files.items()):
    if sid in acp_sessions or sid in k1_sessions:
        continue
    rec = None
    for p in sorted(files, key=lambda q: ('::' in q, q)):
        x = unwrap(JSON.get(p))
        if isinstance(x, dict) and sid in (x.get('session'), x.get('session_id')) and x.get('status'):
            rec = (p, x)
            break
    if not rec:
        unclassified.append(('kimi-session-without-status', sid,
                             'Kimi CLI session id with no structured status record; seen in: ' + ', '.join(ev_out(files, 4))))
        continue
    p, x = rec
    st = x['status']
    r = new_run(run_id='K5:%s' % sid, family='Kimi', model=x.get('model_actual') or x.get('actual_model_alias') or 'kimi-code/k3',
                source_kind='K5-kimi-cli-session', folder=folder_of(p), evidence=ev(files),
                start_utc=x.get('started_utc') or x.get('utc'), date=iso_date(x.get('started_utc') or x.get('utc')) or folder_of(p)[:10],
                date_source='started_utc' if x.get('started_utc') else ('record-utc' if x.get('utc') else 'folder-name'),
                outcome={'timeout': 'blocked/quota/timeout', 'invalid-report': 'invalid-report',
                         'review-complete': 'completed', 'blocked-provider': 'blocked/quota/timeout'}.get(st, 'unknown'),
                verdict=norm_verdict(x.get('scientific_verdict') or x.get('raw_mathematical_verdict')),
                confidence=norm_conf(x.get('confidence') or x.get('raw_mathematical_confidence')),
                accepted={True: 'yes', False: 'no'}.get(x.get('accepted'), 'unknown'),
                accepted_source='record.accepted' if 'accepted' in x else None, elapsed_seconds=x.get('elapsed_seconds'))
    runs.append(r)
    claimed.update(files)

# ----------------------------------------------------------------- K6 launch records / K8 follow-ups
def launch_time(p, x):
    st = x.get('started_utc') or (dt.datetime.fromtimestamp(x['started_unix'], dt.timezone.utc).isoformat() if x.get('started_unix') else None)
    if not st:
        for q in DIR_INDEX.get(vdirname(p), []):
            y = unwrap(JSON.get(q))
            if isinstance(y, dict) and vbase(q) in ('pid.json', 'Root-live-observation.json', 'observed-live-process.json'):
                st = y.get('started_utc') or y.get('utc')
                if st:
                    break
    return st


k2_by_sid = {r['run_id'][3:]: r for r in runs if r['source_kind'] == 'K2-opencode-session'}
evid_folders = collections.defaultdict(set)
for r in runs:
    for e in r['evidence']:
        if e.startswith('reviews/'):
            evid_folders[r['family']].add(folder_of(e))
k6, followups = {}, {}
for p, d in sorted(JSON.items(), key=lambda kv: ('::' in kv[0], kv[0])):
    x = unwrap(d)
    b = vbase(p)
    if not isinstance(x, dict) or 'dry' in b or not re.search(r'launch|execution|^terminal\.json$', b):
        continue
    if PREFLIGHT_NAME.search(p.split('/', 2)[2]):
        continue
    model = x.get('model_requested')
    if not model:
        m = re.search(r'--model\s+(\S+)', ' '.join(map(str, x.get('command_without_prompt') or x.get('argv') or [])))
        model = m.group(1) if m else None
    fam = family(model)
    if fam not in ('DeepSeek', 'Kimi'):
        continue
    st = launch_time(p, x)
    refs = set(SES_RE.findall(FILES[p]))
    if refs:  # a launch that names an existing opencode session = same-session follow-up dispatch
        sid = sorted(refs)[0]
        t0 = k2_by_sid[sid]['ses_time'] if sid in k2_by_sid else None
        if t0 and st and abs((dt.datetime.fromisoformat(st) - dt.datetime.fromisoformat(t0)).total_seconds()) < 60:
            continue  # this launch created the session: it is the K2 run itself
        key = (sid, st or x.get('user_sha256') or x.get('prompt_sha256') or p)
        followups.setdefault(key, {'family': fam, 'session': sid, 'start_utc': st, 'folder': folder_of(p), 'evidence': []})['evidence'].append(p)
        continue
    # launch that created a session: merge into the K2 run whose session id time matches
    if st:
        tl = dt.datetime.fromisoformat(st)
        mt = [r for r in k2_by_sid.values() if -60 <= (dt.datetime.fromisoformat(r['ses_time']) - tl).total_seconds() <= 900]
        if mt:
            mt[0]['evidence'].append(p)
            if mt[0]['date_source'] == 'session-id-timestamp':
                mt[0]['start_utc'], mt[0]['date'], mt[0]['date_source'] = st, iso_date(st), 'started_utc'
            claimed.add(p)
            continue
    if folder_of(p) in evid_folders[fam]:
        continue
    key = (folder_of(p), fam, st)
    if key in k6:
        k6[key]['evidence'].append(p)
        continue
    reps = [q for q in DIR_INDEX.get(vdirname(p), []) if re.search(r'report', vbase(q), re.I) and vbase(q).endswith(('.md', '.txt', '.json'))]
    v = c = None
    for q in sorted(reps):
        v, c = verdict_from_text(FILES[q])
        if v:
            break
    ex = x.get('exit_code', x.get('transport_exit_code'))
    if v:
        outcome = 'completed'
    elif x.get('status') == 'terminal' and ex not in (0, None):
        outcome = 'blocked/quota/timeout'
    else:
        outcome = 'no-terminal-record'
    r = new_run(run_id='K6:%s' % p, family=fam, model=model, source_kind='K6-launch-record', folder=folder_of(p),
                evidence=[p] + reps, start_utc=st, date=iso_date(st) or folder_of(p)[:10],
                date_source='started_utc' if st else 'folder-name', outcome=outcome,
                verdict=norm_verdict(v), confidence=norm_conf(c), elapsed_seconds=x.get('elapsed_seconds'))
    r['notes'].append('launch record without a linked session/receipt; verdict (if any) parsed from report text beside it')
    if outcome == 'blocked/quota/timeout':
        r['notes'].append('process exit %s' % ex)
    k6[key] = r
    claimed.add(p)
runs += list(k6.values())
FOLLOWUPS = list(followups.values()) + K1_FOLLOW
for r in runs:  # Kimi ACP format-repair continuations are also same-session follow-up dispatches
    if r['source_kind'] == 'K4-kimi-acp-turn' and any('format-repair' in vbase(e) and e.endswith('.json') for e in r['evidence']):
        FOLLOWUPS.append({'family': 'Kimi', 'session': r['run_id'], 'start_utc': None, 'folder': r['folder'],
                          'evidence': [e for e in r['evidence'] if 'format-repair' in vbase(e)], 'kind': 'format-repair'})

# ----------------------------------------------------------------- K7 legacy summaries
fam_folders = collections.defaultdict(set)
for r in runs:
    fam_folders[r['family']].add(r['folder'])
for p, d in sorted(JSON.items()):
    x = unwrap(d)
    if not (isinstance(x, dict) and 'summary' in vbase(p) and x.get('model_actual') and 'status' in x):
        continue
    fam = family(x['model_actual'])
    if folder_of(p) in fam_folders[fam]:
        claimed.add(p)
        continue
    unclassified.append(('summary-without-run', p, 'summary names %s (status %s) but no run record of that family in the folder' % (x['model_actual'], str(x.get('status'))[:60])))

# ----------------------------------------------------------------- derived fields
for r in runs:
    r['contract_met'] = (r['outcome'] == 'completed' and r['verdict'] in ('PASS', 'PASS_WITH_NOTES') and r['confidence'] == 'HIGH')
    if r['accepted'] != 'unknown':
        r['accepted_effective'] = r['accepted']
        r['accepted_effective_basis'] = 'recorded'
    elif r['outcome'] == 'unknown':
        r['accepted_effective'] = 'unknown'
        r['accepted_effective_basis'] = 'outcome unknown'
    else:
        r['accepted_effective'] = 'yes' if r['contract_met'] else 'no'
        r['accepted_effective_basis'] = 'contract-equivalent (completed & PASS/PASS_WITH_NOTES & HIGH)'

# ----------------------------------------------------------------- folder census
folders = sorted(d for d in os.listdir(REV) if os.path.isdir(os.path.join(REV, d)))
REPORTISH = re.compile(r'(report|public\.raw|receipt|transport)', re.I)
CAT_RULES = [('lean-ledger/Lean-statement review', re.compile(r'lean', re.I)),
             ('visual/render check', re.compile(r'visual|pixel|render|image|glyph|primary5\d\d|P0\d\d-layout', re.I)),
             ('cold read', re.compile(r'cold', re.I))]
fold = {}
for f in folders:
    frs = [r for r in runs if r['folder'] == f]
    cat = None
    for name, rx in CAT_RULES:
        if rx.search(f):
            cat = name
            break
    if cat is None:
        cat = 'math proof/source review' if frs else 'other (preparation, adjudication, audit, infrastructure)'
    fold[f] = {'category': cat, 'runs': len(frs), 'families': sorted({r['family'] for r in frs})}
    if not frs:
        rep = [q for q in FILES if folder_of(q) == f and REPORTISH.search(vbase(q)) and q not in claimed
               and not re.search(r'packet|SOURCE|sources?/', q.split(f, 1)[1])]
        if rep:
            unclassified.append(('folder-without-run', f, 'report/receipt-like files but no run record (likely adjudication, '
                                 'audit or author work; check): ' + ', '.join(vbase(q) for q in ev_out(rep, 6))))

# ----------------------------------------------------------------- aggregates
def fam_of(r):
    return r['family'] if r['family'] in FAMS else 'other'


agg = {}
for key, fn in [('by_family', fam_of), ('by_date', lambda r: r['date'] or 'unknown'),
                ('by_outcome', lambda r: r['outcome']), ('by_verdict', lambda r: r['verdict']),
                ('by_confidence', lambda r: r['confidence']), ('by_accepted_recorded', lambda r: r['accepted']),
                ('by_accepted_effective', lambda r: r['accepted_effective']),
                ('by_source_kind', lambda r: r['source_kind']), ('by_date_source', lambda r: r['date_source'])]:
    agg[key] = dict(sorted(collections.Counter(fn(r) for r in runs).items()))
for dim in ['date', 'outcome', 'verdict', 'confidence', 'accepted', 'accepted_effective', 'source_kind']:
    t = collections.defaultdict(collections.Counter)
    for r in runs:
        t[fam_of(r)][r[dim] or 'unknown'] += 1
    agg['family_x_' + dim] = {k: dict(sorted(v.items())) for k, v in sorted(t.items())}
agg['format_repaired_runs'] = dict(collections.Counter(fam_of(r) for r in runs if r['format_repaired']))
res = {}
for f in FAMS:
    rs = [r for r in runs if fam_of(r) == f]
    if not rs:
        continue
    el = [r['elapsed_seconds'] for r in rs if isinstance(r['elapsed_seconds'], (int, float))]
    ti = [r for r in rs if r['input_tokens'] is not None]
    res[f] = {'runs': len(rs), 'elapsed_hours_sum': round(sum(el) / 3600, 2),
              'elapsed_coverage': '%d/%d' % (len(el), len(rs)),
              'input_tokens_sum_incl_cache': sum(r['input_tokens'] for r in ti),
              'output_tokens_sum_incl_reasoning': sum(r['output_tokens'] or 0 for r in ti),
              'token_coverage': '%d/%d' % (len(ti), len(rs))}
agg['resources_by_family'] = res
chk = collections.Counter(('receipt.accepted=%s' % r['accepted'], 'contract_met=%s' % r['contract_met'])
                          for r in runs if r['accepted_source'] == 'receipt.accepted')
agg['receipt_accepted_vs_contract_check'] = {' & '.join(k): v for k, v in sorted(chk.items())}
agg['same_session_followup_dispatches'] = {'total': len(FOLLOWUPS), 'by_family': dict(collections.Counter(f['family'] for f in FOLLOWUPS)), 'by_session': dict(collections.Counter(f['session'][-12:] for f in FOLLOWUPS))}
agg['preflight_refusals_not_runs'] = dict(collections.Counter('%s:%s' % (k[0], k[1]) for k in preflight_refusals))
agg['folders'] = {'total': len(folders), 'with_at_least_one_run': sum(1 for v in fold.values() if v['runs']),
                  'by_category': dict(sorted(collections.Counter(v['category'] for v in fold.values()).items())),
                  'by_category_with_run': dict(sorted(collections.Counter(v['category'] for v in fold.values() if v['runs']).items()))}
agg['corpus'] = {'loose_text_files': sum(1 for p in FILES if '::' not in p), 'archives': len(ARCHIVES),
                 'archive_text_members': sum(1 for p in FILES if '::' in p), 'read_errors': errors}

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'review-stats.json'), 'w') as fh:
    out_runs = [dict(r, evidence=ev_out(r['evidence']), n_evidence_files=len(set(r['evidence']))) for r in runs]
    json.dump({'generated_from_commit': __import__('subprocess').run(['git','-C',ROOT,'rev-parse','HEAD'],capture_output=True,text=True).stdout.strip(), 'n_runs': len(runs), 'aggregates': agg, 'runs': out_runs, 'followups': FOLLOWUPS, 'folders': fold},
              fh, indent=1, default=str)
cols = ['run_id', 'family', 'source_kind', 'folder', 'date', 'date_source', 'outcome', 'verdict', 'confidence',
        'accepted', 'accepted_effective', 'format_repaired', 'elapsed_seconds', 'input_tokens', 'output_tokens']
with open(os.path.join(OUT, 'runs.tsv'), 'w') as fh:
    fh.write('\t'.join(cols) + '\n')
    for r in sorted(runs, key=lambda r: (r['date'] or '', r['run_id'])):
        fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
with open(os.path.join(OUT, 'unclassified.txt'), 'w') as fh:
    fh.write('# kind\titem\treason\n')
    for row in unclassified:
        fh.write('\t'.join(row) + '\n')
print(json.dumps({k: agg[k] for k in ('by_family', 'by_outcome', 'by_source_kind', 'preflight_refusals_not_runs', 'same_session_followup_dispatches')}, indent=1))
print('runs', len(runs), 'unclassified', len(unclassified), 'files', len(FILES), 'archives', len(ARCHIVES), 'errors', len(errors))
