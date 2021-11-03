# -*- coding: utf-8 -*-
import pytest
import pprint

from text_calc import strip_square_brackets,get_square_brackets_index

""" VBA の textCalc udf のpython版

サンプル

excelのセルへの入力から数式計算に不要なものを除く

A1セルへの入力（文字）
0.6[kN/m2] * 3.2[m] * 3.4[m]

A2 セルへの入力
=calcText(A1)

A2セルの計算結果は、
0.6*3.2*3.4 の結果が入る

"""

@pytest.mark.skip('tmp')
def test_strip_square_brackets():
    src_txt = '0.6[kN/m2]'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '0.6'

    src_txt = '3.2[m]'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '3.2'



def test_square_brackets_index():
    # 有効な例
    src_txt = '0123 [567] 9'
    get_square_brackets_index(src_txt)
    # assert get_square_brackets_index(src_txt) == (4,8)

    # 有効な例
    src_txt = '0123 [567] 9xxx [zz] x [zzz] xx [ zzzzz ] xx'
    get_square_brackets_index(src_txt)

    # 有効な例　全角混じり
    src_txt = '0123［567] 9xxx[zz] x [zzz] xx [ zzzzz ] xx'
    get_square_brackets_index(src_txt)


    # エラーの例　バランスしていない。括弧の数が違う
    src_txt = 'x [ zz [ zz ] xxx [z] x [zz] xx [zz] xx'
    get_square_brackets_index(src_txt)




    # エラーの例　括弧が入れ子
    src_txt = 'xx [ zz [ z ] z ] xxx [zz] xx [zzz] xx [zz] xx'
    get_square_brackets_index(src_txt)


