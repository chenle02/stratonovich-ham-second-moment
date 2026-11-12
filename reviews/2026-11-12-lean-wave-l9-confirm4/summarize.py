import json, os, glob, sys
OUT = os.path.dirname(os.path.abspath(__file__))
lines = ['# Wave L9 re-review round 4 (strict categories, split modelled-object rule): summary', '',
         'Companion e2c50b5 (wave-l9/repair; round-3 repairs and the split modelled-object rule, docs only; reviewed commit d5667f5), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision e2c50b5. Packets built by scratchpad/build-l9-reconfirm4.py. Every finding below is verbatim from report.json.', '', 'Packets: h1/h2 the 17 changed ledger headings; h3 the three M1 whole-result sections, the register text and the missing-construction moves; h4a-h4d the Index-by-label table in pieces of 99 rows with only the named Lean declarations (numbered excerpts) and module headers; h5 round-3 findings, classification consistency of counts, no new overclaim in d5667f5..e2c50b5, earlier repairs kept. Retry only on tool failure, recorded in the driver log.', '']
for d in sorted(glob.glob(OUT + '/h*/')):
    g = os.path.basename(d.rstrip('/'))
    lines.append(f'## {g}'); lines.append('')
    lines.append('Preflight: contract-check ' + open(d + 'contract-check-1.txt').read().strip() + '; dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt ' + open(d + 'contract-check-2.txt').read().strip()); lines.append('')
    lines.append('Driver log:'); lines.append('```'); lines.append(open(d + 'driver.log').read().rstrip()); lines.append('```')
    atts = sorted(glob.glob(d + 'attempt-*'))
    for a in atts:
        st = open(a + '/STATUS.md').read() if os.path.exists(a + '/STATUS.md') else '(no STATUS.md)'
        lines.append(f'### {os.path.basename(a)}'); lines.append('```'); lines.append(st.strip()); lines.append('```')
    final = atts[-1] if atts else None
    rp = final + '/report.json' if final else None
    if rp and os.path.exists(rp):
        r = json.load(open(rp))
        lines.append(f'Verdict: **{r.get("verdict")}**, confidence: **{r.get("confidence")}** ({os.path.basename(final)})')
        ch = r.get('checks', [])
        from collections import Counter
        lines.append('Check verdicts: ' + ', '.join(f'{k} {v}' for k, v in Counter(c['verdict'] for c in ch).items()) + f' (of {len(ch)})')
        bad = [c for c in ch if c['verdict'] not in ('PASS', 'PASS_WITH_NOTES')]
        if bad:
            lines.append(''); lines.append('Checks not PASS/PASS_WITH_NOTES:')
            for c in bad:
                lines.append(f'- {c["claim"]}: {c["verdict"]}: {c["reason"]}')
        for sev in ('fatal', 'major', 'minor'):
            f = r.get('findings', {}).get(sev, [])
            lines.append(''); lines.append(f'Findings, {sev} ({len(f)}):')
            for x in f:
                lines.append(f'- {x}')
        lines.append(''); lines.append(f'Required repairs ({len(r.get("required_repairs", []))}):')
        for x in r.get('required_repairs', []):
            lines.append(f'- {x}')
        lines.append(''); lines.append(f'Limitations ({len(r.get("limitations", []))}):')
        for x in r.get('limitations', []):
            lines.append(f'- {x}')
    else:
        lines.append('No valid report.json: not a review.')
    lines.append('')
open(OUT + '/SUMMARY.md', 'w').write('\n'.join(lines) + '\n')
print(OUT + '/SUMMARY.md')
