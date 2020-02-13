""" ! Don`t touch the imports
    ! CCC - Global coefficient for adequate scaling speed px,
    else we have abs(vector) >= 1000, what cant be controlable,
    changing this parameter has unobvious consequences, careful.
"""

from modules._vector import Vector, math
from abc import ABC, abstractmethod

CONVERT_CONST_COEFFICIENT = CCC = 1 / 100
BASIC_SHAPES = {
    "triangle": ([0, 0],
                 [math.cos(math.pi / 2) / CCC / 2, 1 / CCC / 2],
                 [1 / CCC / 2, math.cos(math.pi / 2) / CCC / 2]),
    "rocket": ([0, 0],
               [math.cos(math.pi / 3) / CCC / 2, 1 / CCC / 2],
               [math.cos(math.pi / 2) / CCC / 2 + 1 / CCC / 4, 1 / CCC],
               [1 / CCC, math.cos(math.pi / 2) / CCC + 1 / CCC / 4],
               [1 / CCC / 2, math.cos(math.pi / 3) / CCC / 2]),
    "cursor": ([0, 0],
               [math.cos(math.pi / 3) / CCC / 2, 1 / CCC / 2],
               [math.cos(math.pi / 2) / CCC / 2 + 1 / CCC / 4, 1 / CCC],
               [math.cos(math.pi / 6) / CCC / 2, 1 / CCC / 2],
               [1 / CCC / 2, math.cos(math.pi / 6) / CCC / 2],
               [1 / CCC, math.cos(math.pi / 2) / CCC + 1 / CCC / 4],
               [1 / CCC / 2, math.cos(math.pi / 3) / CCC / 2]),
    "arrow": ([0, 0],
              [math.cos(math.pi / 3) / CCC / 2, 1 / CCC / 2],
              [math.cos(math.pi / 6) / CCC / 4, 1 / CCC / 4],
              [1 / CCC / 4, math.cos(math.pi / 6) / CCC / 4],
              [1 / CCC / 2, math.cos(math.pi / 3) / CCC / 2])
}


class BaseObject(ABC):
    """ Basic game obj """

    _ins_count = 0
    _name_base = set()

    def __init__(self, name: str = None, position: Vector = None):
        if position is not None:
            self.__position = Vector(position)
        if name is None:
            self.__name = self._name_gen()
        else:
            self._add_name(name)

    def _add_name(self, name):
        if name in self._name_base:
            self.__name = self._name_gen(name)
        else:
            self._ins_count += 1
            self.__name = name
            self._name_base.add(name)

    def __del__(self):
        self._ins_count -= 1

    @classmethod
    def _name_gen(cls, pattern="GameObject"):
        cls._ins_count += 1
        return pattern + "_" + str(cls._ins_count)

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
        self.__position = _v

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
