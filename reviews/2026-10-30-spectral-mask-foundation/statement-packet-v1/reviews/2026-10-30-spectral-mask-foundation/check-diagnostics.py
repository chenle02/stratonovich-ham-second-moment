#!/usr/bin/env python3
"""Actual covariance/normalization controls, not a spectral/operator proof."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=60
singular=[]
C=m.e/(2*m.sqrt(m.pi))
for rr in ['0.25','1','3']:
 r=m.mpf(rr)
 for yy in ['0','0.5','2']:
  y=m.mpf(yy)
  mass=m.sqrt(max(m.mpf(0),r*r-y*y))/m.pi
  spectral_gauss=r/(2*m.sqrt(m.pi))*m.exp(-y*y/(r*r))
  # Gamma=delta_x1 tensorLeb_x2, original spectral mu=(2pi)^-1Leb_xi1 tensordelta0.
  physical_gauss=(r/(2*m.sqrt(m.pi)))**2*(2*m.sqrt(m.pi)/r)*m.exp(-y*y/(r*r))
  assert m.almosteq(spectral_gauss,physical_gauss,rel_eps=m.mpf('1e-50'))
  assert mass<=m.e*spectral_gauss<=C*r
  singular.append({'r':rr,'transverse_center':yy,'ball_mass':m.nstr(mass,40),'spectral_gaussian':m.nstr(spectral_gauss,40),'physical_dual_gaussian':m.nstr(physical_gauss,40),'uniform_bound':m.nstr(C*r,40)})
riesz=[]
for d,aa in [(1,'0.5'),(2,'1'),(3,'1.5')]:
 a=m.mpf(aa);sphere=2*m.pi**(m.mpf(d)/2)/m.gamma(m.mpf(d)/2)
 M=sphere*2**(d-a-1)*m.gamma((d-a)/2)
 coeff=2**(-a)*m.pi**(-m.mpf(d)/2)*m.gamma((d-a)/2)/m.gamma(a/2)
 for rr in ['0.5','1','2']:
  r=m.mpf(rr)
  spec=coeff*sphere/2*m.gamma(a/2)*r**a
  dual=r**a*M/(2*m.sqrt(m.pi))**d
  mass=coeff*sphere*r**a/a
  assert m.almosteq(spec,dual,rel_eps=m.mpf('1e-50')) and mass<=m.e*dual
  riesz.append({'d':d,'alpha':aa,'r':rr,'centered_gaussian_spectral':m.nstr(spec,40),'physical_dual':m.nstr(dual,40),'centered_ball_mass':m.nstr(mass,40)})
gaussian_masks=[]
for rr in ['1','2','4','8']:
 R=m.mpf(rr);A=(1+R**-2)/2;b=1+R*R/2
 physical=m.pi**m.mpf('1.5')*R**-4/(4*m.sqrt(2)*A**m.mpf('3.5'))
 # Unitary masked Fourier value on xi2=0: -R^-2/(4A^2) exp(-xi1^2/(4A)).
 spectral=(2*m.pi)**2/(2*m.pi)*R**-4/(16*A**4)*m.sqrt(2*m.pi*A)
 # Auxdensity R/(2pi)^(3/2) exp(-R^2 eta2^2/2), testhat=-eta2^2 exp(-|eta|^2/2).
 aux=(2*m.pi)**2*R/(2*m.pi)**m.mpf('1.5')*m.sqrt(m.pi)*3*m.sqrt(m.pi)/(4*b**m.mpf('2.5'))
 assert m.almosteq(physical,spectral,rel_eps=m.mpf('1e-50')) and physical<=aux
 gaussian_masks.append({'R':rr,'original_spatial_variance':'0 (exact second-derivative marginal)','actual_masked_variance_physical':m.nstr(physical,40),'same_variance_spectral':m.nstr(spectral,40),'auxiliary_spectral_variance':m.nstr(aux,40),'aux_over_actual':m.nstr(aux/physical,30)})
# A genuine C_infinity compact plateau for the physical compact-mask counterexample.
def chi(x):
 r=abs(x)
 if r<=1:return m.mpf(1)
 if r>=2:return m.mpf(0)
 A=m.exp(-1/(2-r));B=m.exp(-1/(r-1));return A/(A+B)
def derivs(r):
 c=chi(r);D=(2-r)**-2+(r-1)**-2;Dprime=2*(2-r)**-3-2*(r-1)**-3
 return -c*(1-c)*D,c*(1-c)*((1-2*c)*D*D-Dprime)
I=2*m.quad(lambda r:derivs(r)[0]**2,[1,m.mpf('1.5'),2])
J=2+2*m.quad(lambda r:chi(r)**4,[1,m.mpf('1.5'),2])
ibp=2*m.quad(lambda r:chi(r)*derivs(r)[1],[1,m.mpf('1.5'),2])
assert I>0 and J>0 and m.almosteq(ibp,-I,rel_eps=m.mpf('1e-45'))
out={'scope':'Actual singular/Riesz covariance normalization and linear-variance controls only; Gaussian masks are Schwartz auxiliary examples, separate compact plateau is C_infinity. No operatorpath/moment/Schatten theorem.','precision_decimal_digits':60,'singular_ball_and_gaussian_cases':singular,'riesz_normalization_cases':riesz,'Gaussian_Schwartz_mask_cases':gaussian_masks,'compact_plateau_counterexample':{'original_variance':'0 by exact intchi_second=0','I_int_derivative_squared':m.nstr(I,40),'J_int_chi_fourth':m.nstr(J,40),'IBP_int_chi_chi_second':m.nstr(ibp,40),'actual_masked_spatial_variance_JI2':m.nstr(J*I*I,40)},'all_assertions_passed':True}
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('9singular ball/Gaussian,9Riesz normalization,4Schwartz mask andcompactplateau IBP controls PASS.')
