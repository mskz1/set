# -*- coding: utf-8 -*-
import math

import pytest
import pprint

from src.xs_section import *


def test_xs_H_sec_name():
    assert xs_section_name('H20') == 'H-200x100x5.5x8'
    assert xs_section_name('H200*100') == 'H-200x100x5.5x8'
    assert xs_section_name('H15') == 'H-150x75x5x7'
    assert xs_section_name('H150*75') == 'H-150x75x5x7'
    assert xs_section_name('h15') == 'H-150x75x5x7'
    assert xs_section_name('h150*75') == 'H-150x75x5x7'
    # with pytest.raises(KeyError):
    #     xs_section_name('hs100')
    assert xs_section_name('h100') == 'H-100x100x6x8'
    assert xs_section_name('h100*50') == 'Section_Not_Defined'
    # assert xs_section_name('C100_23') == 'C-100x50x20x2.3'
    assert xs_section_name('C100*50*2.3') == 'C-100x50x20x2.3'
    # assert xs_section_name('C100*23') == 'C-100x50x20x2.3'
    assert xs_section_name('KP100*3.2') == '□P-100x100x3.2'
    assert xs_section_name('KP100*100*3.2') == '□P-100x100x3.2'
    assert xs_section_name('H700') == 'H-700x300x13x24'
    assert xs_section_name('H700*300') == 'H-700x300x13x24'
    assert xs_section_name('H900') == 'H-900x300x16x28'
    assert xs_section_name('H900*300') == 'H-900x300x16x28'


# @pytest.mark.skip()
def test_xs_section_property():
    # assert set(xs_section_property('HS20')) == {'H', 'An', 'Ix', 'Iy', 'ix', 'iy', 'Zx', 'Zy'}
    assert xs_section_property('H20') == ['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)',
                                          'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)',
                                          'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']
    assert xs_section_property('H200*100') == ['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)',
                                               'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)',
                                               'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']

    assert xs_section_property('H20',
                               'ALL') == "['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)', 'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)', 'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']"
    assert xs_section_property('H200*100',
                               'ALL') == "['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)', 'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)', 'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']"

    assert xs_section_property('H20', 'An') == 26.67  # unit:cm2
    assert xs_section_property('H200*100', 'An') == 26.67  # unit:cm2
    assert xs_section_property('H-200x100x5.5x8', 'An') == 26.67  # unit:cm2
    # assert xs_section_property('H-199x199x5x5', 'An') == 'Section_Not_Defined'
    assert xs_section_property('H-199x199x5x5', 'An') == 'NO_DATA'

    db = make_all_section_db()
    # assert xs_section_property('HS20', 'An', db) == 26.67  # unit:cm2
    assert xs_section_property('H200*100', 'An', db) == 26.67  # unit:cm2
    # assert xs_section_property('hs20', 'An', db) == 26.67  # unit:cm2
    assert xs_section_property('h200*100', 'An', db) == 26.67  # unit:cm2
    # assert xs_section_property('hm900', 'An', db) == 305.8
    assert xs_section_property('h900*300', 'An', db) == 305.8
    # assert xs_section_property('hm900', 'Ix', db) == 404000
    assert xs_section_property('h900*300', 'Ix', db) == 404000
    # assert xs_section_property('hm900', 'Zx', db) == 8990
    assert xs_section_property('h900*300', 'Zx', db) == 8990
    assert xs_section_property('L65*65*6', 'An', db) == 7.527
    assert xs_section_property('L65*65*6', 'Cx', db) == 1.81
    assert xs_section_property('L65*65*6', 'tan_alpha', db) == 1
    assert xs_section_property('L65*65*6', 'Iu', db) == 46.6
    assert xs_section_property('L100*10', 'An', db) == 19
    assert xs_section_property('L130*9', 'Zx', db) == 38.7
    assert xs_section_property('L100*75*7', 'An', db) == 11.9
    assert xs_section_property('L100*75*7', 'Cx', db) == 3.06
    assert xs_section_property('L100*75*7', 'Cy', db) == 1.83
    assert xs_section_property('L100*75*7', 'Iu', db) == 144
    assert xs_section_property('L100*75*7', 'Iv', db) == 30.8
    assert xs_section_property('L100*75*7', 'tan_alpha', db) == 0.548


def test_csv_parse():
    hs = make_section_db(HS_SEC_DATA)
    assert hs['H-200x100x5.5x8'][0]['An'] == 26.67
    assert hs['H-600x200x11x17'][1] == ['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)',
                                        'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)',
                                        'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']
    # pprint.pprint(hs)
    ps = make_section_db(P_SEC_DATA)
    # pprint.pprint(ps)
    assert ps['P-76.3x3.2'][0]['An'] == 7.35
    assert ps['P-76.3x3.2'][0]['Zx'] == 12.9
    cs = make_section_db(C_SEC_DATA)
    # pprint.pprint(cs)
    assert cs['C-100x50x20x2.3'][0]['Ix'] == 80.7


def test_xs_all_section_db():
    db = make_all_section_db()
    assert db['H-200x100x5.5x8'][0]['An'] == 26.67
    assert db['P-89.1x2.8'][0]['An'] == 7.59
    assert db['[-100x50x5x7.5'][0]['An'] == 11.92
    # assert db[xs_section_name('hs15')][0]['An'] == 17.85
    assert db[xs_section_name('h150*75')][0]['An'] == 17.85
    assert db[xs_section_name('H-150x75x5x7')][0]['An'] == 17.85
    assert db[xs_section_name('□P-100x100x3.2')][0]['An'] == 12.13
    # assert db[xs_section_name('KP100_32')][0]['An'] == 12.13
    assert db[xs_section_name('KP100*100*3.2')][0]['An'] == 12.13


@pytest.mark.skip('ディクショナリのコンバート時のみ実行用')
def test_convert_dict_to_CSharp_dict():
    for k, v in short_full_name.items():
        kw = '"{}"'.format(k)
        vw = '"{}"'.format(v)
        # print('"{}","{}"'.format(k, v), end='')
        print("{", kw, ",", vw, "}", end='')
        print(',', end='')


# @pytest.mark.skip('ディクショナリのキー追加の試作用')
def test_short_full_name_dict_modify():
    items = list(short_full_name.items())
    for item in items:
        k, v = item[0], item[1]
        if '_' in k:
            new_k = k.replace('_', '*')
            short_full_name[new_k] = v

    # pprint.pprint(short_full_name)
    assert short_full_name['L100*10'] == 'L-100x100x10'
    assert short_full_name['L100*7'] == 'L-100x100x7'
    assert short_full_name['L100*75*7'] == 'L-100x75x7'
    assert short_full_name['C100*50*2.3'] == 'C-100x50x20x2.3'
    assert short_full_name['H100'] == 'H-100x100x6x8'
    assert short_full_name['H19'] == 'H-198x99x4.5x7'
    assert short_full_name['H30'] == 'H-300x150x6.5x9'
    assert short_full_name['KP100*2.3'] == '□P-100x100x2.3'
    assert short_full_name['MZ100'] == '[-100x50x5x7.5'
    # assert short_full_name[''] == ''


@pytest.mark.skip('helpの出力確認用')
def test_xs_section_help():
    print(xs_section_help())


@pytest.mark.skip('出力確認用')
def test_xs_section_registered_all_names():
    db = make_all_section_db()
    # print(xs_section_all_data(db))
    # print(xs_section_all_data(db, ['H']))
    print(xs_section_all_data(db, 'H'))
    # print(xs_section_all_data(db, ['□']))
    # print(xs_section_all_data(db, '□'))
    # print(xs_section_all_data(db, ['P']))
    # print(xs_section_all_data(db, ['C']))
    # print(xs_section_all_data(db, ['[']))
    # print(xs_section_all_data(db, ['L']))


@pytest.mark.skip('出力確認用')
def test_show_all_data_name():
    # pprint.pprint(short_full_name)
    db = make_all_section_db()
    print(xs_show_all_data(db))


@pytest.mark.skip('出力確認用')
def test_make_short_name():
    db = make_all_section_db()
    pprint.pprint(make_short_name(db))


def test_section_type():
    db = make_all_section_db()
    # 断面の種類は、H形鋼、角形鋼管、鋼管、C形、溝形、山形　の６種類　2020-12時点
    assert xs_section_type("h19") == 'H'
    assert xs_section_type("H-200x100x5.5x8") == 'H'
    assert xs_section_type("KP100*100*3.2") == '□'
    assert xs_section_type("P-89.1x2.8") == 'P'
    assert xs_section_type("C100*50*2.3") == 'C'
    assert xs_section_type("[-100x50x5x7.5") == '['
    assert xs_section_type("L65*6") == 'L'
    assert xs_section_type("L65*65*6") == 'L'


def test_rotate_coordinate_system():
    assert rotated_coord((1, 1), math.radians(45)) == pytest.approx((1.4142135623731, 0))
    assert rotated_coord((-1, 1), math.radians(45)) == pytest.approx((0, 1.4142135623731))
    assert rotated_coord((-1, -1), math.radians(45)) == pytest.approx((-1.4142135623731, 0))
    assert rotated_coord((1, -1), math.radians(45)) == pytest.approx((0, -1.4142135623731))
    assert rotated_coord((1, 0), math.radians(30)) == pytest.approx((0.86602540378444, -0.5))


def test_get_point_on_arc():
    r1 = 10
    assert get_point_on_arc(r=r1, alpha=math.radians(45)) == pytest.approx((r1 / 2 ** 0.5, r1 / 2 ** 0.5))
    assert get_point_on_arc(r=r1, alpha=math.radians(135)) == pytest.approx((-r1 / 2 ** 0.5, r1 / 2 ** 0.5))
    assert get_point_on_arc(r=r1, alpha=math.radians(225)) == pytest.approx((-r1 / 2 ** 0.5, -r1 / 2 ** 0.5))
    assert get_point_on_arc(r=r1, alpha=math.radians(315)) == pytest.approx((r1 / 2 ** 0.5, -r1 / 2 ** 0.5))
    assert get_point_on_arc(r=r1, alpha=math.radians(0)) == pytest.approx((r1, 0))
    assert get_point_on_arc(r=r1, alpha=math.radians(360)) == pytest.approx((r1, 0))
    assert get_point_on_arc(r=r1, alpha=math.radians(0), dx=100, dy=-100) == pytest.approx((r1 + 100, 0 - 100))
    assert get_point_on_arc(r=r1, alpha=math.radians(45), dx=50, dy=20) == pytest.approx(
        (r1 / 2 ** 0.5 + 50, r1 / 2 ** 0.5 + 20))
    r1 = 7
    theta = 22
    assert get_point_on_arc(r=r1, alpha=math.radians(theta)) == pytest.approx(
        (r1 * math.cos(math.radians(theta)), r1 * math.sin(math.radians(theta))))


def test_get_points_on_arc():
    r1 = 10
    assert get_points_on_arc(r=r1, start=0., end=math.radians(90), n=2) == [(10.0, 0.0),
                                                                            (7.0710678118654755, 7.071067811865475),
                                                                            (6.123233995736766e-16, 10.0)]
    # print(get_points_on_arc(r=r1, start=0., end=math.radians(90), n=4))
    assert get_points_on_arc(r=r1, start=math.radians(270), end=math.radians(360), n=4) == [
        (-1.8369701987210296e-15, -10.0), (3.8268343236509, -9.238795325112866), (7.07106781186548, -7.07106781186547),
        (9.238795325112871, -3.8268343236508873), (10.0, 1.53142747957078e-14)]


def test_get_rotated_points():
    pts = [(0, 0), (0, 100), (75, 0)]
    dx, dy = -18.31, -30.59
    alpha = math.radians(28.709)
    expected = [(-30.75, -18.03), (17.28, 69.67), (35.03, -54.06)]  # CADでの作図結果
    result = get_rotated_points(pts, dx, dy, alpha)
    for i, res in enumerate(result):
        assert res == pytest.approx(expected[i], abs=0.01)

    # sample1  L-100x75x7
    alpha = math.radians(28.709)
    rp1 = get_point_on_arc(r=5, alpha=alpha, dx=2, dy=95)
    rp2 = get_point_on_arc(r=5, alpha=alpha, dx=70, dy=2)
    pts = [(0, 0), (0, 100), rp1, rp2, (75, 0)]
    dx, dy = -18.31, -30.59
    expected = [(-30.75, -18.03), (17.28, 69.67), (21.64, 64.33), (36.6, -49.91), (35.03, -54.06)]  # CADでの作図結果
    result = get_rotated_points(pts, dx, dy, alpha)
    for i, res in enumerate(result):
        assert res == pytest.approx(expected[i], abs=0.01)

    # sample2  BL-75x45x4.5
    alpha = math.radians(21.108)
    rp1 = get_point_on_arc(r=9, alpha=math.radians(180 + 21.108), dx=9, dy=9)
    pts = [rp1, (0, 9), (0, 75), (4.5, 75), (45, 4.5), (45, 0), (9, 0)]
    dx, dy = -10.38, -25.77
    expected = [(-16.33, -15.15), (-15.72, -11.91), (8.05, 49.66), (12.24, 48.04), (24.64, -32.31), (23.02, -36.51),
                (-10.57, -23.54)]  # CADでの作図結果
    result = get_rotated_points(pts, dx, dy, alpha)
    for i, res in enumerate(result):
        assert res == pytest.approx(expected[i], abs=0.01)

    # sample3  L-65x65x6
    alpha = math.radians(45)
    rp1 = get_point_on_arc(r=4, alpha=alpha, dx=2, dy=61)
    rp2 = get_point_on_arc(r=4, alpha=alpha, dx=61, dy=2)
    pts = [(0, 0), (0, 65), rp1, rp2, (65, 0)]
    dx, dy = -18.10, -18.10
    # print(get_rotated_points(pts, dx, dy, alpha))


def test_m11_m22_angle_stress_tmp():
    # sample1  L-100x75x7
    alpha = math.radians(28.7105604)
    rp1 = get_point_on_arc(r=5, alpha=alpha, dx=2, dy=95)
    rp2 = get_point_on_arc(r=5, alpha=alpha, dx=70, dy=2)
    pts = [(0, 0), (0, 100), rp1, rp2, (75, 0)]
    # dx, dy = -18.31, -30.59
    dx, dy = -18.315536018, -30.589142037
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    # Iu, Iv = 144.136, 30.76  # (cm4)
    Iu, Iv = 144.15192995, 30.761482438  # (cm4)

    Mu = 100 * math.cos(alpha)
    s11 = get_stress_at_points_m11(rotated_pts, Iu, Mu)
    # print(s11)
    assert s11 == [-1.0969875242490872, 4.239258052970119, 3.913990022196299, -3.0362139296547888, -3.289078220981322]
    Mv = 100 * math.sin(alpha)
    s22 = get_stress_at_points_m22(rotated_pts, Iv, Mv)
    # print(s22)
    assert s22 == [-4.803362514021558, 2.6985484170208016, 3.3782059204729507, 5.715067069812436, 5.469032686576473]
    # print([x + y for x, y in zip(s11, s22)])
    assert [x + y for x, y in zip(s11, s22)] == [-5.900350038270645, 6.937806469990921, 7.29219594266925,
                                                 2.6788531401576474, 2.1799544655951513]


def test_angle_section_bending_moment_stress():
    # sample1  L-100x75x7　円周上の点を追加
    alpha = math.radians(28.7088147)
    rpts1 = get_points_on_arc(r=5, dx=2, dy=95, start=0, end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=5, dx=70, dy=2, start=0, end=math.radians(90), n=32)

    pts = [(0, 0), (0, 100)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(75, 0)])

    dx, dy = -18.313859367, -30.586318718  # (mm)
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    Iu, Iv = 144.13587130, 30.759679370  # (cm4)
    Mx, My = 100, 0  # (kN*cm)

    ss = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, Mu=Mx * math.cos(alpha), Mv=Mx * math.sin(alpha))
    assert max(ss) == pytest.approx(7.3501, abs=0.001)
    assert min(ss) == pytest.approx(-5.8999, abs=0.001)

    # sample2  BL-75x45x4.5 円周上の点を追加
    alpha = math.radians(21.107967)
    rpts1 = get_points_on_arc(r=9, dx=9, dy=9, start=math.radians(180), end=math.radians(270), n=32)
    pts = []
    pts.extend(rpts1)
    pts.extend([(0, 9), (0, 75), (4.5, 75), (45, 4.5), (45, 0), (9, 0)])
    dx, dy = -10.380125, -25.7687

    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    Iu, Iv = 33.50109163, 4.68886877  # (cm4)

    ss = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, Mu=Mx * math.cos(alpha), Mv=Mx * math.sin(alpha))
    assert max(ss) == pytest.approx(22.7831, abs=0.001)
    assert min(ss) == pytest.approx(-17.1961, abs=0.001)

    # sample4  L-65x65x6 円周上の点を分割計算
    alpha = math.radians(45)
    rpts1 = get_points_on_arc(r=4, dx=2, dy=61, start=math.radians(0), end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=4, dx=61, dy=2, start=math.radians(0), end=math.radians(90), n=32)
    pts = [(0, 0), (0, 65)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(65, 0)])

    dx, dy = -18.096555532, -18.096555532
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    Iu, Iv = 46.579727445, 12.164198330  # (cm4)
    Mx, My = 100, 0  # (kN*cm)
    # ss = get_stress_at_points_mx_my(rotated_pts, alpha, Iu, Iv, Mx, My)
    ss = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, Mu=Mx * math.cos(alpha), Mv=Mx * math.sin(alpha))
    assert max(ss) == pytest.approx(19.7551, abs=0.001)
    assert min(ss) == pytest.approx(-14.8769, abs=0.001)

    # sample5  L-90x90x10 例題 円周上の点を分割計算
    alpha = math.radians(45)
    rpts1 = get_points_on_arc(r=7, dx=3, dy=83, start=math.radians(0), end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=7, dx=83, dy=3, start=math.radians(0), end=math.radians(90), n=32)

    pts = [(0, 0), (0, 90)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(90, 0)])

    dx, dy = -25.722377552, -25.722377552
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    Iu, Iv = 198.64812558, 51.619538241  # (cm4)
    Mx, My = 225, 0  # (kN*cm)

    ss = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, 207, 88.7)
    assert max(ss) == pytest.approx(11.5000, abs=0.001)
    assert min(ss) == pytest.approx(-6.2508, abs=0.001)
