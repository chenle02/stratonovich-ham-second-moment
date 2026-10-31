"""Exact finite noncommuting controls; no operator-Young/SPDE proof."""
from fractions import Fraction as F
import json
N=3
I=[[F(i==j) for j in range(N)] for i in range(N)]
def add(*ms):return [[sum(m[i][j] for m in ms) for j in range(N)] for i in range(N)]
def scale(a,m):return [[a*v for v in row] for row in m]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def norm(m):return max(sum(abs(v) for v in row) for row in m)
def units(i,j):return [[F(r==i and c==j) for c in range(N)] for r in range(N)]
rows=[]; killed_conjugation=killed_right_product=0
for a,b in [(F(1),F(1)),(F(2),F(1,3)),(F(-1),F(2)),(F(0),F(1)),(F(1),F(0))]:
 A=scale(a,units(0,1));B=scale(b,units(1,2));AB=mul(A,B)
 for t in [F(0),F(1,4),F(1)]:
  H=add(I,scale(t,A));V=add(I,scale(t,B),scale(-t*t/2,AB))
  exact=add(I,scale(t,A),scale(t,B),scale(t*t/2,AB))
  assert mul(H,V)==exact
  wrong_conj=add(I,scale(t,B),scale(t*t/2,AB))
  c=mul(H,wrong_conj)!=exact;rp=mul(V,H)!=exact
  if a*b*t!=0:assert c and rp
  killed_conjugation+=c;killed_right_product+=rp
  projections=[I,units(0,0),scale(F(0),I)]
  for P in projections:assert norm(mul(P,exact))<=norm(mul(P,H))*norm(V)
  rows.append({'a':str(a),'b':str(b),'t':str(t),'factorization':'PASS',
               'wrong_conjugation_refuted':c,'wrong_right_product_refuted':rp,
               'full_operator_infinity_norm':str(norm(exact)),
               'endpoint_factor_norm':str(norm(H)),'error_factor_norm':str(norm(V))})
ones=[[F(1) for j in range(N)] for i in range(N)]
assert norm(ones)==3 and max(v for row in ones for v in row)==1
print(json.dumps({'scope':'3x3 nilpotent Banach-linf induced operator norm, exact rational arithmetic; finite smooth ODE controls only, not actual wave/CM or general Holder proof',
 'rows':rows,'wrong_conjugation_killed':killed_conjugation,'wrong_right_product_killed':killed_right_product,
 'left_multipliers_per_row':3,'entry_norm_guard':{'largest_entry':1,'operator_infinity_norm':3}},indent=2))
