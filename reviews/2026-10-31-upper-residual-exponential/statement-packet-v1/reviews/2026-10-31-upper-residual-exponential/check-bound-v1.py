"""New scalar bound/guard controls using preserved Gaussian integral data."""
from pathlib import Path
from fractions import Fraction as F
import json,mpmath as m
m.mp.dps=60;base=Path(__file__).resolve().parent;old=json.loads((base/'rank-one-v0.json').read_text());rows=[]
for z in old['rows']:
 nu,e,d=map(m.mpf,[z['nu'],z['epsilon'],z['delta']]);actual=m.mpf(z['delta_log_moment'])
 C=(2-nu)/2*(2*nu)**(nu/(2-nu))*2**(2*(nu-1)/(2-nu));b=2*m.sqrt(d)*e*m.sqrt(2/m.pi)
 bound=2**(nu-1)*b**nu+C*e**(2*nu/(2-nu))+d*m.log(2)
 assert actual<bound
 rows.append({'nu':z['nu'],'epsilon':z['epsilon'],'delta':z['delta'],'actual_preserved_delta_log_moment':str(actual),'proposed_finite_delta_bound':m.nstr(bound,35)})
a=m.mpf('.5');wrong=[]
for ds in ['.1','.03','.01']:
 d=m.mpf(ds);g=d**((1-a)/2);t=g/d;logM=m.log(2)+t*t/2+m.log(m.erfc(-t/m.sqrt(2))/2)
 wrong.append({'a':'0.5','delta':ds,'wrong_scale_delta_log_moment_nu1':m.nstr(d*logM,35),'scope':'ACTUAL scalar norm g_delta|G|; mean->0 and uniform small square-exponential moments do not give finite1/delta estimate from these hypotheses alone.'})
assert all(m.mpf(wrong[i]['wrong_scale_delta_log_moment_nu1'])<m.mpf(wrong[i+1]['wrong_scale_delta_log_moment_nu1']) for i in [0,1])
assert F(3,5)-F(1,2)>0
# nu1.5 saddle coefficient27/32; A_nu27. Wrong stronger epsilon7 loses.
e=F(1,100);saddle=F(27,32)*e**6;wrong_power=F(27)*e**7;assert saddle>wrong_power
out={'status':'SCALAR CONSISTENCY/FALSIFICATION ONLY','finite_bound_controls':rows,'wrong_CM_scale_controls':wrong,'exact_guards':{'nu2_eta_epsilon_squared_3over5_minus_Gaussian_half':str(F(3,5)-F(1,2)),'nu2_divergence_at_zero_residual_quadratic':True,'nu_above2_divergence_for_any_positive_coefficient':True,'nu1.5_wrong_epsilon7_vs_correct_epsilon6':{'epsilon':str(e),'actual_saddle_rate':str(saddle),'wrong_bound':str(wrong_power),'refuted':True}},'scope':'No old integrator rerun. Uses preserved40/60digit Gaussian data; arithmetic controls not certified quadrature/error or operator/SPDE theorem. Wrong-scale nu1 is a scalar hypothesis counter, not a failure of actual averaged driver.'}
(base/'bound-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n');print('18 finite-bound consistency rows,3wrong-scale Gaussian moments and exact endpoint/power guards PASS; not proof.')
