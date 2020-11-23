from xs_section import *
import allowable_stress as allw
from section_check import tensile_allowable_force


def test_tensile_stress_check():
    db = make_all_section_db()
    sec = "H-200x100x5.5x8"
    F = 235
    term = "LONG"
    print(tensile_allowable_force(sec, F, term))
