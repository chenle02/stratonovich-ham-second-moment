# V1 rejected: squared-norm and rendered grid transcription errors

Native18283 TERMINAL2,487.364seconds,actualOpus5.5/HIGH24checks,
canonical FAIL/high,accepted=false. Transport/model/text/image coverage
verified; all27input identities matched before repair. Full raw attempt
archived and member SHA256 read back. Original report/receipt unmodified.

Mandatory finding1: grid maximum subscript contains a stray m and broken
word on the source/PDF page140. The submitted patch used a non-raw
backslash-r-m fragment; JavaScript interprets that as carriage-return+m,
and subsequent formatting can remove the control character but retain the
corrupted text. That mechanism is reproduced by character codes; the
original post-format source contains the malformed split. Restore max_k
over the already-defined finite grid, then rebuild and inspect the display.

Mandatory finding2: basis proof says norm(tau tensor q)=Q_sp||tau||_a².
The correct held-source identity is the SQUARED H_W norm. Homogeneity
falsifies the transcription: normalize a nonzero tensor to norm1 and
scale tau by2; the norm becomes2, while the quadratic covariance is4.
Restore the explicit squared formula. No downstream construction changes.
These are GPT transcription repairs from the correct held source, not
reviewer-authored new mathematical arguments. A fresh full gate is needed.

Optional precision: make positive-time test and interval domains explicit,
state E_(r+1)-valued continuity for each E_r input, choose q>=max(p,q0),
and replace the non-premise common-envelope warning by the positive fact
that the Cauchy estimate uses vanishing tail traces. Endpoint nullity,
real fields/Schwartz basis and time-refined variances already follow from
supplied prior results; no theorem is strengthened or new scope inferred.

V1 remains FAIL. Full repaired source and rendered mathematics must pass
fresh same-model/HIGH review; no confidence or model change is authorized.
