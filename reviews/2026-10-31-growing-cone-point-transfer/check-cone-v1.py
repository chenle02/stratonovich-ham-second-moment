"""Deterministic/source/observable diagnostics; no stochastic operator estimate."""
import json
import mpmath as mp

def eta(r):
    r=abs(r)
    if r<=1:return mp.mpf(1)
    if r>=2:return mp.mpf(0)
    aa=mp.exp(-1/(2-r));bb=mp.exp(-1/(r-1))
    return aa/(aa+bb)
def eta_prime(r):
    if r<=1 or r>=2:return mp.mpf(0)
    aa=mp.exp(-1/(2-r));bb=mp.exp(-1/(r-1))
    return -aa*bb*((2-r)**(-2)+(r-1)**(-2))/(aa+bb)**2

def base(d,prec):
    with mp.workdps(prec):
        area=[None,2,2*mp.pi,4*mp.pi][d]
        mass=area*mp.quad(lambda r:eta(r)**2*r**(d-1),[0,1,mp.mpf('1.5'),2])
        grad=area*mp.quad(lambda r:eta_prime(r)**2*r**(d-1),[1,mp.mpf('1.5'),2])
        return mass,grad
scale=[];basevals={}
for d in [1,2,3]:
    aa,bb=base(d,30);a,b=base(d,50)
    assert abs(aa-a)/max(1,a)<mp.mpf('1e-20') and abs(bb-b)/max(1,b)<mp.mpf('1e-20')
    basevals[d]=(a,b)
    for R in [1,2,5]:
        with mp.workdps(50):
            area=[None,2,2*mp.pi,4*mp.pi][d]
            actual=area*(mp.quad(lambda r:eta(r/R)**2*r**(d-1),[0,R,mp.mpf('1.5')*R,2*R])+
                         mp.quad(lambda r:(eta_prime(r/R)/R)**2*r**(d-1),[R,mp.mpf('1.5')*R,2*R]))
            scaling=R**d*a+mp.mpf(R)**(d-2)*b
            upper=R**d*(a+b)
            assert abs(actual-scaling)<mp.mpf('1e-36')*max(1,scaling)
            assert actual<=upper+mp.mpf('1e-36')*max(1,upper)
            scale.append({'d':d,'R':R,'direct_H1_norm_squared':mp.nstr(actual,25),
                          'scaling_formula':mp.nstr(scaling,25),'upper_Ceta_Rd':mp.nstr(upper,25)})
free=[]
for L in [4,8,16,32]:
    with mp.workdps(50):
        R=L+2
        def sol(x,rr):return (eta((x+L)/rr)+eta((x-L)/rr))/2
        good=mp.quad(lambda x:sol(x,R)**2,[-1,0,1])/2
        bad=mp.quad(lambda x:sol(x,1)**2,[-1,0,1])/2
        assert good==1 and bad==0
        free.append({'L':L,'good_R':R,'source_point_square':'1',
                     'good_spatial_square_average':mp.nstr(good,8),
                     'bad_fixed_R1_square_average':mp.nstr(bad,8)})
pulse={}
with mp.workdps(50):
    bump=lambda z:mp.exp(-1/(1-z*z)) if abs(z)<1 else mp.mpf(0)
    Z=mp.quad(bump,[-1,0,1]);aa=lambda s:4*bump(4*(s-mp.mpf('.5')))/Z;bb=lambda y:4*bump(4*(y-3))/Z
    actual=mp.quad(lambda s:aa(s)*mp.quad(lambda y:bb(y)/2 if abs(y)<=6-s else 0,[mp.mpf('2.75'),3,mp.mpf('3.25')]),[mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75')])
    masked=mp.quad(lambda s:aa(s)*mp.quad(lambda y:eta(y)**2*bb(y)/2 if abs(y)<=6-s else 0,[mp.mpf('2.75'),3,mp.mpf('3.25')]),[mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75')])
    assert abs(actual-mp.mpf('.5'))<mp.mpf('1e-40') and masked==0
    pulse={'L':6,'time_support':['.25','.75'],'space_support':['2.75','3.25'],
           'full_first_Picard':mp.nstr(actual,25),'fixed_mask_R1_first_Picard':mp.nstr(masked,10),
           'scope':'smooth nonnegative deterministic potential; higher full terms nonnegative, no CM/noise-law assertion'}
heat=[];observable=[];pref=[]
with mp.workdps(50):
    for eps in [mp.mpf('.5'),mp.mpf(1),mp.mpf(2)]:
        post=mp.exp(-9/(2*eps))/mp.sqrt(2*mp.pi*eps)
        assert post>0
        heat.append({'epsilon':str(eps),'point_mass_location':'3','x':'0','R':1,
                     'mask_after_heat':mp.nstr(post,25),'heat_after_mask':'0',
                     'scope':'deterministic point-mass convolution guard, not a raw Gaussian sample'})
    for k in [mp.pi/2,mp.pi,2*mp.pi]:
        c=mp.quad(lambda x:mp.cos(k*x),[-1,0,1])/2
        s=mp.quad(lambda x:mp.sin(k*x),[-1,0,1])/2
        varavg=c*c+s*s;formula=(mp.sin(k)/k)**2
        assert abs(varavg-formula)<mp.mpf('1e-40')
        observable.append({'k_over_pi':mp.nstr(k/mp.pi,6),'point_variance':'1',
                           'expected_spatial_average_of_squares':'1',
                           'variance_of_spatial_average':mp.nstr(varavg,25),
                           'scope':'stationary Gaussian harmonic toy; covariance not original H:homog class'})
    for d in [1,2,3]:
        a,b=basevals[d];vol=[None,2,mp.pi,4*mp.pi/3][d]
        for delta in [mp.mpf('.25'),mp.mpf('.125'),mp.mpf('.0625'),mp.mpf('.01')]:
            R=1/delta+2
            pref.append({'d':d,'delta':str(delta),'R_delta':str(R),
                         'delta_log_data_upper_prefactor':mp.nstr(delta*mp.log((a+b)*R**d/vol),25),
                         'scope':'H1 upper budget only, not H1/2 exact norm or operator moment'})
print(json.dumps({'scope':'9direct radial H1 scaling checks (base30/50digits),4actual d1free-source cone cases,1smooth-pulse evaluator,3heat-order and3Gaussian-observable toy guards,12prefactor rows; no certified enclosure/CM/stochastic operator proof',
                  'data_scaling_rows':scale,'free_cone_rows':free,'outside_mask_pulse':pulse,
                  'heat_order_rows':heat,'observable_rows':observable,'data_prefactor_rows':pref},indent=2))
