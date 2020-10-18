from ..core.objects.force import Force, FRVC
from ..core.objects.render import *
from interfaces.iimpact import IImpact
import random


class RandomForce(IImpact, Force):

    __range = None
    __acceleration = None

    def __init__(self, root, _range=(-100, 100), acceleration=1):
        super().__init__(root, Vector(0, 0))
        self.color = FRVC
        self.__range = _range
        self.__acceleration = acceleration

    def in_collision(self, other):
        other.impact_on(self)

    def impact_on(self, other):
        pass

    def random(self):
        rnd = random.randint(*self.__range)
        self.target = Vector([random.random() * rnd for _ in range(2)])

    def update(self, *objects):
        super().update(*objects)
        if self.value != self.target:
            _tmp = self.target - self.value
            self.value += _tmp.normalized(self.__acceleration)
