# -*- coding: utf-8 -*-
__author__ = 'mskz'

import x_load.definition


dl = x_load.definition.Load("屋根DL", 300., "N/m2")
print("-"*40)
print(1)
print(dl.label)
print(2)
print("-"*40)

if __name__ == '__main__':
    dl = x_load.definition.Load("屋根DL", 300., "N/m2")

    print(dl)
    from __init__ import ureg, Q_
