"""Finite interval/cube/counting calibration,not a proof or Lean certificate."""
import itertools,json,math
import numpy as np
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss

A0=np.diag([1.,4.])
M=[np.array([[0.,1.],[1.,0.]]),np.array([[.5,0.],[0.,-.5]])]
G0=np.block([[np.zeros((2,2)),np.eye(2)],[-A0,np.zeros((2,2))]])
G=[np.block([[np.zeros((2,2)),np.zeros((2,2))],[m,np.zeros((2,2))]]) for m in M]
v=np.array([1.,.2,.3,-.1])
indices=list(itertools.product(range(3),repeat=2));pos={x:i for i,x in enumerate(indices)}
def ring_flow(intervals):
    lift0=np.kron(np.eye(9),G0);shifts=[]
    for j in range(2):
        S=np.zeros((9,9))
        for p,i in pos.items():
            q=list(p);q[j]+=1;q=tuple(q)
            if q in pos:S[pos[q],i]=1
        shifts.append(S)
    times=sorted(set([0.,1.]+[x for I in intervals for x in I]))
    z=np.zeros(36);z[:4]=v
    for lo,hi in zip(times,times[1:]):
        active=[j for j,I in enumerate(intervals) if I[0]<(lo+hi)/2<I[1]]
        lift=lift0.copy()
        for j in active:lift+=np.kron(shifts[j],G[j])
        z=expm((hi-lo)*lift)@z
    return {p:z[4*i:4*i+4] for p,i in pos.items()}
nodes,weights=leggauss(14)
def quad_vec(fn,lo,hi):
    if hi<=lo:return np.zeros(4)
    out=np.zeros(4)
    for u,w in zip(nodes,weights):out+=w*fn((lo+hi)/2+(hi-lo)*u/2)
    return out*(hi-lo)/2
def cube_coefficient(I1,I2):
    def outer(t1):
        def inner(t2):
            if t1<t2:
                return expm((1-t2)*G0)@G[1]@expm((t2-t1)*G0)@G[0]@expm(t1*G0)@v
            return expm((1-t1)*G0)@G[0]@expm((t1-t2)*G0)@G[1]@expm(t2*G0)@v
        return quad_vec(inner,I2[0],min(t1,I2[1]))+quad_vec(inner,max(t1,I2[0]),I2[1])
    breaks=sorted(set([I1[0],I1[1]]+[x for x in I2 if I1[0]<x<I1[1]]))
    return sum((quad_vec(outer,lo,hi) for lo,hi in zip(breaks,breaks[1:])),np.zeros(4))
layouts=[[(0.,.5),(.5,1.)],[(0.,1.),(.25,.75)],[(0.,.75),(.25,1.)]]
out=[]
H=np.diag([1.,1.,1/5,1/8]) # X_lambda with lambda2,physical A0 frequencies1,2.
for intervals in layouts:
    coeff=ring_flow(intervals);cube=cube_coefficient(*intervals)
    err=float(np.linalg.norm(cube-coeff[(1,1)]));assert err<1e-11
    splits=[]
    for r in indices:
        s=(2-r[0],2-r[1])
        splits.append({'left':r,'right':s,'term':float(coeff[r]@H@coeff[s])})
    out.append({'intervals':intervals,'cube_ordering_error':err,'mixed_variance_coefficient':sum(x['term'] for x in splits),'nine_split_terms':splits})
alpha=1.5;alpha0=.25;beta=4-alpha-alpha0;p=2-alpha0;gamma=3-alpha
def first_inventory(J,k,refined):
    total=0.
    for j in range(J+1):
        h=2.**(-j)
        w=h**beta*(1+1/(k*h))+k**(alpha-2)*h**p if refined else h**beta*(1+1/(k*h))**2
        total+=2**j*w
    return total
limit=1/(1-2**(-(beta-1)))+1/(1-2**(-(beta-2)))+1/(1-2**(-(p-1)))
count=[]
for J in [2,4,8,12,20]:
    refined=first_inventory(J,1,True);crude=first_inventory(J,1,False)
    assert refined<=limit*(1+1e-12)
    count.append({'depth':J,'refined_first_sum':refined,'exact_refined_upper':limit,'crude_first_sum':crude})
assert count[-1]['crude_first_sum']>100*count[-1]['refined_first_sum']
print(json.dumps({'interval_algebra':out,'inventory_first_order':count,'parameters':{'alpha':alpha,'alpha0':alpha0,'beta':beta,'gamma':gamma,'p':p},'status':'PASS','scope':'finite operator/time-ordering diagnostics and exact geometric first-order sum;no infinite-dimensional or full-target certification'},indent=2))
