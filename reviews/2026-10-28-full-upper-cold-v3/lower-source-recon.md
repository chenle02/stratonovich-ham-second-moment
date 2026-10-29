Read-only source reconnaissance for the future lower-bound screen

Status: retrieval only, not an opened proof wave or a new theorem. The current
blind-reader gates still come first. No canonical wiki or source was edited.

The actual wiki concept pages Cameron--Martin and hypercontractivity were
read, followed by the temporal fractional-PAM paper digest/model statement
and primary SPDEForge source. Narrow searches were over content files with
rg. Plain system Python lacked frontmatter; the existing wiki .venv Python
successfully displayed CLI help. No dependency installation or system setup
change was made. Ranked CLI search was not run in the shared checkout,
because it can rebuild a stale index. No shared index write was performed.

Nearest inspected primary source: chen.hu.ea:18:temporal, Temporal asymptotics
for fractional parabolic Anderson model, Xia Chen,Yaozhong Hu,Jian Song,
Xiaoming Song. DOI10.1214/18-EJP139,author-source arXiv1604.03493. Existing
source ../SPDEForge/llm_pack/chen_hu_ea-18-temporal.tex,lines1335--1392,
Section6 opening and equation labelled hyper. Source SHA256: cdde81a4ed8d2c857364e32d6e4598aed7722b24667e8538698516d7bcb4d99a.
The citekey is already present in ../refdb/All.bib and its index/source/wiki
records exist;this is not a missing reference to enqueue again.

Useful boundary: its Mehler argument explicitly uses the Gaussian OU
semigroup and a Feynman--Kac representation for the fractional PARABOLIC
model. The interpolation parameter changes a diagonal self-interaction;
its endpoint rho=0 is Stratonovich,rho=1 Skorohod. The displayed
hypercontractivity estimate has input p strictly greater than1;the actual
application fixes p=2 and output q>=2. It does not supply a first-to-second
moment theorem for our hyperbolic model or the proposed rank-one covariance
perturbation. No transfer of its Feynman--Kac formula,normal ordering or exact
constants is made. This is a source mismatch to respect,not a global no-go.

The wiki concept summary's compressed author attribution should not be used
to identify this paper;the primary title/index and paper digest agree on the
four authors above. This illustrates why a concept page is a retrieval guide,
not a substitute for a version-bound primary statement.

[held back: collaborators' unpublished work]

Additional existing covariance-change source

The wiki paper page and primary source giacomin.lacoin.ea:10:marginal,
Giacomin--Lacoin--Toninelli,Marginal relevance of disorder for pinning models,
CPAM63(2),233--265(2010),DOI10.1002/cpa.20301,were inspected. Primary source
../SPDEForge/llm_pack/giacomin_lacoin_ea-10-marginal.tex,lines1145--1217,
labels eq:covar,eq:densit,eq:dets;SHA256 65bb97d42eb980e7746267352340d355ce7a2989ce66222711bdad677fd67629.
It explicitly changes finitely many Gaussian coordinates while leaving
the remainder independent and unchanged,and computes the determinant density
and its fractional-moment cost. Its covariance has weak negative off-diagonal
correlations with fixed unit marginals. This is useful density-cost background,
not the positive rank-one variance perturbation proposed here and not an HAM
first-moment lower theorem. No determinant estimate from it is imported into
the manuscript. Its wiki,Forge and refdb records already exist;no duplicate
request is enqueued. No Skorohod argument is developed.
