"""Exact algebra controls; actual integral witness is proved separately."""
from fractions import Fraction as Q
import json
rows=[]
for A,B,amp in [(Q(2),Q(1),Q(1)),(Q(5,3),Q(1,4),Q(7,2)),(Q(4,5),Q(1,5),Q(1,3))]:
 det=amp*amp*(A*A-B*B)
 assert A>B>0 and det>0
 assert A/B!=B/A
 rows.append({'A':str(A),'B':str(B),'covariance_amplitude':str(amp),'endpoint_determinant':str(det),'not_proportional':True})
# A=B gives a deliberately non-detecting rank-one case.
assert Q(1)*Q(1)-Q(1)*Q(1)==0
print(json.dumps({'status':'PASS','scope':'3finite endpoint determinant controls and1non-detecting case; not a uniform spectral/wave theorem','rows':rows},indent=2))
