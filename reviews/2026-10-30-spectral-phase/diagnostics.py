from fractions import Fraction as Q
from pathlib import Path
import json
A=((Q(2),Q(0)),(Q(0),Q(1,2)))
B=((Q(1,2),Q(0)),(Q(0),Q(2)))
product=tuple(tuple(sum(B[i][k]*A[k][j] for k in range(2)) for j in range(2)) for i in range(2))
assert product==((1,0),(0,1))
v=(Q(0),Q(100))
assert max(abs(x) for x in v)==100 and v[0]==0
r={'status':'PASS diagnostic witnesses','block_matrices':[[[str(x) for x in row] for row in C] for C in (A,B)],'individual_infinity_operator_norms':[2,2],'product':[[str(x) for x in row] for row in product],'product_norm':1,'large_phase_vector':[str(x) for x in v],'phase_infinity_norm':100,'displacement_observable':0,'scope':'Finite algebra screening only; no counterexample to actual HAM, no spectral/product theorem or Lean certificate.'}
Path(__file__).with_name('diagnostics.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
