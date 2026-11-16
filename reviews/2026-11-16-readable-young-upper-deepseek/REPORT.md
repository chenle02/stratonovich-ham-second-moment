# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

Both assigned proofs are read completely in their OLD and NEW versions, including the unchanged portions. I reconstruct every deduction below from public estimates. The NEW module is an expansion of the OLD module: the two statements are byte-identical, and the added sentences are explanatory rather than load-bearing changes. No new mathematical defect is found. The only reservations are pre-existing terseness points that also existed in OLD and are reconstructable.

The supplied baseline module (`integrated_constant_phase_young.tex`) is UNASSIGNED; I use its stated estimates only after checking their hypotheses, not its proofs. In particular `P:constant-young-linear`, `E:constant-young-estimate`, `E:constant-young-local` are imported results.

---

## L:young-upper-growth

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: see working below.

**Statement range.** OLD statement LF 14–26; OLD proof LF 28–54. NEW statement LF 14–26; NEW proof LF 28–79. Statement and equation labels `E:young-upper-refined-growth`, `E:young-upper-inverse-control` are unchanged.

### Step 1: applicability of the linear Young construction on a real Banach space

The module works on a nonzero real Banach space `\mathcal{X}` with the induced operator norm on `\mathcal{B}(\mathcal{X})`. The imported `P:constant-young-linear` is stated for `\mathcal{B}(F)` with `F` a Hilbert space, but its proof uses only:

- completeness of the path space, i.e. completeness of `C^\theta([0,B];\mathcal{B}(\mathcal{X}))` under the scaled norm;
- bounded bilinear operator multiplication `(P,Q)\mapsto PQ` with `\|PQ\|\le\|P\|\|Q\|`, i.e. constant `1`;
- the Young estimate `E:constant-young-estimate`.

All three transfer verbatim to `\mathcal{B}(\mathcal{X})`. Thus no Hilbert or finite-dimensional structure is imported. This meets the required check.

### Step 2: setting and local estimate

The proof fixes `c_\theta = 2\max(1,C_\theta)`, where `C_\theta` is the Young constant from `E:constant-young-estimate`, and uses the complete scaled norm

```
N_\ell(V) = sup_{a<=t<=a+ell} ||V(t)|| + ell^theta [V]_\theta.
```

The imported local bound `E:constant-young-local` is

```
N_\ell( int_a^.  dD V )
 <= c_\theta [D]_\theta ell^\theta N_\ell(V).
```

The contraction argument below only needs `[D]_\theta`, the Hölder seminorm, while the statement's `d = ||D||_\theta = sup_t ||D(t)|| + [D]_\theta` is the majorant appearing in the growth bound. Since `[D]_\theta <= d`, every contraction derived with `d` is valid.

### Step 3: small-driver regime

If

```
q0 := c_\theta d B^\theta <= 1/4,
```

then also `q := c_\theta [D]_\theta B^\theta <= q0 <= 1/4`.

The affine map `T(V) = I + \int_0^. dD V` has contraction ratio `q <= 1/4` in `N_B`. The fixed point `U_D` satisfies

```
N_B(U_D) <= N_B(I) + q N_B(U_D),
```

hence `N_B(U_D) <= 1/(1-q)`. Since `q <= q0`,

```
sup_t ||U_D(t)|| <= 1/(1-q0).
```

Now for `0 <= r <= 1/4`,

```
(d/dr)(-log(1-r)) = 1/(1-r) <= 4/3 <= 2,
```

so `-log(1-r) <= 2r`. The NEW proof's statement that the derivative is "at most two" is correct (indeed at most `4/3`). Hence

```
log sup_t ||U_D(t)|| <= 2 c_\theta B^\theta d.
```

This is the required linear logarithmic bound. Note it retains the linear term `d`, as the statement demands.

### Step 4: large-driver regime

Assume `c_\theta d B^\theta > 1/4`. Put

```
n_D = ceil( B (4 c_\theta d)^\nu ),
\nu = 1/\theta.
```

First, `x := B(4c_\theta d)^\nu > 1`: indeed the large-driver condition gives `4c_\theta d > B^{-\theta}`, and raising to power `\nu` with `\nu\theta = 1` gives `(4c_\theta d)^\nu > B^{-1}`, hence `x > 1`. Therefore `ceil(x) <= 2x`, so

```
n_D <= 2 B (4 c_\theta d)^\nu.
```

The equal-piece length is `ell = B/n_D`, so

```
ell <= 1/(4 c_\theta d)^\nu = (4 c_\theta d)^{-1/\theta}.
```

The NEW proof's equality `(4c_\theta d)^\nu = (4c_\theta d)^{1/\theta}` is correct since `\nu = 1/\theta`. The local contraction ratio satisfies

```
c_\theta [D]_\theta ell^\theta
 <= c_\theta d (4 c_\theta d)^{-1}
 = 1/4.
```

By the imported contraction theorem, each local solution started at `I` satisfies `N_\ell(Q) <= (4/3)||I|| = 4/3`, so in particular `sup||Q|| <= 4/3`. Composition over the `n_D` pieces gives

```
sup_t ||U_D(t)|| <= (4/3)^{n_D}.
```

Taking logarithms,

```
log sup_t ||U_D(t)||
 <= n_D log(4/3)
 <= 2 log(4/3) B (4 c_\theta)^\nu d^\nu.
```

This is the required `d^\nu` power bound, with no `d`-dependent prefactor beyond the exponent.

### Step 5: combination and the zero driver

The two regimes give exponents bounded respectively by `C_1 d` and `C_2 d^\nu`. Choosing one `c_{\theta,B}` large enough,

```
max( C_1 d, C_2 d^\nu ) <= c_{\theta,B}( d + d^\nu ),
```

so `E:young-upper-refined-growth` holds. Both `d` and `d^\nu = d^{1/\theta}` are retained.

At `d = 0`, `D\equiv 0`, so `U_D = I`; the bound is `1 = exp(0)` with no prefactor. The NEW proof's "without a prefactor" statement is correct.

### Step 6: uniform supermum bounds for evolution and inverse

On the ball `||H||_\theta <= K`, `K >= 1`, choose a uniform partition `0=t_0<...<t_n=B` with mesh `ell` so that `c_\theta K ell^\theta <= 1/4`. This is possible by taking `ell` small. The number of pieces is finite.

For each local factor `Q_j(r) = U_H(r,t_{j-1})` on `[t_{j-1},t_j]`:

- `N_\ell(Q_j) <= 4/3`, as above.
- `Q_j - I = \int_{t_{j-1}}^. dH Q_j`, so by `E:constant-young-local`,

```
N_\ell(Q_j - I)
 <= c_\theta [H]_\theta ell^\theta N_\ell(Q_j)
 <= (1/4)(4/3) = 1/3.
```

In particular `sup ||Q_j - I|| <= 1/3`. Hence `Q_j` is invertible with Neumann inverse

```
Q_j^{-1} = sum_{m>=0} (I - Q_j)^m,
||Q_j^{-1}|| <= sum_{m>=0} (1/3)^m = 3/2.
```

Composing the local factors along the time variable (right-to-left for the product representing `U_H(t,0)`), and reversing the order for the inverse, gives finite uniform bounds

```
M_U := sup_t ||U_H(t)|| <= (4/3)^n,
M_inv := sup_t ||U_H(t)^{-1}|| <= (3/2)^n.
```

This is valid for every `H` in the ball and gives the `C^0` control for both `U_H` and `U_H^{-1}`. No norm-differentiability of `H`, and no Hilbert or free-group structure, is used.

### Step 7: global forward Hölder bound

From `N_\ell(Q_j) <= 4/3` we get

```
ell^\theta [Q_j]_\theta <= 4/3,   [Q_j]_\theta <= (4/3) ell^{-theta}.
```

For `s<t`:

- **Within one piece** `[t_{j-1},t_j]`, writing `U_H(t)=Q_j(t)U_H(t_{j-1})` and `U_H(s)=Q_j(s)U_H(t_{j-1})`:

```
||U_H(t)-U_H(s)||
 <= ||Q_j(t)-Q_j(s)|| M_U
 <= [Q_j]_\theta (t-s)^\theta M_U
 <= (4/3) M_U ell^{-theta}(t-s)^\theta.
```

- **Crossing one boundary** `s<t_j<t`, split `U_H(t)-U_H(s) = [U_H(t)-U_H(t_j)]+[U_H(t_j)-U_H(s)]`. For the left term use `U_H(t)=Q_{j+1}(t)U_H(t_j)` and `Q_{j+1}(t_j)=I`, whence

```
||U_H(t)-U_H(t_j)||
 <= [Q_{j+1}]_\theta(t-t_j)^\theta M_U
 <= (4/3) M_U ell^{-theta}(t-t_j)^\theta.
```

Similarly

```
||U_H(t_j)-U_H(s)|| <= (4/3) M_U ell^{-theta}(t_j-s)^\theta.
```

Then

```
(t-t_j)^\theta + (t_j-s)^\theta
 <= 2^{1-\theta}(t-s)^\theta,
```

which is the estimate quoted in both OLD and NEW.

- **For `t-s >= ell`**, simply

```
||U_H(t)-U_H(s)|| <= 2 M_U
 <= 2 M_U ell^{-theta}(t-s)^\theta.
```

Therefore

```
[U_H]_\theta <= max((4/3)2^{1-\theta}M_U, 2M_U) ell^{-theta}
```

is finite. This reconstructs the terse OLD/NEW sentence "The same scaled estimate bounds local Hölder seminorms... For larger distances use `2 sup||U_H||/\ell^\theta`."

### Step 8: inverse Hölder bound

Using the identity displayed in both proofs,

```
U_H^{-1}(t)-U_H^{-1}(s)
 = - U_H^{-1}(t)(U_H(t)-U_H(s))U_H^{-1}(s),
```

we get

```
||U_H^{-1}(t)-U_H^{-1}(s)||
 <= M_inv^2 [U_H]_\theta (t-s)^\theta.
```

Hence `[U_H^{-1}]_\theta <= M_inv^2 [U_H]_\theta`. Combined with the finite supremum bounds, this proves

```
||U_H||_{C^\theta} + ||U_H^{-1}||_{C^\theta} <= L_{\theta,B,K} < \infty.
```

This is `E:young-upper-inverse-control`. The NEW proof's forward-reference to the inverse identity preceding the actual completion of the forward bounds is logically sound.

**Lost steps/qualifiers.** No lost step. Pre-existing terseness: the boundary-splitting Hölder argument is not fully expanded, and the imported local contraction `N_\ell(Q)<=4/3` is quoted without derivation. Both are reconstructed above.

---

## P:young-upper-multiplicative

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: see working below.

**Statement range.** OLD statement LF 62–72; OLD proof LF 74–100. NEW statement LF 87–97; NEW proof LF 99–155. The target bound is `E:young-upper-multiplicative`.

### Step 1: the conjugation operator and existence of `Z`

Put `U = U_H`, `R = U^{-1}`, and define `G(s)Z = R(s) Z U(s)` for `Z\in\mathcal{B}(\mathcal{X})`. By `L:young-upper-growth`, on the fixed ball `||H||_\theta <= K` the paths `U` and `R` are uniformly bounded in `C^\theta`. Concretely,

```
||G(s)||_{B(B(X))} <= ||R(s)|| ||U(s)|| <= L^2,
```

and

```
||G(s)-G(t)||
 <= ||R(s)-R(t)|| ||U(s)|| + ||R(t)|| ||U(s)-U(t)||,
```

so `[G]_\theta <= 2 L^2` and `||G||_{C^\theta}` is finite uniformly on the ball.

To justify the sandwich Young integral, use the standard Young/sewing viewpoint with increment

```
\delta_{s,t} := G(s)X_{s,t} = R(s) X_{s,t} U(s).
```

For `s<u<t`,

```
\delta_{s,t}-\delta_{s,u}-\delta_{u,t}
 = G(s)(X_{s,t}-X_{s,u}) - G(u)X_{u,t}
 = (G(s)-G(u))X_{u,t},
```

using `X_{s,t}-X_{s,u}=X_{u,t}`. Therefore

```
||\delta_{s,t}-\delta_{s,u}-\delta_{u,t}||
 <= [G]_\theta |u-s|^\theta [X]_\theta |t-u|^\theta
 <= [G]_\theta [X]_\theta |t-s|^{2\theta}.
```

Since `2\theta > 1`, the sewing condition holds, and the Young integral

```
Z(t) = \int_0^t R(s) dX(s) U(s)
```

exists with second-order remainder

```
Z_{s,t} = R(s) X_{s,t} U(s) + O(|t-s|^{2\theta}).
```

This uses only completeness of `\mathcal{B}(\mathcal{X})` and bilinear operator multiplication. It does not use smoothness of `X`; `X` is only `C^\theta`.

For the norm bound, the sewing estimate gives `|Z_{s,t}| <= M |t-s|^\theta + C N B^\theta |t-s|^\theta`, where `M = sup_s ||G(s)|| [X]_\theta` and `N = [G]_\theta[X]_\theta`; since `Z(0)=0`, the supremum of `Z` is controlled the same way. Therefore

```
||Z||_\theta <= L'_{\theta,B,K} x,
 x = ||X||_\theta,
```

as asserted. The constant `L'` depends only on `\theta,B,K` through the ball bounds for `U,R`, not on `X` or any dimension.

### Step 2: the conjugated evolution `V=U_Z`

By the imported `P:constant-young-linear` applied to the driver `Z`, `V=U_Z` exists and is `C^\theta`, with Young remainder

```
V_{s,t} = Z_{s,t} V(s) + O(|t-s|^{2\theta}).
```

Likewise, applied to `H` with integrand `U=U_H`,

```
U_{s,t} = H_{s,t} U(s) + O(|t-s|^{2\theta}).
```

### Step 3: exact product increment in left order

Let `P = U V`. Then exactly

```
P(t)-P(s)
 = (U(s)+U_{s,t})(V(s)+V_{s,t}) - U(s)V(s)
 = U_{s,t}V(s) + U(s)V_{s,t} + U_{s,t}V_{s,t}.
```

This is the NEW proof's displayed decomposition: `U(t)V(t)-U(s)V(s) = U_{s,t}V(s)+U(s)V_{s,t}+U_{s,t}V_{s,t}`. Since `U,V` are `C^\theta`, `||U_{s,t}||` and `||V_{s,t}||` are both `O(|t-s|^\theta)`, so the cross term is `O(|t-s|^{2\theta})`.

Substitute the two Young remainders:

```
P_{s,t}
 = [H_{s,t}U(s)+O(h^{2\theta})]V(s)
   + U(s)[Z_{s,t}V(s)+O(h^{2\theta})]
   + O(h^{2\theta}),
```

with `h=|t-s|`. Since `U(s),V(s)` are bounded (uniformly by the fixed-ball bounds), the `O(h^{2\theta})` terms remain `O(h^{2\theta})`. Hence

```
P_{s,t}
 = H_{s,t}P(s) + U(s)Z_{s,t}V(s) + O(h^{2\theta}),
```

because `P(s)=U(s)V(s)`. Now substitute `Z_{s,t}=R(s)X_{s,t}U(s)+O(h^{2\theta})`:

```
U(s)Z_{s,t}V(s)
 = U(s)R(s)X_{s,t}U(s)V(s) + O(h^{2\theta}).
```

The key noncommutative check is

```
U(s)R(s) = U_H(s)U_H(s)^{-1} = I,
```

so

```
U(s)R(s)X_{s,t}U(s)V(s) = X_{s,t}P(s),
```

without commuting `X_{s,t}` past `U(s)`. The order is preserved: the inverse is adjacent to `U(s)` on the left, and `X_{s,t}` remains in its original middle position. The NEW proof's sentence "the adjacent inverse factors cancel without commuting `X_{s,t}` past any operator" is therefore justified.

Collecting terms,

```
P_{s,t} = H_{s,t}P(s) + X_{s,t}P(s) + O(h^{2\theta})
        = (H+X)_{s,t}P(s) + O(h^{2\theta}).
```

This is exactly the intermediate equation in both OLD and NEW, including the cross term and the left-order cancellation.

### Step 4: partition remainder and uniqueness

Let `0=t_0<...<t_n=t` be a partition of `[0,t]\subseteq[0,B]` with mesh `m`. From Step 3, uniformly over all intervals,

```
|| P_{t_j,t_{j+1}} - (H+X)_{t_j,t_{j+1}}P(t_j) ||
 <= C h_j^{2\theta}.
```

For each interval,

```
h_j^{2\theta} = h_j h_j^{2\theta-1}
 <= h_j m^{2\theta-1},
```

because `2\theta-1>0`. The NEW proof's estimate "length to the power `2\theta` is at most its length times the mesh to the power `2\theta-1`" is correct. Summing:

```
sum_j h_j^{2\theta} <= m^{2\theta-1} sum_j h_j <= B m^{2\theta-1} -> 0,
```

precisely because `2\theta>1`.

Since `P` and `H+X` are `C^\theta`, the left Riemann–Young sums converge to the Young integral `\int_0^t d(H+X)P`. Hence

```
\int_0^t d(H+X)P
 = lim_n sum_j (H+X)_{t_j,t_{j+1}}P(t_j)
 = lim_n sum_j P_{t_j,t_{j+1}}
 = P(t)-P(0).
```

Since `P(0)=U(0)V(0)=I`, `P` is a `C^\theta` solution of the linear Young equation driven by `H+X`. By uniqueness in `P:constant-young-linear`, `P = U_{H+X}`. This is the product identity

```
U_{H+X} = U_H U_Z.
```

No smooth density in the full Hölder norm is invoked; only uniqueness among `C^\theta` solutions. The NEW proof's Step 2 correctly explains the vanishing of the remainder sum via `2\theta>1`.

### Step 5: refined growth applied to the perturbation driver and left multiplication by `A`

Apply `E:young-upper-refined-growth` to the driver `Z` alone, with `d_Z = ||Z||_\theta`:

```
sup_t ||U_Z(t)||
 <= exp{ c_{\theta,B}( d_Z + d_Z^\nu ) }.
```

Using `d_Z <= L'_{\theta,B,K} x`,

```
d_Z + d_Z^\nu
 <= L' x + (L')^\nu x^\nu
 <= C_{\theta,B,K}( x + x^\nu ),
```

since for every `x>=0` one can absorb `L'x` and `(L')^\nu x^\nu` into a single constant times `x+x^\nu`. This is the NEW proof's Step 3 claim and it is correct. The refined-growth lemma requires only `Z\in C^\theta`, `Z(0)=0`, the same horizon `B`, and the same `\theta,\nu`; all hold.

From the product identity,

```
A U_{H+X}(t) = A U_H(t) U_Z(t) = (A U_H(t)) U_Z(t),
```

and by submultiplicativity of the operator norm,

```
||A U_{H+X}(t)||
 <= ||A U_H(t)|| ||U_Z(t)||
 <= ||A U_H(t)|| exp{C_{\theta,B,K}(x+x^\nu)}.
```

This is `E:young-upper-multiplicative`. The deterministic endpoint factor `||A U_H(t)||` is left intact, not replaced by a separate bound. No inverse or lower bound for `A` is needed. The case `A=0` is immediate: both sides are `0`. When `x=0`, `X\equiv 0`, so `Z\equiv 0`, `U_Z = I`, and the inequality is an equality.

**Dependence.** The constant `C_{\theta,B,K}` depends on the Hölder exponent `\theta`, the horizon `B`, and the radius `K` of the fixed driver ball, and not on the size `x` of the perturbation or on the dimension. All arguments are pathwise deterministic inequalities; no stochastic moment bound or overlapping-block evolution is inferred, consistent with the stated requirements.

**Lost steps/qualifiers.** None lost. The standard sewing existence of the sandwich integral `\int R dX U` is not fully expanded in either OLD or NEW; the public check above fills it. This is a pre-existing terseness, not a NEW defect.

---

## AUDIT dispositions

- `L:young-upper-growth`: Old reading COMPLETE; New reading COMPLETE; public reconstruction COMPLETE; argument preservation PRESERVED; new explanations JUSTIFIED.
- `P:young-upper-multiplicative`: Old reading COMPLETE; New reading COMPLETE; public reconstruction COMPLETE; argument preservation PRESERVED; new explanations JUSTIFIED.
- Baseline context `integrated_constant_phase_young.tex` is UNASSIGNED; its proofs are not counted. Its imported estimates are used only after checking that their hypotheses hold in the real Banach space `\mathcal{X}`.
- The NEW proof's small-driver logarithm derivative claim, large-driver piece-length claim, partition-remainder interpolation `h^{2\theta} <= h m^{2\theta-1}`, and `x+x^\nu` conversion are all arithmetically verified.
- The required left-order noncommutative cancellation `U(s)R(s)=I` and the `2\theta>1` vanishing condition are both verified.

## Findings and limits

- **Preservation.** The NEW revision is substantively equivalent to the OLD revision: statements unchanged, the two target proofs enlarged but not weakened, and all new explanatory statements are correct under the same hypotheses, constants, domains, normalizations, and limits.
- **Pre-existing concerns, not rewrite defects.** (i) The sandwich Young integral `Z = \int U_H^{-1} dX U_H` is asserted to exist from the `C^\theta` property of `G`; the proof does not display the sewing condition. The condition is verified above. (ii) The forward global Hölder bound of `U_H` is stated tersely in both revisions; the local-factor/boundary-splitting derivation is checked above. (iii) The referenced no-go `P:nogo-26` and the imported `P:constant-young-linear` are external; only their checked statements/hypotheses are used here.
- **Context limits.** I did not verify the imported Friz–Hairer citation against the external source, did not review the unassigned baseline proofs, and did not certify any PDF/image/Lean/rendered-page correspondence or whole-book truth. The review is confined to the two assigned rewritten proof pairs and their unchanged statements/definitions.
- **No inference beyond scope.** The pathwise inequalities are deterministic. Nothing here produces or requires a stochastic moment bound or an overlapping-block evolution, and neither proof asserts one.

