"""Actual covariance/temporal diagnostics; floating consistency, NOT certified error.
Run with uv --with numpy --with mpmath. No SPDE/ground eigenvalue calculation.
"""
import argparse
import json
from pathlib import Path
import numpy as np
import mpmath as mp


def chi(x):
    x = np.asarray(x, dtype=float)
    out = np.ones_like(x)
    out[x >= 2] = 0
    middle = (x > 1) & (x < 2)
    z = x[middle]
    left, right = np.exp(-1 / (2-z)), np.exp(-1 / (z-1))
    out[middle] = left / (left + right)
    return out


def fn(t, a, n):
    t = np.asarray(t, dtype=float)
    result = np.zeros_like(t)
    interior = (t > 0) & (t < 1)
    x = t[interior]
    r = (1-a)/2
    denom = float(mp.gamma(r)*mp.gamma(1-r))
    result[interior] = (x*(1-x))**(-r)/denom * chi(1/(n*x))*chi(1/(n*(1-x)))
    return result


def temporal(a, n, degree):
    v, w = np.polynomial.legendre.leggauss(degree)
    v, w = (v+1)/2, w/2
    p = 1/(1-a)
    s = v[:, None]
    # t=s-u^(1/(1-a)), u=s^(1-a)*v: exact removal of |s-t|^-a.
    inner = fn(s*(1-v[None, :]**p), a, n) @ w
    variance = 2/(1-a)*np.dot(w, fn(v,a,n)*v**(1-a)*inner)
    values = []
    for point in [0, .25, .5, .75, 1]:
        left = 0 if point == 0 else point**(1-a)/(1-a)*np.dot(w,fn(point*(1-v**p),a,n))
        right = 0 if point == 1 else (1-point)**(1-a)/(1-a)*np.dot(w,fn(point+(1-point)*v**p,a,n))
        values.append(float(left+right))
    return {'a':a,'n':n,'degree':degree,'mass':float(np.dot(w,fn(v,a,n))),
            'raw_temporal_variance':float(variance),'k_fn_grid':values,
            'M_a':float(mp.gamma((1+a)/2)/(mp.gamma(1+a)*mp.gamma((1-a)/2)))}


def compact_bump(degree):
    x,w = np.polynomial.legendre.leggauss(degree)
    f = np.exp(-1/(1-x*x))
    df = -2*x/(1-x*x)**2*f
    norm2 = float(np.dot(w,f*f))
    return {'degree':degree,'b':float(np.dot(w,df*df))/norm2,
            'A_white':float(np.dot(w,f**4))/(norm2**2)}


def scalar_models(digits, bump):
    mp.mp.dps=digits
    cases=[('white-d1',1,'1','.5','white'),('invariant-d2',2,'1','.5','invariant'),
           ('riesz-d2-alpha1.5',2,'1.5','.25','riesz'),('riesz-d3-alpha1.5',3,'1.5','.25','riesz'),
           ('compact-white-d1',1,'1','.5','compact'),('compact-invariant-d2',2,'1','.5','compact')]
    rows=[]
    for name,d,alpha,a,kind in cases:
        alpha,a=mp.mpf(alpha),mp.mpf(a);q=4-alpha;k=3-alpha; sigma=mp.mpf('1.2')
        if kind in ['white','invariant']:
            A=1/(mp.sqrt(2*mp.pi)*sigma); b=d/(2*sigma**2)
        elif kind=='riesz':
            A=(2*sigma**2)**(-alpha/2)*mp.gamma((d-alpha)/2)/mp.gamma(mp.mpf(d)/2)
            b=d/(2*sigma**2)
        else:
            A=mp.mpf(str(bump['A_white']));b=d*mp.mpf(str(bump['b']))
        R=A/b**(alpha/2);M=mp.gamma((1+a)/2)/(mp.gamma(1+a)*mp.gamma((1-a)/2))
        u=alpha/q;C=M/(2*R)*(1+u)**2/u**(alpha/2)
        L=(1/(q*C))**(1/k);ell=mp.sqrt(u*L**2/b);theta=(1+u)*L**2/(ell**alpha*A)
        radicand=theta*ell**alpha*A-ell**2*b
        cost=M*theta**2*ell**alpha*A
        payoff=mp.sqrt(radicand)-cost/2
        target=k*((R/M)*alpha**(alpha/2)/(8*q**(q/2)))**(1/k)
        scale=(alpha*A/b)**(1/(2-alpha))
        energy=scale**alpha*A-scale**2*b/2
        energy_target=(2-alpha)/2*alpha**(alpha/(2-alpha))*R**(2/(2-alpha))
        assert 0<a<1 and 0<alpha and alpha+a<2
        assert abs(radicand/L**2-1)<mp.mpf(10)**(-digits+12)
        assert abs(payoff/target-1)<mp.mpf(10)**(-digits+12)
        assert abs(energy/energy_target-1)<mp.mpf(10)**(-digits+12)
        # Distinct actual scaling laws; omission of Gaussian-test amplitude is detected.
        dilation=mp.mpf(2)
        negative={'wrong_occupation_vs_test_cost_ratio':str(dilation**(4-2*alpha)),
                  'wrong_half_kinetic_energy_ratio':str(2**(-alpha/(2-alpha))),
                  'wrong_fractional_brownian_cost_ratio':str((1-a/2)*(1-a))}
        assert all(abs(mp.mpf(x)-1)>mp.mpf('.01') for x in negative.values())
        rows.append({'name':name,'d':d,'alpha':str(alpha),'a':str(a),'kind':kind,
                     'A_sp':str(A),'b':str(b),'R':str(R),'optimal_lower':str(payoff),
                     'target_lower':str(target),'spatial_energy':str(energy),
                     'relative_opt_error':str(abs(payoff/target-1)),
                     'negative_controls':negative})
    # Actual H1 Gaussian profiles: covariance norm of squares vs H1 distance.
    continuity=[]
    for d,alpha,kind in [(1,mp.mpf(1),'white'),(2,mp.mpf(1),'invariant'),(2,mp.mpf('1.5'),'riesz')]:
        for eps in ['.1','.01','.001']:
            s,t=mp.mpf(1),1+mp.mpf(eps)
            const=1/mp.sqrt(2*mp.pi) if kind!='riesz' else 2**(-alpha/2)*mp.gamma((d-alpha)/2)/mp.gamma(mp.mpf(d)/2)
            As,At=const*s**(-alpha),const*t**(-alpha)
            cross=const*((s*s+t*t)/2)**(-alpha/2)
            overlap=(2*s*t/(s*s+t*t))**(mp.mpf(d)/2)
            h1square=2-2*overlap+d/(2*s*s)+d/(2*t*t)-2*d/(s*s+t*t)*overlap
            covsquare=As+At-2*cross
            assert covsquare>=0 and cross**2<=As*At*(1+mp.mpf(10)**(-digits+10))
            continuity.append({'d':d,'alpha':str(alpha),'eps':eps,'covariance_norm_square':str(covsquare),'H1_distance_square':str(h1square)})
    return {'digits':digits,'models':rows,'continuity':continuity}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    mp.mp.dps=50
    bumps=[compact_bump(n) for n in [256,512]]
    temporal_rows=[temporal(a,n,degree) for a in [.5,.25] for n in [4,8,16] for degree in [256,512]]
    for a in [.5,.25]:
        rows=[r for r in temporal_rows if r['a']==a and r['degree']==512]
        assert all(0<r['mass']<r['M_a'] and 0<r['raw_temporal_variance']<r['M_a'] for r in rows)
        assert all(all(0<x<1.00001 for x in r['k_fn_grid']) for r in rows)
        assert all(rows[j]['mass']<rows[j+1]['mass'] and rows[j]['raw_temporal_variance']<rows[j+1]['raw_temporal_variance'] for j in [0,1])
    s50,s80=scalar_models(50,bumps[-1]),scalar_models(80,bumps[-1])
    for x,y in zip(s50['models'],s80['models']):
        assert abs(mp.mpf(x['optimal_lower'])/mp.mpf(y['optimal_lower'])-1)<mp.mpf('1e-38')
    result={'status':'CONSISTENCY CONTROLS ONLY, not certified error or theorem',
            'numpy_version':np.__version__,'mpmath_version':mp.__version__,
            'temporal':temporal_rows,'compact_bump':bumps,'scalar_50':s50,'scalar_80':s80,
            'scope':'Two quadrature degrees and two working precisions; no rigorous error enclosure, exact spectral calculation, full H1 density/continuity proof or actual solution moment computed. Gaussian spatial profiles are H1 but NOT compact; compact white/invariant product bumps separately tested.'}
    Path(args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'temporal_cases':len(temporal_rows),'spatial_models':len(s80['models']),'continuity_controls':len(s80['continuity'])}))

if __name__=='__main__':main()
