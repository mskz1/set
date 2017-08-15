# -*- coding: utf-8 -*-
__author__ = 'mskz'


import unit.definition as u
import nose


def test1():
    f1 = u.UaNum(10., u.kN)
    print(f1)


def test_numericalunit():
    import numericalunits as nu
    nu.reset_units('SI')
    l1 = 1000.0 * nu.mm
    print(l1/nu.mm)
    l2 = 1000.
    print(l2)


def test_pint():
    from pint import UnitRegistry
    ur = UnitRegistry()
    d1 = 1000. * ur.mm
    d2 = 0.5 * ur.m
    d3 = d1+d2

    print("-"*30,"d3")
    print("{:~}".format(d3))
    print(d3.to('mm'))
    print("{:~}".format(d3))

    print("-"*30,"f1")
    f1 = 10. * ur.kN
    print(f1)
    print("{:~}".format(f1))

    print("-"*30,"m1")
    m1 = f1*d2
    print(m1)
    print("{:~}".format(m1))

    print(m1.to('kN*cm'))
    m2 = 50. * ur.kN * ur.m
    print(m2)
    print("{:~}".format(m2))

    print("-"*30,"s1")
    a1 = 10.*ur.cm**2
    s1 = f1 / a1
    print(s1.to('kN/cm^2'))
    print("{:~}".format(s1))
    print("{:P}".format(s1))


if __name__ == '__main__':
    # nose.main()
    # test1()
    #test_numericalunit()
    test_pint()