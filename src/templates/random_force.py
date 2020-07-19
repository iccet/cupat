from ..core.obj.force import Force, FRVC, Vector
from ..core.obj.render import *
import random


class RandomForce(Force):
    __range = None
    __acceleration = None

    def __init__(self, root, _range=(-100, 100), acceleration=1):
        super().__init__(root)
        self.color = FRVC
        self.__range = _range
        self.__acceleration = acceleration

    def random(self):
        random.seed()
        _nf = random.randint(*self.__range)
        self.target = Vector([random.random() * _nf for _ in range(2)])

    def update(self, *objects):
        super().update(*objects)
        if self.force != self.target:
            _tmp = self.target - self.force
            self.force += _tmp.normalized(self.__acceleration)
