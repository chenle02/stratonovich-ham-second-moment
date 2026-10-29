"""Exact fixed-lambda equality anchors; checks existing probes, not a new run."""
from fractions import Fraction as Q
import argparse
import hashlib
import itertools
import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
PAIRINGS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))


def exact(m,pairing,parameters):
    colors=[0]*m+[1]*(4-m)
    charged=[p for p,v in zip(pairing,parameters) if v]
    # All nonzero temporal charges must lie within one and the SAME chain.
    if any(colors[i]!=colors[j] for i,j in charged):
        return None
    if len({colors[i] for i,j in charged})>1:
        return None
    labels=[next(k for k,p in enumerate(pairing) if j in p) for j in range(4)]
    ABC=[Q(0),Q(0),Q(0)]
    qproduct=Q(1)
    for c in range(2):
        chain=[j for j in range(4) if colors[j]==c]
        for rank,j in enumerate(chain):
            q=1+sum(v for (i,k),v in zip(pairing,parameters)
                    if colors[i]==colors[k]==c and i<j<=k)
            qproduct*=q
            if rank==0:
                ABC[labels[j]]+=q
            elif labels[j]!=labels[chain[rank-1]]:
                ABC[2]+=q
    A,B,C=ABC
    return (A+B+C)/(4*(A+B)*(A+C)*(B+C)*qproduct)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=HERE/'lambda-15.json')
    parser.add_argument('--out',type=Path,default=HERE/'exact-anchors.json')
    args=parser.parse_args()
    data=json.loads(args.input.read_text())
    rows=[]
    for run in data['runs']:
        parameters=[Q(str(v)) for v in run['lambdas']]
        lookup={r['key']:r for r in run['diagrams']}
        for m,p in itertools.product(range(5),PAIRINGS):
            target=exact(m,p,parameters)
            if target is None:
                continue
            key=str(m)+':'+ '|'.join(''.join(map(str,pair)) for pair in p)
            r=lookup[key]
            rows.append(dict(lambdas=run['lambdas'],key=key,exact=str(target),
                             actual=r['actual'],shared=r['shared'],
                             actual_relative_error=r['actual']/float(target)-1,
                             shared_relative_error=r['shared']/float(target)-1,
                             difference=r['difference'],difference_se=r['difference_replicate_se']))
    assert len(rows)==129
    out=dict(status='Exact rational anchors with floating residuals;not certified enclosures',
             input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             anchors=rows,count=len(rows),
             max_actual_relative_error=max(abs(r['actual_relative_error']) for r in rows),
             max_shared_relative_error=max(abs(r['shared_relative_error']) for r in rows),
             max_equality_difference_in_reported_se=max(abs(r['difference'])/r['difference_se'] for r in rows))
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='anchors'},indent=2))


if __name__=='__main__':
    main()
