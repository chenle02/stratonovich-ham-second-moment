# Root source check before review

Authority: sources/chen-2026-author/aap-chen-2025.pdf, SHA-256
5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c.
Root visually inspected rendered PDF pages 10–12, 14–15, 22–23,
33–35, 37, 42, 60–61. Text extraction was navigation only.

- Pages 10–12: expansion, product identity (2.18), and expected Wick
  integrals (2.20)–(2.21). Lemma 2.5 supplies higher-Lp convergence
  for deterministic integrands, so tensor-product integrability is explicit.
- Page 14 explicitly permits either chain to have length zero.
- Page 15: Theorem 3.1 has factors 2 on Q1, equal Q0 and Q1 cardinalities,
  and even Q2. No additional sum over partitions Q is printed.
- Page 22: (4.4) is a limit of smoothed mixed expectations, not a bound.
- Page 34: the displayed single-kernel mass has exponent 2n; direct
  integration gives exponent 2. The subsequent product count uses exponent 2.
- Page 35: (5.3) explicitly states C independent of n and t; (5.4)
  inherits this assertion. The step uses theta=n/t in Lemma A.1.
- Pages 60–61: (A.3) is explicitly for large theta. It does not justify
  a uniform estimate down to theta=0.
- Page 37 prints the cross-reference (4.4) in Remark 5.1 as reported.
- Page 42: Remark 6.3 identifies the single-chain ordering limitation.

Independent first-order test, d=1 and gamma=delta_0, a=alpha_0:
G(s,x)=1/2 1_{|x|<s}, hence integral G(s,x)G(r,x)dx=min(s,r)/2.
The first-order square is
  E[S_1(t)^2]=t^(3-a)/[(1-a)(2-a)(3-a)].
Since 0<a<1, this refutes a uniform Ct^2 bound for this individual term.
The two order-(0,2) and (2,0) terms each equal half this value.
This does not refute the large-time exponential bound of Remark 5.1.

Root's proposed scope for review: test the complete written repair and
homogeneous envelope, not an intrinsic impossibility theorem for every
application of Theorem 3.1. No independent review has yet been completed.
