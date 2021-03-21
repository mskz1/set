# -*- coding: utf-8 -*-
import pytest

from rebar import rebar_spec, rebar_size_list_as_string, rebar_size_list


def test_rebar_spec():
    assert rebar_spec('D10', 'A') == 71.33
    assert rebar_spec('D10', 'L') == 30
    assert rebar_spec('D10', 'd') == 9.53
    assert rebar_spec('D10', 'DO') == 11
    assert rebar_spec('D13', 'A') == 126.7
    assert rebar_spec('D16', 'A') == 198.6
    assert rebar_spec('D22', 'A') == 387.1
    assert rebar_spec('D25', 'A') == 506.7

    # assert rebar_spec(prop_name='ALL') == ['d(mm)', 'DO(mm)', 'A(mm**2)', 'L(mm)']
    assert rebar_spec(prop_name='ALL') == "['d(mm)', 'DO(mm)', 'A(mm**2)', 'L(mm)']"
    # assert rebar_spec() == ['d(mm)', 'DO(mm)', 'A(mm**2)', 'L(mm)']
    assert rebar_spec() == "['d(mm)', 'DO(mm)', 'A(mm**2)', 'L(mm)']"


def test_get_size_list_as_string():
    # print(rebar_size_list())
    # assert rebar_size_list_as_string() == ['D6', 'D8', 'D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D35', 'D38', 'D41', 'D51']
    assert rebar_size_list_as_string() == '[ D6, D8, D10, D13, D16, D19, D22, D25, D29, D32, D35, D38, D41, D51 ]'

def test_get_size_list():
    assert rebar_size_list() == ['D6', 'D8', 'D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D35', 'D38', 'D41', 'D51']
