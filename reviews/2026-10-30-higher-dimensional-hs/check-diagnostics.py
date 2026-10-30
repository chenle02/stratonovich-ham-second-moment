#!/usr/bin/env python3
"""Whole-space temporal and exact matrix/shell controls only, not a no-go proof."""
import sympy as s
import mpmath as m
import json
from pathlib import Path
m.mp.dps=50
cp,sp,cq,sq,p,q,H=s.symbols('cp sp cq sq p q H',real=True,nonzero=True)
Sm=s.Matrix([[cp,-sp/p],[p*sp,cp]])
B=s.Matrix([[0,0],[H,0]])
Sf=s.Matrix([[cq,sq/q],[-q*sq,cq]])
product=Sm*B*Sf
assert s.simplify(product[1,0]-H*cp*cq)==0
assert s.simplify(product[0,0]+H*sp*cq/p)==0
# ACTUAL raw temporal test: f(t)=t²(1-t)² on[0,1],zero elsewhere,C1.
# It belongs to the same Gaussian test completion by smooth interior approximation.
coeff=[m.mpf(16)/15,-m.mpf(64)/35,m.mpf(256)/315]
rho=[m.mpf(5)/2,m.mpf(7)/2,m.mpf(9)/2]
def kh(t):return sum(c*(t**r+(1-t)**r) for c,r in zip(coeff,rho))
def moment(r,w):
    if w==0:return 1/(r+1)
    return m.hyp1f1(r+1,r+2,1j*w)/(r+1)
def cosine(w):return m.re(sum(c*(moment(r,w)+m.exp(1j*w)*moment(r,-w)) for c,r in zip(coeff,rho)))
J=m.mpf(64)/693;assert m.almosteq(cosine(0),J,rel_eps=m.mpf('1e-45'))
assert s.integrate(s.Symbol('t')**2*(1-s.Symbol('t'))**2,(s.Symbol('t'),0,1))==s.Rational(1,30)
# Elementary uniformbounds f<=1/16,|f'|<=1/2 yield k<=1/4,Lipk<=2.
Btime=m.mpf(9)/4;threshold=4*Btime/J
rows=[]
for r in [128,256,512]:
 for diff in [m.mpf(0),m.mpf('0.25'),m.mpf('0.5'),m.mpf(1)]:
    v=m.mpf(r)+diff
    I=(cosine(m.mpf(r)-v)+cosine(m.mpf(r)+v))/2
    assert m.mpf(r)>=threshold and I>=J/8
    rows.append({'r':str(r),'s':str(v),'difference':str(diff),'actual_time_cosine_product':m.nstr(I,35),'proposed_lower_J_over_8':m.nstr(J/8,35),'positive_margin':m.nstr(I-J/8,35)})
# Independent literal quadratures at two moderate frequencies crosscheck moment formula.
for w in [m.mpf('0.5'),m.mpf(4)]:
 direct=m.quad(lambda t:kh(t)*m.cos(w*t),[0,m.mpf('0.5'),1])
 assert m.almosteq(direct,cosine(w),rel_eps=m.mpf('1e-40'))
# Exact dyadic radial-shell integrals: ignore positive sphere factor only.
shells=[]
for j in range(7):
 lo=2**j;hi=2**(j+1)
 shells.append({'j':j,'radii':[lo,hi],'d1_integral_rminus2':str(s.Rational(1,lo)-s.Rational(1,hi)),'d2_integral_rminus1':'log(2)','d3_integral_r0':str(hi-lo)})
out={'scope':'Exact 2x2 actual wave matrix and whole-space radial/temporal controls; not a Gaussian HS/SPDE no-go proof, no spatial Hhat value or source energy computed','precision_decimal_digits':50,'matrix':[[str(s.factor(product[i,j])) for j in range(2)] for i in range(2)],'temporal_test':'f(t)=t^2(1-t)^2 1_[0,1],C1zeroextension in actualrawGaussiancompletion at a=1/2','J_exact':'64/693','f_mass_exact':'1/30','time_IBP_bound':'9/4','radius_threshold_exact':str(s.Rational(4)*s.Rational(9,4)/s.Rational(64,693)),'rows':rows,'literal_quadrature_crosschecks':2,'radial_shells':shells,'all_assertions_passed':True}
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact wave-matrix control,12actualtemporal cases,2quadrature crosschecks and7radial shells PASS.')
