"""Small-order physical/candidate transforms;finite numerical tests,not proof."""
from pathlib import Path
from fractions import Fraction as Q
from scipy.integrate import quad
import math,json
rows=[]
for a in [0.25,0.5,0.75]:
 for theta in [0.5,1.0,2.0]:
  # Actual white min(s,t)/2 integral,split into its two ordered cones.
  t_int=quad(lambda t:t*math.exp(-2*theta*t),0,math.inf,epsabs=1e-11)[0]
  v_int=quad(lambda v:v**(-a)*math.exp(-theta*v),0,math.inf,epsabs=1e-10)[0]
  actual=t_int*v_int
  actual_closed=math.gamma(1-a)*theta**(a-3)/4
  shared=quad(lambda lam:lam**(a-1)/((theta+lam)*(theta+lam/2)),0,math.inf,epsabs=1e-10)[0]/(4*theta*math.gamma(a))
  predicted=(2-2**a)*actual_closed
  # Independent-clock value after averaging r=u-v;stable rationalization.
  def independent_integrand(lam):
   R=math.sqrt(theta*theta+lam*lam)
   return 2*theta*lam**(a-1)/((theta+lam+R)*R*(theta+lam))
  independent=quad(independent_integrand,0,math.inf,epsabs=1e-10)[0]/(4*theta*math.gamma(a))
  assert abs(actual/actual_closed-1)<2e-8
  assert abs(shared/predicted-1)<2e-8
  assert 0<independent<=shared<actual
  rows.append({'a':a,'theta':theta,'actual':actual,'actual_closed':actual_closed,'shared_clock':shared,'shared_ratio':shared/actual,'expected_shared_ratio':2-2**a,'independent_clock':independent})
variance_checks=0
for u in [Q(1,4),Q(1),Q(2)]:
 for v in [Q(1,2),Q(1),Q(3)]:
  for rho in [Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]:
   assert u+v-2*rho*min(u,v)>=abs(u-v)
   variance_checks+=1
# Unequal gap/horizon damping controls and static endpoint are independent.
unequal=[]
for theta1,theta2 in [(0.5,1.0),(1.0,2.0),(2.0,0.5)]:
 a=0.5
 s=quad(lambda t:t*math.exp(-(theta1+theta2)*t),0,math.inf)[0]
 left=s*(quad(lambda v:v**(-a)*math.exp(-theta1*v),0,math.inf)[0]+quad(lambda v:v**(-a)*math.exp(-theta2*v),0,math.inf)[0])/2
 right=math.gamma(1-a)*(theta1**(a-1)+theta2**(a-1))/(2*(theta1+theta2)**2)
 assert abs(left/right-1)<2e-8
 unequal.append({'theta1':theta1,'theta2':theta2,'ratio':left/right})
result={'status':'PASS finite calibration only','common_damping_cases':rows,'exact_variance_order_cases':variance_checks,'unequal_damping_cases':unequal,'scope':'Tests exact fixed-order white cross integrals vs a named unweighted Brownian clock ansatz. Not a proof of all-rho bound,full model conjecture no-go,high-order asymptotics or sharp constant.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'common_cases':len(rows),'variance_checks':variance_checks,'unequal_cases':len(unequal),'half_exponent_unit_case':rows[4]},indent=2))
