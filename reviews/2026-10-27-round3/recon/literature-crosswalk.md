# G2 literature and source crosswalk — bounded reconnaissance

[held back: collaborators' unpublished work]

## Exact target and outcome

Target: for the Stratonovich wave equation with data (1,0), temporal covariance
|s-r|^(-alpha0), homogeneous nonnegative spatial covariance of degree -alpha,
0<alpha0<1, alpha+alpha0<2, prove
limsup t^(-kappa) log E u(t,x)^2 < infinity,
kappa=(4-alpha-alpha0)/(3-alpha), first in d=1 and eventually d=1,2,3.
The spatial-white case alpha=d=1 is included. The G0 exponent
rho=(4-alpha-alpha0)/(3-alpha-alpha0) is weaker and is not substituted for
this target.

**No direct implication of this target was found in the specific theorems
examined below.** This is not an exhaustive nonexistence/novelty result.
The most useful existing mechanism is the Hu–Meyer self-contraction grouping
in Balan's static Stratonovich paper. It is already published methodology;
a time-dependent implementation and a sufficiently sharp estimate remain
unproved obligations. The pathwise CDST estimates are also a possible lead,
but currently supply neither the stated flat-data application nor a uniform
large-time annealed estimate.

## Source identity and actual reading coverage

Paths in this report are relative to the Article repository root.

| Source | Exact artifact / identity | SHA-256 | Coverage in this reconnaissance |
|---|---|---|---|
| X. Chen time-dependent author version | `sources/chen-2026-author/aap-chen-2025.pdf`, 64pp; pinned author version whose title page says Submitted, not arXiv v1 | `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c` | Hash checked; existing G0 source audit/notes consulted; current author publication list reports Accepted, a separate status observation that does not upgrade the pinned PDF edition. No fresh whole-source proof audit. |
| Chen–Deya–Song–Tindel (CDST) preprint | `../SPDEForge/sources/chen_deya_ea-23-hyperbolic/chen_deya_ea-23-hyperbolic.pdf`, arXiv:2205.15773v1 (31 May 2022), 34pp | `b6a8fc7aa43a166af7387eb149b90610d8e5307415bc2c11aa4663c05c30d03b` | TeX Section4/5 statements and proof estimates read beyond introduction; rendered pp17,18,22,24,28 checked. Not every Besov/Strichartz proof in Sections2–3 re-proved. |
| CDST correct publisher layout | [author-linked OUP advance PDF](https://web.math.utk.edu/~xchen3/111111-1.pdf), DOI10.1093/imrn/rnad039, 54pp, advance pagination1–54 | `ad9b5c135a12d5c454f1dcf66cae3e5fa70567452de87683919effb1ae26d491` | Retrieved to temporary storage, not installed into source repositories. Rendered pp28,29,36,39,47 checked against the preprint arguments. Published-layout Theorem4.8 corresponds to preprint Theorem4.7. Final journal citation is IMRN2023(21),18575–18628; this artifact does not print those final page numbers. |
| Balan (2022) | `../SPDEForge/sources/balan-22-stratonovich/balan-22-stratonovich.pdf`, publisher PDF, J. Theoret. Probab.35,2643–2689, DOI10.1007/s10959-021-01144-y | `ca4a52ae68340516f7c2f3dccf4f7fe8fc39cfde569be841df1b082777187d2c` | Intro hypotheses, Theorems1.2/1.3, Theorem3.3 proof, Section5 finite-spectral-measure estimate and Section6.1 contraction grouping examined in text; rendered journal pp2644,2645,2648,2666,2680 checked. Not a complete proof audit. |
| Chen–Hu (2025) | `../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`, AOP53(6),2144–2195, DOI10.1214/24-AOP1758 | `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22` | Rendered PDF pp4,14 (Theorems1.2 and3.3) inspected; existing publication audit consulted. No disputed white-noise constant adopted; no full LDP proof audit. |
| Balan–Conus (2016), comparison only | `../../../All_PDFs/b/balan_conus-16-intermittency.pdf`, AOP44(2),1488–1534, DOI10.1214/15-AOP1005 | `4fc3f73cc6164c1c9cc6a384ffdfb3389d21d34be1e86bcfbc681375a59d2756` | Existing local TeX model and Theorem2.1; rendered journal pp1492,1494 checked. Skorohod theory is not developed here. |

### A misfiled canonical PDF, preserved rather than repaired

`../../../All_PDFs/c/chen_deya_ea-23-hyperbolic.pdf` is **not CDST**.
Its hash is `9ed4b0ae633cc79eb1b985ecf00b2ae67db83061fd0d8a73628704b5b664a5da`.
The actual title is *Exponential asymptotics for Brownian self-intersection
local times under Dalang's condition*, EJP28(2023),article119,
DOI10.1214/23-EJP985 (18 PDF pages). The SPDEForge numbering warning pointed
to this canonical pathname, so trusting the filename alone would have been
wrong. It was excluded from CDST evidence. The correct OUP layout was recovered
from the authors' own publication links; no file was replaced or repaired.

## Application crosswalk

[held back: collaborators' unpublished work]

Source-fidelity classification: the selected CDST and Balan statements are
**VERIFIED at the statement/application level** under their actual hypotheses;
this is not a whole-paper proof certification. The wrong canonical CDST file
is an artifact-identity failure, not a mathematical defect in CDST. The previously
recorded Chen intermediate-uniformity and Chen–Hu printed-constant issues remain
scoped SOURCE-INTERNAL-DISCREPANCIES; they are not enlarged here.

### CDST proof-consumer checks, not just an introduction summary

The noise exponent alpha is distinct from CDST's negative spatial regularity
parameter (call it alpha_s), and the project's growth kappa is distinct from
CDST's kappa_s. Corollary5.7 invokes Theorem4.8 for its admissible noise;
it does not replace the theorem's data hypothesis. Notation4.7 explicitly
puts H^s inside unweighted L². Lemma4.9 and its proof consume those Sobolev
norms. A weighted *solution* space does not make the constant initial datum
satisfy an unweighted *data* assumption.

The regime is nonempty: d=1, a0=a=1/4, with smooth compactly supported data,
admits e.g. alpha_s=.15, kappa_s=.2, gamma_s=.2, theta=.85, p=100 in (4.4).
This verifies feasibility, not the flat-data transfer. Inspection of the
proof also shows a horizon-dependent weight threshold mu_* in p29; the
Picard c_T of p39 is not an asserted universal time-independent constant.
No estimate has been optimized here, so this is not a no-go for the pathwise
method.

## Established mechanisms worth testing, with exact limits

1. **Group self-contractions first.** Balan Section6.1, pp2679–2680,
   writes the Stratonovich solution as a sum of Wiener-chaos projections K_m,
   each summing original orders n with n-m even. This explicitly groups
   traces rather than treating Stratonovich orders as orthogonal. A
   time-dependent implementation would need trace-kernel estimates uniform
   in order and the correct t dependence. It is a known organizational
   mechanism, not a new claim that it gives the needed factorial gain.
2. **Do not promote compact-time estimates to sharp growth.** Balan
   Theorem3.3 proof p2666 keeps C_(p,mu,T)=(p-1)K_mu C_T² T(T∨1)^(3/2),
   with C_T=2sqrt(2)(T∨1), and a factorial denominator (n!)^(1/4).
   This proves summability, not the proposed sharp homogeneous estimate.
   Section5's easier finite-mu bounds also have constants depending on mu(R^d),
   which do not remain bounded under homogeneous singular mollifier removal.
3. **Poisson interpolation is a real source lead.** Balan Theorem1.3 p2648
   uses independent Poisson times and wave-distributed velocities, but its
   integrand is a product of noisy field values, not a positive exponential
   of an occupation integral. Do not import heat-equation Feynman–Kac
   positivity or Jensen bounds for an exponential without a new argument.
4. **Partial-regime pathwise work requires several separate bridges.**
   Flat-data localization, large-horizon constants, integrability of the
   random growth factor, point evaluation, and identification with Chen's
   regularized solution must each be stated. Success on one does not imply
   G:upper, even when alpha0+alpha<1 in d1.

[held back: collaborators' unpublished work]

## Search coverage, access limits and investment decision

Local searches covered the project's source manifest/notes, relevant wiki
pages, refdb entries, CDST Sections4–5, Balan compact-time proof and grouping
sections, and the static theorem/representation. General web searches used
both “Stratonovich wave equation moment time-dependent upper bound” and
“hyperbolic Anderson Stratonovich moments fractional time”, with primary-site
restrictions in followups. Author publication lists were consulted, yielding
the correct CDST OUP layout and the current time-dependent author-PDF link.

MathSciNet record requests for MR4665631 and MR4509081 and zbMATH DOI queries
were inaccessible through the available web tool. The OUP DOI route failed,
but an author-hosted publisher PDF was accessible. No complete forward-citation
search, MathSciNet review/citation audit, or full-paper proof audit of every
serious candidate was completed. Query/identity receipts are retained in
`literature-query-receipt.json` alongside this report.

**Decision: REFRAME as bounded route reconnaissance.** Proceed with small,
explicitly falsifiable Stratonovich-specific candidate inequalities and source
bridges. Do not claim the target novel or publishable, or call this a closed
literature gate. Before substantial proof investment in a selected new route,
complete its focused primary-source dependency and implication audit. The
specific direct applications rejected above need not be rediscovered.
