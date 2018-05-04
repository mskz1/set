import xlwings as xw
from cross_section.section import SectionDB
from cross_section.section import short_full_name

CM = ['cm', 'CM', 'cm2', 'cm3', 'cm4']


@xw.func
def sectionDB(name, param, unit=None):
    """鋼材の断面諸量を返す"""
    db = SectionDB()
    db.load('./cross_section/section.dat')
    sec = db.get_section(short_full_name[name])
    return sec.get_prop(param).magnitude
