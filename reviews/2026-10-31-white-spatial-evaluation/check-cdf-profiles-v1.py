"""Actual deterministic profile integrals; proposed white bounds, not PDE values."""
import hashlib
import json
from pathlib import Path
import mpmath as mp

P=Path(__file__).resolve().parent


def run(dps):
    with mp.workdps(dps):
        profiles=[]
        specs=[('sech_half','sech',mp.mpf(1)/2,mp.mpf(0)),
               ('sech_shift','sech',mp.mpf(2),mp.mpf(7)/10),
               ('gauss_half','gaussian',mp.mpf(1)/2,mp.mpf(-1)),
               ('gauss_two','gaussian',mp.mpf(2),mp.mpf(0))]
        for name,kind,w,shift in specs:
            if kind=='sech':
                f=lambda x:mp.sqrt(w/2)/mp.cosh(w*(x-shift))
                df=lambda x:-w*mp.tanh(w*(x-shift))*f(x)
                F=lambda x:(1+mp.tanh(w*(x-shift)))/2
                expected_A,expected_b=w/3,w*w/3
            else:
                f=lambda x:(w/mp.pi)**(mp.mpf(1)/4)*mp.exp(-w*(x-shift)**2/2)
                df=lambda x:-w*(x-shift)*f(x)
                F=lambda x:(1+mp.erf(mp.sqrt(w)*(x-shift)))/2
                expected_A,expected_b=mp.sqrt(w/(2*mp.pi)),w/2
            cuts=[-mp.inf,shift-1/w,shift,shift+1/w,mp.inf]
            quad=lambda fun:mp.quad(fun,cuts)
            mass=quad(lambda x:f(x)**2)
            A=quad(lambda x:f(x)**4)
            b=quad(lambda x:df(x)**2)
            cross=quad(lambda x:df(x)*f(x)*(1-2*F(x)))
            cdfterm=quad(lambda x:f(x)**2*(1-2*F(x))**2)
            derivative_errors=[abs(mp.diff(F,x)-f(x)**2) for x in [shift-1/w,shift,shift+1/(2*w)]]
            rows=[]
            for z in [mp.mpf(0),w,-w]:
                direct=quad(lambda x:(df(x)-z*f(x)*(1-2*F(x)))**2)
                polynomial=b-2*z*A+z*z/3
                rows.append(dict(z=z,direct_square=direct,polynomial=polynomial,
                                 residual=abs(direct-polynomial),
                                 wrong_cross_sign_gap=abs(direct-(b+2*z*A+z*z/3)),
                                 wrong_quarter_gap=abs(direct-(b-2*z*A+z*z/4))))
            z=3*A
            minimum_square=quad(lambda x:(df(x)-z*f(x)*(1-2*F(x)))**2)
            profiles.append(dict(case=name,kind=kind,width=w,shift=shift,mass=mass,A=A,b=b,
                mass_residual=abs(mass-1),A_residual=abs(A-expected_A),b_residual=abs(b-expected_b),
                cross_residual=abs(cross-A),cdf_third_residual=abs(cdfterm-mp.mpf(1)/3),
                cdf_derivative_residual=max(derivative_errors),GN_slack=b-3*A*A,
                minimized_square=minimum_square,minimum_residual=abs(minimum_square-(b-3*A*A)),
                observed_ratio=A/mp.sqrt(b),rows=rows))
        maxima={}
        for field in ['mass_residual','A_residual','b_residual','cross_residual','cdf_third_residual','cdf_derivative_residual','minimum_residual']:
            v=max(r[field] for r in profiles)
            maxima[field]=dict(value=v,cases=[r['case'] for r in profiles if r[field]==v])
        squaremax=max(r['residual'] for p in profiles for r in p['rows'])
        maxima['square_expansion']=dict(value=squaremax,cases=[dict(case=p['case'],z=r['z']) for p in profiles for r in p['rows'] if r['residual']==squaremax])
        assert all(m['value']<mp.mpf(10)**(-dps+6) for m in maxima.values())
        assert all(r['wrong_cross_sign_gap']>mp.mpf('0.01') and r['wrong_quarter_gap']>mp.mpf('0.001') for p in profiles for r in p['rows'] if r['z']!=0)
        bounds=[]
        for a in [mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4]:
            M=mp.gamma((1+a)/2)/(mp.gamma(1+a)*mp.gamma((1-a)/2))
            K=2**a/(1-a)
            for c in [mp.mpf(1),mp.mpf(4)]:
                lo=mp.mpf(2)/3*mp.sqrt(c/M);hi=mp.mpf(2)/3*mp.sqrt(c*K)
                assert 0<lo<hi
                bounds.append(dict(a=a,covariance_mass=c,M=M,K0=K,proposed_lower=lo,
                    proposed_upper=hi,relative_width=hi/lo,
                    proposed_bound_status='conditional on WS1 proof/application gate; not a computed exact C2'))
        def enc(x):
            if isinstance(x,mp.mpf):return mp.nstr(x,dps+8)
            if isinstance(x,list):return [enc(v) for v in x]
            if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
            return x
        return enc(dict(dps=dps,profiles=profiles,maxima=maxima,proposed_bounds=bounds))


data=dict(schema='white-CDF-profile-calibration/1',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    mpmath_version=mp.__version__,runs=[run(40),run(70)],
    exact_negative_controls=[dict(test='wrong4A_squared_le_b',A='1/3',b='1/3',false_statement='4/9<=1/3'),
                             dict(test='wrong_half_spatial_energy',c=1,width=1,value='1/6',false_ceiling='1/12')],
    scope='deterministic profile consistency and proposed derived-bound evaluations; no H1 proof, interval enclosure, PDE simulation or exact C2 evaluation')
with mp.workdps(85):
    data['precision_differences']=[dict(case=r['case'],A_difference=mp.nstr(abs(mp.mpf(r['A'])-mp.mpf(s['A'])),80),b_difference=mp.nstr(abs(mp.mpf(r['b'])-mp.mpf(s['b'])),80)) for r,s in zip(data['runs'][0]['profiles'],data['runs'][1]['profiles'])]
(P/'cdf-profile-screen-v1.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(maxima=[dict(dps=r['dps'],maxima=r['maxima']) for r in data['runs']],unit_covariance_half_time=[r for r in data['runs'][-1]['proposed_bounds'] if r['a']=='0.5' and r['covariance_mass']=='1.0'])))
