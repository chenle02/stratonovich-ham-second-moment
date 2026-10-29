"""Freeze temporal growth-type candidates;reuse only the exact source-image cohort."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,subprocess,gzip
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--build-log',type=Path,required=True);args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[2];R=Path(__file__).resolve().parent
OLD=ROOT/'reviews/2026-10-29-near-static-lower';P=R/'packet-v1'
assert not P.exists();P.mkdir()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
src=ROOT/'notes/notes_stratonovich_ham_second_moment.tex';s=src.read_text()
old=subprocess.check_output(['git','show','HEAD:'+str(src.relative_to(ROOT))],cwd=ROOT,text=True)
def proofs(t):return {re.findall(r'\\ref\{([^}]+)\}',m.group())[-1]:m.group() for m in re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',t,re.S)}
a,b=proofs(old),proofs(s);assert len(a)==55 and len(b)==58
for k,v in a.items():assert b[k]==v,k
new=sorted(set(b)-set(a));newformal=new+['R:temporal-type-scope']
for env in ['lemma','proposition','theorem','corollary','hypothesis','goal','remark','conjecture','definition']:
 pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
 x=re.findall(pat,old,re.S);y=[z for z in re.findall(pat,s,re.S) if not any(r'\label{'+k+'}' in z for k in newformal)];assert x==y,env
log=src.with_suffix('.log').read_text();assert not re.search(r'(^!|[Uu]ndefined|Overfull)',log,re.M) and '\t' not in s
pages=int(re.search(r'Output written on .*?\((\d+) pages',log,re.S).group(1));assert pages==105
h=sha(src);subprocess.run(['format-tex',str(src)],check=True,stdout=subprocess.DEVNULL);assert sha(src)==h
bind={'baseline_revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'pages':pages,'proofs':58,'new_proofs':new,'all_55_prior_proofs_byte_equal':True,'all_prior_formal_statements_byte_equal':True,'original_full_goal_and_covariance_scope_unchanged':True,'tex_sha256':sha(src),'pdf_sha256':sha(src.with_suffix('.pdf')),'gate':{'errors':0,'undefined':0,'overfull':0,'tabs':0},'status':'CANDIDATE;fresh scoped HIGH review required;no fixed-positive-a sharp completion'}
dump(R/'change-binding.json',bind);dump(P/'change-binding.json',bind)
positions=[s.index(t) for t in [r'\section{Model and standing assumptions}',r'\section{Gate G1:',r'\subsection{Finite Gaussian models and their terminal kernels}',r'\section{A static lower comparison',r'\subsection{Temporal interpolation of the full moment}',r'\section{Targets}']]
for name,i,j in [('construction-inputs.txt',0,1),('upper-inputs.txt',2,3),('prior-lower-inputs.txt',3,4),('temporal.txt',4,5)]:
 (P/name).write_text(s[positions[i]:positions[j]].rstrip()+'\n')
for a,b in [(src,'canonical.tex'),(src.with_suffix('.pdf'),'canonical.pdf'),(src.with_suffix('.bbl'),'references.bbl'),(ROOT/'PROJECT-GOAL.md','project-goal.md'),(OLD/'source-rendering.json','source-rendering.json'),(R/'calibration.py','calibration.py'),(R/'calibration.json','calibration.json')]:
 shutil.copyfile(a,P/b)
images=[]
for f in sorted((OLD/'source-images').glob('*.png')):
 shutil.copyfile(f,P/f.name);images.append({'path':f.name,'kind':'image','sha256':sha(f),'media_type':'image/png'})
assert len(images)==11
for name in ['chen-hu-2025.pdf','chen-hu-2025.txt']:shutil.copyfile(OLD/'packet-v1'/name,P/name)
(P/'source-map.md').write_text('''Three NEW proofs in temporal.txt;all55prior proofs/formal statements unchanged.
No new external source theorem or numerical normalization is introduced.
Prior-lower-inputs.txt gives the reviewed static endpoint/norm series,raw-power
mean Holder,positive-series LIMSUP type,static minorant and near-static gap.
Construction and upper inputs contain the reused all-chain joint/temporal-tail
and full moment interfaces. Complete quantitative operator internals are in
optional canonical.tex/PDF;they are not requested as a new whole-paper audit.
Known external static input is Chen--HuTh1.2(1.9)p2147,structural p1/p2law with
actualpositivefiniteL0;no white numeric Cor1.12value is adopted. Required
source images cover the same11exact PNGs as the prior native calibration.
The candidate supplies static series convergence from the fractional upper;
source(4.3)onp2171is contextual and not used quantitatively.
The same image cohort permits preparation reuse only;THIS scientific attempt
must prove its own source delivery. No old review report is supplied.

Critical new quantifiers:
- p1has ONE specified empty/nonempty split; p2sums ALL2k+1splits.
- Every pairing has coefficientONE;ordered-chain kernels contain no extra n!.
- Raw temporal powers interpolate on the SAME positive spatial measure.
- Endpoints may includea=0,defined as static covariance1,notGamma_E(0).
- Coefficient types use LIMSUP,not an exact coefficient root limit.
- Each actual rate is normalized by its OWN T^kappa(a);nu=3-alpha is fixed.
- Only UPPER rates are log-convex/continuous in the interior.
- Both time-liminf/time-limsup approach static constants only in an ITERATED
  a->0aftertimeasymptotic limit. No fixed-positive-aTlimit or simultaneous/
  uniform-in-T/shape result follows. Original full G:sharp remains open.
- Observables are Eu and Eu2,p1is not E|u|;no higher-p/Skorohod assertion.
Diagnostics:30exact whiteorder2Holder cases;static15diagram total11/540;
96positive atomic samples with all split assignments. Atomic data are NOT
continuum quadrature or an analytic proof/Lean certificate.
''')
required=[{'path':x} for x in ['temporal.txt','prior-lower-inputs.txt','construction-inputs.txt','upper-inputs.txt','project-goal.md','change-binding.json','source-map.md','source-rendering.json','calibration.py','calibration.json']]+images
for n in ['rate-shape-screen.md','rate-shape-screen.py','rate-shape-screen.json']:
 shutil.copyfile(R/n,P/n);required.append({'path':n})
dump(R/'required-v1.json',required);dump(R/'manifest-v1.json',{f.name:sha(f) for f in sorted(P.iterdir()) if f.is_file()})
(R/'build-driver.txt.gz').write_bytes(gzip.compress(args.build_log.read_bytes(),mtime=0))
print(json.dumps({'pages':pages,'proofs':58,'new':new,'required_texts':13,'images':11,'packet_members':len(list(P.iterdir()))},indent=2))
