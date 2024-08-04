# from load import Type, UnitLoad, LoadCombination
from load import *
import pytest


def test_load():
    ld1 = UnitLoad()
    assert ld1.value == 0.
    assert ld1.description == ''
    ld2 = UnitLoad(type=Type.DL, value=600., description='屋根')
    print(ld2)


def test_vars():
    ld1 = UnitLoad()
    print(vars(ld1))


def test_load_get_method():
    ld = UnitLoad(type=Type.DL, value=600., description='屋根DL')
    assert ld.get_as_point_load(1, 1) == 600.
    assert ld.get_as_point_load(2, 3) == 3600.
    assert ld.get_as_distributed_load(2) == 1200.
    assert ld.get_as_distributed_load(3) == 1800.


@pytest.mark.skip('実装変更のため')
def test_load_combo_old():
    ld_combo = LoadCombination()
    dl = UnitLoad(type=Type.DL, value=600., description='屋根固定荷重')
    sl = UnitLoad(type=Type.SL, value=800.0, description='積雪荷重')
    ld_combo.add('G+S', {dl: 1.0, sl: 1})  # クラスのインスタンスをキーにするには、ハッシュ可能にしなければならない？
    print(ld_combo)


@pytest.mark.skip('実装変更のため')
def test_load_combo_2():
    lcombo = LoadCombination()
    # assert lcombo.__class__.load_id == 0
    assert lcombo.current_load_id == 0
    id_dl = lcombo.add_load(type=Type.DL, value=600., description='屋根DL')
    id_dl_w = lcombo.add_load(type=Type.DL, value=650., description='壁DL')
    id_sl = lcombo.add_load(type=Type.SL, value=800., description='SL')
    print()
    print(lcombo)
    # lcombo.add_combo('DL+SL', (id_dl, 1), (id_sl, 1))

    # assert lcombo.current_load_id == 1

    # lcombo.add_load()


def test_load_combo():
    lcombo = LoadCombination('G', [LoadCase.G], [1])
    assert lcombo.get_factor(LoadCase.G) == 1

    lcombo2 = LoadCombination('G+S', [LoadCase.G, LoadCase.S], [1, 1])
    assert lcombo2.get_factor(LoadCase.G) == 1.0
    assert lcombo2.get_factor(LoadCase.S) == 1.0

    lcombo3 = LoadCombination('G+0.7S', [LoadCase.G, LoadCase.S], [1, 0.7])
    assert lcombo3.get_factor(LoadCase.G) == 1.0
    assert lcombo3.get_factor(LoadCase.S) == 0.7


def test_load_registry_sample_use_case():
    lreg = LoadRegistry()
    ld_yane_dl_id = lreg.add_load(ld_type=Type.DL, value=600.0, load_case=LoadCase.G, description='屋根DL')
    ld_sl_id = lreg.add_load(ld_type=Type.SL, value=780.0, load_case=LoadCase.S, description='SL')
    print(lreg.loads)
    print(lreg.show_loads())
    lreg.remove_load(ld_yane_dl_id)
    print(lreg.show_loads())
    ld_yane_dl_id = lreg.add_load(ld_type=Type.DL, value=600.0, load_case=LoadCase.G, description='屋根DL')
    print(lreg.show_loads())
    lreg.modify_load(ld_yane_dl_id, value=550.0, description='屋根DL2')
    print(lreg.show_loads())
    lreg.add_load_combo('G', [LoadCase.G], [1])
    lreg.add_load_combo('G+S', [LoadCase.G, LoadCase.S], [1, 1])
    lreg.add_load_combo('G+0.7S', [LoadCase.G, LoadCase.S], [1, 0.7])
    lreg.add_load_combo('G+P+0.35S+K', [LoadCase.G, LoadCase.P, LoadCase.S, LoadCase.K], [1, 1, 0.35, 1])
    print(lreg.show_load_combo())
    # lreg.remove_load_combo('G+S')
    print(lreg.show_load_combo())
    assert lreg.unit_loads[ld_yane_dl_id].get_as_point_load(1, 1) == 550 * 1 * 1
    assert lreg.get_as_point_load('G', 1, 1) == (550 * 1) * 1 * 1
    assert lreg.get_as_distributed_load('G', 1) == (550 * 1) * 1
    assert lreg.get_as_point_load('G', 1, 2) == (550 * 1) * 1 * 2
    assert lreg.get_as_distributed_load('G', 1.5) == (550 * 1) * 1.5
    assert lreg.get_as_point_load('G+S', 1, 2) == (550 * 1 + 780 * 1) * 1 * 2
    assert lreg.get_as_distributed_load('G+S', 1.5) == (550 * 1 + 780 * 1) * 1.5
    assert lreg.get_as_point_load('G+0.7S', 1, 2) == (550 * 1 + 780 * 0.7) * 1 * 2
    assert lreg.get_as_distributed_load('G+0.7S', 1.5) == (550 * 1 + 780 * 0.7) * 1.5
