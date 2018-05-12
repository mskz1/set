import xlwings as xw
from cross_section.section import SectionDB
from cross_section.section import short_full_name

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
db.load('./cross_section/section.dat')


def _strip_unit(src):
    """
    cm*2, mm**4 から、cm, mmだけを取り出す
    :return:
    """
    return UNIT_CM


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
            return sec.get_prop(param).magnitude
        except KeyError:
            return ERROR_FOR_NO_SECTION_PROPERTY


# TODO 指定した単位で返す
def test_db():
    assert section_db('HS19', 'Name') == 'H-198x99x4.5x7'
    assert section_db('HS19', 'H') == 198.
    # assert section_db('hs19', 'H', 'cm') == 19.8
    assert section_db('HS19', 'B') == 99.
    assert section_db('HS19', 't1') == 4.5
    assert section_db('HS19', 't2') == 7.
    assert section_db('HS19', 'Ix') == 1540.
    assert section_db('HS19', 'Zx') == 156.
    assert section_db('hs19', 'Zx') == 156.
    assert section_db('HS19', 'ix') == 8.25
    assert section_db('HS19', 'An') == 22.69
    assert section_db('HS19', 'η') == 7.43
    assert section_db('HS19', 'Ae') == ERROR_FOR_NO_SECTION_PROPERTY
    assert section_db('HS198', 'An') == ERROR_FOR_NO_SECTION_NAME


def test_strip_unit():
    assert _strip_unit('cm') == UNIT_CM
    assert _strip_unit('mm') == UNIT_MM

