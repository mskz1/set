import pytest

from src.var2val import *


def make_dict():
    return dict(a=2, b=3, c=4, x=1.1, y=2.2, α=111, β=222, γ=333)


var_value_csv = """
a,=,,2
b,=,,10
x,=,,9.8
y,=,,11.5"""


def test_add_space_around_operator():
    assert add_space_around_operator('a+b') == 'a + b'
    assert add_space_around_operator('a+b-c/d+(2*x/y)^2') == 'a + b - c / d +  ( 2 * x / y )  ^ 2'


def test_var2val():
    var_dict = make_dict()
    assert var2val("a*b", var_dict) == '2*3'
    assert var2val("a+b+c-a-b-c*a/b^c", var_dict) == '2+3+4-2-3-4*2/3^4'
    assert var2val("a + b + c - a - b - c*a/b^c", var_dict) == '2+3+4-2-3-4*2/3^4'
