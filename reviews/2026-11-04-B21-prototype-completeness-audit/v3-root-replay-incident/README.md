# Root replay incident and corrected verification

Date: 2026-11-04. Root made this harness error; the producer's held grammar
was correct.

Root tried to replay the held v3 schema builder by intercepting Path.write_text.
The builder also appends through Path.open("a"), which that interception missed.
Two attempted replays therefore appended two duplicate public-completeness
sections to operative-grammar.md. Root stopped concurrent audits, preserved
the complete10195-byte postimage, and restored only its own appended suffix.
The original6899-byte prefix independently matched the held manifest hash
77b0361c941bd6ad4f4084a1e9566931270f5859e2e43f6a046392d5300f2e0e.
All22 manifest members then matched their original hashes. Source28TeX/PDF and
source-map-bound prior reports were checked unchanged; no native path was
written. No provider ran.

The corrected replay uses a disposable full sibling copy, after inspecting
program write paths. Generation, schema/grammar,99purecontrols and40minimum
all reproduce their seven held output artifacts byte for byte. The whole
original held tree remains byte-identical before and after that replay.
The supplied executable repeats this isolated method; it never writes the
custody directory. The raw accidental postimage is incident evidence only.

Durable lesson: never assume intercepting one writer makes arbitrary code
read only. Inspect all output paths; use an isolated disposable copy or a
complete virtual filesystem. Hash the entire held tree before and after.
This incident does not justify a new native call, source change, confidence
promotion or retrospective report repair. Canonical lesson promotion remains
separate from this preserved project record.

V3's actual source associations and status-aware behavior were read by Root.
Its independent implementation/retention audit and exact future runtime/
projected-source binding still govern any next packet/readiness decision.
