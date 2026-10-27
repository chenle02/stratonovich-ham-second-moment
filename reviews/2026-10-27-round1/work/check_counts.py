"""Finite falsification controls; not an all-order proof."""
from fractions import Fraction
from math import factorial
import json

def pairings(xs):
    if not xs:
        yield ()
        return
    x=xs[0]
    for i,y in enumerate(xs[1:],1):
        for tail in pairings(xs[1:i]+xs[i+1:]):
            yield ((x,y),)+tail

rows=[]
for k in range(1,5):
    ps=list(pairings(tuple(range(2*k))))
    expected=factorial(2*k)//(2**k*factorial(k))
    assert len(ps)==expected
    by_split=[]
    for m in range(2*k+1):
        counts={}
        for D in ps:
            cross=sum((a<m)!=(b<m) for a,b in D)
            counts[cross]=counts.get(cross,0)+1
        assert sum(counts.values())==expected
        by_split.append({'m':m,'n':2*k-m,'cross_pair_counts':counts})
    rows.append({'k':k,'pairings':expected,'terms_all_splits':(2*k+1)*expected,'splits':by_split})
a0=Fraction(1,2)
c0=1/((1-a0)*(2-a0)*(3-a0))
result={'scope':'exact finite counts through total order eight; white-space order-two coefficient at alpha0=1/2',
        'rows':rows,'white_test':{'I11_coefficient':str(c0),'I02_coefficient':str(c0/2),'total_degree_two_coefficient':str(2*c0)}}
print(json.dumps(result,indent=2))
