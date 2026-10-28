from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def check(a, theta):
    alpha = sum(a)
    assert F(1) < alpha < F(2) and F(0) < theta < 2-alpha
    assert all(F(0) <= x < F(1) for x in a)
    L = [max(F(0), (x-1+theta)/theta) for x in a]
    U = [min(F(1), x/theta) for x in a]
    lo, up = sum(L), sum(U)
    assert lo < 1 < up
    lam = (1-lo)/(up-lo)
    assert 0 < lam < 1
    b = [l+lam*(u-l) for l,u in zip(L,U)]
    v = [(x-theta*y)/(1-theta) for x,y in zip(a,b)]
    beta = (alpha-theta)/(1-theta)
    assert sum(b) == 1 and sum(v) == beta and alpha < beta < 2
    for x,l,u,y,z in zip(a,L,U,b,v):
        assert theta*y+(1-theta)*z == x
        if x == 0:
            assert l == u == y == z == 0
        else:
            assert l < y < u and 0 < y < 1 and 0 < z < 1
    return dict(a=list(map(str,a)),theta=str(theta),L=list(map(str,L)),U=list(map(str,U)),lam=str(lam),b=list(map(str,b)),static=list(map(str,v)),beta=str(beta))

count=0
zero_count=0
active_lower_hist={str(i):0 for i in range(4)}
for nums in product(range(10), repeat=3):
    a=tuple(F(n,10) for n in nums)
    alpha=sum(a)
    if not 1 < alpha < 2:
        continue
    for fraction in [F(1,1000),F(1,10),F(1,2),F(9,10),F(999,1000)]:
        theta=fraction*(2-alpha)
        row=check(a,theta)
        count+=1
        zero_count+=any(x==0 for x in a)
        active_lower_hist[str(sum(F(x)>0 for x in row['L']))]+=1
adversarial=[
    ((F(9,10),F(3,5),F(0)),F(1,4)),
    ((F(999,1000),F(1,1000),F(1,1000)),F(998,1000)),
    ((F(999,1000),F(999,1000),F(0)),F(1,1000)),
    ((F(2,3),F(2,3),F(1,3)),F(1,6)),
    ((F(1,2),F(1,2),F(1,2)),F(1,4)),
]
rows=[check(*case) for case in adversarial]
result={'status':'PASS','arithmetic':'exact fractions.Fraction; no floating arithmetic','grid_cases':count,'grid_cases_with_zero_coordinate':zero_count,'active_lower_count_histogram':active_lower_hist,'adversarial_cases':rows,'scope':'finite controls only, not proof or review of covariance/SPDE claims'}
Path(__file__).with_name('checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='adversarial_cases'},indent=2))
