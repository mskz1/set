from section_check import allowable_tensile_force
from section_check import allowable_compressive_force
import pytest

F_235 = 235  # N/mm2
F_325 = 325
LONG_TERM = "LONG"
SHORT_TERM = "SHORT"


def test_allowable_tensile_force():
    sec = "H-200x100x5.5x8"  # An = 26.67 cm2
    assert allowable_tensile_force(sec, F_235, LONG_TERM) == pytest.approx(417.83)
    assert allowable_tensile_force(sec, F_235, SHORT_TERM) == pytest.approx(626.745)
    assert allowable_tensile_force(sec, F_325, LONG_TERM) == pytest.approx(577.85)
    assert allowable_tensile_force(sec, F_325, SHORT_TERM) == pytest.approx(866.775)

    sec = "L65*6"  # An = 7.527 cm2
    assert allowable_tensile_force(sec, F_235, LONG_TERM) == pytest.approx(117.923)
    assert allowable_tensile_force(sec, F_235, SHORT_TERM) == pytest.approx(176.8845)


# @pytest.mark.skip("WIP")
def test_allowable_compressive_force():
    sec = "H-200x100x5.5x8"  # An = 26.67 cm2, iy=2.24[cm]
    lk = 300.
    assert allowable_compressive_force(sec, F_235, LONG_TERM, lk) == pytest.approx(138.9, abs=0.1)
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lk) == pytest.approx(208.4, abs=0.1)

    sec = "P89.1*2.8"
    lk = 400.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lk) == pytest.approx(61.86, abs=0.1)



@pytest.mark.skip("WIP")
def test_allowable_bending_moment():
    sec = "H-200x100x5.5x8"  # An = 26.67 [cm2], Zx=181 [cm3]

    pass
