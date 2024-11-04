from bsl.yokohogou import *
import pytest


@pytest.mark.parametrize("sec, L, mat, expected", [
    ('H294', 10320.0, Material.S400N, 3),
    # todo : add more case
])
def test_get_num_of_equivalent_restraint(sec, L, mat, expected):
    # 均等配置の場合のテスト
    yh = Yokohogou(sec=sec, L=L, material=mat)
    assert yh.get_number_of_equivalent_placement_lateral_restraint() == expected


@pytest.mark.parametrize("sec, L, mat, step, expected", [
    ('H24', 6800.0, Material.S400N, 0, 1000.0),  # 長さのまるめ　指定なし
    ('H25', 6800.0, Material.S400N, 0, 1125.0),
    ('H25', 6800.0, Material.S400N, 5, 1125.0),  # 長さのまるめ 5mm指定
    ('H25', 6800.0, Material.S400N, 10, 1130.0),  # 長さのまるめ 10mm指定
    ('H25', 6800.0, Material.S400N, 50, 1150.0),  # 長さのまるめ 50mm指定
    # todo : add more case
])
def test_get_lb(sec, L, mat, step, expected):
    yh = Yokohogou(sec=sec, L=L, material=mat)
    assert yh.get_lb(step=step) == expected


@pytest.mark.parametrize("sec, L, mat, expected", [
    ('H24', 6800.0, Material.S400N, 73.32 * 1e6),
    ('H25', 6800.0, Material.S400N, 84.13 * 1e6),
    # todo : add more case
])
def test_Mp(sec, L, mat, expected):
    yh = Yokohogou(sec=sec, L=L, material=mat)
    assert yh.Mp == expected


@pytest.mark.parametrize("sec, L, mat, expected", [
    ('H24', 6800.0, Material.S400N, 65.33 * 1e6),
    ('H25', 6800.0, Material.S400N, 74.495 * 1e6),
    # todo : add more case
])
def test_My(sec, L, mat, expected):
    yh = Yokohogou(sec=sec, L=L, material=mat)
    assert yh.My == expected


@pytest.mark.parametrize("sec, L, Lb, mat, M1, M2, expected", [
    ('H24', 6800, 2400.0, Material.S400N, 62.12, 0, 60.457264464444675 * 1e6),
    ('H25', 6800, 2300.0, Material.S400N, 68.29, 0, 69.5324474041749 * 1e6),
    # todo : add more case
])
def test_Mas(sec, L, Lb, mat, M1, M2, expected):
    yh = Yokohogou(sec=sec, L=L, material=mat)
    assert yh.Mas(Lb, M1, M2) == expected


@pytest.mark.parametrize(
    "sec,      L,       mat,        end_condition, expected_M1, expected_M2", [
        ('H24', 6800.0, Material.S400N, Condition.Mp_Mp, 87.984 * 1e6, 87.984 * 1e6),
        ('H25', 6800.0, Material.S400N, Condition.Mp_Mp, 100.956 * 1e6, 100.956 * 1e6),
        # todo : add more case
    ])
def test_Me(sec, L, mat, end_condition, expected_M1, expected_M2):
    yh = Yokohogou(sec=sec, L=L, material=mat, end_force_condition=end_condition)
    yh.set_Me()
    assert yh.M_Left == expected_M1
    assert yh.M_Right == expected_M2


def test_restraint_spans():
    yh = Yokohogou('H40', L=8000.0)
    yh.restraint_spans = [2500, 3000, 2500]
    assert yh.lb_spans == [2500, 3000, 2500]
    assert yh.lb_positions == [0, 2500, 5500, 8000]


def test_M_at():
    yh = Yokohogou('H40', L=8000.0)
    yh.M_Left = 100.0
    yh.M_Right = 100.0
    assert yh.Q == (100 + 100) / 8000  # 0.025
    assert yh.M_at(x=0) == 100.0
    assert yh.M_at(x=4000.) == 0.0
    assert yh.M_at(x=8000.) == 100.0
    assert yh.M_at(x=1000.) == 75.0  # 100-0.025*1000=75
    assert yh.M_at(x=7000.) == 75.0
    assert yh.M_at(x=2000.) == 50.0
    assert yh.M_at(x=6000.) == 50.0
    assert yh.M_at(x=3000.) == 25.0


def test_check_yokohogou():
    yh = Yokohogou(sec='H24', L=6800.0)
    yh.set_Me()
    # print(yh.get_input_data())
    yh.set_member_end_restraints()
    # print(yh.restraint_spans)
    assert yh.restraint_spans == [1000.0, 4800.0, 1000.0]

    yh = Yokohogou(sec='H24', L=12800.0)
    yh.set_Me()
    # print(yh.get_input_data())
    yh.set_member_end_restraints()
    # print(yh.restraint_spans)
    assert yh.restraint_spans == [1000.0, 1000.0, 8800.0, 1000.0, 1000.0]




@pytest.mark.parametrize("x, step, expected", [
    (1, 1, 1),
    (1.1, 1, 2),
    (1, 5, 5),
    (5, 5, 5),
    (5.1, 5, 10),
    (1000, 100, 1000),
    (1000.1, 100, 1100),
    (1001, 100, 1100),
])
def test_x_ceiling(x, step, expected):
    yh = Yokohogou()
    # assert -(-x // step) * step == expected
    assert yh.x_ceiling(x, step) == expected
