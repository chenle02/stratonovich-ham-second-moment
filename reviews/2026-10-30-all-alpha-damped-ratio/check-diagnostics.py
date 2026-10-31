#!/usr/bin/env python3
"""Unreviewed scalar tests for a future all-alpha static-control comparison."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=45
def fg(c):
 if c==0:return m.mpf('0.5'),m.mpf('0.125')
 f=-m.expm1(-c/2)/c
 if abs(c)<m.mpf('1e-8'):
  g=sum((-c)**n*m.mpf('0.5')**(n+2)/(m.factorial(n)*(n+2)) for n in range(7))
 else:g=(-m.expm1(-c/2)-(c/2)*m.exp(-c/2))/(c*c)
 return f,g
def values(a,D):
 c=lambda lam:lam+lam*lam/(2*D)
 low=m.quad(lambda x:fg(c(x**(1/a)))[0],[0,m.mpf('0.5'),1])/a
 tail=m.quad(lambda lam:lam**(a-1)*fg(c(lam))[0],[1,2,4,m.inf])
 R=2*(low+tail)/m.gamma(a)
 I1=m.quad(lambda lam:lam**a*fg(c(lam))[1],[0,1,2,4,m.inf])
 I2=m.quad(lambda lam:lam**(a+1)*fg(c(lam))[1],[0,1,2,4,m.inf])
 Eul=2*I1/(m.gamma(a)*R);Eul2=2*I2/(m.gamma(a)*R)
 logRd=Eul2/(2*D*D)
 deltaPrime=-m.log1p(a*a/(D*(D+2*a)))/2
 derivative=logRd+deltaPrime
 lower=a*a/(2*(D+4*a)*(D+2*a))
 assert abs(Eul+Eul2/D-a)<m.mpf('1e-20')
 assert Eul*Eul<=Eul2/2+m.mpf('1e-25')
 assert derivative>=lower-m.mpf('1e-24')
 return R,derivative,lower,Eul,Eul2
rows=[]
for aa in ['0.01','0.1','0.5','0.9','0.99']:
 a=m.mpf(aa)
 for dd in ['0.1','1','2','4']:
  D=m.mpf(dd);R,derivative,lower,E1,E2=values(a,D)
  rows.append({'a':aa,'D':dd,'q':m.nstr(D+2*a,14),'R':m.nstr(R,28),'log_F_q_derivative':m.nstr(derivative,28),'proposed_positive_lower':m.nstr(lower,28),'E_u_lambda':m.nstr(E1,28),'E_u_lambda_squared':m.nstr(E2,28)})
actual=[]
for aa in ['0.1','0.5','0.9']:
 a=m.mpf(aa);M=m.gamma((1+a)/2)/(m.gamma(1+a)*m.gamma((1-a)/2))
 for uu in ['0.25','0.9','0.99']:
  alpha=1+(1-a)*m.mpf(uu);q=4-alpha;D=q-2*a;R,_,_,_,_=values(a,D)
  Delta=(q*m.log(q)+D*m.log(D))/2-(q-a)*m.log(q-a)
  ratio=M*R*m.exp(Delta);gain=ratio**(-1/(q-1))
  actual.append({'a':aa,'alpha':m.nstr(alpha,18),'original_alpha_plus_a':m.nstr(alpha+a,18),'M_R_expDelta':m.nstr(ratio,28),'scalar_gain':m.nstr(gain,28),'scope':'admissible d2/3 parameter range, no moment theorem inferred'})
out={'status':'UNREVIEWED falsification only','working_precision':45,'scope':'20 scalar derivative/moment-identity controls incl outside-model q,9 actual alpha>1 parameter scalar-ratio controls. No extension of accepted d1 moment consumer, source energy identification or certified accuracy. D is scalar q-2a, NOT physicaldimension.','derivative_controls':rows,'alpha_above_one_controls':actual,'all_assertions_passed':True}
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('20 damped-ratio derivative/IBP/CS and9 alpha>1 scalar controls PASS; not a lower-bound theorem.')
