from enum import Enum
from dataclasses import dataclass

# 2024-0928 プロトタイプ






@dataclass
class Profile:
    name: str = 'H-200x100x5.5x8'
    An: float = 26.67
    Ix: float = 1810.
    Iy: float = 134.
    Zx: float = 181.
    Zy: float = 26.7




HS_SEC_DATA = """SERIES,HS-,H形鋼細幅,H-HxBxt1xt2
FORMAT,H-,H,B,t1,t2
PROPERTY, H,  B, t1, t2,  r,    An,     W,    Ix,    Iy, ix, iy,    Zx,    Zy, ib,   eta,   Zpx, Zpy 
UNIT,    mm, mm, mm, mm, mm, cm**2, kgf/m, cm**4, cm**4, cm, cm, cm**3, cm**3, cm,   -, cm**3, cm**3
HS-,200,100,5.5,8,8,    26.67      ,20.9,   1810,   134,  8.23,2.24,181,26.7,2.63,6.57,205,41.6
HS-,600,200,11,17,13,131.7,103,75600,2270,24,4.16,2520,227,5.09,8.98,2900,358"""