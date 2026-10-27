"""Floating cross-checks, not certified quadrature or proof.
Run: uv run --with numpy --with scipy python <this file>.
"""
import numpy as np
from scipy.stats import qmc
from scipy.integrate import quad
from math import factorial
from fractions import Fraction
import json

def F(a,b,c):
    return 4*a*b-np.maximum(a+b-c,0)**2+np.maximum(np.abs(a-b)-c,0)**2

refs=['1/2880','1/8640','1/5760','1/576','29/34560','1/640','1/144','1/480','31/17280']
runs=[]
for seed in (271,828):
    x=qmc.Sobol(4,scramble=True,seed=seed).random_base2(18)
    s=np.sort(x,axis=1); a,b,c,d=np.diff(np.c_[np.zeros(len(x)),s],axis=1).T
    vals=[a*c/4,a*np.minimum(np.minimum(b,c),d)/4,a*np.minimum(b,d)/4]
    result=[float(v.mean()/factorial(4)) for v in vals]
    r=x[:,0]; s=np.sort(x[:,1:],axis=1); a,b,c=np.diff(np.c_[np.zeros(len(x)),s],axis=1).T
    vals=[np.minimum(r,a)*b/4,F(r,a,np.minimum(b,c))/16,F(r,a,c)/16]
    result += [float(v.mean()/factorial(3)) for v in vals]
    s=np.sort(x[:,:2],axis=1); a,b=np.diff(np.c_[np.zeros(len(x)),s],axis=1).T
    s=np.sort(x[:,2:],axis=1); c,d=np.diff(np.c_[np.zeros(len(x)),s],axis=1).T
    vals=[a*c/4,np.minimum(a,c)*np.minimum(b,d)/4,F(a,c,np.minimum(b,d))/16]
    result += [float(v.mean()/4) for v in vals]
    runs.append({'seed':seed,'samples':len(x),'estimates':result,'relative_errors':[z/float(Fraction(r))-1 for z,r in zip(result,refs)]})
# Independent transformed two-dimensional triangular integration for Riesz I11,
# compared with the integrated one-dimensional formula at alpha=alpha0=1/2,c=1.
a=0.5; a0=0.5
one=quad(lambda u: 2*(((2-u*u)**(3-a)-(u*u)**(3-a))/(2*(3-a))-(1-u*u)*(u*u)**(2-a)),0,1,epsabs=1e-12)[0]/((1-a)*(2-a))
two=quad(lambda u: quad(lambda r:2*((2*r+u*u)**(2-a)-(u*u)**(2-a)),0,1-u*u,epsabs=1e-12)[0],0,1,epsabs=1e-12)[0]/((1-a)*(2-a))
print(json.dumps({'status':'floating checks only; randomized Sobol errors are empirical, not rigorous error bars','static_references':refs,'runs':runs,'riesz_order2':{'alpha':a,'alpha0':a0,'c_alpha':1,'integrated_formula':one,'direct_triangle':two,'absolute_difference':abs(one-two)}},indent=2))
