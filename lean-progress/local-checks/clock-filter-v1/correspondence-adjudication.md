# Exact Lean type/application adjudication

Source86de3d8e5475cb6120414c400e26be6b59bc0c12. Native first-party
Claude Opus5.5/HIGH,112.922s,PASS_WITH_NOTES,all four checksPASS,
accepted=true,coverage=true. Seven required texts completely delivered;
source/contract/native event/read-ledger hashes bound. No required repairs.
Unchanged frozen Lean source SHA:
0e501b255a23661c3c75d2dc98e08390c6ba4324a73537367f0c07aac6843d38.

All five minor findings are adjudicated:

1. Concrete positive-lambda Lebesgue restriction is NOT instantiated in
   Lean. Its nonzero/support facts remain a hand-checked application step.
   This is a conditional generic integral theorem,not a formal SPDE consumer.
2. Make the total function explicit:extend the analytic density w_theta by
   zero forlambda<=0. Measurability on positive lambda and integrability of
   this extension against sigma=volume.restrict(Ioi0) remain analytic inputs.
   In Lean,Integrable already includes AEstrong measurability. No premise is
   omitted or desired strict comparison assumed;the extension off support is
   irrelevant. The density's continuity follows from its explicit resolvent
   power formula on positive lambda,but no new formal claim is made here.
3. Reviewer did NOT inspect controls or independently compute hashes. Root
   executed all three controls,read every log and matched all source/object
   hashes. Wrong normalization,wrong filter and zero-measure strictness each
   fail on unsolved False after successful imports,not setup errors. Exact
   sources/logs are in evidence/attempt-03/;no reviewer execution is credited.
4. Earlier attempts were outside this narrow packet. Both snapshots/logs are
   preserved in evidence/attempt-01/ and attempt-02/:reserved binder parse
   failure,then final proof-term orientation mismatch. No theorem statement
   or premise changed. Full source history is not attributed to the reviewer.
5. Cli has no build root and is not imported by the chosen Mathlib modules.
   The direct runtime resolved all actual imports. No dependency rebuild or
   complete package replay is claimed.

Two review PRE-FLIGHT failures are preserved:attempt1passed a descriptive
string where target must name a packet file;attempt2encountered an unsupported
auto-updated Claude CLI2.1.312. Neither reached scientific review. Attempt3
used the EXISTINGpinned2.1.304 runtime after successful doctor. No global setup
was changed,no coverage gate bypassed,no threshold lowered,no model fallback.
The39member native archive includes all three attempts/drivers and doctor.

Future unchanged uses of these exact three theorems can cite the source,
printed types,axioms and local replay rather than repeat scalar proof review.
Fresh analytic applications still need hypothesis and source correspondence
checks. Full package trust gate,concrete model instantiation,all-order clock
comparison,sharp constant,novelty and circulation remain separate.

Durable lesson:freeze the type boundary before writing Lean. Derive
integrability when it is part of the claim. A successful kernel check covers
the proposition actually encoded;an independent application check must identify
the correct integration measure and any unformalized analytic inputs. Pin the
review runtime before launch as well as pinning Lean/Mathlib dependencies.
