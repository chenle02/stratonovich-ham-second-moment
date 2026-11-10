import json,re,hashlib,subprocess,collections
from pathlib import Path
R=Path('<HOME>/.local/state/Le-AI-Lab/stratonovich-fixed-mask-young-wave')
O=Path(__file__).parent
D='reviews/2026-11-02-main-deepseek/'
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(R),*a])
L=json.loads((R/(D+'depth-ledger-v41.json')).read_bytes())
I=json.loads((R/(D+'proof-index-v6.json')).read_bytes())
N=json.loads((R/(D+'proof-index-v6-neutral.json')).read_bytes())
head=git('rev-parse','HEAD').decode().strip(); science=I['scientific_source_revision']
assert head=='4d3a3da6fe7443bb92bf3c8e77157221284758b7',head
assert not git('status','--porcelain'), 'worktree not clean'
errors=[]; files=[]; proofs=[]; statements=[]; mismatches=[]; flags=[]; operations=[]
def check(ok,msg):
 if not ok:errors.append(msg)
def raw_at(path,start,env):
 data=(R/path).read_bytes();t=data.decode('utf-8');offset=sum(len(x) for x in t.splitlines(keepends=True)[:start-1]);m=re.search(r'\\begin\{'+re.escape(env)+r'\}(.*?)\\end\{'+re.escape(env)+r'\}',t[offset:],re.S)
 assert m,(path,start,env)
 check(m.start()<len(t[offset:].splitlines(keepends=True)[0]),f'{path}:{start}: env starts later than claimed line')
 return m.group(1).encode(), t.count('\n',0,offset+m.end())+1
for f in I['files']:
 data=(R/f['path']).read_bytes();actual=sha(data)
 check(actual==f['sha256'],f['path']+' index file hash')
 check(len(data)==f['bytes'],f['path']+' byte count')
 check(data==git('show',science+':'+f['path']),f['path']+' scientific git blob')
 check(f==next(x for x in N['source_files'] if x['path']==f['path']),f['path']+' neutral map file binding')
 files.append(dict(f,actual_sha256=actual,equals_scientific_git_blob=True))
M={p['id']:p for p in I['proofs']};NM={p['id']:p for p in N['proofs']}
check(len(M)==len(L['proofs'])==214,'proof counts')
for ix,row in enumerate(L['proofs']):
 p=M[row['id']];body,end=raw_at(p['path'],p['line'],'proof');actual=sha(body)
 check(actual==p['raw_body_sha256']==p['body_sha256']==NM[p['id']]['raw_body_sha256'],p['id']+' current exact raw hash')
 check(end==p['end_line'],p['id']+' proof end locator')
 check(sha((R/p['path']).read_bytes())==p['source_sha256'],p['id']+' index source module hash')
 for key,expected in [('source_path',p['path']),('source_line',p['line']),('raw_proof_sha256',actual),('current_source_sha256',p['source_sha256']),('claim_label',p['claim_label'])]:
  if row.get(key)!=expected:
   item={'id':row['id'],'field':key,'old':row.get(key),'new':expected,'path':p['path'],'source_line':p['line']};mismatches.append(item)
   operations.extend([{'op':'test','path':f'/proofs/{ix}/id','value':row['id']},{'op':'test','path':f'/proofs/{ix}/{key}','value':row.get(key)},{'op':'replace','path':f'/proofs/{ix}/{key}','value':expected}])
 old=row.get('previous_reviewed_raw_proof_sha256');literal=(old==actual)
 if old is not None and row.get('current_body_matches_previous_review_binding')!=literal:
  item={'id':row['id'],'field':'current_body_matches_previous_review_binding','old':row.get('current_body_matches_previous_review_binding'),'new':literal,'preserved_previous_reviewed_raw_proof_sha256':old,'current_raw_proof_sha256':actual};flags.append(item)
  operations.extend([{'op':'test','path':f'/proofs/{ix}/id','value':row['id']},{'op':'test','path':f'/proofs/{ix}/current_body_matches_previous_review_binding','value':row.get('current_body_matches_previous_review_binding')},{'op':'replace','path':f'/proofs/{ix}/current_body_matches_previous_review_binding','value':literal}])
 fresh=row.get('actual_new_six_body_review')
 if fresh:check(fresh['source_candidate_body_sha256']==actual,p['id']+' actual new six review binding')
 s=p['statement'];sb,se=raw_at(s['path'],s['start_line'],s['environment'])
 check(sha(sb)==s['raw_statement_body_sha256'],p['id']+' owning formal statement hash');check(se==s['end_line'],p['id']+' owning formal statement end')
 proofs.append({'id':p['id'],'path':p['path'],'line':p['line'],'end_line':end,'label':p['claim_label'],'actual_raw_body_sha256':actual,'actual_source_sha256':sha((R/p['path']).read_bytes()),'depth_state':row['depth_state']})
for s in N['formal_statements']:
 b,e=raw_at(s['path'],s['start_line'],s['environment']);check(sha(b)==s['raw_body_sha256'],str(s)+' formal body');check(e==s['end_line'],str(s)+' formal end');statements.append(dict(s,actual_raw_body_sha256=sha(b)))
check(len(statements)==240,'formal statement count')
check(M['PROOF093']['claim_label']=='P:actual-operator-driver','deferred093 owner')
for path in sorted(set(x['path'] for x in mismatches)):
 oldhash=sha(git('show','b4b6efccacbbccd8f747225330e9ccb27bc097a6:'+path))
 check(all(x['old']==oldhash for x in mismatches if x['path']==path and x['field']=='current_source_sha256'),path+' stale hash historical b4b6 identity')
oldstatus=L['source_binding_status'];newstatus=I['source_binding_status']
operations.extend([{'op':'test','path':'/source_binding_status','value':oldstatus},{'op':'replace','path':'/source_binding_status','value':newstatus}])
pdf='notes/notes_stratonovich_ham_second_moment.pdf';pdfb=(R/pdf).read_bytes()
check(pdfb==git('show',science+':'+pdf),'current PDF differs scientific commit')
info=subprocess.check_output(['pdfinfo',str(R/pdf)]).decode();pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1));check(pages==263,'PDF page count')
# Patch is a proposal only; simulate in memory to verify no verdict/history mutation.
C=json.loads(json.dumps(L))
for op in operations:
 keys=op['path'].strip('/').split('/');p=C
 for k in keys[:-1]:p=p[int(k)] if isinstance(p,list) else p[k]
 k=int(keys[-1]) if isinstance(p,list) else keys[-1]
 if op['op']=='test':assert p[k]==op['value']
 else:p[k]=op['value']
for a,b in zip(L['proofs'],C['proofs']):
 for k in a:
  if k not in ('current_source_sha256','current_body_matches_previous_review_binding'):check(a[k]==b[k],a['id']+' unintended alteration '+k)
report={'scope':'Read-only author/workflow metadata audit, not independent scientific review; proposed patch NOT applied','workflow_head':head,'scientific_source_revision':science,'input_files':[{ 'path':x,'sha256':sha((R/x).read_bytes())} for x in [D+'depth-ledger-v41.json',D+'proof-index-v6.json',D+'proof-index-v6-neutral.json','PROJECT-GOAL.md','Progress.md']], 'all28source_files_exact_index_and_scientific_commit':not errors,'proof_count':214,'formal_statement_count':240,'exact_body_path_label_and_current_line_mismatches':[x for x in mismatches if x['field']!='current_source_sha256'],'stale_current_module_hash_count':len(mismatches),'stale_current_module_hashes':mismatches,'false_current_vs_preserved_previous_flags':flags,'top_level_stale_current_descriptor':{'field':'source_binding_status','old':oldstatus,'new':newstatus},'historical_fields_to_preserve':['previous_reviewed_raw_proof_sha256','historical_review_source_line','historical_before_*','new_coupled_main_report.report_source_revision','all literal original/correction review outcomes and confidence','source_base_head and predecessor_index (inherited historical lineage; do not silently rebase)'],'state_counts':dict(collections.Counter(x['depth_state'] for x in L['proofs'])),'remaining_not_scoped_high':[{'id':x['id'],'claim_label':x['claim_label'],'state':x['depth_state'],'evidence':x['evidence']} for x in L['proofs'] if x['depth_state']!='SCOPED_HIGH_TEXT_DEPTH_ACCEPTED'],'current_pdf':{'path':pdf,'sha256':sha(pdfb),'pages':pages,'equals_scientific_commit_blob':True},'errors':errors,'no_Article_git_provider_or_grade_writes':True}
for name,obj in [('findings.json',report),('minimal-current-metadata-patch.json',operations),('actual-source-proof-statement-bindings.json',{'files':files,'proofs':proofs,'formal_statements':statements})]:
 (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'errors':errors,'stale_module_hashes':len(mismatches),'false_flags':len(flags),'top_descriptor':1,'proofs':len(proofs),'statements':len(statements),'files':len(files),'pdf':report['current_pdf']},indent=2))
assert not errors
