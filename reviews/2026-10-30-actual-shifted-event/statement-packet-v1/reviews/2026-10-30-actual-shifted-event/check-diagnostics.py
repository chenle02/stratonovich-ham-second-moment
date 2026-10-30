"""Exact finite controls for floor/remainder and noncommuting products."""
from fractions import Fraction as Q
import json

def mul(A, B):
  return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(A, B):
  return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def sub(A, B):
  return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]
I=[[Q(1),Q(0)],[Q(0),Q(1)]]
Z=[[Q(0),Q(0)],[Q(0),Q(0)]]
As=[[[Q(1),Q(1,10)],[Q(0),Q(1)]],[[Q(1),Q(0)],[Q(1,8),Q(1)]],[[Q(11,10),Q(1,20)],[Q(0),Q(9,10)]]]
Bs=[[[Q(1),Q(0)],[Q(0),Q(1)]],[[Q(1),Q(0)],[Q(0),Q(1)]],[[Q(1),Q(0)],[Q(0),Q(1)]]]
# Ordered products P=A_(n-1)...A_0.
prod=lambda xs: I if not xs else mul(xs[-1],prod(xs[:-1]))
terms=Z
for k in range(3):
  terms=add(terms,mul(mul(prod(Bs[k+1:]),sub(As[k],Bs[k])),prod(As[:k])))
assert terms==sub(prod(As),prod(Bs))
assert mul(As[0],As[1])!=mul(As[1],As[0])
count=0;partial_count=0
for n in range(4,41):
 for T in range(1,6):
  if n<T:continue
  delta=Q(1,n);N=n//T;s=n-N*T
  assert N>=1 and 0<=s<T and delta*(N*T+s)==1
  h=lambda t: 1+t*t
  rate=delta*(T*sum(h(delta*m*T) for m in range(N))+s*h(delta*N*T))
  assert abs(rate-Q(4,3))<=2*T*delta
  if s:
   assert rate!=delta*T*sum(h(delta*m*T) for m in range(N))
   partial_count+=1
  count+=1
for n in range(1,21):
 assert (1+Q(1,n))**n-1>=1
for n in [1,2,4,8]:
 delta=Q(1,n**4)
 assert delta*Q(n)*Q(n*n)==Q(1,n)  # delta*(Zthreshold/sqrt(delta))
print(json.dumps({'status':'PASS','scope':'Exact finite witnesses only; no stochastic/operator theorem','floor_remainder_cases':count,'nonzero_partial_cases':partial_count,'ordered_noncommuting_telescope_cases':1,'unit_error_not_product_closeness_cases':20,'moderate_density_scaling_cases':4},indent=2))
