from src.modules.linalg.vector import Vector
from interfaces.idynamic import IDynamic


class TransientTarget(IDynamic, object):
    __target: Vector = None
    __value: Vector = Vector(0, 0)
    __acceleration = None

    def update(self):
        pass

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: Vector):
        if isinstance(target, Vector):
            self.__target = target
        else:
            raise TypeError

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, force):
        if isinstance(force, Vector):
            self.__value = force
        else:
            raise TypeError

    def __init__(self, target: Vector):
        self.__target = target
