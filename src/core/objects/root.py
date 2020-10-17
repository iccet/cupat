from src.modules.linalg.vector import Vector


class RootObject:
    __position = None

    def __init__(self, position: Vector = None):
        if position is not None:
            self.__position = Vector(position)
        else:
            self.logger.exception('Object %s is not constructible', self)
            raise ValueError

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, _v: Vector):
        if isinstance(_v, Vector):
            self.__position = _v
        else:
            raise TypeError
