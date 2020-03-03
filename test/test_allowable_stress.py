# -*- coding: utf-8 -*-
import pytest

from allowable_stress import steel_ft, steel_fc_aij, steel_fc_bsl, steel_fb2_aij, steel_fb_aij


def test_steel_ft():
    # print(steel_ft(235))
    # print(steel_ft(235)*1.5)
    assert steel_ft(F=235) == 235 / 1.5
    assert steel_ft(F=235) * 1.5 == 235.
    assert steel_ft(F=325) == 325 / 1.5
    assert steel_ft(F=325) * 1.5 == 325.


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
