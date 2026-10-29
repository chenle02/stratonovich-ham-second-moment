"""Exact finite Gaussian-degree screen;not an SPDE proof or norm certificate."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


def norm2(f):
    # Unnormalized orthogonal Hermites:H_a have norm^2=product a_j!.
    return sum((c*c*factorial(a)*factorial(b) for (a,b),c in f.items()),Q(0))


def multiply(f,h):
    out={}
    for index,c in f.items():
        for j,hj in enumerate(h):
            up=list(index);up[j]+=1;up=tuple(up)
            out[up]=out.get(up,Q(0))+hj*c
            if index[j]:
                down=list(index);down[j]-=1;down=tuple(down)
                out[down]=out.get(down,Q(0))+hj*index[j]*c
    return {a:c for a,c in out.items() if c}


cases=0
for N in range(9):
    basis=[(a,b) for a in range(N+1) for b in range(N+1-a)]
    inputs=[{index:Q(1)} for index in basis]
    inputs += [{index:Q((-1)**(a+b)*(a+2*b+1),a+b+1)
                for index in basis for a,b in [index]}]
    for f in inputs:
        for h in [(Q(1),Q(0)),(Q(1),Q(1)),(Q(2,3),Q(-3,5))]:
            out=multiply(f,h);v=sum((c*c for c in h),Q(0))
            assert norm2(out)<=4*(N+1)*v*norm2(f)
            assert all(sum(index)<=N+1 for index in out)
            cases+=1
# F=g_1 is coupled to the external coordinate,not its independent vacuum.
f={(1,0):Q(1)};out=multiply(f,(Q(1),Q(0)))
assert out=={(2,0):Q(1),(0,0):Q(1)}
assert norm2(out)==3 and norm2(f)==1
result={'cases':cases,'degrees':'0 through8,two Gaussian coordinates',
        'coarse_bound':'||W(h)F||_2^2 <= 4(N+1)||h||^2||F||_2^2',
        'mixed_and_homogeneous_inputs_checked':True,
        'annihilation_retained':True,
        'negative_control':{'input':'F=g_1','external':'W(h)=g_1',
                            'actual_product_norm_squared':3,'incorrect_vacuum_bound_squared':1},
        'status':'PASS finite diagnostics only',
        'does_not_prove':'Infinite-degree/infinite-mode result,Bochner limit,uniform mixed-width bound or mild equation'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
