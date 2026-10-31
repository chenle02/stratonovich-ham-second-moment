#!/usr/bin/env python3
"""Actual joint source covariance and deterministic-test variance controls."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=45
heat=lambda e,x:m.exp(-x*x/(2*e))/m.sqrt(2*m.pi*e)
def kap(a,eta,t):
 if t==0:return eta**(-a)/(a*m.gamma(a))
 return abs(t)**(-a)*m.gammainc(a,0,abs(t)/eta)/m.gamma(a)
def ou_norm(lam,T):
 z=lam*T
 if abs(z)<m.mpf('1e-8'):
  return 2*sum((-lam)**n*T**(n+2)/(m.factorial(n)*(n+1)*(n+2)) for n in range(8))
 return 2*(T/lam+m.expm1(-z)/(lam*lam))
def time_cut(a,eta,T):
 U=1/eta
 return U**a/(a*m.gamma(a))*m.quad(lambda x:ou_norm(U*x**(1/a),T),[0,m.mpf('.5'),m.mpf('.9'),m.mpf('.99'),1])
# Actual d1 whiteGamma/alpha1 and d2 delta_x1 tensorLeb_x2,alpha1 share covariance
# in the first coordinate; d2 source field is invariant in x2, not spatialwhite2.
points=[(m.mpf(e),m.mpf(d),m.mpf(t),m.mpf(x)) for e,d,t,x in [('.1','.2','0','0'),('.1','.2','.5','.4'),('.3','.05','0','0'),('.3','.05','.5','-.3'),('.02','.1','.25','.1')]]
a=m.mpf('.5')
C=m.matrix([[kap(a,max(di,dj),ti-tj)*heat(ei+ej,xi-xj) for ej,dj,tj,xj in points] for ei,di,ti,xi in points])
assert min(m.eigsy(C,eigvals_only=True))>-m.mpf('1e-35')
eta1,eta2=m.mpf('.2'),m.mpf('.05');eps=m.mpf('.1')
v1=kap(a,eta1,0)*heat(2*eps,0);v2=kap(a,eta2,0)*heat(2*eps,0)
correct=v1*v2-v1*v1;wrong=v1*v2-v2*v2
assert correct>0 and wrong<0
# Wrong spatial cross using twice min epsilon also violates the 2x2 PSD condition.
e1,e2=m.mpf('.1'),m.mpf('.4');k=kap(a,eta1,0)
s1=k*heat(2*e1,0);s2=k*heat(2*e2,0);sc=k*heat(e1+e2,0);sw=k*heat(2*min(e1,e2),0)
assert s1*s2-sc*sc>0 and s1*s2-sw*sw<0
rows=[]
for aa in ['.25','.5','.75']:
 a=m.mpf(aa)
 for TT in ['.5','1']:
  T=m.mpf(TT);rawtime=2*T**(2-a)/((1-a)*(2-a));S0=m.sqrt(m.pi)
  prev=None
  for ee,dd in [('.5','.5'),('.05','.1'),('.005','.01'),('.0005','.001')]:
   e,d=m.mpf(ee),m.mpf(dd);tc=time_cut(a,d,T)
   Se=m.sqrt(m.pi/(1+e));Sc=m.sqrt(m.pi/(1+e/2));Sr=S0-2*Sc+Se
   raw=rawtime*S0;cut=tc*Se;res=(rawtime-tc)*S0+tc*Sr
   direct=raw-2*tc*Sc+cut
   assert 0<cut<=raw and 0<=res<=raw and abs(res-direct)<m.mpf('1e-35')
   if prev is not None:assert res<prev
   prev=res
   rows.append({'a':aa,'T':TT,'epsilon':ee,'delta':dd,'raw_variance':m.nstr(raw,28),'source_variance':m.nstr(cut,28),'residual_variance_orthogonal_slices':m.nstr(res,28),'residual_variance_cross_formula':m.nstr(direct,28),'residual_over_raw':m.nstr(res/raw,22)})
out={'working_precision':45,'scope':'Actual d1white/d2singular alpha1 source-covariance controls;5point jointmatrix and wrong-joint-parameter PSD controls;24 raw-completion indicator-time/Gaussianspace deterministictest variance controls. Not operator/sourcepath/Young/u-moment proof or certifiedaccuracy.','joint_point_model':'d1Gamma=delta0 or d2Gamma=delta_x1 tensorLeb_x2; d2pointcov independentx2','point_parameters':[[str(x) for x in row] for row in points],'joint_PSD_minimum':m.nstr(min(m.eigsy(C,eigvals_only=True)),28),'wrong_temporal_min_instead_of_max':{'correct_determinant':m.nstr(correct,28),'wrong_determinant':m.nstr(wrong,28)},'wrong_spatial_cross_twice_min_instead_of_sum':{'correct_determinant':m.nstr(s1*s2-sc*sc,28),'wrong_determinant':m.nstr(s1*s2-sw*sw,28)},'test_variance_controls':rows,'test_class':'tau=1_[0,T] is in rawcompletion, not literalC_infinitybasis; spatialGaussianSchwartz, d2transversemarginal gives commonpositive factor2pi so variance ratios same','finite_span_coupling_control':{'model':'g1,g2 independentstd,raw=g1+g2,cut=g1','Varraw':2,'Varcut':1,'Covrawcut':1,'forced_linear_coefficient_in_raw_coordinate':'1/2','resulting_wrong_Varcut':'1/2','scope':'one-coordinate illustration only,not proof of nonmeasurability in fullrawspan'}}
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('Actual5point jointcov/2wrong-parameterPSD and24 coupledtest source/residual variance controls PASS.')
