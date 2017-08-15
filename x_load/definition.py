# -*- coding: utf-8 -*-
__author__ = 'mskz'

#
#LONG_TERM = "LONG"

#load_type
DISTRIBUTED_LOAD = 1
POINT_LOAD = 2

#unit_definition
KN = "kN"
N = "N"
kN_m2 = "kN/m2"
kN_m = "kN/m"


class Load(object):
    def __init__(self, label, value, unit, load_type=None):
        self.label = label
        self.value = value
        self.unit = unit
        self.load_type = load_type

    def __repr__(self):
        return "".join(map(str, ["名称:", self.label, ", 値:", self.value,
                                 ", 単位:", self.unit, ", タイプ:", self.load_type]))
        # return self.label+str(self.value)+self.unit+str(self.load_type)

    def print_all_attributes(self):
        print("-"*30)
        for k, d in self.__dict__.items():
            print(k, "=", d)
        print("-"*30)


if __name__ == '__main__':
    print("-----START-----")
    dl = Load("屋根DL", 300., "N/m2")
    print(dl)
    # print(dl.__dir__())
    # print(dl.__dict__)
    dl.print_all_attributes()
    print("-----END-----")
    print()

