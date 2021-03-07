# -*- coding: utf-8 -*-
import pytest

from allowable_stress import steel_ft, steel_fc_aij, steel_fc_bsl, steel_fb2_aij, steel_fb_aij, steel_fb1_aij, \
    steel_fb_bsl, steel_fs, calc_J, calc_Iw, calc_C, steel_fb_aij2005,steel_fb_aij2002


def test_steel_ft():
    assert steel_ft(F=235) == 235 / 1.5
    assert steel_ft(F=235) == pytest.approx(156.6667)
    assert steel_ft(F=235) * 1.5 == 235.
    assert steel_ft(F=325) == 325 / 1.5
    assert steel_ft(F=325) * 1.5 == 325.


def test_steel_fs():
    assert steel_fs(F=235) == 235 / (1.5 * 3 ** 0.5)
    assert steel_fs(F=235) == pytest.approx(90.4515)
    assert steel_fs(F=325) == pytest.approx(125.0926)


def test_steel_fc():
    assert steel_fc_aij(F=235, lambda_=0) == 235 / 1.5
    assert steel_fc_aij(F=235, lambda_=50) == pytest.approx(135.274, abs=0.01)
    assert steel_fc_aij(F=235, lambda_=100) == pytest.approx(86.273, abs=0.01)
    assert steel_fc_aij(F=235, lambda_=150) == pytest.approx(41.5145, abs=0.01)
    assert steel_fc_aij(F=235, lambda_=200) == pytest.approx(23.3519, abs=0.01)
    assert steel_fc_aij(F=235, lambda_=250) == pytest.approx(14.9452, abs=0.01)
    assert steel_fc_aij(F=325, lambda_=0) == 325 / 1.5
    assert steel_fc_aij(F=325, lambda_=50) == pytest.approx(176.8466, abs=0.01)
    assert steel_fc_aij(F=325, lambda_=100) == pytest.approx(93.2114, abs=0.01)
    assert steel_fc_aij(F=325, lambda_=150) == pytest.approx(41.5145, abs=0.01)
    assert steel_fc_aij(F=325, lambda_=200) == pytest.approx(23.3519, abs=0.01)
    assert steel_fc_aij(F=325, lambda_=250) == pytest.approx(14.9452, abs=0.01)


def test_steel_fc_compare_aij_to_bsl():
    # 学会式と基準法式の fc 比較
    for l in range(0, 251):
        assert steel_fc_aij(F=235, lambda_=l) == pytest.approx(steel_fc_bsl(F=235, lambda_=l), abs=0.055)


# @pytest.mark.skip()
def test_steel_fb():
    assert steel_fb2_aij(F=235, lb=0) == 235 / 1.5
    assert steel_fb2_aij(F=235, lb=1000, h=200, Af=800) == 235 / 1.5
    assert steel_fb2_aij(F=235, lb=2000, h=200, Af=800) == pytest.approx(235 / 1.5)
    assert steel_fb2_aij(F=235, lb=3000, h=200, Af=800) == pytest.approx(118.6666)
    assert steel_fb2_aij(F=235, lb=4000, h=200, Af=800) == pytest.approx(89.0)
    assert steel_fb2_aij(F=235, lb=5000, h=200, Af=800) == pytest.approx(71.2)
    assert steel_fb2_aij(F=235, lb=6000, h=200, Af=800) == pytest.approx(59.3333)
    assert steel_fb2_aij(F=235, lb=7000, h=200, Af=800) == pytest.approx(50.8571)
    assert steel_fb2_aij(F=235, lb=8000, h=200, Af=100 * 8) == pytest.approx(44.5)
    assert steel_fb2_aij(F=235, lb=1000, h=500, Af=3200) == 235 / 1.5
    assert steel_fb2_aij(F=235, lb=5000, h=500, Af=200 * 16) == pytest.approx(113.92)

    assert steel_fb1_aij(F=235, lb=1000, i=26.3, C=1) == pytest.approx(150.3529)
    assert steel_fb1_aij(F=235, lb=2000, i=26.3, C=1) == pytest.approx(131.4115)
    assert steel_fb1_aij(F=235, lb=3000, i=26.3, C=1) == pytest.approx(99.8425)
    assert steel_fb1_aij(F=235, lb=4000, i=26.3, C=1) == pytest.approx(55.6459)
    assert steel_fb1_aij(F=235, lb=5000, i=26.3, C=1) == pytest.approx(-1.1783, abs=0.001)
    assert steel_fb1_aij(F=235, lb=6000, i=26.3, C=1) == pytest.approx(-70.63, abs=0.001)
    assert steel_fb1_aij(F=235, lb=6000, i=26.3, C=1.75) == pytest.approx(26.7828, abs=0.001)
    assert steel_fb1_aij(F=235, lb=6000, i=26.3, C=2.3) == pytest.approx(57.8420, abs=0.001)
    assert steel_fb1_aij(F=235, lb=6000, i=52, C=2.3) == pytest.approx(131.3871, abs=0.001)
    assert steel_fb1_aij(F=235, lb=6000, i=52, C=1.75) == pytest.approx(123.4421, abs=0.001)
    assert steel_fb1_aij(F=235, lb=6000, i=52, C=1) == pytest.approx(98.5236, abs=0.001)

    assert steel_fb1_aij(F=325, lb=6000, i=52, C=1) == pytest.approx(105.4605, abs=0.001)

    assert steel_fb_aij(F=235, lb=2000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(235 / 1.5)
    assert steel_fb_aij(F=235, lb=3000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(118.6667)
    assert steel_fb_aij(F=235, lb=4000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(89.0)
    assert steel_fb_bsl(F=235, lb=4000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(89.0)

    assert steel_fb_aij(F=235, lb=5000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(71.2)
    assert steel_fb_aij(F=235, lb=6000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(59.3333)
    assert steel_fb_aij(F=235, lb=7000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(50.8571)
    assert steel_fb_aij(F=235, lb=8000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(44.5)

    assert steel_fb_aij(F=235, lb=5000, i=52, C=1, h=500, Af=200 * 16) == pytest.approx(116.2895)
    assert steel_fb_aij(F=235, lb=7000, i=52, C=1, h=500, Af=200 * 16) == pytest.approx(81.3714)

    from xs_section import make_all_section_db
    db = make_all_section_db()

    assert steel_fb_aij2002('H-500x200x10x16',db,lb=5000,M3=1) == pytest.approx(116.2895)
    assert steel_fb_aij2002('H-500x200x10x16',db,lb=7000,M3=1) == pytest.approx(81.3714)
    assert steel_fb_aij2002('H-200x100x5.5x8',db,lb=7000,M3=1) == pytest.approx(50.8571)


def test_saint_venent_calc_j():
    assert calc_J('H-200x100x5.5x8') == pytest.approx(4.48, abs=0.01)
    assert calc_J('H-300x150x6.5x9') == pytest.approx(9.95, abs=0.01)
    assert calc_J('H-500x200x10x16') == pytest.approx(70.7, abs=0.1)
    assert calc_J('H-900x300x16x28') == pytest.approx(558, abs=0.1)
    assert calc_J('[-100x50x5x7.5') == pytest.approx(1.72, abs=0.01)
    assert calc_J('[-125x65x6x8') == pytest.approx(2.96, abs=0.01)
    assert calc_J('[-300x90x9x13') == pytest.approx(19.5, abs=0.01)


def test_calc_Iw():
    assert calc_Iw('H-200x100x5.5x8', Iy=134) == pytest.approx(12300, abs=50)
    assert calc_Iw('H-300x150x6.5x9', Iy=508) == pytest.approx(108000, abs=500)
    assert calc_Iw('H-500x200x10x16', Iy=2140) == pytest.approx(1250000, abs=5000)
    assert calc_Iw('H-900x300x16x28', Iy=12600) == pytest.approx(24000000, abs=50000)
    assert calc_Iw('H-900x300x16x28', Iy=12600) == pytest.approx(240e+5, abs=5e+4)
    assert calc_Iw('[-100x50x5x7.5', Iy=26, Cy=1.54, An=11.92, Ix=188) == pytest.approx(405, abs=0.1)
    assert calc_Iw('[-125x65x6x8', Iy=61.8, Cy=1.90, An=17.11, Ix=424) == pytest.approx(1540, abs=5)
    assert calc_Iw('[-300x90x9x13', Iy=309, Cy=2.22, An=48.57, Ix=6440) == pytest.approx(46300, abs=1)


def test_calc_C():
    assert calc_C(M1=0, M2=0) == 1
    assert calc_C(M1=1, M2=1) == 2.3
    assert calc_C(M1=1, M2=-1) == 1.0
    assert calc_C(M1=2, M2=1) == 2.3


# @pytest.mark.skip('Not implemented yet')
def test_steel_fb_aij2005():
    from xs_section import make_all_section_db
    db = make_all_section_db()
    assert steel_fb_aij2005('H-200x100x5.5x8', db) == 235 / 1.5
    assert steel_fb_aij2005('H-200x100x5.5x8', db, lb=1000, M3=1) == pytest.approx(144.9, abs=0.1)
    assert steel_fb_aij2005('H-200x100x5.5x8', db, lb=2000, M3=1) == pytest.approx(114.0, abs=0.1)
    assert steel_fb_aij2005('H-200x100x5.5x8', db, lb=4000, M3=1) == pytest.approx(71.8, abs=0.1)
    assert steel_fb_aij2005('H-200x100x5.5x8', db, lb=6000, M3=1) == pytest.approx(45.4, abs=0.1)

    assert steel_fb_aij2005('H-500x200x10x16', db, lb=5000, M3=1) == pytest.approx(96.0, abs=0.1)
    assert steel_fb_aij2005('H-500x200x10x16', db, lb=7000, M3=1) == pytest.approx(72.5, abs=0.1)


# @pytest.mark.skip('時間がかかるため')
def test_steel_fb_compare_aij_to_bsl():
    # 学会式と基準法式の fb 比較
    for f in [235, 325]:
        for lb in range(0, 9000, 500):
            for i in range(20, 100, 10):
                for c in [1, 1.75, 2.3]:
                    for h in [100, 200, 300, 400, 500, 600]:
                        for af in [50 * 7.5, 100 * 8, 150 * 12, 200 * 12]:
                            assert steel_fb_aij(F=f, lb=lb, i=i, C=c, h=h, Af=af) == pytest.approx(
                                steel_fb_bsl(F=f, lb=lb, i=i, C=c, h=h, Af=af), abs=0.17)


@pytest.mark.skip('__doc__ の出力例')
def sample_test_steel_f_doc():
    print(steel_ft.__doc__)
    print(steel_fs.__doc__)
    print(steel_fc_bsl.__doc__)
    print(steel_fb_bsl.__doc__)


@pytest.mark.skip('プロットサンプル')
def sample_test_data_plot():
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = []
    y = []
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=235, lb=lb, i=1, C=1, h=10, Af=1))
    ax.plot(x, y)

    x = []
    y = []
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=235, lb=lb, i=1, C=2.3, h=10, Af=1))
    ax.plot(x, y)

    x = []
    y = []
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=235, lb=lb, i=1, C=2.3, h=4, Af=1))
    ax.plot(x, y)

    ax.grid()
    ax.set_ylim(0, 160)
    ax.set_xlim(0, 250)
    plt.show()
