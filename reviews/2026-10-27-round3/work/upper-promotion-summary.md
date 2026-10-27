# Status-only promotion

The exact writer report and unified diff are preserved byte-for-byte in
`../upper-promotion-evidence.tar.xz`, under their original work/ paths.
A unified diff legitimately contains space-only context lines; archiving
preserves them without relaxing the repository whitespace gate or modifying
hash-bearing evidence. Root verified the archive readback.

Root independently compared the accepted and promoted TeX: all14proof
environments, all27statement bodies and every equation block are unchanged.
Only title, abstract, headings and scope-status prose were promoted after
Opus acceptance. Exact before/after and artifact hashes, plus clean build
checks, are in `../upper-promotion-binding.json`.
