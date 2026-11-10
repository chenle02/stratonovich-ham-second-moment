"""Auxiliary EXACT torus factor diagnostics; not whole-space K singular values."""
from pathlib import Path
import json,itertools
import numpy as np
import sympy as s
Q=s.Rational

def diagonal_trace(d,rho,N,u=8):
 # Sum in slabs to keep local memory small even in dimension3.
 axis=np.arange(-N,N+1,dtype=float)/rho
 if d==1:return float(np.sum((1+axis*axis)**(-u/2)))
 yz=axis[:,None]**2+axis[None,:]**2
 if d==2:return float(np.sum((1+yz)**(-u/2)))
 return float(sum(np.sum((1+x*x+yz)**(-u/2)) for x in axis))

cal=[]
for d in [1,2,3]:
 exact=sum((s.Integer(1)+sum(s.Integer(k)**2 for k in ks))**(-4) for ks in itertools.product(range(-1,2),repeat=d))
 value=diagonal_trace(d,1,1)
 assert abs(value-float(exact))<2e-14
 cal.append({'d':d,'rho':1,'cube_cutoff':1,'exact_q32_gamma_quarter_diagonal_trace':str(exact),'floating_value':value,'absolute_error':abs(value-float(exact)),'zero_mode_exact':'1'})
rows=[]
for d in [1,2,3]:
 for rho in [1,2,4]:
  for mult in [8,16]:
   N=mult*rho;value=diagonal_trace(d,rho,N)
   # Max-norm dyadic shells: count<=5^d 2^(jd)(N+1)^d,
   # diagonal<=rho^u (2^j(N+1))^-u; u=8>d.
   tail=5**d*rho**8*(N+1)**(d-8)/(1-2**(d-8))
   rows.append({'d':d,'rho':rho,'cube_cutoff':N,'computed_factor_trace':value,'analytic_tail_upper_evaluated_float':tail,'normalized_trace_lower':value/rho**d,'normalized_trace_upper':(value+tail)/rho**d,'normalized_S32_factor_lower':value**(1/32)/rho**(d/32),'normalized_S32_factor_upper':(value+tail)**(1/32)/rho**(d/32)})
params=[]
for d in [1,2,3]:
 for a in [Q(1,2),Q(9,10),Q(99,100)]:
  alpha=s.Integer(1);gamma=Q(1,4);ceiling=1-a/2;margin=ceiling-Q(1,2)
  theta=Q(1,2)+margin/4;eta=Q(1,2)+margin/2;beta=Q(1,2)+3*margin/4
  threshold=max(s.Integer(d)/gamma,1/(beta-eta),2*d/(1-a))
  q=2*(s.floor(threshold/2)+1)
  assert q%2==0 and q*gamma>d and beta-eta-1/q>0 and q>2*d/(1-a)
  power=(1-a)/2-s.Integer(d)/q;assert power>0
  bad=2*(s.floor((s.Integer(d)/gamma)/2)+1)
  bad_power=(1-a)/2-s.Integer(d)/bad
  params.append({'d':d,'a':str(a),'alpha':'1','gamma':'1/4','theta':str(theta),'eta_time':str(eta),'beta_time':str(beta),'fixed_even_Q':int(q),'anchor_decay_power_exact':str(power),'wrong_Q_using_only_qgamma':int(bad),'wrong_Q_decay_power_exact':str(bad_power),'wrong_Q_anchor_fails':bool(bad_power<=0),'finite_delta_power_values':{str(delta):float(delta**power) for delta in [Q(1,16),Q(1,256),Q(1,65536)]}})
out={'scope':'18truncated sums for the ACTUAL auxiliary torus diagonal factor,3exact finite rational multiplicity calibrations,9exact admissible scalar parameter/decay checks; no whole-space K singular values or SPDE simulation','lattice_rows':rows,'finite_calibrations':cal,'parameter_rows':params,'limitations':['Dyadic remainder formula is analytic; its floating evaluation is not computer-certified enclosure.','Diagonal is only the accepted factorization middle operator, not Kout/Kin or a periodic state replacement.','No unknown Schur factor is inferred bounded from these lattice numbers; full analytic dilation audit remains mandatory.','Constants may grow with Q and a near1; finite-delta powers near1 do not promise useful numerical asymptotics.','No stochastic driver expectation measured.'],'versions':{'numpy':np.__version__,'sympy':s.__version__}}
Path(__file__).with_name('radius-factor-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'lattice_rows':len(rows),'exact_multiplicity_calibrations':len(cal),'exact_parameter_cases':len(params),'bad_q_anchor_failures':sum(x['wrong_Q_anchor_fails'] for x in params),'normalized_trace_ranges':{str(d):[min(x['normalized_trace_lower'] for x in rows if x['d']==d),max(x['normalized_trace_upper'] for x in rows if x['d']==d)] for d in [1,2,3]},'scope':out['scope']},indent=2))
