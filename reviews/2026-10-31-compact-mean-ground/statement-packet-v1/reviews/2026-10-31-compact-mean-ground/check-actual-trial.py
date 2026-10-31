#!/usr/bin/env python3
"""Actual original d3 singular covariance Rayleigh-trial consistency, not certification."""
import mpmath as mp
from pathlib import Path
import json

def evaluate(dps):
 mp.mp.dps=dps
 def h2(x):return mp.exp(-2/(1-x*x)) if abs(x)<1 else mp.mpf(0)
 def grad2(x):return 4*x*x/(1-x*x)**4*h2(x) if abs(x)<1 else mp.mpf(0)
 def fourth(x):return mp.exp(-4/(1-x*x)) if abs(x)<1 else mp.mpf(0)
 parts=[0,mp.mpf('.5'),mp.mpf('.8'),mp.mpf('.95'),1]
 N=2*mp.quad(h2,parts);K=2*mp.quad(grad2,parts);L=2*mp.quad(fourth,parts)
 D=3*K/N;Q=L/(N*N);b0=2*D/Q
 assert min(N,K,L,D,Q,b0)>0
 rows=[]
 for scale in [1,2,4]:
  Ds=D/scale**2;Qs=Q/scale;bs=2*Ds/Qs
  energy=Ds-bs*Qs
  assert abs(energy+Ds)<mp.mpf(10)**(-dps+5)
  rows.append({'spatial_scale':scale,'D':mp.nstr(Ds,28),'Q':mp.nstr(Qs,28),'b0':mp.nstr(bs,28),'trial_energy_at_b0':mp.nstr(energy,28)})
 return {'dps':dps,'normalizer':mp.nstr(N,30),'D':mp.nstr(D,30),'Q':mp.nstr(Q,30),'b0':mp.nstr(b0,30),'scaled_rows':rows}
low=evaluate(35);high=evaluate(60)
mp.mp.dps=60
for k in ['normalizer','D','Q','b0']:
 assert abs(mp.mpf(low[k])-mp.mpf(high[k]))<mp.mpf('1e-27')
out={'scope':'Floating consistency checks of explicit integral definitions and exact Rayleigh scaling identity, no rigorous quadrature enclosure/eigenvalue calculation/source theorem/certified accuracy.',
     'actual_model':'d=3, Gamma=delta_x1 tensor Leb_x2 tensor Leb_x3, alpha=1, a=.5 (alpha+a<2).',
     'test':'h(x)=exp(-1/(1-x²)) on |x|<1, else0; phi=h/sqrt(int h²); g(x)=product_j phi(x_j), ||g||2=1.',
     'mask':'Choose actual even [0,1] zeta_R with R=2, so m=1 on supp g and compact. For scale L use R=2L.',
     'actual_mean':'Gamma*g²=phi(x1)², independent of x2,x3; U=m(Gamma*g²) is compact. int U g²=int phi^4=Q; D=3int|phi-prime|².',
     'algebraic_identity':'b0=2D/Q gives D-b0Q=-D; for all b>=b0 the trial is negative. At scale L, D_L=D/L²,Q_L=Q/L,b0_L=b0/L. Positivity/normalization and scaling are analytic obligations; quadrature numbers alone are not proof.',
     'weak_potential_warning':'This changes the test profile and its potential with L. It does not assert every fixed compact attractive d3 potential binds at every strength.',
     'runs':[low,high],'precision_agreement':'Printed values agree within1e-27; this is working-precision consistency, not a certified error bound.'}
Path(__file__).with_name('actual-trial-v0.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual d3 singular-profile trial at three scales, 35/60-digit agreement; not an eigenvalue or accuracy certificate.')
