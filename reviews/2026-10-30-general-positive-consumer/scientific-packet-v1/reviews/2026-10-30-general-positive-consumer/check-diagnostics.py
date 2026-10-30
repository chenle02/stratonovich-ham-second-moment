"""Exact finite cone/covariance controls; not a physical field evaluator."""
from fractions import Fraction as Q
import json

EPS=Q(1,1000000);THETA=Q(1,8);DECAY=Q(1,64)
def ell(z,lam):return (z[0]+z[1]/lam)/2
def step(z,lam,t,m):
 a=ell(z,lam);r=(z[0]-a,z[1]-lam*a)
 decay=1-(1-DECAY)*t
 err=EPS*t*((-1)**m)
 return (a+decay*r[0]+err*z[1],lam*a+decay*r[1]-err*z[0])
rows=[]
for N in [1,2,5,17,100]:
 z=(Q(1),Q(0));last=None
 for m in range(N):
  sigma=Q(m%3,100);lam=1+sigma/10
  z=step(z,lam,Q(1),m);a=ell(z,lam)
  rem=max(abs(z[0]-a),abs(z[1]-lam*a))
  assert a>0 and rem<=THETA*a
  if last is None:assert a>=Q(49,100)
  else:assert a>=Q(99,100)*last
  last=a
 for t in [Q(0),Q(1,4),Q(1)]:
  sigma=Q(N%3,100);lam=1+sigma/10
  final=step(z,lam,t,N)
  assert final[0]>=last/2
  rows.append({'N':N,'partial':str(t),'positive_terminal':True})
# Indexsigma0 has positive eigenphase slope1, not zero coupling.
assert 1+Q(0)/10==1
K=[[Q(3),Q(1)],[Q(1),Q(2)]]
G=[[Q(2),Q(1)],[Q(1),Q(3)]]
Psi=[[Q(1),Q(2)],[Q(3),Q(1)]]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def determinant(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
assert determinant(K)>0 and determinant(G)>0 and determinant(Psi)!=0
h=mul(mul(K,Psi),G)
v=sum(Psi[i][j]*h[i][j] for i in range(2) for j in range(2))
quad=sum(Psi[i][a]*K[i][j]*G[a][b]*Psi[j][b] for i in range(2) for j in range(2) for a in range(2) for b in range(2))
assert v==quad>0
wrong_profile_L2=sum(h[i][a]**2 for i in range(2) for a in range(2))
assert wrong_profile_L2!=v
qavg=[sum(Psi[i][a] for i in range(2)) for a in range(2)]
Uavg=[sum(G[a][b]*qavg[b] for b in range(2)) for a in range(2)]
assert all(h[i][a]>=Uavg[a] for i in range(2) for a in range(2))
assert v>=sum(qavg[a]*Uavg[a] for a in range(2))>0
rank1=[[qavg[a]/2 for a in range(2)] for i in range(2)]
h1=mul(mul(K,rank1),G)
v1=sum(rank1[i][a]*h1[i][a] for i in range(2) for a in range(2))
assert v1!=v
print(json.dumps({'status':'PASS','scope':'Finite normalized cone and Gaussian-test-coordinate covariance algebra ONLY; neither family is asserted to be a physical HAM discretization','cone_parameters':{'epsilon':str(EPS),'aperture':str(THETA),'normalized_decay':str(DECAY),'sigma_m':'(m mod3)/100','lambda_sigma':'1+sigma/10','phase':'R2 sup norm, e=(1,lambda),ell=(v+w/lambda)/2','initial':['1','0'],'operator':'Pi+decay(t)*(I-Pi)+signed epsilon*t skew error','full_step_t':'1'},'cone_cases':rows,'covariance':{'K':[[str(x) for x in y] for y in K],'G':[[str(x) for x in y] for y in G],'Psi':[[str(x) for x in y] for y in Psi],'raw_variance':str(v),'rank1_replacement_variance':str(v1),'wrong_profile_L2_cost':str(wrong_profile_L2),'direct_covariance_matches':True}},indent=2))
