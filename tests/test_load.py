from load import *
import pytest


def test_UnitLoad():
    ld1 = UnitLoad()
    assert ld1.value == 0.
    assert ld1.description == ''

    ld2 = UnitLoad(type=Type.DL, value=600., description='屋根')
    assert ld2.type == Type.DL
    assert ld2.value == 600.
    assert ld2.description == '屋根'


def test_vars(capsys):
    ld1 = UnitLoad()
    print(vars(ld1))
    output = capsys.readouterr().out.rstrip()
    assert output == "{'type': <Type.DL: 'DL'>, 'load_case': <LoadCase.G: 'G'>, 'value': 0.0, 'description': ''}"


def test_UnitLoad_get_method():
    ld = UnitLoad(type=Type.DL, value=600., description='屋根DL')
    assert ld.get_as_point_load(1, 1) == 600.  # 1[m] * 1[m] * 600[N/m2] =
    assert ld.get_as_point_load(2, 3) == 3600.  # 2[m] * 3[m] * 600[N/m2] =
    assert ld.get_as_distributed_load(2) == 1200.  # 2[m] * 600[N/m2] =
    assert ld.get_as_distributed_load(3) == 1800.


def test_load_combo_init():
    lcombo1 = LoadCombination(label='G', load_cases=[LoadCase.G], factors=[1], term=LoadTerm.LONG)
    assert lcombo1.get_factor(LoadCase.G) == 1
    assert lcombo1.term == LoadTerm.LONG
    with pytest.raises(ValueError):
        assert lcombo1.get_factor(LoadCase.S) == 1

    lcombo2 = LoadCombination(label='G+S', load_cases=[LoadCase.G, LoadCase.S], factors=[1, 1], term=LoadTerm.SHORT)
    assert lcombo2.get_factor(LoadCase.G) == 1.0
    assert lcombo2.get_factor(LoadCase.S) == 1.0
    assert lcombo2.term == LoadTerm.SHORT

    lcombo3 = LoadCombination(label='G+0.7S', load_cases=[LoadCase.G, LoadCase.S], factors=[1, 0.7],
                              term=LoadTerm.SHORT)
    assert lcombo3.get_factor(LoadCase.G) == 1.0
    assert lcombo3.get_factor(LoadCase.S) == 0.7


def test_load_registry_sample_use_case(capsys):
    ld_reg = LoadRegistry()
    ld_yane_dl_id = ld_reg.add_load(ld_type=Type.DL, value=600.0, load_case=LoadCase.G, description='屋根DL')
    ld_sl_id = ld_reg.add_load(ld_type=Type.SL, value=780.0, load_case=LoadCase.S, description='SL')

    print(ld_reg.loads)
    output = capsys.readouterr().out.rstrip()
    assert output == (
        "{1: UnitLoad(type=<Type.DL: 'DL'>, load_case=<LoadCase.G: 'G'>, value=600.0, description='屋根DL'),"
        " 2: UnitLoad(type=<Type.SL: 'SL'>, load_case=<LoadCase.S: 'S'>, value=780.0, description='SL')}")

    print(ld_reg.show_loads())
    output = capsys.readouterr().out.rstrip()
    assert output == """---------------------------- registered unit loads -----------------------------
   id   type    value(N/m2) LoadCase   description
    1    DL          600.00    G       屋根DL
    2    SL          780.00    S       SL
--------------------------------------------------------------------------------"""

    ld_reg.remove_load(ld_yane_dl_id)
    print(ld_reg.show_loads())
    output = capsys.readouterr().out.rstrip()
    assert output == """---------------------------- registered unit loads -----------------------------
   id   type    value(N/m2) LoadCase   description
    2    SL          780.00    S       SL
--------------------------------------------------------------------------------"""

    ld_yane_dl_id = ld_reg.add_load(ld_type=Type.DL, value=600.0, load_case=LoadCase.G, description='屋根DL')
    print(ld_reg.show_loads())
    output = capsys.readouterr().out.rstrip()
    assert output == """---------------------------- registered unit loads -----------------------------
   id   type    value(N/m2) LoadCase   description
    2    SL          780.00    S       SL
    3    DL          600.00    G       屋根DL
--------------------------------------------------------------------------------"""

    ld_reg.modify_load(ld_yane_dl_id, value=550.0, description='屋根DL2')
    print(ld_reg.show_loads())
    output = capsys.readouterr().out.rstrip()
    assert output == """---------------------------- registered unit loads -----------------------------
   id   type    value(N/m2) LoadCase   description
    2    SL          780.00    S       SL
    3    DL          550.00    G       屋根DL2
--------------------------------------------------------------------------------"""

    ld_reg.add_load_combo('G', [LoadCase.G], [1], LoadTerm.LONG)
    ld_reg.add_load_combo('G+S', [LoadCase.G, LoadCase.S], [1, 1], LoadTerm.SHORT)
    ld_reg.add_load_combo('G+0.7S', [LoadCase.G, LoadCase.S], [1, 0.7], LoadTerm.LONG)
    ld_reg.add_load_combo('G+P+0.35S+K', [LoadCase.G, LoadCase.P, LoadCase.S, LoadCase.K], [1, 1, 0.35, 1],
                          LoadTerm.SHORT)
    print(ld_reg.show_load_combo())
    output = capsys.readouterr().out.rstrip()
    assert output == """------------------------- registered load combinations -------------------------
          label               load_cases             factors                term
              G                    ['G']                 [1]                LONG
            G+S               ['G', 'S']              [1, 1]               SHORT
         G+0.7S               ['G', 'S']            [1, 0.7]                LONG
    G+P+0.35S+K     ['G', 'P', 'S', 'K']     [1, 1, 0.35, 1]               SHORT
--------------------------------------------------------------------------------"""

    # lreg.remove_load_combo('G+S')
    # print(lreg.show_load_combo())

    assert ld_reg.unit_loads[ld_yane_dl_id].get_as_point_load(1, 1) == 550 * 1 * 1
    assert ld_reg.get_as_point_load('G', 1, 1) == (550 * 1) * 1 * 1
    assert ld_reg.get_as_distributed_load('G', 1) == (550 * 1) * 1
    assert ld_reg.get_as_point_load('G', 1, 2) == (550 * 1) * 1 * 2
    assert ld_reg.get_as_distributed_load('G', 1.5) == (550 * 1) * 1.5
    assert ld_reg.get_as_point_load('G+S', 1, 2) == (550 * 1 + 780 * 1) * 1 * 2
    assert ld_reg.get_as_distributed_load('G+S', 1.5) == (550 * 1 + 780 * 1) * 1.5
    assert ld_reg.get_as_point_load('G+0.7S', 1, 2) == (550 * 1 + 780 * 0.7) * 1 * 2
    assert ld_reg.get_as_distributed_load('G+0.7S', 1.5) == (550 * 1 + 780 * 0.7) * 1.5
    with pytest.raises(KeyError):  # 登録されていないラベルの時
        assert ld_reg.get_as_point_load('G+K', 1, 1) == 1.
        assert ld_reg.get_as_distributed_load('G+W', 1.5) == 1.

    assert ld_reg.get_load_combo_names(LoadTerm.LONG) == ['G', 'G+0.7S']
    assert ld_reg.get_load_combo_names(LoadTerm.SHORT) == ['G+S', 'G+P+0.35S+K']
