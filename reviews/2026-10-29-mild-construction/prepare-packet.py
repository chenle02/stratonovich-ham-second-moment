"""Freeze independent mild-construction candidate and prepare carrier-only plan."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import gzip

ROOT = Path(__file__).resolve().parents[2]
ROUND = Path(__file__).resolve().parent
OLD = ROOT/'reviews/2026-10-29-explicit-justifications'
PACKET = ROUND/'packet-v1'
CAL = ROUND/'carrier-packet-v1'
assert not PACKET.exists() and not CAL.exists(), 'Refusing packet overwrite'
shutil.copytree(OLD/'packet-v1', PACKET)
CAL.mkdir()
source = ROOT/'notes/notes_stratonovich_ham_second_moment.tex'
s = source.read_text()
baseline = '67ec196b2b566ddbb28b593755f5dc8b09dfae39'
previous = subprocess.check_output(['git','show',baseline+':'+str(source.relative_to(ROOT))],cwd=ROOT,text=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path,obj):
    path.write_text(json.dumps(obj,indent=2)+'\n')


def proofs(text):
    out={}
    for m in re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',text,re.S):
        refs=re.findall(r'\\ref\{([^}]+)\}',m.group())
        assert refs and refs[-1] not in out
        out[refs[-1]]=m.group()
    return out


before,after=proofs(previous),proofs(s)
assert len(before)==46 and len(after)==48
assert set(after)-set(before)=={'L:vertex-crude','P:mild-construction'}
for env in ['lemma','proposition','theorem','corollary','hypothesis','goal','remark','conjecture','definition']:
    pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
    a=re.findall(pat,previous,re.S);b=re.findall(pat,s,re.S)
    b=[x for x in b if not any(r'\label{'+k+'}' in x for k in ['L:vertex-crude','P:mild-construction'])]
    assert a==b,env
log=source.with_suffix('.log').read_text()
assert not re.search(r'(^!|[Uu]ndefined|Overfull)',log,re.M)
assert '\t' not in s
pages=int(re.search(r'Output written on .*?\((\d+) pages',log,re.S).group(1))
assert pages==92
labels=re.findall(r'\\label\{([^}]+)\}',s);assert len(labels)==len(set(labels))
change={'baseline_revision':baseline,'tex_sha256':sha(source),'pdf_sha256':sha(source.with_suffix('.pdf')),
        'pages':pages,'proofs':48,'new_proofs':sorted(set(after)-set(before)),
        'changed_existing_proofs':[k for k in before if before[k]!=after[k]],
        'unchanged_existing_proofs':sum(before[k]==after[k] for k in before),
        'all_prior_formal_statements_byte_equal':True,
        'original_full_covariance_and_sharp_target_unchanged':True,
        'no_uniqueness_claim_or_normalization_correction':True,
        'gate':{'errors':0,'undefined':0,'overfull':0,'tabs':0},
        'status':'CANDIDATE;fresh source-bound primary/HIGH and cold required'}
dump(ROUND/'change-binding.json',change);dump(PACKET/'proof-change-map.json',change)
bounds=[0]+[s.index(x) for x in [r'\section{G2 upper bounds for spatial exponents at most one}',r'\section{A static phase estimate at first variance order}',r'\section{Interval fields and the full upper bound}',r'\section{Targets}']]
for name,l,u in zip(['foundation.txt','calibrations.txt','operators.txt','intervals.txt'],bounds,bounds[1:]):
    (PACKET/name).write_text(s[l:u].rstrip()+'\n')
for src,dst in [(source,'canonical.tex'),(source.with_suffix('.pdf'),'canonical.pdf'),(source.with_suffix('.bbl'),'references.bbl')]:
    shutil.copyfile(src,PACKET/dst)
req=json.loads((OLD/'required-v1.json').read_text())
old_images=[x for x in req if x.get('kind')=='image'];assert len(old_images)==24
new_derivation=json.loads((ROUND/'new-source-images/derivation.json').read_text())
assert 'All12tiles opened' in new_derivation['root_visual_inspection']
new_images=[]
for item in new_derivation['new_images']:
    f=ROUND/'new-source-images'/item['path'];assert sha(f)==item['sha256']
    shutil.copyfile(f,PACKET/f.name)
    new_images.append({'path':f.name,'kind':'image','sha256':sha(f),'media_type':'image/png'})
all_images=old_images+new_images;assert len(all_images)==36
for row in all_images:
    f=PACKET/row['path'];assert sha(f)==row['sha256'];shutil.copyfile(f,CAL/f.name)
shutil.copyfile(ROUND/'new-source-images/derivation.json',PACKET/'mild-rendering.json')
for src,dst in [('multiplication-screen.py','mild-multiplication-screen.py'),('multiplication-screen.json','mild-multiplication-screen.json')]:
    shutil.copyfile(ROOT/'reviews/2026-10-29-full-upper-cold-v5'/src,PACKET/dst)
source_text=(ROOT/'reviews/2026-10-29-full-upper-cold-v5/packet-v1/chen-current-author.txt').read_text().split('\f')
with (PACKET/'source-excerpts.txt').open('a') as f:
    for page in [9,10,14,15,32,34,35,36,60,61]:
        f.write('\nCURRENT AUTHOR FULL PRINTED PAGE '+str(page)+'\n'+source_text[page-1].rstrip()+'\n')
(PACKET/'source-dependency-audit.md').write_text('''Current source dependency map;root prose is not proof authority.

Moment estimate/geometric series passage:fixed-order Theorem4.1 and CP operator
input. Independent mild identification:L:vertex-crude and P:mild-construction,
using sourceTheorem3.1 and LemmaA.1 plus the fixed-order limit. No source5(ii)
proof or(5.3)/(5.4)uniformity is imported. The repaired crude constants may
depend on the fixed covariance;they do not enter the sharp-scale upper bound.

AuthorSection4 argument is provided completely in author-section4.txt.
Its Lemma4.4 ->(4.4)limit ->Lemma2.4 ->Theorem4.1 uses fixed Laplace
parameters and precedes Section5's defective degree/time substitution.
The source's mild definition is(2.12)p9/Definition2.1p10. Its original
Section5(ii),pp35--36,uses(5.3) as a consumer;the candidate now supplies
an independent proof of this consumer with an e^(theta0*t) factor.
First-moment printed normalization is still not corrected/adopted.
No new hypercontractivity or Skorohod model theorem is imported.
''')
(PACKET/'source-map.txt').write_text('''Primary source PDFs are supplied complete as optional context;required
images/texts define actual coverage,not availability. Read every required
file completely. Source images are direct PDF renders,not OCR reconstruction.

chen-current-author.pdf SHA2565f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c:
pp2--4 model/spectral condition/quoted normalization;pp9--10 joint noise and
onefold definition/ordered kernels;pp12--15 Wick/Green convention/norms and
Theorem3.1; p22 fixed-order Theorem4.1; p30equal-length limits;pp35--36
original mild-proof consumer of faulty(5.3);pp60--61 LemmaA.1 with LARGE
THETA restriction for(A.3). New pages10,15,35,36,60,61 are two overlapping
tiles each;both tiles of every page are required. All preceding24images
are retained byte-for-byte. Full Section4 and appended source texts help
check dependencies;they do not replace rendered formulas.

crouzeix-palencia-v1.pdf: (3)p1,function algebra p2,Theorem6pp5--6.
chen-2023.pdf:Theorem1.1p2 finiteness only,no Corollary1.2 import.
chen-hu-2025.pdf:standing classp2145,Theorem1.2p2147,generalized covariance
(2.18)p2152,product conventions2151--2153,fixed-order2165,scaling2173,
finiteness2175,coefficient rate(5.15)p2180. These are auxiliary interfaces,
not new inputs of the independent mild construction or moment estimate.
Balan--Conus full source text is optional calibration context only.
''')
(PACKET/'mild-source-map.md').write_text('''Candidate repair:the original class/upper/sharp target is unchanged.

L:vertex-crude is a uniform bound over ALL positive vertexwise widths.
Its source3.1hypotheses are checked edge by edge:finite Gaussian-weighted
spatial spectral measures,positive covariances,temporal Laplace prefixes.
N0/N1/N2 are uniformly dominated by the full-covariance norms. Keep theta
above theta0 and choose theta0+n/t. This yields q_n(t),not the faulty
source all-time C^n*t^(2n)/n! without the extra exponential.

P:mild-construction proves the actual sourceDefinition2.1/(2.12) equation.
Closed Gaussian degree<=n includes annihilation/traces. Multiplication by
ANY coupled linear Gaussian coordinate is bounded on this degree space
by2sqrt(n+1) times its standard deviation;the Hermite proof is supplied.
V_a is used only at FIXED external widths. Uniform external-width tails
come separately from the mixed-vertex bound q_n,never from V_a.

Check all consumers:pointwise L2 inner convergence plus stationary uniform
spatial error;measurability;product continuity;Bochner/time domination;
d3 weak Green limits using bounded continuous vector functions/tightness;
inner limits at fixed external widths;then joint fixed-order convergence
and order tails. Full product W_a*u is identified by closedness and the
summable sqrt(n)*q_(n-1) bound. No uniqueness or source5(ii) proof assumed.
The moment estimate remains independent of this crude bound,but its mild
interpretation now explicitly has this additional proved branch.
The522finite rational cases are diagnostics,not analytic proof or Lean.
''')
with (PACKET/'calibration.md').open('a') as f:
    f.write('\nCurrent candidate adds independent vertexwise/mild construction:two new proofs;two old consumers change;all prior formal statements unchanged. No old review verdict covers these proofs. The522Gaussian cases include a coupled negative control. No lower theorem or source correction is introduced.\n')
req += [{'path':x} for x in ['mild-source-map.md','mild-multiplication-screen.py','mild-multiplication-screen.json','mild-rendering.json']]
req += new_images
dump(PACKET/'reading-map.json',{'pages':pages,'proofs':48,'scope':'Original full upper,independent mild construction and retained interfaces',
                              'new_proofs':change['new_proofs'],'changed_existing_proofs':change['changed_existing_proofs'],
                              'required_images':len(all_images),'no_prior_reports_in_packet':True,
                              'all_prior_formal_statements_unchanged':True})
dump(ROUND/'required-v1.json',req)
dump(ROUND/'manifest-v1.json',{p.relative_to(PACKET).as_posix():sha(p) for p in sorted(PACKET.rglob('*')) if p.is_file()})
(CAL/'images.txt').write_text('Native image-carrier/legibility calibration ONLY;not a mathematical review.\nOpen all36PNGs with direct Read using only file_path. The new author pages\n10,15,35,36,60,61 each have top/bottom windows with140pixel overlap covering\nall1600scaled vertical pixels and the full page width. Read both tiles.\nDimensions do not certify delivery;root independently checks native bytes.\n\n'+'\n'.join(x['path']+' '+x['sha256'] for x in all_images)+'\n')
dump(ROUND/'carrier-required-v1.json',[{'path':'images.txt'}]+all_images)
dump(ROUND/'carrier-manifest-v1.json',{p.name:sha(p) for p in sorted(CAL.iterdir()) if p.is_file()})
(ROUND/'carrier-contract-v1.txt').write_text('''This is ONLY a native image-carrier/legibility calibration,not science.
Read images.txt and open ALL36required source images exactly once with
direct Read using only file_path. Do not solve or verify mathematics,run
commands,browse,edit or delegate. Report any unreadable/truncated image.
Root separately verifies exact native image bytes/media;do not claim hashes.
Return ONLY a bare JSON object,no preamble,fence or afterword. Schema
subscription-review-report/1,verdict,confidence,source_coverage,checks with
claim CARRIER_ONLY and verdict/reason,findings(fatal,major,minor),
required_repairs,limitations. Choose your own legibility verdict/confidence.
State inside limitations:this is not a scientific review,proof check,
independent mathematical vote or circulation clearance.
''')
contract=(OLD/'contract-v1.txt').read_text();contract=contract[contract.index('Independently VERIFY OR REFUTE'):]
contract=contract.replace('explicit-justification revision','independent mild-construction revision').replace('C1--C17','C1--C19')
a=contract.index('C15:');b=contract.index('\nC16:',a)
contract=contract[:a]+'''C15: Uniform geometric tails and moment estimate. Verify L:uniform-series-tail and the full T:full-upper moment estimate,using B(T;2) for tails and B(T;1) for the final bound. The interval moment estimate and its geometric-series limit remain independent of P:mixed,L:crude-corrected and sourceSection5. The separate mild identification now explicitly uses the new vertexwise crude bound and Gaussian degree argument in C18/C19;do NOT require blanket crude-bound independence of that new branch. Check the updated consumers and five-stage trace,no circularity or lost original dimension/covariance scope. No first-moment constant is used.\n''' +contract[b:]
# C17's old known-mild-import description is superseded by the new construction.
contract=contract.replace('Known mild identification remains a separate import,not claimed independent of every Section5step.','The current mild identification is independently proved in C18/C19,not imported from Section5(ii).')
extra='''C18: NEW uniform arbitrary-vertex bound. Prove L:vertex-crude at all positive per-vertex spatial/temporal widths,all n,t,original full Gamma class/d1--3. Check exact sourceTheorem3.1edge hypotheses from author14/15images and norm assumptions from sourceLemmaA.1author60/61BOTHtiles. Positive finite Gaussian-weighted spectral measures,temporal prefixes,all-rho and heat-removal inequalities must justify bounds uniform over every vertex width. Keep theta>=theta0 and choose theta0+n/t;check P_n*n^(-2n)<=2^n/n!,the exponential e^(theta0*t),q_n,weighted summability and joint fixed-order limit. Green width precedes noise removal. Its constants may depend on the FIXED covariance;they must not enter the parameter-only sharp-scale constant. No false all-time source(5.3)/(5.4) uniformity or Riesz/angular restriction.

C19: NEW independent mild construction. Read actual source(2.12)p9/Definition2.1p10 and Section5(ii)pp35--36BOTHtiles. Prove P:mild-construction independently,not by importing its desired conclusion. Verify closed finite Gaussian degree of regularized terms and X_n including contractions;prove the occupied multiplication bound for arbitrary coupled H,F using normalized Hermite raising+lowering and closedness,not a vacuum/independence estimate. Check strongly measurable fields,spatial L2 continuity of smooth terms and uniform-in-y approximation error by JOINT stationarity. For fixed external widths,degree-bounded multiplication must preserve inner L2 convergence;uniform integrable time/Green domination gives actual I_(n,a)=inner limit,including n=1empty inner array. Mixed-vertex q_n bound then gives tails uniform in external a. V_a can diverge and is used ONLY for fixed-a product existence,never for uniform a->0tails. Check d3 continuous bounded vector functions,finite continuous partition-of-unity approximation,tightness and dominated time integration justify Green eta-first limits;no order exchange hidden. Prove I_(n,a)->X_n from JOINT fixed-order convergence after establishing inner limits. Prove the actual product W_a*u and full integral equal their series by closedness and sum sqrt(n)*q_(n-1). Then a->0at fixed N,then N->infinity. Verify original mild equation,data convention,no uniqueness assumed. Updated P:mixed now invokes the independently constructed series without a circular dependency;main upper constant unaffected. No new hypercontractivity or Skorohod model theorem imported. The522finite rational checks are not analytic proof.

'''
contract=contract.replace('Return ONLY a bare JSON object',extra+'Return ONLY a bare JSON object')
contract='''Fresh substantive candidate:two new independent vertexwise/mild-construction proofs and updated consumers of the ORIGINAL full upper. No prior reports are supplied. All old theorem statements and the original sharp target stay unchanged. The enlarged36PNGcohort requires its own carrier calibration before scientific dispatch;calibration is not a math vote. Independently decide verdict/confidence;HIGH remains the acceptance threshold,not a requested answer.\n\n'''+contract
contract=contract.replace('The main upper proof is independent of P:mixed and its crude series consumer.','The moment estimate and its geometric series-limit passage are independent of P:mixed and its crude series consumer;the separate new mild-construction branch is audited in C18/C19.')
(ROUND/'contract-v1.txt').write_text(contract)
(ROUND/'build-driver.txt.gz').write_bytes(gzip.compress(Path('<HOME>/.local/state/tmp/stratonovich-mild-candidate-build.txt').read_bytes(),mtime=0))
print(json.dumps({'change':change,'required_texts':sum(x.get('kind')!='image' for x in req),'required_images':len(all_images),'packet_members':len(list(PACKET.iterdir())),'carrier_only_members':len(list(CAL.iterdir()))},indent=2))
