"""Exact polynomial-sector checks, independent of time-minimum reductions.
Run: uv run --with sympy python <this file>.
"""
import sympy as s
import json
u,v=s.symbols('u v',nonnegative=True)
R=s.Rational

def integral(m,n,p,q,r,z):
    # Integrate (1-p*u-q*v)^m (1-r*u-z*v)^n on both positive halves.
    cuts={s.Integer(0)}
    umax=min([1/s.Rational(x) for x in (p,r) if x] or [s.oo])
    if umax==s.oo: raise ValueError('unbounded u')
    cuts.add(umax)
    if q and z:
        root=s.solve((1-p*u)/q-(1-r*u)/z,u)
        if root and 0<root[0]<umax: cuts.add(root[0])
    cuts=sorted(cuts)
    total=0
    for a,b in zip(cuts,cuts[1:]):
        mid=(a+b)/2
        candidates=[(1-p*u)/q] if q else []
        if z: candidates.append((1-r*u)/z)
        vmax=min(candidates,key=lambda x:x.subs(u,mid))
        if vmax.subs(u,mid)<0: continue
        total+=s.integrate(s.integrate((1-p*u-q*v)**m*(1-r*u-z*v)**n,(v,0,vmax)),(u,a,b))
    return s.factor(total)

# Each row gives three sectors, each with its reflected sector, and |Jacobian|=1.
# Single-chain rows use m=0, so the first length is irrelevant.
rows=[
 ('04-A',0,4,[(0,0,1,1),(0,0,1,2),(0,0,2,1)]),
 ('04-B',0,4,[(0,0,1,3),(0,0,1,4),(0,0,4,3)]),
 ('04-C',0,4,[(0,0,1,2),(0,0,1,3),(0,0,3,2)]),
 ('13-1',1,3,[(1,0,1,1),(1,1,1,2),(1,0,2,1)]),
 ('13-2',1,3,[(1,0,1,3),(1,1,1,2),(1,0,2,3)]),
 ('13-3',1,3,[(1,0,1,2),(1,1,1,1),(1,0,1,2)]),
 ('22-A',2,2,[(1,0,1,1),(1,1,1,0),(1,0,0,1)]),
 ('22-B',2,2,[(1,1,1,1),(1,2,1,2),(2,1,2,1)]),
 ('22-C',2,2,[(1,1,1,2),(1,2,1,1),(2,1,1,2)]),
]
expected=[R(1,2880),R(1,8640),R(1,5760),R(1,576),R(29,34560),R(1,640),R(1,144),R(1,480),R(31,17280)]
out=[]
for (name,m,n,sectors),target in zip(rows,expected):
    vals=[integral(m,n,*x) for x in sectors]
    value=s.factor(2*sum(vals)/(16*s.factorial(m)*s.factorial(n)))
    assert value==target,(name,value,target)
    out.append({'diagram':name,'sector_lengths':sectors,'sector_integrals':[str(x) for x in vals],'coefficient':str(value)})
print(json.dumps({'method':'exact rational polynomial sector integration; not Lean','rows':out,'total_order_four':'11/540'},indent=2))
