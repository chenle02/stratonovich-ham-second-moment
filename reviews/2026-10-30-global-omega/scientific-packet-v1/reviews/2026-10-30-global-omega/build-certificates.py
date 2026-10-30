#!/usr/bin/env python3
"""Exact rational certificates for a candidate analytic envelope; no Gamma proof."""
import sympy as s,json
from pathlib import Path
x,t=s.symbols('x t');r=s.Rational
E=1/(2*(1-x))+x*(1-x)/(2-x)+x*(x+1)*(1-x)**2/(3*(3-x))
C=1/(3-2*x)+(2*x+1)*(1-x)/(3*(5-2*x))
g=1-r(3,5)*x;L=r(177,100)*(1-r(7,5)*x)
Vweak=2*(1-4*x*x)/g*(E-2*g*C*x*L)*(3-4*x)/(3-4*x-2*x*x)
V=s.factor(Vweak*(1-x*x+x**4/2))
D=750*(3-x)*(2-x)*(1-x)*(5-2*x)*(3-2*x)*(5-3*x)*(3-4*x-2*x*x)
Q=s.Poly(s.cancel(D*(1-V)/x),x)
assert Q.degree()==15
assert s.cancel(D*(1-V)-x*Q.as_expr())==0
n=15;scale=4**15;certs=[]
for label,sub in [('left',t/4),('right',(1+t)/4)]:
 p=s.Poly(Q.as_expr().subs(x,sub).expand(),t)
 bern=[sum(p.nth(j)*s.binomial(i,j)/s.binomial(n,j) for j in range(i+1)) for i in range(n+1)]
 coeff=[s.Integer(scale*b*s.binomial(n,i)) for i,b in enumerate(bern)]
 assert all(scale*b*s.binomial(n,i)==coeff[i] for i,b in enumerate(bern))
 shifted=[int(coeff[i]-s.binomial(n,i)) for i in range(n+1)]
 assert all(c>0 for c in shifted)
 rhs=sum(s.Integer(c)*t**i*(1-t)**(n-i) for i,c in enumerate(shifted))
 assert s.expand(scale*p.as_expr()-1-rhs)==0
 certs.append({'label':label,'substitution':str(sub),'scale':scale,'degree':n,'shifted_positive_coefficients':shifted,'all_coefficients_strictly_positive':True})
p=s.Poly(Q.as_expr().subs(x,t/2).expand(),t)
whole=[sum(p.nth(j)*s.binomial(i,j)/s.binomial(n,j) for j in range(i+1)) for i in range(n+1)]
weak=[]
for z in [r(1,20),r(1,10),r(1,5),r(3,10)]:
 val=s.factor((1-Vweak).subs(x,z));assert val<0;weak.append({'x':str(z),'one_minus_weak_envelope':str(val),'negative':True})
base=Path(__file__).resolve().parent
out={'scope':'Exact rational identities and positive Bernstein coefficients ONLY. Analytic Gamma/kernel envelope and SPDE consequence need proof/review.','Q_descending_coefficients':[int(c) for c in Q.all_coeffs()],'Q_expression':str(Q.as_expr()),'D_expression':str(D),'V_expression':str(V),'identity':'D(x)*(1-V(x))=x*Q(x)','certificates':certs,'failed_whole_interval_certificate':{'nonpositive_coefficients':[{'index':i,'value':str(c)} for i,c in enumerate(whole) if c<=0],'scope':'Negative Bernstein coefficient refuses this certificate, not polynomial positivity.'},'failed_weak_envelope':weak}
(base/'certificates-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact degree15 rational identity and two16term positive certificates PASS; weak-envelope failures retained.')
