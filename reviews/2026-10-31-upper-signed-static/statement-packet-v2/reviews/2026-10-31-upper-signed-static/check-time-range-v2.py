"""Exact exponents for the analytic time-bubble guard; not a norm integral."""
from fractions import Fraction as F
import json
rows=[]
a=F(1,2)
assert (a/2-1)*2+2-a==0
for n in [1,2,4]:
    eps=F(1,2**(60*n))
    vals=[]
    for r in [F(3),F(4),F(5)]:
        ex=1/r-a/2
        intpower=60*n*ex
        assert intpower.denominator==1
        v=F(1,2**intpower.numerator) if intpower>=0 else F(2**(-intpower.numerator))
        vals.append({'r':str(r),'1_over_r_minus_a_over_2':str(ex),'local_Lr_scaling':str(v)})
    rows.append({'n':n,'epsilon':str(eps),'rows':vals})
print(json.dumps({'scope':'exact exponent/scaling-factor check for a=.5; no Gaussian/operator/SPDE norm computed; local lower profile constant not evaluated','raw_Ht_norm_squared_scaling_exponent':'0','rows':rows},indent=2))
