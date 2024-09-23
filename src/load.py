from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar


class Type(Enum):
    # 荷重タイプ
    DL = 'DL'  # 固定荷重
    SL = 'SL'  # 積雪荷重
    WL = 'WL'  # 風荷重
    LL = 'LL'  # 積載荷重


class LoadCase(Enum):
    G = 'G'  #
    S = 'S'
    W = 'W'
    K = 'K'
    P = 'P'


class LoadTerm(Enum):
    LONG = 'LONG'
    SHORT = 'SHORT'


@dataclass
class UnitLoad:
    """
    単位面荷重データ（N/m2）
    """
    # id: int = 0
    type: Type = Type.DL  # 荷重タイプ
    load_case: LoadCase = LoadCase.G  # 所属する荷重ケース

    value: float = 0.  # 荷重値（N/m2）
    description: str = ""  # 説明メモ

    def get_as_point_load(self, a: float, b: float) -> float:
        """
        集中荷重値P(N)を返す。
        :param a: 負担幅１（m）
        :param b: 負担幅２（m）
        :return:
        """
        return self.value * a * b

    def get_as_distributed_load(self, a: float) -> float:
        """
        分布荷重値ｗ（N/m）を返す。
        :param a: 負担幅（m）
        :return:
        """
        return self.value * a


@dataclass
class xxLoadCase:
    """荷重ケース"""
    name: str = ""
    load: UnitLoad = UnitLoad()


@dataclass
class xxLoadCombination:
    """面荷重データのグループ/荷重ケースの組合せ？？"""
    # 荷重ケースとその組合せ係数、荷重ケースの追加・削除　をするには。。。
    # 荷重に固有のidを割り当て、それで設定する？
    label: str = ''
    current_load_id: ClassVar = 0
    id_load: dict[int, UnitLoad] = field(default_factory=dict)

    def add(self, label: str, ld_factor: dict[UnitLoad, float]):
        pass

    def add_load(self, type: Type, value: float, description: str):
        # 消す？
        self.current_load_id += 1
        return self.current_load_id

    def delete_load(self, load_id: int):
        # 消す？
        pass

    def add_combo(self, label, *factors):
        # 消す？
        print(label, factors)
        pass


@dataclass
class LoadCombination:
    """
    荷重組合せ　名称、荷重ケースとその係数を保持
    """
    label: str = ''  # 名称
    load_cases: list[LoadCase] = field(default_factory=list)  # 含まれる荷重ケースのリスト
    factors: list[float] = field(default_factory=list)  # 上記各荷重ケースの係数
    term: LoadTerm = LoadTerm.LONG  # 荷重種別（長期/短期）

    def get_factor(self, load_case: LoadCase):
        # 含まない荷重ケースを指定した場合は ValueError
        return self.factors[self.load_cases.index(load_case)]


@dataclass
class LoadRegistry:
    """
    荷重データ（）を登録・管理するオブジェクト

    単位荷重は荷重id（1～）で管理。削除した場合、そのidは以後欠番となる。
    """
    # unit_loads = {}
    unit_loads: dict[int, UnitLoad] = field(default_factory=dict)
    current_load_id: ClassVar = 0
    # load_combo = {}
    load_combo: dict[str, LoadCombination] = field(default_factory=dict)

    @property
    def loads(self):
        return self.unit_loads

    def show_loads(self):
        result = [' registered unit loads '.center(80, '-')]
        result += [f"{'id':>5}{'type':^10}{'value(N/m2)':>12}{'LoadCase':^10}{'  description'}"]
        # result += [f'id={k}, type={ld.type.value}, value={ld.value}(N/m2), description={ld.description}' for k, ld in
        #           self.unit_loads.items()]
        result += [f'{k:>5}{ld.type.value:^10}{ld.value:12.2f}{ld.load_case.value:^10}  {ld.description}' for k, ld in
                   self.unit_loads.items()]
        result += ['-' * 80]
        return '\n'.join(result)

    def add_load(self, ld_type: Type, value: float, load_case: LoadCase, description: str) -> int:
        self.current_load_id += 1
        self.unit_loads[self.current_load_id] = UnitLoad(type=ld_type, value=value, description=description,
                                                         load_case=load_case)
        return self.current_load_id

    def remove_load(self, load_id: int):
        del self.unit_loads[load_id]

    def modify_load(self, load_id: int, **kwd):
        for key, value in kwd.items():
            setattr(self.unit_loads[load_id], key, value)

    def add_load_combo(self, label: str, load_cases: list[LoadCase], factors: list[float],
                       term: LoadTerm = LoadTerm.LONG):
        self.load_combo[label] = LoadCombination(label=label, load_cases=load_cases, factors=factors, term=term)

    def remove_load_combo(self, combo_label: str):
        del self.load_combo[combo_label]

    def show_load_combo(self):
        result = [' registered load combinations '.center(80, '-')]
        result += [f"{'label':>15}{'load_cases':>25}{'factors':>20}{'term':>20}"]
        result += [f"{k:>15}{str([lc.value for lc in v.load_cases]):>25}{str(v.factors):>20}{str(v.term.value):>20}" for
                   k, v in self.load_combo.items()]
        result += ['-' * 80]
        return '\n'.join(result)

    def get_as_point_load(self, label: str, a: float, b: float) -> float:
        """
        集中荷重値P(N)を返す

        :param label: 荷重組合せの名称
        :param a: 負担幅１（ｍ）
        :param b: 負担幅２（ｍ）
        :return:
        """
        load_combo = self.load_combo[label]
        result = 0.0
        for ld in self.unit_loads.values():
            if ld.load_case in load_combo.load_cases:
                # result += ld.value * load_combo.get_factor(ld.load_case) * a * b
                result += ld.get_as_point_load(a, b) * load_combo.get_factor(ld.load_case)
        return result

    def get_as_distributed_load(self, label: str, a: float) -> float:
        """
        分布荷重値ｗ（N/m）を返す。

        :param label: 荷重組合せの名称
        :param a: 負担幅（m）
        :return:
        """
        load_combo = self.load_combo[label]
        result = 0.0
        for ld in self.unit_loads.values():
            if ld.load_case in load_combo.load_cases:
                result += ld.get_as_distributed_load(a) * load_combo.get_factor(ld.load_case)
        return result

    def get_load_combo_names(self, term: LoadTerm) -> list[str]:
        """長期/短期の指定をして、該当する荷重組合せの名称すべてをリストで返す"""
        result = []
        for label, lcombo in self.load_combo.items():
            if lcombo.term == term:
                result.append(label)
        return result
