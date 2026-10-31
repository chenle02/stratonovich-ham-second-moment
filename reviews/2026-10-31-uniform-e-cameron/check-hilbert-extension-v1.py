"""Exact finite tensor norm and Gaussian moment diagnostics, r=4."""
from pathlib import Path
import json
import sympy as s
Q=s.Rational
O=s.Matrix([[Q(3,5),Q(4,5),0],[-Q(4,5),Q(3,5),0],[0,0,1]])
assert O.T*O==s.eye(3)
a=s.Matrix([1,-2,1]);b=s.Matrix([Q(3,5),Q(4,5),0])
cases=[('rank1',a*b.T,s.Integer(18),b),('diagonal',s.diag(1,2,-3),s.Integer(81),s.Matrix([0,0,1])),('rotated_diagonal',s.diag(1,2,-3)*O,s.Integer(81),O.T*s.Matrix([0,0,1]))]
def output4(A,X):
 Y=A*X
 return sum(sum(Y[i,j]**2 for j in range(Y.cols))**2 for i in range(Y.rows))
def input4(X):return sum(x*x for x in X)**2
rows=[]
for name,A,norm4,v in cases:
 for m in [1,2,5,11]:
  c=s.Matrix(1,m,lambda i,j:Q((j%3)-1,2) if j else s.Integer(1))
  for tag,X in [('aligned',v*c),('mixed',s.Matrix(3,m,lambda i,j:Q(((i+2)*(j+3)%11)-5,7)))]:
   lhs=output4(A,X);rhs=norm4*input4(X)
   assert lhs<=rhs
   if tag=='aligned':assert lhs==rhs
   rows.append({'case':name,'Hilbert_coordinates':m,'input':tag,'L4_Hilbert_norm_fourth':str(lhs),'scalar_operator_norm_fourth_times_input_norm_fourth':str(rhs),'exact_inequality':True,'saturates':lhs==rhs})
moments=[]
for B in [s.Matrix([[1,0],[0,1]]),s.Matrix([[1,2],[2,4]]),s.Matrix([[1,2,3],[0,1,-1],[2,0,1]])]:
 C=B*B.T;tr=s.trace(C);actual=tr**2+2*s.trace(C*C)
 assert actual<=3*tr**2
 moments.append({'covariance_trace':str(tr),'exact_Hilbert_Gaussian_fourth_moment':str(actual),'scalar_m4_times_trace_squared':str(3*tr**2),'exact_inequality':True})
# Rank-one time operator tensor Hilbert identity: distinct unit spatial
# directions keep their image distance, no compactness inference.
separation=[]
for m in [2,5,11]:
 e1=s.zeros(1,m);e1[0,0]=1
 e2=s.zeros(1,m);e2[0,1]=1
 D=b*(e1-e2)
 input2=sum(x*x for x in D)
 output=output4(a*b.T,D)
 assert input2==2 and output==72
 separation.append({'Hilbert_coordinates':m,'input_distance_squared':str(input2),'output_L4_Hilbert_distance_fourth':str(output),'exact_independent_of_dimension':True})
out={'scope':'24exact finite tensor norm cases at r4,3Gaussian fourth-moment algebra cases,3finite orthogonal-spatial separation guards; no full infinite-dimensional proof/actual fractional C_t approximation','norm_cases':rows,'gaussian_moment_cases':moments,'noncompactness_sequence_guards':separation,'caution':'A dimension-dependent sqrt(m) upper can be valid but is too loose; these checks do not refute such an upper. Tensor compactness requires a separate argument and is not claimed.','sympy_version':s.__version__}
Path(__file__).with_name('hilbert-extension-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('24 exact tensor norm cases,3Gaussian moment cases and3spatial separation guards pass')
