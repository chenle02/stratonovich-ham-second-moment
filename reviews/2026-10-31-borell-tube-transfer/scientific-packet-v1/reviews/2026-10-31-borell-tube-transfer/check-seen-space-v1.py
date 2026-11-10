"""Exact finite Gaussian seen-space and scalar-tail integral calibrations."""
from pathlib import Path
import json
import sympy as s
b=s.Matrix([s.Rational(3,5),s.Rational(4,5),0]);a=s.Matrix([1,2])
cases=[('identity',s.eye(2),s.eye(2),s.Matrix([1,-2])),('unused_coordinate',s.Matrix([[1,0,0],[0,2,0]]),s.diag(1,1,0),s.Matrix([1,s.Rational(-1,2)])),('rank_one',a*b.T,b*b.T,s.Matrix([1,1])),('zero',s.zeros(2,3),s.zeros(3),s.Matrix([1,1]))]
rows=[]
for name,A,P,p in cases:
 assert P.T==P and P*P==P and A*P==A and P.rank()==A.rank()
 phi=s.Matrix(list(range(1,A.cols+1)));seen=P*phi;unused=phi-seen
 assert A*phi==A*seen and (seen.T*unused)[0]==0
 v=(A.T*p).dot(A.T*p);opt=A.T*p;score=(p.T*A*opt)[0]-opt.dot(opt)/2
 assert score==v/2
 assert phi.dot(phi)-seen.dot(seen)==unused.dot(unused)
 rows.append({'case':name,'covariance_rank':A.rank(),'raw_dimension':A.cols,'linear_MGF_rate_exact':str(v/2),'optimal_control_score_exact':str(score),'same_image_exact':[str(x) for x in A*phi],'minimum_seen_preimage_norm_squared':str(seen.dot(seen)),'full_raw_preimage_norm_squared':str(phi.dot(phi)),'unused_raw_norm_squared':str(unused.dot(unused)),'wrong_full_norm_depends_on_unused_direction':bool(unused.dot(unused)>0)})
r,delta,M=s.symbols('r delta M',positive=True)
f=4*s.exp(-r*r/(8*delta))
assert s.simplify(-s.diff(f,r)-r/delta*s.exp(-r*r/(8*delta)))==0
integral=s.integrate(r/delta*s.exp(-r*r/(8*delta)),(r,M,s.oo))
assert s.simplify(integral-4*s.exp(-M*M/(8*delta)))==0
combined=s.exp(-M*M/(8*delta))*integral
assert s.simplify(combined-4*s.exp(-M*M/(4*delta)))==0
out={'scope':'4exact finite Gaussian seen-space/linear variational cases and symbolic Rayleigh tail primitive; CAS algebra not Lean or infinite-dimensional proof','cases':rows,'tail_integral_exact':str(integral),'combined_cutoff_tail_exact':str(combined),'sympy_version':s.__version__}
Path(__file__).with_name('seen-space-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('4 exact seen-space/linear-Gaussian cases and Rayleigh tail primitive pass')
