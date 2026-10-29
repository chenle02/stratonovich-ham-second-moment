"""Unreviewed exact-reduction probe for white (1,3), pair partition 03|12.

lambda is the terminal cross-pair charge; nu is the earlier self-pair charge.
theta=1. Jdag drops the positive clock overlap and therefore enlarges J.
High-precision quadrature is diagnostic, not a certified interval.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time

import mpmath as mp


def actual(lam, nu):
    c, b = 1 + lam, 1 + nu
    return (b * (c*c+c+1) + c**3+c+1) / (32*c**3*(b+c-1)*(b+1))


def nfun(b):
    return 2/(mp.pi*b*b) + 2*(b*b-1)*mp.atan(b)/(mp.pi*b**3)


def clock_enlarged(lam, nu):
    b, c = 1+nu, 1+lam
    if lam == 0:
        return mp.mpf(3)/(32*b)
    A = lam+lam*lam/2
    d = mp.sqrt(b*b+c*c-1)
    M = 2/mp.pi * (mp.quad(lambda t: 1/(c*c+(b*b+1-c*c)*t*t), [0,1])
                   + mp.quad(lambda t: 1/(d*d+(2-c*c)*t*t), [0,1]))
    return ((M-1/(c*d))/(A*A) + 2/A*(nfun(b)-1/(c**3*d)))/64


def hplus(q):
    return ((1-q)*mp.erfc(mp.sqrt(q/2))
            + mp.sqrt(2*q/mp.pi)*mp.exp(-q/2))


def lminus(A):
    c = mp.sqrt(1+2*A)
    return 1/A + (1-1/c)/(A*A) - 2/(A*c**3)


def heat_fiber(lam,w):
    if lam == 0:
        return mp.mpf(6), mp.mpf(0)
    A = lam+lam*lam/2
    cutoff = w+200
    value = (mp.quad(lambda q: hplus(q)*mp.exp(-A*(w-q)), [0,w])
             + mp.quad(lambda q: hplus(q)*mp.exp(-A*(q-w)), [w,cutoff])
             + mp.exp(-A*w)*lminus(A))
    # Exact analytic upper bound for the OMITTED positive q tail, not a
    # certificate for the finite-interval quadrature/rounding error.
    tail = 2/mp.sqrt(mp.pi)*mp.gammainc(mp.mpf(5)/2,cutoff/2,mp.inf)
    return value,tail


def rayleigh_laplace(s,w):
    return 1-s*mp.sqrt(mp.pi*w/2)*mp.exp(s*s*w/2)*mp.erfc(s*mp.sqrt(w/2))


def transformed_wave_fiber(lam,w):
    if lam == 0:
        return mp.mpf(6)
    if lam == 1:
        e = mp.exp(w/2)*mp.erfc(mp.sqrt(w/2))
        moment = mp.sqrt(mp.pi*w/2)*(1+w)*e-w
        return moment+mp.mpf(7)/4*rayleigh_laplace(1,w)
    c = 1+lam
    acoef = 2*(c+2)/(c**3*(2-c))
    bcoef = 2*(c-1)/(c*(2-c))
    return acoef*rayleigh_laplace(lam,w)-bcoef*rayleigh_laplace(1,w)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dps',type=int,default=50)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--skip-fibers',action='store_true')
    args=p.parse_args();mp.mp.dps=args.dps;started=time.monotonic()
    params=['0','.1','1','10'];closed=[]
    for x in params:
        for y in params:
            lam,nu=mp.mpf(x),mp.mpf(y)
            I,J=actual(lam,nu),clock_enlarged(lam,nu)
            closed.append(dict(lam=x,nu=y,actual=str(I),clock_upper=str(J),
                               difference=str(I-J),ratio=str(J/I)))
    fibers=[]
    if not args.skip_fibers:
        for x in ['.1','.5','1','2','10']:
            for y in ['.001','.01','.1','1','10','100']:
                lam,w=mp.mpf(x),mp.mpf(y)
                H,tail=heat_fiber(lam,w);T=transformed_wave_fiber(lam,w)
                fibers.append(dict(lam=x,w=y,heat=str(H),transformed_wave=str(T),
                                   difference=str(T-H),heat_omitted_tail_bound=str(tail)))
    result=dict(status='UNREVIEWED floating falsification of candidate reductions',
                diagram='white (1,3),03|12;lambda=cross,nu=self;theta1',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                mpmath_version=mp.__version__,dps=args.dps,closed=closed,fibers=fibers,
                elapsed_seconds=time.monotonic()-started,
                exclusion='No analytic inequality,all-order,sharp or Skorohod claim;quadrature is not certified.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'elapsed':result['elapsed_seconds'],'minimum_closed_difference':
                     str(min(mp.mpf(r['difference'])for r in closed)),
                     'negative_fibers':[r for r in fibers if mp.mpf(r['difference'])<0]},indent=2))


if __name__=='__main__':
    main()
