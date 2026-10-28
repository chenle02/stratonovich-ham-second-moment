#!/usr/bin/env python3
"""Exact finite diagram inventory only; no analytic estimate is evaluated."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first, *tail = vertices
    for other in tail:
        for rest in matchings(tuple(v for v in tail if v != other)):
            yield ((first, other),) + rest


def classify(chains, matching):
    terminals = {c[-1] for c in chains if c}
    owner = {v: i for i, c in enumerate(chains) for v in c}
    edges = []
    for edge in matching:
        types = ['T' if v in terminals else 'I' for v in edge]
        row = {'edge': list(edge), 'endpoint_types': ''.join(sorted(types))}
        if types.count('T') == 1:
            terminal = next(v for v in edge if v in terminals)
            interior = next(v for v in edge if v not in terminals)
            chain = chains[owner[interior]]
            pos = chain.index(interior)
            left = chain[pos-1] if pos else 'root'
            right = chain[pos+1]
            row.update(terminal=terminal, interior=interior,
                       merge_neighbors=[left, right])
            if owner[terminal] == owner[interior]:
                row['time_case'] = ('same_chain_endpoint_T_equals_b' if terminal == right
                                    else 'same_chain_remote_T_gt_b')
            else:
                row['time_case'] = ('cross_chain_T_inside_or_right_of_interval' if left == 'root'
                                    else 'cross_chain_T_left_inside_or_right_of_interval')
        elif types.count('T') == 2:
            row['time_case'] = 'two_terminals_no_interior_merge_vertex'
        else:
            row['time_case'] = 'no_terminal_endpoint_selected'
        edges.append(row)
    return edges


def deletion_sequences(chains, matching):
    if not matching:
        return [()]
    terminals = {c[-1] for c in chains if c}
    result = []
    for edge in matching:
        if not terminals.intersection(edge):
            continue
        remaining_chains = tuple(tuple(v for v in c if v not in edge) for c in chains)
        remaining_matching = tuple(e for e in matching if e != edge)
        for rest in deletion_sequences(remaining_chains, remaining_matching):
            result.append((edge,) + rest)
    return result


def main():
    output = {'kind': 'finite-combinatorial-inventory', 'analytic_claims': [], 'orders': []}
    for total in (2, 4):
        diagrams = []
        edge_type_counts = Counter()
        time_case_counts = Counter()
        for m in range(total+1):
            chains = (tuple(range(1, m+1)), tuple(range(m+1, total+1)))
            for matching in matchings(tuple(range(1, total+1))):
                edges = classify(chains, matching)
                edge_type_counts.update(e['endpoint_types'] for e in edges)
                time_case_counts.update(e['time_case'] for e in edges)
                sequences = deletion_sequences(chains, matching)
                assert sequences
                assert all(len(s) == total//2 for s in sequences)
                diagrams.append({'split': [m, total-m],
                                 'chains': [list(c) for c in chains],
                                 'matching': [list(e) for e in matching],
                                 'edges': edges,
                                 'terminal_incident_edge_count': sum('T' in e['endpoint_types'] for e in edges),
                                 'complete_pair_deletion_sequence_count': len(sequences)})
        assert len(diagrams) == {2: 3, 4: 15}[total]
        output['orders'].append({'total_order': total, 'diagram_count': len(diagrams),
                                 'edge_type_counts': dict(sorted(edge_type_counts.items())),
                                 'time_case_counts': dict(sorted(time_case_counts.items())),
                                 'every_diagram_has_terminal_edge': all(d['terminal_incident_edge_count'] > 0 for d in diagrams),
                                 'diagrams': diagrams})
    target = Path(__file__).with_name('consumer-inventory.json')
    target.write_text(json.dumps(output, indent=2)+'\n')
    for order in output['orders']:
        print(order['total_order'], order['diagram_count'], order['edge_type_counts'], order['time_case_counts'])

if __name__ == '__main__':
    main()
