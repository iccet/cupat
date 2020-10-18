from .base import *
from src.modules.linalg.vector import Vector
from .root import RootObject
from .force import Force, ParasiteForce
from interfaces.idynamic import IDynamic
from interfaces.iincollision import IInCollision
from interfaces.iimpact import IImpact
from interfaces.icontrol import IControl
from inertial import InertialObject
from utils.regular import square_mask
import math


class PhysicObject(InertialObject, RootObject, BaseObject,
                   IDynamic, IInCollision, IImpact, IControl):
    speed: Force = None
    acceleration: Force = None

    _external_mutable = True
    _controls_response = True
    _static = True

    __collision_shape: list = None
    __collision_box: list = None

    def __init__(self, name: str = None, position=None, collision_shape: list = None):
        BaseObject.__init__(self, name)
        RootObject.__init__(self, position)
        self.__collision_shape = [(Vector(point) + self.position) for point in collision_shape]
        InertialObject.__init__(self)
        self.speed = Force(self, Vector(0, 0))
        self.speed_target = Force(self, Vector(0, 0))
        self.acceleration = ParasiteForce(self, Vector(0, 0))

    @property
    def collision(self):
        return self.__collision_shape

    @property
    def collision_box(self):
        min_x, min_y, max_x, max_y = square_mask(self)
        return min_x, min_y, max_x - min_x, max_y - min_y

    @property
    def move_target(self):
        return self.speed.target

    @collision.setter
    def collision(self, shape: list):
        self.__collision_shape = shape

    @move_target.setter
    def move_target(self, _l: list):
        self.speed.target = Vector(_l)

    def control_impact(self):
        if self._controls_response:
            self.speed_target.value = self.move_target - self.position
            self.speed.value += (self.move_target - self.position) / 1000  # time reduce effect

    def _update_collision(self):
        self.mass_vector = self._calc_center_mass()
        _a = Vector.angle_between_vectors(self.mass_vector - self.position,
                                          self.move_target - self.position) + math.pi

        self.collision = [(Vector(point) + self.speed.value).rotate(_a, self.position)
                          for point in self.collision]
        self.geometry = [(Vector(point) + self.speed.value).rotate(_a, self.position)
                         for point in self.geometry]

    def in_collision(self, other):
        pass

    def impact_on(self, other):
        if self._external_mutable:
            self.speed.value += other.value * CCC / 2

    def update(self):
        self.control_impact()
        self.inertial_impact()
        self.speed.update()
        self.speed_target.update()
        self.acceleration.update()
        self.position += self.speed.value
        # self.move_vector += self.speed.value  # fixed target mode
        self._update_collision()

