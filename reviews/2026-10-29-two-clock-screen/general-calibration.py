"""Finite radial probes of exact resolvent and clock-filter formulas;not proof."""
from pathlib import Path
from scipy.integrate import quad
import math,json,warnings
from scipy.integrate import IntegrationWarning
warnings.simplefilter("error",IntegrationWarning)
rows=[];spectral=[]
for alpha in [0.5,1.0,1.5,1.75]:
 a=0.125
 for theta in [0.5,1.0,2.0]:
  def diff(lam):
   return theta**(alpha-2)*(-math.expm1((alpha-2)*math.log1p(lam/theta)))
  def w(lam):return lam**(a-2)*diff(lam)/(2*theta*math.gamma(a))
  def smooth(t):
   lam=t**8
   quotient=diff(lam)/lam if lam else (2-alpha)*theta**(alpha-3)
   return 8*t**(8*a-1)*quotient/(2*theta*math.gamma(a))
  K=quad(smooth,0,math.inf,epsabs=1e-10,epsrel=1e-9)[0]
  K_closed=theta**(alpha+a-4)*math.gamma(3-alpha-a)/(2*(1-a)*math.gamma(2-alpha))
  J=quad(lambda t:2*theta*smooth(t)/(2*theta+t**8),0,math.inf,epsabs=1e-10,epsrel=1e-9)[0]
  assert abs(K/K_closed-1)<2e-7
  assert 0<J<K
  if alpha==1:assert abs(J/K-(2-2**a))<2e-7
  rows.append({'alpha':alpha,'a':a,'theta':theta,'actual':K,'actual_closed':K_closed,'shared_candidate':J,'ratio':J/K})
 for lam in [0.1,1.0,3.0]:
  theta=1.0
  c=2*math.sin(math.pi*alpha/2)/math.pi # calibrates R_Gamma(1)=1
  def f(r):
   return c*r**(alpha-1)*(2*theta+lam)/(2*theta*(theta*theta+r*r)*((theta+lam)**2+r*r))
  I=quad(lambda t:2*t*f(t*t),0,math.inf,epsabs=1e-10,epsrel=1e-9)[0]
  expected=(1-(1+lam)**(alpha-2))/(2*theta*lam)
  assert abs(I/expected-1)<2e-7
  spectral.append({'alpha':alpha,'lambda':lam,'ratio':I/expected})
result={'status':'PASS finite radial calibration only','actual_and_filtered_cases':rows,'spectral_resolvent_cases':spectral,'scope':'Radial densities used ONLY to probe formulas. General proof must and does use arbitrary homogeneous Radon spectral measures,no density/isotropy. Not a general proof,all-order clock lower bound or model counterexample.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'actual_cases':len(rows),'spectral_cases':len(spectral),'shared_ratio_range':[min(x['ratio'] for x in rows),max(x['ratio'] for x in rows)]},indent=2))
