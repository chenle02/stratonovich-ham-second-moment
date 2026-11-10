#!/usr/bin/env python3
"""Prospective record/source guards. Resolution is not proof truth or full-parent credit."""
from pathlib import Path,PurePosixPath
import json,re,hashlib,sys
sys.dont_write_bytecode=True
from jsonschema import Draft202012Validator,RefResolver
ROOT=Path(__file__).resolve().parent;PLAN=ROOT.parent/'stratonovich-af97-themed-main-plan-20261103';load=lambda p:json.loads(p.read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
PH=re.compile(r'^\s*(see below|standard|as above|same as(?: source)?|checked|read fully|coherent|pending|not worked|source complete|source available)[.!\s]*$',re.I)
def hasmath(v):return bool(v.strip()) and not PH.fullmatch(v) if isinstance(v,str) else isinstance(v,list) and any(hasmath(z) for z in v)
def resolve(d,p):
 if not isinstance(p,str) or not p.startswith('/'):raise ValueError('RFC6901 path required')
 for t in p[1:].split('/'):
  if re.search(r'~(?![01])',t):raise ValueError('bad escape')
  t=t.replace('~1','/').replace('~0','~')
  if isinstance(d,list):
   if not re.fullmatch(r'0|[1-9][0-9]*',t):raise ValueError('numeric array index required')
   d=d[int(t)]
  else:d=d[t]
 return d

def schema_validator():
 paths=[ROOT/'carrier/current/report-schema.json',ROOT/'carrier/report-schema.json']
 docs={p.as_uri():load(p) for p in paths}
 def deny(uri):raise ValueError('Unregistered/remote schema reference forbidden: '+uri)
 resolver=RefResolver(base_uri=paths[0].as_uri(),referrer=docs[paths[0].as_uri()],store=docs,handlers={'file':deny,'http':deny,'https':deny})
 return Draft202012Validator(docs[paths[0].as_uri()],resolver=resolver)

def problems(report,receipt=None):
 a=load(ROOT/'carrier/current/assignment.json');frozen=load(ROOT/'assignment-external-full-bindings.json');canonical={q['id']:q for q in load(PLAN/'proof-ownership.json')['proofs']};pq={q['id']:q for q in frozen['owned_bindings']};sq={s['id']:s for s in frozen['formals']};current=set(a['proof_order']);errs=[]
 def need(v,msg):
  if not v:errs.append(msg)
 try:errs += ['SCHEMA '+str(list(e.absolute_path))+': '+e.message[:130] for e in schema_validator().iter_errors(report)]
 except Exception as e:errs.append('SCHEMA resolution '+str(e));return errs
 if not isinstance(report,dict):return errs or ['Report is not object']
 def exact(k,ids,ordered=False):
  rows=report.get(k,[])
  if not isinstance(rows,list):errs.append(k+' not array');return []
  keys=[x.get('id') for x in rows if isinstance(x,dict)];need(len(rows)==len(keys)==len(set(keys)) and set(keys)==set(ids),k+' exact target set missing/duplicate/extra')
  if ordered:need(keys==ids,k+' fixed order mismatch')
  return rows
 ps=exact('proofs',a['proof_order'],True);ss=exact('formal_statements',[s[0] for s in a['formal_records']],True);js=exact('joins',a['canonical_join']);apps=exact('applications',a['boundary_applications']);actual={r.get('id'):r for r in ps if isinstance(r,dict)}
 owner=dict(x.split('\t') for x in (ROOT/'carrier/maps/canonical-owner-units.tsv').read_text().splitlines()[1:]);need(len(owner)==214 and all(owner[q]==v['owner_unit'] for q,v in canonical.items()),'actual canonical214 owner map')
 oldreg=load(ROOT/'carrier/input-clause-registry.json');known=[]
 for e in oldreg['ineligible_unqualified_premises']:
  root,suffix=e['ref'];alias,prefix=oldreg['roots'][root];known.append((oldreg['files'][alias]['path'],prefix+suffix))
 hqual=load(ROOT/'carrier/current/H-error-qualifications.json')
 for family,paths in hqual['H_unqualified_ineligible'].items():known += [('prior-math/H-calculations.json','/'+family+p) for p in paths]
 allowed={v['path']:v['sha256'] for v in oldreg['files'].values()};allowed['prior-math/H-calculations.json']=next(f['sha256'] for f in load(ROOT/'prompt-frame-bindings.json')['frames'] if f['path']=='prior-math/H-calculations.json')
 explicit={}
 for c in oldreg['clauses']:
  q=canonical[c['proof']];need(c['body']==q['raw_body_sha256'] and c['owner']==q['owner_unit'],'prior catalog bound identity')
  for root,suffix in c['refs']:
   alias,prefix=oldreg['roots'][root];explicit[(oldreg['files'][alias]['path'],prefix+suffix)]=c['proof']
 explicit[('prior-math/interval-calculations.json','/author_root_comparisons/0/root_mathematical_comparison_exact_excerpt')]='PROOF047'
 fields={'actual_working','constants_and_limits','consumer_check','remaining_obligation'}
 def body_bytes(q):
  # Only frozen source module bytes, never current mutable Article or directory search.
  path=(ROOT/'carrier'/q['path']).resolve()
  if not path.is_relative_to((ROOT/'carrier').resolve()):raise ValueError('source escape')
  b=path.read_bytes()
  if sha(b)!=q['source_sha256']:raise ValueError('changed source module')
  lines=b.splitlines(keepends=True);part=b''.join(lines[q['line']-1:q['end_line']]);inner=part.split(b'\\begin{proof}',1)[1].rsplit(b'\\end{proof}',1)[0]
  if sha(inner)!=q['raw_body_sha256']:raise ValueError('changed source body')
  return b,lines
 def actual_source_argument(fragment,q,lo,hi):
  # Bounded structural exclusion of headers, declarations, closing/metadata only.
  if set(range(lo,hi+1))<=set([q['line'],q['end_line'],q.get('closing_sentence_line',q['end_line']-1)]):return False
  text=fragment.decode();text=re.sub(r'(?<!\\)%[^\n]*','',text)
  lines=[]
  for line in text.splitlines():
   z=line.strip()
   if not z or z.startswith('\\begin{proof}') or z.startswith('\\end{proof}') or z.startswith('This proves '):continue
   if re.fullmatch(r'(?:\\(?:label|ref|eqref|pageref)\{[^}]*\}|PROOF\d{3}|[.{}\s])+',z):continue
   lines.append(z)
  return bool(lines)
 def source_clause(d):
  ref=d.get('math_reference');m=re.fullmatch(r'source-proof:([A-Za-z0-9_./-]+\.tex)#(PROOF[0-9]{3})@([1-9][0-9]*):([1-9][0-9]*)',ref or '')
  if not m:return False
  path,ident,sa,sb=m.groups();target=d.get('target');q=canonical.get(target)
  if ident!=target or target in current or not q or path!=q['path'] or PurePosixPath(path).is_absolute() or any(x in ['.','..'] for x in path.split('/')):return False
  lo,hi=int(sa),int(sb)
  if lo>hi:return False
  mode=d.get('clause_id','').split(':',1)[0]
  if mode not in ['SOURCE_FULL_PROOF','SOURCE_STATEMENT_AND_PROOF','SOURCE_SUBCLAUSE'] or not d.get('clause_id','').split(':',1)[-1].strip():return False
  if mode=='SOURCE_FULL_PROOF':ok=(lo,hi)==(q['line'],q['end_line'])
  elif mode=='SOURCE_STATEMENT_AND_PROOF':ok=q['statement']['path']==path and (lo,hi)==(q['statement']['start_line'],q['end_line'])
  else:ok=q['line']<=lo<=hi<=q['end_line']
  if not ok:return False
  if not all(hasmath(d.get(k)) and str(d.get(k)).strip().lower() not in ['none','source complete','source available',target.lower()] for k in ['actual_hypotheses','actual_consumer_check','unresolved_parent_condition']):return False
  try:
   b,lines=body_bytes(q);fragment=b''.join(lines[lo-1:hi]);proof_fragment=b''.join(lines[max(lo,q['line'])-1:min(hi,q['end_line'])])
   if not actual_source_argument(proof_fragment,q,max(lo,q['line']),min(hi,q['end_line'])):return False
   if receipt is not None:receipt.append({'kind':'STRUCTURAL_SOURCE_RESOLUTION_NOT_MATH_ACCEPTANCE','target':target,'owner_unit':owner[target],'path':path,'module_sha256':sha(b),'canonical_body_sha256':q['raw_body_sha256'],'mode':mode,'range_LF':[lo,hi],'fragment_sha256':sha(fragment),'remaining_full_parent_condition':d['unresolved_parent_condition']})
   return True
  except (ValueError,KeyError,IndexError,TypeError,OSError,UnicodeError):return False
 def json_clause(ref,target):
  try:
   if not isinstance(ref,str) or ref.count('#')!=1:return False
   name,ptr=ref.split('#');tokens=ptr[1:].split('/') if ptr.startswith('/') else []
   if name in ['','current']:
    value=resolve(report,ptr)
    if len(tokens)<3:return False
    if tokens[0]=='proofs':
     rec=report['proofs'][int(tokens[1])];q=canonical[target]
     if rec['id']!=target or tokens[2] not in fields or rec['raw_body_sha256']!=q['raw_body_sha256'] or rec['source_sha256']!=q['source_sha256']:return False
    elif tokens[0]=='formal_statements' and tokens[2]=='actual_clause_and_scope_check':
     rec=report['formal_statements'][int(tokens[1])];s=sq.get(rec['id'])
     if target in current or not s or s['role']!='INPUT_APPLICATION' or s['own_proof_id']!=target or rec['source_sha256']!=s['source_sha256'] or rec['body_sha256']!=s['raw_body_sha256']:return False
    elif tokens[0]=='model_and_constant_audit' and tokens[2]=='actual_deduction':
     if target in current or report['model_and_constant_audit'][int(tokens[1])].get('target')!=target:return False
    else:return False
    return hasmath(value)
   if name not in allowed:return False
   p=(ROOT/'carrier'/name).resolve()
   if not p.is_relative_to((ROOT/'carrier').resolve()):return False
   raw=p.read_bytes()
   if sha(raw)!=allowed[name] or any(n==name and (ptr==bad or bad.startswith(ptr+'/')) for n,bad in known):return False
   data=json.loads(raw)
   if explicit.get((name,ptr))==target:return hasmath(resolve(data,ptr))
   roots=[(v[0],v[1]) for v in oldreg['roots'].values()]
   for alias,prefix in roots:
    if oldreg['files'][alias]['path']!=name:continue
    stem=prefix+'/proofs/'
    if ptr.startswith(stem):
     t=ptr[len(stem):].split('/')
     if len(t)<2 or not re.fullmatch(r'0|[1-9][0-9]*',t[0]) or t[1] not in fields:return False
     rec=resolve(data,stem+t[0]);q=canonical[target]
     if rec.get('id')!=target or rec.get('raw_body_sha256')!=q['raw_body_sha256'] or rec.get('source_sha256')!=q['source_sha256']:return False
     return hasmath(resolve(data,ptr))
   stem='/actual_B_phase_factual_working/mathematical_errata/'
   if name=='prior-math/B-phase-calculations.json' and ptr.startswith(stem):
    t=ptr[len(stem):].split('/');item=resolve(data,stem+t[0])
    if len(t)!=2 or t[1]!='corrected_derivation' or item.get('affected_proof')!=target:return False
    rec=next(x for x in data['actual_B_phase_original_working']['proofs'] if x.get('id')==target);q=canonical[target]
    return rec.get('raw_body_sha256')==q['raw_body_sha256'] and rec.get('source_sha256')==q['source_sha256'] and hasmath(resolve(data,ptr))
   if name=='prior-math/H-calculations.json':
    stem='/original_H_mathematics/proofs/'
    if ptr.startswith(stem):
     t=ptr[len(stem):].split('/')
     if len(t)<2 or not re.fullmatch(r'0|[1-9][0-9]*',t[0]) or t[1] not in fields:return False
     rec=resolve(data,stem+t[0]);q=canonical[target]
     return rec.get('id')==target and rec.get('raw_body_sha256')==q['raw_body_sha256'] and rec.get('source_sha256')==q['source_sha256'] and hasmath(resolve(data,ptr))
    # Correct additive H facts with explicit source-bound target association.
    if ptr.startswith('/factual_H_mathematics/corrections/'):
     t=ptr.split('/');i=int(t[3]);targetmap={0:'PROOF200',1:'PROOF194',2:'PROOF195',3:'PROOF132',4:'PROOF132',5:'PROOF132',6:'PROOF201',7:'PROOF199',8:'PROOF118',9:'PROOF204',10:'PROOF203',11:'PROOF131'}
     if len(t)!=5 or t[4]!='corrected_derivation' or targetmap.get(i)!=target:return False
     return hasmath(resolve(data,ptr))
   return False
  except (ValueError,KeyError,IndexError,TypeError,AttributeError,OSError,StopIteration):return False
 def clause(d):return source_clause(d) if str(d.get('math_reference','')).startswith('source-proof:') else json_clause(d.get('math_reference'),d.get('target'))
 def working(rec,label):
  if rec.get('status')=='CHECKED':need(hasmath(rec.get('actual_working')),label+' actual nonplaceholder working required')
  else:need(bool(str(rec.get('remaining_obligation','')).strip()),label+' remaining condition required')
 def dep(d,label,parent=None):
  if not isinstance(d,dict):return
  target=d.get('target');kind=d.get('kind');state=d.get('state');role=d.get('premise_role');use=d.get('use_scope')
  need(hasmath(d.get('actual_hypotheses')) and hasmath(d.get('actual_consumer_check')),label+' actual hypotheses/consumer check required')
  if isinstance(target,str) and re.fullmatch(r'PROOF\d{3}',target):need(kind in ['OWN','DOWNSTREAM_CONTEXT'],label+' OWN cannot be disguised as given/import')
  if kind=='OWN':
   q=canonical.get(target)
   if not q:errs.append(label+' unknown exact OWN target');return
   need(d.get('target_label')==q['claim_label'] and d.get('owner_unit')==owner[target] and d.get('source_body_sha256')==q['raw_body_sha256'],label+' wrong exact target label/owner/body')
   need(role in ['PREMISE','CONDITIONAL_PREMISE'],label+' OWN premise/context mismatch')
   if target in current:
    need(not str(d.get('math_reference','')).startswith('source-proof:'),label+' source text cannot replace current reconstruction')
    need(state in ['CURRENT_MATH_RECONSTRUCTED','PENDING_MATH'],label+' current OWN cannot inherit prior completion')
    if state=='CURRENT_MATH_RECONSTRUCTED':
     if use=='IDENTIFIED_SUBCLAUSE':need(clause(d) and hasmath(d.get('unresolved_parent_condition')),label+' actual current math clause/parent condition required')
     else:need(use=='FULL_CURRENT_CLAIM' and actual.get(target,{}).get('status')=='CHECKED',label+' full-current over pending/incomplete parent')
   elif state=='PRIOR_MATH_CONSUMER_VALIDATED':need(use=='IDENTIFIED_SUBCLAUSE' and hasmath(d.get('clause_id')) and hasmath(d.get('unresolved_parent_condition')) and clause(d),label+' exact outside OWN math/source scope and parent condition required')
   else:need(state=='PENDING_MATH',label+' outside OWN requires actual clause or pending state')
   if state=='PENDING_MATH' and parent=='CHECKED':errs.append(label+' checked consumer hides pending actual premise')
  if kind in ['GIVEN_MODEL_ASSUMPTION','GLOBAL_HYPOTHESIS']:need(role in ['PREMISE','CONDITIONAL_PREMISE'] and state=='GIVEN_ASSUMPTION',label+' actual given premise/state invalid')
  if kind=='DOWNSTREAM_CONTEXT':need(role in ['DOWNSTREAM_CONSUMER','CONTEXT_ONLY'] and state=='CONTEXT_ONLY',label+' context cannot promote a premise')
  if kind=='DEFINITION':need(role=='DEFINITION_USED' and state=='DEFINITION_APPLIED',label+' definition role/state invalid')
  if kind=='PROPERTY_PROVED':need(role=='PROPERTY_UNDER_PROOF' and state=='PROPERTY_BEING_ESTABLISHED',label+' proved property not given')
  if kind=='PROPERTY_REFUTED':need(role=='PROPERTY_UNDER_REFUTATION' and state=='PROPERTY_BEING_REFUTED',label+' refuted property not assumed')
 for rec in ps:
  if not isinstance(rec,dict) or rec.get('id') not in pq:continue
  q=pq[rec['id']];lab=rec['id']
  for k,v in [('owner_label',q['claim_label']),('path',q['path']),('proof_LF',f"{q['line']}:{q['end_line']}"),('raw_body_sha256',q['raw_body_sha256']),('source_sha256',q['source_sha256'])]:need(rec.get(k)==v,lab+' wrong '+k)
  working(rec,lab);need(rec.get('phase_working_reference') is None,lab+' current work cannot be inherited')
  for d in rec.get('inputs',[]):dep(d,lab,rec.get('status'))
  if lab=='PROOF185' and rec.get('status')=='CHECKED':need(any(d.get('target')=='PROOF165' and d.get('kind')=='OWN' and d.get('premise_role') in ['PREMISE','CONDITIONAL_PREMISE'] for d in rec.get('inputs',[])),'PROOF185 needs actual165 compact norm floor, not168 conservation/051 vector bound')
 for rec in ss:
  if not isinstance(rec,dict) or rec.get('id') not in sq:continue
  s=sq[rec['id']];lab=rec['id']
  for k,v in [('path',s['path']),('environment',s['environment']),('ordinal',s['ordinal']),('LF',f"{s['start_line']}:{s['end_line']}"),('body_sha256',s['raw_body_sha256']),('classification','OWN'),('role',s['role']),('own_proof_id',s['own_proof_id']),('source_sha256',s['source_sha256'])]:need(rec.get(k)==v,lab+' exact declaration/source/role mismatch '+k)
  if rec.get('status')=='CHECKED':
   need(hasmath(rec.get('actual_clause_and_scope_check')),lab+' actual scope/application working required')
   if s['role']=='own_deduction':need(actual.get(s['own_proof_id'],{}).get('status')=='CHECKED',lab+' full formal ahead of current parent')
   elif s['role']=='INPUT_APPLICATION':need(any(d.get('target')==s['own_proof_id'] and d.get('kind')=='OWN' and d.get('use_scope')=='IDENTIFIED_SUBCLAUSE' for d in rec.get('inputs',[])) and hasmath(rec.get('remaining_obligation')),lab+' boundary application needs parent clause and no full-parent credit')
   else:need(s['own_proof_id']=='PROOF168' and hasmath(rec.get('remaining_obligation')),lab+' context-use must retain OWN168/full-parent boundary')
  for d in rec.get('inputs',[]):dep(d,lab,rec.get('status'))
 for rec in js+apps:
  if not isinstance(rec,dict):continue
  lab=rec.get('id','application');working(rec,lab)
  for d in rec.get('inputs',[]):dep(d,lab,rec.get('status'))
  if lab=='JOIN-POINT-UPPER' and rec.get('status')=='CHECKED':
   targets={d.get('target') for d in rec.get('inputs',[]) if d.get('kind')=='OWN'};need({'PROOF189','PROOF192','PROOF193'}<=targets,'point join missing actual current point/signed coupling inputs');need(all(p.get('status')=='CHECKED' for p in ps),'complete point join ahead of current14')
 gs=report.get('given_hypotheses',[]);need(len(gs)==1,'exact S064 given record required')
 for d in gs:
  dep(d,'S064');need(d.get('target')=='S064' and d.get('target_label')=='H:homog' and d.get('source_body_sha256')==frozen['given']['raw_body_sha256'] and d.get('kind') in ['GLOBAL_HYPOTHESIS','GIVEN_MODEL_ASSUMPTION'] and d.get('premise_role')=='PREMISE' and d.get('state')=='GIVEN_ASSUMPTION','actual original S064 role/source given')
 pending=False
 for d in report.get('provisional_dependencies',[]):
  dep(d,'global dependency')
  if d.get('kind')=='OWN' and d.get('state')=='PENDING_MATH' and d.get('premise_role') in ['PREMISE','CONDITIONAL_PREMISE']:pending=True
 if pending:need(report.get('verdict') not in ['PASS','PASS_WITH_NOTES'] and not all(p.get('status')=='CHECKED' for p in ps) and not any(p.get('status')=='CHECKED' for p in js+apps),'pending global actual premise contradicts complete/checked application')
 if any(p.get('status')!='CHECKED' for p in ps+ss+js+apps):need(report.get('verdict') not in ['PASS','PASS_WITH_NOTES'],'complete-scope header over unresolved assigned work')
 need(report.get('completed_public_record') is True,'incomplete public record cannot be invented')
 return errs

def fixture():
 a=load(ROOT/'carrier/current/assignment.json');f=load(ROOT/'assignment-external-full-bindings.json');r={'schema':'PROSPECTIVE_THEMED_MAIN_REPORT_V1','phase_id':a['phase_id'],'kind':'OWN_WORKING','source_commit':a['source_commit'],'verdict':'INCONCLUSIVE','confidence':'low','judgment_reason':'SYNTHETIC record control, not mathematical work.','actual_reading_scope':[],'proofs':[],'formal_statements':[],'joins':[],'applications':[],'primary_applications':[],'finite_controls':[],'provisional_dependencies':[],'model_and_constant_audit':[],'semantic_cycles':[],'findings':[],'limitations':['SYNTHETIC ONLY'],'completed_public_record':True,'given_hypotheses':[]}
 for q in f['owned_bindings']:r['proofs'].append({'id':q['id'],'owner_label':q['claim_label'],'path':q['path'],'proof_LF':f"{q['line']}:{q['end_line']}",'raw_body_sha256':q['raw_body_sha256'],'source_sha256':q['source_sha256'],'status':'LIMITED','actual_working':[],'inputs':[],'constants_and_limits':[],'consumer_check':'Synthetic unperformed.','remaining_obligation':'Full current deduction remains unperformed.','phase_working_reference':None})
 for s in f['formals']:r['formal_statements'].append({'id':s['id'],'path':s['path'],'environment':s['environment'],'ordinal':s['ordinal'],'LF':f"{s['start_line']}:{s['end_line']}",'body_sha256':s['raw_body_sha256'],'classification':'OWN','role':s['role'],'own_proof_id':s['own_proof_id'],'status':'LIMITED','actual_clause_and_scope_check':'Synthetic unperformed.','remaining_obligation':'Full parent remains outside current scope or incomplete; no credit.','source_sha256':s['source_sha256'],'inputs':[]})
 for k,seq in [('joins',a['canonical_join']),('applications',a['boundary_applications'])]:
  for ident in seq:r[k].append({'id':ident,'status':'LIMITED','actual_working':[],'inputs':[],'constants_and_limit_order':[],'semantic_dependency_check':'Synthetic unperformed.','full_model_scope':'Synthetic no clearance.','remaining_obligation':'Current coupling/boundary application unperformed.'})
 s=f['given'];r['given_hypotheses']=[{'target':'S064','target_label':'H:homog','owner_unit':None,'kind':'GLOBAL_HYPOTHESIS','premise_role':'PREMISE','state':'GIVEN_ASSUMPTION','use_scope':'FULL_CURRENT_CLAIM','clause_id':'H:homog','actual_hypotheses':'Original supplied admissible model assumptions.','actual_consumer_check':'Synthetic record only; actual applications unperformed.','source_body_sha256':s['raw_body_sha256'],'math_reference':None,'unresolved_parent_condition':'Given model, not an OWN proof to invent.'}];return r
if __name__=='__main__':
 receipt=[];issues=problems(load(Path(sys.argv[1])),receipt);print(json.dumps({'mechanical_record_valid':not issues,'issues':issues,'source_reference_receipts':receipt,'mathematical_acceptance':False},indent=2));raise SystemExit(bool(issues))
