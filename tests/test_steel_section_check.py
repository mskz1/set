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


@pytest.mark.parametrize(
    "               sec,      F,     lkx,    lky,     term,  expected", [
        ("H-200x100x5.5x8", F_235, 3000.0, 3000.0, LONG_TERM, 138.9),  # An = 26.67 cm2, iy=2.24[cm]
        ("H-200x100x5.5x8", F_235, 3000.0, 3000.0, SHORT_TERM, 208.4),
        ("H-200x100x5.5x8", F_235, 6000.0, 1000.0, LONG_TERM, 305.6),
        ("H-200x100x5.5x8", F_235, 6000.0, 3000.0, LONG_TERM, 138.9),
        ("P89.1*2.8", F_235, 4000.0, 4000.0, SHORT_TERM, 61.86),
        ("P89.1*2.8", F_235, 4000.0, 2000.0, SHORT_TERM, 61.86),
        ("H-300x300x10x15", F_235, 8000.0, 8000.0, SHORT_TERM, 1420.40746),  # An = 118.5 cm2
        ("L65*6", F_235, 4000.0, 4000.0, SHORT_TERM, 10.68),
        ("L65*6", F_235, 12000.0, 4000.0, SHORT_TERM, 4.54),
        ("KP100*3.2", F_235, 4000.0, 4000.0, SHORT_TERM, 153.5),
        ("KP100*50*3.2", F_235, 4000.0, 4000.0, SHORT_TERM, 33.2),
        ("KP150*100*4.5", F_235, 5000.0, 5000.0, SHORT_TERM, 197.6),
        ("C100*50*2.3", F_235, 4000.0, 4000.0, SHORT_TERM, 16.7),
        ("C100*50*2.3", F_235, 12000.0, 4000.0, SHORT_TERM, 7.85),
        ("MZ100", F_235, 4000.0, 4000.0, SHORT_TERM, 22.8),
        ("MZ100", F_235, 12000.0, 4000.0, SHORT_TERM, 18.29),
    ])
def test_allowable_compressive_force_parame(sec, F, lkx, lky, term, expected):
    # 部材の圧縮耐力の算定
    assert allowable_compressive_force(sec, F, term, lkx=lkx, lky=lky) == pytest.approx(expected, abs=0.1)


@pytest.mark.parametrize(
    "sec, direc, lb,term,exp", [
        ("H-200x100x5.5x8", 'X', 0., LONG_TERM, 28.3566),  # An = 26.67 [cm2], Zx=181 [cm3], Zy=26.7 [cm3]
        ("H-200x100x5.5x8", 'X', 0., SHORT_TERM, 42.535),
        ("H-200x100x5.5x8", 'Y', 0., LONG_TERM, 4.183),
        ("H-200x100x5.5x8", 'Y', 0., SHORT_TERM, 6.2745),
        ("H-200x100x5.5x8", 'X', 3000., LONG_TERM, 16.258),
        ("H-200x100x5.5x8", 'Y', 3000., SHORT_TERM, 6.2745),
        ("H-600x200x11x17", 'X', 0., LONG_TERM, 394.799),  # An = 131.7 [cm2], Zx=2520 [cm3], Zy=227 [cm3]
        ("H-600x200x11x17", 'X', 0., SHORT_TERM, 592.2),
        ("H-600x200x11x17", 'X', 3000., LONG_TERM, 314.9),
        ("H-600x200x11x17", 'X', 6000., LONG_TERM, 199.85),
        ("H-300x300x10x15", 'X', 0., SHORT_TERM, 317.25),
        ("H-300x300x10x15", 'X', 4000., SHORT_TERM, 278.349),
        ("KP100*100*3.2", 'X', 0., LONG_TERM, 5.875),  # An = 12.13 [cm2], Zx=37.5 [cm3], Zy= 37.5[cm3]
        ("KP100*100*3.2", 'X', 4000., LONG_TERM, 5.875),
        ("KP150*100*4.5", 'X', 4000., LONG_TERM, 13.739),  # An = 21.17 [cm2], Zx=87.7 [cm3], Zy= 70.4[cm3]
        ("KP150*100*4.5", 'Y', 4000., LONG_TERM, 11.029),
    ])
def test_allowable_bending_moment_H_KP_section(sec, direc, lb, term, exp):
    # 部材の曲げ耐力の算定（H形鋼）
    assert allowable_bending_moment(sec=sec, direc=direc, lb=lb, term=term) == pytest.approx(exp, abs=0.01)


# @pytest.mark.skip("WIP")
def test_allowable_bending_moment():
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


@pytest.mark.parametrize(
    "　　　　　　　　　　sec, 　　　F, 　　　　term, 　N, Mx, My, Qx, Qy, 　lkx, 　lky, 　lb, expected", [
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
