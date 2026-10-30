#!/usr/bin/env python3
"""Finite temporal covariance calibrations; no all-frequency/operator theorem."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=40
rows=[]
for aa in ['0.1','0.5','0.9']:
 a=m.mpf(aa);b=1/(1-a)
 for hh in ['1','0.125']:
  h=m.mpf(hh)
  for ww in ['0','1','16','64']:
   w=m.mpf(ww)
   for shape,Ss in [('constant','0'),('linear','0'),('linear','2'),('quadratic','0'),('quadratic','2')]:
    S=m.mpf(Ss)
    def autocorr(v):
     ell=h-v
     if shape=='constant':return ell
     if shape=='linear':return (S*S+S*v)*ell+(2*S+v)*ell**2/2+ell**3/3
     return ((S+ell)**5-S**5)/5+v*((S+ell)**4-S**4)/2+v*v*((S+ell)**3-S**3)/3
    # v=h z^(1/(1-a)) removes the integrable v^-a singularity exactly.
    val=2*h**(1-a)*b*m.quad(lambda z:autocorr(h*z**b)*m.cos(w*h*z**b),[0,m.mpf('0.25'),m.mpf('0.5'),m.mpf('0.75'),1])
    M=m.mpf(1) if shape=='constant' else (S+h if shape=='linear' else (S+h)**2)
    D=m.mpf(0) if shape=='constant' else (m.mpf(1) if shape=='linear' else 2*(S+h))
    denom=h**(2-a)*(M+h*D)**2*(1+(h*w)**2)**((a-1)/2)
    assert val>0 and m.isfinite(val)
    if shape=='constant' and w==0:assert m.almosteq(val,2*h**(2-a)/((1-a)*(2-a)),rel_eps=m.mpf('1e-35'))
    rows.append({'a':aa,'h':hh,'omega':ww,'amplitude':shape,'interval_start':Ss,'variance':m.nstr(val,25),'candidate_scale_without_Ca':m.nstr(denom,25),'ratio':m.nstr(val/denom,25)})
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps({'working_precision':40,'status':'finite calibration only, not certified quadrature accuracy','scope':'120 constant/linear/quadratic amplitude temporal covariance rows, three a, two h, four omega; exact constant-amplitude zero-frequency identity asserted. No operator/path/moment theorem.','rows':rows},indent=2)+'\n')
print('120 temporal covariance calibrations computed; no uniform estimate proved.')
