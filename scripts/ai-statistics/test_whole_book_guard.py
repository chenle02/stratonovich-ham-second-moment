#!/usr/bin/env python3
"""Test the whole-book guard of make_appendix.py.

Usage (from the repository root): python3 -I scripts/ai-statistics/test_whole_book_guard.py
Exits non-zero on the first failure. The committed ledger must pass; a row that
accepts the whole book, a row without the field, or a non-boolean value must be
refused. The upper-case field name is the one the ledger and its schema use; a
lower-case key alone must not satisfy the guard.
"""
import copy
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("make_appendix", os.path.join(HERE, "make_appendix.py"))
mod = importlib.util.module_from_spec(spec)
sys.modules["make_appendix"] = mod
spec.loader.exec_module(mod)

ledger = json.load(open(os.path.join(mod.ROOT, mod.LEDGER_DEFAULT)))
rows = ledger["rows"]
failures = []


def refused(rows_):
    try:
        mod.check_no_whole_book(rows_)
    except SystemExit:
        return True
    return False


def case(name, rows_, want_refused):
    got = refused(rows_)
    print(f"{'ok  ' if got == want_refused else 'FAIL'} {name}: refused={got}")
    if got != want_refused:
        failures.append(name)


case("committed ledger passes", rows, False)

r = copy.deepcopy(rows)
r[0][mod.WHOLE_BOOK] = True
case("one row true is refused", r, True)

r = copy.deepcopy(rows)
del r[-1][mod.WHOLE_BOOK]
case("one row without the field is refused", r, True)

r = copy.deepcopy(rows)
r[3][mod.WHOLE_BOOK] = "yes"
case("a non-boolean value is refused", r, True)

r = copy.deepcopy(rows)
del r[2][mod.WHOLE_BOOK]
r[2]["whole_book_accepted"] = False
case("a lower-case key alone is refused", r, True)

sys.exit(1 if failures else 0)
