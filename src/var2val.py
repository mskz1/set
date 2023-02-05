# import re

SPACE_CHAR = '#'
# SPACE_CHAR_ZENKAKU = '＃'


def replace_space_moji(txt):
    """
    意図的に入力されているスペースを別の文字に一旦置き換える。
    :param txt:
    :return:
    """
    return txt.replace(' ', ' ' + SPACE_CHAR + ' ')


def add_space_around_operator(txt):
    """
    演算子の前後にスペースを追加する。
    :param txt:
    :return:
    """
    operators = ['+', '-', '*', '/', '%', '^', '(', ')', 'MOD', '\\'] \
                + ['＋', 'ー', '＊', '／', '％', '＾', '（', '）']
    for op in operators:
        txt = txt.replace(op, ' ' + op + ' ')
    return txt


def var2val(txt, var_val):
    """
    変数名の含まれる計算式の文字列の、変数名を実際の値に置き換えた文字列にして返す。
    :param txt:
    :param var_val:
    :return:
    """
    txt_m = add_space_around_operator(replace_space_moji(txt))
    txt_lst = txt_m.split(' ')
    result = []
    for wd in txt_lst:
        if wd in var_val.keys():
            result.append(str(var_val[wd]))
        elif wd == SPACE_CHAR:
            result.append(' ')
        else:
            result.append(wd)
    return "".join(result)
