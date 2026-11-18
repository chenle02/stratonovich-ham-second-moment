# What was removed from the published history, and why

This repository publishes a filtered copy of the project's development
history: its commits in their original order, with their original dates and
messages, after a documented, reproducible filter removed what could not be
published. This file lists every class of removal, why it was removed and how
much.

The filter removed whole files, held back paragraphs inside files and commit
messages, and dropped the commits that touched only removed material (counted
below). It changes no mathematical statement or proof in the manuscripts.
Where a commit touched both published and removed material, the commit still
appears, and its message is kept unless a rule below says otherwise. The
original history and the withheld records are retained privately.

## Commit identifiers

- **IDs change.** Rewriting history changes every commit identifier.
  Commit IDs quoted inside files and messages refer to the original
  history. Use `history/commit-map.tsv` to translate an original ID into
  the published one.
- **Commits.** At the first publication (v1.0.0), the original history had
  2,582 commits on its two branches. The published history had 2,012, plus
  one commit that adds `history/commit-map.tsv`. Later releases add their
  commits on top of the published history, which is never rewritten; each
  release's commit-map commit states how many original commits it adds, how
  many are published and how many became empty.
- **Dropped commits.** At the first publication, 570 commits touched only
  removed material, so they became empty and were dropped. Each is listed in `history/commit-map.tsv`
  with a zero target.

## Classes of removal

"File versions" counts each version of a file in the history.
"Occurrences" counts individual replacements. The counts are those of the
export of 2026-11-16 (origin `6e83976c`); the few commits made after it, up to
the release, are filtered by the same rules, and `history/commit-map.tsv`
lists every commit.

### Other people's work

| Rule | What | Why | How | Count |
|---|---|---|---|---|
| 1 | Source papers kept for reading (`sources/`) | Other authors' copyrighted texts | Removed; cited by arXiv identifier or DOI | 162 file versions |
| 2, 12, 18 | Copies of other authors' papers, books and source files inside review packets, and collaborators' source copies | Copyright; collaborators' unpublished work | Removed by path | 1,420 file versions |
| 15, 18, 25 | Excerpts, page-selected copies and retrieval captures of other people's texts | Copyright | Removed by name and shape | 131 file versions |
| 15, 16, 26 | Files identified by their content: third-party text (author blocks, addresses), and files describing the AI tools' standing configuration | Copyright; private configuration | Removed | 96 file versions (with the rule-38 records below) |
| 16b | Copies of another project's README | Copyright of documentation | Removed; the project is cited instead | 1 file version |
| 16c | Text extracts of pages of another author's unpublished paper | Copyright; unpublished work | Removed | 8 file versions |
| 15c | Reviewers' readings of page images of other authors' books and papers, which reproduced passages of those pages | Copyright | Removed | 16 file versions |
| 18 | Images that are not renders of this manuscript | Most are page images of other papers | Removed. Only images named as renders of this manuscript and passing an OCR check are kept, plus the exception below | 205 file versions |
| 32 | Excerpts of software source (Mathlib) and a binary source capture | License notices absent | Removed | 12 file versions |

### Collaborators' unpublished work

| Rule | What | Why | How | Count |
|---|---|---|---|---|
| 5, 19, 23, 29, 35 | Passages about collaborators' ongoing, unpublished research (another project on the Skorohod regime of the same model) | Not ours to publish before they do | Replaced by "[held back: collaborators' unpublished work]" (a TeX comment in manuscript files), or "[held back]" inside data records. The few sentences in the current manuscripts that cite the project are kept | 21,012 occurrences in files; 6 commit-message paragraphs |
| 19 | Older PDF versions and page images of the manuscript that carry more of that material than the current text | As above | Removed | 60 file versions |
| 19d | Names and checksums of the collaborators' source files that were read, left in manifests after the files themselves were removed | As above | Path replaced by `<held back>`, its checksum by `"<removed>"` | 34 occurrences |
| 40 | Coordination records with that project's private Lean packages, and paragraphs naming those packages | As above | Removed or held back | 38 file versions, plus paragraphs in the occurrence count above |

### Held back until the source author has been told (rule 38)

| Rule | What | Why | How | Count |
|---|---|---|---|---|
| 38, 38b | Review records that discuss possible errors, misprints or normalization issues in X. Chen's **unpublished** author version, on which this work builds | He should see such comments before the public does | Replaced by "[held back until the source author has been told]"; JSON records with such content removed. TeX copies of the manuscript itself are not affected (38a) | 303 paragraphs; 36 records (in the 96 above) |

This hold is temporary. Once X. Chen has been told, these records will be
restored in an append-only update, recorded in the history.

### Private infrastructure and accounts

| Rule | What | Why | How | Count |
|---|---|---|---|---|
| 6, 24 | Home directories, host names, the network name of the hub machine, internal remote paths, a dynamic-DNS name and a private IP address | Private infrastructure | Replaced by `<HOME>`, `<HUB>`, `<REMOTES>`, `<IP>` | about 147,700 occurrences |
| 21 | Names of the maintainer's machines | Private infrastructure | Replaced by `<MACHINE>` | 12,567 occurrences |
| 30 | Remotes of private repositories (bibliography, knowledge base, wiki) | Private | Replaced by `<REMOTE>` | 37 occurrences |
| 37, 37b | Names of other private projects and their wiki pages | Private | Replaced by `<PRIVATE-PROJECT>`; files that search or pin them removed | 1,301 occurrences; 1 file version |
| 40 | Names of other private Lean packages | Private | Replaced by `<PRIVATE-PACKAGE>`. Public packages, this project's own packages and the named dependency `gaussian-chaos-lean` are kept | 4,740 occurrences |
| 3, 14, 20, 26, 31, 34 | Captures of AI-tool configuration, account and usage records, tool-home listings, quota evidence folders and account probes | Private operational data, including other people's account names | Removed | 443 file versions |
| 20, 36 | Account aliases, and fields recording an AI account's plan, subscription, utilization or limits | Private | Replaced by `<account>` or `"<removed>"` | 1,295 occurrences |
| 20b | The same aliases written together with neighbouring words, and file names built from them | Private | Replaced by `<account>` | 2,997 occurrences |
| 20c | The maintainer's own AI account names | Private | Replaced by `<account A>` and `<account B>` | 1,222 occurrences |
| 34, 34b, 36 | Paragraphs or tokens tying an address to an AI account, or reporting the state of an AI account | Private | Replaced by "[held back: AI account details]", `<account email removed>` or `<account removed>` | 1,101 + 72 + 3,850 |
| 6c | The name of a machine on the maintainer's home network, and paragraphs reporting its network observations | Private infrastructure | Name replaced by `<HOST>`; the paragraphs replaced by "[held back: private network details]" | 8 paragraphs |
| 6c-b | A partial address on the maintainer's home network | Private infrastructure | Replaced by `<IP>` | 8 occurrences |
| 6d | Home directories in the encoded form some AI tools use for their working folders | Private infrastructure | Replaced by `-<HOME>-` | 1,225 occurrences |
| 34c | Paragraphs, and fields of data records, that tie an AI account to its plan, its billing limits or its share of usage | Private | Paragraphs replaced by "[held back: AI account details]"; fields by `"<removed>"` or `<account>` | 3,069 paragraphs; 10 fields |
| 34d | The same ties written in compressed shorthand (a weekly percentage or a plan code next to an account name) | Private | Replaced by "[held back: AI account details]" | 4,896 paragraphs |
| 34e | Names of a paid plan or a service route, in paragraphs that name one of the maintainer's own AI accounts | Private | Only the plan or route name is replaced, by `<plan removed>`; the paragraph is kept | 5,030 occurrences |
| 34f | The same plan and route names anywhere outside the manuscripts, data records included | Private | Replaced by `<plan removed>` | 5,820 occurrences |
| 42 | The maintainer's AI account identifier, the name of its paid plan and its usage figures, in spellings the earlier rules missed (including glued forms) | Private | Replaced by `<account removed>`, `<plan removed>`, `<usage removed>` or `<HOME>`; the maintainer's e-mail address and homepage are kept | 16,348 occurrences |
| 14 | Email addresses of people other than Le Chen | Privacy | Replaced by `<email removed>`; Le Chen's own addresses kept | 546 occurrences |
| 11 | Web addresses carrying access identifiers | Login or session data | Replaced by `<URL with access parameters removed>` | none in the final run |

### Containers, links and private planning

| Rule | What | Why | How | Count |
|---|---|---|---|---|
| 4, 10, 17 | Compressed archives and bundles of review evidence, recognized by content signature at any nesting level | Too large for GitHub, and they contain material from the rows above | Replaced by small stub files giving the name, size and original SHA-256. **Not deposited in v1:** the archives are not published. A cleaned, separately audited deposit may follow later | 1,294 archive versions |
| 7 | Links into a private bibliography and private publication folders | They point outside this repository | The bibliography symlink is replaced by a frozen bibliography of the cited entries; other symlinks removed | 1 + 3 |
| 9, 27 | The maintainer's private release-planning notes, and paragraphs about planning with named third parties | Private | Removed or replaced by "[held back: private planning]" | 3,674 file versions; 62 paragraphs |
| 41 | A line in copies of the project's wiki page naming a researcher as a possible collaborator | Private planning about a named person | Removed | 36 file versions |
| 9, 39 | Commit-message lines about private planning, personal session links in commit trailers, and subjects of planning commits | Private | Lines removed; subjects replaced by a neutral subject | 260 lines; 402 trailers; 216 subjects |

## What was kept on purpose

- **The process record:** model names, review grades, failed routes and the
  reviewers' own words. This is the record the repository exists to show.
- **Quota and model-availability history,** in files and in commit
  messages (rules 28, 28b), and the model session transcripts (rule 16).
  These are part of how the work was done.
- **Tool layouts already stripped of identity** (`<HOME>/.local/…`, local
  service addresses; rule 24c), and the name of the university cluster.
- **Le Chen's own email addresses,** including the Auburn user name that is
  part of one of them.
- **Published papers in the bibliography,** including those of
  collaborators. Also the sentences of the current manuscript that cite the
  collaborators' project.
- **Illustrative media (exception to rule 18):** the AI-generated guitar
  illustration and two short videos in `media/guitar-sandstorm/`. They are
  dedicated to the public domain (CC0), with their LICENSE, provenance
  record and SHA-256 values, and they are kept at the author's request.
  Also the two historical page scans in `media/historical-astronomy/`,
  shown in the preface: Galileo, *Sidereus Nuncius* (1610), folio 23r (scan:
  University of Oklahoma Libraries), with a JPEG copy used in the PDF, and
  Huygens, *Systema Saturnium* (1659), page 55 (scan: Smithsonian
  Libraries). Both are in the public domain (Wikimedia Commons tag
  PD-old-100); their sources, licence tags and SHA-256 values are in the
  directory's provenance record, and they are kept at the author's request.
  Also the lean-pkg logo in `media/lean-pkg/`, shown beside the lean-pkg
  paragraph of Appendix F: the author's own tool, copied unchanged from its
  repository (Apache-2.0); source commit and SHA-256 value in the directory's
  provenance record. Kept at the author's request.
- **The scripts and data behind Appendix E** ("The AI work in numbers") in
  `scripts/ai-statistics/`: the review-run counts, the token totals and the
  kind and status of each recorded no-go, so that every number in that
  appendix can be rebuilt. The token totals (`tokens/token-totals.json`) are
  a deliberate, narrow exception to the removal of tool records above: they
  are sums per model, the same figures the appendix prints, with no account
  names or account state. The full no-go ledger behind the no-go counts is
  held back (rules 19 and 38); only its counts are published.
- **One commit message naming the Lean companion** (rule 22), which is
  public.

## How this was checked

- **Rules not published:** the filter and its rules are not published,
  because the rules necessarily contain the very strings they remove.
- **Automated checks:** the result was checked by an automated verifier
  (commit counts, file sizes, containers by content signature, OCR of
  every image, text of every PDF, email addresses, and the patterns of
  every rule above) and by a secret scanner.
- **Blind audits:** after every dry run, an AI system from a different
  model family audited the filtered history blind, without access to the
  original. The filter was revised until such an audit found nothing
  outside the decisions recorded here.
- **Final audit:** a final audit of the published history, with explicit
  coverage of every image, every PDF and every passage about other
  people's work, precedes publication.
- **The original:** the original history is retained privately by Le Chen.
