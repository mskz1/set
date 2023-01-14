import xlwings as xw

import allowable_stress as alws
import rebar
import bolt
import xs_section
import text_calc

XL_CATEGORY = 'Structural Engineering Tools'

db = xs_section.make_all_section_db()


@xw.func(category=XL_CATEGORY)
@xw.arg('t', doc='文字列')
def calcText(t, caller):
    """文字列から、[...]で囲まれた部分を除き、数式として計算する"""
    return caller.sheet.Evaluate(text_calc.strip_square_brackets(t))


@xw.func(category=XL_CATEGORY)
def xsVersion():
    return "xl_set AddIn, Test ver.2022-1231"


@xw.func(category=XL_CATEGORY)
@xw.arg('F', doc='F値(N/mm2)')
def xsSteel_ft(F):
    """長期許容引張応力度(N/mm2)を返す関数"""
    return alws.steel_ft(F)


@xw.func(category=XL_CATEGORY)
@xw.arg('F', doc='F値(N/mm2)')
def xsSteel_fs(F):
    """長期許容せん断応力度(N/mm2)を返す関数"""
    return alws.steel_fs(F)


@xw.func(category=XL_CATEGORY)
@xw.arg('F', doc='F値(N/mm2)')
@xw.arg('lamb', doc='細長比')
def xsSteel_fc_bsl(F, lamb):
    """長期許容圧縮応力度(N/mm2)を返す関数。建築基準法(Building Standard Law)版"""
    return alws.steel_fc_bsl(F, lamb)


@xw.func(category=XL_CATEGORY)
@xw.arg('F', doc='F値(N/mm2)')
@xw.arg('Lb', doc='圧縮フランジの支点間距離(mm)')
@xw.arg('ib', doc='断面二次半径(mm)')
@xw.arg('C', doc='補正係数')
@xw.arg('h', doc='はりのせい(mm)')
@xw.arg('Af', doc='圧縮フランジの断面積(mm2)')
def xsSteel_fb_bsl(F, Lb, ib, C, h, Af):
    """長期許容曲げ応力度(N/mm2)を返す関数。建築基準法(Building Standard Law)版"""
    return alws.steel_fb_bsl(F, Lb, ib, C, h, Af)


@xw.func(category=XL_CATEGORY)
@xw.arg('F', doc='F値(N/mm2)')
@xw.arg('secName', doc='断面名称')
@xw.arg('Lb', doc='圧縮フランジの支点間距離(mm)')
@xw.arg('M1', doc='座屈補剛区間端部の大きい方のM')
@xw.arg('M2', doc='座屈補剛区間端部の小さい方のM')
@xw.arg('M3', doc='座屈補剛区間内の最大のM')
def xsSteel_fb_aij2005(F, secName, Lb, M1, M2, M3):
    """長期許容曲げ応力度(N/mm2)を返す関数。建築基準法(Building Standard Law)版"""
    return alws.steel_fb_aij2005(secName, db, Lb, M1, M2, M3, F)


@xw.func(category=XL_CATEGORY)
@xw.arg('size', doc='鉄筋径 D10, D13, D16...')
@xw.arg('propertyName', doc='データ名 d, DO, A, L')
def xsRebarSpec(size, propertyName):
    """鉄筋関連のデータを返す関数"""
    return rebar.rebar_spec(size, propertyName)


@xw.func(category=XL_CATEGORY)
@xw.arg('strength', doc='強度区分 F10T, F8T, 6T, 4T')
@xw.arg('size', doc='ボルトサイズ M16, M20...')
@xw.arg('propertyName', doc='データ名 Qal, Qas, Tal...')
def xsBoltSpec(strength, size, propertyName):
    """ボルト関連のデータを返す関数"""
    return bolt.xs_bolt_spec(strength, size, propertyName)


@xw.func(category=XL_CATEGORY)
@xw.arg('abbrName', doc='断面略称（H20,h194*150など）')
def xsSectionName(abbrName):
    """形鋼の略称からフル名称を返す関数"""
    return xs_section.xs_section_name(abbrName)


@xw.func(category=XL_CATEGORY)
@xw.arg('name', doc='断面略称（H20など）あるいはフル名称')
@xw.arg('propertyName', doc='断面特性名（ALL,An,Ix,Zxなど）')
def xsSectionProperty(name, propertyName):
    """形鋼の断面性能値を返す関数"""
    return xs_section.xs_section_property(name, propertyName, db)


