"""Finite Gaussian/Rayleigh diagnostics only; no AWS or wave proof."""
from pathlib import Path
import json
import mpmath as mp

def quad_rayleigh_scaled(a,delta):
 t=a/mp.sqrt(delta)
 pts=sorted(set([mp.mpf(0),max(mp.mpf(0),t-10),t,t+10]))+[mp.inf]
 return mp.quad(lambda u:u*mp.exp(-(u-t)**2/2),pts)
def quad_mgf_scaled(lam,p,delta):
 h=p*lam/mp.sqrt(delta)
 return mp.quad(lambda z:mp.exp(h*z-z*z/2-h*h/2)/mp.sqrt(2*mp.pi),[-mp.inf,h-10,h,h+10,mp.inf])
def closed_rayleigh_scaled(a,delta):
 t=a/mp.sqrt(delta)
 return mp.exp(-t*t/2)+t*mp.sqrt(2*mp.pi)*mp.erfc(-t/mp.sqrt(2))/2
rows=[];tails=[]
for ds in ['0.25','0.0625','0.015625','0.00390625']:
 for ls in ['0','0.5','2']:
  for ps in [-1,0,1]:
   evals=[]
   for prec in [35,70]:
    mp.mp.dps=prec;delta=mp.mpf(ds);lam=mp.mpf(ls);p=mp.mpf(ps)
    a=abs(p*lam);b=2*lam*mp.sqrt(2*delta/mp.pi)
    j=quad_rayleigh_scaled(a,delta);jc=closed_rayleigh_scaled(a,delta)
    m=quad_mgf_scaled(lam,p,delta)
    err=abs(j/jc-1)
    assert err<mp.mpf('1e-24') and abs(m-1)<mp.mpf('1e-24')
    logtrue=a*a/2+delta*mp.log(m)
    logbound=abs(p)*b+a*a/2+delta*mp.log(j)
    assert logbound+mp.mpf('1e-24')>=logtrue
    aw=a*mp.sqrt(delta);jw=quad_rayleigh_scaled(aw,delta)
    wrong=abs(p)*b+aw*aw/2+delta*mp.log(jw)
    evals.append({'precision':prec,'scaled_MGF_integral':mp.nstr(m,28),'scaled_Rayleigh_integral':mp.nstr(j,28),'relative_Rayleigh_closedform_error':mp.nstr(err,8),'delta_log_true_MGF':mp.nstr(logtrue,28),'delta_log_tube_bound':mp.nstr(logbound,28),'delta_log_wrong_CM_bound':mp.nstr(wrong,28)})
   rows.append({'delta':ds,'lambda':ls,'p':ps,'evaluations':evals,'two_precision_log_bound_difference':mp.nstr(abs(mp.mpf(evals[0]['delta_log_tube_bound'])-mp.mpf(evals[1]['delta_log_tube_bound'])),8),'wrong_halfaction_variational_gap':mp.nstr(a*a/4,12),'wrong_CM_bound_below_actual_MGF':bool(a>0 and wrong<logtrue-mp.mpf('1e-20')),'zero_signal':a==0})
  mp.mp.dps=70;delta=mp.mpf(ds);lam=mp.mpf(ls)
  for rs in ['0','0.25','0.75','2']:
   r=mp.mpf(rs)
   if lam==0:actual=mp.mpf(0);borell=mp.mpf(0);wrongactual=mp.mpf(0);mass=mp.mpf(1)
   else:
    c=2*mp.sqrt(2/mp.pi);mass=mp.erf(c/mp.sqrt(2));ahat=mp.sqrt(2)*mp.erfinv(2*mass-1)
    actual=mp.erfc((c+r/mp.sqrt(delta))/mp.sqrt(2))
    borell=mp.erfc((ahat+r/mp.sqrt(delta))/mp.sqrt(2))/2
    wrongactual=mp.erfc((c+r)/mp.sqrt(2))
   radial=mp.exp(-r*r/(2*delta))
   assert actual<=borell+mp.mpf('1e-60') and borell<=radial+mp.mpf('1e-60')
   tails.append({'delta':ds,'lambda':ls,'control_radius':rs,'base_ball_probability':mp.nstr(mass,25),'actual_correct_tube_complement':mp.nstr(actual,25),'Borell_primary_bound':mp.nstr(borell,25),'Rayleigh_bound':mp.nstr(radial,25),'wrong_CM_actual_tube_complement':mp.nstr(wrongactual,25),'wrong_CM_halfaction_tail_refuted':bool(lam>0 and wrongactual>radial+mp.mpf('1e-40'))})
mp.mp.dps=70
cells=[]
for k in [4,5,6,7,8]:
 delta=mp.mpf(1)/(2**k)
 for family,n in [('polynomial_d3',(2**k)**3),('exponential',2**(2**(k-2)))]:
  u=mp.sqrt(2*delta*mp.log(2*n));upper=u+delta/u;b0=mp.mpf(2)/5
  logprob=n*mp.log(mp.erf(b0/mp.sqrt(2*delta)))
  lower=b0*(-mp.expm1(logprob))
  cells.append({'delta':str(delta),'family':family,'exact_integer_cells':str(n),'delta_log_cells':mp.nstr(delta*mp.log(n),20),'mean_max_upper_union_integral':mp.nstr(upper,25),'fixed_threshold':'2/5','log_probability_max_below_threshold':mp.nstr(logprob,25),'mean_max_lower':mp.nstr(lower,25),'twice_mean_lower':mp.nstr(2*lower,25),'twice_mean_upper':mp.nstr(2*upper,25)})
out={'scope':'36finite scalar Gaussian MGF/Rayleigh cases at35/70digits,48exact-law scalar tail evaluations,10finite Gaussian-cell formulas; floating diagnostics not certified enclosure/AWS/wave theorem','moment_rows':rows,'tube_tail_rows':tails,'cell_rows':cells,'limitations':['No Monte Carlo or clipping; direct quadrature versus closed forms remains floating arithmetic.','Finite Gaussian models only, not original wave operator/CM realization.','Gaussian cell expectation values are explicit analytic lower/upper formulas evaluated numerically, not exact expectations.','Polynomial/exponential asymptotic distinction still needs the stated analytic limit arguments.'],'mpmath_version':mp.__version__}
Path(__file__).with_name('gaussian-tube-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'moment_rows':len(rows),'tail_rows':len(tails),'cell_rows':len(cells),'wrong_CM_moment_failures':sum(x['wrong_CM_bound_below_actual_MGF'] for x in rows),'wrong_CM_tail_failures':sum(x['wrong_CM_halfaction_tail_refuted'] for x in tails),'max_two_precision_log_change':max(float(x['two_precision_log_bound_difference']) for x in rows),'scope':out['scope']},indent=2))
