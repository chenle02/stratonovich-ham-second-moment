#!/usr/bin/env python3
"""Exact parameter/count controls plus floating first-order Holder calibration."""
from fractions import Fraction as F
from pathlib import Path
import json,math
import mpmath as mp
mp.mp.dps=60
alpha,a0,theta=F(7,4),F(3,16),F(7,32)
b0=a0/theta; beta=(alpha-theta)/(1-theta)
assert b0==F(6,7) and beta==F(49,25)
assert a0<theta<2-alpha and 0<b0<1 and 1<beta<2
assert 2*theta+(1-theta)*(3-beta)==3-alpha
assert theta*(3-b0)+(1-theta)*(4-beta)==4-alpha-a0
assert alpha+2*a0>2

def matchings(v):
    if not v:
        yield ();return
    for j in v[1:]:
        for rest in matchings(tuple(x for x in v[1:] if x!=j)):
            yield ((v[0],j),)+rest
counts=[]
for k in (1,2):
    ps=list(matchings(tuple(range(1,2*k+1))))
    assert len(ps)==math.factorial(2*k)//(2**k*math.factorial(k))
    counts.append({'k':k,'pairings':len(ps),'splits':2*k+1,
                   'full_disjoint_components':len(ps)*(2*k+1),
                   'empty_chain_components':2*len(ps)})

def number(x):return mp.mpf(x.numerator)/x.denominator
c,t=mp.mpf(3)/7,mp.mpf(2)/3

def j02(degree,temporal,d):
    degree,temporal=number(degree),number(temporal)
    spatial=c if d==3 else c*mp.beta(1-degree/2,mp.mpf(1)/2)/2
    return spatial*t**(4-degree-temporal)/((2-degree-temporal)*(3-degree-temporal)*(4-degree-temporal))
rows=[]
for d in (2,3):
    target=j02(alpha,a0,d);low=j02(F(1),b0,d);static=j02(beta,F(0),d)
    rhs=low**number(theta)*static**(1-number(theta))
    assert target<=rhs
    rows.append({'d':d,'target_J02':mp.nstr(target,35),'low_J02':mp.nstr(low,35),
                 'static_J02':mp.nstr(static,35),'holder_rhs':mp.nstr(rhs,35),
                 'ratio':mp.nstr(target/rhs,35)})
output={'scope':'author diagnostics only; numerical values are not certified enclosures',
        'parameters':{k:str(v) for k,v in [('alpha',alpha),('alpha0',a0),('theta',theta),('b0',b0),('beta',beta)]},
        'amplitude':'3/7','time':'2/3','precision_decimal_digits':60,
        'exact_affine_and_interval_checks':True,'exact_counts':counts,
        'same_chain_k1_floating_holder_check':rows,
        'not_claimed':['finite counts as all-order proof','numerical inequality as analytic proof','static coefficient constant evaluated']}
Path(__file__).with_name('author-checks.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
