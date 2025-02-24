# -*- coding: utf-8 -*-
import pytest

# print(sys.path)
# print(os.environ['PYTHONPATH'])

from src.allowable_stress import steel_ft, steel_fc_aij, steel_fc_bsl, steel_fb2_aij, steel_fb_aij, steel_fb1_aij, \
    steel_fb_bsl, steel_fs, calc_J, calc_Iw, calc_C, steel_fb_aij2005, steel_fb_aij2002


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
    # todo:Sチャートとあわない？ 2024-0225
    # assert steel_fb_aij(F=235, lb=3500, i=32.7, C=1, h=248, Af=124 * 8) == pytest.approx(152/1.5)
    # assert steel_fb_bsl(F=235, lb=3500, i=32.7, C=1, h=248, Af=124 * 8) == pytest.approx(152/1.5)

    from src.xs_section import make_all_section_db
    db = make_all_section_db()

    assert steel_fb_aij2002('H-500x200x10x16', db, lb=5000, M3=1) == pytest.approx(116.2895)
    assert steel_fb_aij2002('H-500x200x10x16', db, lb=7000, M3=1) == pytest.approx(81.3714)
    assert steel_fb_aij2002('H-200x100x5.5x8', db, lb=7000, M3=1) == pytest.approx(50.8571)


def test_saint_venent_calc_j():
    assert calc_J('H-200x100x5.5x8') == pytest.approx(4.48, abs=0.01)
    assert calc_J('H-300x150x6.5x9') == pytest.approx(9.95, abs=0.01)
    assert calc_J('H-500x200x10x16') == pytest.approx(70.7, abs=0.1)
    assert calc_J('H-900x300x16x28') == pytest.approx(558, abs=0.1)
    assert calc_J('[-100x50x5x7.5') == pytest.approx(1.72, abs=0.01)
    assert calc_J('[-125x65x6x8') == pytest.approx(2.96, abs=0.01)
    assert calc_J('[-300x90x9x13') == pytest.approx(19.5, abs=0.01)
    assert calc_J('C-100x50x20x2.3') == pytest.approx(0.0936, abs=0.001)


def test_calc_Iw():
    assert calc_Iw('H-200x100x5.5x8', Iy=134) == pytest.approx(12300, abs=50)
    assert calc_Iw('H-300x150x6.5x9', Iy=508) == pytest.approx(108000, abs=500)
    assert calc_Iw('H-500x200x10x16', Iy=2140) == pytest.approx(1250000, abs=5000)
    assert calc_Iw('H-900x300x16x28', Iy=12600) == pytest.approx(24000000, abs=50000)
    assert calc_Iw('H-900x300x16x28', Iy=12600) == pytest.approx(240e+5, abs=5e+4)
    assert calc_Iw('[-100x50x5x7.5', Iy=26, Cy=1.54, An=11.92, Ix=188) == pytest.approx(405, abs=0.1)
    assert calc_Iw('[-125x65x6x8', Iy=61.8, Cy=1.90, An=17.11, Ix=424) == pytest.approx(1540, abs=5)
    assert calc_Iw('[-300x90x9x13', Iy=309, Cy=2.22, An=48.57, Ix=6440) == pytest.approx(46300, abs=1)
    assert calc_Iw('C-100x50x20x2.3', Iy=19, Cy=1.86, An=5.17, Ix=80.7) == pytest.approx(254.75, abs=0.1)


@pytest.mark.parametrize(
    "M1, M2, M3, expected", [
        # (0, 0, 0, 1.0),
        (0, 0, 0, 1.75),  # 2025-0202 change
        (1, 1, 0, 2.3),
        (1, -1, 0, 1.0),
        (1, 0, 0, 1.75),
        (2, 1, 0, 2.3),  # 複曲率 M2/M1:正
        (2, -1, 0, 1.3),  # 単曲率 M2/M1:負
        (3, -1, 0, 1.4333333333333333),  # 単曲率 M2/M1:負
        (5, -4, 0, 1.1019999999999999),  # 単曲率 M2/M1:負
    ])
def test_calc_C(M1, M2, M3, expected):
    assert calc_C(M1=M1, M2=M2, M3=M3) == expected


@pytest.mark.parametrize(
    "              sec,       lb, M1, M2, M3, expected, abs_tol", [
        ('H-200x100x5.5x8', 0.00, 0., 0., 0., 235 / 1.5, 0.001),
        ('H-200x100x5.5x8', 1000, 0., 0., 1, 144.9, 0.1),  # 中間モーメントがmax -> C=1
        ('H-200x100x5.5x8', 1000, 0., 0., 0, 153.09, 0.1),  # 中間モーメントがmax -> C=1
        ('H-200x100x5.5x8', 2000, 0., 0., 1, 114.0, 0.1),
        ('H-200x100x5.5x8', 4000, 0., 0., 1, 71.8, 0.1),
        ('H-200x100x5.5x8', 6000, 0., 0., 1, 45.4, 0.1),
        ('H-500x200x10x16', 5000, 0., 0., 1, 96.0, 0.1),
        ('H-500x200x10x16', 7000, 0., 0., 1, 72.5, 0.1),
        ('[-100x50x5x7.5', 0.000, 0., 0., 1, 235 / 1.5, 0.001),
        ('[-100x50x5x7.5', 3000., 0., 0., 1, 90.53, 0.1),
        ('C-100x50x20x2.3', 0.00, 0., 0., 1, 235 / 1.5, 0.001),
        ('C-100x50x20x2.3', 3000, 0., 0., 1, 67.09, 0.1),
        ('□P-150x150x6', 3000.00, 0., 0., 1, 235/1.5, 0.1),
        ('P-89.1x4.5', 3000.0000, 0., 0., 1, 235/1.5, 0.1),

        # 中間モーメントが最大ではない場合
        ('H-200x100x5.5x8', 4000, 2., -1, 0, 86.04, 0.1),  # 単曲率（M2/M1:負）
        ('H-200x100x5.5x8', 4000, 2., 1, 0, 129.87, 0.1),  # 複曲率（M2/M1:正）
        ('H-200x100x5.5x8', 4000, 2., 0, 0, 105.37, 0.1),  #
        ('H-200x100x5.5x8', 4000, 10, -9, 0, 74.23, 0.1),  #
        ('H-200x100x5.5x8', 4000, 10, 9, 0, 134.15, 0.1),  #
        ('H-200x100x5.5x8', 8000, 2., -1, 0, 42.69, 0.1),  # 単曲率（M2/M1:負）
        ('H-248x124x5x8', 1760.0, 60.49, -36.29, 0, 141.91, 0.1),  # 単曲率（M2/M1:負）

    ])
def test_steel_fb_aij2005(sec, lb, M1, M2, M3, expected, abs_tol):
    from src.xs_section import make_all_section_db
    db = make_all_section_db()
    assert steel_fb_aij2005(shape_name=sec, db=db, lb=lb, M1=M1, M2=M2, M3=M3) == pytest.approx(expected, abs=abs_tol)


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
def test_sample_data_plot():
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
