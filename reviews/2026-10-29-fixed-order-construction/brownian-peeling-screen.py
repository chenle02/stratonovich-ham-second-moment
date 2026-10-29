"""Exact finite falsification of the Brownian pairing bound; not analytic proof."""
from fractions import Fraction as Q
from pathlib import Path
import json

def pairings(items):
 if not items:
  yield [];return
 x,*tail=items
 for h in tail:
  for rest in pairings([v for v in tail if v!=h]):yield [(x,h)]+rest

def determinant(matrix):
 a=[row[:] for row in matrix];out=Q(1)
 for i in range(len(a)):
  pivot=next(j for j in range(i,len(a)) if a[j][i])
  if pivot!=i:a[i],a[pivot]=a[pivot],a[i];out=-out
  p=a[i][i];out*=p
  for j in range(i+1,len(a)):
   f=a[j][i]/p
   for k in range(i+1,len(a)):a[j][k]-=f*a[i][k]
 return out

cases=0;partitions=0;strict=0
for j in range(1,5):
 for D in pairings(list(range(1,2*j+1))):
  partitions+=1
  partner={a:b for edge in D for a,b in [edge,edge[::-1]]}
  for gaps in [[Q(1)]*(2*j),[Q(i,3) for i in range(1,2*j+1)],[Q(1,i) for i in range(1,2*j+1)],[Q(1 if i%2 else 7,5) for i in range(1,2*j+1)]]:
   t=[Q(0)]
   for g in gaps:t.append(t[-1]+g)
   remain=set(range(1,2*j+1));selected=[];selected_gap_product=Q(1)
   while remain:
    last=max(remain);h=partner[last];prev=max(remain-{last},default=0)
    gap=t[last]-t[prev]
    assert gap>=gaps[last-1]>0
    selected.append(last);selected_gap_product*=gap
    remain-={last,h}
   assert len(selected)==len(set(selected))==j
   C=[[min(t[b],t[d])-min(t[b],t[c])-min(t[a],t[d])+min(t[a],t[c]) for c,d in D] for a,b in D]
   for width in [Q(0),Q(1,10),Q(2)]:
    M=[[C[a][b]+(width if a==b else 0) for b in range(j)] for a in range(j)]
    det=determinant(M)
    # For Gamma=delta0, E product p_width(B_b-B_a) equals
    # (2*pi)^(-j/2)/sqrt(det(C+width*I)). Compare the proved heat bound.
    assert det>=selected_gap_product>0,(D,t,width,det,selected_gap_product)
    strict+=det>selected_gap_product;cases+=1
result={'status':'PASS exact finite checks only','pair_partitions_orders_one_through_four':partitions,'Gaussian_determinant_heat_bound_cases':cases,'strict_cases':strict,'selected_endpoints_distinct_and_gaps_dominate':True,'model':'d1 white spatial covariance; Gaussian heat smoothed; exact rational Brownian increment covariances','does_not_prove':'General covariance heat bound, Brownian conditioning argument, integrated moment formula, weak/joint convergence or any SPDE theorem'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
