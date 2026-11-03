from fractions import Fraction as F
from math import sqrt,ceil,log
import json
from pathlib import Path
O=Path(__file__).parent
n=16
actual=n*(n+2);false_input=9*n;retained=9*(n*n+n)//2;maximum=9*n*n
assert (actual,false_input,retained,maximum)==(288,144,1224,2304)
assert false_input<actual<=retained<=maximum
# A<=B does not imply A²<=B²: A=diag(1,0), B=A+ones.
A=[[1,0],[0,0]];B=[[2,1],[1,1]];diffpowers=[[4,3],[3,2]]
assert diffpowers[0][0]*diffpowers[1][1]-diffpowers[0][1]**2==-1
v=[F(1),F(-3,2)];quadratic=sum(v[i]*diffpowers[i][j]*v[j] for i in range(2) for j in range(2));assert quadratic==F(-1,2)
# Explicit gamma/theta/beta/eta/q0 for an original singular-line-admissible parameter tuple.
a=F(1,5);alpha=F(5,4);d=2;gamma=F(1,4);theta=F(5,8);eta=F(11,16);beta=F(3,4);q0=18
assert gamma<min(F(1,2),(2-alpha)/2)
assert F(1,2)<theta<eta<beta<min(1-a/2,(3-a-alpha)/2)
rho0=beta-eta-F(1,q0);assert rho0==F(1,144)>0 and q0*gamma>d
assert beta-eta-F(1,16)==0 # endpoint q=16 would destroy temporal denominator
indices=[]
for p in [F(1),F(3,2),F(7),F(18),F(101,5),F(1000)]:
 q=max(q0,2*ceil(p/2));assert q>=p and q<=p+q0+2 and q<=(q0+3)*p
 indices.append({'p':str(p),'q':q})
# Fixed common compact envelope diagonal j^-2: exact finite Gaussian S4 tail
# is3 sum j^-4, retained Gaussian upper9 sum j^-4<=3/N³ uniformly in M.
tails=[]
for N in [1,4,16]:
 M=128;trace=sum((F(1,j**4) for j in range(N+1,M+1)),F(0))
 actualtail=3*trace;retainedtail=9*trace;uniform=F(3,N**3)
 assert actualtail<=retainedtail<=uniform
 tails.append({'N':N,'M':M,'operator_envelope_tail_norm':float(F(1,(N+1)**2)),'actual_L4S4_fourth':float(actualtail),'retained_fourth':float(retainedtail),'uniform_in_M_fourth_upper':float(uniform)})
# Correlated contraction xi=(Z/sqrt2,Z/sqrt2); all-ones v produces equal
# second moment2 to independent g1+g2. Offdiagonal covariance cannot be dropped.
correlated={'covariance':[['1/2','1/2'],['1/2','1/2']],'eigenvalues':[0,1],'left_second_moment':2,'standard_comparison_second_moment':2}
# Distinct direct/adjoint gain-one substitutions at s=1/2.
s=F(1,2);r_direct=s-gamma;r_adjoint=s+gamma-1
assert r_direct==F(1,4) and r_adjoint==F(-1,4)
assert 2*s-r_adjoint-1==s-gamma and 2*s-r_adjoint==s+1-gamma
# Full F free columns and compact potential plateau first responses, lambda2,t1.
lam=F(2);t=F(1)
response={'constant_displacement_position_first':str(lam*t*t/2),'constant_displacement_velocity_first':str(lam*t),'constant_velocity_position_free':str(t),'constant_velocity_position_first':str(lam*t**3/6),'constant_velocity_velocity_first':str(lam*t*t/2)}
assert response['constant_velocity_position_first']=='1/3'
# Holder of fixed n products:1/2=n/(4n)+1/4.
for factors in [1,2,5,17]:assert F(factors,4*factors)+F(1,4)==F(1,2)
# Raw probability exponent includes g_delta ONCE.
ar=F(1,2);pr=6;gamma_pr=pr*(1-ar)/2-1;wrong=pr*(1-ar)-1
assert gamma_pr==F(1,2) and wrong==2
# Averaging squares cannot be replaced by squaring the average.
avgsquares=F(1,2)*1+F(1,2)*1;squareavg=(F(1,2)*1+F(1,2)*(-1))**2
assert avgsquares==1 and squareavg==0
# Point-data prefactor has delta log cost->0 (C_eta/vd normalized to1 for diagnostic).
prefactors=[]
for k in [4,8,16,32]:
 delta=2.0**(-k);cost=delta*d*log(1/delta+2);prefactors.append({'delta':delta,'normalized_log_data_cost':cost})
assert all(prefactors[i+1]['normalized_log_data_cost']<prefactors[i]['normalized_log_data_cost'] for i in range(3))
report={'scope':'Author finite algebra/negative controls only, not analytic proof or independent review','all_checks_passed':True,'n16_two_variances':{'actual':actual,'false_input_only':false_input,'retained_average':retained,'maximum':maximum},'operator_power_order_counterexample':{'A':A,'B':B,'B_minus_A':'all-ones positive rankone','B2_minus_A2':diffpowers,'determinant':-1,'vector':list(map(str,v)),'quadratic':str(quadratic)},'strict_path_parameters':{'alpha':str(alpha),'a':str(a),'d':d,'gamma':str(gamma),'theta':str(theta),'eta':str(eta),'beta':str(beta),'q0':q0,'rho0':str(rho0),'uniform_denominator':1-2.0**(-float(rho0)),'inadmissible_q16_temporal_gap':0},'per_p_indices':indices,'diagonal_compact_tail_examples':tails,'moving_projection_negative_control':{'operators':'T_N=e_N tensor e_N on l2','strong_limit':0,'operator_norm':1,'trace_power':1,'no_common_positive_compact_envelope':'<B e_N,e_N>>=1 would contradict compactness'},'correlated_source_comparison':correlated,'gain_indices':{'direct':str(r_direct),'adjoint':str(r_adjoint)},'both_constant_columns':response,'zero_start_negative_control':{'path':'F(t)=nonzero fixed rankone P','all_increments':0,'supremum_norm':1,'reason':'zero-start is required for increment-only norm bound'},'raw_max_exponent':{'a':str(ar),'p':pr,'correct':str(gamma_pr),'double_g_delta_wrong':str(wrong)},'average_of_squares':{'average_of_squares':str(avgsquares),'square_of_average':str(squareavg)},'point_data_cost':prefactors}
(O/'finite-check-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'all_checks_passed':True,'n16':report['n16_two_variances'],'temporal_gap':str(rho0),'gain_indices':report['gain_indices']},indent=2))
