"""Bounded exact calibration for proposed lower route;not an SPDE proof."""
from fractions import Fraction as F
from pathlib import Path
import json

scales=[]
for alpha in [F(1,4),F(1,2),F(1),F(3,2),F(7,4)]:
    for a in [F(1,16),F(1,8),F(1,4),F(1,2),F(3,4)]:
        if a>=1 or a+alpha>=2:
            continue
        nu=3-alpha;q=(4-alpha)/nu;kappa=(4-alpha-a)/nu
        static_clock=1-a/(4-alpha)
        assert static_clock*q==kappa
        wrong_clock=1-2*a/(4-alpha)
        assert wrong_clock*q!=kappa
        assert kappa-wrong_clock*q==a/nu
        scales.append({'alpha':str(alpha),'alpha0':str(a),'static_clock_power':str(static_clock),'kappa':str(kappa)})

# The already-reviewed first mean coefficient for d=alpha=1 at horizon1.
def m1(a):
    return F(1,2)/((1-a)*(2-a)*(3-a))

holder_cases=0
for b in [F(1,4),F(1,2),F(3,4)]:
    for denominator in range(2,9):
        for numerator in range(1,denominator):
            theta=F(numerator,denominator);a=theta*b
            assert m1(a)**denominator<=m1(F(0))**(denominator-numerator)*m1(b)**numerator
            holder_cases+=1

# Test the proposed separation algebra on anchors Mb/K0=2^j.
windows=0
for alpha in [F(1,4),F(1,2),F(1),F(3,2),F(7,4)]:
    nu=3-alpha;q=(4-alpha)/nu
    for j in range(1,9):
        theta=F(1,2*j)
        mean_relative_exponent=F(j)*theta/nu
        ratio_gap_exponent=q-1-mean_relative_exponent
        assert ratio_gap_exponent==F(1,2)/nu>0
        windows+=1

out={'status':'PASS finite exact calibration only','scaling_cases':len(scales),
     'scalings':scales,'white_order_two_Holder_cases':holder_cases,
     'strict_window_exponent_cases':windows,
     'negative_control':'Using T^-alpha0 as amplitude rather than variance loses alpha0/nu in the time exponent;all cases refused',
     'does_not_prove':'Full-model covariance comparison,coefficient Holder at all orders,entire-series asymptotics,strict intermittency or theorem novelty'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='scalings'},indent=2))
