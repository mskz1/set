# -*- coding: utf-8 -*-
__author__ = 'mskz'


from x_material import steel
import unittest
import math

"""
日本建築学会　鋼構造設計規準
　計算式モジュール のテストモジュール

"""


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_ft(self):
        #self.assertEqual(ft(F[steel.SS400]), 235.0/1.5)
        str = "%.4f" % steel.ft(steel.F[steel.SS400])
        self.assertEqual(str, "156.6667")
        str = "%.4f" % steel.ft(steel.F[steel.SM490])
        self.assertEqual(str, "216.6667")

    def test_fs(self):
        str = "%.4f" % steel.fs(steel.F[steel.SS400])
        self.assertEqual(str, "90.4515")
        str = "%.4f" % steel.fs(steel.F[steel.SM490])
        self.assertEqual(str, "125.0926")

    def test_lamuda(self):
        str = "%.3f" % steel.lamuda(steel.F[steel.SS400])
        self.assertEqual(str, "119.789")
        str = "%.3f" % steel.lamuda(steel.F[steel.SM490])
        self.assertEqual(str, "101.861")

    def test_calcC(self):
        self.assertEqual(steel.calcC(1.0,1.0), 1.0)
        self.assertEqual(steel.calcC(1.0,0.5)
                         , (1.75 - 1.05*0.5 + 0.3*(0.5**2)))
        self.assertEqual(steel.calcC(1.0,0.5), 1.3)
        self.assertEqual(steel.calcC(1.0,0.0), 1.75)
        self.assertEqual(steel.calcC(1.0,-1.0), 2.3)

    def test_fb(self):
        txt = "%.3f" % steel.fb(F_value=steel.F[steel.SS400],lb=3000.0,i=26.3,C=1.0
                                  ,h=200.0,Af=100*8.0)
        self.assertEqual(txt, "118.667")
        txt = "%.3f" % steel.fb(F_value=steel.F[steel.SS400],lb=1000.0,i=26.3,C=1.0
                                  ,h=200.0,Af=100*8.0)
        self.assertEqual(txt, "156.667")
        txt = "%.3f" % steel.fb(F_value=steel.F[steel.SS400],lb=5000.0,i=26.3,C=1.0
                                  ,h=200.0,Af=100*8.0)
        self.assertEqual(txt, "71.200")

    def test_fc(self):
        txt = "%.4f" % steel.fc(F_value=steel.F[steel.SS400],lk=3000.0,i=26.3)
        self.assertEqual(txt, "71.1632")

        txt = "%.4f" % steel.fc(F_value=steel.F[steel.SS400],lk=0.0,i=26.3)
        self.assertEqual(txt, "156.6667")

        txt = "%.4f" % steel.fc(F_value=steel.F[steel.SS400],lk=50.0,i=1.0)
        self.assertEqual(txt, "135.2741")

        txt = "%.4f" % steel.fc(F_value=steel.F[steel.SS400],lk=200.0,i=1.0)
        self.assertEqual(txt, "23.3519")


#--------------------------------------------
if __name__ == '__main__':
    #unittest.main()

    #print steel.ft(steel.F[steel.SS400])
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFunctions))
    unittest.TextTestRunner(verbosity=2).run(suite)

