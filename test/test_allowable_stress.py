# -*- coding: utf-8 -*-
import pytest

from allowable_stress import steel_ft, steel_fc


def test_steel_ft():
    # print(steel_ft(235))
    # print(steel_ft(235)*1.5)
    assert steel_ft(F=235) == 235 / 1.5
    assert steel_ft(F=235) * 1.5 == 235.
    assert steel_ft(F=325) == 325 / 1.5
    assert steel_ft(F=325) * 1.5 == 325.


def test_steel_fc():
    assert steel_fc(F=235, lambda_=0) == 235 / 1.5
    assert steel_fc(F=235, lambda_=50) == pytest.approx(135.274, abs=0.01)
    assert steel_fc(F=235, lambda_=100) == pytest.approx(86.273, abs=0.01)
    assert steel_fc(F=235, lambda_=150) == pytest.approx(41.5145, abs=0.01)
    assert steel_fc(F=235, lambda_=200) == pytest.approx(23.3519, abs=0.01)
    assert steel_fc(F=235, lambda_=250) == pytest.approx(14.9452, abs=0.01)
    assert steel_fc(F=325, lambda_=0) == 325 / 1.5
    assert steel_fc(F=325, lambda_=50) == pytest.approx(176.8466, abs=0.01)
    assert steel_fc(F=325, lambda_=100) == pytest.approx(93.2114, abs=0.01)
    assert steel_fc(F=325, lambda_=150) == pytest.approx(41.5145, abs=0.01)
    assert steel_fc(F=325, lambda_=200) == pytest.approx(23.3519, abs=0.01)
    assert steel_fc(F=325, lambda_=250) == pytest.approx(14.9452, abs=0.01)

@pytest.mark.skip()
def test_steel_fb():
    assert steel_fb1(F=235) == 0.
