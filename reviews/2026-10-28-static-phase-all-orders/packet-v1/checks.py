"""Finite noncommuting/Fourier-band algebra screens,not an analytic proof."""
import itertools,json,math
import numpy as np
from scipy.linalg import expm,fractional_matrix_power
from scipy.special import beta
rows=[]
H=[np.array([[0.,1.],[1.,0.]]),np.array([[.5,0.],[0.,-.5]])]
sigma=np.linalg.norm(sum(h@h for h in H),2)**.5
for N in [1,2,3,5]:
    indices=[x for x in itertools.product(range(N+1),repeat=2) if sum(x)<=N]
    pos={x:i for i,x in enumerate(indices)}; gs=[]
    for j in range(2):
        g=np.zeros((len(indices),len(indices)))
        for m,k in enumerate(indices):
            nxt=list(k);nxt[j]+=1;nxt=tuple(nxt)
            if nxt in pos:g[pos[nxt],m]=math.sqrt(k[j]+1);g[m,pos[nxt]]=math.sqrt(k[j]+1)
        gs.append(g)
    K=sum(np.kron(h,g) for h,g in zip(H,gs))
    actual=np.linalg.norm(K,2);bound=2*math.sqrt(N+1)*sigma
    assert actual<=bound+1e-10
    rows.append({'N':N,'fock_dimension':len(indices),'operator_norm':actual,'bound':bound})
complex_rows=[]
for a in [.6,.9]:
    I=beta(.5,1-a/2);delta=min(.25,math.pi/(8*I))
    for R in [2.,10.,100.]:
        A0=np.diag([1.,R*R]);B=np.array([[0.,R**a],[R**a,0.]])
        A=A0+np.eye(2);S=np.diag([1.,1.,1/math.sqrt(2),1/math.sqrt(1+R*R)])
        maxnorm=0.;rootdiff=0.
        for theta in np.linspace(0,2*math.pi,17)[:-1]:
            z=delta*np.exp(1j*theta);L=A0-z*B
            Q=np.diag(np.sqrt(np.diag(A)))@fractional_matrix_power(L+np.eye(2),-.5)
            rootdiff=max(rootdiff,float(np.linalg.norm(Q-np.eye(2),2)))
            gen=np.block([[np.zeros((2,2)),np.eye(2)],[-L,np.zeros((2,2))]])
            for t in [.1,1.,3.]:
                flow=S@expm(t*gen)@np.linalg.inv(S)
                val=float(np.linalg.norm(flow,2));assert val<=100*math.exp(2*t)
                maxnorm=max(maxnorm,val)
        assert rootdiff<=1/6+1e-8
        complex_rows.append({'a':a,'R':R,'delta':delta,'max_root_difference':rootdiff,'max_phase_norm':maxnorm})
vacuum_rows=[]
def vacuum_coefficient(n,N):
    indices=[x for x in itertools.product(range(N+1),repeat=2) if sum(x)<=N]
    pos={x:i for i,x in enumerate(indices)}; gs=[]
    for j in range(2):
        g=np.zeros((len(indices),len(indices)))
        for k,v in enumerate(indices):
            w=list(v);w[j]+=1;w=tuple(w)
            if w in pos:g[pos[w],k]=math.sqrt(v[j]+1);g[k,pos[w]]=math.sqrt(v[j]+1)
        gs.append(g)
    dim=2*len(indices); A=np.kron(np.eye(len(indices)),np.diag([1.,4.]))
    B=sum(np.kron(g,h) for g,h in zip(gs,H))
    G0=np.block([[np.zeros((dim,dim)),np.eye(dim)],[-A,np.zeros((dim,dim))]])
    G1=np.block([[np.zeros((dim,dim)),np.zeros((dim,dim))],[B,np.zeros((dim,dim))]])
    lift=np.kron(np.eye(n+1),G0)+np.kron(np.diag(np.ones(n),-1),G1)
    initial=np.zeros((n+1)*2*dim);initial[:2]=[1.,.3];initial[dim:dim+2]=[.2,-.1]
    result=(expm(lift)@initial)[n*2*dim:(n+1)*2*dim]
    return {k:np.r_[result[2*i:2*i+2],result[dim+2*i:dim+2*i+2]] for k,i in pos.items()}
for n in [1,2]:
    small=vacuum_coefficient(n,n);large=vacuum_coefficient(n,n+2)
    gap=sum(np.linalg.norm(large[k]-small.get(k,np.zeros(4)))**2 for k in large)**.5
    assert gap<1e-10
    too_shallow=vacuum_coefficient(n,n-1)
    refusal=sum(np.linalg.norm(large[k]-too_shallow.get(k,np.zeros(4)))**2 for k in large)**.5
    assert refusal>1e-5
    vacuum_rows.append({'order':n,'N_equals_n_difference':gap,'N_equals_n_minus1_refusal_gap':refusal})
print(json.dumps({'fock_noncommuting':rows,'complex_phase':complex_rows,'vacuum_cutoff':vacuum_rows,'status':'PASS','scope':'finite diagnostic only;the abstract comparison condition for B_R is checked by the three analytic rho regions in the accompanying calibration'},indent=2))
