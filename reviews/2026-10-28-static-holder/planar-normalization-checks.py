#!/usr/bin/env python3
"""Finite exact parameter and normalization controls, not proof certification."""
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=60
alpha,a0,theta=F(3,2),F(1,4),F(3,8)
b0=a0/theta;beta=(alpha-theta)/(1-theta)
assert b0==F(2,3) and beta==F(9,5)
assert a0<theta<2-alpha and alpha<beta<2
assert theta*(alpha-1)+(1-theta)*(alpha-beta)==0
assert 2*theta+(1-theta)*(3-beta)==3-alpha
assert theta*(3-b0)+(1-theta)*(4-beta)==4-alpha-a0
# Gamma=|x1|^-1/2 dx1 delta_0(dx2): integral over unit ball=4.
atom_mass=F(4); S_atom=(2-alpha)*atom_mass
assert S_atom==2 and S_atom/4==F(1,2)
assert (alpha-1)-F(1,2)==0
# Riesz gamma=c|x|^-alpha: unit-ball mass=2*pi*c/(2-alpha).
# Verify the rational prefactor; the common symbolic pi cancels.
c=F(3,7);ball_prefactor=2*c/(2-alpha)
assert (2-alpha)*ball_prefactor==2*c
# Product covariance: four quadrants and u=sin(phi)^2 give
# S=2*Beta((1-a1)/2,(1-a2)/2), with both arguments positive.
a1,a2=F(9,10),F(3,5)
assert a1+a2==alpha
x,y=(1-a1)/2,(1-a2)/2
assert x==F(1,20) and y==F(1,5)
val=2*mp.beta(mp.mpf(x.numerator)/x.denominator,mp.mpf(y.numerator)/y.denominator)
out={'status':'author normalization controls; not scientific review or Lean',
'parameters':{k:str(v) for k,v in [('alpha',alpha),('alpha0',a0),('theta',theta),('b0',b0),('beta',beta)]},
'exact_radial_weight_cancellation':True,'exact_coefficient_powers':True,
'riesz':{'amplitude':str(c),'S':'2*pi*c','closing_constant':'pi*c/2'},
'atomic_angular':{'covariance':'|x1|^(-1/2) dx1 delta_0(dx2)','unit_ball_mass':str(atom_mass),'S':str(S_atom),'Gamma_low':'Lebesgue measure on x1-axis','closing_constant':str(S_atom/4)},
'product':{'a1':str(a1),'a2':str(a2),'S_exact':'2*B(1/20,1/5)','S_floating':mp.nstr(val,40),'precision_digits':60},
'limitations':['exact normalization/algebra only','Beta decimal not a certified enclosure','no empirical moment estimate','physical angular mass not identified with general spectral mass']}
Path(__file__).with_name('planar-normalization-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
