"""Exact small-amplitude screen; scalar endpoint toy, outside target parameters."""
from fractions import Fraction as F
from math import factorial
import json

def mul(p,q):
    out={}
    for (a,b),v in p.items():
        for (c,d),w in q.items():
            if a+c+b+d<=4:
                key=(a+c,b+d);out[key]=out.get(key,F(0))+v*w
    return out

def add(p,q):
    out=dict(p)
    for k,v in q.items():out[k]=out.get(k,F(0))+v
    return out

def gaussian_even(k):
    assert k%2==0
    return F(factorial(k),2**(k//2)*factorial(k//2))

def expectation(p):
    out={}
    for (a,b),v in p.items():
        if a%2==0 and b%2==0:
            k=(a+b)//2
            out[k]=out.get(k,F(0))+v*gaussian_even(a)*gaussian_even(b)
    return out

c1={(j,0):F(1,factorial(2*j)) for j in range(5)}
s1={(j,0):F(1,factorial(2*j+1)) for j in range(5)}
c2={(0,j):F(1,factorial(2*j)) for j in range(5)}
s2={(0,j):F(1,factorial(2*j+1)) for j in range(5)}
z1={(1,0):F(1)}
u2=add(mul(c2,c1),mul(mul(s2,z1),s1))
single=expectation(mul(c1,c1));two=expectation(mul(u2,u2))
product={k:sum((v*w for a,v in single.items() for b,w in single.items() if a+b==k),F(0)) for k in range(3)}
assert single[0]==two[0]==1
assert single[1]==F(1,3) and two[1]==3
assert two[1]-product[1]==F(7,3)
print(json.dumps({'single_block_coefficients':{k:str(v) for k,v in single.items()},'two_block_coefficients':{k:str(v) for k,v in two.items()},'product_of_single_block_values_coefficients':{k:str(v) for k,v in product.items()},'first_order_gap':'7/3','status':'PASS','scope':'exact formal small-amplitude diagnostic,not analytic or stochastic-PDE proof; scalar spatially constant, piecewise-static temporal toy outside target covariance class'},indent=2))
