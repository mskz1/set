import xloil as xlo

import allowable_stress as alws
import rebar
import bolt
import xs_section
import text_calc
import var2val

XL_CATEGORY = 'Structural Engineering Tools'

db = xs_section.make_all_section_db()


def range2dict(app, rng):
    """
    エクセルのセルレンジの最左列に変数名、最右列に値が入っているとして変数名：値の辞書オブジェクトを返す

    2023-0224 仮実装　要テスト xloil必要
    :return:
    """
    result = {}
    for rn in rng.Areas:
        col_idx_left = rn.Column
        col_idx_right = rn.Columns(rn.Column.Count).Column
        row_idx_top = rn.Row
        row_idx_bottom = rn.Rows(rn.Rows.Count).Row

        for row_idx in range(row_idx_top, row_idx_bottom + 1):
            if app.Cells(row_idx, col_idx_left).Value:
                result[str(app.Cells(row_idx, col_idx_left).Value)] = app.Cells(row_idx, col_idx_right).Value
    return result


@xlo.func(group=XL_CATEGORY, args={'t': '文字列', 'rng': '変数名と価のセル範囲'})
def var2val(t, rng):
    """文字列内の変数名を価で置き換えた文字列を返す。"""
    var_val = range2dict(xlo.app(), rng)
    return var2val.var2val(t, var_val)


@xlo.func(group=XL_CATEGORY,
          args={'t': '文字列', 'calc': '数式を計算するか（TRUE/FALSE）'})
def calcText(t, calc=True):
    """文字列から、[...]で囲まれた部分を除き、数式として計算する"""
    # return xlo.Caller().Worksheet.Evaluate(text_calc.strip_square_brackets(t))
    if calc:
        return xlo.active_worksheet().Evaluate(text_calc.strip_square_brackets(t))
    else:
        return text_calc.strip_square_brackets(t)


@xlo.func(group=XL_CATEGORY)
def xsVersion():
    return "xl_set AddIn, Test ver.2022-1231"


@xlo.func(group=XL_CATEGORY,
          args={'F': 'F値(N/mm2)'})
def xsSteel_ft(F):
    """長期許容引張応力度(N/mm2)を返す関数"""
    return alws.steel_ft(F)


@xlo.func(group=XL_CATEGORY,
          args={'F': 'F値(N/mm2)'})
def xsSteel_fs(F):
    """長期許容せん断応力度(N/mm2)を返す関数"""
    return alws.steel_fs(F)


@xlo.func(group=XL_CATEGORY,
          args={'F': 'F値(N/mm2)', 'lamb': '細長比'})
def xsSteel_fc_bsl(F, lamb):
    """長期許容圧縮応力度(N/mm2)を返す関数。建築基準法(Building Standard Law)版"""
    return alws.steel_fc_bsl(F, lamb)


@xlo.func(group=XL_CATEGORY,
          args={'F': 'F値(N/mm2)', 'Lb': '圧縮フランジの支点間距離(mm)', 'ib': '断面二次半径(mm)', 'C': '補正係数', 'h': 'はりのせい(mm)',
                'Af': '圧縮フランジの断面積(mm2)'})
def xsSteel_fb_bsl(F, Lb, ib, C, h, Af):
    """長期許容曲げ応力度(N/mm2)を返す関数。建築基準法(Building Standard Law)版"""
    return alws.steel_fb_bsl(F, Lb, ib, C, h, Af)


@xlo.func(group=XL_CATEGORY,
          args={'F': 'F値(N/mm2)', 'secName': '断面名称', 'Lb': '圧縮フランジの支点間距離(mm)', 'M1': '座屈補剛区間端部の大きい方のM',
                'M2': '座屈補剛区間端部の小さい方のM', 'M3': '座屈補剛区間内の最大のM'})
def xsSteel_fb_aij2005(F, secName, Lb, M1, M2, M3):
    """長期許容曲げ応力度(N/mm2)を返す関数。建築基準法(Building Standard Law)版"""
    return alws.steel_fb_aij2005(secName, db, Lb, M1, M2, M3, F)


@xlo.func(group=XL_CATEGORY,
          args={'size': '鉄筋径 D10, D13, D16...', 'propertyName': 'データ名 d, DO, A, L'})
def xsRebarSpec(size, propertyName):
    """鉄筋関連のデータを返す関数"""
    return rebar.rebar_spec(size, propertyName)


@xlo.func(group=XL_CATEGORY,
          args={'strength': '強度区分 F10T, F8T, 6T, 4T', 'size': 'ボルトサイズ M16, M20...',
                'propertyName': 'データ名 Qal, Qas, Tal...'})
def xsBoltSpec(strength, size, propertyName):
    """ボルト関連のデータを返す関数"""
    # __doc__ = bolt.xs_bolt_spec.__doc__
    return bolt.xs_bolt_spec(strength, size, propertyName)


@xlo.func(group=XL_CATEGORY,
          args={'abbrName': '断面略称（H20,h194*150,kp100*3.2など）'})
def xsSectionName(abbrName):
    """形鋼の略称からフル名称を返す関数"""
    return xs_section.xs_section_name(abbrName)


@xlo.func(group=XL_CATEGORY,
          args={'name': '断面略称（H20など）あるいはフル名称',
                'propertyName': '断面特性名（ALL,An,Ix,Zxなど）'})
def xsSectionProperty(name, propertyName):
    """形鋼の断面性能値を返す関数"""
    return xs_section.xs_section_property(name, propertyName, db)
