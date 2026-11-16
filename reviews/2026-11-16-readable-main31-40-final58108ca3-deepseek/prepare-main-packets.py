from pathlib import Path
import subprocess,re,json,hashlib,shutil,datetime,argparse
ap=argparse.ArgumentParser();ap.add_argument('--output-root',required=True);ap.add_argument('--reference',required=True);ap.add_argument('--repo',required=True);args=ap.parse_args()
ROOT=Path(args.output_root);REF=Path(args.reference);PATH='notes/notes_stratonovich_ham_second_moment.tex';V={'old':'cdde711c248862f33207860107dd0e6b31d60852','new':'58108ca3065cb408eb13b06cc772fe71de546535'};sha=lambda b:hashlib.sha256(b).hexdigest();B={k:subprocess.check_output(['git','-C',args.repo,'show',v+':'+PATH]) for k,v in V.items()};S={k:b.decode() for k,b in B.items()};UNION=ROOT/'stratonovich-main62-readable-worker-union-20261116/WORKER-UNION.json';ub=UNION.read_bytes();U=json.loads(ub);assert sha(B['new'])=='85a7d3e9e2402a1e763391dea691d1b0c1e3f877974395f3939a59f5fd066901';assert U['old_module_sha256']==sha(B['old'])
def parse(s):
 D={};ns={}
 for d in re.finditer(r'\\begin\{(theorem|lemma|proposition|corollary|nogo)\}.*?\\end\{\1\}',s,re.S):
  e=d.group(1);ns[e]=ns.get(e,0)+1;l=next((q for q in re.findall(r'\\label\{([^}]+)\}',d.group()) if q.startswith(('T:','L:','P:','C:'))),None)
  if l:D[l]=(d,ns[e])
 arr=[]
 for i,m in enumerate(re.finditer(r'\\begin\{proof\}(?:\[[^\n]*\])?.*?\\end\{proof\}',s,re.S),1):
  h=m.group().split('\n')[0];x=re.search(r'\\ref\{([^}]+)\}',h);l=x.group(1) if x else max((d.start(),l) for l,(d,_) in D.items() if d.start()<m.start())[1];d,n=D[l];arr.append({'global_main_ordinal':i,'label':l,'environment':d.group(1),'environment_ordinal':n,'statement_lf':[s.count('\n',0,d.start())+1,s.count('\n',0,d.end())+1],'statement_sha256':sha(d.group().encode()),'proof_lf':[s.count('\n',0,m.start())+1,s.count('\n',0,m.end())+1],'proof_environment_sha256':sha(m.group().encode()),'proof_environment_bytes':len(m.group().encode()),'proof_heading':h,'statement_chars':[d.start(),d.end()],'proof_chars':[m.start(),m.end()]})
 return arr,D
P={};D={}
for k,s in S.items():P[k],D[k]=parse(s)
assert len(P['old'])==len(P['new'])==len(U['proofs'])==62
for a,b,u in zip(P['old'],P['new'],U['proofs']):assert a['global_main_ordinal']==b['global_main_ordinal']==u['ordinal'] and a['label']==b['label']==u['owner'] and a['proof_environment_sha256']==u['old_proof_sha256']
def slicechars(k,a,z):
 s=S[k];a=s.rfind('\n',0,a)+1;end=s.find('\n',z);z=len(s) if end<0 else end+1;return s[a:z].encode(),[s.count('\n',0,a)+1,s.count('\n',0,z)]
def block(k,kind):
 s=S[k];ps=P[k]
 if kind=='01-10':return [slicechars(k,ps[0]['statement_chars'][0],ps[9]['proof_chars'][1])]
 if kind=='11-20':return [slicechars(k,ps[10]['statement_chars'][0],ps[11]['proof_chars'][1]),slicechars(k,s.index('\\section{A static phase estimate at first variance order}'),ps[19]['proof_chars'][1])]
 if kind=='21-30':return [slicechars(k,ps[20]['statement_chars'][0],ps[26]['proof_chars'][1]),slicechars(k,s.index('\\section{Finite-order checks in one space dimension}'),ps[29]['proof_chars'][1])]
 if kind=='31-40':return [slicechars(k,s.index('\\section{Upper bounds for spatial exponents at most one}'),s.index('\\section{Riesz bounds by interpolation with static noise}')-1)]
 if kind=='41-50':return [slicechars(k,s.index('\\section{Riesz bounds by interpolation with static noise}'),ps[49]['proof_chars'][1])]
 if kind=='51-62':
  end=re.search(r'(?m)^\\chapter\{',s[ps[61]['proof_chars'][1]:]);assert end
  return [slicechars(k,ps[50]['statement_chars'][0],ps[61]['proof_chars'][1]+end.start()-1)]
focus={'01-10': 'Reconstruct Jensen and its conditional numerical specialization; exact\nmixed Stratonovich products and full nonnegative second-moment series retaining\nself/unequal/empty chains; white low-order calibration; homogeneous damped norms\nand temporal tails; translated covariance Cauchy--Schwarz; complete pairing\nproduct/fusion estimate; spatial Wick-measure and joint vertexwise limits; corrected\ncrude and uniform vertex bounds. Check exact root-forward versus terminal chain\nconventions, finite positive measures, all kernel/factorial/Laplace constants,\nspectral versus physical masses, Radon/singular covariance, dimensions1–3 and\nGreen smoothing before noise removal. Track induction/fusion subcases, disjoint\npair temporal tails, boundary faces, joint arbitrary relative widths, first-chaos\nversus Stratonovich orders and uniformity. No orthogonality of different ordered\nStratonovich terms, arbitrary covariance-order wave comparison, or imported\nsolution-series identification may replace the actual deduction. Source results\nare imported only at their explicit stated hypotheses; no source-image fidelity\nreview is assigned.\n', '11-20': 'Reconstruct independent canonical mild-series construction and conditional\nsource identification, the common-pairing majorant and its scale limitation,\nstatic phase contraction/variance calculation (including second-order mean),\ncomplex numerical-range/resolvent/holomorphic-function bound, Gaussian Fock\nform and exact finite-word cutoff, all static orders, interaction blocks and\ndimension-independent interval contractions. Check every domain and positivity/\nself-adjointness distinction, complex parameter/root/power order, noncommuting\noperator word, finite versus full cutoff use, real/complex Sobolev weights,\nfree-group growth, spatial/temporal covariance constants, both creation and\nannihilation, and all exponent/factorial identities. Preserve static first-\nvariance scope versus all-order bounds, genuine product/cocycle assumptions,\nnegative/zero cases, no arbitrary-phase covariance monotonicity and no scalar\nsolution-value multiplication. Imported CP/Janson statements may be used only\nas explicitly stated in the proof; check their target applications without\nclaiming new primary-PDF/source-fidelity or full external-theorem review.\n', '21-30': 'Reconstruct complex sums with changing phase weights, coefficient inventory\nproduct, the full fixed degree-split estimate, interval coefficients, terminal\nWick formula, scaled-moment series tails, full all-model upper scale, and the\nthree finite-order white/static/Riesz calculations. Check numerical-range and\nchanging-weight constants, finite-word and Fourier/Fock controls, Cauchy\ncoefficient extraction, no unjustified infinite trace/cutoff limit, both chain\nsplits and pairings, covariance majorant versus Gaussian projection/conditional\nJensen use, full canonical series and order of source/Green/time limits.\nFor the upper theorem keep genuine independent interval fields and their actual\nnonnegative diagram domination; do not replace by false arbitrary-phase\ncovariance order. Check all dyadic scales, low orders, prefactors, admissible\nparameter/dimension ranges and zero covariance. Finite-order calculations must\nretain exact Green/kernel/covariance normalization, all self/unequal/empty split\ncontributions and strict scopes, without Skorohod substitution or sharp-constant\nidentification. Imported mathematical inputs may be used as stated only when\nnot assigned in this packet; every assigned proof must itself be reconstructed.\n', '31-40': 'Reconstruct all ten direct spatial-bound, convolution, moment-upper and obstruction arguments. Check the determinant-one chain-increment change, opening/closing labels, backward integration, white versus Riesz covariance, independent regularization widths, spectral ball masses, translated Gaussian Fourier bound, endpoint alpha=1 treatment, every temporal-pairing symmetry factor, conjugate Holder exponents, Gamma/factorial constants and exact kappa. Preserve d=1 versus d=2/3 hypotheses, additional spatial-maximum condition, zero/nonzero and small/large parameter boundaries, source-dependent/Jensen calibration qualifications, no limit interchange and no asserted sharp constants. The higher-dimensional counterexamples obstruct a spatial supremum method, not existence or the full-scale theorem. Reconstruct each assigned conclusion, including unchanged calibration/corollary proofs; do not replace them with cited baseline conclusions.\n', '41-50': 'Reconstruct all ten static-input, interpolation, planar/product/plane endpoint, endpoint-closure and three-dimensional conditional-transfer proofs. Check actual imported static coefficient estimates under their stated generalized-covariance, homogeneity and Dalang hypotheses; coefficient-wise versus moment growth inputs; all kernel/Holder exponents and normalization constants; angular/polar measure identities and positive definiteness; Gaussian regularization before multiplication/fractional powers; endpoint zero cases and arbitrary independent widths; invertible pushforwards versus transformed wave kernels; finite positive sums and their constants. Preserve the conditional endpoint factorization assumption, actual target/endpoint original wave kernels, anisotropic covariance scopes and nonuniformity of mixtures or endpoints. Check the physical/spectral energy lemma only as supplied unassigned boundary input here, applying its exact hypotheses without assigning its proof. Distinguish source finiteness, quantitative coefficient rates and moment-law assertions; no primary-PDF proof or sharp-constant identification is requested.\n', '51-62': 'Reconstruct all twelve proofs, including unchanged three-dimensional endpoint corollaries and static continuity. Check actual endpoint spectra/masses and transformed covariance hypotheses; physical versus spectral Sobolev energy for a Radon covariance, Fourier factors, trace/translation and approximation/duality limits; static endpoint canonical expansion and imported moment-law hypotheses; temporal Holder exponents, source/Green/noise limit order, beta/kappa parameter dependence, mean versus full moment coefficients, nonnegative series and scalar type extraction, lower comparisons and near-static ratio/continuity domains. For clock arguments derive all low-order Laplace factors and the full cross-transform, spectral resolvent, analytic power and Brownian average identities with justified Fubini/regularization removal and nonzero/strictness qualifications. Preserve fixed-order versus solution transforms, gap damping versus physical horizons, correlated clocks versus spatial paths, and the restricted direct-substitution no-go; do not extend it to all two-clock representations, source constants or Skorohod results. No arbitrary source/large-time/parameter limit interchange or numerical constant identification is allowed.\n'}
for number,kind,lo,hi in [(65,'01-10',1,10),(66,'11-20',11,20),(67,'21-30',21,30),(68,'31-40',31,40),(69,'41-50',41,50),(70,'51-62',51,62)]:
 o=ROOT/('stratonovich-readable-main'+kind+'-deepseek-58108ca3-20261116');o.mkdir(exist_ok=True);(o/'inputs').mkdir(exist_ok=True);(o/'workspace').mkdir(exist_ok=True)
 for f in ['model-profile.json','MODEL-LIMITS.json']:shutil.copyfile(REF/f,o/f)
 files=[]
 def add(name,b,k,lf,role):
  b.decode();assert b''.join(B[k].splitlines(keepends=True)[lf[0]-1:lf[1]])==b;(o/'inputs'/name).write_bytes(b);files.append({'path':'inputs/'+name,'bytes':len(b),'sha256':sha(b),'source_revision':V[k],'source_path':PATH,'selection':'LF_RANGE','source_lf':lf,'role':role})
 for k in ['old','new']:
  for i,(b,lf) in enumerate(block(k,kind),1):add(k+'-target-'+str(i)+'.txt',b,k,lf,'ASSIGNED '+k.upper()+' scientific target block. Only global main proof ordinals '+str(lo)+'–'+str(hi)+' assigned; all complete declarations/proofs and intervening scientific definitions retained.')
 ctx=(REF/'inputs/context-model-assumptions.txt').read_bytes();assert B['old'].count(ctx)==1;at=B['old'].index(ctx);lf=[B['old'][:at].count(b'\n')+1,B['old'][:at+len(ctx)].count(b'\n')];add('context-model-assumptions.txt',ctx,'old',lf,'UNASSIGNED exact model/covariance/data/zero case.')
 s=S['old'];a=s.index('The solution is the Stratonovich expansion');z=s.index('The full mixed-term expansion',a);b,lf=slicechars('old',a,z-1);add('context-canonical-expansion.txt',b,'old',lf,'UNASSIGNED canonical ordered kernel, terminal endpoints and two-chain/Wick conventions.')
 # Unassigned complete scientific argument blocks contain no administrative review appendices.
 if lo>=11:
  for i,(b,lf) in enumerate(block('old','01-10'),1):add('context-baseline-main01-10-'+str(i)+'.txt',b,'old',lf,'UNASSIGNED baseline scientific covariance/kernel/construction inputs; their proofs are not assigned or counted.')
 if lo>=21:
  for i,(b,lf) in enumerate(block('old','11-20'),1):add('context-baseline-main11-20-'+str(i)+'.txt',b,'old',lf,'UNASSIGNED baseline mild/static/complex/Fock input context; no extra proof review assigned.')
 if lo>=41:
  for i,(b,lf) in enumerate(block('old','31-40'),1):add('context-baseline-main31-40-'+str(i)+'.txt',b,'old',lf,'UNASSIGNED complete direct spatial/convolution input context; these upstream proofs are not assigned or counted.')
 if lo>=51:
  for i,(b,lf) in enumerate(block('old','21-30'),1):add('context-baseline-main21-30-'+str(i)+'.txt',b,'old',lf,'UNASSIGNED baseline coefficient, full upper and series-tail context; these proofs are not assigned or counted.')
  for i,(b,lf) in enumerate(block('old','41-50'),1):add('context-baseline-main41-50-'+str(i)+'.txt',b,'old',lf,'UNASSIGNED baseline endpoint constructions and conditional transfer context, including preceding parameter definitions; proofs not assigned or counted.')
 if lo==41:
  ss=S['old'];a=ss.index('\\section{Physical and spectral energy for measure covariances}');z=ss.index('\\chapter{Static comparisons and the clock obstruction}',a);b,lf=slicechars('old',a,z-1);add('context-physical-spectral-energy.txt',b,'old',lf,'UNASSIGNED complete scientific energy section for the explicitly invoked forward boundary input; its proof is not assigned here.')
 # Complete external declarations for scientific qualifications, not new assigned proofs.
 for lab in ['T:first','T:intrinsic-second-moment','T:intro-second-moment']+(['T:full-upper'] if lo==1 else []):
  if lab in D['old']:
   d,_=D['old'][lab];b,lf=slicechars('old',d.start(),d.end());add('context-'+lab.replace(':','-')+'.txt',b,'old',lf,'UNASSIGNED complete boundary theorem declaration; no target deduction may be skipped by treating a cited conclusion as an oracle.')
 if lo==1:
  d,_=D['old']['P:mild-construction'];b,lf=slicechars('old',d.start(),d.end());add('context-P-mild-construction.txt',b,'old',lf,'UNASSIGNED complete canonical mild-construction declaration used as a stated boundary; its proof is not assigned here.')
 # Definitions of the model exponent and intro hypotheses are in this exact scientific equation.
 at=s.index('\\label{E:kappa}');a=s.rfind('\\begin{',0,at);env=re.search(r'\\begin\{([^}]+)\}',s[a:]).group(1);z=s.index('\\end{'+env+'}',at)+len('\\end{'+env+'}');b,lf=slicechars('old',a,z);add('context-E-kappa.txt',b,'old',lf,'UNASSIGNED exact exponent definition.')
 # Complete scientific cross-reference declarations, explicitly unassigned.
 if lo==31:
  rr=re.search(r'\\begin\{remark\}\[Purpose of these calculations\]\\label\{R:G1-scope\}.*?\\end\{remark\}',s,re.S);assert rr;b,lf=slicechars('old',rr.start(),rr.end());add('context-R-G1-scope.txt',b,'old',lf,'UNASSIGNED complete finite-order scope remark, for the target comparison qualification.')
 def add_external(name,path,b,lf,role):
  source=subprocess.check_output(['git','-C',args.repo,'show',V['old']+':'+path]);assert b''.join(source.splitlines(keepends=True)[lf[0]-1:lf[1]])==b
  (o/'inputs'/name).write_bytes(b);files.append({'path':'inputs/'+name,'bytes':len(b),'sha256':sha(b),'source_revision':V['old'],'source_path':path,'selection':'LF_RANGE','source_lf':lf,'role':role})
 ip='notes/integrated_intrinsic_constant.tex';ib=subprocess.check_output(['git','-C',args.repo,'show',V['old']+':'+ip]);add_external('context-intrinsic-constant.txt',ip,ib,[1,len(ib.splitlines())],'UNASSIGNED complete baseline intrinsic-constant module for the explicit contrasting/navigation theorem reference. Its proofs are not assigned or counted; it cannot replace any target deduction.')
 if lo==1:
  for path,labels in [('notes/integrated_occupation_ceiling.tex',['T:intrinsic-occupation-ceiling','C:intrinsic-spatial-bracket']),('notes/integrated_white_evaluation.tex',['T:white-moment-bounds'])]:
   raw=subprocess.check_output(['git','-C',args.repo,'show',V['old']+':'+path]);ss=raw.decode()
   for label in labels:
    dd=next(x for x in re.finditer(r'\\begin\{(theorem|corollary|proposition|lemma)\}.*?\\end\{\1\}',ss,re.S) if '\\label{'+label+'}' in x.group());a=ss.rfind('\n',0,dd.start())+1;z=ss.find('\n',dd.end());z=len(ss) if z<0 else z+1
    add_external('context-'+label.replace(':','-')+'.txt',path,ss[a:z].encode(),[ss.count('\n',0,a)+1,ss.count('\n',0,z)],'UNASSIGNED complete scientific navigation/boundary declaration cited outside target proofs; its proof is not assigned or supplied, and it cannot replace any assigned derivation.')
  ss=S['old'];a=ss.index('\\section{Upper bounds for spatial exponents at most one}');z=ss.find('\n',ss.index('\\label{S:d1-upper}',a))+1
  add('context-navigation-S-d1-upper.txt',ss[a:z].encode(),'old',[ss.count('\n',0,a)+1,ss.count('\n',0,z)],'UNASSIGNED complete navigation section heading cited outside target proofs, not a proof or mathematical oracle.')
 nogos={1:[5,7,20],11:[11,14,15],21:[],31:[6,8,10],41:[],51:[9,12,13,17,18]}[lo]
 for n in nogos:
  path='notes/no-go/'+('pairings' if n in [5,6,7,10,17,18] else 'phase' if n in [14,15,20] else 'covariance')+'.tex';raw=subprocess.check_output(['git','-C',args.repo,'show',V['old']+':'+path]);ss=raw.decode();label='P:nogo-'+f'{n:02}';dd=next(m for m in re.finditer(r'\\begin\{nogo\}.*?\\end\{nogo\}',ss,re.S) if '\\label{'+label+'}' in m.group());a=ss.rfind('\n',0,dd.start())+1;z=ss.find('\n',dd.end());z=len(ss) if z<0 else z+1;b=ss[a:z].encode();lf=[ss.count('\n',0,a)+1,ss.count('\n',0,z)];add_external('context-'+label.replace(':','-')+'.txt',path,b,lf,'UNASSIGNED complete scientific counterclaim declaration for an explicit target reference; its proof is not assigned, supplied or counted.')
 assigned=[]
 for a,b in zip(P['old'][lo-1:hi],P['new'][lo-1:hi]):
  def clean(q):return{k:v for k,v in q.items() if not k.endswith('_chars')}
  assigned.append({'global_main_ordinal':a['global_main_ordinal'],'label':a['label'],'old':clean(a),'new':clean(b),'statement_unchanged':a['statement_sha256']==b['statement_sha256'],'current_body_equals_baseline':a['proof_environment_sha256']==b['proof_environment_sha256']})
 pm={'source_file':PATH,'old_revision':V['old'],'source_revision':V['new'],'old_main_sha256':sha(B['old']),'new_main_sha256':sha(B['new']),'old_main_bytes':len(B['old']),'new_main_bytes':len(B['new']),'assigned_global_ordinals':[lo,hi],'hash_convention':'Complete UTF8 statement/proof environment begin through end closing brace, excluding following newline. Global literal-main LF/ordinals; no input/include expansion. Explicit optional proof heading resolves deferred owner.','proofs':assigned};assert all(q['statement_unchanged'] for q in assigned);(o/'PROOF-MANIFEST.json').write_text(json.dumps(pm,indent=2)+'\n')
 c='''# Assigned task: ten rewritten main-file proofs

Independently compare each complete OLD and NEW assigned proof, its full
statement, definitions and hypotheses. Reconstruct substantive deductions with
checkable public equations/estimates and evaluate every added roadmap, heading
and explanation. Retained statement/display bytes alone are not mathematical
evidence; do not treat OLD as an oracle or silently repair the source.
Read unchanged proofs explicitly too; no hash match establishes completion.

Only the ten global main-file ordinals in the inventory are assigned. OLD/NEW
target frames are exact scientific LF selections, not an expanded book. Literal
input directives are source syntax, not instructions to access files. All
allowed mathematical context is embedded. Boundary context proofs are explicitly
UNASSIGNED and must not be counted as assigned completion. Check consumer uses
at their stated hypotheses. If a target invokes another assigned result, derive
both assigned arguments rather than using its baseline conclusion as an oracle.
If genuinely necessary context is absent, report the precise limitation and
PARTIAL/UNCERTAIN reading rather than invent it. Distinguish introduced defects
from pre-existing concerns and imported facts from proofs given here.

'''+focus[kind]+'''
Do not browse, execute tools, read external files, delegate, edit or contact
anyone. Everything allowed is embedded. This is a bounded proof-readability
argument-preservation assignment, not whole-book, primary-source/PDF/image,
Lean quotation/certificate, render, human verification or release acceptance.

# Output contract

Begin with:
# Review Result
Category: proof-readability-equivalence
Model: <actual model identity if known>
Verdict: PASS | PASS_WITH_NOTES | FAIL | INCONCLUSIVE
Confidence: high | medium | low

Verdict/confidence are unforced. Give exactly one '## <proof label>' section for
each assigned label in inventory order, reporting:
- Global main ordinal: <integer>
- Old reading: COMPLETE | PARTIAL | NOT_READ
- New reading: COMPLETE | PARTIAL | NOT_READ
- Argument preservation: PRESERVED | CHANGED | UNCERTAIN
- New explanations: JUSTIFIED | CONCERN | UNCERTAIN
- Evidence: public equations/estimates and concrete deductions using labels or
  OLD/NEW GLOBAL source LF ranges, not just mechanical or source-label summaries.
- Lost steps/qualifiers, unresolved/missing deductions and pre-existing concerns.

End with '## Findings and limits'. Honest partial or inconclusive outcomes are
allowed. A partially read assigned proof forbids claiming full assignment
completion. Do not demand or disclose private reasoning; provide only checkable
public mathematical derivations. Aim about 6000 words or less while giving
substantive evidence for all ten proofs; name any uncompleted required steps.
''';c=re.sub(r'\bten\b',str(hi-lo+1),c);c=(o/'CONTRACT.md').read_text();assert 'For every assigned proof, enumerate its original logical steps' in c
 mi={'source_file':PATH,'old_revision':V['old'],'new_revision':V['new'],'assigned_ordinals':[lo,hi],'proofs':[{'global_main_ordinal':q['global_main_ordinal'],'label':q['label'],'old_statement_lf':q['old']['statement_lf'],'new_statement_lf':q['new']['statement_lf'],'old_proof_lf':q['old']['proof_lf'],'new_proof_lf':q['new']['proof_lf'],'old_proof_heading':q['old']['proof_heading'],'new_proof_heading':q['new']['proof_heading']} for q in assigned],'line_convention':'GLOBAL literal-main LF, not prompt/frame local lines; context proofs UNASSIGNED.'}
 prompt=c.encode()+b'\n# Exact assigned proof inventory\n'+json.dumps(mi,indent=2).encode()+b'\n\n';frames=[]
 for f in files:
  b=(o/f['path']).read_bytes();name=Path(f['path']).name;prompt+=('===== BEGIN '+name+' =====\n'+json.dumps({k:f[k] for k in ['source_path','source_revision','selection','source_lf','role','bytes','sha256']})+'\n===== RAW UTF8 SOURCE =====\n').encode();at=len(prompt);prompt+=b;frames.append({'path':f['path'],'payload_byte_offset':at,'payload_bytes':len(b),'payload_sha256':sha(b)});prompt+=('\n===== END '+name+' =====\n\n').encode()
 (o/'INPUT.txt').write_bytes(prompt)
 m={'review_record_id':'RP0'+str(number),'scope':'Exactly global literal-main ordinals '+str(lo)+'–'+str(hi)+' old/new proof preservation; other context proofs unassigned; no global acceptance','old_revision':V['old'],'source_revision':V['new'],'source_file':PATH,'old_main_sha256':sha(B['old']),'new_main_sha256':sha(B['new']),'old_main_bytes':len(B['old']),'new_main_bytes':len(B['new']),'assigned_global_ordinals':[lo,hi],'proof_labels':[q['label'] for q in assigned],'input_files':files,'embedded_frames':frames,'prompt_sha256':sha(prompt),'prompt_bytes':len(prompt),'contract_sha256':sha(c.encode()),'proof_manifest_sha256':sha((o/'PROOF-MANIFEST.json').read_bytes()),'profile_sha256':sha((o/'model-profile.json').read_bytes()),'model_limits_sha256':sha((o/'MODEL-LIMITS.json').read_bytes()),'route':'paper-review-deepseek','requested_model':'deepseek/deepseek-v4-pro','requested_variant':None,'pure_mode':True,'agent':'artifact-reviewer','all_tools_denied':True,'combined_reasoning_public_output_cap':98304,'timeout_seconds':3600,'coordinator_launch_limit':1,'coordinator_retry_continuation_fallback':False,'native_hidden_requests_not_inferred_from_process_count':True,'provider_calls_started_during_preparation':0,'status':'PREPARED_AWAITING_OWNER_SCOPE_REVIEW_PREFLIGHT_AND_FREEZE','coordinator_identity_crosscheck':{'external_worker_union_sha256':sha(ub),'all62_old_ordinals_owners_body_hashes_match_old_retained_inventory':True,'all62_new_owners_and_body_hashes_freshly_recomputed':True,'not_reviewer_input':True},'no_preflight_claim':'No native/provider call, admission, observed tool denial or reading evidence produced.'};(o/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');
 if Path(__file__).resolve()!=(o/'prepare-main-packets.py').resolve():shutil.copyfile(__file__,o/'prepare-main-packets.py')
 print(m['review_record_id'],len(prompt),sha(prompt),[(q['global_main_ordinal'],q['label']) for q in assigned])
