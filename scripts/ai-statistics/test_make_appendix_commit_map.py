"""make_appendix.original_commit: the book prints the development-history commit on both trees.

Run: python3 -m pytest -q scripts/ai-statistics/test_make_appendix_commit_map.py
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("make_appendix", HERE / "make_appendix.py")
ma = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ma)

ORIG = "c2359a4f341b36fff87e7e89782549adb2b4e567"
PUB = "f1cfa7b1bf1683409630508d075e9afdddef5039"


def write_map(tmp, rows):
    p = tmp / "commit-map.tsv"
    p.write_text("original_commit\tpublished_commit\n" + "".join(f"{a}\t{b}\n" for a, b in rows))
    return str(p)


def test_public_commit_maps_back_to_the_original(tmp_path):
    m = write_map(tmp_path, [(ORIG, PUB)])
    assert ma.original_commit(PUB[:8], PUB, m) == ORIG[:8]


def test_private_tree_without_a_map_keeps_the_commit(tmp_path):
    assert ma.original_commit(ORIG[:8], ORIG, str(tmp_path / "absent.tsv")) == ORIG[:8]


def test_unmapped_and_zero_entries_keep_the_commit(tmp_path):
    m = write_map(tmp_path, [("0" * 40, PUB)])
    assert ma.original_commit(PUB[:8], PUB, m) == PUB[:8]
    m = write_map(tmp_path, [(ORIG, "e" * 40)])
    assert ma.original_commit(PUB[:8], PUB, m) == PUB[:8]
