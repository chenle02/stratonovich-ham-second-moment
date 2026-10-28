"""Exact rational bookkeeping controls; not an analytic proof."""
from fractions import Fraction as F
from pathlib import Path
import json
import math
rows=[]
for a,a0 in [(F(3,2),F(1,4)),(F(7,4),F(3,16)),(F(19,10),F(9,100)),(F(101,100),F(9,10))]:
    th=(a0+2-a)/2
    b0=a0/th
    b=(a-th)/(1-th)
    assert 0<a0<th<2-a<1 and 0<b0<1 and 1<b<2
    q=2*th+(1-th)*(3-b)
    power=th*(3-b0)+(1-th)*(4-b)
    assert q==3-a and power==4-a-a0
    rows.append({k:str(v) for k,v in {'alpha':a,'alpha0':a0,'theta':th,'endpoint_time':b0,'static_beta':b,'factorial_power':q,'time_power':power}.items()})
counts=[]
for k in range(1,5):
    P=math.factorial(2*k)//(2**k*math.factorial(k))
    splits=sum(F(1,math.factorial(m)*math.factorial(2*k-m)) for m in range(2*k+1))
    assert P*splits==F(2**k,math.factorial(k))
    counts.append({'k':k,'pairings':P,'split_sum':str(splits),'combined':str(P*splits)})
Path(__file__).with_name('finite-algebra-checks.json').write_text(json.dumps({'status':'exact rational and finite checks only; no analytic proof','parameter_rows':rows,'temporal_count_rows':counts},indent=2)+'\n')
print('4 exact parameter witnesses and k=1..4 pairing/split identities PASS')
