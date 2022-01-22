import xlwings as xw
from cross_section.section import SectionDB
from cross_section.section import short_full_name
from pytest import approx

try:
    from cross_section import ureg, Q_
# except SystemError:
except ImportError:
    from __init__ import ureg, Q_

UNIT_CM = 'cm'
UNIT_MM = 'mm'
UNIT_M = 'm'

ERROR_FOR_NO_SECTION_PROPERTY = 'NO DATA'
ERROR_FOR_NO_SECTION_NAME = 'INVALID SECTION NAME'

# 断面データベース生成
db = SectionDB()
# db.load('C:/Users/user/PycharmProjects/set/cross_section/section.dat')
db.load('C:/Users/00014149/PycharmProjects/set/cross_section/section.dat')


def _strip_unit(src):
    """
    cm*2, mm**4 から、cm, mmだけを取り出す
    :param src: 文字列
    :return:
    """
    unit_base = ['c', 'm']
    res = ''
    for c in src.lower():
        if c in unit_base:
            res += c
    return res


@xw.func
def section_db(name, param, unit=None):
    """鋼材の断面諸量を返す"""
    # db = SectionDB()
    # db.load('./cross_section/section.dat')
    global db
    try:
        sec = db.get_section(short_full_name[name.upper()])
    except KeyError:
        return ERROR_FOR_NO_SECTION_NAME
    if param.upper() == 'NAME':
        return sec.name
    else:
        try:
            val = sec.get_prop(param)
            src_dim = str(val.dimensionality)[-1]
            # print('src_dim:',str(val.dimensionality),':',src_dim)
            if src_dim not in ['2', '3', '4']:
                src_dim = ''
            if unit:
                to_unit = _strip_unit(unit)
                if src_dim:
                    to_unit = to_unit + '**' + src_dim
                return val.to(to_unit).magnitude
            else:
                return val.magnitude
        except KeyError:
            return ERROR_FOR_NO_SECTION_PROPERTY


#
def test_db():
    assert section_db('HS19', 'Name') == 'H-198x99x4.5x7'
    assert section_db('HS19', 'H') == 198.
    assert section_db('hs19', 'H', 'cm') == 19.8
    assert section_db('hs19', 'H', 'm') == 0.198
    assert section_db('HS19', 'B') == 99.
    assert section_db('HS19', 't1') == 4.5
    assert section_db('HS19', 't2') == 7.
    assert section_db('HS19', 'Ix') == 1540.
    assert section_db('HS19', 'Ix', 'mm4') == approx(1540*10000)
    assert section_db('HS19', 'Zx') == 156.
    assert section_db('hs19', 'Zx') == 156.
    assert section_db('hs19', 'Zx', 'mm') == 156.*1000
    assert section_db('HS19', 'ix') == 8.25
    assert section_db('HS19', 'An') == 22.69
    assert section_db('hs19', 'An', 'mm2') == 2269
    assert section_db('hs19', 'An', 'M') == 0.002269
    assert section_db('HS19', 'η') == 7.43
    assert section_db('HS19', 'Ae') == ERROR_FOR_NO_SECTION_PROPERTY
    assert section_db('HS198', 'An') == ERROR_FOR_NO_SECTION_NAME


def test_strip_unit():
    # a = Q_('100mm^2')
    # print(a)
    # print(a.units)
    # print(type(str(a.units)))
    # print(a.dimensionality)
    # print(type(str(a.dimensionality)))
    # print(a.compatible_units('cm'))
    # print(a.to('cm'))
    assert _strip_unit('cm') == UNIT_CM
    assert _strip_unit('mm') == UNIT_MM
    assert _strip_unit('M^2') == UNIT_M
    assert _strip_unit('cm3') == UNIT_CM
    assert _strip_unit('cm**4') == UNIT_CM
    assert _strip_unit('(mm**4)') == UNIT_MM
    # assert _strip_unit('ｃｍ') == UNIT_CM   # 全角処理どうするか？
