# -*- coding: utf-8 -*-
import pytest
import pprint

from xs_section import *


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


def test_angle_property_calc_Iu_Iv_sample():
    import math

    def get_eu_ev(A, B, alpha, cx, cy):
        eu1 = -10 * cy * math.sin(alpha) + (10 * cx - A) * math.cos(alpha)
        eu2 = (B - 10 * cy) * math.sin(alpha) + 10 * cx * math.cos(alpha)
        ev1 = -10 * cy * math.cos(alpha) - 10 * cx * math.sin(alpha)
        ev2 = (B - 10 * cy) * math.cos(alpha) - 10 * cx * math.sin(alpha)
        ev2a = -10 * cy * math.cos(alpha) - (10 * cx - A) * math.sin(alpha)
        return eu1, eu2, ev1, ev2, ev2a

    db = make_all_section_db()
    sec = 'L-90x90x10'
    A = xs_section_property(sec, 'A', db)
    B = xs_section_property(sec, 'B', db)
    t = xs_section_property(sec, 't', db)
    Iu = xs_section_property(sec, 'Iu', db)
    Iv = xs_section_property(sec, 'Iv', db)
    cy = xs_section_property(sec, 'Cx', db)
    cx = xs_section_property(sec, 'Cy', db)
    # cx = 2.57
    # cy = 2.57
    # print(A, B, t, cx, cy, Iu, Iv)
    alpha = math.pi / 4.
    eu1_s = A * math.sin(alpha)
    ev1_s = 10 * cx / math.sin(alpha)
    ev2_s = A * math.cos(alpha) - 10 * cx / math.sin(alpha)
    # print(eu1_s, ev1_s, ev2_s)
    # eu1 = -10 * cy * math.sin(alpha) + (10 * cx - A) * math.cos(alpha)
    # eu2 = (B - 10 * cy) * math.sin(alpha) + 10 * cx * math.cos(alpha)
    # ev1 = -10 * cy * math.cos(alpha) - 10 * cx * math.sin(alpha)
    # ev2 = (B - 10 * cy) * math.cos(alpha) - 10 * cx * math.sin(alpha)
    # eu1, eu2, ev1, ev2, ev2a = get_eu_ev(A, B, alpha, cx, cy)
    eu1, eu2, ev1, ev2 = get_eu_ev_of_angle(A, B, alpha, cx, cy)

    # print(eu1, eu2, ev1, ev2)
    assert eu1 == pytest.approx(63.63961030678927)
    assert eu2 == pytest.approx(63.63961030678927)
    assert ev1 == pytest.approx(36.345288552988535)
    assert ev2 == pytest.approx(27.294321753800737)
    print(10 * Iu / eu1, 10 * Iv / ev1)

    zu, zv = get_Zu_Zv_of_angle(sec, db)
    print(zu, zv)

    # print('-' * 30)
    # L-100x75x7
    A = 100
    B = 75
    t = 7
    Iu = 144
    Iv = 30.8
    # cx = 1.83
    cx = 3.06
    # cy = 3.06
    cy = 1.83
    # print(A, B, t, cx, cy, Iu, Iv)
    alpha = math.atan(0.548)
    # アングルのフィレット部は考慮しない
    eu1, eu2, ev1, ev2, ev2a = get_eu_ev(A, B, alpha, cx, cy)
    eu1, eu2, ev1, ev2 = get_eu_ev_of_angle(A, B, alpha, cx, cy)
    # print(eu1, eu2, ev1, ev2, ev2a)
    assert eu1 == pytest.approx(69.65517135983993)
    assert eu2 == pytest.approx(54.08324813335662)
    assert ev1 == pytest.approx(30.75377665147421)
    assert ev2 == pytest.approx(35.01788502102573)
    # assert ev2a == pytest.approx(17.303384143899073)
    zu, zv = get_Zu_Zv_of_angle('L-100x75x7')
    print('L-100x75x7 : Zu, Zv', zu, zv)
    Iu_100x75 = xs_section_property('L-100x75x7', 'Iu')
    Iv_100x75 = xs_section_property('L-100x75x7', 'Iv')
    print('L-100x75 : Iu, Iv', Iu_100x75, Iv_100x75)



def test_get_zu_zv_of_angle():
    db = make_all_section_db()
    sec_name = 'L90*10'
    zu, zv = get_Zu_Zv_of_angle(sec_name, db)
    assert zu == pytest.approx(31.269, abs=0.01)
    assert zv == pytest.approx(14.224, abs=0.01)
    sec_name = 'L-100x75x7'
    zu, zv = get_Zu_Zv_of_angle(sec_name, db)
    assert zu == pytest.approx(20.673, abs=0.01)
    assert zv == pytest.approx(8.795, abs=0.01)
