from pathlib import Path
import re,json,hashlib,subprocess,shutil
b=Path('reviews/2026-11-12-nogo-topology');old=b/'packet-v2';p=b/'confirmation-packet-v3';p.mkdir()
rows=[]
def cp(src,dst):
 q=p/dst;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(src.read_bytes());rows.append({'packet':dst,'source':str(src),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
for name in ['topology.tex','nogo-projection-escape.tex','nogo-feature-range.tex']:
 source=Path('notes/no-go/topology.tex') if name=='topology.tex' else Path('notes/figures')/name
 cp(source,'candidate/'+name);cp(old/'candidate'/name,'previous/'+name)
for name in ['integrated_cameron_mean.tex','integrated_temporal_equilibrium.tex','projection-mathematics.md','homogeneity-hypothesis.tex']:
 cp(old/'sources'/name,'sources/'+name)
normalize=lambda s:re.sub(r'\s+','',s)
a=(old/'candidate/topology.tex').read_text();expected=a.replace('for every finite\n$r\\ge1$','for every\n$2<r<2/a$').replace('With $\\theta=2/3$ and $\\nu=1/\\theta=3/2$, no finite constant $C>0$ gives','On $[0,1]$, with $\\theta=2/3$ and $\\nu=1/\\theta=3/2$, no finite constant\n$C>0$ gives')
assert normalize(expected)==normalize((p/'candidate/topology.tex').read_text())
for name in ['nogo-projection-escape.tex','nogo-feature-range.tex']:assert normalize((p/'candidate'/name).read_text())==normalize((p/'previous'/name).read_text())
(p/'CHANGE-CONTRACT.md').write_text('Mandatory repair: NG25 completed mean map operator-norm assertion now quantifies only 2<r<2/a, the domain range of the cited completed compact map. The explicit translated time-constant control lower-bound calculation is unchanged.\nOptional clarity: NG26 scalar time interval is now explicitly [0,1].\nAll three target files were formatted by format-tex with2-space indentation. Author mechanically compared every non-whitespace character: the only differences from previous/topology.tex are those two sentence replacements; both diagrams differ only in whitespace. Reviewer must judge the repaired claim independently. No past review verdict is supplied.\n')
(p/'READING-PLAN.md').write_text('Read all lines of these files; the entire new and prior target are supplied to check the exact change and unchanged mathematical scope. Other no-gos need only change-correspondence checking, not a new full proof review.\n'+'\n'.join('- '+r['packet'] for r in rows)+'\n- CHANGE-CONTRACT.md\n')
manifest={'source_revision':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'scope':'new NG25 valid-range statement and proof, explicit NG26 interval, exact mathematical correspondence of remaining six no-gos and two diagrams','files':rows,'normalized_delta_checked':True}
(b/'confirmation-manifest-v3.json').write_text(json.dumps(manifest,indent=2)+'\n');print(manifest['source_revision'],rows[0]['sha256'])
