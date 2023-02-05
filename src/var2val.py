# import re

SPACE_CHAR = '#'


def replace_space_moji(txt):
    return txt.replace(' ', ' ' + SPACE_CHAR + ' ')


def add_space_around_operator(txt):
    operators = ['+', '-', '*', '/', '%', '^', '(', ')', 'MOD', '\\']
    for op in operators:
        txt = txt.replace(op, ' ' + op + ' ')
    return txt


def var2val(txt, var_val):
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
