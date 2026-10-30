#!/usr/bin/env python3
"""Scalar optimization/normalization controls; no SPDE/energy evaluator."""
import mpmath as mp
import json
mp.mp.dps=80
cases=[('1','0.1','0.5','1','1/7'),('0.5','0.25','1','2','2'),('0.25','0.75','2','3','1.5'),('1','0.9','1','2','3'),('0.75','0.5','0.5','1','2'),('0.1','0.9','1','2','1')]
def number(s):
    if '/' in s:
        a,b=s.split('/');return mp.mpf(a)/mp.mpf(b)
    return mp.mpf(s)
def show(x):return mp.nstr(x,45)
rows=[]
integer_gap_left=39**39*21**21
integer_gap_right=2*30**60
assert integer_gap_left>integer_gap_right
for aa,tt,nn,cc,ee in cases:
    alpha,a,eta,c,E=map(number,[aa,tt,nn,cc,ee])
    q=4-alpha;k=3-alpha;beta=alpha/4
    assert 0<alpha<=1 and 0<a<1 and alpha+a<2
    M=(2*E/(2-alpha))**((2-alpha)/2)*(2*eta/alpha)**(alpha/2)
    A=mp.sqrt(q/4)*(alpha/4)**(alpha/(2*q))*M**(1/q)
    v=(2*c*A/q)**(q/k)
    T=(beta*mp.sqrt(v*M))**(1/(1-beta))
    I2=mp.sqrt(v*M)*T**beta-T
    score=c*mp.sqrt(I2)-v/2
    F0=k*((2*E/(2-alpha))**((2-alpha)/2)/(8*q**(q/2)))**(1/k)
    ceiling=c**(q/k)*(2*eta)**(alpha/(2*k))*F0
    assert mp.almosteq(I2,A*A*v**(2/q),rel_eps=mp.mpf('1e-65'))
    assert mp.almosteq(score,ceiling,rel_eps=mp.mpf('1e-65'))
    Fa=k*((q-2*a)**((q-2*a)/2)/(8*(q-a)**(q-a))*(2*E/(2-alpha))**((2-alpha)/2))**(1/k)
    gap=(q*mp.log(q)+(q-2*a)*mp.log(q-2*a))/2-(q-a)*mp.log(q-a)
    assert gap>0 and Fa>F0
    assert mp.almosteq(Fa/F0,mp.exp(gap/k),rel_eps=mp.mpf('1e-65'))
    wrongv=(c*A/q)**(q/k)
    wrongscore=c*A*wrongv**(1/q)-wrongv
    assert not mp.almosteq(wrongscore,ceiling,rel_eps=mp.mpf('1e-30'))
    assert mp.almosteq(wrongscore/ceiling,2**(-1/k),rel_eps=mp.mpf('1e-65'))
    omitted_eta=c**(q/k)*F0
    if eta!=mp.mpf('0.5'):assert not mp.almosteq(omitted_eta,ceiling,rel_eps=mp.mpf('1e-30'))
    # Scalar-only derivative signs, independent sampled neighboring T and v.
    for z in ['0.5','0.9','1.1','2']:
        f=number(z);Tu=T*f;vu=v*f
        assert mp.sqrt(v*M)*Tu**beta-Tu<=I2
        assert c*A*vu**(1/q)-vu/2<=ceiling
    if alpha==mp.mpf('0.1') and a==mp.mpf('0.9') and eta==1:
        assert gap>(alpha/2)*mp.log(2) and ceiling<c**(q/k)*Fa
    rows.append(dict(alpha=aa,a=tt,eta=nn,c=cc,energy_parameter=ee,M=show(M),T=show(T),v=show(v),direct_score=show(score),closed_ceiling=show(ceiling),F0=show(F0),Fa=show(Fa),Fa_over_F0=show(Fa/F0),strict_convexity_gap=show(gap),wrong_full_cost_ratio=show(wrongscore/ceiling)))
out={'scope':'Six explicit scalar optimization controls only; E is an arbitrary positive input, not a computed source/occupation energy; no physical HAM evaluator or route no-go proof','precision_decimal_digits':80,'all_assertions_passed':True,'cases':rows,'exact_integer_gap':{'left_formula':'39^39*21^21','right_formula':'2*30^60','left':str(integer_gap_left),'right':str(integer_gap_right),'strict_difference':str(integer_gap_left-integer_gap_right),'positive':True,'scope':'Exact auxiliary displayed-map gap criterion at alpha=1/10,a=9/10,eta=1; no computed occupation energy/source value'}}
print(json.dumps(out,indent=2))
