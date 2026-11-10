from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import mpmath as mp
P=Path(__file__).resolve().parent
frozen=json.loads((P/'target-freeze-v1.json').read_text())
assert hashlib.sha256((P/'target-v1.md').read_bytes()).hexdigest()==frozen['sha256']
rows=[];max_precision=mp.mpf(0);max_formula=mp.mpf(0);bad_poly=[];bad_rate=[]
def spectral(ktext,vtext,ttext,dps):
 with mp.workdps(dps):
  k=mp.mpf(ktext);v=k*k if vtext=='critical' else mp.mpf(vtext);t=mp.mpf(ttext)
  b=mp.sqrt(1+k*k);h=k*k-v;K=max(mp.mpf(1),abs(v)/b);lam=mp.sqrt(max(mp.mpf(0),-h))
  if h>0:c=mp.cos(t*mp.sqrt(h));s=mp.sin(t*mp.sqrt(h))/mp.sqrt(h)
  elif h<0:c=mp.cosh(t*mp.sqrt(-h));s=mp.sinh(t*mp.sqrt(-h))/mp.sqrt(-h)
  else:c=mp.mpf(1);s=t
  A=mp.matrix([[0,b],[-h/b,0]]);X=mp.expm(t*A)
  Y=mp.matrix([[c,b*s],[-h*s/b,c]])
  sv=mp.svd_r(X,compute_uv=False);norm=max(sv);lognorm=mp.log(norm)
  rel=mp.norm(X-Y)/max(mp.mpf(1),mp.norm(X))
  log_bound=mp.log(8)+2*mp.log(1+K)+mp.log(1+t)+lam*t
  return dict(lognorm=+lognorm,formula_rel=+rel,log_bound=+log_bound,
              wrong_no_poly=+(lognorm-(mp.log(8)+2*mp.log(1+K)+lam*t)),
              wrong_zero_rate=+(lognorm-(mp.log(8)+2*mp.log(1+K)+mp.log(1+t))),
              lambda_value=+lam,E_norm=+(abs(v)/b),h=+h)
for k in ['0','1e-8','.5','2','10']:
 for v in ['-4','-1','0','.5','3','critical']:
  for t in ['0','.25','1','8','128']:
   a=spectral(k,v,t,40);b=spectral(k,v,t,80)
   with mp.workdps(80):
    diff=abs(a['lognorm']-b['lognorm']);max_precision=max(max_precision,diff)
    max_formula=max(max_formula,a['formula_rel'],b['formula_rel'])
    assert b['lognorm']<=b['log_bound']+mp.mpf('1e-60')
    assert b['formula_rel']<mp.mpf('1e-65')
    key=[k,v,t]
    if b['wrong_no_poly']>mp.mpf('1e-25'):bad_poly.append(key)
    if b['wrong_zero_rate']>mp.mpf('1e-25'):bad_rate.append(key)
    rows.append({'k':k,'V':v,'t':t,**{q:mp.nstr(w,28) for q,w in b.items()},'lognorm_precision_diff_unrounded':mp.nstr(diff,12)})
def mul(a,b):return [[sum(a[i][l]*b[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
q1=[[F(0),F(1)],[-F(1),F(0)]];q2=[[F(0),F(1,2)],[-F(2),F(0)]]
prod=mul(q2,q1);assert prod==[[-F(1,2),F(0)],[F(0),-F(2)]]
exact={'Q1':[[str(x) for x in z] for z in q1],'Q2':[[str(x) for x in z] for z in q2],'Q2Q1':[[str(x) for x in z] for z in prod],
 'ordered_norm_exact':'2','individual_positive_part_rates':['0','0'],
 'wrong_integrated_rate_bound':'1 < 2', 'position_actual':'-1/2','wrong_position_product':'0',
 'noncommuting':mul(q1,q2)!=prod,'scope':'Exact finite stable oscillators at quarter periods; NOT actual masked PDE/time-CM controls'}
assert exact['noncommuting']
with mp.workdps(80):
 shear=mp.matrix([[1,1],[0,1]]);quarter=mp.matrix([[0,mp.mpf('.5')],[-2,0]])
 norm=lambda a:max(mp.svd_r(a,compute_uv=False))
 ordered=norm(shear*quarter);scalar=norm(shear)*norm(quarter)
 assert ordered<scalar and mp.norm(shear*quarter-quarter*shear)>0
 noncommuting={'ordered_norm':mp.nstr(ordered,28),'scalar_product_norms':mp.nstr(scalar,28),'strict_gap':mp.nstr(scalar-ordered,28),'scope':'strict counterexample to equality; submultiplicativity is positive calibration'}
cells=[]
for B in [1,4,16]:
 for N in [2,7,31]:
  for frac in [F(0),F(1,10**6),F(1,8),F(999999,10**6)]:
   delta=1/(B*(F(N)+frac));ell=B*frac;n=N+1
   assert 0<delta<F(1,B) and 0<=ell<B
   assert delta*(N*B+ell)==1 and delta*n<=F(2,B)
   # For constant unit field the true nonempty-cell average is exactly1.
   wrong=str(frac) if frac else 'empty: omitted'
   cells.append({'B':B,'N':N,'partial_fraction':str(frac),'delta':str(delta),'last_length':str(ell),'partition_total':'1','delta_n':str(delta*n),'delta_n_upper':str(F(2,B)),'correct_last_average':'1' if frac else 'empty: omitted','wrong_full_B_average':wrong})
assert bad_poly and bad_rate
keys={(F(k), F(k)**2 if v=='critical' else F(v),F(t)) for k,v,t in [(r['k'],r['V'],r['t']) for r in rows]}
out={'scope':'finite evaluator consistency and explicit wrong-claim negative controls; NOT analytic AWS/PDE/uniform proof or certified enclosure',
 'precision':[40,80],'precision_comparison':'original unrounded mp objects at80digits before formatting',
 'static_raw_rows':len(rows),'static_distinct_parameter_configs':len(keys),'t0_identity_rows':sum(r['t']=='0' for r in rows),'nonzero_time_distinct_configs':sum(t!=0 for k,v,t in keys),
 'max_log_norm_precision_change':mp.nstr(max_precision,12),'max_expm_vs_spectral_relative_error':mp.nstr(max_formula,12),
 'wrong_no_polynomial_fail_rows':bad_poly,'wrong_zero_rate_fail_rows':bad_rate,
 'static_rows':rows,'exact_switched_stable':exact,'strict_noncommuting_norm_gap':noncommuting,'cell_rows':cells,
 'infinite_spatial_guard':'Accepted U Section5: (C_t f) tensor e_j, e_j orthonormal, pairwise distance sqrt(2)||C_t f||Lr. No finite grid replaces this infinite-rank no-compactness witness.',
 'formal':'no new Lean/compiler/fact count; finite arithmetic tests are not kernel certificates'}
# One complete JSON object per static/cell row, short enough for full delivery.
head={k:v for k,v in out.items() if k not in ['static_rows','cell_rows']}
s=json.dumps(head,indent=2)[:-2]+',\n  "static_rows": [\n'+',\n'.join('    '+json.dumps(r) for r in rows)+'\n  ],\n  "cell_rows": [\n'+',\n'.join('    '+json.dumps(r) for r in cells)+'\n  ]\n}\n'
assert json.loads(s)==out
(P/'interface-controls-v1.json').write_text(s)
print(json.dumps({k:out[k] for k in ['static_raw_rows','static_distinct_parameter_configs','t0_identity_rows','nonzero_time_distinct_configs','max_log_norm_precision_change','max_expm_vs_spectral_relative_error']}))
print('wrong_no_poly',len(bad_poly),'wrong_zero_rate',len(bad_rate),'cells',len(cells),'delivery_lines',len(s.splitlines()))
