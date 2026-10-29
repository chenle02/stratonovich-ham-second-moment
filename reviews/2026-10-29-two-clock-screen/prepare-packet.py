[held back until the source author has been told]

norm-inputs.txt supplies original full covariance/dimension class and the
already proved finite N2quadratic form with Gaussian smoothing,physical
G_theta(s,x)G_theta(t,y)and radial measure homogeneity. The actualK_Gamma
is this order1cross gap transform,not a full solution Laplace integral.
The new proof derives its exact positive spectral lambda kernel explicitly.
No spectral density,isotropy or covariance pointwise heat monotonicity.
h_Gamma(w)=(p_w*Gamma)(0) is an AVERAGED heat factor,not a point value of a
generalized covariance along a random path;take spatial heat limits first.
The analytic complex power in6.1is not the modulus used later in7.1.

New candidate shared-clock value J1is the ACTUALcross density filtered by
2theta/(2theta+lambda);every constant-rhoBrownianpair hasJ_rho<=J1<K.
This is strict for every original nonzero covariance and positivea.
Atalpha1the ratio is2-2^a,with white normalization checked separately.
Statica0is defined separately as covariance1,never Gamma_E(0).

Scope:constant Brownian correlationrho*min(u,v),independent spatial chains,
no extra ordering weights,and unrestricted operational rectangle. Other
derived couplings/weights,one-sided inequalities,or asymptotic equivalence
remain open. In fact the first-pair inequality supports possible LOWERuse;
it does not refute such a route. Preserve original full G:sharp.
Initial numeric quadrature warning is retained outside required calculations;
refined endpoint substitutions remove it without tolerance relaxation.
All numeric/radial probes are finite diagnostics,not proofs of Radon generality.
''')
texts=['clock.txt','norm-inputs.txt','project-goal.md','change-binding.json','source-map.md','source-excerpts.txt','source-rendering.json','calibration.py','calibration.json','general-calibration.py','general-calibration.json','general-calibration-warning.md']
required=[{'path':n} for n in texts]+images
dump(R/'required-v1.json',required);dump(R/'manifest-v1.json',{f.name:sha(f) for f in sorted(P.iterdir()) if f.is_file()})
(CAL/'images.txt').write_text('Carrier/legibility ONLY,not science. Read ALL12PNGs with direct Read(file_path only). Every source37--42page has two overlapping direct windows. Root separately verifies native bytes.'+chr(10)*2+chr(10).join(i['path']+' '+i['sha256'] for i in images)+chr(10))
dump(R/'carrier-required-v1.json',[{'path':'images.txt'}]+images)
dump(R/'carrier-manifest-v1.json',{f.name:sha(f) for f in sorted(CAL.iterdir()) if f.is_file()})
(R/'carrier-contract-v1.txt').write_text('''ONLY native image-carrier/legibility calibration,not science.
Read images.txt and ALL12required PNGs exactly once with direct Read using
ONLYfile_path. No math verification,commands,browsing,editing or delegation.
Report unreadable/cutoff images. Root separately checks exact bytes.
Return ONLY bare valid JSON,no preamble/fence/afterword.
Schema subscription-review-report/1,verdict,confidence,source_coverage,
checks claimCARRIER_ONLY/verdict/reason,findings fatal/major/minor,
required_repairs,limitations. Your own legibility verdict/confidence.
State in limitations:this is not science,proof,mathematical vote or circulation
clearance. Escape quotations and backslashes;plain strings are sufficient.
''')
(R/'build-driver.txt.gz').write_bytes(gzip.compress(args.build_log.read_bytes(),mtime=0))
print(json.dumps({'pages':pages,'proofs':60,'new':new,'required_texts':len(texts),'images':12,'members':len(list(P.iterdir()))},indent=2))
