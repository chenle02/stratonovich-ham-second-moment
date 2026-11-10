#!/usr/bin/env python3
"""Fixed original d3 CM spatial profile; broad trial/mask consistency only."""
from pathlib import Path
import json
import mpmath as mp

def run(dps):
 mp.mp.dps=dps
 def h2(x):return mp.exp(-2/(1-x*x)) if abs(x)<1 else mp.mpf(0)
 parts=[0,mp.mpf('.5'),mp.mpf('.8'),mp.mpf('.95'),1]
 N=2*mp.quad(h2,parts)
 K=2*mp.quad(lambda x:4*x*x/(1-x*x)**4*h2(x) if x<1 else 0,parts)
 Q=2*mp.quad(lambda x:h2(x)**2,parts)/(N*N)
 D=3*K/N;b=mp.mpf('.1');rows=[]
 for L in [1,4,16,64,256,1024]:
  potential=2*mp.quad(lambda x:h2(x)*h2(x/L),parts)/(L*N*N)
  kinetic=D/(L*L);energy=kinetic-b*potential
  assert potential>0
  rows.append({'trial_scale':L,'mask_R':2*L,'fixed_original_Q':mp.nstr(Q,28),'potential_trial':mp.nstr(potential,28),'kinetic_trial':mp.nstr(kinetic,28),'energy_at_FIXED_b_point1':mp.nstr(energy,28)})
 assert mp.mpf(rows[0]['energy_at_FIXED_b_point1'])>0
 assert mp.mpf(rows[-1]['energy_at_FIXED_b_point1'])<0
 return {'working_digits':dps,'rows':rows}
a=run(35);b=run(60)
for u,v in zip(a['rows'],b['rows']):
 for k in ['fixed_original_Q','potential_trial','kinetic_trial','energy_at_FIXED_b_point1']:
  assert abs(mp.mpf(u[k])-mp.mpf(v[k]))<mp.mpf('1e-25')
out={'scope':'Floating consistency, not certified quadrature/error/eigenvalue or continuum theorem. q and its original raw spatial covariance cost remain FIXED at all trial scales.',
 'model':'Original admissible d3 Gamma=delta_x1 tensorLeb_x2 tensorLeb_x3,alpha1,a=.5.',
 'fixed_profile':'q=g0², g0=product normalized h(xj), h=exp(-1/(1-x²)) on(-1,1). q does NOT change with L.',
 'broad_trial':'psi_L=L^(-3/2)g0(x/L); U_L=m_(2L)*(Gamma*q), with m=1 on both support psi_L and support g0. Gamma*q=phi(x1)².',
 'exact_integral_definition':'Dtrial=D0/L²; Vtrial=(1/L)int phi(x)² phi(x/L)² dx. int U_L*g0²=Q0 is unchanged, while b=.1 is FIXED. Only mask/trial widen.',
 'point':'Wide tests can make energy negative for this family of enlarged masks without changing q/cost. This is NOT all-strength binding of a single fixed compact potential.',
 'runs':[a,b],'agreement':'35/60 working-digit printed values agree within1e-25; not a certified error estimate.'}
Path(__file__).with_name('fixed-profile-trial-v0.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS fixed ORIGINAL q/cost and b=.1 at six broad-trial/mask scales, 35/60-digit consistency; no eigenvalue certificate.')
