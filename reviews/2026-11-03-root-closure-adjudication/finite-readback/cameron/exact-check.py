from pathlib import Path
from fractions import Fraction as F
from math import floor, gamma, sqrt, pi, sin, cos, log, isfinite
import json

base=Path(__file__).resolve().parent
a=F(1,2);alpha=F(1);s=F(3,8);gamma_sp=F(1,4)
theta=F(5,8);eta_t=F(11,16);beta_t=F(23,32)
r=F(3);p=F(7,4);nu=1/theta;Q=64
assert alpha/4<s<F(1,2)
assert 0<gamma_sp<min(F(1,2),(2-alpha)/2)
assert F(1,2)<theta<eta_t<beta_t<min(1-a/2,(3-a-alpha)/2)
assert 1/(1-theta)<r<2/a and nu<=p<2<r
rows=[]
for d in [1,3]:
    assert ((0<alpha<d) or (alpha==d==1)) and alpha+a<2
    gap=beta_t-eta_t-F(1,Q);anchor=(1-a)/2-F(d,Q)
    assert Q*gamma_sp>d and gap>0 and Q>2*d/(1-a) and anchor>0
    rows.append({'d':d,'model':'white c delta0' if d==1 else 'c dx1 dx2 delta0(dx3)','Q_gamma':str(Q*gamma_sp),'dyadic_gap':str(gap),'anchor_delta_exponent':str(anchor),'radon_ball_exponent':str(F(d)-alpha),'Schur_row_radius_exponent':str(-F(d,2)),'Schur_column_radius_exponent':str(F(d,2)),'Schur_product_radius_exponent':str(-F(d,2)+F(d,2))})

primitive_gap=1-1/r-theta
projection_power=1/p-1/r
base_power=1-nu/p;mean_power=1-nu/r
assert (primitive_gap,projection_power,base_power,mean_power)==(F(1,24),F(5,21),F(3,35),F(7,15))
assert (a/2-1)*2+2-a==0
assert (1-a)/2+a/2==F(1,2)
assert 1+(-1+nu/r)+nu*(3-1/r)==3*nu
assert 1+(-1+nu/p)==nu/p
assert 1+r*(3-1/r)==3*r
assert 2/(1-a*r/2)==8

clocks=[]
for B,delta in [(2,F(1,16)),(2,F(3,40)),(1,F(2,7)),(3,F(1,20))]:
    assert 0<delta<min(F(1),F(1,B))
    N=(1/(delta*B)).numerator//(1/(delta*B)).denominator
    tau=1/delta-N*B;n=N+1
    lengths=[F(B)]*N+[tau]
    starts=[F(m)*delta*B for m in range(n)]
    ends=[x+delta*ell for x,ell in zip(starts,lengths)]
    assert N>=1 and 0<=tau<B and ends[-1]==1
    assert all(ends[m]==starts[m+1] for m in range(N))
    assert sum(delta*ell for ell in lengths)==1 and delta*n<=F(2,B)
    clocks.append({'B':B,'delta':str(delta),'N':N,'n':n,'tau':str(tau),'slow_last_start':str(starts[-1]),'slow_last_end':str(ends[-1]),'empty_last':tau==0,'delta_n':str(delta*n),'two_over_B':str(F(2,B))})

kappa_ball=F(13);s_threshold=F(35)
tail_power=kappa_ball*(2-nu)-3*nu
bad1=r*(3+kappa_ball)-s_threshold*r
bad2=r*(3+kappa_ball)+s_threshold*(nu-r)
assert tail_power==F(2,5) and bad1==-57 and bad2==-1
assert s_threshold>r*(3+kappa_ball)/(r-nu)

free=[]
for B in [1,2,4,8]:
    assert 3+2*B*B<=9*B*B
    G_upper=sqrt(3+2*B*B)
    Cpr=G_upper**2*(B**float(1-1/r)+B**float(1-1/r-theta))
    assert Cpr<=18*B**float(3-1/r)*(1+1e-14)
    free.append({'B':B,'G_Frobenius_upper':G_upper,'three_B':3*B,'C_pr_from_Frobenius_bound':Cpr,'eighteen_B_power_upper':18*B**float(3-1/r)})

Cyoung=1/(1-2**float(1-2*theta))
ctheta=2*max(1,Cyoung)
Cgr=4+log(4)+2*(4*ctheta)**float(nu)
Cs_squared=2**float(2*s)/(1-2**float(-2*(s-alpha/4)))
moment_gauss=[{'dimension':n,'identity_embedding_norm':1,'Gaussian_squared_norm_expectation':n,'Gaussian_norm_expectation':sqrt(2)*gamma((n+1)/2)/gamma(n/2)} for n in [1,4,16,64]]
group_difference=[]
for t in [0.1,0.01,0.001]:
    k=pi/t
    matrix=[[cos(t*k),sqrt(1+k*k)*sin(t*k)/k],[-k*sin(t*k)/sqrt(1+k*k),cos(t*k)]]
    lower=max(abs(matrix[0][0]-1),abs(matrix[1][1]-1))
    assert lower>1.999999
    group_difference.append({'t':t,'frequency_pi_over_t':k,'diagonal_norm_difference_lower':lower})

result={'scope':'Author exact rational budgets and finite diagnostic checks only; no provider review or substitute for analytic proofs.','parameters':{'a':str(a),'alpha':str(alpha),'s':str(s),'beta_sp':str(F(1,2)-s),'gamma':str(gamma_sp),'theta':str(theta),'eta_t':str(eta_t),'beta_t':str(beta_t),'r':str(r),'p':str(p),'nu':str(nu),'Q':Q},'white_and_plane_controls':rows,'primitive_Holder_gap':str(primitive_gap),'projection_weight_power':str(projection_power),'base_power_mean_exponent':str(base_power),'mean_and_last_delta_exponent':str(mean_power),'raw_isometry_delta_exponent':'0','actual_covariance_delta_exponent':'1/2','temporal_c_t_upper':'2','coarse_mean_B_exponent':str(3*nu),'coarse_base_B_exponent':str(nu/p),'bad_cell_B_exponent':str(3*r),'true_clocks':clocks,'outer_free_and_primitive_constants':free,'Young_constants_diagnostic':{'C_Young':Cyoung,'c_theta':ctheta,'C_gr':Cgr,'finite':all(isfinite(x) for x in [Cyoung,ctheta,Cgr])},'C_s_squared_diagnostic':Cs_squared,'control_ball_budget':{'kappa_ball':str(kappa_ball),'threshold_s':str(s_threshold),'tail_growth_exponent':str(tail_power),'bad_first_exponent':str(bad1),'bad_second_exponent':str(bad2)},'finite_Gaussian_embedding_countercontrol':moment_gauss,'E_F_range_countercontrol':{'A_F':[[0,1],[0,0]],'range_in_E':True,'E_restriction_norm':0,'F_norm':1,'constant_column_nonzero':True,'scope':'Finite algebra inference control, not an alternative covariance model.'},'physical_group_not_norm_continuous_diagnostic':group_difference,'uniform_smooth_head_tail_counterexample':'Analytic translated-control proof in worked-replay.md section13 and falsification.md; no numerical decay claim.'}
(base/'exact-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
