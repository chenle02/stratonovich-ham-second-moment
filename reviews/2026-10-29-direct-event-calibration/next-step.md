# Next bounded model test: a physical phase-space block norm

Planning only; no operator estimate, regularity threshold or lower theorem
is asserted below. Exact scaling and scalar calibration are now reviewed.

On a time block of size delta, the fast-wave equation becomes a unit-time
wave equation with noise amplitude delta^((1-a)/2), before any spatial
rescaling. The scalar proof suggests studying local transfer errors, but a
physical random phase-space operator and its point-evaluation consumer have
not been constructed uniformly in the spatial cutoff.

Immediate task: test the FIRST Gaussian response in candidate physical phase
spaces before opening an operator proof wave. In particular, do not assume
the usual energy phase H1 x L2 is appropriate for a spatially rough field.
Write the actual position and velocity kernels, and check their spectral
integrability and cutoff growth. Choose a rougher phase only if it supports
both iteration and the desired terminal observable. Keep global data1 and
the expanding backward cone/weights explicit.

Closest newly reread held input: Balan--Tudor, The stochastic wave equation
with fractional noise: a random field approach, source
../SPDEForge/llm_pack/balan_tudor-10-stochastic.tex, SHA256
b64494a0cf156bcc9548371578cb0f1503dce0f7101a52d8a5119f6a0ca89cc1.
Selected actual coverage: lines693--735, wave-th/rem-AB-equiv; lines815--838,
definition of N_t and wave-prop-1. It supplies the ADDITIVE position kernel
spectral order2H+1 and its norm formula. It does not, in those passages,
supply a velocity-phase or multiplicative random-operator estimate. Do not
claim that derivative extension merely by removing the sine denominator.
This is a held source, not a new reference to enqueue; no publisher-version
proof or exhaustive whole-source audit was performed.

A useful eventual estimate would bound unit-block random-operator errors
in Lp uniformly in the block number/cutoff, with order delta^((1-a)/2), in
a genuinely invariant phase norm. It is UNPROVED. Only if such a bound and
a deterministic spectral cone were justified could a high-p union bound
control all order1/delta blocks; temporal independence is not required by a
union bound. Parent constant-data moment bounds do not themselves give an
operator norm on arbitrary phase data.

[held back: collaborators' unpublished work]