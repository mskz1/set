# -*- coding: utf-8 -*-
import pytest

from rebar import rebar_spec


def test_rebar_spec():
    assert rebar_spec('D10', 'A') == 71.33
    assert rebar_spec('D10', 'L') == 30
    assert rebar_spec('D10', 'd') == 9.53
    assert rebar_spec('D10', 'DO') == 11
    assert rebar_spec('D13', 'A') == 126.7
    assert rebar_spec('D16', 'A') == 198.6
    assert rebar_spec('D22', 'A') == 387.1
    assert rebar_spec('D25', 'A') == 506.7

    assert rebar_spec(prop_name='ALL') == ['d(mm)', 'DO(mm)', 'A(mm**2)', 'L(mm)']
    assert rebar_spec() == ['d(mm)', 'DO(mm)', 'A(mm**2)', 'L(mm)']

