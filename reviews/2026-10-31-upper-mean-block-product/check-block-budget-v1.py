"""Scoped actual free-sector and finite budget/time-order diagnostics."""
from fractions import Fraction as F
import json
import mpmath as mp

def opnorm(A):
    a,b,c,d=list(A); ss=a*a+b*b+c*c+d*d; det=a*d-b*c
    return mp.sqrt((ss+mp.sqrt(max(mp.mpf(0),ss*ss-4*det*det)))/2)
def flow(v,t):
    if v==0:return mp.matrix([[1,t],[0,1]])
    z=mp.sqrt(v);return mp.matrix([[mp.cosh(z*t),mp.sinh(z*t)/z],
                                 [z*mp.sinh(z*t),mp.cosh(z*t)]])
def mpf(q):return mp.mpf(q.numerator)/q.denominator
free=[]
for B in [1,2,4,8,16,64,256]:
    vals=[]
    for prec in [40,70]:
        with mp.workdps(prec):
            tau=mp.matrix([[1,B],[0,1]]);n=opnorm(tau)
            jordan=(mp.sqrt(B*B+4)+B)/2
            assert abs(n-jordan)<mp.mpf(10)**(-prec+8)*max(1,n)
            vals.append(mp.log(n)/B)
    assert abs(vals[0]-vals[1])<mp.mpf('1e-25')
    assert vals[1]>0
    free.append({'B':B,'constant_sector_product_rate':mp.nstr(vals[1],26),
                 'scope':'actual invariant free constant sector only; not full free F norm'})
clocks=[]
for B in [1,2,5]:
    for ratio in [F(1,7),F(2,15),F(3,19),F(5,32)]:
        delta=ratio/B;nfull=(1/(delta*B)).numerator//(1/(delta*B)).denominator
        ell=1/delta-nfull*B
        assert 0<=ell<B and nfull*delta*B+delta*ell==1
        assert delta*(nfull+1)<=F(2,B)
        clocks.append({'B':B,'delta':str(delta),'N':nfull,'ell_last':str(ell),
                       'slow_length_sum':'1'})
r=F(3);nu=F(5,3);theta=1/nu;a=F(1,2);p=F(7,4)
assert F(1,2)<theta<F(3,4) and 1/(1-theta)<r<2/a and nu<=p<2<r
threshold=[]
for m,s in [(0,8),(0,6),(1,10),(1,8)]:
    criterion=s>r*(3+m)/(r-nu)
    ex1=3*(r*(3+m)-s*r);ex2=3*(r*(3+m)+s*(nu-r))
    assert ex1.denominator==ex2.denominator==1
    assert criterion==(ex2<0)
    for n in [2,4,8,16]:
        f=lambda e:F(n**int(e)) if e>=0 else F(1,n**int(-e))
        threshold.append({'m':m,'s':s,'n':n,'B':n**3,'meets_strict_threshold':criterion,
                          'first_tail_scaling':str(f(ex1)),
                          'nu_tail_scaling':str(f(ex2))})
last=[]
for n in [2,4,8,16]:
    delta=F(1,n**9);B=3;N=n**9//B;ell=n**9-N*B
    assert ell in [1,2] and delta*N*B+delta*ell==1
    last.append({'B':B,'n':n,'delta':str(delta),'ell_last':ell,
                 'delta_to_1_minus_nu_over_r':str(F(1,n**4)),
                 'scope':'exact worst Lr budget exponent; no actual CM profile constructed'})
noncomm=[]
for B,x in [(B,x) for B in [1,2,4] for x in [F(1,3),F(1,2),F(2,3)]]+[(1,F(0)),(1,F(1))]:
    with mp.workdps(70):
        xi=mpf(x);t=mp.mpf(B)
        left=flow(1,(1-xi)*t)*flow(0,xi*t)
        reverse=flow(0,xi*t)*flow(1,(1-xi)*t)
        frozen=flow(1-xi,t)
        g=opnorm(left-frozen);h=opnorm(left-reverse)
        if x in [0,1]:assert g==h==0
        else:assert g>0 and h>0
    diag=-F(B*B,2)*x*(1-x)
    upper=-F(B**3,3)*(x-x**3)
    if 0<x<1:assert diag and upper
    noncomm.append({'B':B,'switch_fraction':str(x),'flow_freeze_gap_norm2':mp.nstr(g,24),
                    'reverse_order_gap_norm2':mp.nstr(h,24),
                    'exact_interaction_primitive_gap_diag':str(diag),
                    'exact_interaction_primitive_gap_upper':str(upper),
                    'scope':'finite scalar-wave phase toy, not compact spatial/CM/F operator'})
print(json.dumps({'scope':'finite diagnostics only; no certified enclosure or uniform operator/CM/SPDE proof',
                  'free_constant_sector':free,'last_clock_cases':clocks,
                  'threshold_cases':threshold,'worst_last_exponents':last,
                  'noncommuting_toy_cases':noncomm},indent=2))
