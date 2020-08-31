# -*- coding: utf-8 -*-

from allowable_stress import steel_fb_bsl, steel_fb_aij2005, steel_fb_aij2002, calc_C

from xs_section import make_all_section_db, xs_section_property, xs_section_name
import matplotlib.pyplot as plt


def main_truss_lower_chord():
    MEM_SIZE = 'size'
    L_WARIKOMI = 'len_warikomi'  # GPL割り込み長さ
    T_GPL = 't_gpl'  # GPL 板厚
    D_GPL = 'd_gpl'  # GPL せい（ボルト位置）

    N_BOLT = 'n_bolt'
    SIZE_BOLT = 'size_bolt'
    DE_GPL = 'd_end_gpl'    # 柱端部GPLせい
    # 母材
    members = ['KP175*175*9', 'KP175*175*6', 'KP150*150*9', 'KP150*150*6']

    kp175_9 = {MEM_SIZE: 'KP175*175*9', L_WARIKOMI: 350, T_GPL: 16, D_GPL: 260, N_BOLT: 4, SIZE_BOLT:'M22'
               }


    for m in members:
        print(xs_section_name(m), xs_section_property(m, 'An'))

    pass
    print(kp175_9)


if __name__ == '__main__':
    main_truss_lower_chord()
    pass
