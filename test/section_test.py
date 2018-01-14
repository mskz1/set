# -*- coding: utf-8 -*-
__author__ = 'mskz'

import unittest

from cross_section.section import *

try:
    from cross_section import ureg, Q_
except:
    from __init__ import ureg, Q_


class MyTestCase(unittest.TestCase):
    # def test_conversion_factor(self):
    #     self.assertEqual(conversion_factor(uMM, uMM), 1.0)
    #     self.assertEqual(conversion_factor(uCM, uMM), 10.0)
    #     self.assertEqual(conversion_factor(uM, uMM), 1000.0)
    #     self.assertEqual(conversion_factor(uMM, uM), 0.001)
    #     self.assertEqual(conversion_factor(uCM, uM), 0.01)
    #     self.assertEqual(conversion_factor(uCM, uCM), 1.0)

        # self.assertEqual(True, False)

    # def test_section_db(self):
    #     db = SectionDB()
    #     db.x_load()

    def test_section(self):
        # PROPERTY, H,  B, t1, t2, r , An

        h_200_prop_data = dict(H="200 *mm", B="100*mm", t1="5.5*mm", t2="8*mm",
                     r="8*mm", An="26.67*cm**2", Zx="181*cm**3")
        self.assertEqual(h_200_prop_data['H'],"200 *mm")

        h_200_prop = {}
        for k in h_200_prop_data.keys():
            h_200_prop[k] = Q_(h_200_prop_data[k])
        self.assertEqual(h_200_prop['H'], Q_(200, "mm"))
        self.assertEqual(h_200_prop['B'], Q_(100, "mm"))
        self.assertEqual(h_200_prop['An'], Q_(26.67, "cm**2"))

        name_form = ['H-', 'H', 'B', 't1', 't2']
        h1 = Section("HS-", "H形鋼細幅", h_200_prop, name_form)
        h1.set_name()
        self.assertEqual(h1.name, "H-200x100x5.5x8")
        self.assertEqual(h1.get_prop("An"),Q_(26.67, 'cm**2'))



    def test_section_property_2(self):
        sp_H = SectionProperty("H", Q_(100, "mm"))
        self.assertEqual(sp_H.value, Q_(10, "cm"))
        self.assertEqual(sp_H.value.magnitude, 100)
        # self.assertEqual(sp_H.value.units, "mm")
        sp_H.value = Q_(248, "mm")
        self.assertEqual(sp_H.value, Q_(248, "mm"))


    # def test_section_property(self):
    #     sp_H = SectionProperty("H",100.0)
    #     #print(sp.value)
    #     #print(sp.value(unit=uCM))
    #     print(sp_H)
    #     print(sp_H.name,":",sp_H.get_value(uCM),"cm",sp_H.dimension)
    #     print(sp_H.name,":",sp_H.get_value(uM),"m",sp_H.dimension)
    #
    #     sp_A = SectionProperty("An",20.0,unit=uCM,dim=2)
    #     print(sp_A)
    #     print(sp_A.name,":",sp_A.get_value(uMM),"mm",sp_A.dimension)
    #
    #     sp_Z = SectionProperty("Zx",400.0,unit=uCM,dim=3)
    #     print(sp_Z)
    #     print(sp_Z.name,":",sp_Z.get_value(uMM),"mm",sp_Z.dimension)
    #
    #     sp_I = SectionProperty("Ix",1800.0,unit=uCM,dim=4)
    #     print(sp_I)
    #     print(sp_I.name,":",sp_I.get_value(uMM),"mm",sp_I.dimension)



def test1():
#     sp = SectionProperty("Zx", value=10., unit=uCM, dim=3)
#     print(sp.value)
    sp_H = SectionProperty("H", Q_(100, "mm"))


if __name__ == '__main__':
    #unittest.main()
    # import nose
    # nose.main()
    test1()

