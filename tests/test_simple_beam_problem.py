# -*- coding: utf-8 -*-
import pytest
import pprint
from src.beam_model import SimpleBeamSteel
from load import *
from beam_formula import SimplySupportedBeamWithUniformDistributedLoad, SimplySupportedBeamWithMultiplePointLoad


@pytest.fixture()
def load_combo():
    ld_reg = LoadRegistry()
    ld_reg.add_load(ld_type=Type.DL, value=600.0, load_case=LoadCase.G, description='屋根DL')
    ld_reg.add_load(ld_type=Type.SL, value=780.0, load_case=LoadCase.S, description='SL')
    ld_reg.add_load(ld_type=Type.WL, value=1000.0, load_case=LoadCase.W, description='WL')
    ld_reg.add_load_combo('G', [LoadCase.G], [1], LoadTerm.LONG)
    ld_reg.add_load_combo('G+S', [LoadCase.G, LoadCase.S], [1, 1], LoadTerm.SHORT)
    ld_reg.add_load_combo('G-W', [LoadCase.G, LoadCase.W], [1, -1], LoadTerm.SHORT)

    return ld_reg


@pytest.fixture()
def simple_beam(load_combo):
    ld = load_combo
    sb = SimpleBeamSteel(span=5000.0)
    sb.set_load_registry(ld)
    sb.section_name = 'H25'
    sb.add_udl(lcombo='G', a=3000.)
    sb.add_udl(lcombo='G+S', a=3000.)
    sb.add_udl(lcombo='G-W', a=3000.)
    return sb


def test_simple_beam_1(simple_beam):
    sb = simple_beam
    assert sb.get_max_internal_force(LoadTerm.LONG) == 5.625
    assert sb.get_max_internal_force(LoadTerm.SHORT) == pytest.approx(12.9375)

    assert sb.get_max_deflection(LoadTerm.LONG) == pytest.approx(0.1804439209164819)
    assert sb.get_max_deflection(LoadTerm.SHORT) == pytest.approx(0.41502101810790837)
    # print(sb.ld_reg.get_load_combo_names(LoadTerm.LONG))
    sb.check_section()

    print()
    # pprint.pprint(sb)


