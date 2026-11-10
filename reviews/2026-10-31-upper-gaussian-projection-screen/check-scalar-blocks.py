"""Scalar raw-time covariance calibration only; no SPDE/operator upper bound."""
from pathlib import Path
import json,math,itertools
rows=[]
for a in [.25,.5,.9]:
 for N in [4,8,16]:
  delta=1/N;sigma2=1.5;nu=2-a;den=(1-a)*(2-a)
  C=[[sigma2*delta**(1-a)*((abs(i-j)+1)**nu+abs(abs(i-j)-1)**nu-2*abs(i-j)**nu)/den for j in range(N)] for i in range(N)]
  assert all(x>0 for row in C for x in row)
  actual=delta**2*sum(map(sum,C));target=delta*sigma2*2/den
  assert abs(actual/target-1)<1e-11
  diagonal_only=delta**2*sum(C[i][i] for i in range(N))
  maximum_lipschitz_square=max(C[i][i] for i in range(N))
  if N<=8:
   sign_max=max(delta**2*sum(s[i]*s[j]*C[i][j] for i in range(N) for j in range(N)) for s in itertools.product([-1,1],repeat=N))
   assert abs(sign_max/target-1)<1e-11
  else:sign_max=None
  assert diagonal_only<actual and maximum_lipschitz_square>actual
  rows.append({'a':a,'N':N,'delta':delta,'spatial_test_variance':sigma2,
    'signed_average_variance':actual,'target_delta_sigma2_Ca':target,
    'l1_average_CM_lipschitz_square_by_sign_enumeration':sign_max,
    'maximum_CM_lipschitz_square':maximum_lipschitz_square,
    'false_independent_blocks_variance':diagonal_only,
    'mean_l1_average':math.sqrt(2/math.pi)*math.sqrt(C[0][0]),
    'scope':'Floating covariance/completion calibration; NOT a full operator/SPDE/exponential equivalence theorem.'})
Path(__file__).with_name('scalar-blocks-v0.json').write_text(json.dumps({'status':'PRE-PROOF CALIBRATION ONLY','rows':rows,'precision':'ordinary double, no rigorous error enclosure','model':'Actual raw-time |s-t|^-a Gaussian covariance tested on fixed spatial q with B(q,q)=3/2. Original Gamma is unchanged; only the auxiliary test is scaled.'},indent=2)+'\n')
print('9 actual scalar block-covariance cases and sign enumeration at N4/8 pass; no SPDE upper claim.')
