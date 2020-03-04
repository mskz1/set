# -*- coding: utf-8 -*-
import pytest

from allowable_stress import steel_ft, steel_fc_aij, steel_fc_bsl, steel_fb2_aij, steel_fb_aij, steel_fb1_aij, \
    steel_fb_bsl, steel_fs


def test_steel_ft():
    # print(steel_ft(235))
    # print(steel_ft(235)*1.5)
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
    # 学会式と基準法式の比較
    for l in range(0, 251):
        # print(l)
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
    assert steel_fb_aij(F=235, lb=5000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(71.2)
    assert steel_fb_aij(F=235, lb=6000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(59.3333)
    assert steel_fb_aij(F=235, lb=7000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(50.8571)
    assert steel_fb_aij(F=235, lb=8000, i=26.3, C=1, h=200, Af=100 * 8) == pytest.approx(44.5)

    assert steel_fb_aij(F=235, lb=5000, i=52, C=1, h=500, Af=200 * 16) == pytest.approx(116.2895)
    assert steel_fb_aij(F=235, lb=7000, i=52, C=1, h=500, Af=200 * 16) == pytest.approx(81.3714)


# @pytest.mark.skip('時間がかかるため')
def test_steel_fb_compare_aij_to_bsl():
    for f in [235, 325]:
        for lb in range(0, 9000, 500):
            for i in range(20, 100, 10):
                for c in [1, 1.75, 2.3]:
                    for h in [100, 200, 300, 400, 500, 600]:
                        for af in [50 * 7.5, 100 * 8, 150 * 12, 200 * 12]:
                            assert steel_fb_aij(F=f, lb=lb, i=i, C=c, h=h, Af=af) == pytest.approx(
                                steel_fb_bsl(F=f, lb=lb, i=i, C=c, h=h, Af=af), abs=0.17)


# @pytest.mark.skip('doc_test')
def test_steel_f_doc():
    print(steel_ft.__doc__)
    print(steel_fs.__doc__)
    print(steel_fc_bsl.__doc__)
    print(steel_fb_bsl.__doc__)
