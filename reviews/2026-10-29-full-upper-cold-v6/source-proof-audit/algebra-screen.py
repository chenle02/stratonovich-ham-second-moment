"""Falsify literal intermediate source formulas;not a theorem counterexample."""
from fractions import Fraction as F
from pathlib import Path
import json

rows=[]
for n in range(1,6):
    lambdas=[F(j+1) for j in range(2*n)]
    times=[F(j+1) for j in range(n)]+[F(2*(j+1)) for j in range(n)]
    gaps=[]
    for lo in [0,n]:
        gaps += [times[j]-(times[j-1] if j>lo else 0) for j in range(lo,lo+n)]
    printed=[sum(lambdas[j:n],F(0)) for j in range(n)]+[sum(lambdas[n+j:2*n],F(0)) for j in range(n,2*n)]
    corrected=[sum(lambdas[j:n if j<n else 2*n],F(0)) for j in range(2*n)]
    target=sum((x*y for x,y in zip(lambdas,times)),F(0))
    bad=sum((x*y for x,y in zip(printed,gaps)),F(0));good=sum((x*y for x,y in zip(corrected,gaps)),F(0))
    assert bad!=target and good==target
    rows.append({'n':n,'lhs':str(target),'printed_rhs':str(bad),'corrected_rhs':str(good)})
normalizations=[]
for a,b in [(F(1),F(1)),(F(1,2),F(3)),(F(2),F(3))]:
    integral=F(4)/(a*a*b*b)
    printed=a*b*integral;corrected=a*a*b*b/F(4)*integral
    assert corrected==1
    normalizations.append({'theta1':str(a),'theta2':str(b),'printed_product':str(printed),'corrected_product':str(corrected)})
S1=S2=F(1,4);cross=F(1,4)
assert cross*cross<=S1*S2 and cross>S1*S2
# All admissible pair-count patterns are safely bounded after adding1.
patterns=0
for n in range(1,6):
 for a in range(n+1):
  for b in range(n-a+1):
   c=n-a-b
   # Square to avoid fractional powers from mutual Cauchy--Schwarz.
   for x,y in [(F(1,4),F(1,4)),(F(1,3),F(3)),(F(2),F(4))]:
    assert x**(2*a+c)*y**(2*b+c)<=(1+x)**(2*n)*(1+y)**(2*n)
    patterns+=1
out={'status':'Literal source-step issues confirmed by exact algebra',
     'source_pdf_sha256':'5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c',
     'rendered_pages_checked':[25,26,27,28],
     'second_chain_tail_index_cases':rows,
     'Laplace_horizon_normalization_cases':normalizations,
     'occupation_power_negative_control':{'S1':str(S1),'S2':str(S2),'cross':str(cross),'sqrt_CS_bound_satisfied':True,'printed_product_bound_fails':True},
     'safe_one_plus_bound_cases':patterns,
     'heat_filter_issue':'p26drops factor1/2from the spatial Gaussian exponent between consecutive equality lines;monotonicity/zero-width limit survives after retaining it',
     'scope':'Intermediate proof formulas,not falsification of Theorem4.1 or a source-normalization correction. Full reconstruction and independent review still required.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['second_chain_tail_index_cases','Laplace_horizon_normalization_cases']},indent=2))
