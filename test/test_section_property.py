# 断面諸量のテスト
import pytest

from cross_section.section import SecParameter
from cross_section.section import SectionProperty

try:
    from . import ureg, Q_
except ImportError:
    from __init__ import ureg, Q_


def test_section_parameter():
    # Pintを使わない場合を試作中
    Zx = SecParameter('Zx', 250, 'cm3')
    Ix = SecParameter('Ix', 3400., 'cm4')
    assert (Zx.get('cm3') == 250)
    assert Zx.get() == 250
    assert Zx.get('mm3') == 250000
    Zx.set(100., 'cm3')
    assert Zx.get('mm3') == 100000
    assert Ix.get('m4') == 0.000034
    H = SecParameter('H', 400., 'mm')
    assert H.get('cm') == 40.
    assert H.get('m') == 0.4


def test_section_property():
    # Pintを使う場合
    prop = SectionProperty('Zx', Q_(250, 'cm**3'))
    assert (prop.value == Q_(250, 'cm**3'))
    assert (prop.value == Q_(250000, 'mm**3'))
    assert (prop.value != Q_(249, 'cm**3'))
    assert (prop.name == 'Zx')
    assert prop.value.magnitude == 250.

