#!/usr/bin/env python3
"""Index retained review artifacts after release filtering; never filter or export content."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,datetime,posixpath
from urllib.parse import quote

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--filtered-root',required=True,type=Path);ap.add_argument('--output',required=True,type=Path);ap.add_argument('--filter-receipt',required=True,type=Path);ap.add_argument('--ack-filtered',action='store_true',required=True);a=ap.parse_args();root=a.filtered_root.resolve();out=a.output.resolve();out.relative_to(root)
 if not a.filter_receipt.is_file():raise SystemExit('Existing filter-review receipt required; this tool does not grant release approval.')
 def git(*args):return subprocess.check_output(['git','-C',str(root),*args])
 if git('rev-parse','--is-inside-work-tree').strip()!=b'true':raise SystemExit('Expected a filtered Git checkout.')
 head=git('rev-parse','HEAD').decode().strip();commits=git('log','--all','--format=%H %T').decode().splitlines();trees={}
 for line in commits:
  c,t=line.split();trees.setdefault(t,c)
 forbidden_prefixes=('private/','sources/review-packets/','.kimi-code/','.codex/','.claude/')
 forbidden_names=re.compile(r'(^|/)(?:session-export[^/]*|native-events[^/]*|wire\.jsonl|auth\.json|credentials[^/]*|\.env(?:\..*)?)$',re.I)
 selector=re.compile(r'(?:review|report|telemetry|receipt|adjudication|disposition|run-ledger|usage)',re.I)
 versions={};current={};bad=0
 outrel=out.relative_to(root).as_posix().rstrip('/')+'/'
 for tree,commit in trees.items():
  for record in git('ls-tree','-rz','--full-tree',tree).split(b'\0'):
   if not record:continue
   meta,path=record.split(b'\t',1);mode,typ,oid=meta.decode().split();name=path.decode('utf-8')
   if name.startswith(forbidden_prefixes) or forbidden_names.search(name):bad+=1;continue
   if typ!='blob' or not selector.search(name) or name.startswith(outrel):continue
   key=(name,oid);v=versions.setdefault(key,{'path_at_revision':name,'git_blob':oid,'mode':mode,'example_commit':commit,'tree_occurrences':0});v['tree_occurrences']+=1
 if bad:raise SystemExit(f'Refused: {bad} retained private/runtime path occurrences. Revisit release filtering; no content exported.')
 for record in git('ls-tree','-rz','--full-tree','HEAD').split(b'\0'):
  if record:
   meta,path=record.split(b'\t',1);mode,typ,oid=meta.decode().split()
   if typ=='blob':current[path.decode()]=oid
 blobinfo={}
 for _,oid in versions:
  if oid in blobinfo:continue
  proc=subprocess.Popen(['git','-C',str(root),'cat-file','blob',oid],stdout=subprocess.PIPE);h=hashlib.sha256();size=0
  while True:
   chunk=proc.stdout.read(1024*1024)
   if not chunk:break
   h.update(chunk);size+=len(chunk)
  if proc.wait()!=0:raise SystemExit('Git blob read failed; incomplete inventory not emitted.')
  blobinfo[oid]={'sha256':h.hexdigest(),'bytes':size}
 rows=[]
 for (name,oid),v in sorted(versions.items()):
  row={**v,**blobinfo[oid],'present_at_head':current.get(name)==oid,'content_exported':False};row['relative_link']=quote(posixpath.relpath(name,out.relative_to(root).as_posix()),safe='/') if row['present_at_head'] else None;rows.append(row)
 out.mkdir(parents=True,exist_ok=True);receipt_hash=hashlib.sha256(a.filter_receipt.read_bytes()).hexdigest();data={'schema':'filtered-review-history-index/1','generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'filtered_head':head,'filter_receipt_sha256':receipt_hash,'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'reachable_commits_scanned':len(commits),'distinct_trees_scanned':len(trees),'selection_regex':selector.pattern,'scope':'Every matching path/blob version in all reachable filtered Git trees; not untracked files, reflogs, removed private records or scientific acceptance. Every tracked file below review-named paths matches.','versions':rows};(out/'inventory.json').write_text(json.dumps(data,indent=2)+'\n')
 lines=['# Retained review history index','',f'Filtered revision `{head}`. {len(rows)} retained path/blob versions across {len(trees)} distinct trees.','', 'This is an artifact index, not a count of independent reviews or accepted proofs. Historical versions remain in Git; no content is re-exported. Current-version links are relative. Missing current links indicate historical versions, not missing evidence.','', '| Artifact | SHA256 | Bytes | Historical/current |','|---|---|---:|---|']
 for r in rows:
  label=r['path_at_revision'].replace('|','\\|');label=f'[{label}]({r["relative_link"]})' if r['relative_link'] else '`'+label+'`';lines.append(f'| {label} | `{r["sha256"]}` | {r["bytes"]} | '+('current' if r['present_at_head'] else 'Git blob `'+r['git_blob']+'`')+' |')
 (out/'README.md').write_text('\n'.join(lines)+'\n');(out/'SHA256SUMS').write_text(''.join(hashlib.sha256((out/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in ['inventory.json','README.md']));print(json.dumps({'retained_versions':len(rows),'commits_scanned':len(commits),'content_exported':False}))
if __name__=='__main__':main()
