from xs_section import xs_section_property, xs_section_name
import allowable_stress as alws


def allowable_tensile_force(sec, F, term):
    """
    部材の許容引張耐力を返す
    :param sec: 断面名
    :param F: F値 [N/mm2]
    :param term: 荷重種別（短期・長期）"LONG" / "SHORT"
    :return: [kN]
    """
    area = xs_section_property(sec, 'An')
    term_factor = 1.0
    if term == 'LONG':
        term_factor = 1.0
    elif term == 'SHORT':
        term_factor = 1.5
    ft = alws.steel_ft(F)
    return term_factor * area * ft / 10.


def allowable_compressive_force(sec, F, term, lk):
    area = xs_section_property(sec, 'An')
    sec_full_name = xs_section_name(sec)
    # TODO 断面により、iの名称が異なる。ix,iy,iu,iv,,,
    if sec_full_name[0] in ['H']:
        iy = xs_section_property(sec, 'iy')
    if sec_full_name[0] in ['P']:
        iy = xs_section_property(sec, 'ix')

    term_factor = 1.0
    if term == 'LONG':
        term_factor = 1.0
    elif term == 'SHORT':
        term_factor = 1.5
    # print(iy)

    fc = alws.steel_fc_bsl(F, lk / iy)
    # print(fc)
    return term_factor * area * fc / 10.
