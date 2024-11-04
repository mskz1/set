import math
from enum import Enum
from dataclasses import dataclass, field

from xs_section import xs_section_property, short_full_name, make_all_section_db
from section_check import allowable_bending_moment
from allowable_stress import steel_fb_aij2005, steel_fb_bsl, calc_C


class Material(Enum):
    S400N = '400N'
    S490N = '490N'


class Condition(Enum):
    Mp_Mp = 'Mp_Mp'
    Mp_M1 = 'Mp_M1'


@dataclass
class Yokohogou:
    """鉄骨梁　保有耐力横補剛の検討"""
    sec: str = "H40"
    L: float = 5000.0  # (mm)
    material: Material = Material.S400N
    end_force_condition: Condition = Condition.Mp_Mp
    M_Left: float = 0.0  # 検討用梁端M 左端(N*mm)
    M_Right: float = 0.0  # 検討用梁端M 右端(N*mm)
    # restraint_location: list = field(default_factory=list)  # 補剛材位置を格納
    restraint_spans: list = field(default_factory=list)  # 横補剛の配置間隔

    db = make_all_section_db()

    def get_number_of_equivalent_placement_lateral_restraint(self) -> int:
        """ 均等配置による必要横補剛個所数 n を返す"""
        iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        lambda_y = self.L / iy
        if self.material == Material.S400N:
            n = (lambda_y - 170) / 20
        elif self.material == Material.S490N:
            n = (lambda_y - 130) / 20
        else:
            raise ValueError
        return math.ceil(n)

    def get_lb(self, step=0) -> float:
        """
        梁端部に近い部分に横補剛を設ける場合 Myを超える領域での最長補剛間隔 lb (mm)を返す
        """
        B = xs_section_property(self.sec, 'B', self.db)
        tf = xs_section_property(self.sec, 't2', self.db)
        Af = B * tf
        H = xs_section_property(self.sec, 'H', self.db)
        iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        if self.material == Material.S400N:
            lb = min(250 * Af / H, 65 * iy)
        elif self.material == Material.S490N:
            lb = min(200 * Af / H, 50 * iy)
        else:
            raise ValueError
        if step:
            return self.x_ceiling(lb, step)
        else:
            return lb

    @property
    def alpha(self) -> float:
        """材質の強度クラスに応じた安全率 α を返す。"""
        if self.material == Material.S400N:
            return 1.2
        elif self.material == Material.S490N:
            return 1.1
        else:
            raise ValueError

    @property
    def Mp(self) -> float:
        """全塑性モーメント Mp (N*mm)を返す"""
        Zpx = xs_section_property(self.sec, 'Zpx', self.db) * 1e3  # (mm3)
        if self.material == Material.S400N:
            return Zpx * 235.0  # (N*mm)
        elif self.material == Material.S490N:
            return Zpx * 325.0  # (N*mm)
        else:
            raise ValueError

    @property
    def My(self) -> float:
        """降伏モーメント My (N*mm)を返す"""
        Zx = xs_section_property(self.sec, 'Zx', self.db) * 1e3  # (mm3)
        if self.material == Material.S400N:
            return Zx * 235.0  # (N*mm)
        elif self.material == Material.S490N:
            return Zx * 325.0  # (N*mm)
        else:
            raise ValueError

    def Mas(self, Lb=0.0, M1=0., M2=0.) -> float:
        """短期許容曲げモーメント Mas (N*mm) を返す"""
        Zx = xs_section_property(self.sec, 'Zx', self.db) * 1e3  # (mm3)
        F = 235 if self.material == Material.S400N else 325
        fb = steel_fb_aij2005(shape_name=short_full_name[self.sec], db=self.db, lb=Lb, M1=M1, M2=M2, F=235)

        # B = xs_section_property(self.sec, 'B', self.db)
        # tf = xs_section_property(self.sec, 't2', self.db)
        # Af = B * tf
        # H = xs_section_property(self.sec, 'H', self.db)
        # iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        # ib = xs_section_property(self.sec, 'ib', self.db) * 10  # (mm)
        # c = calc_C(M1, M2)
        # fb = steel_fb_bsl(F=F, lb=Lb, i=ib, C=c, h=H, Af=Af)
        return 1.5 * fb * Zx

    def set_Me(self):
        """検討用　端部モーメントの設定を行う"""
        if self.end_force_condition == Condition.Mp_Mp:
            self.M_Left = self.alpha * self.Mp
            self.M_Right = self.alpha * self.Mp
        else:
            raise NotImplementedError

    @property
    def lb_spans(self) -> list:
        """横補剛間隔の一覧を返す"""
        return self.restraint_spans

    @property
    def lb_positions(self) -> list:
        """横補剛位置（部材左端からの距離）を返す。０、スパンを含む"""
        result = [0]
        for sp in self.restraint_spans:
            x_prev = result[-1]
            result.append(x_prev + sp)
        return result

    @property
    def Q(self):
        """想定モーメント分布に対応する せん断力 Q を返す Q = (M1+M2) / L"""
        return (self.M_Left + self.M_Right) / self.L

    def M_at(self, x):
        """指定位置の想定モーメントを返す。部材左端からの距離 x (mm)を指定"""
        return abs(self.M_Left - x * self.Q)

    def set_member_end_restraints(self, step=0):
        self.restraint_spans.clear()
        self.set_Me()
        req_lb = self.get_lb(step)
        max_n = int(self.L / (2 * req_lb))
        for i in range(max_n):
            if self.M_at(i * req_lb) > self.My:
                self.restraint_spans.insert(i, req_lb)
                self.restraint_spans.insert(-i, req_lb)

        center_span = self.L - sum(self.restraint_spans)
        self.restraint_spans.insert(int(len(self.restraint_spans) / 2), center_span)
        # todo : 左右非対称配置となる場合の処理　2024-1104

    def get_input_data(self) -> str:
        """計算条件の出力用文字列を返す"""
        result = []
        result.append("保有耐力横補剛検討")
        result.append(f'スパン：{self.L} [mm]')
        result.append(f'はり断面：{short_full_name[self.sec]}')
        result.append(f'鋼材強度：{"400N" if self.material.S400N else "490N"}')
        return '\n'.join(result)

    @staticmethod
    def x_ceiling(x, step):
        """数値 x を 指定の数 step の倍数となるようにまるめる"""
        return -(-x // step) * step
