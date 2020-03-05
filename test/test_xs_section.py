# -*- coding: utf-8 -*-
import pytest, pprint

from cross_section.xs_section import *


def test_xs_H_sec_name():
    assert xs_section_name('HS20') == 'H-200x100x5.5x8'
    assert xs_section_name('HS15') == 'H-150x75x5x7'
    assert xs_section_name('hs15') == 'H-150x75x5x7'
    # with pytest.raises(KeyError):
    #     xs_section_name('hs100')
    assert xs_section_name('hs100') == 'Section_Not_Defined'
    assert xs_section_name('C100_23') == 'C-100x50x20x2.3'
    assert xs_section_name('C100*23') == 'C-100x50x20x2.3'
    assert xs_section_name('KP100*32') == '□P-100x100x3.2'
    assert xs_section_name('HM700') == 'H-700x300x13x24'
    assert xs_section_name('HM900') == 'H-900x300x16x28'


# @pytest.mark.skip()
def test_xs_section_property():
    # assert set(xs_section_property('HS20')) == {'H', 'An', 'Ix', 'Iy', 'ix', 'iy', 'Zx', 'Zy'}
    assert xs_section_property('HS20') == ['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)',
                                           'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)',
                                           'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']
    assert xs_section_property('HS20',
                               'ALL') == "['H(mm)', 'B(mm)', 't1(mm)', 't2(mm)', 'r(mm)', 'An(cm**2)', 'W(kgf/m)', 'Ix(cm**4)', 'Iy(cm**4)', 'ix(cm)', 'iy(cm)', 'Zx(cm**3)', 'Zy(cm**3)', 'ib(cm)', 'eta(-)', 'Zpx(cm**3)', 'Zpy(cm**3)']"

    assert xs_section_property('HS20', 'An') == 26.67  # unit:cm2
    assert xs_section_property('H-200x100x5.5x8', 'An') == 26.67  # unit:cm2
    # assert xs_section_property('H-199x199x5x5', 'An') == 'Section_Not_Defined'
    assert xs_section_property('H-199x199x5x5', 'An') == 'NO_DATA'

    db = make_all_section_db()
    assert xs_section_property('HS20', 'An', db) == 26.67  # unit:cm2
    assert xs_section_property('hs20', 'An', db) == 26.67  # unit:cm2
    assert xs_section_property('hm900', 'An', db) == 305.8
    assert xs_section_property('hm900', 'Ix', db) == 404000
    assert xs_section_property('hm900', 'Zx', db) == 8990


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
    assert db[xs_section_name('hs15')][0]['An'] == 17.85
    assert db[xs_section_name('H-150x75x5x7')][0]['An'] == 17.85
    assert db[xs_section_name('□P-100x100x3.2')][0]['An'] == 12.13
    assert db[xs_section_name('KP100_32')][0]['An'] == 12.13


@pytest.mark.skip('ディクショナリのコンバート時のみ実行用')
def test_convert_dict_to_CSharp_dict():
    for k, v in short_full_name.items():
        kw = '"{}"'.format(k)
        vw = '"{}"'.format(v)
        # print('"{}","{}"'.format(k, v), end='')
        print("{", kw, ",", vw, "}", end='')
        print(',', end='')


@pytest.mark.skip('ディクショナリのキー追加の試作用')
def test_short_full_name_dict_modify():
    items = list(short_full_name.items())
    for item in items:
        k, v = item[0], item[1]
        if '_' in k:
            new_k = k.replace('_', '*')
            short_full_name[new_k] = v
    pprint.pprint(short_full_name)


@pytest.mark.skip('helpの出力確認')
def test_xs_section_help():
    print(xs_section_help())


@pytest.mark.skip('出力確認')
def test_xs_section_registered_all_names():
    db = make_all_section_db()
    # print(xs_section_all_data(db))
    print(xs_section_all_data(db, ('H')))
    print(xs_section_all_data(db, ['□']))
    print(xs_section_all_data(db, ['P']))
    print(xs_section_all_data(db, ['C']))
    print(xs_section_all_data(db, ['[']))

def test_make_short_name():
    db = make_all_section_db()
    make_short_name(db)
