"""Positive independent quadratures for the candidate middle-cross reduction.

Floating checks are not certified enclosures. Relative checks retain the
same1e-45threshold at60digits; tiny exponential components are rescaled.
"""
import hashlib
import json
from pathlib import Path
import mpmath as mp

HERE=Path(__file__).resolve().parent
mp.mp.dps=60


def actual(b,c):
    return (2*b*b+4*b*c+2*c*c-c+1)/(8*b*c*(b+1)*(2*b+1)*(b+c-1)*(2*b+2*c-1))


def resolvent(b,c,r):
    return (b+c+r+1)/(4*b*c*(c+1)*r*(b+c+r)*(b+r+1))


def upper(b,c):
    d,e=mp.sqrt(b*b+c*c-1),mp.sqrt(b*b+1)
    f1=(d+e+b+1)/(d*e*(b+d+1)*(b+e+1))
    f2=(d*d+d*e+e*e+(2*b+c+1)*(d+e)+(b+c)*(b+1))/(d*e*(b+c+d)*(b+c+e)*(b+d+1)*(b+e+1))
    return resolvent(b,c,e)+(f1+f2)/(4*b*c*(c+1)*(d+e))


def bridge(b,a,tau):
    r=mp.sqrt(b*b+2*a)
    return 2*(r+b)/(b*r*((r+b)**2+2*tau))


def bridge_difference(b,d,p,tau):
    # (T(d)-T(p))/(p-d), written with a positive polynomial numerator.
    C=b*b+2*tau
    num=d*p*(p+d+2*b)+b*(p*p+p*d+d*d+2*b*(p+d)+C)
    return 2*num/(b*d*p*((d+b)**2+2*tau)*((p+b)**2+2*tau))


def clock_positive(b,c):
    A=(c*c-1)/2;d=mp.sqrt(b*b+2*A)
    def f(z):
        s=(1+z*z)/2;tau=z*z/2;p=mp.sqrt(b*b+2*s)
        value=bridge(b,s,tau)+2*s/(d+p)*bridge_difference(b,d,p,tau)
        return value/(s*(s+A))
    return mp.quad(f,[0,1,mp.inf])/(16*mp.pi)


def triple_numeric(b,c,a):
    r=mp.sqrt(b*b+2*a);v=r+b
    return v/(2*mp.pi*b*r)*mp.quad(
        lambda z:1/((z*z+1)*(z*z+c*c)*(z*z+v*v)),[0,1,mp.inf])


def main():
    rows=[];triples=[];survival=[]
    for bx in ['1','2','11']:
        b=mp.mpf(bx)
        for ax in ['0','.5','1.5','60']:
            a=mp.mpf(ax)
            for dx in ['0','.1','4']:
                tau=mp.mpf(dx)
                numeric=mp.quad(lambda t:(b*b+2*a*t+2*tau*t*(1-t))**(-mp.mpf(3)/2),[0,1])
                value=bridge(b,a,tau);err=abs(value-numeric)/value
                assert err<mp.mpf('1e-45')
                rows.append(dict(b=bx,a=ax,tau=dx,closed=str(value),positive_quad=str(numeric),relative_error=str(err)))
        for cx in ['1','1.1','2','11']:
            c=mp.mpf(cx)
            for a in [mp.mpf(0),mp.mpf('.5'),(c*c-1)/2]:
                r=mp.sqrt(b*b+2*a);value=resolvent(b,c,r);numeric=triple_numeric(b,c,a)
                err=abs(value-numeric)/value;assert err<mp.mpf('1e-45')
                triples.append(dict(b=bx,c=cx,a=str(a),closed=str(value),positive_quad=str(numeric),relative_error=str(err)))
    for ax in ['.105','.5','1.5','60']:
        A=mp.mpf(ax)
        for sx in ['.5','.6','1.5','61']:
            s=mp.mpf(sx)
            for wx in ['0','.1','1','10']:
                w=mp.mpf(wx);slow=min(A,s)
                direct=mp.exp(-(A-slow)*w)+mp.quad(lambda t:A*mp.exp(-A*t-s*(w-t)+slow*w),[0,w])
                closed=(s*mp.exp(-(A-slow)*w)-A*mp.exp(-(s-slow)*w))/(s-A) if A!=s else 1+A*w
                err=abs(direct-closed)/closed;assert err<mp.mpf('1e-45')
                h=mp.mpf('.5');lo=min(A,h)
                uniform_scaled=(h*mp.exp(-(A-lo)*w)-A*mp.exp(-(h-lo)*w))/(h-A) if A!=h else 1+A*w
                uniform=uniform_scaled*mp.exp(-lo*w);value=closed*mp.exp(-slow*w)
                assert value<=uniform*(1+mp.mpf('1e-50'))
                survival.append(dict(A=ax,s=sx,w=wx,relative_error=str(err),value=str(value),uniform=str(uniform)))
    old=json.loads((HERE.parent/'2026-10-29-degree-four-clock-probe/lambda-refined-17.json').read_text())
    fixed=[]
    for run in old['runs']:
        lam,nu=map(mp.mpf,map(str,run['lambdas']));b,c=1+nu,1+lam
        I=actual(b,c);J=clock_positive(b,c);U=upper(b,c)
        if lam:assert J<U<I
        else:assert abs(J-I)/I<mp.mpf('1e-45') and abs(U-I)/I<mp.mpf('1e-45')
        v=next(q for q in run['diagrams']if q['key']=='1:02|13')
        fixed.append(dict(lam=str(lam),nu=str(nu),actual=str(I),clock_upper_positive_quad=str(J),survival_bound=str(U),old_sample_actual=v['actual'],old_actual_relative_error=str(mp.mpf(str(v['actual']))/I-1)))
    out=dict(status='PASS finite floating consistency;not an analytic proof/enclosure',dps=60,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             bridge_checks=rows,triple_checks=triples,survival_checks=survival,fixed_cases=fixed)
    HERE.joinpath('calibration.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'bridge':len(rows),'triple':len(triples),'survival':len(survival),'fixed':len(fixed),
                      'max_bridge_relative_error':str(max(mp.mpf(q['relative_error'])for q in rows)),
                      'max_triple_relative_error':str(max(mp.mpf(q['relative_error'])for q in triples))},indent=2))


if __name__=='__main__':
    main()
