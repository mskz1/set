from xs_section import xs_section_property


def tensile_allowable_force(sec, F, term):
    area = xs_section_property(sec, 'An')
    f = 1.0
    if term == 'LONG':
        f = 1.0
    elif term == 'SHORT':
        f = 1.5
    print('Tas=', area * F / 10 * f, '[kN]')
    pass
