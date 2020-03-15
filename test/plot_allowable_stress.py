# -*- coding: utf-8 -*-

from allowable_stress import steel_ft, steel_fc_aij, steel_fc_bsl, steel_fb2_aij, steel_fb_aij, steel_fb1_aij, \
    steel_fb_bsl, steel_fs, steel_fb_aij2005, steel_fb_aij2002, calc_C

from cross_section.xs_section import make_all_section_db
import matplotlib.pyplot as plt


# import numpy as np


def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    F = 235
    i = 1
    Af = 1

    x = []
    y = []
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=F, lb=lb, i=i, C=1, h=10, Af=Af))
    ax.plot(x, y)

    x.clear()
    y.clear()
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=F, lb=lb, i=i, C=2.3, h=10, Af=Af))
    # ax.plot(x, y)

    x.clear()
    y.clear()
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=F, lb=lb, i=i, C=2.3, h=4, Af=Af))
    # ax.plot(x, y)

    db = make_all_section_db()
    x.clear()
    y.clear()
    shape = 'H-200x100x5.5x8'
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_aij2005(shape, db, lb=lb, M3=1))
    ax.plot(x, y)

    ax.grid()
    ax.set_ylim(0, 160)
    # ax.set_ylim(0, 220)
    ax.set_xlim(0, 250)
    plt.show()


def data_plot2():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x = []
    y = []

    db = make_all_section_db()
    shape = 'H-200x100x5.5x8'
    # shape = 'H-300x150x6.5x9'
    # shape = 'H-400x200x8x13'
    # shape = 'H-600x200x11x17'
    # shape = 'H-488x300x11x18'
    L = 6 * 1000  # mm
    pitch = 5
    m1 = 2
    m2 = -1
    m3 = 5

    x.clear()
    y.clear()
    for lb in range(1, L, pitch):
        x.append(lb)
        y.append(steel_fb_aij2005(shape, db, lb=lb, M1=m1, M2=m2, M3=m3))
    ax.plot(x, y, label='aij 2005')

    x.clear()
    y.clear()
    for lb in range(1, L, pitch):
        x.append(lb)
        y.append(steel_fb_aij2002(shape, db, lb=lb, M1=m1, M2=m2, M3=m3))
    ax.plot(x, y, ls='--', label='aij 1973')

    ax.grid(ls='--')
    ax.set_ylim(0, 160)
    ax.set_xlim(0, L)
    ib = db[shape][0]['ib']
    info = '{}\nib={}(cm), C={:.2f}\n lambda=0~{:.0f}'.format(shape,ib , calc_C(m1, m2, m3),L/(ib*10))
    # ax.annotate(info, xy=(0.015, 0.02), xycoords='axes fraction')
    plt.ylabel('fb (N/mm2)')
    plt.xlabel('Lb (mm)')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right', title=info)

    plt.show()



if __name__ == '__main__':
    # data_plot()
    data_plot2()
