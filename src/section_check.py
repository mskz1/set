# from src.xs_section import xs_section_property, xs_section_name, get_Zu_Zv_of_angle
from xs_section import xs_section_property, xs_section_name, get_Zu_Zv_of_angle
# import src.allowable_stress as alws
import allowable_stress as alws


def allowable_tensile_force(sec: str, F: float = 235., term: str = 'LONG') -> float:
    """
    部材の許容引張耐力を返す。全断面積に対して。

    :param sec: 断面名
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）str "LONG" / "SHORT"
    :return: tNa 許容引張耐力[kN]
    """
    # TODO:有効断面積の対応？　
    area = xs_section_property(sec, 'An')
    term_factor = 1.0
    if term == 'LONG':
        term_factor = 1.0
    elif term == 'SHORT':
        term_factor = 1.5
    ft = alws.steel_ft(F)
    return term_factor * area * ft / 10.


def allowable_compressive_force(sec: str, F: float = 235., term: str = 'LONG', lkx: float = 0.,
                                lky: float = 0.) -> float:
    """
    部材の許容圧縮耐力を返す。

    :param sec: 断面名
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）str "LONG" / "SHORT"
    :param lkx: 座屈長さ X方向 [mm]  2024.6.16 cm -> mm
    :param lky: 座屈長さ Y方向 [mm]
    :return: cNa 許容圧縮耐力[kN]
    """
    area = xs_section_property(sec, 'An')
    sec_full_name = xs_section_name(sec)
    # TODO:有効断面？（幅厚比、断面欠損）
    # 断面により、iの名称が異なる。ix,iy,iu,iv,,,
    ix = 0.01
    iy = 0.01
    lambda_ = 0.0

    if sec_full_name[0] in ['P']:  # 鋼管
        ix = xs_section_property(sec, 'ix')
        iy = ix
        lambda_ = max(0.1 * lkx / ix, 0.1 * lky / iy)
    elif sec_full_name[0] in ['L']:  # 山形鋼
        # u,v 方向 lkxはU軸、lkyはV軸まわりで計算
        ix = xs_section_property(sec, 'iu')
        iy = xs_section_property(sec, 'iv')
        lambda_ = max(0.1 * lkx / ix, 0.1 * lky / iy)
    else:  # H, KP, [, C　その他断面
        ix = xs_section_property(sec, 'ix')
        iy = xs_section_property(sec, 'iy')
        lambda_ = max(0.1 * lkx / ix, 0.1 * lky / iy)

    term_factor = 1.0
    if term == 'LONG':
        term_factor = 1.0
    elif term == 'SHORT':
        term_factor = 1.5

    fc = alws.steel_fc_bsl(F, lambda_)
    return term_factor * area * fc / 10.


def allowable_bending_moment(sec: str, M1: float = 0, M2: float = 0, M3: float = 1, direc: str = 'X', lb: float = 0.,
                             F: float = 235., term: str = 'LONG', fb_edition: str = '2005') -> float:
    """
    部材の許容曲げ耐力を返す。

    :param sec: 断面名
    :param M1: 座屈補剛区間端部の大きい方のM
    :param M2: 座屈補剛区間端部の小さい方のM
    :param M3: 座屈補剛区間内の最大のM
    :param direc: 断面の軸指定 強軸/弱軸まわり　"X" / "Y"
    :param lb: 圧縮フランジの支点間距離 (mm)
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）str "LONG" / "SHORT"
    :return: Ma 許容曲げモーメント [kN*m]
    """

    # TODO:断面による処理の違いを実装
    # from src.xs_section import make_all_section_db
    from xs_section import make_all_section_db
    db = make_all_section_db()
    section_full_name = xs_section_name(sec)

    # H形鋼
    if section_full_name.startswith('H-'):
        z, fb = 0, 0
        if direc == 'X':
            z = xs_section_property(sec, 'Zx', db)
            if fb_edition == '2005':
                fb = alws.steel_fb_aij2005(section_full_name, db, lb=lb, M1=M1, M2=M2, M3=M3, F=F)
            else:
                # fb = alws.steel_fb_aij(F=F,lb=lb,i=)
                fb = alws.steel_fb_aij2002(section_full_name, db, lb=lb, M1=M1, M2=M2, M3=M3, F=F)
        if direc == 'Y':
            z = xs_section_property(sec, 'Zy', db)
            # 弱軸曲げ 横座屈なし fb=ft
            fb = alws.steel_ft()

        term_factor = 1.0 if term == 'LONG' else 1.5

        return term_factor * z * (fb / 10.) / 100.

    # 角形鋼菅
    if section_full_name.startswith('□P-'):
        z, fb = 0, 0
        if direc == 'X':
            z = xs_section_property(sec, 'Zx', db)
        if direc == 'Y':
            z = xs_section_property(sec, 'Zy', db)
        # 横座屈なし fb=ft
        fb = alws.steel_ft()
        term_factor = 1.0 if term == 'LONG' else 1.5

        return term_factor * z * (fb / 10.) / 100.

    # 鋼菅
    if section_full_name.startswith('P-'):
        z, fb = 0, 0
        z = xs_section_property(sec, 'Zx', db)
        # 横座屈なし fb=ft
        fb = alws.steel_ft()
        term_factor = 1.0 if term == 'LONG' else 1.5

        return term_factor * z * (fb / 10.) / 100.

    # 溝形鋼
    if section_full_name.startswith('[-'):
        z, fb = 0, 0

        if direc == 'X':
            z = xs_section_property(sec, 'Zx', db)
            fb = alws.steel_fb_aij2005(section_full_name, db, lb=lb, M1=M1, M2=M2, M3=M3, F=F)

        if direc == 'Y':
            z = xs_section_property(sec, 'Zy', db)
            # 横座屈なし fb=ft
            fb = alws.steel_ft()
        term_factor = 1.0 if term == 'LONG' else 1.5

        return term_factor * z * (fb / 10.) / 100.

    # TODO:C形鋼  fbの計算を確認 WIP fb=ftとする場合も用意するか？
    # C形鋼
    if section_full_name.startswith('C-'):
        z, fb = 0, 0
        if direc == 'X':
            z = xs_section_property(sec, 'Zx', db)
            fb = alws.steel_fb_aij2005(section_full_name, db, lb=lb, M1=M1, M2=M2, M3=M3, F=F)
        if direc == 'Y':
            z = xs_section_property(sec, 'Zy', db)
            # 横座屈なし fb=ft
            fb = alws.steel_ft()
        term_factor = 1.0 if term == 'LONG' else 1.5

        return term_factor * z * (fb / 10.) / 100.

    # 山形鋼
    if section_full_name.startswith('L-'):
        # TODO 主軸が傾いているため、u,v方向への分解が必要　u,v方向のそれぞれのMaを返す？
        z, fb = 0, 0
        if direc == 'X':
            z = xs_section_property(sec, 'Zx', db)
        if direc == 'Y':
            z = xs_section_property(sec, 'Zy', db)
        if direc == 'U':
            z, _ = get_Zu_Zv_of_angle(sec, db)
        if direc == 'V':
            _, z = get_Zu_Zv_of_angle(sec, db)

        # 横座屈なし fb=ft
        fb = alws.steel_ft()
        term_factor = 1.0 if term == 'LONG' else 1.5

        return term_factor * z * (fb / 10.) / 100.


def section_check(sec: str, F: float, term: str, N: float, Mx: float, My: float = 0., Qx: float = 0., Qy: float = 0.,
                  lkx: float = 0., lky: float = 0., lb: float = 0.):
    """
    応力 N,M,Q(kN, kN*m, kN)をあたえ、部材の検定比を返す。 N<0で圧縮 N>0で引張
    :param sec: 断面名
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）str "LONG" / "SHORT"
    :param N: 軸力 [kN] 圧縮は負値
    :param Mx: x軸まわりモーメント [kN*m]
    :param My: y軸まわりモーメント [kN*m]
    :param Qx: せん断力（現状未対応）[kN]
    :param Qy: せん断力（現状未対応）[kN]
    :param lkx: x軸方向座屈長さ [mm]
    :param lky: y軸方向座屈長さ [mm]
    :param lb: 横座屈長さ [mm]
    :return:
    """
    # WIP : 応力NMQをあたえ、部材の検定比を返す。
    # todo : せん断に対する検討は別にする？
    if N < 0:
        N_f = -N / allowable_compressive_force(sec, F, term, lkx, lky)
    else:
        N_f = N / allowable_tensile_force(sec, F, term)

    # 2025-0126 Mx=0 の時、ゼロ割発生回避
    if Mx != 0:
        Mx_f = Mx / allowable_bending_moment(sec, M3=Mx, direc='X', lb=lb, F=F, term=term)
    else:
        Mx_f = 0.0
    My_f = My / allowable_bending_moment(sec, M3=My, direc='Y', lb=lb, F=F, term=term)
    return N_f + Mx_f + My_f
