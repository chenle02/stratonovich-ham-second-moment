"""Exact exponent/gauge checks before proof; no HAM stability conclusion."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,math

def mm(a,b):
 return [[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]
rows=[]
for alpha in [F(1,4),F(1,2),F(1),F(5,4),F(3,2)]:
 for a in [F(1,10),F(1,3),F(3,4),F(99,100)]:
  if alpha+a>=2:continue
  k=(4-alpha-a)/(3-alpha)
  assert k>1
  assert -a/2+(1-k)*(2-alpha/2)==-k/2
  assert 1-a/2+(1-k)*(1-alpha/2)==k/2
  rows.append(dict(alpha=str(alpha),a=str(a),kappa=str(k),physical_space_exponent=str(1-k)))
for w in [F(-2),F(-1),F(-1,80),F(0),F(1,80),F(1),F(2)]:
 gp=[[F(1),F(0)],[w,F(1)]];gm=[[F(1),F(0)],[-w,F(1)]];A=[[F(0),F(1)],[F(1),F(0)]]
 assert mm(gm,gp)==[[1,0],[0,1]]
 assert mm(mm(gm,A),gp)==[[w,1],[1-w*w,-w]]
a=math.cosh(math.sqrt(2));b=math.sinh(math.sqrt(2))/math.sqrt(2);rho=math.acosh(a+b)/2
assert 0<rho<1
# Floating Floquet values are display only. The proof uses periodic Riccati
# and strict Cauchy--Schwarz, not this numerical sign or a clipped product.
floquet=dict(a=a,b=b,rho=rho,comparison_background_rate=1,primitive_sup_for_delta='delta',scale='delta=1/(2N)',numerical_only=True)
out=dict(status='PASS exact finite exponent/gauge controls; floating Floquet display only',exponent_cases=len(rows),rows=rows,gauge_cases=7,floquet=floquet,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),not_SPDE_residual_stability=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
