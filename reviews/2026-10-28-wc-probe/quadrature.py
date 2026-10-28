"""Deterministic floating diagnostics for WC at h=1,W=0; no certified enclosures.
Run: uv run --with numpy --with scipy python reviews/2026-10-28-wc-probe/quadrature.py
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.special import ellipkm1
from scipy.integrate import quad


def time_density(a,b):
    den=(1+a-b)*(1-a+b)
    complementary=4*a*b/den
    return ellipkm1(complementary)/(2*np.pi**2*np.sqrt(den))


def integral(z,alpha,n,angular='plain'):
    nodes,weights=np.polynomial.legendre.leggauss(n)
    v=(nodes+1)/2; wv=weights/2
    p=4/(2-alpha)
    radial=v**p
    if angular=='plain':
        phi=np.pi*v; wp=np.pi*wv
    else:
        psi=np.pi*v/2
        c=np.sqrt((1-z)/(1+z))
        phi=2*np.arctan(c*np.tan(psi))
        wp=np.pi*wv*c/(np.cos(psi)**2+c*c*np.sin(psi)**2)
    total=0.0
    for ph,w in zip(phi,wp):
        R=(1-z*z)/(2*(1-z*np.cos(ph)))
        a=R*radial
        b=np.sqrt((a-z)**2+2*a*z*(1-np.cos(ph)))
        density=time_density(a,b)
        # r^(1-alpha)dr = R^(2-alpha)*p*v^3 dv, exactly.
        total+=w*np.dot(wv,R**(2-alpha)*p*v**3*density)
    return 2*total


def main():
    controls=[]
    for a,b in [(0.1,0.2),(0.3,0.3),(0.001,0.7),(0.4,0.599)]:
        L=1-a-b
        direct=quad(lambda th:1/(2*np.pi**2*np.sqrt((2*a+L*np.sin(th)**2)*(2*b+L*np.cos(th)**2))),0,np.pi/2,epsabs=1e-12)[0]
        closed=float(time_density(a,b))
        controls.append({'a':a,'b':b,'direct_theta':direct,'elliptic':closed,'relative_difference':abs(closed-direct)/direct})
    calibrations=[];rows=[]
    for n in [64,128,256]:
        for z in [0,0.5,0.9,0.99,0.999,0.9999]:
            exact=np.sqrt(1-z*z)/(4*np.pi)
            for angular in ['plain','ellipse']:
                val=integral(z,0,n,angular)
                calibrations.append({'n':n,'z':z,'angular':angular,'computed':val,'unweighted_control':exact,'relative_error':abs(val/exact-1)})
        for alpha in [1.5,1.6,1.75,1.9]:
            for eps in [0.1,0.01,0.001,0.0001]:
                z=1-eps
                for angular in ['plain','ellipse']:
                    val=float(integral(z,alpha,n,angular))
                    rows.append({'n':n,'alpha':alpha,'epsilon':eps,'angular':angular,'value':val,'endpoint_scaled':val*eps**(alpha-1.5),'ratios':{str(q):val/(1/(2*np.pi*np.sqrt(1-z*z)))**(2*q-1) for q in [0.55,0.7,0.85,0.95]}})
    out={'status':'FLOATING_DIAGNOSTIC_NOT_CERTIFIED','object':'WC lhs at h=1,Z=(1-epsilon,0),W=0','scope':'Does not establish global uniform bound, full moment bound, or rigour of a limiting power','method':'Exact time-variable reduction proposed in root memo; elliptic evaluation; two angular parameterizations; n=64,128,256 Gauss-Legendre; no clipping or Monte Carlo','errors':'Refinement/parameterization discrepancy is diagnostic only, not a rigorous quadrature error enclosure. Floating rounding and unresolved layers remain.','time_density_controls':controls,'unweighted_calibrations':calibrations,'rows':rows}
    path=Path(__file__).with_name('quadrature-results.json'); path.write_text(json.dumps(out,indent=2)+'\n')
    print('max theta identity relative discrepancy',max(x['relative_difference'] for x in controls))
    for n in [64,128,256]:
        print('n',n,'max unweighted calibration error',max(x['relative_error'] for x in calibrations if x['n']==n))
    for alpha in [1.5,1.6,1.75,1.9]:
        print('alpha',alpha,[(r['epsilon'],round(r['endpoint_scaled'],6)) for r in rows if r['alpha']==alpha and r['n']==256 and r['angular']=='plain'])

if __name__=='__main__':main()
