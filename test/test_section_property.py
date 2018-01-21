# 断面諸量のテスト

from cross_section.section import SecParameter
from cross_section.section import SectionProperty
try:
    from . import ureg, Q_
except ImportError:
    from __init__ import ureg, Q_


def test_section_parameter():
    para = SecParameter('Zx', 250, 'cm3')
    assert (para.to('cm3') == 250)
    # assert (para.to('mm3') == 250000)


def test_section_property():
    prop = SectionProperty('Zx', Q_(250, 'cm**3'))
    assert (prop.value == Q_(250, 'cm**3'))
    assert (prop.value == Q_(250000, 'mm**3'))
    assert (prop.value != Q_(249, 'cm**3'))
    assert (prop.name == 'Zx')


