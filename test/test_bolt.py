# -*- coding: utf-8 -*-
import pytest

from bolt import htb_spec
from bolt import ParameterError
from bolt import HTB_SIZES, HTB_STRENGTHS


def test_bolt_spec():
    assert htb_spec(size='M16', prop='QA', term='LONG') == 30.2
    assert htb_spec(size='m16', prop='Qa', term='Long') == 30.2
    assert htb_spec(size='M16', prop='QA', term='SHORT') == 45.2
    assert htb_spec(size='M24', prop='TA', term='LONG') == 140.
    assert htb_spec(size='M24', prop='TA', term='SHORT') != 140.
    assert htb_spec(size='M24', prop='TA', term='SHORT') == 210.
    with pytest.raises(ParameterError):
        htb_spec(size='M17', prop='TA', term='SHORT')
    with pytest.raises(ParameterError):
        htb_spec(size='M16', prop='TA', term='SHORT-TIME')
    with pytest.raises(ParameterError):
        htb_spec(size='M16', prop='Tu')

    assert htb_spec(size='M16', prop='DIA') == 16
    assert htb_spec(size='m16', prop='dia') == 16
    assert htb_spec(size='M27', prop='DIA') == 27
    assert htb_spec(size='M16', prop='HOLE_DIA') == 18
    assert htb_spec(size='M27', prop='HOLE_DIA') == 30

    assert htb_spec(size='M16', prop='QA', term='LONG', strength='F8T') == 21.4
    assert htb_spec(size='M27', prop='QA', term='LONG', strength='F8T') == 61.0



def test_bolt_spec_short_long():
    for strg in HTB_STRENGTHS:
        for size in HTB_SIZES:
            qal = htb_spec(size=size, prop='QA', term='LONG', strength=strg)
            qas = htb_spec(size=size, prop='QA', term='SHORT', strength=strg)
            assert qas / qal == pytest.approx(1.5, rel=0.01)
        for size in HTB_SIZES:
            tal = htb_spec(size=size, prop='TA', term='LONG', strength=strg)
            tas = htb_spec(size=size, prop='TA', term='SHORT', strength=strg)
            assert tas / tal == pytest.approx(1.5, rel=0.01)
