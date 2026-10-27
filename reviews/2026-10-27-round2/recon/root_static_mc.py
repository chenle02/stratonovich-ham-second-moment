"""Independent bounded-indicator static check; numerical evidence, not proof."""
import json, math
import numpy as np
rng=np.random.default_rng(20261027)
N=1048576
pairs=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
rows=[]
for m in range(5):
    counts=np.zeros(3,dtype=np.int64)
    for batch in range(N//16384):
        u=rng.random((16384,6))
        times=np.concatenate((np.sort(u[:,:m],axis=1),np.sort(u[:,m:4],axis=1)),axis=1)
        colors=2*u[:,4:]-1
        for k,D in enumerate(pairs):
            pos=np.empty((16384,4))
            for c,(i,j) in enumerate(D): pos[:,i]=colors[:,c];pos[:,j]=colors[:,c]
            ok=np.ones(16384,dtype=bool)
            for chain in [range(m),range(m,4)]:
                pt=0.;px=0.
                for i in chain:
                    ok &= np.abs(pos[:,i]-px) <= times[:,i]-pt
                    pt=times[:,i];px=pos[:,i]
            counts[k]+=np.count_nonzero(ok)
    scale=1/(4*math.factorial(m)*math.factorial(4-m))
    p=counts/N
    rows.append({'m':m,'n':4-m,'estimates':list(p*scale),'standard_errors':list(np.sqrt(p*(1-p)/N)*scale)})
print(json.dumps({'method':'independent IID uniform time/space indicator integration of original delta-contracted wave integrals','samples_per_split':N,'seed':20261027,'warning':'Monte Carlo standard errors are diagnostic only, not certified integration or proof','rows':rows},indent=2))
