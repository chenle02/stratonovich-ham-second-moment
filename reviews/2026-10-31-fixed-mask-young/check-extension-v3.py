#!/usr/bin/env python3
"""Exact finite extension/Young-order controls, not a continuum wave model."""
from fractions import Fraction as F
from pathlib import Path
import json

def zero(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):
 a=zero(n,n)
 for i in range(n): a[i][i]=F(1)
 return a
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def power(a,n):
 out=eye(len(a))
 for _ in range(n):out=mul(a,out)
 return out
def lift(a,p,q):
 top=mul(a,p);cols=mul(a,q)
 return [r+s for r,s in zip(top,cols)]+zero(2,6)
A=zero(4,4);A[0][1]=F(1)
B=zero(4,4);B[1][2]=F(1)
P1=eye(4);P2=eye(4);P2[3][3]=F(0)
Q1=[[F(x) for x in row] for row in [[0,0],[1,0],[0,1],[2,3]]]
Q2=[[F(x) for x in row] for row in [[0,0],[1,0],[0,1],[-5,7]]]
Af,Bf=lift(A,P1,Q1),lift(B,P1,Q1)
assert Af==lift(A,P2,Q2) and Bf==lift(B,P2,Q2)
assert Af[0][4]==1 and Bf[1][5]==1  # constants have actual response columns
Af_dropped=[row[:] for row in Af];Bf_dropped=[row[:] for row in Bf]
for matrix in [Af_dropped,Bf_dropped]:
 for row in matrix:
  row[4]=row[5]=F(0)
assert Af_dropped[0][4]==0!=Af[0][4] and Bf_dropped[1][5]==0!=Bf[1][5]
assert all(x==0 for row in Af[4:]+Bf[4:] for x in row)
I=eye(6);AB=mul(Af,Bf);BA=mul(Bf,Af)
assert BA==zero(6,6) and AB!=BA and mul(AB,AB)==zero(6,6)
correct=mul(add(I,Bf),add(I,Af));wrong=mul(add(I,Af),add(I,Bf))
assert correct!=wrong
dropped_evolution=mul(add(I,Bf_dropped),add(I,Af_dropped))
constant_displacement=zero(6,1);constant_displacement[4][0]=F(1)
constant_velocity=zero(6,1);constant_velocity[5][0]=F(1)
assert mul(dropped_evolution,constant_displacement)==constant_displacement
assert mul(dropped_evolution,constant_velocity)==constant_velocity
assert mul(correct,constant_displacement)[0][0]==1
assert mul(correct,constant_velocity)[1][0]==1
assert mul(correct,constant_displacement)!=mul(dropped_evolution,constant_displacement)
assert mul(correct,constant_velocity)!=mul(dropped_evolution,constant_velocity)
assert all(correct[i]==I[i] for i in [4,5])
rows=[]
for k in [1,2,3,4,8]:
 e=F(1,k);N=k*k
 grid=[F(j,4*N) for j in range(4*N+1)]
 first_loop_coordinates=[(F(0),F(0)),(e,F(0)),(e,e),(F(0),e),(F(0),F(0))]
 dt=grid[1]-grid[0]
 assert e**4/dt**3==64*k*k
 derived_loop=I
 for j in range(4):
  dx=first_loop_coordinates[j+1][0]-first_loop_coordinates[j][0]
  dy=first_loop_coordinates[j+1][1]-first_loop_coordinates[j][1]
  derived_loop=mul(add(I,add(scale(dx,Af),scale(dy,Bf))),derived_loop)
 loop=mul(add(I,scale(-e,Bf)),mul(add(I,scale(-e,Af)),mul(add(I,scale(e,Bf)),add(I,scale(e,Af)))))
 assert loop==derived_loop==add(I,scale(-e*e,AB))
 endpoint=power(loop,N)
 assert endpoint==add(I,scale(F(-1),AB)) and endpoint!=I
 assert endpoint[0][5]==-1
 dropped_loop=mul(add(I,scale(-e,Bf_dropped)),mul(add(I,scale(-e,Af_dropped)),mul(add(I,scale(e,Bf_dropped)),add(I,scale(e,Af_dropped)))))
 dropped_endpoint=power(dropped_loop,N)
 assert mul(dropped_endpoint,constant_velocity)==constant_velocity
 assert mul(endpoint,constant_velocity)[0][0]==-1
 assert mul(endpoint,constant_velocity)!=mul(dropped_endpoint,constant_velocity)
 rows.append({'k':k,'loop_count':N,'time_segment_count':4*N,'time_segment_length':str(dt),'driver_coordinate_sup':str(e),
              'theta_three_quarters_seminorm_lower_to_fourth':str(e**4/dt**3),
              'endpoint_difference_e1_from_second_constant':'-1','dropped_endpoint_e1_from_second_constant':'0'})
# First-order actual d2 source positive-chain quadrature from accepted moment gate.
prior=Path(__file__).with_name('source-first-order-witness.json')
d=json.loads(prior.read_text())
w=d['row']
assert F(w['masked'])>0
out={'scope':'Exact rational finite block-extension/Young composition controls. E markers and constant markers are abstract direct-sum coordinates, NOT a finite-grid proof that continuum constants lie outside Sobolev E. No replacement SPDE or continuum certification.',
     'cutoff_independence':'PASS (inactive fourth coordinate and two different constant localization columns)',
     'constant_response_negative_control':'Explicit wrong dropped-column evolution fixes both constant vectors, while the correct chronological evolution produces e1/e2 response. Five repeated-loop endpoints disagree on the second constant vector.',
     'left_order_negative_control':'Chronological evolution (I+B)(I+A) differs from (I+A)(I+B).',
     'C0_only_negative_control':rows,
     'C0_scope':'Small supremum of the driving path alone does NOT imply Young solution convergence. Four-segment loops; theta=3/4 seminorm diverges. Target requires actual Ctheta convergence, theta>1/2.',
     'actual_source_first_order_quadrature_witness':w,
     'actual_source_witness_scope':'Accepted finite positive quadrature, original singular d2 source model. Strictly positive first-order response; no error-controlled continuum approximation.'}
Path(__file__).with_name('extension-controls-v3.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact cutoff/constant columns/left order and five C0-only negative controls; actual-source finite first-order witness retained.')
