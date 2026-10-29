"""Exact finite controls for the scalar-shape obstruction;not an SPDE result."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
checks=0
for x in [Q(1),Q(9,8),Q(5,4),Q(3,2),Q(7,4),Q(2)]:
 for k in range(1,13):
  b=sum(comb(k,j)**2 for j in range(k+1))
  assert b<=4**k
  assert x**(2*k)*b<=(8*x)**k
  checks+=1
 ratio_squared=Q(8)/x
 assert 4<=ratio_squared<=8
 if x>1:assert ratio_squared<8
result={'status':'PASS exact finite controls only','Jensen_coefficient_cases':checks,'ratio_squared':'8/x in[4,8],strictly below8forx>1','scope':'Supports the explicitly proved scalar-shape inference obstruction;NOT an SPDE counterexample,physical rate formula or novelty claim'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
