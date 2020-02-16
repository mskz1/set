# -*- coding: utf-8 -*-
import pytest

from .xs_section import *


def test_xs_H_sec_name():
    assert xs_section_name('HS20') == 'H-200x100x5.5x8'
    assert xs_section_name('HS15') == 'H-150x75x5x7'
    assert xs_section_name('hs15') == 'H-150x75x5x7'
    # with pytest.raises(KeyError):
    #     xs_section_name('hs100')
    assert xs_section_name('hs100') == 'Section_Not_Defined'


# @pytest.mark.skip()
def test_xs_H_sec_property():
    assert set(xs_section_property('HS20')) == {'H', 'An', 'Ix', 'Iy', 'ix', 'iy', 'Zx', 'Zy'}
    assert xs_section_property('HS20', 'An') == 26.67  # unit:cm2
    assert xs_section_property('H-200x100x5.5x8', 'An') == 26.67  # unit:cm2
