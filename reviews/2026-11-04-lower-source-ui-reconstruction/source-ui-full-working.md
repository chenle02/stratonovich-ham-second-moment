# Same-noise source, Young uniform integrability, and the two moment passages

Author reconstruction, 2026-11-04, science af97. Assigned deductions095/102/103/110 and consumers125/189. Prerequisites remain CURRENT OWN inputs as qualified in the clause table; no full-parent acceptance or review vote. Whole214/240/13 and native INCONCLUSIVE are unchanged.

## 1. Fixed data and the retaining coupling

Write a=α₀. Retain H:homog exactly: d=1,2,3; 0<a<1; nonnegative even positive-definite tempered Radon Γ, with positive even tempered spectral measure μ and Γ(cA)=c^(d−α)Γ(A); 0<α<d or α=d=1; a+α<2. No angular or spatial spectral density is assumed. Every positive covariance amplitude is retained. Γ=0 is treated separately below. Fix finite R,T and physical mask 0≤m≤1, compact smooth, applied to the field AFTER spatial regularization. Choose

    0<γ<min(1/2,(2−α)/2),
    1/2<θ<β<min(1−a/2,(3−a−α)/2).

Here β is driver regularity. Constants depend on fixed parameters, amplitude and cutoffs; none are claimed uniform in growing R,T,N or δ→0.

Let H_W be the raw covariance quotient completion, W the given isonormal process, Bθ=Cθ([0,T];B(E)), E=H½×H⁻½. OWN085–093 supply real smooth test ONB f_j, actual coefficients A_j(t), and

    M_N=Σ(j≤N) W(f_j)A_j → M in every finite Lᵖ(Bθ),
    || ||M||Bθ ||Lᵖ ≤ K√p, p≥2.

Its row is the literal completed test h=m 1_(0,t)v_zG_w with the actual Sobolev adjoint, both phase entries/Bessel orientations and continuous zero-frequency sine quotient (named OWN input).

OWN096–098 use heat contraction Cε, multiplier exp(−ε|ξ|²/2), also for Radon Γ. In feature space G with temporal measure λ^(a−1)dλ/Γ_E(a),

    (ℱf)(λ,r)=√(2λ) ∫(t>0,t≥r) exp(−λ(t−r)) f(t,·)dt.

The r-integral equals exp(−λ|t−s|), then λ-integration gives |t−s|^(−a). On the extension I(ℱf)=W(f) literally; extra independent noise acts only on (ran ℱ)⊥. Set Pη=1_(λ≤η⁻¹), Qρ=CεPη, Yρ(f)=I(Qρℱf). Then Dρ=W−Yρ=I((I−Qρ)ℱf) on the same space. Orthogonal splitting gives

    ||(I−Qρ)g||² = ||(I−Pη)g||² + ||Pη(I−Cε)g||² ≤ ||g||².

Both source and residual variances are ≤||f||H_W². Moreover

    ||(I−Qρ)g|| ≤ ||(I−Cε)g|| + ||(I−Pη)g|| →0

at arbitrary relative positive width rates. Source and residual are correlated; neither their independence nor independence of sources is used. Positive-width pointfields have joint covariance

    Cov(Yεη(t,x),Yε'η'(s,y))
      = K_max(η,η')(t−s) Γ_(ε+ε')(x−y),
    Kη(v)=Γ_E(a)⁻¹ ∫₀^(η⁻¹) exp(−λ|v|) λ^(a−1)dλ,
    Γ_e=p_e*Γ.

Single-source spatial width is 2ε. Sources may use auxiliary noise; the raw limit is W-measurable. No rough time slice is used.

## 2. PROOF095: actual operator transfer and joint convergence

For a centered Gaussian Y with Var Y(f)≤C||f||², the variance bound first annihilates covariance-null tests and extends Y continuously H_W→L². For any finite real coefficients t_j,

    Var Σt_jY(f_j) ≤ C Σt_j²,

so its covariance matrix is ≤CI, although its coordinates need not be independent. If v_j are deterministic Banach-space vectors, x↦||Σx_jv_j||ᵖ is convex for p≥1. Add an independent Gaussian of covariance CI−Cov(Y(f_j)) ONLY in this finite comparison. Conditional Jensen gives

    ||ΣY(f_j)v_j||Lᵖ ≤ √C ||ΣW(f_j)v_j||Lᵖ.

Apply to successive coefficient tails A_j in Bθ. Completeness gives the actual limit M_Y, with

    ||M_Y−M_Y,N||LᵖBθ ≤ √C ||M−M_N||LᵖBθ,
    ||M_Y||LᵖBθ ≤ √C ||M||LᵖBθ.

Limits lie in the separable coefficient-path span and hence are strongly measurable. A uniform subsequence passes compact values at every time; scalar Gaussian limits retain Gaussianity. Finite rows Y(P_Nh) converge to Y(h). Dense Schwartz pairs/rational times and continuity give actual version/basis independence and linearity. No filter is commuted through m or the wave group.

For jointly Gaussian W,Yρ let Dρ=W−Yρ, with uniform residual variance bound C_D. Put t_N,p=||M−M_N||LᵖBθ and s_N(ρ)=Σ(j≤N)Var Dρ(f_j). The finite residual covariance matrix has operator norm at most its trace s_N. Thus the quantitative error is

    ||M_Yρ−M||LᵖBθ
       ≤ √C_D t_N,p + √s_N(ρ) ||M_N||LᵖBθ.             (1)

Choose N first, then remove widths for that finite head. For finitely many global/local pullbacks, max≤sum of their errors(1) proves JOINT convergence with original correlations. Retaining source/residual constants equal1, so full-path √p bounds are uniform in widths at fixed parameters.

## 3. Both F columns, ordinary primitives, and quantitative UI

F=E⊕R², ||(e,c₁,c₂)||²=||e||E²+c₁²+c₂², interpreted as (e₁+c₁,e₂+c₂). E is closed and proper, not dense. The free group is

    S_F(t)(e,c₁,c₂)=(S_E(t)e,c₁+t c₂,c₂).

Choose the source's auxiliary ψ=1 on the enlarged localization of M, and Lψ(e,c₁,c₂)=ψe+(c₁ψ,c₂ψ)∈E. The two-sided localization DχM=M=MDχ holds coefficientwise and hence for all transferred paths. Define A=iMLψ, Aρ=iM_YρLψ. The cutoff choice is immaterial since Dχ(Lψ−Lψ')=0. Thus,

    A(0,1,0)=iM(ψ,0),   A(0,0,1)=iM(0,ψ),
    Ai=iM,   π_CA=0,
    ||Aρ−A||LᵖCθ ≤ ||Lψ|| ||M_Yρ−M||LᵖCθ →0.        (2)

Bounded composition transfers joint convergence and all Gaussian norm bounds for BOTH constant columns.

At positive width b(t)=mYρ(t) is continuous in time and compact smooth in space, with bounded derivatives on the finite horizon (OWN099). Define B_F(b)(e,c₁,c₂)=(0,b(e₁+c₁))∈E. Then

    ||B_F(b)||F→E ≤ ||b||∞+||b||₂.

The actual ordinary primitive is statewise

    A_Eρ(t)z=∫₀ᵗ S_E(−r) B_F(b(r)) S_F(r)z dr.        (3)

For E data, the Sobolev adjoint row gives ∫b v_zG_w; the point-feature integral equals Yρ(h). Approximate its time indicator in the raw norm and in time-L² spatial-supremum norm on common compact support. Bounded point-feature norms pass both integrals to the same L² variable. Countably many dense states/rational times extend the equality to all E data/times. To reach either constant column, free finite propagation makes z and iLψz equal near supp m throughout the horizon; multiplying by b kills their difference. This proves (3) on F, rather than claiming density. It is operator-norm Lipschitz by the displayed B_F bound and finite-horizon group bounds; no operator-norm derivative of S_E or S_F is asserted.

The needed Young estimates are quantitative. Banach Young integration applies to θ>1/2 and bounded operator multiplication (constant one). On an interval of length ℓ use Nℓ(V)=sup||V||+ℓ^θ[V]θ. Its integral map obeys

    Nℓ(∫dD V) ≤ cθ[D]θ ℓ^θ Nℓ(V).

Choose cθKℓ^θ≤1/4 when ||D||Cθ≤K. Contraction yields Nℓ(U)≤2 times its initial norm; subtraction yields local Lipschitz dependence, and patching ≤C_T(1+||D||Cθ^(1/θ)) pieces gives

    ||U_D||triangle ≤ C_T exp(C_T(1+||D||Cθ)^ν),
    ν=1/θ∈(1,2).                                     (4)

Invertibility follows from ||U−I||≤1/3 on each piece, then composition. The imported estimate is Friz–Hairer Sections1.4–1.5/4.1, (4.3), pp13/61–62; no nonlinear flow theorem or Theorem11.6 is invoked.

If Xρ=||Aρ||Cθ satisfies ||Xρ||Lᵖ≤K√p, then E Xρ^(2n)≤K^(2n)(2n)^n and n!≥(n/e)^n give

    supρ E exp(c₀Xρ²)<∞ whenever 2ec₀K²<1.            (5)

This also holds for X₀=||A||. On the common driver ball of radius K', (2) and local Young Lipschitz give convergence of Uρ in probability; explicitly

    P(||Uρ−U||triangle>ε)
     ≤2H exp(−c₀K'²)+(L_K'/ε)^q E||Aρ−A||Cθ^q.

Take widths→0 at fixed K', then K'→∞. For every finite r, since ν<2 there is C_r with rC_T(1+x)^ν≤c₀x²+C_r. Equations(4),(5) therefore give uniform r-th flow moments on the ORIGINAL unweighted measure. For Vρ=||Uρ−U||triangle,

    E Vρᵖ ≤ εᵖ+(E Vρ^(2p))½ P(Vρ>ε)½ → εᵖ.

Then ε↓0 proves every finite Lᵖ convergence. This proves UI on the original measure, without square-exponential flow moments or a tilted source limit. Physical Pρ(t,s)=S_F(t)Uρ(t,s)S_F(−s) obeys

    ||Pρ−P||bounded-triangle ≤ C_T² ||Uρ−U||triangle.   (6)

The norm is on bounded families, not norm-continuous physical paths. Separability and bounded conjugation give measurable norms; closed isometric restriction gives E-flow convergence. No growing-R,T F-bound is claimed.

## 4. PROOF102: ordinary scalar Picard, two-point Wick comparison, Bochner average

At fixed positive widths the coefficient is sample-bounded by M on any compact backward cone. With G_d the positive Green MEASURE, mass G_d(r,R^d)=r, ordered chain mass obeys

    M₀(t)=1, M_n(t)=∫₀ᵗ(t−s)M_(n−1)(s)ds=t^(2n)/(2n)!.

Hence each scalar Picard term is ≤M^nT^(2n)/(2n)!, uniformly on that cone. The series solves the continuous ordinary mild equation, data(1,0). A difference is bounded by B M^nT^(2n)/(2n)!→0. This proves only positive-width ordinary uniqueness.

The stochastic integral at each order is a Bochner L² integral. Gaussian Hölder bounds its integrand by √((2n−1)!!) Vρ^(n/2), with Vρ=Kη(0)Γ_2ε(0)<∞. This bound times the finite chain mass justifies expectation/Fubini. Wick differentiating the Gaussian moment generating function produces ALL unordered pairings with coefficient one; self-pairs, unequal chains and the empty chain stay. Symmetrization adds no n! or m!n! factor (OWN049). Multiplying each vertex by m∈[0,1] reduces every nonnegative covariance product, since Kη and Γ_2ε are nonnegative. Thus, termwise,

    0≤E[Xρ,n^m(t,x) Xρ,k^m(t,y)]
       ≤E[Xρ,n(t,x) Xρ,k(t,y)].                       (7)

The width-uniform OWN008 bound, after OWN101 comparison, is

    ||Xρ,n^(m)(t,x)||₂≤q_n(t)
      =e^(θ₀t) C^(n/2)t^n/√(n!),  q₀=e^(θ₀t),
    Q_T=Σq_n(T)<∞.

Its ratio tends to zero, including Σ√(n+1)q_n(T). Therefore the series converges absolutely in L², and Σ(n,k)E|Xρ,n^(m)(x)Xρ,k^(m)(y)|≤Q_t². Products of partial sums converge in L¹; (7) passes to full fields. Only the unmasked source is spatially stationary, so Cauchy–Schwarz gives

    0≤E[uρ^m(t,x)uρ^m(t,y)]≤E|uρ(t,0)|².              (8)

Gaussian increments/product bounds give finite-order L² spatial continuity; uniform q_n tails pass it to the sum. Its separable L² image is bounded by Q_t, proving Bochner integrability against compact smooth φ. For φ≥0,

    E|Bρ|² ≤ ||φ||₁² E|uρ(t,0)|²,
    Bρ=∫φ(x)uρ^m(t,x)dx.                              (9)

Absolute Fubini is bounded by ||φ||₁²Q_t². This requires φ≥0, not pathwise solution order, velocity comparison, arbitrary-phase PSD order or independent chains. For d=3 use the actual sphere measure: first smooth Green at FIXED noise widths, remove that smoothing by bounded continuous Wick products and unchanged masses, then remove noise widths. This is measure integration, not integration against a nonexistent Green density.

## 5. PROOF103: canonical point moment without reconstructing a rough field

At each fixed pair of orders, the current source covariance is exactly the vertexwise convention of OWN006. Reverse each terminal chain at its common horizon, s'_j=t−s_(n+1−j), z'_j=−z_(n+1−j) (or translate the terminal point first). Even time/spatial covariance removes sign changes, and labels give a bijection on ALL pairings, including empty chains. OWN006 supplies the joint noise-width limit for each diagram: spatial convergence at fixed temporal cutoff, followed by the temporal tail bound uniform in all spatial widths. That tail is C_(k,T₁,T₂)(N₁^(1/η)(1)+N₂^(1/η)(1)²)→0. Its squeeze permits arbitrary relative rates; it is not a diagonal-only limit.

Consequently E[Xρ,n(t,0)Xρ,k(t,0)]→E[X_n(t,0)X_k(t,0)] with the original canonical chain conventions (OWN002/006). Choose N with Σ_(n>N or k>N)q_n(t)q_k(t)<ε. Both source and canonical double-series tails are ≤ε. The finite square tends to its limit; then ε↓0 yields

    E|uρ(t,0)|² → E|u(t,0)|².                         (10)

This is the existing canonical L² series; no rough PDE uniqueness is used. If Bρ→Z in L², then

    |E|Bρ|²−E|Z|²|≤||Bρ−Z||₂ (||Bρ||₂+||Z||₂)→0.

Equations(9),(10) give E|Z|²≤||φ||₁²E|u(t,0)|². Bρ→Z remains a separate premise. We use independent008/006, not050 with a scaled-moment premise inferred circularly from final C2.

## 6. PROOF110: actual F observable equals the Bochner average

For φ≥0, smooth compact, ∫φ=1, define

    Oφ(e,c₁,c₂)=〈e₁,φ〉+c₁,
    ||Oφ||≤(||φ||H⁻½²+1)½,  e₀=(0,1,0),
    Z_m=Oφ P_A(t,0)e₀.

Z_m is W-measurable by the separable raw driver, continuous Young map and bounded conjugation/observable. No H½ point trace is used.

For fixed ρ, (3) turns Young sums into the ordinary statewise interaction integral: its error is bounded by the uniform modulus of continuity of U times ∫||C(r)||dr. The F Picard terms satisfy ||W_n||C_TF≤C_T^(n+1)B_T^nT^n/n!, B_T=sup||B_F(b)||. Their displacements equal the scalar terms by induction. Indeed the forcing f_r=b(r)X_(n−1)(r) is smooth with one compact support, and testing the phase integral gives

    〈[W_n(t)]₁,φ〉
      =∫₀ᵗ∫ f_r(y)∫G_d(t−r,dz)φ(y+z)dy dr
      =〈X_n(t),φ〉.

Absolute Fubini is bounded by ∫||φ||∞||f_r||₁(t−r)dr<∞. Thus the F series converges in distributions to the same locally uniform ordinary scalar Picard sum. Its total displacement is uρ^m, including the constant coordinate; this also works with d3 sphere Green.

The resulting pathwise integral Cρ=∫φuρ^m equals the Bochner L² integral Bρ from (9). To check equality of versions rigorously, E∫|φuρ^m|≤Q_t||φ||₁ and weighted Cauchy–Schwarz gives E|Cρ|²≤Q_t²||φ||₁². For each bounded random Ξ, the bounded L² functional E[Ξ·] commutes with the Bochner integral and absolute Fubini, so EΞBρ=EΞCρ. Choosing Ξ=sign(Bρ−Cρ) gives E|Bρ−Cρ|=0. Hence

    Bρ=OφP_Aρ(t,0)e₀,
    ||Bρ−Z_m||Lᵖ≤||Oφ|| ||e₀|| ||P_Aρ−P_A||Lᵖ →0.   (11)

Equations(9)–(11) discharge103 through a bounded average, not a rough F point value.

## 7. Consumer125: fixed-δ ordered products on the original measure

Fix δ,B,N, the mask R and the chosen smooth raw control, with L=δ⁻¹ and L_ext=(N+1)B≥L. Keep a SINGLE retaining slow source. The raw isometric pullback T_(δ,0)f(s,x)=δ^(a/2−1)f(s/δ,x) has covariance factor δ^(a−2)δ²δ^(−a)=1. Its translates retain global/local correlations. Their pointfields satisfy

    Y_fast(u,x)=δ^(a/2)Yεη(δu,x),
    Y_m(u,x)=Y_fast(mB+u,x),
    δ^a Kη(δv)=K_(η/δ)(v).                            (12)

Apply (1)–(6) jointly on the fixed finite global/local horizons. The ordinary integral change of variables proves the source cocycle

    S_F(mB)[A_glob,ρ(mB+u)−A_glob,ρ(mB)]S_F(−mB)
      =X_m,ρ(u).

Bounded restriction/difference/conjugation passes this identity to the actual raw paths. Young uniqueness, not rough PDE uniqueness, gives the restart for the full physical two-entry phase. Composition identifies the ordered factors through the final remainder τ (including τ=0).

Let n=N+1; F_m,ρ and F_m be source/raw factors and Cρ≥1 their maximum norms, eρ their maximum difference. Joint convergence and all finite uniform moments give supρ||Cρ||q<∞, ||eρ||q→0 for all finite q. Telescoping the noncommuting ORDERED product yields

    ||∏F_m,ρ−∏F_m|| ≤ n Cρ^n eρ,
    ||∏F_m,ρ−∏F_m||L²
       ≤ n ||Cρ||L^(4n)^n ||eρ||L⁴ →0.                (13)

No independence or uniformity in N is needed. Bounded Oφ,e₀ identify U_δB as the tested source L² limit.

Set g=δ^((1−a)/2), Γδ=g²Γ. Equation(12) gives the source at exactly that amplitude and widths (ε,η/δ): gY_fast=√δYεη(δu). Linear raw drivers and both F columns scale by g, and an n-vertex source chain by g^n. Thus (9)–(11) at Γδ give

    E U_δB² ≤ E|u_Γδ(L,0)|² = E|u_Γ(T,0)|²,
    δ=T^(−κ), κ=(4−α−a)/(3−α).                        (14)

The equality uses119/ordinary time change passed through fixed orders and summable series; source limits precede asymptotics.

The raw Gaussian identity (OWN121) is applied directly to the everywhere continuous nonnegative ordered-product functional, with the original Z=W(Ψ) and v=Var Z:

    E U_δB²=E[exp(−Z/√δ−v/(2δ))Y_δB²].              (15)

No convergence under this density was used to prove (13) or (14). The shifted product is already a raw Young functional; no source Cameron mean replaces Ψ. Global half-action v/2 and the actual mask are unchanged. Cone/lower-event estimates remain separate OWN inputs.

## 8. Consumer189: TWO limits at each fixed δ, then canonical scaling

Here specifically L=δ⁻¹, R=L+2, Tδ=δ^(−1/κ), g=δ^((1−a)/2), Γδ=g²Γ, z=(η(·/R),0)∈E and D=B₁. OWN187/188 use finite propagation and plateau margins to prove the ordinary prelimit equality

    E||pr₁P_E^ρ(L,0)z||L²(D)²
       = |D| E|u_Γδ,ρ(L,0)|².                        (16)

This is source cone equality for compact masked/constant unmasked data, on the actual given-W pullback; no masked stationarity.

First limit: (2)–(6), with fixed δ,R,L,g, give ||P_E^ρ−P_E||L²bounded-triangle→0 by closed restriction from F. Since ||pr₁e||L²(D)≤||e||E, the left displacement converges in L²(Ω;L²(D)). If aρ,a are these displacements, then

    |E||aρ||²−E||a||²|≤||aρ−a||L² (||aρ||L²+||a||L²)→0.

Second, separate limit: (10) at Γδ and widths (ε,τ/δ) gives E|u_Γδ,ρ(L,0)|²→E|u_Γδ(L,0)|². Only the point moment law is required. Passing the two limits through (16) proves

    E|u_Γδ(L,0)|²=|D|⁻¹E||pr₁P_δz||L²(D)².           (17)

Only afterward OWN119/125 give E|u_Γ(Tδ,0)|²=E|u_Γδ(L,0)|². The fixed-δ source limit is not exchanged with δ↓0 or a growing cone. The initial-data prefactor is harmless only at this later rate stage: ||η(·/R)||H½²≤CηR^d, and δlog[Cη|D|⁻¹(δ⁻¹+2)^d]→0. No uniform-R F-bound, raw point trace or density of E in F is used. Raw endpoint finiteness/upper-rate machinery (185/190–193) is a separate application, not a premise smuggled into the source UI argument.

## 9. Falsification checks and remaining scope

For Γ=0 all drivers vanish, U=I,P=S_F; e₀ gives Bρ=Z_m=1 and equality in(9)–(11),(14). The other constant datum gives displacement t, velocity1; deleting its column breaks general-phase restart. With compact datum equal1 on the enlarged cone, (16) has exactly |D| on its left, confirming the volume normalization. No nonzero-covariance Gaussian tilt is applied in this zero branch.

For admissible d1 white Γ=cδ₀, 0<a<1, Γ_2ε=cp_2ε is nonnegative and Kη(0)Γ_2ε(0) finite. Thus the same coefficient-one Wick formulas, chain mass t^(2n)/(2n)!, and cutoff comparison apply directly; they do not require a Riesz endpoint argument. The free Green identity ∫₀ᵗG_d(t−r,R^d)dr=t²/2 checks the first scalar Picard time integration in all three dimensions. Singular directional covariances retain the same positive measure/heat/feature argument; no eigenstate or angular density enters this seam. These are normalization/scope checks, not new moment formulas.

No source defect is established. The four assigned deductions are reconstructed conditional on the exact CURRENT OWN clauses in the table. Ancestors004–008/061–093 and separate cone/scaling/Gaussian identities are application-matched, not fully re-proved or accepted here. Full119–126/190–193 and all other whole-goal proofs remain assigned; no Chen-energy identification, rough PDE uniqueness or native grade change follows.
