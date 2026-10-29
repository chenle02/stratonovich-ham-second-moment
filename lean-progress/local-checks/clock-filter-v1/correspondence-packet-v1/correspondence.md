# Exact application map

This review checks THREEtypes and their correspondence only. Mathematical
clock-screen proofs already passed a separate source-bound cross-family
review;do not re-prove or promote the full SPDE. The types and axioms printed
in types-and-axioms.txt come from live compiled source,not the parser.

resolvent_partial_fraction:the per-frequency kernel in paper-clock.txt is
rewritten exactly as the difference of the theta and theta+lambda resolvents
divided by2theta*lambda. r is real;actual |xi| is allowed. theta,lambda>0.

clock_filter_bounds:paper multiplier2theta/(2theta+lambda) lies strictly in
(0,1). strict_filter_integral:take sigma=volume restricted to(0,infinity),
w=w_theta of the paper. This measure is nonzero and supported on positive
lambda;it is infinite,which the Lean type permits. The paper separately
proves w_theta integrable and strictly positive there. These remain explicit
analytic inputs,not formalized here. Filtered integrability is a conclusion,
not a premise. The representation K=intw and J1=intfilter*w is also external.
Thus the theorem supplies J1<K CONDITIONALLYon those actual model inputs.
No spatial spectral measure is substituted for the lambda measure.

No custom axiom,desired comparison hypothesis,finite-measure assumption,
or new SPDE theorem is intended. Local receipt records source replay and
semantic controls. This pilot creates no repo or official verified package.
No reviewer should infer full dependency rebuild,Comparator,whole-paper,
novelty,circulation,full sharp constant or all-order lower comparison.
