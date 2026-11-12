"""Collect observed attempt metadata without converting refusals into acceptances."""
from pathlib import Path
import datetime,hashlib,json,subprocess,collections
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
specs=[
 ('reviews/2026-11-12-nogo-pairings/deepseek-attempt-01','pairings','original-full-review',None),
 ('reviews/2026-11-12-nogo-pairings/kimi-attempt-01','pairings','original-full-review',None),
 ('reviews/2026-11-12-nogo-covariance-phase/deepseek-attempt-01','covariance-phase','original-full-review',None),
 ('reviews/2026-11-12-nogo-covariance-phase/kimi-attempt-01','covariance-phase','pre-dispatch-source-path-refusal',None),
 ('reviews/2026-11-12-nogo-covariance-phase/kimi-attempt-02','covariance-phase','full-review-after-pre-dispatch-path-repair','kimi-attempt-01'),
 ('reviews/2026-11-12-nogo-optimization/deepseek-attempt-01','optimization','original-full-review',None),
 ('reviews/2026-11-12-nogo-optimization/kimi-attempt-01','optimization','original-full-review',None),
 ('reviews/2026-11-12-nogo-optimization/candidate-v2/deepseek-attempt-01','optimization','expanded-proof-and-source-context-review','deepseek-attempt-01'),
 ('reviews/2026-11-12-nogo-optimization/phase-confirmation/kimi-attempt-01','optimization','expanded-No-go33-review-invalid-format','kimi-attempt-01'),
 ('reviews/2026-11-12-nogo-optimization/phase-complete-context/kimi-attempt-01','optimization','No-go33-complete-governing-source-context-review','phase-confirmation/kimi-attempt-01'),
 ('reviews/2026-11-12-nogo-topology/deepseek-attempt-01','topology','original-full-review',None),
 ('reviews/2026-11-12-nogo-topology/kimi-attempt-01','topology','original-full-review-invalid-format',None),
 ('reviews/2026-11-12-nogo-topology/kimi-format-01','topology','same-session-format-only-continuation','kimi-attempt-01'),
 ('reviews/2026-11-12-nogo-topology/deepseek-confirmation-01','topology','substantive-domain-repair-confirmation','deepseek-attempt-01'),
 ('reviews/2026-11-12-nogo-topology/kimi-confirmation-01','topology','substantive-domain-repair-confirmation','kimi-attempt-01'),
 ('reviews/2026-11-12-nogo-topology/kimi-full-v3-01','topology','full-review-of-substantively-repaired-candidate','kimi-attempt-01'),
 ('private/audit/2026-11-12-nogo-expansion/visual-cold/kimi-attempt-01','visual-navigation','fresh-cold-reading-and-49-image-review',None),
]
def read(p):return json.loads(p.read_text()) if p.is_file() else None
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
def rel(p):return p.relative_to(ROOT).as_posix()
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
def public_body(d):
 for name in ['report.json','report-native.json']:
  p=d/name
  if p.is_file():return read(p),rel(p),'parsed-public-report'
 p=d/'report.txt'
 if p.is_file():
  text=p.read_text()
  try:
   j,_=json.JSONDecoder().raw_decode(text[text.index('{'):]);return j,rel(p),'JSON-body-observation-only; full surrounding prose retained; not acceptance'
  except (ValueError,json.JSONDecodeError):pass
 return None,None,None
rows=[]
for path,group,relationship,parent in specs:
 d=ROOT/path;row={'attempt':path,'group':group,'relationship':relationship,'parent_within_group':parent}
 r=read(d/'receipt.json');report,rpath,rkind=public_body(d)
 if 'kimi' in d.name:
  row['route']='native-subscription-cli-kimi'
  if r is None:row.update(status='live-no-terminal-receipt',native_acceptance=None)
  else:
   row.update(status=r.get('status'),native_acceptance=r.get('accepted'),native_receipt=rel(d/'receipt.json'),native_receipt_sha256=sha(d/'receipt.json'))
   fields=['model_requested','model_actual','model_alias_actual','configured_effort','effort_actual','session_id','actual_route_verified','source_revision','input_hashes','started_utc','finished_utc','elapsed_seconds','transport_exit_code','transport_ok','scientific_verdict','confidence','diagnostics','usage_records','tool_calls_observed','candidate_hashes_unchanged','resumed_from','resume_mode','resume_binding','format_lineage','image_read_enabled']
   row['native_fields']={k:r.get(k) for k in fields}
 else:
  launch=read(d/'launch.json');done=read(d/'exit.json');row.update(route='opencode-paper-review-deepseek',status='terminal' if done else 'live',native_acceptance=None,native_acceptance_note='OpenCode scientific report; no subscription-CLI accepted flag exists.',launch=launch,process_exit=done)
  exports=[p for p in [d/'public-native-export.json',d/'public-export.json'] if p.is_file()]
  if exports:
   export=read(exports[0]);metadata=[]
   for x in walk(export):
    if x.get('role')=='assistant' and ('modelID' in x or 'providerID' in x):
     metadata.append({k:x.get(k) for k in ['id','sessionID','providerID','modelID','mode','agent','variant','finish','time','tokens','cost']})
   row['native_assistant_metadata']=metadata;row['public_native_export']=rel(exports[0]);row['public_native_export_sha256']=sha(exports[0])
  raw=d/'raw.jsonl'
  if raw.exists():
   events=[json.loads(x) for x in raw.read_text().splitlines()];row['native_sessions']=sorted({x['sessionID'] for x in events if x.get('sessionID')});row['event_timestamps_ms']=[{'type':x['type'],'timestamp':x.get('timestamp')} for x in events if x.get('type') in ['step_start','step_finish']]
 if report:
  row['public_report_observation']={'path':rpath,'interpretation':rkind,'sha256':sha(ROOT/rpath),'schema':report.get('schema'),'alternative_schema_key':report.get('$schema'),'verdict':report.get('verdict'),'confidence':report.get('confidence'),'checks':report.get('checks'),'findings':report.get('findings'),'required_repairs':report.get('required_repairs'),'source_coverage':report.get('source_coverage'),'limitations':report.get('limitations')}
 row['evidence_sha256']={p.name:sha(p) for p in d.iterdir() if p.is_file() and p.suffix in ['.json','.jsonl','.txt','.md']}
 rows.append(row)
scopes={'pairings':[1,2,3,4,5,6,7,10,17,18],'covariance-phase':[8,9,11,12,13,14,15,16,19,20,31],'topology':[21,22,24,25,26,27,30,32],'optimization':[23,28,29,33]}
assert sorted(sum(scopes.values(),[]))==list(range(1,34))
sessions=set()
for row in rows:
 if row.get('native_fields',{}).get('session_id'):sessions.add(row['native_fields']['session_id'])
 sessions.update(row.get('native_sessions',[]))
result={'schema':'nogo-chapter-review-telemetry/1','collected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checkout_head_at_collection':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'collection_script':rel(Path(__file__).resolve()),'authoring':{'family':'GPT','exact_model':None,'authoring_token_usage':None,'authoring_elapsed_seconds':None,'missing_data_reason':'Not instrumented in this session; do not infer authoring totals from review timings or commit timestamps.','delegated_author_sections':['pairings','covariance-phase','topology'],'root_author_section':'optimization; integration/navigation'},'aggregation_rules':['Raw provider token/cost dictionaries retain their original meaning; no cross-provider token sums, inferred billing, or invented zero usage.','Parallel review elapsed times are not summed into human wall-clock duration.','A same-session format continuation is not an independent scientific vote.','A pre-dispatch refusal is an operational attempt, not a completed model review.','Reported verdict/confidence, native receipt acceptance, source delivery, and root scientific adjudication are distinct.','A parsed body of an invalid-format report is observation only and never overrides the native refusal.','Missing data are null, not zero.','Whole-book and human verification are not certified by these scoped checks.'],'scopes':scopes,'attempt_count':len(rows),'distinct_observed_native_session_count':len(sessions),'attempts':rows,'source_manifest_paths':[rel(p) for p in sorted((ROOT/'reviews').glob('2026-11-12-nogo-*/**/*manifest*.json')) if 'workspace' not in p.parts],'final_validation':'reviews/2026-11-12-nogo-integration/validation.json','final_disposition':'reviews/2026-11-12-nogo-integration/DISPOSITION.json'}
(OUT/'TELEMETRY.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'attempt_records':len(rows),'distinct_observed_sessions':len(sessions),'status_counts':dict(collections.Counter(r['status'] for r in rows))},indent=2))
