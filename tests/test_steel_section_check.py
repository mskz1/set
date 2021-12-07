from section_check import allowable_tensile_force
from section_check import allowable_compressive_force
from section_check import allowable_bending_moment
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
    # TODO WIP チェック必要。関数引数もチェック　座屈長さ X方向とY方向　両方指定時
    sec = "H-200x100x5.5x8"  # An = 26.67 cm2, iy=2.24[cm]
    lk = 300.  # cm?
    assert allowable_compressive_force(sec, F_235, LONG_TERM, lky=lk) == pytest.approx(138.9, abs=0.1)
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lky=lk) == pytest.approx(208.4, abs=0.1)

    lk_x = 600.  # cm?
    lk_y = 100.  # cm?
    assert allowable_compressive_force(sec, F_235, LONG_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(138.9, abs=0.1)
    # 305.8?

    sec = "P89.1*2.8"
    lk = 400.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lky=lk) == pytest.approx(61.86, abs=0.1)

    sec = "L65*6"
    lk = 400.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lky=lk) == pytest.approx(10.68, abs=0.1)

    sec = "KP100*3.2"
    lk = 400.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lky=lk) == pytest.approx(153.5, abs=0.1)


# @pytest.mark.skip("WIP")
def test_allowable_bending_moment():
    sec = "H-200x100x5.5x8"  # An = 26.67 [cm2], Zx=181 [cm3], Zy=26.7 [cm3]
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(28.3566, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='SHORT') == pytest.approx(42.535, abs=0.01)

    assert allowable_bending_moment(sec, direc='Y', lb=lb, term='LONG') == pytest.approx(4.183, abs=0.01)
    assert allowable_bending_moment(sec, direc='Y', lb=lb, term='SHORT') == pytest.approx(6.2745, abs=0.01)

    lb = 3000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(16.258, abs=0.01)
    assert allowable_bending_moment(sec, direc='Y', lb=lb, term='SHORT') == pytest.approx(6.2745, abs=0.01)

    sec = "H-600x200x11x17"  # An = 131.7 [cm2], Zx=2520 [cm3], Zy=227 [cm3]
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(394.799, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='SHORT') == pytest.approx(592.2, abs=0.01)

    lb = 3000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(314.9, abs=0.01)

    lb = 6000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(199.85, abs=0.01)

    sec = "KP100*100*3.2"  # An = 12.13 [cm2], Zx=37.5 [cm3], Zy= 37.5[cm3]
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(5.875, abs=0.01)

    sec = "P114.3*4.5"  # An = 15.5 [cm2], Zx= 41[cm3], Zy= [cm3]
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(6.42, abs=0.01)




    sec = "MZ100"  # An = 11.92 [cm2], Zx=37.6 [cm3], Zy= 7.52[cm3]
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(5.89, abs=0.01)

    lb = 2000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(4.07, abs=0.01)

    lb = 4000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(2.89, abs=0.01)


    # チャートでは、u,v方向に荷重を分解し、(σu+σv)/ft で検定している。
    # TODO 山形鋼　主軸がX、Y軸から傾いているため、処理が必要
    # 2021-0425 一旦コメントアウト
    # sec = "L90*7"  # An = 12.2 [cm2], Zx= [cm3], Zy= [cm3]
    # lb = 0.  # mm
    # assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(1.873, abs=0.01)
    #



    # TODO : add code
    #  断面による計算の違いを考慮

