from linalg.vector import Vector
from abc import ABC, abstractmethod

""" CCC - Global coefficient for adequate scaling speed px,
    else we have abs(vector) >= 1000, what cant be controlable,
    changing this parameter has unobvious consequences, careful.
"""
CONST_CONVERT_COEFFICIENT = CCC = 1 / 100


class BaseObject(ABC):
    """ Basic game obj """

    count = 0
    objects = set()  # TODO create set of BaseObjects

    def __init__(self, name: str = None, position: Vector = None, root=None):
        self.root = root
        if position is not None:
            self.__position = Vector(position)
            self.name = name

    def __del__(self):
        self.count -= 1

    @abstractmethod
    def in_collision(self, other):
        """ Impact OF external objects """
        pass

    @abstractmethod
    def on_external_impact(self, other):
        """ Impact ON external objects """
        pass

    @abstractmethod
    def update(self):
        pass

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, _v: Vector):
        if isinstance(_v, Vector):
            self.__position = _v
        else:
            raise TypeError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name is None:
            self.__name = self._name_gen()
        elif name in self.objects:
            self.__name = self._name_gen(name)
        else:
            self.count += 1
            self.__name = name
            self.objects.add(name)

    @classmethod
    def _name_gen(cls, pattern="GameObject"):
        cls.count += 1
        return pattern + "_" + str(cls.count)
