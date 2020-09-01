# -*- coding: utf-8 -*-

import allowable_stress
from xs_section import make_all_section_db, xs_section_property, xs_section_name
import matplotlib.pyplot as plt
import weld
import bolt


def main_truss_lower_chord():
    MEM_SIZE = 'size'
    L_WARIKOMI = 'len_warikomi'  # GPL割り込み長さ
    T_GPL = 't_gpl'  # GPL 板厚
    D_GPL = 'd_gpl'  # GPL せい（ボルト位置）

    N_BOLT = 'n_bolt'
    SIZE_BOLT = 'size_bolt'
    DE_GPL = 'd_end_gpl'  # 柱端部GPLせい

    members = []
    kp175_9 = {MEM_SIZE: 'KP175*175*9', L_WARIKOMI: 350, T_GPL: 16, D_GPL: 260, N_BOLT: 4, SIZE_BOLT: 'M22'
               }
    kp175_9_2 = {MEM_SIZE: 'KP175*175*9', L_WARIKOMI: 300, T_GPL: 12, D_GPL: 320, N_BOLT: 4, SIZE_BOLT: 'M20'
                 }
    kp150_9 = {MEM_SIZE: 'KP150*150*9', L_WARIKOMI: 250, T_GPL: 12, D_GPL: 260, N_BOLT: 4, SIZE_BOLT: 'M20'
               }

    members.append(kp175_9)
    members.append(kp175_9_2)
    members.append(kp150_9)

    for m in members:
        print("=" * 40)
        print("母材断面：{}".format(xs_section_name(m[MEM_SIZE])))
        print("母材 断面積：{} [cm2]".format(xs_section_property(m[MEM_SIZE], 'An')))
        mem_strength_tensile = xs_section_property(m[MEM_SIZE], 'An') * 23.5  # kN

        print("母材 許容引張耐力：{:.2f} [kN]".format(mem_strength_tensile))
        lk = 400.
        i = xs_section_property(m[MEM_SIZE], 'ix')
        mem_strength_compression = xs_section_property(m[MEM_SIZE], 'An') * 100. * allowable_stress.steel_fc_bsl(
            lambda_=lk / i) * 1.5 / 1000.
        print("　設定座屈長さ:{} [cm]".format(lk))
        print("母材 許容圧縮耐力：{:.2f} [kN]".format(mem_strength_compression))
        print("母材 許容圧縮耐力　x 0.5：{:.2f} [kN]".format(mem_strength_compression * 0.5))

        # 鋼管割り込み部　溶接
        t = xs_section_property(m[MEM_SIZE], 't')
        warikomi_weld_strength = weld.fillet_weld_strength(m[L_WARIKOMI], weld.fillet_weld_size(t), n=4) * 1.5 / 1000.
        print("　鋼管割り込み長さ：{} [mm]".format(m[L_WARIKOMI]))
        print("割り込み溶接部 短期耐力：{:.2f} [kN]".format(warikomi_weld_strength))

        # GPL有効断面
        t = m[T_GPL]
        d_e = m[D_GPL] - m[N_BOLT] * bolt.htb_spec(m[SIZE_BOLT], 'HOLE_DIA')
        print("　GPL t={}, d={}".format(t, m[D_GPL]))
        print("  HTB {}-{}".format(m[N_BOLT], m[SIZE_BOLT]))
        gpl_strength = t * d_e * 235 / 1000.
        print("GPL有効断面 短期耐力：{:.2f} [kN]".format(gpl_strength))

        # ボルト耐力
        print("ボルト耐力（２面せん断）：{:.2f} [kN]".format(m[N_BOLT] * 2 * bolt.htb_spec(m[SIZE_BOLT], 'QAS')))

        # 柱側溶接部
        col_t = 4.5
        t = min(m[T_GPL], col_t)
        d = m[D_GPL]
        gpl_column_end_weld_strength = weld.fillet_weld_strength(d, weld.fillet_weld_size(t), n=2) * 1.5 / 1000.
        print("　GPL柱端せい：{} [mm]".format(d))
        print("　柱板厚：{} [mm]".format(col_t))
        print("柱側 溶接部 短期耐力：{:.2f} [kN]".format(gpl_column_end_weld_strength))


if __name__ == '__main__':
    main_truss_lower_chord()
    pass
