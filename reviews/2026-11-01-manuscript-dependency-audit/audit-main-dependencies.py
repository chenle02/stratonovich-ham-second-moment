from pathlib import Path
import re,json,hashlib,subprocess,collections
r=Path(__file__).resolve().parents[2];inv=json.loads((r/'reviews/2026-11-01-coverage-recovery/proof-inventory-v1.json').read_text());files=inv['files'];texts={p:(r/p).read_text() for p in files};nodes={};owner={};spans={p:[] for p in files}
for path,text in texts.items():
 assert hashlib.sha256(text.encode()).hexdigest()==hashlib.sha256(subprocess.check_output(['git','show','887fbfbe0fa4368d6b32a436615d73349b2445d8:'+path],cwd=r)).hexdigest(),path
refpattern=r'\\(?:eqref|ref|autoref|cref|Cref)\{([^}]+)\}'
def refs(t):return sorted({x.strip() for a in re.findall(refpattern,t) for x in a.split(',')})
for path,t in texts.items():
 for m in re.finditer(r'\\begin\{(theorem|lemma|proposition|corollary|definition|hypothesis|conjecture|goal|remark)\}(.*?)\\end\{\1\}',t,re.S):
  labs=re.findall(r'\\label\{([^}]+)\}',m.group(2))
  if not labs:continue
  key=labs[0];assert key not in nodes,key
  nodes[key]={'id':key,'kind':m.group(1),'path':path,'line':t.count('\n',0,m.start())+1,'statement':m.group(0),'proofs':[],'labels':labs};spans[path].append((m.start(),m.end(),key))
  for lab in labs:assert lab not in owner,lab;owner[lab]=key
for proof in inv['proofs']:
 path=proof['path'];t=texts[path];start=sum(len(x) for x in t.splitlines(keepends=True)[:proof['line']-1]);assert t.startswith('\\begin{proof}',start),(path,proof['line'])
 end=t.index('\\end{proof}',start)+len('\\end{proof}');body=t[start:end];key=owner.get(proof['claim_label'],proof['claim_label'])
 if key not in nodes:nodes[key]={'id':key,'kind':'proof-with-external-statement','path':path,'line':proof['line'],'statement':'','proofs':[],'labels':[key]};owner[key]=key
 nodes[key]['proofs'].append({'proof_id':proof['id'],'text':body,'line':proof['line']});spans[path].append((start,end,key))
 for lab in re.findall(r'\\label\{([^}]+)\}',body):
  if lab in owner:assert owner[lab]==key,(lab,key)
  owner[lab]=key
for path,t in texts.items():
 for m in re.finditer(r'\\label\{([^}]+)\}',t):
  lab=m.group(1)
  if lab in owner:continue
  start=t.rfind('\n\n',0,m.start());start=0 if start<0 else start+2;end=t.find('\n\n',m.end());end=len(t) if end<0 else end
  key=lab;node={'id':key,'kind':'context-or-definition','path':path,'line':t.count('\n',0,start)+1,'statement':t[start:end],'proofs':[],'labels':[lab]};nodes[key]=node;owner[lab]=key
for key,n in nodes.items():
 alltext=n['statement']+'\n'+'\n'.join(p['text'] for p in n['proofs']);n['references']=refs(alltext);n['edges']=sorted({owner[q] for q in n['references'] if q in owner and owner[q]!=key});n['unresolved_references']=[q for q in n['references'] if q not in owner];n['external_citekeys']=sorted({k.strip() for a in re.findall(r'\\cites?\{([^}]+)\}',alltext) for k in a.split(',')})
def closure(roots):
 todo=list(roots);seen=set()
 while todo:
  key=todo.pop()
  if key in seen:continue
  assert key in nodes,key;seen.add(key);todo.extend(nodes[key]['edges'])
 return seen
roots=['H:homog','T:full-upper','T:intrinsic-second-moment'];core=closure(roots)
extra=['T:intrinsic-occupation-ceiling','C:intrinsic-spatial-bracket','P:white-spatial-energy','T:white-moment-bounds','C:white-relative-width','P:Jensen'];extended=closure(roots+extra)
bysection=collections.defaultdict(lambda:{'all_proofs':0,'core_reached':0,'with_bounds_reached':0,'unreached_labels':[]})
for p in inv['proofs']:
 s=p['section_title'];bysection[s]['all_proofs']+=1;key=owner[p['claim_label']]
 if key in core:bysection[s]['core_reached']+=1
 else:bysection[s]['unreached_labels'].append(p['claim_label'])
 if key in extended:bysection[s]['with_bounds_reached']+=1
out=r/'reviews/2026-11-01-manuscript-dependency-audit';out.mkdir(exist_ok=True)
summary={'scope':'AUTHOR reference reachability audit ONLY, not proof validity, semantic completeness or permission to delete material','source_revision':'887fbfbe0fa4368d6b32a436615d73349b2445d8','roots':roots,'additional_bound_calibration_roots':extra,'proofs_total':213,'core_proofs_reached':sum(v['core_reached'] for v in bysection.values()),'with_bounds_proofs_reached':sum(v['with_bounds_reached'] for v in bysection.values()),'core_nodes':len(core),'with_bounds_nodes':len(extended),'limitations':['Explicit labels are not all mathematical dependencies. Unlabelled setup, definitions, prose imports and cross-section conventions need manual checking.','Navigation/status references can overinclude. Unreached does not prove unnecessary; reached does not prove necessary or correct.','No source/proof/PDF or frozen review input is changed. Full existing review obligations stay open.'],'sections':dict(bysection),'core_labels':sorted(core),'with_bounds_labels':sorted(extended),'unresolved_in_core':[{ 'owner':k,'labels':nodes[k]['unresolved_references']} for k in sorted(core) if nodes[k]['unresolved_references']]}
(out/'reference-reachability-v1.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'reference-edges-v1.json').write_text(json.dumps({k:{q:v for q,v in n.items() if q not in ['statement','proofs']}|{'proof_ids':[p['proof_id'] for p in n['proofs']]} for k,n in nodes.items()},indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['sections','core_labels','with_bounds_labels','limitations']},indent=2))
for title,v in bysection.items():print(f"{v['core_reached']:3}/{v['with_bounds_reached']:3}/{v['all_proofs']:3} {title}")
