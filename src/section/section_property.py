from abc import ABC, abstractproperty
from abc import abstractmethod


class Section(ABC):
    def __init__(self, label=''):
        self.label = label

    @abstractmethod
    def An(self):
        """断面積を返す"""
        pass

    @abstractmethod
    def Zx(self):
        """断面係数を返す"""
        pass

    @abstractmethod
    def Ix(self):
        """断面２次モーメントを返す"""
        pass


class RectangularSection(Section):
    def __init__(self, w: float, h: float, label: str = ''):
        """
        矩形断面
        :param w: 幅（mm）
        :param h: せい（mm）
        :param label: 名称（省略可）
        """
        super().__init__(label)
        self.w = w
        self.h = h

    @property
    def An(self):
        return self.w * self.h

    @property
    def Zx(self):
        return (1. / 6.) * self.w * self.h ** 2

    @property
    def Ix(self):
        return (1. / 12.) * self.w * self.h ** 3
