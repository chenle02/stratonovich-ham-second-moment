from pathlib import Path
import hashlib,json,subprocess,tarfile
root=Path.cwd();base=root/'reviews/2026-11-12-nogo-topology';packet=base/'packet-v1';packet.mkdir()
items=[]
def put(dst,src,data=None,scope='complete file'):
 p=root/src;raw=p.read_bytes();b=raw if data is None else data
 q=packet/dst;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b)
 items.append({'packet':dst,'source':src,'scope':scope,'source_sha256':hashlib.sha256(raw).hexdigest(),'packet_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'copy_equal':b==raw})
for p in ['notes/no-go/topology.tex','notes/figures/nogo-projection-escape.tex','notes/figures/nogo-feature-range.tex']:
 put('candidate/'+Path(p).name,p)
for p in ['notes/integrated_temporal_equilibrium.tex','notes/integrated_cameron_mean.tex','notes/integrated_source_convergence.tex','notes/integrated_covariance_foundation.tex','notes/integrated_compact_gaussian.tex']:
 put('sources/'+Path(p).name,p)
p='notes/higher-dimensional-hs-obstruction.md';s=(root/p).read_text();a=s.index('## 1.');b=s.index('Consequently an analogue');put('sources/hs-obstruction-mathematics.md',p,s[a:b].encode(),'exact complete mathematical Sections1-8; review-status introduction and retrospective conclusion excluded')
p='notes/upper-cameron-compactness.md';s=(root/p).read_text();a=s.index('## 9.');b=s.index('All C1-C3 and this negative guard');v=s[a:b].replace('ACCEPTED\nscalar','scalar');put('sources/projection-mathematics.md',p,v.encode(),'Section9 mathematical witness; historical acceptance adjective removed; no proof omitted')
p='reviews/2026-10-31-upper-residual-exponential/nonlinear-next-screen-v0.md';s=(root/p).read_text();a=s.index('Root exact scalar falsification');b=s.index('A precise possible next');put('sources/block-cost-mathematics.md',p,s[a:b].encode(),'complete exact scalar/rare-block mathematical screen, excluding prospective plans and past review statuses')
p='reviews/2026-11-07-gupper22-MAIN-public-and-range-counterexample/complete-public-result-counterexample-and-skeptic-packet.tar.gz'
with tarfile.open(root/p) as t:
 m=next(m for m in t.getmembers() if m.name.endswith('COUNTERCHECK/report.md'));s=t.extractfile(m).read().decode()
a=s.index('## Exact counterexample');b=s.index('## Does any assigned');s=s[a:b];s=s.replace('This directly falsifies the public assertion.','This disproves the range inclusion.').replace('This directly falsifies the public assertion.','This disproves the range inclusion.')
put('sources/feature-range-mathematics.md',p,s.encode(),'exact mathematical counterexample and fixed-extension sections of '+m.name+'; review-history sections excluded; one reporting sentence neutralized')
# Parameters and definitions needed by all statements, copied from the book hypothesis.
p='notes/notes_stratonovich_ham_second_moment.tex';s=(root/p).read_text();a=s.index('\\begin{hypothesis}',s.index('\\label{H:homog}')-150) if False else 0
# Locate exact environment containing H:homog.
pos=s.index('\\label{H:homog}');a=s.rfind('\\begin{hypothesis}',0,pos);b=s.index('\\end{hypothesis}',pos)+len('\\end{hypothesis}')
put('sources/homogeneity-hypothesis.tex',p,s[a:b].encode(),'complete environment H:homog only')
rev=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
manifest={'source_revision':rev,'candidate_kind':'uncommitted frozen working-tree candidate; content hashes govern','scope':'NG21,22,24,25,26,27,30,32 mathematics only; chapter relocation/rendering/whole-book excluded','files':items}
(base/'packet-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
paths=[i['packet'] for i in items]
(packet/'READING-PLAN.md').write_text('Read every line of each of the following mathematical files. Sources are supplied for derivation checking, not as accepted verdicts. No old review report is supplied.\n\n'+'\n'.join('- '+p for p in paths)+'\n')
print(rev,len(items),sum(i['bytes'] for i in items),hashlib.sha256((packet/'candidate/topology.tex').read_bytes()).hexdigest())
