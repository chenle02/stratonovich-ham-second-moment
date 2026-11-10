#!/usr/bin/env python3
"""Actual d1 white first-chaos block coupling controls; no operator/event proof."""
from pathlib import Path
import json
import mpmath as mp

def run(dps):
 mp.mp.dps=dps
 a=mp.mpf('.5');delta=mp.mpf('.25');N=4;A=mp.mpf(2)
 def H(s):
  if 0<=s<=1:return (s**(1-a)+(1-s)**(1-a))/(1-a)
  return (s**(1-a)-(s-1)**(1-a))/(1-a)
 def K(h):
  if h==0:
   return mp.quad(lambda x:(1-x*x)**2,[0,1])  # r=x² removes RAW singularity
  def f(x):
   if x==0:return mp.mpf(0)
   return x**5/2*(1/mp.sqrt(h+1-x*x)+1/mp.sqrt(h-1+x*x))
  return mp.quad(f,[0,1])  # r=1-x², actual .25*(1-r)² two triangles
 assert abs(K(0)-1/((1-a)*(2-a)*(3-a)))<mp.mpf(10)**(-dps+8)
 C=mp.matrix([[delta**(1-a)*K(abs(i-j)) for j in range(N)] for i in range(N)])
 m=[];raw=[]
 for j in range(N):
  s=j*delta
  fast=mp.sqrt(delta)*mp.quad(lambda u:(1-u)*H(s+delta*u),[0,mp.mpf('.5'),1])
  slow=delta**(-mp.mpf('.5'))*mp.quad(lambda t:(1-(t-s)/delta)*H(t),[s,s+delta/2,s+delta])
  assert abs(fast-slow)<mp.mpf(10)**(-dps+8)
  m.append(fast);raw.append(slow)
 v=2*A*2/((1-a)*(2-a));Sigma=mp.matrix(N+1)
 for i in range(N):
  for j in range(N):Sigma[i,j]=C[i,j]
  Sigma[i,N]=Sigma[N,i]=m[i]
 Sigma[N,N]=v
 eigmin=min(mp.eigsy(Sigma,eigvals_only=True));assert eigmin>0
 b=mp.matrix([mp.mpf('.1'),mp.mpf('.2'),mp.mpf('.3'),mp.mpf('.4')]);r=1/mp.sqrt(delta)
 mean_shift=sum(b[i]*m[i] for i in range(N))
 lhs=(b.T*C*b)[0]/2
 joint=mp.matrix([b[i] for i in range(N)]+[-r])
 rhs=-r*r*v/2+r*mean_shift+(joint.T*Sigma*joint)[0]/2
 assert abs(rhs-lhs)<mp.mpf(10)**(-dps+8)
 wrong_independent_log=lhs+r*mean_shift
 wrong_jacobian_log=lhs+r*(delta-1)*mean_shift
 diagonal_cell_cost=delta**(1-a)*v
 wrong_cost_log=lhs+r*r*(v-diagonal_cell_cost)/2
 assert abs(wrong_independent_log-lhs)>mp.mpf('.1')
 assert abs(wrong_jacobian_log-lhs)>mp.mpf('.1')
 assert wrong_cost_log-lhs>1
 return {'working_digits':dps,'Cxx':[[mp.nstr(C[i,j],26) for j in range(N)] for i in range(N)],'Cov_XZ':[mp.nstr(x,26) for x in m],
  'Cov_XZ_slow_test':[mp.nstr(x,26) for x in raw],'Var_Z':mp.nstr(v,26),'joint_PSD_min_eigenvalue':mp.nstr(eigmin,26),
  'MGF_log_lhs':mp.nstr(lhs,26),'MGF_log_correct_rhs':mp.nstr(rhs,26),
  'wrong_independent_Z_log_rhs':mp.nstr(wrong_independent_log,26),'wrong_missing_Jacobian_log_rhs':mp.nstr(wrong_jacobian_log,26),
  'wrong_diagonal_only_cost':mp.nstr(diagonal_cell_cost,26),'wrong_cost_log_rhs':mp.nstr(wrong_cost_log,26)}
lo=run(40);hi=run(65)
for k in ['Var_Z','joint_PSD_min_eigenvalue','MGF_log_lhs','MGF_log_correct_rhs']:
 assert abs(mp.mpf(lo[k])-mp.mpf(hi[k]))<mp.mpf('1e-24')
out={'scope':'Actual original d1 Gamma=delta0,alpha1,a=.5, RAW first-chaos point-wave kernels and Gaussian completion tests. Numerical covariance/MGF consistency, not certified quadrature/operator/Young/cone/event proof.',
 'definitions':'delta=1/4; sm=m delta; k_m(s,y)=delta^(-1/2) 1_[sm,sm+delta](s) G1(1-(s-sm)/delta,y), G1(r,y)=.5*1_|y|<=r; X_m=W(k_m). Z=W(1_[0,1](s)*1_[-2,2](y)). One SAME W/Z, not independent time blocks.',
 'completion_boundary':'Indicators and point-first-response kernels are raw H-completion tests in this admissible d1 model; NOT literal Cc-infinity Psi or a bounded point functional on F. CC-smooth positive test/averaging approximations converge at first chaos. No target low-Sobolev point trace is inferred.',
 'covariance_formula':'Cij=delta^(1-a)/4 int_0^1 (1-r)^2[(|i-j|+r)^(-a)+abs(|i-j|-r)^(-a)]dr; CovXmZ=sqrt(delta)int_0^1(1-u)H(sm+delta*u)du; H(s)=int_0^1|s-t|^-a dt; VarZ=4*2/((1-a)(2-a)).',
 'source_calibration':'K0 integrator after actual r=x² substitution agrees with closed1/((1-a)(2-a)(3-a)); the evaluator is exercised, not a separately hardcoded return.',
 'gaussian_test':'F(X)=exp(sum b_i X_i), b=(.1,.2,.3,.4). E F(X)=exp(-r²v/2) E[exp(-rZ)F(X+r Cov(X,Z))], r=delta^-1/2. Compare LOG values; wrong independence, missing Jacobian and diagonal-only cost all differ.',
 'mask':'Any actual mask=1 on[-2,2] leaves the displayed first-chaos kernels and Z unchanged; no masked covariance cost substituted.',
 'precision_scope':'40/65-working-digit printed agreement, NOT rigorous error/eigenvalue/accuracy certification. PSD follows from the actual test covariance construction; its numerical eigenvalue is only a consistency check.',
 'runs':[lo,hi]}
Path(__file__).with_name('coupled-blocks-v0.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual four coupled RAW d1 blocks: Jacobian/PSD/Gaussian same-Z MGF; three wrong models rejected,40/65digit consistency only.')
