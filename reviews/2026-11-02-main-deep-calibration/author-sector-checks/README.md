# Exact author-side sector checks

Replay from any directory with:

    uv run --with sympy==1.14.0 python check.py

The script resolves the repository from its committed path. It verifies the
unchanged source against scientific887 and computes every one of the 27
sector integrals from the physical chain lengths. The JSON records each
piecewise bound, inner polynomial, value, reflected normalized row and total.
The calculation uses exact rational arithmetic; all entries agree, total11/540.

This is an author-side finite check, not an independent review, a proof of
regularization, an asymptotic constant or an upgrade of MEDIUM to HIGH.
The initial external execution used an absolute checkout path; the committed
copy changes only root discovery and is replayed in place before commit.
