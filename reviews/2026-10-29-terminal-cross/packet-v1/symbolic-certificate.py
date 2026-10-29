"""Exact algebra checks; Lean checks the final real-valued consumer as well."""
from pathlib import Path
import hashlib
import json
import sympy as s


b,c,x,y=s.symbols('b c x y',real=True)
A,t=s.symbols('A t',positive=True)
P=c*c+c+1
N=b*P+c**3+c+1
poly=s.expand((c+1)**2*((c*c+1)*b*b+c*c-1)*N*N
              -4*(c*c+1)*P*P*(b+c-1)**2*(b+1)**2)
shift=s.Poly(s.expand(poly.subs({b:x+1,c:y+1})),x,y)
assert len(shift.terms())==47 and all(k>0 for _,k in shift.terms())
assert all(m[1]>=1 for m,_ in shift.terms())
rows=[]
for region in ['A<t','t<A']:
    if region=='A<t':
        C=4*t*t/((t-A)*(t+A)**2)
        D=2*A/((t-A)*(t+A))
        slow,fast=A,t
    else:
        C=2*A/((A-t)*(A+t))
        D=4*t*t/((A-t)*(A+t)**2)
        slow,fast=t,A
    mass=2*(A+2*t)/(A+t)**2
    rate=A*t/(A+2*t)
    assert s.cancel(C-D-mass)==0
    assert s.cancel((C-D)*rate-(C*slow-D*fast))==0
    rows.append(dict(region=region,mass_identity=True,convex_rate_identity=True))
out=dict(status='PASS exact symbolic identities;not analytic/SPDE verification',
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         monomials=[dict(x=i,y=j,coefficient=int(k))for(i,j),k in shift.terms()],
         all_47_coefficients_positive=True,all_terms_divisible_by_y=True,
         component_checks=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='monomials'},indent=2))
