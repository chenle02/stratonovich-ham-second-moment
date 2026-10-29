"""Independent rational geometry/covariance checks and executed calibration."""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('degree_four', HERE/'degree-four.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def clip(poly, a, b, c):
    out = []
    for P, R in zip(poly, poly[1:]+poly[:1]):
        fp, fr = a*P[0]+b*P[1]-c, a*R[0]+b*R[1]-c
        if fp <= 0:
            out.append(P)
        if (fp < 0 < fr) or (fr < 0 < fp):
            t = fp/(fp-fr)
            out.append((P[0]+t*(R[0]-P[0]), P[1]+t*(R[1]-P[1])))
    return out


def polygon_area(gaps, g):
    times = [sum(gaps[:j+1]) for j in range(4)]
    bounds = [None, None]
    C = None
    for chain in g['chains']:
        if not chain:
            continue
        j = chain[0]
        p = g['labels'][j]
        bounds[p] = times[j] if bounds[p] is None else min(bounds[p], times[j])
        for i, j in zip(chain, chain[1:]):
            if g['labels'][i] != g['labels'][j]:
                d = times[j]-times[i]
                C = d if C is None else min(C, d)
    A, B = bounds
    if A is None:
        A = B+C
    if B is None:
        B = A+C
    poly = [(-A,-B),(A,-B),(A,B),(-A,B)]
    if C is not None:
        poly = clip(clip(poly, Q(1), Q(-1), C), Q(-1), Q(1), C)
    return abs(sum(P[0]*R[1]-R[0]*P[1] for P,R in zip(poly,poly[1:]+poly[:1])))/32


def exact_determinant(gaps, g):
    times = [sum(gaps[:j+1]) for j in range(4)]
    def cov(p, q):
        i,j = p
        k,l = q
        return sum(s*t*min(times[u],times[v]) for u,s in [(i,-1),(j,1)]
                   for v,t in [(k,-1),(l,1)] if g['colors'][u]==g['colors'][v])
    p,q = g['pairing']
    return cov(p,p)*cov(q,q)-cov(p,q)**2


def main():
    gs=base.graphs()
    patterns=[(1,1,1,1),(1,2,3,7),(9,1,2,1),(1,10,1,2),(2,1,17,1),(1,2,1,19)]
    geometric=0
    for z in patterns:
        gaps=[Q(v,sum(z)) for v in z]
        x=np.array([[float(v) for v in gaps]])
        t=np.cumsum(x,axis=1)
        for g in gs:
            target=polygon_area(gaps,g)
            value=float(base.physical_volume(x,t,g)[0])
            assert math.isclose(value,float(target),rel_tol=1e-12,abs_tol=1e-14)
            determinant=sum(c*gaps[i]*gaps[j] for i,j,c in g['det_terms'])
            assert determinant==exact_determinant(gaps,g)>0
            geometric+=1
    old=json.loads((HERE.parent/'2026-10-29-near-static-lower/white-order-four-screen.json').read_text())
    lookup={r['a']:r for r in old['white_one_chain_total_order_four']}
    numerical=json.loads((HERE/'refined-18.json').read_text())
    checks=[]
    for run in numerical['runs']:
        a=run['a']
        for row in run['diagrams']:
            if a==0:
                exact=float(Q(row['static_exact']))
                names=['actual','shared']
            elif row['key'][0] in '04':
                shape={'01|23':'adjacent','02|13':'crossing','03|12':'nested'}[row['key'][2:]]
                exact=lookup[a][shape]*math.gamma(7-2*a)
                names=['actual','shared']
            elif row['key'] in ['2:01|23','1:01|23','3:03|12']:
                exact=math.gamma(1-a)**2/(4 if row['key'][0]=='2' else 8)
                names=['actual']
            else:
                continue
            for name in names:
                # Diagnostic acceptance, not a rigorous enclosure. Fixed budget:
                # 8 replicate SE plus a 0.2% relative floating/finite-probe allowance.
                error=abs(row[name]-exact)
                budget=8*row[name+'_replicate_se']+.002*abs(exact)
                checks.append(dict(a=a,key=row['key'],quantity=name,reference=exact,
                                   value=row[name],abs_error=error,budget=budget,pass_=error<=budget))
    assert all(c['pass_'] for c in checks)
    result=dict(status='PASS finite evaluator calibration only;not proof of comparison',
                rational_geometry_cases=geometric,rational_covariance_determinant_cases=geometric,
                normalization='Spatial area includes1/16;Gaussian pair density includes1/(2pi).',
                calibration_error_budget='8 scramble-replicate SE +0.2%relative;diagnostic,not certified',
                calibration=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='calibration'}|{'calibration_cases':len(checks)},indent=2))


if __name__=='__main__':
    main()
