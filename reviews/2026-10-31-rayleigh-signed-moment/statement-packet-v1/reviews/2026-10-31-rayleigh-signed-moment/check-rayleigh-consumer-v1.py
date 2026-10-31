from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
import json,hashlib
P=Path(__file__).resolve().parent
freeze=json.loads((P/'target-freeze-v1.json').read_text());assert hashlib.sha256((P/'target-v1.md').read_bytes()).hexdigest()==freeze['sha256']
def case(profile,delta_spec,dps):
 with mp.workdps(dps):
  if isinstance(delta_spec,tuple):
   branch,n=delta_spec;angle=(mp.mpf('.5') if branch=='high' else mp.mpf('1.5'))*mp.pi+2*mp.pi*n
   delta=mp.exp(-angle);score=mp.mpf('.75') if branch=='high' else mp.mpf('.25');a=mp.sqrt(2*score);kind='linear'
  else:delta=mp.mpf(delta_spec);kind=profile;a=mp.mpf(1)
  if kind=='zero':rs=mp.mpf(0);score=mp.mpf(0);g=lambda r:mp.mpf(0)
  elif kind=='linear':rs=a;score=a*a/2;g=lambda r:a*r
  else:
   c=mp.mpf('.25');nu=mp.mpf('1.5');rs=(c*nu)**(1/(2-nu));score=c*rs**nu-rs*rs/2;g=lambda r:c*r**nu
  ustar=rs/mp.sqrt(delta)
  points=sorted(set([mp.mpf(0),max(mp.mpf(0),ustar-32),ustar,ustar+32]))+[mp.inf]
  # Center only the exponent, not the radius domain. u>=0 throughout.
  j=mp.quad(lambda u:u*mp.exp((g(mp.sqrt(delta)*u)-delta*u*u/2-score)/delta),points)
  q=score+delta*mp.log(j)
  if kind in ['zero','linear']:
   z=mp.mpf(0) if kind=='zero' else a/mp.sqrt(delta)
   jexact=mp.exp(-score/delta)+z*mp.sqrt(2*mp.pi)*(1+mp.erf(z/mp.sqrt(2)))/2
   residual=abs(j-jexact)/jexact
  else:residual=None
  return {'delta':+delta,'score':+score,'normalized_log_integral':+q,'excess_over_score':+(q-score),'centered_integral':+j,'formula_relative_residual':None if residual is None else +residual}
rows=[];maxdiff=mp.mpf(0);maxcase=None;formula_max={40:(mp.mpf(0),None),80:(mp.mpf(0),None)}
specs=[(p,d) for p in ['zero','linear','power3over2'] for d in ['.25','.0625','.015625','.00390625']]+[('oscillating_linear',(b,n)) for b in ['high','low'] for n in [0,1,2]]
wrongfinite=[];wrongsubseq=[]
for profile,spec in specs:
 values={prec:case(profile,spec,prec) for prec in [40,80]}
 label={'profile':profile,'delta_spec':list(spec) if isinstance(spec,tuple) else spec}
 with mp.workdps(80):
  diff=abs(values[40]['normalized_log_integral']-values[80]['normalized_log_integral'])
  if diff>maxdiff:maxdiff=diff;maxcase=label
  for prec in [40,80]:
   v=values[prec]['formula_relative_residual']
   if v is not None and v>formula_max[prec][0]:formula_max[prec]=(v,label)
  if values[80]['excess_over_score']>mp.mpf('1e-25'):wrongfinite.append(label)
  if profile=='oscillating_linear' and spec[0]=='high' and values[80]['normalized_log_integral']>mp.mpf('.25'):wrongsubseq.append(label)
  rows.append({**label,'per_precision':{str(prec):{k:None if v is None else mp.nstr(v,30) for k,v in values[prec].items()} for prec in [40,80]},'unrounded_normalized_log_precision_diff':mp.nstr(diff,14)})
assert len(wrongfinite)==14 and len(wrongsubseq)==3
cutoffs=[]
for A1 in [F(0),F(1,4),F(1)]:
 for cball in [F(1,2),F(1)]:
  for kap in [9,10]:
   for B in [1,4,16,64]:
    # nu=3/2. Exact equivalent squared cutoff after positive squaring.
    lhs=16*A1*A1*B**9;rhs=cball*B**kap;holds=lhs<=rhs
    if kap==10 and B==64:assert holds
    if kap==9 and A1==1:assert not holds
    if A1==0:assert holds
    cutoffs.append({'A1':str(A1),'c_ball':str(cball),'kappa_ball':kap,'B':B,'squared_lhs':str(lhs),'squared_rhs':str(rhs),'cutoff_holds':holds})
diagonal=[]
for n in [4,8,12]:
 d=F(1,2**n)
 for B in [1,2,4]:diagonal.append({'n':n,'delta':str(d),'B':B,'min(1,delta*2^B)':str(min(F(1),d*2**B)),'kind':'fixedB'})
 assert d*2**n==1
 diagonal.append({'n':n,'delta':str(d),'B':n,'min(1,delta*2^B)':'1','kind':'diagonalB=n'})
normalizers=[{'delta':d,'correct_Rayleigh_mass':'1','wrong_omit_1_over_delta_mass':d,'wrong_upper_for_unit_observable':True} for d in ['.25','.0625','.015625','.00390625']]
out={'scope':'finite scalar quadrature/evaluator/quantifier comparators,NOT actual PDE/AWS or certified enclosures','precision':[40,80],
 'quadrature_rows':rows,'raw_quadrature_count':len(rows),'zero_signal_rows':4,'wrong_exact_finite_Laplace_claim_failures':wrongfinite,'wrong_lower_subsequence_score_failures':wrongsubseq,
 'max_unrounded_normalized_log_precision_change':mp.nstr(maxdiff,14),'precision_maximizing_case':maxcase,
 'formula_residual_max_by_precision':{str(prec):{'maximum':mp.nstr(v[0],14),'case':v[1]} for prec,v in formula_max.items()},
 'formula_scope':'zero/linear profiles only; power3over2 has precision consistency only,not a closed-form residual or certified error',
 'cutoff_rows':cutoffs,'cutoff_scope':'48exactrational parameter configurations;16A1=0rows trivial; sufficient exponent10 eventual only; critical exponent9 fails when constants demand it',
 'diagonal_rows':diagonal,'diagonal_scope':'exact array min(1,delta*2^B): fixedB tends0,delta_n=2^-n,B_n=n gives1; not actual waveerror',
 'wrong_normalizer_rows':normalizers,
 'old_tail_reuse':'front4/quarterexponent old BT/Lean scalar fixture unchanged,NOT rerun here','new_Lean_or_compiler':False}
# Whole row objects on individual lines; every value retained in direct JSON.
keys=['quadrature_rows','cutoff_rows','diagonal_rows'];header={k:v for k,v in out.items() if k not in keys}
s=json.dumps(header,indent=2)[:-2]
for key in keys:s+=',\n  '+json.dumps(key)+': [\n'+',\n'.join('    '+json.dumps(v) for v in out[key])+'\n  ]'
s+='\n}\n';assert json.loads(s)==out
(P/'rayleigh-controls-v1.json').write_text(s)
print(json.dumps({'quadratures':len(rows),'max_precision_diff':mp.nstr(maxdiff,14),'max_case':maxcase,'formula_maxima':out['formula_residual_max_by_precision'],'wrong_finite_count':len(wrongfinite),'wrong_subseq_count':len(wrongsubseq),'cutoff_rows':len(cutoffs),'diagonal_rows':len(diagonal),'delivery_lines':len(s.splitlines())}))
