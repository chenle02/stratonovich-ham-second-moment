"""Exact finite Gaussian isometry amplitude/adjoint diagnostics only."""
import sympy as s
import json
from pathlib import Path
Q=s.Rational
T=s.Matrix([[1,0,0],[0,Q(3,5),0],[0,Q(4,5),0],[0,0,1],[0,0,0]])
assert T.T*T==s.eye(3)
F=s.Matrix([[1,2,-1],[0,3,2]])
phis=[s.Matrix([1,2,3,4,5]),s.Matrix([0,1,-1,2,-3]),s.Matrix([0,0,0,0,1])]
rows=[]
for delta,a in [(Q(1,16),Q(1,2)),(Q(1,256),Q(1,4)),(Q(1,64),Q(2,3))]:
 q=delta**(a/2);g=delta**((1-a)/2)
 assert g*q==s.sqrt(delta)
 for j,Phi in enumerate(phis):
  fast=T.T*Phi
  orth=Phi-T*fast
  assert T.T*orth==s.zeros(3,1)
  assert (fast.T*fast)[0]<=(Phi.T*Phi)[0]
  covariance=F*fast
  H=covariance/q
  direction=fast/q
  assert F*direction==H
  assert g*covariance==s.sqrt(delta)*H
  wrong_uncorrected=covariance-H
  wrong_scaled_factor=covariance-s.sqrt(delta)*H
  signal=bool(H!=s.zeros(2,1))
  if signal:
   assert wrong_uncorrected!=s.zeros(2,1)
   assert wrong_scaled_factor!=s.zeros(2,1)
  rows.append({'delta':str(delta),'a':str(a),'slow_control_case':j,'raw_isometry_exact':True,'orthogonal_residual_exact':True,'fast_adjoint_contraction_exact':True,'mean_direction_identity_exact':True,'scaled_covariance_identity_exact':True,'nonzero_signal':signal,'wrong_missing_direction_factor_detected':signal,'wrong_unscaled_sqrt_delta_detected':signal})
out={'scope':'finite rational Gaussian-coordinate isometry algebra only, not actual fractional raw covariance or PDE/SPDE evidence','rows':rows,'sympy_version':s.__version__}
Path(__file__).with_name('block-direction-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('9 exact covariance/isometry/normalization cases;6nonzero false-factor guards and3zero-signal calibrations passed')
