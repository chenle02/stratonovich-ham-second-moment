# Dispatch schema repair

First dispatch on087ee98 exited4 before a model review: required-sources
items allow path and optional ranges, not sha256. This is an input-schema
rejection, not a mathematical report, live review or accepted gate. Retain
all SHA256 bindings in statement-manifest-v1.json and give the runner the
supported path-only plan. Target, packet and diagnostics unchanged. A new
native output directory is required; do not overwrite a partial artifact.
