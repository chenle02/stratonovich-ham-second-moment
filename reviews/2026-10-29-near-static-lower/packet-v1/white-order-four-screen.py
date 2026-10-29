"""White-space one-chain order4 mean calibration; not an SPDE proof."""
from pathlib import Path
import json,math
from fractions import Fraction as Q
from scipy.integrate import quad

def coefficient(a):
 # r2+r3+r4=u; p3=z,p2=x,p4=1-z-x. Integrate r1 and u exactly.
 radial=1/(4*(4-2*a)*(5-2*a)*(6-2*a))
 adjacent=math.gamma(1-a)**2/(4*math.gamma(7-2*a))
 nested=radial/(2*(1-a)*(2-a)*(3-a))
 def f(z):
  half=(1-z)/2
  def kernel(x):return (x+z)**(-a)*(1-x)**(-a)
  if z<1/3:
   left=quad(lambda x:x*kernel(x),0,z,epsabs=1e-11,epsrel=1e-10)[0]
   right=quad(lambda x:z*kernel(x),z,half,epsabs=1e-11,epsrel=1e-10)[0]
   return 2*(left+right)
  return 2*quad(lambda x:x*kernel(x),0,half,epsabs=1e-11,epsrel=1e-10)[0]
 c1,e1=quad(f,0,1/3,epsabs=1e-10,epsrel=1e-10)
 c2,e2=quad(f,1/3,1,epsabs=1e-10,epsrel=1e-10)
 crossing=radial*(c1+c2)
 return {'a':a,'adjacent':adjacent,'nested':nested,'crossing':crossing,'total':adjacent+nested+crossing,'cross_angular_error_estimate':e1+e2}
rows=[coefficient(a) for a in [0,1/8,1/4,3/8,1/2,9/16,3/4]]
z=rows[0]
for key,expected in [('adjacent',Q(1,2880)),('nested',Q(1,5760)),('crossing',Q(1,8640)),('total',Q(11,17280))]:
 assert abs(z[key]-float(expected))<1e-12,(key,z[key],expected)
lookup={r['a']:r['total'] for r in rows};tests=[]
for a,b,theta in [(1/8,1/4,1/2),(1/4,1/2,1/2),(3/8,3/4,1/2),(9/16,3/4,3/4)]:
 left=lookup[a];right=lookup[0]**(1-theta)*lookup[b]**theta
 assert left<=right+1e-10,(a,b,left,right)
 tests.append({'a':a,'b':b,'theta':theta,'left':left,'right':right,'ratio':left/right})
result={'status':'PASS finite numerical calibration only','white_one_chain_total_order_four':rows,'static_exact_checks':'1/2880+1/5760+1/8640=11/17280','raw_time_Holder_cases':tests,'does_not_prove':'General covariance comparison,Gaussian joint limits,all-order Holder,entire-series type,strict mean/second-moment separation or novelty'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'static_total':z['total'],'Holder_ratios':[x['ratio'] for x in tests]},indent=2))
