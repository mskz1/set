# -*- coding: utf-8 -*-
import pytest

from rebar import rebar_spec


def test_rebar_spec():
    assert rebar_spec('D10', 'A') == 71
    assert rebar_spec('D10', 'L') == 30
    assert rebar_spec(prop_name='ALL') == ['D(mm)', 'A(mm**2)', 'L(mm)']
    assert rebar_spec() == ['D(mm)', 'A(mm**2)', 'L(mm)']

