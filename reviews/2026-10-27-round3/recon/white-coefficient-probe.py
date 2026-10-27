#!/usr/bin/env python3
"""Bounded importance probe of white Stratonovich order-four coefficients.
Run: uv run --with numpy python white-coefficient-probe.py --output FILE
This is floating statistical evidence, not certified integration or a proof.
"""
import argparse
from fractions import Fraction
from pathlib import Path
import json
import math
import numpy as np

LABELS = ['04-A','04-B','04-C','13-A','13-B','13-C','22-A','22-B','22-C']
STATIC = ['1/2880','1/8640','1/5760','1/576','29/34560','1/640','1/144','1/480','31/17280']
# Each vertex selects a pair-color and one of that pair's two endpoints.
PAIRINGS = [((0,0),(0,1),(1,0),(1,1)),
            ((0,0),(1,0),(0,1),(1,1)),
            ((0,0),(1,0),(1,1),(0,1))]


def event(base, gap, orientation, spatial, vertices, split):
    """Original ordered-chain and Green-cone test; no sorting of vertices.

    A time is represented by base[color] + flag*gap[color]. For vertices
    of the same color we subtract the flags FIRST. Thus a positive gap
    of 1e-50 is retained even when base + gap rounds to base in float64.
    """
    n = len(base)
    mask = np.ones(n, dtype=bool)
    colors = [v[0] for v in vertices]
    flags = [orientation[:,c] if endpoint == 0 else 1-orientation[:,c]
             for c, endpoint in vertices]
    for chain in (range(0, split), range(split,4)):
        previous = None
        for j in chain:
            c = colors[j]
            if previous is None:
                dt = base[:,c] + flags[j]*gap[:,c]
                dx = spatial[:,c]
            else:
                p = previous
                cp = colors[p]
                if c == cp:
                    dt = (flags[j]-flags[p])*gap[:,c]
                    dx = np.zeros(n)
                else:
                    dt = ((base[:,c]-base[:,cp])
                          + flags[j]*gap[:,c]-flags[p]*gap[:,cp])
                    dx = spatial[:,c]-spatial[:,cp]
            mask &= (dt > 0) & (np.abs(dx) < dt)
            previous = j
    return mask


def wilson(count, n, z=1.959963984540054):
    p = count/n
    d = 1+z*z/n
    mid = (p+z*z/(2*n))/d
    width = z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return [max(0.,mid-width), min(1.,mid+width)]


def ratio_summary(means, covariance, i, j, n):
    ratio = means[i]/means[j]
    variance = (covariance[i,i] + ratio*ratio*covariance[j,j]
                - 2*ratio*covariance[i,j])/(n*means[j]*means[j])
    se = math.sqrt(max(0.,variance))
    return {'estimate':float(ratio), 'delta_method_standard_error':se,
            'normal_95_interval':[float(ratio-1.96*se),float(ratio+1.96*se)],
            'uses_within_draw_covariance':True}


def run(a, n, seed, chunk):
    rng = np.random.default_rng(seed)
    counts = np.zeros(9,dtype=np.int64)
    sums = np.zeros(3)
    products = np.zeros((3,3))
    pair_collapses = 0
    zero_gaps = 0
    min_gap = math.inf
    # Metrics per draw are (a2, A2, D2), with the common Z^2/4 removed.
    for start in range(0,n,chunk):
        size = min(chunk,n-start)
        h = rng.beta(1-a,2,size=(size,2))
        lower = rng.random((size,2))*(1-h)
        flip = rng.integers(0,2,size=(size,2),dtype=np.int8)
        x = rng.uniform(-1,1,size=(size,2))
        pair_collapses += int(np.count_nonzero((lower+h)==lower))
        zero_gaps += int(np.count_nonzero(h==0))
        min_gap = min(min_gap,float(h.min()))
        events = np.column_stack([event(lower,h,flip,x,D,m)
                                  for m in (0,1,2) for D in PAIRINGS])
        counts += events.sum(axis=0,dtype=np.int64)
        one = events[:,:3].sum(axis=1)
        mixed = events[:,3:6].sum(axis=1)
        diagonal = events[:,6:].sum(axis=1)
        metrics = np.column_stack((one,2*one+2*mixed+diagonal,diagonal)).astype(float)
        sums += metrics.sum(axis=0)
        products += metrics.T @ metrics
    Z = 2/((1-a)*(2-a))
    factor = Z*Z/4
    means = sums/n
    covariance = (products - n*np.outer(means,means))/(n-1)
    diagrams=[]
    for label,count,reference in zip(LABELS,counts,STATIC):
        p = count/n
        item={'diagram':label,'event_count':int(count),'event_probability':float(p),
              'coefficient_estimate':float(factor*p),
              'binomial_standard_error':float(factor*math.sqrt(p*(1-p)/n)),
              'wilson_95_interval':[factor*z for z in wilson(int(count),n)]}
        if a==0:
            exact=float(Fraction(reference))
            true_p=exact/factor
            item.update({'static_exact':reference,
                         'z_against_exact':float((factor*p-exact)/(factor*math.sqrt(true_p*(1-true_p)/n)))})
        if label in ('04-A','22-A'):
            if label == '04-A':
                exact = math.exp(2*(math.lgamma(1-a)-math.log(2))
                                 - math.lgamma(1+2*(3-a)))
            else:
                exact = 1/(4*((1-a)*(2-a)*(3-a))**2)
            true_p = exact/factor
            item['analytic_control'] = {
                'formula': '[Gamma(1-a)/2]^2/Gamma(1+2(3-a))' if label == '04-A'
                           else '1/[4((1-a)(2-a)(3-a))^2]',
                'exact_formula_float_evaluation':exact,
                'z_against_formula':(factor*p-exact)/(factor*math.sqrt(true_p*(1-true_p)/n))}
        diagrams.append(item)
    output={'alpha0':a,'seed':seed,'samples':n,'Z':Z,'factor':factor,
            'diagrams':diagrams,
            'aggregates':{name:{'estimate':float(factor*means[j]),
                                'standard_error':float(factor*math.sqrt(covariance[j,j]/n))}
                          for j,name in enumerate(('a2','A2','D2'))},
            'A2_over_a2':ratio_summary(means,covariance,1,0,n),
            'D2_over_a2':ratio_summary(means,covariance,2,0,n),
            'per_draw_metric_covariance':covariance.tolist(),
            'floating_diagnostics':{'naively_collapsed_pair_times':pair_collapses,
                                    'number_of_sampled_pairs':2*n,
                                    'zero_beta_gaps':zero_gaps,
                                    'minimum_beta_gap':min_gap,
                                    'same_pair_gap_subtraction':'direct signed gap; no L+h minus L'},
            'rare_event_min_count':int(counts.min())}
    return output


def controls():
    base=np.array([[.25,.5]])
    gap=np.array([[1e-50,1e-50]])
    flip=np.array([[0,0]],dtype=np.int8)
    spatial=np.array([[.1,-.1]])
    # Domestic pairs are (1,2),(3,4); on split22 each second vertex must
    # remain strictly later, even though the pair's stored floats coincide.
    assert (base+gap==base).all()
    assert bool(event(base,gap,flip,spatial,PAIRINGS[0],2)[0])
    return {'tiny_gap_control':'PASS','gap':1e-50,
            'normalization':'Beta(1-a,2), uniform lower endpoint, fair orientation give |s-r|^-a/Z; two spatial colors have density1/4 and four Green factors1/16, hence J=Z^2/4*P(event)'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    parser.add_argument('--power',type=int,default=22)
    parser.add_argument('--chunk-power',type=int,default=16)
    args=parser.parse_args()
    out={'status':'Unreviewed floating statistical probe; not certified integration or asymptotic evidence',
         'normalization_control':controls(),
         'correlation':'Within each draw all nine diagrams reuse the same two covariance-pair times and two spatial colors. Draws and parameter runs are independently generated. Aggregate and ratio errors use the observed within-draw covariance.',
         'error_scope':'Individual Wilson intervals assume ideal IID Bernoulli draws; ratio intervals use an asymptotic delta method. PRNG and floating arithmetic are not certified. Intervals are pointwise, not simultaneous across diagrams or parameters.',
         'runs':[]}
    for i,a in enumerate((0.,.25,.5,.75,.9)):
        result=run(a,2**args.power,2026102700+i,2**args.chunk_power)
        out['runs'].append(result)
        print(json.dumps({'a':a,'min_count':result['rare_event_min_count'],
                          'A2/a2':result['A2_over_a2'],
                          'D2/a2':result['D2_over_a2']}),flush=True)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    main()
