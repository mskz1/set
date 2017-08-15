# -*- coding: utf-8 -*-
__author__ = 'mskz'

# Cantilever with End Load - T301
# Cantilever with Intermediate Load - T302
# Cantilever with Uniform Load - T303
# Cantilever with Moment Load - T304
# Simple Supports with Center Load - T305
# Simple Supports with Intermediate Load - T306
# Simple Supports with Uniform Load - T307
# Simple Supports with Moment Load - T308
# Simple Supports with Twin Loads - T309
# Simple Supports with Overhanging Load - T310
# Propped Cantilever with Center Load - T311
# Propped Cantilever with Intermediate Load - T312
# Propped Cantilever with Uniform Load - T313
# Fixed Beam with Center Load - T314
# Fixed Beam with Intermediate Load - T315
# Fixed Beam with Uniform Load - T316

# -----------------------------------------------
# Simply Supported Beam with a Centered Load
# 単純梁＿中央集中荷重
#
#def M_SSB_CL(L=0.0,P=0.0):
#    return P * L / 4.0
#
#def D_SSB_CL(L=0.0, P=0.0, E=20500.0, I=0.0):
#    return  P * L**3 / (48.0 * E * I) *10.0
#

#----------------------------------------------


class AbstractBeamFormula(object):
    # 抽象クラス
    def __init__(self):
        pass

    def calcM(self):
        pass

    def printResult(self):
        propKeys = self.__dict__.keys()

        for key in propKeys:
            print(key,":",self.__dict__[key])

    def getR1(self):
        # 始点側反力を返す
        pass

    def getR2(self):
        # 終点側反力を返す
        pass

    def getM_at_n(self,n):
        # モーメント値を返す（部材をn分割する？）
        pass

    def getM_at(self,a):
        # モーメント値を返す（指定位置）
        pass

    def getD_at_n(self,n,E,I):
        # たわみ値を返す（部材をn分割する？）
        pass

    def getD_at(self,n,E,I):
        # たわみ値を返す（部材をn分割する？）
        pass

    def getMmax(self):
        # 最大モーメント値を返す
        pass

    def getDmax(self,E,I):
        # 最大たわみ値を返す
        pass

    def getMcenter(self):
        # スパン中央位置のモーメント値を返す
        pass

    def getDcenter(self,E,I):
        # スパン中央位置のたわみ値を返す
        pass

#----------------------------
