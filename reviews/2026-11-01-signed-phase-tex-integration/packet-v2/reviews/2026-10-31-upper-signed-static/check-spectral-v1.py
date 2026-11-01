"""Finite full scalar spectral-matrix diagnostics, not a wave/SPDE theorem."""
import json
from fractions import Fraction as F
import mpmath as mp

def norm2(a,b,c,d):
    ss=a*a+b*b+c*c+d*d
    det=a*d-b*c
    return mp.sqrt((ss+mp.sqrt(max(mp.mpf(0),ss*ss-4*det*det)))/2)
def one(K,h,t,dps):
    with mp.workdps(dps):
        h=mp.mpf(h);t=mp.mpf(t);cc=2+K*K
        lam=mp.sqrt(max(0,-h))
        if h>0: co=mp.cos(t*mp.sqrt(h));si=mp.sin(t*mp.sqrt(h))/mp.sqrt(h)
        elif h<0: co=mp.cosh(t*mp.sqrt(-h));si=mp.sinh(t*mp.sqrt(-h))/mp.sqrt(-h)
        else:co=mp.mpf(1);si=t
        fac=mp.exp(-lam*t)
        a=d=fac*co;b=fac*mp.sqrt(h+cc)*si;c=-fac*h*si/mp.sqrt(h+cc)
        n=norm2(a,b,c,d)
        if t==0:assert n==1
        if h==0:
            jordan=(mp.sqrt(b*b+4)+abs(b))/2
            assert abs(n-jordan)<=mp.mpf(10)**(-dps+8)*max(1,jordan)
        envelope=8*(1+K)*(1+t)
        assert n<=envelope
        return n,envelope,abs(co*co+h*si*si-1)
rows=[]
for K in [2,8]:
    for h in ['-4','-0.25','0','0.25','4','64']:
        for t in ['0','0.25','1','4','16']:
            n40,_,_=one(K,h,t,40);n70,b,det=one(K,h,t,70)
            with mp.workdps(80):err=abs(n40-n70)/max(1,n70)
            assert err<mp.mpf('1e-25')
            rows.append({'K':K,'h':h,'t':t,'normalized_full_norm2':mp.nstr(n70,26),
                         'matrix_envelope':mp.nstr(b,12),'precision_relative_difference':mp.nstr(err,8),
                         'determinant_identity_residual':mp.nstr(det,8)})
root=[]
for n in [2,4,16,256]:
    eps=F(1,n*n);lam=F(1,n)
    assert lam*lam==eps and lam/eps==n
    root.append({'n':n,'epsilon':str(eps),'lambda':str(lam),'lambda_over_epsilon':str(lam/eps)})
form=[]
for K in [1,2,8]:
    c=2+K*K
    for z in [F(1),F(K+2),F(K+3),F(100)]:
        grad2=z*z-1
        qlow=grad2-K*z
        low=qlow+c
        upper=grad2+K*z+c
        assert F(1,2)*z*z<=low and low>=1
        assert upper<=3*(1+K*K)*z*z
        if z>K+2:assert qlow>1
        form.append({'K':K,'H1_norm':str(z),'shifted_lower':str(low),
                     'shifted_upper':str(upper),'guards':'PASS'})
print(json.dumps({'scope':'60 finite scalar spectral fibers at40/70digits; full induced Euclidean matrix norm, no certified enclosure/actual multiplier/CM/eigenstate/SPDE computation',
                  'spectral_rows':rows,'sqrt_lipschitz_guard_exact':root,'form_budget_rows_exact':form,
                  'free_velocity_guard':'tau(t)=(1,t;0,1), norm>=sqrt(1+t^2) by velocity input; excludes a time-uniform pure exponential at lambda0 analytically',
                  'averaging_guard':'1_Q=0 a.e. but equals1 on rational left samples; not a coded integral or actual CM field'},indent=2))
