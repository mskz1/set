# -*- coding: utf-8 -*-
import pytest

from bolt import htb_spec
from bolt import ParameterError
from bolt import HTB_SIZES, HTB_STRENGTHS


def test_bolt_spec():
    assert htb_spec(size='M16', prop_name='QA', term='LONG') == 30.2
    assert htb_spec(size='m16', prop_name='Qa', term='Long') == 30.2
    assert htb_spec(size='M16', prop_name='QA', term='SHORT') == 45.2
    assert htb_spec(size='M24', prop_name='TA', term='LONG') == 140.
    assert htb_spec(size='M24', prop_name='TA', term='SHORT') != 140.
    assert htb_spec(size='M24', prop_name='TA', term='SHORT') == 210.
    with pytest.raises(ParameterError):
        htb_spec(size='M17', prop_name='TA', term='SHORT')
    with pytest.raises(ParameterError):
        htb_spec(size='M16', prop_name='TA', term='SHORT-TIME')
    with pytest.raises(ParameterError):
        htb_spec(size='M16', prop_name='Tu')

    assert htb_spec(size='M16', prop_name='DIA') == 16
    assert htb_spec(size='m16', prop_name='dia') == 16
    assert htb_spec(size='M27', prop_name='DIA') == 27
    assert htb_spec(size='M16', prop_name='HOLE_DIA') == 18
    assert htb_spec(size='M27', prop_name='HOLE_DIA') == 30

    assert htb_spec(size='M16', prop_name='QA', term='LONG', strength='F8T') == 21.4
    assert htb_spec(size='M27', prop_name='QA', term='LONG', strength='F8T') == 61.0


def test_bolt_spec_short_long():
    for strg in HTB_STRENGTHS:
        for size in HTB_SIZES:
            qal = htb_spec(size=size, prop_name='QA', term='LONG', strength=strg)
            qas = htb_spec(size=size, prop_name='QA', term='SHORT', strength=strg)
            assert qas / qal == pytest.approx(1.5, rel=0.01)
        for size in HTB_SIZES:
            tal = htb_spec(size=size, prop_name='TA', term='LONG', strength=strg)
            tas = htb_spec(size=size, prop_name='TA', term='SHORT', strength=strg)
            assert tas / tal == pytest.approx(1.5, rel=0.01)


@pytest.mark.skip('不要か検討中')
def test_get_function_docstring():
    # print(htb_spec(doc=True))
    print(htb_spec.__doc__)


def test_get_all_property_names():
    # print(htb_spec(property_names=True))
    assert htb_spec(property_names=True) == ['QA', 'TA', 'DIA', 'HOLE_DIA']

