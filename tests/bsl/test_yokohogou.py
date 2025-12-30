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
    ('H25', 6800.0, Material.S400N, 10, 1120.0),  # 長さのまるめ 10mm指定
    ('H25', 6800.0, Material.S400N, 50, 1100.0),  # 長さのまるめ 50mm指定
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
    ('H24', 6800, 2400.0, Material.S400N, 62.12, 40.0, 61.55515609201724 * 1e6),
    ('H24', 6800, 1000.0, Material.S400N, 60.0, 20.0, 64.50193848758025 * 1e6),
    ('H25', 6800, 2300.0, Material.S400N, 68.29, 0, 69.5324474041749 * 1e6),
    ('H50', 7000, 6000.0, Material.S400N, 200.0, 50.0, 365392549.5744368),
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


def test_set_member_end_restraints():
    yh = Yokohogou(sec='H24', L=6800.0)
    yh.set_Me()
    # print(yh.get_input_data())
    yh.set_member_end_restraints()
    # print(yh.restraint_spans)
    # assert yh.restraint_spans == [1000.0, 4800.0, 1000.0]
    assert yh.restraint_spans == [1000.0, 1600.0, 1600.0, 1600.0, 1000.0]

    yh = Yokohogou(sec='H25', L=6800.0)
    yh.set_Me()
    # print(yh.get_input_data())
    yh.set_member_end_restraints(step=100)
    # print(yh.restraint_spans)
    # assert yh.restraint_spans == [1000.0, 4800.0, 1000.0]
    assert yh.restraint_spans == [1100.0, 2300.0, 2300.0, 1100.0]

    yh = Yokohogou(sec='H24', L=12800.0)
    yh.set_Me()
    # print(yh.get_input_data())
    yh.set_member_end_restraints()
    # print(yh.restraint_spans)
    # todo: 確認必要 2024-1109
    # assert yh.restraint_spans == [1000.0, 1000.0, 2200.0, 2200.0, 2200.0, 2200.0, 1000.0, 1000.0]
    assert yh.restraint_spans == [1000.0, 1000.0, 1466.6666666666667, 1466.6666666666667, 1466.6666666666667,
                                  1466.6666666666667, 1466.6666666666667, 1466.6666666666667, 1000.0, 1000.0]
    # print(yh.get_output_data())


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


@pytest.mark.parametrize("x, step, expected", [
    (1, 1, 1),
    (1.1, 1, 1),
    (1, 5, 0),
    (5, 5, 5),
    (5.1, 5, 5),
    (1000, 100, 1000),
    (1000.1, 100, 1000),
    (1001, 100, 1000),
    (1099, 100, 1000),
    (1175, 50, 1150),

])
def test_x_flooring(x, step, expected):
    yh = Yokohogou()
    assert yh.x_flooring(x, step) == expected


@pytest.mark.skip('出力サンプル sample')
def test_output_sample1():
    # yh = Yokohogou(sec='H25', L=8000.0)
    yh = Yokohogou(sec='H24', L=6800.0)
    print()
    print(yh.get_input_data())
    print(yh.get_output_data(step=100))

    yh = Yokohogou(sec='H25', L=6800.0)
    print()
    print(yh.get_input_data())
    print(yh.get_output_data(step=100))

    yh = Yokohogou(sec='H294', L=10320.0)
    print()
    print(yh.get_input_data())
    print(yh.get_output_data(step=50))

    yh = Yokohogou(sec='H24', L=12800.0)
    print()
    print(yh.get_input_data())
    print(yh.get_output_data())


# @pytest.mark.skip('出力サンプル sample')
def test_output_sample2():
    # 算定計算
    # yh = Yokohogou(sec='H24', L=6800.0)
    # yh = Yokohogou(sec='H24', L=11000.0)
    yh = Yokohogou(sec='H24', L=7000.0)
    print()
    print(yh.get_input_data())
    print(yh.get_output_data(step=100))

    # 検定計算
    # yh = Yokohogou(sec='H24', L=6800.0)
    # yh = Yokohogou(sec='H24', L=11000.0)
    yh = Yokohogou(sec='H24', L=7000.0)
    # yh.restraint_spans = [1000, 2400, 2400,1000]
    # span = [1000, 1000, 3500, 3500, 1000, 1000]  # H24 L=11000
    # span = [1000, 2400, 2400, 1000]  # H24
    # span = [1000, 1000, 2800, 1000, 1000]  # H24
    # span = [1000, 5000/3, 5000/3, 5000/3, 1000]  # H24
    span = [1000, 1250, 2500, 1250, 1000]  # H24

    # span = [1000, 1000, 3000, 1000, 1000]  # H24 L=7000
    # span = [1100, 2300, 2300, 1100]  # H25
    print()
    print(yh.get_input_data())
    print(yh.get_output_data(step=100, restraint_span=span))


def test_output_sample3():
    # 算定計算
    # yh = Yokohogou(sec='H24', L=6800.0)
    # yh = Yokohogou(sec='H24', L=11000.0)
    yh = Yokohogou(sec='H24', L=7400.0)
    print()
    print(yh.get_input_data())
    yh.set_member_end_restraints(step=100, eq_flg=False)
    print(yh.get_output_data(eq_flg=False))
    print(yh.get_output_data(eq_flg=True))

    # print(yh.get_output_data(step=100))


@pytest.mark.parametrize("sec, L, lb_spans, expected", [
    ('H25', 6800.0, [1100, 2300, 2300, 1100], 'OK'),
    ('H24', 6800.0, [1000, 2400, 2400, 1000], 'NG'),
    ('H24', 12800.0, [1000, 1000, 1760, 1760, 1760, 1760, 1760, 1000, 1000], 'NG'),  # todo:check-2024-1123
    ('H24', 12800.0, [1000, 1000, 2200, 2200, 2200, 2200, 1000, 1000], 'NG'),  # todo:check-2024-1123

])
def test_check_hogou_rule_tanbu(sec, L, lb_spans, expected):
    # 補剛間隔を与え、基準をみたすかチェックする
    yh = Yokohogou(sec=sec, L=L)
    yh.restraint_spans = lb_spans
    assert yh.check_hogou_rule_tanbu() == expected
    # 出力する時は以下のコメントを解除
    # print(yh.get_input_data())
    # yh.check_hogou_rule_tanbu(print_on=True)


def test_get_My_position():
    yh = Yokohogou(sec='H24', L=8000.0)
    # Q=21,996[N], x= (87,984,000-65330000) / 21996
    assert yh.get_My_position() == 1029.91452991453
    yh = Yokohogou(sec='H24', L=6800.0)
    assert yh.get_My_position() == 875.4273504273505


@pytest.mark.parametrize(
    "      L,    M1,   M2, expected", [
        (8000.0, 100, 100, 4000.0),
        (8000.0, 0, 100, 0.0),
        (8000.0, 100, 0, 8000.0),
        (8000.0, 10, 70, 1000.0),
        (8000.0, 70, 10, 7000.0),
        (8000.0, 100, 10, 8000.0 * 10 / 11),
        (8000.0, 10, 100, 8000.0 * 1 / 11),
    ])
def test_get_M0_position(L, M1, M2, expected):
    yh = Yokohogou(sec='H24', L=L)
    yh.M_Left = M1
    yh.M_Right = M2
    assert yh.get_M0_position() == expected


@pytest.mark.skip("list sample　挙動確認")
def test_list_swap():
    a_o = [1, 2, 2, 1]
    a_b = a_o[:]
    center_span = 10
    print(len(a_o))
    center_index = int(len(a_o) / 2)
    a_b.insert(center_index, center_span)
    # print(a_o)
    print(a_b)


def test_set_center_span_hogou():
    yh = Yokohogou(sec='H24', L=7000.0)


def test_sample_iterator():
    # ジェネレーターでの試行
    def get_hogou_pitch(L, n, rlb, pitch=1):
        # ジェネレーター
        if n == 2 or n == 3:
            L1 = rlb
            while L1 < L / 2:
                if n == 2:
                    yield [L1, L - 2 * L1, L1]
                elif n == 3:
                    yield [L1, (L - 2 * L1) / 2, (L - 2 * L1) / 2, L1]
                L1 += pitch

        # elif n == 3:
        #     L1 = rlb
        #     while L1 < L / 2:
        #         yield [L1, (L - 2 * L1) / 2, (L - 2 * L1) / 2, L1]
        #         L1 += pitch
        elif n == 4 or n == 5:
            L1 = rlb
            L2 = rlb
            while L1 + L2 < L / 2:
                while L1 + L2 < L / 2:
                    if n == 4:
                        # L_i = get_hogou_pitch(L - 2 * L1, n - 2, rlb, pitch=pitch)
                        # yield [L1] + next(L_i) + [L1]
                        yield [L1, L2, L - 2 * (L1 + L2), L2, L1]
                    elif n == 5:
                        yield [L1, L2, (L - 2 * (L1 + L2)) / 2, (L - 2 * (L1 + L2)) / 2, L2, L1]

                    L2 += pitch
                L2 = rlb
                L1 += pitch

    for x in get_hogou_pitch(1000, 5, 100, pitch=50):
        # print(x)
        pass
    # print(list(get_hogou_pitch(1000, 2, 100, pitch=50)))
    # print(list(get_hogou_pitch(1000, 3, 100, pitch=50)))
    # print(list(get_hogou_pitch(1000, 5, 100, pitch=50)))

    # -------------------------------- Test
    hogou_pitch = get_hogou_pitch(1000, 2, 100, 5)
    assert next(hogou_pitch) == [100, 800, 100]
    assert next(hogou_pitch) == [105, 790, 105]

    assert list(get_hogou_pitch(1000, 2, 100, pitch=100)) == [[100, 800, 100], [200, 600, 200], [300, 400, 300],
                                                              [400, 200, 400]]
    assert list(get_hogou_pitch(1000, 2, 100, pitch=50)) == [[100, 800, 100], [150, 700, 150], [200, 600, 200],
                                                             [250, 500, 250], [300, 400, 300], [350, 300, 350],
                                                             [400, 200, 400], [450, 100, 450]]
    assert list(get_hogou_pitch(1000, 3, 100, pitch=100)) == [[100, 400.0, 400.0, 100], [200, 300.0, 300.0, 200],
                                                              [300, 200.0, 200.0, 300], [400, 100.0, 100.0, 400]]

    assert list(get_hogou_pitch(1000, 3, 100, pitch=50)) == [[100, 400.0, 400.0, 100], [150, 350.0, 350.0, 150],
                                                             [200, 300.0, 300.0, 200], [250, 250.0, 250.0, 250],
                                                             [300, 200.0, 200.0, 300], [350, 150.0, 150.0, 350],
                                                             [400, 100.0, 100.0, 400], [450, 50.0, 50.0, 450]]

    assert list(get_hogou_pitch(1000, 4, 100, pitch=50)) == [[100, 100, 600, 100, 100], [100, 150, 500, 150, 100],
                                                             [100, 200, 400, 200, 100], [100, 250, 300, 250, 100],
                                                             [100, 300, 200, 300, 100], [100, 350, 100, 350, 100],
                                                             [150, 100, 500, 100, 150], [150, 150, 400, 150, 150],
                                                             [150, 200, 300, 200, 150], [150, 250, 200, 250, 150],
                                                             [150, 300, 100, 300, 150], [200, 100, 400, 100, 200],
                                                             [200, 150, 300, 150, 200], [200, 200, 200, 200, 200],
                                                             [200, 250, 100, 250, 200], [250, 100, 300, 100, 250],
                                                             [250, 150, 200, 150, 250], [250, 200, 100, 200, 250],
                                                             [300, 100, 200, 100, 300], [300, 150, 100, 150, 300],
                                                             [350, 100, 100, 100, 350]]

    assert list(get_hogou_pitch(1000, 5, 100, pitch=50)) == [[100, 100, 300.0, 300.0, 100, 100],
                                                             [100, 150, 250.0, 250.0, 150, 100],
                                                             [100, 200, 200.0, 200.0, 200, 100],
                                                             [100, 250, 150.0, 150.0, 250, 100],
                                                             [100, 300, 100.0, 100.0, 300, 100],
                                                             [100, 350, 50.0, 50.0, 350, 100],
                                                             [150, 100, 250.0, 250.0, 100, 150],
                                                             [150, 150, 200.0, 200.0, 150, 150],
                                                             [150, 200, 150.0, 150.0, 200, 150],
                                                             [150, 250, 100.0, 100.0, 250, 150],
                                                             [150, 300, 50.0, 50.0, 300, 150],
                                                             [200, 100, 200.0, 200.0, 100, 200],
                                                             [200, 150, 150.0, 150.0, 150, 200],
                                                             [200, 200, 100.0, 100.0, 200, 200],
                                                             [200, 250, 50.0, 50.0, 250, 200],
                                                             [250, 100, 150.0, 150.0, 100, 250],
                                                             [250, 150, 100.0, 100.0, 150, 250],
                                                             [250, 200, 50.0, 50.0, 200, 250],
                                                             [300, 100, 100.0, 100.0, 100, 300],
                                                             [300, 150, 50.0, 50.0, 150, 300],
                                                             [350, 100, 50.0, 50.0, 100, 350]]
