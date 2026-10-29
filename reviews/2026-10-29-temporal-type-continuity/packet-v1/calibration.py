"""Finite full-two-chain interpolation checks;not an SPDE theorem."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import math,json

def A1(a):return Q(2)/((1-a)*(2-a)*(3-a))
exact=[]
for l in [Q(0),Q(1,8),Q(1,4)]:
 for h in [Q(1,2),Q(3,4)]:
  for theta in [Q(1,2),Q(1,3),Q(2,3),Q(1,4),Q(3,4)]:
   a=(1-theta)*l+theta*h;n=theta.denominator;m=theta.numerator
   assert A1(a)**n<=A1(l)**(n-m)*A1(h)**m
   exact.append((l,a,h,theta))
# Already source-checked exact static order4rows include all fifteen diagrams.
zero=Q(11,17280);unequal=Q(143,34560);equal=Q(187,17280)
assert 2*zero+2*unequal+equal==Q(11,540)
assert equal!=Q(11,540) and equal+2*unequal!=Q(11,540)
D=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
def area(a,b,c):
 return 4*a*b-max(a+b-c,0)**2+max(abs(a-b)-c,0)**2

def spatial(times,chains,pairs):
 colors={v:i for i,pair in enumerate(pairs) for v in pair}
 bounds=[None,None,None]
 for chain in chains:
  prev=None
  for v in chain:
   gap=times[v]-(Q(0) if prev is None else times[prev])
   if prev is None:kind=colors[v]
   elif colors[prev]!=colors[v]:kind=2
   else:prev=v;continue
   bounds[kind]=gap if bounds[kind] is None else min(bounds[kind],gap)
   prev=v
 a,b,c=bounds
 if a is None:return b*c/4
 if b is None:return a*c/4
 if c is None:return a*b/4
 return area(a,b,c)/16
atoms=[]
for times in [[Q(x,11) for x in [1,3,6,10]],[Q(x,10) for x in [1,2,4,8]]]:
 for m in range(5):
  for first in combinations(range(4),m):
   second=tuple(x for x in range(4) if x not in first)
   for pair in D:
    weight=spatial(times,[first,second],pair)
    q=abs(times[pair[0][0]]-times[pair[0][1]])*abs(times[pair[1][0]]-times[pair[1][1]])
    assert weight>=0 and q>0
    atoms.append((weight,q))
assert len(atoms)==96

def sample(a):return sum(float(w)*math.exp(-float(a)*math.log(float(q))) for w,q in atoms)
ratios=[]
for l,a,h,theta in exact:
 left=sample(a);right=sample(l)**float(1-theta)*sample(h)**float(theta)
 assert left<=right*(1+1e-12)
 ratios.append(left/right)
result={'status':'PASS finite calibrations only','exact_order_two_Holder_cases':len(exact),'static_order_four':'2*(11/17280)+2*(143/34560)+187/17280=11/540','negative_controls':'Dropping empty/unequal splits fails the exact static coefficient','positive_atomic_order_four_points':len(atoms),'all_split_Holder_cases':len(ratios),'maximum_atomic_Holder_ratio':max(ratios),'scope':'Atomic samples include all3pairings and all16ordered split assignments at each of2time grids;not continuum quadrature. Does not prove joint limits,all-order interpolation,actual growth-type continuity or novelty.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
