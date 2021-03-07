# -*- coding: utf-8 -*-
import pytest

from bolt import htb_spec_old, bolt_spec, xs_bolt_spec, htb_spec, xs_bolt_all_property_names
from bolt import xs_htb_all_property_names
from bolt import ParameterError
from bolt import HTB_SIZES, HTB_STRENGTHS


@pytest.mark.skip('旧関数_実装変更のため')
def xxx_test_bolt_spec_old():
    assert htb_spec_old(size='M16', prop_name='QA', term='LONG') == 30.2
    assert htb_spec_old(size='m16', prop_name='Qa', term='Long') == 30.2
    assert htb_spec_old(size='M16', prop_name='QA', term='SHORT') == 45.2
    assert htb_spec_old(size='M24', prop_name='TA', term='LONG') == 140.
    assert htb_spec_old(size='M24', prop_name='TA', term='SHORT') != 140.
    assert htb_spec_old(size='M24', prop_name='TA', term='SHORT') == 210.
    with pytest.raises(ParameterError):
        htb_spec_old(size='M17', prop_name='TA', term='SHORT')
    with pytest.raises(ParameterError):
        htb_spec_old(size='M16', prop_name='TA', term='SHORT-TIME')
    with pytest.raises(ParameterError):
        htb_spec_old(size='M16', prop_name='Tu')

    assert htb_spec_old(size='M16', prop_name='DIA') == 16
    assert htb_spec_old(size='m16', prop_name='dia') == 16
    assert htb_spec_old(size='M27', prop_name='DIA') == 27
    assert htb_spec_old(size='M16', prop_name='HOLE_DIA') == 18
    assert htb_spec_old(size='M27', prop_name='HOLE_DIA') == 30

    assert htb_spec_old(size='M16', prop_name='QA', term='LONG', strength='F8T') == 21.4
    assert htb_spec_old(size='M27', prop_name='QA', term='LONG', strength='F8T') == 61.0


def test_bolt_spec_short_long():
    for strength in HTB_STRENGTHS:
        for size in HTB_SIZES:
            qal = htb_spec_old(size=size, prop_name='QA', term='LONG', strength=strength)
            qas = htb_spec_old(size=size, prop_name='QA', term='SHORT', strength=strength)
            assert qas / qal == pytest.approx(1.5, rel=0.01)
        for size in HTB_SIZES:
            tal = htb_spec_old(size=size, prop_name='TA', term='LONG', strength=strength)
            tas = htb_spec_old(size=size, prop_name='TA', term='SHORT', strength=strength)
            assert tas / tal == pytest.approx(1.5, rel=0.01)


def test_get_all_property_names():
    assert htb_spec_old(property_names=True) == ['QA', 'TA', 'Dia', 'Hole_dia']
    assert xs_bolt_all_property_names() == 'Dia(mm), Hole_dia(mm), Qal(kN), Qas(kN), Tal(kN), Tas(kN)'
    assert xs_htb_all_property_names() == 'Dia(mm), Hole_dia(mm), Qal(kN), Qas(kN), Tal(kN), Tas(kN), Qu(kN), Tu(kN)'


def test_bolt_spec():
    assert bolt_spec('M16', 'Qal', '6T') == 25.4

    assert bolt_spec('M16', 'QAL', '6T') == 25.4
    assert bolt_spec('M16', 'Qas', '6T') == 38.1
    assert bolt_spec('M24', 'Qas', '6T') == 85.6
    assert bolt_spec('M27', 'Tas', '6T') == 193.0
    assert bolt_spec('M16', 'Qal', '4T') == 14.5
    assert bolt_spec('M16', 'Qal') == 14.5  # default strength='4T'
    assert bolt_spec('M16', 'Tal', '4T') == 25.1
    assert bolt_spec('M24', 'Qas', '4T') == 48.9
    assert bolt_spec('M12', 'Qas', '4T') == 11.7
    assert bolt_spec(size='M12', prop_name='Qas', strength='4T') == 11.7

    assert bolt_spec('M16', 'DIA') == 16
    assert bolt_spec('M16', 'HOLE_DIA') == 17

    assert bolt_spec('M17', 'Qas') == 'NO_DATA'

    assert htb_spec('M16', 'Qas', 'F10T') == 45.2
    assert htb_spec('m16', 'QAS', 'F10T') == 45.2
    assert htb_spec(size='M16', prop_name='Qal') == 30.2

    assert htb_spec(size='M24', prop_name='TAL') == 140.
    assert htb_spec(size='M24', prop_name='TAS') != 140.
    assert htb_spec('M24', 'TAS') == 210.

    assert htb_spec('M17', 'TAS') == 'NO_DATA'
    assert htb_spec('M20', 'TUS') == 'NO_DATA'
    assert htb_spec('M16', 'dia') == 16
    assert htb_spec('m16', 'dia') == 16
    assert htb_spec('M27', 'DIA') == 27
    assert htb_spec('M16', 'HOLE_DIA') == 18
    assert htb_spec('M27', 'HOLE_DIA') == 30

    assert htb_spec('M16', 'QAL', 'F8T') == 21.4
    assert htb_spec('M27', 'QAL', 'F8T') == 61.0

    assert htb_spec('M16', 'Qu') == 121
    assert htb_spec('M16', 'Tu') == 157
    assert htb_spec('M27', 'Tu') == 459
    assert htb_spec('M27', 'Tu', 'F8T') == 367
    assert htb_spec('M20', 'QU', 'F8T') == 151
    assert htb_spec('M20', 'qu', 'f8t') == 151


# @pytest.mark.skip('')
def test_xs_bolt():
    # xl_set udf 検討
    assert xs_bolt_spec('F10T', 'M16', 'Qas') == 45.2
    assert xs_bolt_spec('F10T', 'M16',
                        'ALL') == 'Dia(mm), Hole_dia(mm), Qal(kN), Qas(kN), Tal(kN), Tas(kN), Qu(kN), Tu(kN)'

    assert xs_bolt_spec('4T', 'M16', 'Tal') == 25.1
    assert xs_bolt_spec('4T', 'M24', 'Qas') == 48.9
    assert xs_bolt_spec('4T', 'M12', 'Qas') == 11.7
