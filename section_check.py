from xs_section import xs_section_property, xs_section_name
import allowable_stress as alws


def allowable_tensile_force(sec, F, term):
    """
    部材の許容引張耐力を返す。全断面積に対して。
    :param sec: 断面名
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）"LONG" / "SHORT"
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


def allowable_compressive_force(sec, F=235., term='LONG', lkx=0., lky=0.):
    """
    部材の許容圧縮耐力を返す。
    :param sec: 断面名
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）"LONG" / "SHORT"
    :param lkx: 座屈長さ X方向 [cm]
    :param lky: 座屈長さ Y方向 [cm]
    :return: cNa 許容圧縮耐力[kN]
    """
    area = xs_section_property(sec, 'An')
    sec_full_name = xs_section_name(sec)
    # TODO 断面により、iの名称が異なる。ix,iy,iu,iv,,,
    #  各方向別の座屈長さ指定などの対応
    iy = 0.01
    if sec_full_name[0] in ['H']:
        iy = xs_section_property(sec, 'iy')
    if sec_full_name[0] in ['P']:
        iy = xs_section_property(sec, 'ix')
    if sec_full_name[0] in ['L']:
        iy = xs_section_property(sec, 'iv')

    term_factor = 1.0
    if term == 'LONG':
        term_factor = 1.0
    elif term == 'SHORT':
        term_factor = 1.5

    fc = alws.steel_fc_bsl(F, lky / iy)
    return term_factor * area * fc / 10.


def allowable_bending_moment(sec, M1=0, M2=0, M3=1, direc='X', lb=0., F=235., term='LONG'):
    """
    部材の許容曲げ耐力を返す。
    :param sec: 断面名
    :param M1:座屈補剛区間端部の大きい方のM
    :param M2:座屈補剛区間端部の小さい方のM
    :param M3:座屈補剛区間内の最大のM
    :param direc: 断面の軸指定 強軸/弱軸まわり　"X" / "Y"
    :param lb: 圧縮フランジの支点間距離 (mm)
    :param F: F値 [N/mm2]
    :param term:荷重種別（短期・長期）"LONG" / "SHORT"
    :return: Ma 許容曲げモーメント [kN*m]
    """
    # TODO:断面による処理の違いを実装
    # H形鋼
    from xs_section import make_all_section_db
    db = make_all_section_db()
    z, fb = 0, 0
    if direc == 'X':
        z = xs_section_property(sec, 'Zx')
        fb = alws.steel_fb_aij2005(sec, db, lb=lb, M1=M1, M2=M2, M3=M3, F=F)

    if direc == 'Y':
        z = xs_section_property(sec, 'Zy')
        fb = alws.steel_ft()

    term_factor = 1.0 if term == 'LONG' else 1.5

    return term_factor * z * (fb / 10.) / 100.

