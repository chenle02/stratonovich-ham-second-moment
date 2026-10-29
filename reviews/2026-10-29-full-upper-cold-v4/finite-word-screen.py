"""Exact finite algebra checks for the proposed clarification;not a proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ZERO = (F(0),) * 4
V = (F(1), F(1, 5), F(3, 10), F(-1, 10))
M = [((0, 1), (1, 0)), ((1, 0), (0, -1))]


def add(state, key, value):
    before = state.get(key, ZERO)
    after = tuple(x + y for x, y in zip(before, value))
    if any(after):
        state[key] = after
    elif key in state:
        del state[key]


def free(state, step):
    # Arbitrary bounded deterministic free-like factors,I+tau*G_0.
    # They preserve Gaussian degrees and need not commute with insertions.
    tau = F(1, step + 2)
    return {d: (v[0] + tau*v[2], v[1] + tau*v[3],
                v[2] - tau*v[0], v[3] - 4*tau*v[1])
            for d, v in state.items()}


def insert(state, color, caps=None):
    out = {}
    mat = M[color]
    for degree, v in state.items():
        spatial = (F(0), F(0),
                   mat[0][0]*v[0] + mat[0][1]*v[1],
                   mat[1][0]*v[0] + mat[1][1]*v[1])
        # Probabilists' unnormalized Hermites:H_j*Z=H_(j+1)+j*H_(j-1).
        # A diagonal basis normalization does not change cutoff equality.
        up = list(degree);up[color] += 1;up = tuple(up)
        if caps is None or up[color] <= caps[color]:
            add(out, up, spatial)
        if degree[color]:
            down = list(degree);down[color] -= 1;down = tuple(down)
            add(out, down, tuple(degree[color]*x for x in spatial))
    return out


def run(word, caps=None):
    state = free({(0, 0): V}, 0)
    seen = [0, 0]
    for step, color in enumerate(word, 1):
        if seen[color] == 0:
            assert all(d[color] == 0 for d in state), (word, step)
        state = insert(state, color, caps)
        seen[color] += 1
        assert all(all(d[i] <= seen[i] for i in range(2)) for d in state)
        if seen[color] == 1:
            assert all(d[color] == 1 for d in state)
        state = free(state, step)
    return state


cases = 0
for length in range(5):
    for word in product(range(2), repeat=length):
        counts = tuple(word.count(i) for i in range(2))
        caps = tuple(2*((n+1)//2) for n in counts)
        assert all(n <= cap for n, cap in zip(counts, caps))
        assert run(word) == run(word, caps), (word, caps)
        cases += 1

assert run((0, 1)) != run((1, 0))
assert (0, 0) in run((0, 0)), "Annihilation/self-contraction was lost"
assert (2, 0) in run((0, 0)), "Creation branch was lost"
assert run((0, 0)) != run((0, 0), (1, 0)), "Too-small cutoff control is vacuous"

# The isolated optimized form bound does not imply the real-part bound.
# This is NOT a counterexample to the lemma's stronger all-rho hypothesis.
s = F(1, 2);delta = F(1, 4)
optimized_bound_squared = 4*delta**2*s  # a=1/2,lambda=1
required_real_control_squared = delta**2*(1+s**2)**2
assert optimized_bound_squared > required_real_control_squared

out = {
    "status": "PASS",
    "finite_word_cases": cases,
    "word_lengths": "0 through4",
    "independent_colors": 2,
    "spatial_components": 2,
    "noncommuting_word_outputs_differ": True,
    "self_contraction_and_creation_both_retained": True,
    "too_small_cutoff_changes_output": True,
    "fresh_color_is_vacuum_before_first_use": True,
    "real_part_justification_countercheck": {
        "a": "1/2", "lambda": "1", "s": "1/2", "delta": "1/4",
        "optimized_bound_squared": str(optimized_bound_squared),
        "required_control_squared": str(required_real_control_squared),
        "isolated_implication_fails": True,
        "lemma_not_refuted": True,
        "repair": "Evaluate the existing all-rho form hypothesis at rho=lambda for the real part;rho=s is for the imaginary part",
    },
    "scope": "Finite exact polynomial-domain algebra with arbitrary deterministic free-like factors,not actual PDE evolution,norm certification,infinite-mode convergence or a theorem proof",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
