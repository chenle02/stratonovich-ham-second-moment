# Author recheck of envelope010

Scope: current af97 P:envelope, main source LF1525–1600. This is an author
calculation and falsification check, not independent review or acceptance.
No source edit is needed. It retains the exact numerical majorant rather than
mistaking its lower bound for a lower bound on the second moment.

Write q=beta−1 and D=K exp(beta) (2/beta)^beta. For k≥1 the exact summand is

T_k(t) = (2k+1) P_k K^k exp(beta k) [2t/(beta k)]^(beta k).

Its factorial normalization is exactly

T_k(t) = D^k t^(beta k)/(k!)^q
         × (2k+1) [P_k/k!] [(k!) / k^k]^beta.

The factor P_k/k! is essential. A normalization retaining P_k rather than
P_k/k! introduces an extra factorial. Directly multiplying by(k!)^q and
using q=beta−1 proves the displayed identity without asymptotic notation.

P_2=3 and P_3=15 give the exact checks

T_2 (2!)^q / t^(2beta) = (15/2) D^2 (1/2)^beta,
T_3 (3!)^q / t^(3beta) = (35/2) D^3 (2/9)^beta.

For all k≥1, 1≤P_k/k!≤2^k, 1≤2k+1≤3^k and
exp(−beta k)≤[(k!)/k^k]^beta≤1. Thus a=D exp(−beta) and b=6D
suffice for the source's two factorial-series bounds. The k=0 term is1 on
each side. Since q>1, the upper series obeys the nonnegative l^q/l^1
comparison exp(q z^(1/q)). For z large, k=floor(z^(1/q)/2)≥1 gives
z^k/(k!)^q ≥ [z^(1/q)/k]^(qk) ≥2^(qk), establishing the matching
power z^(1/q). This is the numerical majorant's power beta/(beta−1),
strictly above beta/(3−alpha) because beta−1=3−alpha−alpha0.

The JSON log-domain checks test exact kth identities and uniform bounds at
k=2,3,4,6,10 for five beta values in(2,4). They are finite falsification
checks supporting the displayed algebra, not an analytic proof by sampling.
The upstream homogeneous source norm and marked-edge application remain
separately assigned own proofs; this calculation does not discharge them.
