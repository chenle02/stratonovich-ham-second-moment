# Precision recording repair and stronger false-action diagnostic

V1's two_precision_log_bound_difference subtracted values AFTER display
rounding to28digits. A reported zero was agreement of displayed strings,
not the actual35/70digit difference. Preserve v1script/JSON; do not use
that zero as a precision-error bound. Other quadrature inequalities and
closed-form comparisons were computed before formatting and are unaffected.

V2 stores unrounded mpmath results from both precisions and computes the
difference at the higher precision. This is still consistency, not a
certified enclosure. It also evaluates a normalized WRONG Rayleigh law
with doubled action,using the SAME quadrature at(a/2,delta/2),rather than
only displaying the variational coefficient gap. Its smaller predicted
moment fails against the exact Gaussian MGF at the tested small deltas.
Zero-signal cases cannot detect either false scaling and remain labeled.
This new run changes a faulty measurement and adds an actual false-guard
calculation; it is not a rerun of unchanged tests to get a favorable vote.
