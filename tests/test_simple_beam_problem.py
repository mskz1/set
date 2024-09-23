# -*- coding: utf-8 -*-
import pytest
import pprint
from src.beam_model import SimpleBeamSteel
from load import *
from beam_formula import SimplySupportedBeamWithUniformDistributedLoad, SimplySupportedBeamWithMultiplePointLoad


@pytest.fixture()
def load_combo_yane():
    ld_reg = LoadRegistry()
    ld_reg.add_load(ld_type=Type.DL, value=600.0, load_case=LoadCase.G, description='屋根DL')
    ld_reg.add_load(ld_type=Type.SL, value=780.0, load_case=LoadCase.S, description='SL')
    ld_reg.add_load(ld_type=Type.WL, value=1000.0, load_case=LoadCase.W, description='WL')
    ld_reg.add_load_combo('G', [LoadCase.G], [1], LoadTerm.LONG)
    ld_reg.add_load_combo('G+S', [LoadCase.G, LoadCase.S], [1, 1], LoadTerm.SHORT)
    ld_reg.add_load_combo('G-W', [LoadCase.G, LoadCase.W], [1, -1], LoadTerm.SHORT)

    return ld_reg


@pytest.fixture()
def simple_beam_udl(load_combo_yane):
    ld = load_combo_yane
    sb = SimpleBeamSteel(span=5000.0)
    sb.set_load_registry(ld)
    sb.section_name = 'H25'
    sb.add_udl(lcombo='G', a=3000.)
    sb.add_udl(lcombo='G+S', a=3000.)
    sb.add_udl(lcombo='G-W', a=3000.)
    return sb


@pytest.fixture()
def simple_beam_ptl(load_combo_yane):
    ld = load_combo_yane
    sb = SimpleBeamSteel(span=5000.0)
    sb.set_load_registry(ld)
    sb.section_name = 'H25'
    # WIP 2024-0921 nと負担幅をパラメーターにするか？
    sb.add_n_pt_l(lcombo='G', p=sb.ld_reg.get_as_point_load('G', 2.5, 3) / 1000.0, n=1)
    sb.add_n_pt_l(lcombo='G+S', p=sb.ld_reg.get_as_point_load('G+S', 2.5, 3) / 1000.0, n=1)
    return sb


def test_simple_beam_1(simple_beam_udl):
    sb = simple_beam_udl
    assert sb.get_max_internal_force(LoadTerm.LONG) == 5.625
    assert sb.get_max_internal_force(LoadTerm.SHORT) == pytest.approx(12.9375)

    assert sb.get_max_deflection(LoadTerm.LONG) == pytest.approx(0.1804439209164819)
    assert sb.get_max_deflection(LoadTerm.SHORT) == pytest.approx(0.41502101810790837)

    assert sb.check_section() == pytest.approx((0.11326, 0.17366), abs=0.00001)

    # pprint.pprint(sb)


def test_simple_beam_2_point_load(simple_beam_ptl):
    sb = simple_beam_ptl
    assert sb.get_max_internal_force(LoadTerm.LONG) == 5.625
    assert sb.get_max_deflection(LoadTerm.LONG) == pytest.approx(0.144, abs=0.001)
    assert sb.get_max_internal_force(LoadTerm.SHORT) == pytest.approx(12.9375)
    assert sb.get_max_deflection(LoadTerm.SHORT) == pytest.approx(0.332, abs=0.001)
    assert sb.check_section() == pytest.approx((0.113, 0.174), abs=0.001)


@pytest.mark.parametrize("L, Lb, term", [
    (4000, 0, LoadTerm.LONG),
])
def test_simple_beam_data(simple_beam_udl, L, Lb, term):
    sb = simple_beam_udl
