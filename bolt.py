# -*- coding: utf-8 -*-

# class Bolt:
#     def __init__(self):
#         self._name = ""
#         self._hole_dia = 0
#         self._Qa_long = 0.
#         self._Qa_short = 0.
#         self._Na_long = 0.
#         self._Na_short = 0.


# class K:
#     M16 = 'M16'
#     M20 = 'M20'
#     M22 = 'M22'
#     M24 = 'M24'
#     M27 = 'M27'
#     M30 = 'M30'
#     F10T = 'F10T'
#     F8T = 'F8T'
#     Qal = 'Qal'  # 長期許容せん断力(kN) １面せん断
#     Qas = 'Qas'  # 短期許容せん断力(kN) １面せん断
#     Dia = 'Dia'  # ボルト軸径(mm)
#     Hole_dia = 'Hole_dia'  # ボルト孔径(mm)


M16 = 'M16'
M20 = 'M20'
M22 = 'M22'
M24 = 'M24'
M27 = 'M27'
M30 = 'M30'

F10T = 'F10T'
F8T = 'F8T'

Qal = 'Qal'  # 長期許容せん断力(kN) １面せん断
Qas = 'Qas'  # 短期許容せん断力(kN) １面せん断

Tal = 'Tal'  # 長期許容引張力(kN)
Tas = 'Tas'  # 短期期許容引張力(kN)

Dia = 'Dia'  # ボルト軸径(mm)
Hole_dia = 'Hole_dia'  # ボルト孔径(mm)

# 寸法はmm, 力はkN
# HTB_M16 = dict(name='M16', dia=16, hole_dia=18, Qal=30.2, Qas=45.3)
HTB_M20 = dict(name='M20', dia=20, hole_dia=22, Qal=47.1, Qas=70.6)

# HTB_M16 = dict(name='M16', dia=16, hole_dia=18, Qal=30.2, Qas=45.3)

# HTB_M16 = {K.Dia: 16, K.Qal: 30.2, K.Qas: 45.3}
HTB_M16 = {Dia: 16, Qal: 30.2, Qas: 45.3}

HTB_SPC = {}
HTB_SPC['M16'] = HTB_M16
HTB_SPC['M20'] = HTB_M20

HTB_SIZE = ['M16', 'M20', 'M22', 'M24', 'M27', 'M30']
HTB_STRENGTH = ['F8T', 'F10T']


# def htb_spec(size, type, term=None, F_type=K.F10T):
#     if F_type == K.F10T:
#         if size == K.M16:
#             if type == K.Qal:
#                 return 30.2
#             elif type == K.Qas:
#                 return 45.3
#         elif size == K.M20:
#             if type == K.Qal:
#                 return 30.2
#             elif type == K.Qas:
#                 return 45.3
#         elif size == K.M22:
#             pass
#         elif size == K.M24:
#             pass
#         elif size == K.M27:
#             pass
#
#     elif F_type == K.F8T:
#         pass


def htb_spec(size, type, term=None, F_type=F10T):
    if F_type == F10T:
        if size == M16:
            if type == Qal:
                return 30.2
            elif type == Qas:
                return 45.3
        elif size == M20:
            if type == Qal:
                return 30.2
            elif type == Qas:
                return 45.3
        elif size == M22:
            pass
        elif size == M24:
            pass
        elif size == M27:
            pass

    elif F_type == F8T:
        pass

