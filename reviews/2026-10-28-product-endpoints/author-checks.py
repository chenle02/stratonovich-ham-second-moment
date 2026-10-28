#!/usr/bin/env python3
"""Exact finite checks of canonical midpoint choices, not proof or Lean."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,math

def endpoint(a,a0):
    alpha=sum(a)
    assert all(0<=x<1 for x in a) and 1<alpha<2 and 0<a0<2-alpha
    theta=(a0+2-alpha)/2
    L=[max(F(0),(x-1+theta)/theta) for x in a]
    U=[min(F(1),x/theta) for x in a]
    assert sum(L)<1<sum(U)
    lam=(1-sum(L))/(sum(U)-sum(L))
    bb=[l+lam*(u-l) for l,u in zip(L,U)]
    vv=[(x-theta*y)/(1-theta) for x,y in zip(a,bb)]
    b0=a0/theta;beta=(alpha-theta)/(1-theta)
    assert a0<theta<2-alpha and 0<b0<1 and alpha<beta<2
    assert sum(bb)==1 and sum(vv)==beta
    assert 2*theta+(1-theta)*(3-beta)==3-alpha
    assert theta*(3-b0)+(1-theta)*(4-beta)==4-alpha-a0
    Q,Nu=3-beta,4-beta
    assert Nu-Q==1 and Nu/Q-1==1/Q
    for x,y,z in zip(a,bb,vv):
        assert x==theta*y+(1-theta)*z
        assert (y==z==0) if x==0 else (0<y<1 and 0<z<1)
    return {'a':list(map(str,a)),'alpha0':str(a0),'theta':str(theta),'b':list(map(str,bb)),
            'v':list(map(str,vv)),'b0':str(b0),'beta':str(beta),
            'active_coordinates':[j+1 for j,x in enumerate(a) if x>0]}
count=0;zeros=0
for a in product([F(0),F(1,4),F(1,2),F(3,4)],repeat=3):
    if not 1<sum(a)<2:continue
    for f in [F(1,10),F(1,2),F(9,10)]:
        endpoint(a,(2-sum(a))*f);count+=1;zeros+=any(x==0 for x in a)
examples=[endpoint((F(9,10),F(3,5),F(0)),F(1,8)),
          endpoint((F(99,100),F(99,100),F(0)),F(1,100)),
          endpoint((F(1,2),F(1,2),F(1,2)),F(1,4))]
try:endpoint((F(1),F(1,2),F(0)),F(1,4))
except AssertionError:excluded_one_refused=True
else:raise AssertionError('Excluded coordinate exponent1 accepted')
counts=[{'k':k,'pairings':math.factorial(2*k)//(2**k*math.factorial(k)),
         'splits':2*k+1,'components':(2*k+1)*math.factorial(2*k)//(2**k*math.factorial(k))} for k in [1,2]]
out={'status':'exact finite controls only; no analytic or independent-review claim',
     'canonical_midpoint_grid_cases':count,'grid_cases_with_zero_coordinate':zeros,
     'all_assertions_pass':True,'excluded_coordinate_one_refused':excluded_one_refused,
     'static_p2_factor_check':'Nu-Q=1, hence 2^(-Q)*2^Nu=2; also Nu/Q-1=1/Q',
     'examples':examples,'full_disjoint_measure_counts':counts,
     'limitations':['not a proof of the continuous exponent lemma','not a stochastic convergence test',
                    'not a certificate for the covariance-comparison hypothesis of an arbitrary covariance']}
Path(__file__).with_name('author-checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
