"""Exact exponent/normalization controls only, no covariance/spectral proof."""
from fractions import Fraction as Q
import json
rows=[]
I,v=Q(2,3),Q(3,5)
for alpha in [Q(1),Q(1,2),Q(1,4)]:
 p,d=alpha.numerator,alpha.denominator
 for u in [Q(2),Q(1,2)]:
  s=u**(2*d)
  amplitude=u**(2*(3*d-p))
  measure_push=u**(2*(p-d))
  assert amplitude*measure_push==s*s
  eigen_amp=u**d
  assert eigen_amp*eigen_amp/s==1
  assert 1/s!=1  # wrong unnormalized eigenfunction is detected
  variance=amplitude*s
  expected_variance=u**(2*(4*d-p))
  assert variance==expected_variance
  c=amplitude
  assert c*s==variance
  assert c*(s*I)-variance*v/2==variance*(I-v/2)
  assert c*(s*I)-(s**2)*v/2!=variance*(I-v/2)
  exponent=(4-alpha)/(3-alpha)
  assert exponent-1==1/(3-alpha) and exponent>1
  rows.append({'alpha':str(alpha),'s':str(s),'q_amplitude':str(amplitude),
    'measure_push':str(measure_push),'variance_scale':str(variance),
    'eigen_L2_normalized':True,'score_relation':True})
print(json.dumps({'status':'PASS','scope':'6finite exact exponent/normalization controls; not class/operator/variance/supremum proof','cases':rows},indent=2))
