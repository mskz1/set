from section.section_property import *


def test_rectangular_section():
    s = RectangularSection(w=50, h=100)
    assert s.An == 50 * 100.
    assert s.Zx == (1. / 6.) * 50 * 100 ** 2
    assert s.Ix == (1. / 12.) * 50 * 100 ** 3
