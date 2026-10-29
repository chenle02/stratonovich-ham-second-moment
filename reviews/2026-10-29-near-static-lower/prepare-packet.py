"""Freeze the bounded internal lower-comparison candidate and image calibration."""
from pathlib import Path
import subprocess,re,json,hashlib,shutil,gzip,argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--build-log',type=Path,required=True)
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[2];R=Path(__file__).resolve().parent
P=R/'packet-v1';CAL=R/'carrier-packet-v1';assert not P.exists() and not CAL.exists();P.mkdir();CAL.mkdir()
src=ROOT/'notes/notes_stratonovich_ham_second_moment.tex';s=src.read_text();old=subprocess.check_output(['git','show','HEAD:'+str(src.relative_to(ROOT))],cwd=ROOT,text=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def proofs(t):return {re.findall(r'\\ref\{([^}]+)\}',m.group())[-1]:m.group() for m in re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',t,re.S)}
before,after=proofs(old),proofs(s);assert len(before)==51 and len(after)==55
for k,v in before.items():assert after[k]==v,k
new=sorted(set(after)-set(before));newformal=new+['R:near-static-scope']
for env in ['lemma','proposition','theorem','corollary','hypothesis','goal','remark','conjecture','definition']:
 pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
 a=re.findall(pat,old,re.S);b=[x for x in re.findall(pat,s,re.S) if not any(r'\label{'+k+'}' in x for k in newformal)];assert a==b,env
log=src.with_suffix('.log').read_text();assert not re.search(r'(^!|[Uu]ndefined|Overfull)',log,re.M) and '\t' not in s
pages=int(re.search(r'Output written on .*?\((\d+) pages',log,re.S).group(1));assert pages==102
h=sha(src);subprocess.run(['format-tex',str(src)],check=True,stdout=subprocess.DEVNULL);assert sha(src)==h
change={'baseline_revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'pages':pages,'proofs':55,'new_proofs':new,'all_51_prior_proofs_byte_equal':True,'all_prior_formal_statements_byte_equal':True,'original_full_upper_sharp_and_covariance_scopes_retained':True,'tex_sha256':sha(src),'pdf_sha256':sha(src.with_suffix('.pdf')),'gate':{'errors':0,'undefined':0,'overfull':0,'tabs':0},'status':'CANDIDATE;fresh source-bound cross-family HIGH review required;not novelty or original sharp completion'}
dump(R/'change-binding.json',change);dump(P/'change-binding.json',change)
a=s.index(r'\section{A static lower comparison');b=s.index(r'\section{Targets}',a);(P/'lower.txt').write_text(s[a:b].rstrip()+'\n')
a=s.index(r'\section{Model and standing assumptions}');b=s.index(r'\section{Gate G1:',a);(P/'construction-inputs.txt').write_text(s[a:b].rstrip()+'\n')
a=s.index(r'\subsection{Finite Gaussian models and their terminal kernels}');b=s.index(r'\section{A static lower comparison',a);(P/'upper-inputs.txt').write_text(s[a:b].rstrip()+'\n')
for a,b in [(src,'canonical.tex'),(src.with_suffix('.pdf'),'canonical.pdf'),(src.with_suffix('.bbl'),'references.bbl'),(ROOT/'PROJECT-GOAL.md','project-goal.md'),(R/'source-rendering.json','source-rendering.json')]:shutil.copyfile(a,P/b)
for n in ['near-static-calibration.py','near-static-calibration.json','white-order-four-screen.py','white-order-four-screen.json']:
 shutil.copyfile(R/n,P/n)
(P/'static-source-map.md').write_text('''Bounded internal corollary candidate;novelty UNVERIFIED.

New four proofs are in lower.txt. All51prior proofs and every prior formal
statement are exactly unchanged;machine comparison is bound separately.
construction-inputs.txt and upper-inputs.txt give the reused model/limit and
regularized upper/tail interfaces. The unchanged interval/phase quantitative
internals are available in optional canonical.tex/PDF,not requested as a new
whole-paper audit. No prior report/verdict is supplied as mathematical proof.

Only new external analytic input:published Chen--HuTheorem1.2(1.9)p2147,
its structural static moment law atp1,p2and positive finite actualL0. No
absolute white-noise constant or current-author first-mean L_*formula is
used. Static class/convention:pp2145--2146,explicit generalized covariance
(2.18)p2152,ordered kernels/multiple heat-limit definitionp2150,fixed-order
Theorem3.8(i)p2165. All corresponding direct PDF images are required.
Published2171shows the source's series-convergence discussion,but candidate
DOES NOT USE its quantitative(4.3)or all-time uniformity. It constructs the
static fixed orders via our positive spatial lemma and its static full series
via finite Wick comparison with a FIXED positive fractional-time exponent,
our regularized-amplitude upper bound and uniform geometric-tail lemma.
This construction must be checked for circularity:the original full upper
uses no static actual solution/moment-law input. It is already proved before
this new section;the static Brownian mass argument does not assume U exists.

All width limits for Holder use RAW time powers at fixed spatial smoothing,
not exponent-dependent Laplace-prefix normalizations. A finite common-time
cutoff sandwich and uniform high-tail bound identify the raw spatial limit.
The zero-time exponent is a separately defined STATIC covariance one.
Both models use the SAME spatial smoothing for finite Wick comparison;
no pointwise spatial heat-covariance monotonicity or covariance-order coupling.
The comparison noise strength T^(-a/2) is amplitude,not T^(-a).

The strict p1/p2gap is against twice the ACTUAL Eu limsup,only near0.
No E|u| or full-pintermittency assertion. Static baseline lower holds all
admissible a,but it is not the original2^kappa_st*L_*(a)sharp lower target.
Full G:sharp remains unchanged/open. Tests are finite diagnostics only.
''')
images=[]
for f in sorted((R/'source-images').glob('*.png')):
 shutil.copyfile(f,P/f.name);shutil.copyfile(f,CAL/f.name);images.append({'path':f.name,'kind':'image','sha256':sha(f),'media_type':'image/png'})
assert len(images)==11
shutil.copyfile(ROOT/'reviews/2026-10-29-mild-construction/packet-v1/chen-hu-2025.pdf',P/'chen-hu-2025.pdf')
shutil.copyfile(ROOT/'reviews/2026-10-29-full-upper-cold-v7/packet-v1/chen-hu-2025.txt',P/'chen-hu-2025.txt')
req=[{'path':n} for n in ['lower.txt','construction-inputs.txt','upper-inputs.txt','project-goal.md','change-binding.json','static-source-map.md','source-rendering.json','near-static-calibration.py','near-static-calibration.json','white-order-four-screen.py','white-order-four-screen.json']]+images
dump(R/'required-v1.json',req);dump(R/'manifest-v1.json',{p.name:sha(p) for p in sorted(P.iterdir()) if p.is_file()})
(CAL/'images.txt').write_text('Carrier/legibility calibration ONLY,not scientific review. Read all11PNGs with direct Read using file_path only. New printed2146/2150/2171have two overlapping windows each,covering the full1600pixel scaled height. All five retained images are exact earlier bytes.\n\n'+'\n'.join(x['path']+' '+x['sha256'] for x in images)+'\n')
dump(R/'carrier-required-v1.json',[{'path':'images.txt'}]+images)
dump(R/'carrier-manifest-v1.json',{p.name:sha(p) for p in sorted(CAL.iterdir()) if p.is_file()})
(R/'carrier-contract-v1.txt').write_text('''ONLY native image-carrier and legibility calibration,not mathematics.
Read images.txt and open ALL11required PNGs exactly once with direct Read
using ONLY file_path. No command execution,browsing,editing or delegation.
Report unreadable/truncated images. Root separately verifies exact delivery;
do not claim hashes. Return ONLY bare JSON,no preamble/fence/afterword.
Use schema subscription-review-report/1,verdict,confidence,source_coverage,
checks with claim CARRIER_ONLY/verdict/reason,findings fatal/major/minor,
required_repairs,limitations. Decide your own legibility verdict/confidence.
State in limitations:this is not a scientific review,mathematical vote or
proof/circulation clearance. Escape all strings as valid JSON.
''')
(R/'build-driver.txt.gz').write_bytes(gzip.compress(args.build_log.read_bytes(),mtime=0))
print(json.dumps({'pages':pages,'proofs':55,'new':new,'required_texts':11,'source_images':11,'members':len(list(P.iterdir()))},indent=2))
