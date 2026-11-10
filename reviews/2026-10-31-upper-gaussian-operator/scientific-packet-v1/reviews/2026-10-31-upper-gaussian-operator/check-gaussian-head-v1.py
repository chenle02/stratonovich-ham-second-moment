"""Finite Gaussian density and tail diagnostics, not CM/operator/SPDE proof."""
from fractions import Fraction as F
import json
import mpmath as mp

def log_tail(J,delta,c,nu,M,prec):
    with mp.workdps(prec):
        delta=mp.mpf(delta);c=mp.mpf(c);nu=mp.mpf(nu);M=mp.mpf(M)
        assert J>=1 and delta>0 and M>0
        decay=M-c*nu*M**(nu-1)
        assert decay>0
        anchor=c*M**nu-M*M/2
        step=delta/decay
        def integrand(u):
            rr=M+step*u
            diff=c*(rr**nu-M**nu)-(rr*rr-M*M)/2
            return rr**(J-1)*mp.exp(diff/delta)
        integral=mp.quad(integrand,[0,1,4,16,mp.inf])
        lognorm=(1-mp.mpf(J)/2)*mp.log(2)-mp.loggamma(mp.mpf(J)/2)-mp.mpf(J)/2*mp.log(delta)
        answer=lognorm+anchor/delta+mp.log(step)+mp.log(integral)
        calibration=None
        if c==0:
            calibration=mp.log(mp.gammainc(mp.mpf(J)/2,M*M/(2*delta),mp.inf)/mp.gamma(mp.mpf(J)/2))
            assert abs(answer-calibration)<mp.mpf(10)**(-prec+10)*max(1,abs(calibration))
            if J==2:assert abs(answer+M*M/(2*delta))<mp.mpf(10)**(-prec+10)
        bound=J*mp.log(2)-M*M/(8*delta)
        assert 4*c<=M**(2-nu) and answer<=bound
        return answer,bound,calibration
rows=[]
for J in [1,2,4]:
    for delta in ['1','0.25']:
        for c,M in [('0','1'),('1','16'),('1','32')]:
            a,_,_=log_tail(J,delta,c,'1.5',M,40)
            b,bd,cal=log_tail(J,delta,c,'1.5',M,70)
            with mp.workdps(80):difference=abs(a-b)/max(1,abs(b))
            assert difference<mp.mpf('1e-25')
            rows.append({'J':J,'delta':delta,'C':c,'nu':'1.5','M':M,
                         'log_tail':mp.nstr(b,28),'log_majorant':mp.nstr(bd,28),
                         'precision_relative_difference':mp.nstr(difference,8),
                         'C0_chi_square_calibration':None if cal is None else mp.nstr(cal,28)})
normalizers=[]
for J in [1,2,4,8]:
    vals=[]
    for prec in [40,70]:
        with mp.workdps(prec):
            cJ=2**(1-mp.mpf(J)/2)/mp.gamma(mp.mpf(J)/2)
            val=cJ*mp.quad(lambda r:r**(J-1)*mp.exp(-r*r/8),[0,1,4,16,mp.inf])
            assert abs(val-2**J)<mp.mpf(10)**(-prec+10)*2**J
            vals.append(val)
    normalizers.append({'J':J,'computed_residual_gaussian_normalizer':mp.nstr(vals[1],26),
                        'exact_2_power_J':2**J})
cost=[]
for b in [F(1,2),F(1),F(2)]:
    expected=2*b*b
    for gamma in [F(1,2),F(1),F(1,4)]:
        phi=b/gamma;score=2*b*phi-gamma*phi*phi
        assert score==b*b/gamma
        cost.append({'b':str(b),'quadratic_action_coefficient':str(gamma),
                     'stationary_phi':str(phi),'score':str(score),
                     'equals_variance_delta_gaussian_log_MGF_rate':score==expected})
# nu=3/2 gives cutoff M>=16*C^2. Removing it fails at C=1,M=x=1.
C=M=x=F(1)
assert C*x-x*x/F(2)>-M*M/F(8)-x*x/F(8)
wrongcut={'C':'1','M':'1','x':'1','nu':'1.5','lhs':'1/2','rhs':'-1/4',
          'scope':'x^nu=1 exact; missing cutoff refuted'}
threshold=[]
# nu5/3 => 3nu/(2-nu)=15. C1=1,M0=512 gives cutoff ratio2*B^((m-15)/3).
for m in [18,12]:
    ex=(m-15)//3
    assert F(m,3)-5==ex
    for B in [2,4,8,16]:
        M0_root=8
        ratio=F(M0_root,4)*(F(B**ex) if ex>=0 else F(1,B**(-ex)))
        threshold.append({'m':m,'B':B,'M0':M0_root**3,'C1':1,'nu':'5/3','cutoff_ratio_M_to_2_minus_nu_over_4C1B3nu':str(ratio),
                          'eventual_direction':'grows' if ex>0 else 'decreases'})
entropy=[{'n':n,'delta':str(F(1,n)),'J':n,
          'delta_times_J':'1','normalized_log_2_power_J':'log2, does not vanish'} for n in [2,4,8,16]]
print(json.dumps({'scope':'18 finite radial tails40/70digits with6chi calibrations,4residual Gaussian integral normalizers,9exact cost rows; no certified enclosure/CM/operator/SPDE claim',
 'radial_tail_rows':rows,'residual_normalizer_rows':normalizers,'half_action_rows_exact':cost,
 'wrong_cutoff_exact':wrongcut,'polynomial_threshold_rows_exact':threshold,
 'rank_entropy_guard_exact':entropy,
 'positive_action_guard':'exp(+u^2/(2delta)) is not a normalized Gaussian density; divergence analytic, not integrated',
 'empty_head_guard':'J0 tail0 and bulk prefactor1 by convention; no radial integral used'},indent=2))
