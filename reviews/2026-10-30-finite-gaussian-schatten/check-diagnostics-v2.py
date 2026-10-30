#!/usr/bin/env python3
"""Finite Gaussian matrix polynomial controls; not a continuum operator theorem."""
import mpmath as m,json,itertools
from pathlib import Path
m.mp.dps=50
trace=lambda A:sum(A[i,i] for i in range(A.rows))
cases={
 'scalar_complex':[m.matrix([[1]]),m.matrix([[2j]])],
 'noncommuting_hermitian':[m.matrix([[0,1],[1,0]]),m.matrix([[1,0],[0,-1]]),m.matrix([[m.mpf('0.5'),0],[0,m.mpf('0.5')]])],
 'rectangular_complex':[m.matrix([[1,1j],[2,-1],[0,1]]),m.matrix([[0,2],[1j,0],[1,-1j]]),m.matrix([[1,-1],[0,1j],[-2,0]])]
}
rows=[]
for name,As in cases.items():
 n,o=As[0].cols,As[0].rows
 Vout=sum((A*A.H for A in As),m.matrix(o));Vin=sum((A.H*A for A in As),m.matrix(n))
 for power in [1,2,3,4]:
  p=2*power
  # Hermite order power+1 integrates every coordinate degree<=2power exactly in exact arithmetic.
  nodes,weights=m.gauss_quadrature(power+1,'hermite');ev=m.mpf(0)
  for inds in itertools.product(range(power+1),repeat=len(As)):
   X=sum((m.sqrt(2)*nodes[j]*A for j,A in zip(inds,As)),m.matrix(o,n))
   w=m.fprod(weights[j]/m.sqrt(m.pi) for j in inds)
   val=trace((X.H*X)**power);assert abs(m.im(val))<m.mpf('1e-40')
   ev+=w*m.re(val)
  tout=m.re(trace(Vout**power));tin=m.re(trace(Vin**power))
  upper=(p-1)**power*max(tout,tin)
  average_upper=(p-1)**power*(tout+tin)/2
  assert ev<=upper+m.mpf('1e-38') and ev<=average_upper+m.mpf('1e-38')
  if p==2:assert abs(ev-tout)<m.mpf('1e-38') and abs(tin-tout)<m.mpf('1e-38')
  rows.append({'case':name,'input_dimension':n,'output_dimension':o,'Gaussian_count':len(As),'p':p,'expected_trace_XstarX_power':m.nstr(ev,30),'trace_output_variance_power':m.nstr(tout,30),'trace_input_variance_power':m.nstr(tin,30),'proposed_upper_powered':m.nstr(upper,30),'average_upper_powered':m.nstr(average_upper,30),'ratio_of_p_roots':m.nstr((ev/upper)**(m.mpf(1)/p),25),'Hermite_order':power+1})
# Both variance directions are essential in the general finite inequality.
N=16;p=4;true_moment=N*(N+2);dropped_variance_upper=9*N;correct_upper=9*N*N
assert true_moment>dropped_variance_upper and true_moment<=correct_upper
out={'working_precision':50,'scope':'finite Gaussian polynomial matrix controls only; 12 cases by Hermite quadrature and two explicit fourth-moment negative controls, no continuum, actual noise, Schatten-valued series/path or PDE claim. Numeric arithmetic not a formal proof.','rows':rows,'both_variances_negative_controls':[{'shape':'row 1x16, A_k=e_k^T','omitted':'output variance','exact_p4_moment':true_moment,'wrong_input_only_upper':dropped_variance_upper,'correct_max_upper':correct_upper},{'shape':'column 16x1, A_k=e_k','omitted':'input variance','exact_p4_moment':true_moment,'wrong_output_only_upper':dropped_variance_upper,'correct_max_upper':correct_upper}]}
Path(__file__).with_name('diagnostics-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print('12 finite Gaussian Schatten moment controls and both one-variance negative controls PASS.')
