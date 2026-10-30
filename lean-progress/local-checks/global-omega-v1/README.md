# Global Omega exact finite rational core (provisional)

Actual publicdefinitions envelopePolynomialQ,envelopeDenomD,envelopeRationalV
match frozenGamma-envelope target; fullprinteddefs ANDtypes in
 definitions-types-and-axioms.txt. Fourpublictheorems verify twoquarter
Bernsteinboundscaling4^15Q>=1, Qpositive on[0,1/2], and actualV<1 for
0<x<=1/2. Constants are exactREALrationals/integerpowers, not casts of
floats, proxytypes or assumeddesiredpositivity. Proofs use explicit16term
positive identities and ring/positivity; rationalclearing all denominators
withactualdomainbounds. No oracle/CAS result is trusted byLean kernel.

MathlibTactic4.35.0/56a0058,pinnedlateststableofficialAPIchecked.
Cleancompile/audit/freshownedreplay,5matchingartifacts,standard3axioms,
2actualFalsecontrols. WrongOrigin tests the excludedx0 whereV=1;
WeakEnvelope divides outretainedP atx1/10, recovering theknownfailedweak
bound>1. Both failatFalse, notunknownAPI. Initialcompileattemptfailed to
clear differentlynormalizeddenominators (3-2x versus3-x*2); source/log
preserved. Successor adds ONLYcanonicalnonzerofacts,no publicstatement/
definition/coefficients changed. No linter/guardweakened/cluster use.

ExactSympycertificatebuilder andLeangenerator replaybyteidentically;
actualcompiledsourceSHA equalsreceipt. Bothfullnativearchives member-
verified. Independent COMPLETEdefs/types/actualGamma-rationalapplication
review required. Gamma/Beta/integral/kernel/energy/globalOmega/SPDE proof
is ANALYTIC, notkernelcertified bythese finitelemmas. No newpackage/
companion/donor/lease/registry/HPC/Comparator transaction; L0/PROPOSED.
