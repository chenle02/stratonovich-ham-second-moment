#!/usr/bin/env python3
"""Candidate identities/quadratures and exact scalar control only."""
import mpmath as mp,json
mp.mp.dps=50
potential=[]
for a in map(mp.mpf,['0.1','0.5','0.9']):
    r=(1-a)/2;C=mp.gamma(r)*mp.gamma(1-r)
    def density(t):return (t*(1-t))**(-r)/C
    for s in map(mp.mpf,['0','0.25','0.5','0.9','1']):
        power=1/(1-a)
        value=mp.mpf(0)
        if s>0:
            value+=s**(1-a)/(1-a)*mp.quad(lambda u:density(s*(1-u**power)),[0,1])
        if s<1:
            value+=(1-s)**(1-a)/(1-a)*mp.quad(lambda u:density(s+(1-s)*u**power),[0,1])
        assert mp.almosteq(value,1,rel_eps=mp.mpf('1e-18')),(a,s,value)
        potential.append({'a':str(a),'sigma':str(s),'potential':mp.nstr(value,35),'error':mp.nstr(abs(value-1),8)})
    mass=mp.beta(1-r,1-r)/C
    formula=mp.gamma((1+a)/2)/(mp.gamma(1+a)*mp.gamma((1-a)/2))
    assert mp.almosteq(mass,formula,rel_eps=mp.mpf('1e-45'))
a=mp.mpf('0.5');alpha=mp.mpf(1);q=4-alpha;d=q-2*a
cap=mp.gamma(1+a)*mp.gamma((1-a)/2)/mp.gamma((1+a)/2)
gap=(q*mp.log(q)+(q-2*a)*mp.log(q-2*a))/2-(q-a)*mp.log(q-a)
# Drop exp(-u lambda), then integrate actual Gaussian-Laplace upper bound.
row_upper=mp.gamma(a/2)/mp.gamma(a)*2**(a-1)*d**(a/2)/(1-a/2)
# Log-convexity Gamma(3/4)<=pi^(1/4), retained as analytic obligation.
certified_ratio_lower=3*mp.pi**(mp.mpf(3)/4)*2**(mp.mpf(1)/4)/8
assert cap>row_upper*mp.exp(gap)
assert cap/row_upper>=certified_ratio_lower
assert certified_ratio_lower>mp.exp(gap)
left=157**3*5**4;right=9*2**28;assert left>right
out={'scope':'Candidate temporal potential identity tested by singularity-resolved quadrature; point comparison controls only. No Beta/static/spectral/energy/SPDE theorem proved.','precision_decimal_digits':50,'potential_cases':potential,'point':{'alpha':'1','a':'1/2','capacity':mp.nstr(cap,35),'row_upper':mp.nstr(row_upper,35),'exp_map_gap':mp.nstr(mp.exp(gap),35),'ratio_lower_using_Gamma_logconvexity':mp.nstr(certified_ratio_lower,35),'exact_integer_left_formula':'157^3*5^4','exact_integer_right_formula':'9*2^28','exact_left':str(left),'exact_right':str(right),'exact_difference':str(left-right),'pi_lower_bound_required':'pi>157/50'},'all_assertions_passed':True}
print(json.dumps(out,indent=2))
