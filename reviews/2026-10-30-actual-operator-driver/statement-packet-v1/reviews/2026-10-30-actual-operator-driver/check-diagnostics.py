#!/usr/bin/env python3
"""Actual CM time convolution/mask-order and finite compact-tail controls only."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=40
def bump(u):
 v=u-1
 if v<=0 or v>=1:return m.mpf(0)
 return m.exp(-1/(v*(1-v)))
def bump_prime(u):
 v=u-1
 if v<=0 or v>=1:return m.mpf(0)
 return bump(u)*(1-2*v)/(v*v*(1-v)**2)
def conv(t,a,f):
 if t<1 or t>2:return m.quad(lambda u:abs(t-u)**(-a)*f(u),[1,m.mpf('1.5'),2])
 b=1/(1-a);v=m.mpf(0)
 if t>1:
  ell=t-1;v+=ell**(1-a)*b*m.quad(lambda z:f(t-ell*z**b),[0,m.mpf('0.5'),1])
 if t<2:
  ell=2-t;v+=ell**(1-a)*b*m.quad(lambda z:f(t+ell*z**b),[0,m.mpf('0.5'),1])
 return v
rows=[];eps=m.mpf('0.00001')
for aa in ['0.1','0.5','0.9']:
 a=m.mpf(aa)
 for tt in ['0','0.5','1','1.25','1.5','2','2.5']:
  t=m.mpf(tt);value=conv(t,a,bump);deriv=conv(t,a,bump_prime)
  fd=(conv(t+eps,a,bump)-conv(t-eps,a,bump))/(2*eps)
  assert value>0 and abs(fd-deriv)<m.mpf('1e-5')
  rows.append({'a':aa,'t':tt,'CM_time_mean':m.nstr(value,25),'derivative_moved_to_test':m.nstr(deriv,25),'symmetric_difference':m.nstr(fd,25),'absolute_difference':m.nstr(abs(fd-deriv),20)})
def chi(x):
 r=abs(x)
 if r<=1:return m.mpf(1)
 if r>=2:return m.mpf(0)
 A=m.exp(-1/(2-r));B=m.exp(-1/(r-1));return A/(A+B)
Q=2+2*m.quad(chi,[1,m.mpf('1.5'),2]);I2=2+2*m.quad(lambda x:chi(x)**2,[1,m.mpf('1.5'),2])
assert Q>I2>0
# Actual Gamma=delta_x1 tensorLeb_x2, q=chi(x1)chi(x2), R1 radialzeta=chi(|x|).
# Correct mask AFTER covariance convolution vs incorrect inside convolution.
mask=[]
for yy in ['0','1.5','3']:
 y=m.mpf(yy);correct=chi(abs(y))*Q;wrong=I2
 mask.append({'x':['0',yy],'correct_zeta_times_Gamma_q_spatial_factor':m.nstr(correct,25),'incorrect_Gamma_zetaq_factor':m.nstr(wrong,25)})
assert m.mpf(mask[-1]['correct_zeta_times_Gamma_q_spatial_factor'])==0 and I2>0
# Finite positive covariance tail example; diagonal B_j=j^-2 is compact trace class.
# These are matrix calibrations only, not the actual noise driver.
tail=[]
for N in [0,4,16,64]:
 b=[m.mpf(j)**-2 for j in range(1,257)]
 op=max(b[N:]) if N<256 else 0;tr=sum(x*x for x in b[N:])
 tail.append({'finite_dimension':256,'cutoff_N':N,'tail_operator_norm':m.nstr(op,22),'tail_S2_power':m.nstr(tr,22)})
assert all(m.mpf(tail[i+1]['tail_operator_norm'])<m.mpf(tail[i]['tail_operator_norm']) for i in range(3))
assert all(m.mpf(tail[i+1]['tail_S2_power'])<m.mpf(tail[i]['tail_S2_power']) for i in range(3))
out={'working_precision':40,'scope':'21 actual smoothcompact time-test CM convolutions/derivative controls; actual d2 singular covariance mask-order control;4 finite diagonal compact-tail calibrations. No original operator/path/Gaussian-series proof and no certified quadrature accuracy.','time_test':'exp(-1/((u-1)(2-u))) on(1,2),zerootherwise, actual C_c^infinity(0,infinity)','CM_time_controls':rows,'actual_singular_d2_mask_order':mask,'spatial_test_variance_factor':m.nstr(I2*Q*Q,25),'finite_compact_tail':tail,'analytic_boundary_controls':['A null raw test can occur for invariant-directionGamma; no injectivity assumed.','A nonzero source test at x1 shifted5 has zero masked CMmean for R1 in the delta_x1 tensorLeb_x2 model.','Without a COMPACT positive envelope, rankone projections onto disjoint translated compact smooth states converge weakly to0 but retain operator/Schattennorm1.','Independent Gaussian diagonal sums over those translated states have uniform bounded variance byI but unbounded limiting sampleoperator norm; this is outside compact-localization hypotheses, not a claim about the actual masked model.']}
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('21 actual CMtime/derivative,actual singular mask-order and finite compact-tail controls PASS.')
