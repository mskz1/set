from src.section_check import allowable_tensile_force
from src.section_check import allowable_compressive_force
from src.section_check import allowable_bending_moment
from src.section_check import section_check
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
    lk = 3000.  # mm
    assert allowable_compressive_force(sec, F_235, LONG_TERM, lkx=lk, lky=lk) == pytest.approx(138.9, abs=0.1)
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk, lky=lk) == pytest.approx(208.4, abs=0.1)

    lk_x = 6000.  # mm
    lk_y = 1000.  # mm
    assert allowable_compressive_force(sec, F_235, LONG_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(305.6, abs=0.1)

    lk_x = 6000.  # mm
    lk_y = 3000.  # mm
    assert allowable_compressive_force(sec, F_235, LONG_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(138.9, abs=0.1)

    sec = "P89.1*2.8"
    lk = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk, lky=lk) == pytest.approx(61.86, abs=0.1)

    lk_x = 4000.
    lk_y = 2000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(61.86, abs=0.1)

    sec = "H-300x300x10x15"  # An = 118.5 cm2
    lk_x = 8000.
    lk_y = 8000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(1420.40746, abs=0.1)

    sec = "L65*6"
    lk = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk, lky=lk) == pytest.approx(10.68, abs=0.1)

    lk_x = 12000.
    lk_y = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(4.54, abs=0.01)

    sec = "KP100*3.2"
    lk = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk, lky=lk) == pytest.approx(153.5, abs=0.1)

    sec = "KP100*50*3.2"
    lk = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk, lky=lk) == pytest.approx(33.2, abs=0.1)

    sec = "KP150*100*4.5"
    lk = 5000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk, lky=lk) == pytest.approx(197.6, abs=0.1)

    sec = "C100*50*2.3"
    lk_x = 4000.
    lk_y = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(16.7, abs=0.1)
    lk_x = 12000.
    lk_y = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(7.85, abs=0.01)

    sec = "MZ100"
    lk_x = 4000.
    lk_y = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(22.8, abs=0.1)
    lk_x = 12000.
    lk_y = 4000.
    assert allowable_compressive_force(sec, F_235, SHORT_TERM, lkx=lk_x, lky=lk_y) == pytest.approx(18.29, abs=0.1)


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

    sec = "H-300x300x10x15"
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='SHORT') == pytest.approx(317.25, abs=0.01)
    lb = 4000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='SHORT') == pytest.approx(278.349, abs=0.01)

    sec = "KP100*100*3.2"  # An = 12.13 [cm2], Zx=37.5 [cm3], Zy= 37.5[cm3]
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(5.875, abs=0.01)

    lb = 4000.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(5.875, abs=0.01)

    sec = "KP150*100*4.5"  # An = 21.17 [cm2], Zx=87.7 [cm3], Zy= 70.4[cm3]
    lb = 4000.  # mm
    assert allowable_bending_moment(sec, lb=lb, direc='X', term='LONG') == pytest.approx(13.739, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, direc='Y', term='LONG') == pytest.approx(11.029, abs=0.01)

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

    sec = "C100*50*2.3"  # An = 5.172 [cm2], Zx= 16.1[cm3], Zy= 6.06[cm3]
    lb = 0.  # mm
    # TODO:C形鋼の実装 fb=ft とする場合と、fb低減する場合
    assert allowable_bending_moment(sec, lb=lb, term='LONG') == pytest.approx(2.522, abs=0.01)

    # チャートでは、u,v方向に荷重を分解し、(σu+σv)/ft で検定している。
    # TODO 山形鋼　主軸がX、Y軸から傾いているため、処理が必要　fbはftとして良いか？　断面形状にもよるか。
    # 2022-0109 一旦コメントアウト
    sec = "L90*7"  # An = 12.2 [cm2], Zx= 14.2[cm3], Zy= 14.2[cm3], Ix=Iy=93[cm4],Iu=148,Iv=38.3
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='X') == pytest.approx(2.22466, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='U') == pytest.approx(3.643, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='V') == pytest.approx(1.724, abs=0.01)

    sec = "L90*10"  # An =  [cm2], Zx= [cm3], Zy= [cm3], Ix=Iy=[cm4],Iu=,Iv=
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='X') == pytest.approx(3.055, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='U') == pytest.approx(4.898, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='V') == pytest.approx(2.228, abs=0.01)

    sec = "L75*6"  # An =  [cm2], Zx= [cm3], Zy= [cm3], Ix=Iy=[cm4],Iu=,Iv=
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='X') == pytest.approx(1.326, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='U') == pytest.approx(2.162, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='V') == pytest.approx(1.021, abs=0.01)

    sec = "L100*75*7"  # An =  [cm2], Zx= [cm3], Zy= [cm3], Ix=Iy=[cm4],Iu=,Iv=
    lb = 0.  # mm
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='X') == pytest.approx(2.663, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='Y') == pytest.approx(1.566, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='U') == pytest.approx(3.238, abs=0.01)
    assert allowable_bending_moment(sec, lb=lb, term='LONG', direc='V') == pytest.approx(1.377, abs=0.01)

    # TODO : add code
    #  断面による計算の違いを考慮　山形鋼の各ポイントで、圧縮側、引張側で不利な判定


# @pytest.mark.skip('WIP')
def test_section_check():
    N = 10.  # kN
    Mx = 20.0  # kN*m
    sec = "H-200x100x5.5x8"  # An = 26.67 cm2
    assert section_check(sec, F_235, SHORT_TERM, N, Mx) == pytest.approx(0.48615, abs=0.001)
    N = -10.  # kN
    Mx = 20.0  # kN*m
    sec = "H-200x100x5.5x8"  # An = 26.67 cm2
    assert section_check(sec, F_235, SHORT_TERM, N, Mx) == pytest.approx(0.48615, abs=0.001)


@pytest.mark.parametrize(
    "sec, F, term, N, Mx, My,                                 Qx, Qy, lkx, lky, lb, expected",
    [
        ('H-200x100x5.5x8', F_235, SHORT_TERM, 10., 20., 0., 0., 0., 000., 000., 000., 0.48615),
        ('H-200x100x5.5x8', F_235, SHORT_TERM, 0., 20., 0., 0., 0., 000., 000., 4000., 1.0253068),
        ('H-200x100x5.5x8', F_235, SHORT_TERM, -10., 20., 0., 0., 0., 000., 000., 000., 0.48615),
        ('H-200x100x5.5x8', F_235, SHORT_TERM, -10., 20., 0., 0., 0., 5000., 5000., 000., 0.60346),
        ('H-200x100x5.5x8', F_235, SHORT_TERM, -10., 20., 0., 0., 0., 8000., 2000., 4000., 1.053292),
        ('H-200x100x5.5x8', F_235, SHORT_TERM, -5., 5., 3., 0., 0., 8000., 4000., 4000., 0.77709),
        ('H-300x300x10x15', F_235, SHORT_TERM, -200., 100., 0., 0., 0., 8000., 8000., 4000., 0.5000659),
        ('H-300x300x10x15', F_235, SHORT_TERM, -200., 100., 0., 0., 0., 000., 000., 000., 0.38702855),
        ('H-300x300x10x15', F_235, SHORT_TERM, -200., 100., 50., 0., 0., 8000., 8000., 4000., 0.97287916),
        ('□P-150x150x4.5', F_235, SHORT_TERM, -80., 7., 3., 0., 0., 4000., 4000., 000., 0.528169),
    ])
def test_section_check_paramet(sec, F, term, N, Mx, My, Qx, Qy, lkx, lky, lb, expected):
    assert section_check(sec, F, term, N, Mx, My, Qx, Qy, lkx, lky, lb) == pytest.approx(expected, abs=0.001)
