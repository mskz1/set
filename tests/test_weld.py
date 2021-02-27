# -*- coding: utf-8 -*-
import pytest

from weld import fillet_weld_size, fillet_weld_strength


def test_fillet_welding_size():
    # Ｔ継手 2019.1.28
    assert fillet_weld_size(2.3, weld_type='T') == 3.5
    assert fillet_weld_size(2.3) == 3.5
    assert fillet_weld_size(3.2) == 4.5
    assert fillet_weld_size(4.0) == 6.0
    assert fillet_weld_size(4.5) == 6.0
    assert fillet_weld_size(6) == 6.0
    assert fillet_weld_size(9) == 7.0
    assert fillet_weld_size(12) == 9.0
    assert fillet_weld_size(16) == 12.0
    assert fillet_weld_size(19) == 14.0
    assert fillet_weld_size(20) == 14.0
    assert fillet_weld_size(6.5) == 7.0

    with pytest.raises(ValueError):
        assert fillet_weld_size(15, weld_type='WRAP')
        assert fillet_weld_size(15, weld_type='OVER')

    # 重ね継手 全社標準　2019.1.28
    assert fillet_weld_size(2.3, weld_type='L') == 2.0
    assert fillet_weld_size(3.2, weld_type='L') == 2.5
    assert fillet_weld_size(4.0, weld_type='L') == 3.5
    assert fillet_weld_size(4.5, weld_type='L') == 4.0
    assert fillet_weld_size(6.0, weld_type='L') == 5.0
    assert fillet_weld_size(9.0, weld_type='L') == 7.0
    assert fillet_weld_size(12.0, weld_type='L') == 9.0
    assert fillet_weld_size(16.0, weld_type='L') == 12.0


def test_fillet_welding_strength():
    assert fillet_weld_strength(L=100, S=6) == pytest.approx(33430.88999)
    assert fillet_weld_strength(L=100, S=6, n=2) == pytest.approx(66861.77997)
    assert fillet_weld_strength(L=100, S=9) == pytest.approx(46727.26669)



