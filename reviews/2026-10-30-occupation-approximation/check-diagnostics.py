#!/usr/bin/env python3
"""Exact finite controls only; not a density/form/spectral/SPDE proof."""
from fractions import Fraction as F
import json
out={'scope':'Finite exact covariance/scaling and wrong-topology controls only; no density/form/spectral/SPDE proof','riesz_spreading':[],'white_time_cutoffs':[]}
# a=alpha=1/2,c_Gamma=1: interval self-energy is (8/3)*length^(3/2).
# psi_n=n^-5 1_(0,1)(t)1_(0,n^8)(x): exact powers have no float roots.
for n in [1,2,3,5,10]:
    R=n**8; amplitude=F(1,n**5)
    l2sq=amplitude**2*R
    mass=amplitude*R
    spatial=F(8,3)*amplitude**2*n**12
    variance=F(8,3)*spatial
    assert l2sq==F(1,n*n) and mass==n**3 and variance==F(64,9)*n*n
    out['riesz_spreading'].append({'n':n,'R':R,'amplitude':str(amplitude),'spacetime_L2_squared':str(l2sq),'spatial_mass':str(mass),'raw_variance':str(variance)})
# White alpha=1,a=1/2,unit spatial interval; raw variance=8/3.
previous=F(0)
for n in [1,2,3,5,10,100]:
    root=F(n,n+1);ell=root**2
    cost=F(8,3)*root**3
    normalized_cost=cost/ell**2
    assert previous<cost<F(8,3)<normalized_cost
    assert normalized_cost==F(8,3)/root
    out['white_time_cutoffs'].append({'n':n,'time_length':str(ell),'unrenormalized_cost':str(cost),'mass_renormalized_cost':str(normalized_cost),'limit_raw_cost':'8/3'})
    previous=cost
out['all_assertions_passed']=True
print(json.dumps(out,indent=2))
