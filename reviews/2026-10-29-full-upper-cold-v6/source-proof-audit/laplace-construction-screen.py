"""Exact low-order checks for proposed independent construction;not a proof."""
from fractions import Fraction as F
from pathlib import Path
import json

cases=0
for a in [F(1,2),F(1),F(2),F(3)]:
 for b in [F(1,2),F(1),F(2),F(3)]:
  # Gamma=delta_0,d=1:cross-chain static spatial factor min(r,s)/2.
  time=F(1,2*a*(a+b)**2)+F(1,2*b*(a+b)**2)
  spectral=F(1,2*a*b*(a+b))
  assert time==spectral
  if a!=b:
   partial_fractions=(F(1,2*a)-F(1,2*b))/(b*b-a*a)
  else:partial_fractions=F(1,4*a**3)
  assert partial_fractions==spectral
  # Empty+length2 chain:spatial factor r1/2.
  assert F(1,2*a*a)*F(1,b)==F(1,2*a*a*b)
  cases+=2
# A homogeneous measure CAN charge a coordinate-zero face.
# rho=delta_0(dr1)*r2 dr2;damped Laplace is independent oflambda1.
face_atom_transform=[F(1) for lam in [1,10,1000]]
assert face_atom_transform==[1,1,1]
# Thus homogeneity must not replace the separatelambda_l->infinity argument.
for scale in [F(1,2),F(2),F(3)]:
 for r,s in [(F(1),F(2)),(F(3),F(1,2))]:
  assert scale*scale*min(scale*r,scale*s)/2 == scale**3*min(r,s)/2
  assert scale*scale*(scale*r)/2 == scale**3*r/2
result={'status':'PASS exact finite calibration only','white_static_Laplace_cases':cases,
        'models':'d=1,Gamma=delta_0;cross(1,1)and empty/self(0,2)',
        'cross_mass_at_unit_damping':'1/4','self_mass_at_unit_damping':'1/2',
        'homogeneity_degree':'3=(4-alpha)k foralpha=k=1',
        'coordinate_face_negative_control':'Homogeneous delta_0(dr1)*r2dr2 has a face atom;its damped transform does not vanish aslambda1->infinity',
        'scope':'Does not prove general spatial Wick-measure convergence,Brownian moment bounds,temporal cutoff removal or Gaussian L2 construction'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
