# Proof-index identity and main-report adjudication

This is an author locator correction, not a mathematical review or proof
acceptance. All 28 manuscript source files were compared byte-for-byte with
scientific commit `887fbfbe0fa4368d6b32a436615d73349b2445d8`; all match.
The old frozen index and inventory remain immutable.

## All 213 identities checked

Every proof's actual final “This proves” reference was resolved to its
corresponding statement, and the statement environment type was checked.
Optional deferred proof headings were checked against the closing reference.
No identity was inferred from the nearest preceding label. The full set of
213 proof starts equals the inventory; all original IDs, source paths, start
lines and raw proof-body hashes are preserved. The successor also records
exact end lines, statement spans and the identity evidence for every row.

Only one old locator is wrong:

- **PROOF093:** `notes/integrated_actual_operator_driver.tex:555–591`
  proves **P:actual-operator-driver**, whose statement is at lines 27–55.
  Both the deferred heading at line 555 and final closing reference at
  line 590 identify that proposition. The old index incorrectly copied
  **L:driver-holder-limit**, which owns the preceding, distinct PROOF092.
  These are not duplicate proof bodies.

All other 212 closing identities agree with the old inventory. The optional
heading of PROOF093 is the only deferred proof heading in the 213 blocks.
For legacy raw hashes, the optional heading is included between the literal
begin-proof and end-proof markers, exactly as in the old inventory. The new
JSON additionally records the hash of the body with that heading excluded.
This is hash-definition clarification, not a scientific byte change.

## Compare the actual report without upgrading it

The raw report's P001–P213 ordinals were matched to PROOF001–PROOF213.
There are 211 exact label matches, one harmless abbreviation and one actual
locator mismatch:

- P001 says “Jensen” rather than the exact label **P:Jensen**. Preserve the
  raw label and its CK status; the ordinal and proof identity are unambiguous.
- P093 says “(dup of P092)” with status **NF**. That wording follows the
  flawed supplied locator but is not the actual proof identity. It does not
  establish that the deferred proposition proof was checked. Preserve the
  raw wording and NF status; do not transfer another proof's coverage.

Literal row counts are **30 CK, 58 CK·NH and 125 NF**. The report's summary
of 78 checked/qualified and 135 NF is inconsistent with its own rows.
The legend defines CK and NF but does not define CK·NH. Its 58 qualified
rows must not be relabelled fully CHECKED or PASS. The arithmetic count
30+58=88 is a count of two distinct strings, not an acceptance measure.

The report remains MEDIUM, its full-main-theorem conclusion remains
INCONCLUSIVE at the HIGH gate, and its source/image/whole-proof limitations
are unchanged. A corrected locator supplies no new reviewer vote or coverage.
The successor JSON retains every raw report label, status, note and line;
all accepted-coverage flags remain false.
