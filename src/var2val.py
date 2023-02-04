import re


def add_space_around_operator(txt):
    operators = ['+', '-', '*', '/', '%', '^', '(', ')', 'MOD', '\\']
    for op in operators:
        txt = txt.replace(op, ' ' + op + ' ')
    return txt


def var2val(txt, var_val):
    # result = re.split('[\+\-\*/\^]', txt)
    txt = add_space_around_operator(txt)
    txt_lst = txt.split(' ')
    result = []
    for wd in txt_lst:
        if wd in var_val.keys():
            result.append(str(var_val[wd]))
        else:
            result.append(wd)
    return "".join(result)


