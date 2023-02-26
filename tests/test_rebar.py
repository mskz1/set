# -*- coding: utf-8 -*-
import pprint

from src.rebar import rebar_spec, rebar_size_list_as_string, rebar_size_list
from src.rebar import Size, Property, make_deformed_bar_data, rebar_spec2


def test_rebar_spec2():
    assert rebar_spec(Size.D10.value, 'A') == 71.33
    # spec = make_deformed_bar_data()
    # pprint.pprint(spec)
    # print(spec[Size.D6][Property.Area])
    # print(spec[Size.D8][Property.Area])
    assert rebar_spec2(Size.D10, Property.Area) == 71.33
    assert rebar_spec2(Size.D10, Property.Perimeter) == 30
    assert rebar_spec2(Size.D10, Property.Diameter) == 9.53
    assert rebar_spec2(Size.D10, Property.MaxOuterDiameter) == 11
    assert rebar_spec2(Size.D13, Property.Area) == 126.7
    assert rebar_spec2(Size.D16, Property.Area) == 198.6
    assert rebar_spec2(Size.D22, Property.Area) == 387.1
    assert rebar_spec2(Size.D25, Property.Area) == 506.7


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
    assert rebar_size_list() == ['D6', 'D8', 'D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D35', 'D38',
                                 'D41', 'D51']
