# -*- coding: utf-8 -*-
import pytest

def test_rebar_spec():
    assert rebar_spec('D10','A') == 71
    assert rebar_spec('D10','L') == 30