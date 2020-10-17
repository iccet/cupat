from .base import *
from .force import Force, ParasiteForce
import math


class PhysicObject(BaseObject):
    __mass = None
    speed: Force = None
    acceleration: Force = None
    mass_vector: Vector = None

    _external_mutable = True
    _controls_response = True
    _static = True

    __collision_shape: list = None
    __collision_box: list = None

    class Instant:
        def energy(self):
            return (abs(self.speed.value) ** 2 * self.__mass) / 2

        def impulse(self):
            return Vector(self.speed.value * self.__mass)

    def __init__(self, name: str = None, position=None, collision_shape: list = None, mass=.5):
        super().__init__(name, position)
        self.__collision_shape = [(Vector(point) + self.position) for point in collision_shape]
        self.mass_vector = self._calc_center_mass()
        self.__mass = mass
        self.speed = Force(self, Vector(0, 0))
        self.speed_target = Force(self, Vector(0, 0))
        self.acceleration = ParasiteForce(self, Vector(0, 0))
        self._update_collision_box()

    @property
    def center_mass(self):
        return self.mass_vector

    @property
    def collision(self):
        return self.__collision_shape

    @property
    def collision_box(self):
        return self.__collision_box

    @property
    def move_target(self):
        return self.speed.target

    @collision.setter
    def collision(self, shape: list):
        self.__collision_shape = shape

    @move_target.setter
    def move_target(self, _l: list):
        self.speed.target = Vector(_l)

    def _calc_center_mass(self):
        _col = self.collision
        _len = len(_col)
        return Vector([sum(Vector.component(_col, 0)) / _len,
                       sum(Vector.component(_col, 1)) / _len])

    def _calc_mass(self):
        pass

    def _control_impact(self):
        """ Sum of control by player or ... non player forces,
         who getting control on actor
        """
        if self._controls_response:
            self.speed_target.value = self.move_target - self.position
            self.speed.value += self.speed_target.value / 1000  # time reduce effect

    def _inertial_impact(self):
        """ Sum of all actor inertial force momentum """
        _old_speed = self.speed.value.copy()
        _new_mass_vector = self.mass_vector.copy()
        self.mass_vector = self._calc_center_mass()
        _moment_vector = self.mass_vector - _new_mass_vector
        self.speed.value += _moment_vector * CCC

        self.acceleration.value = -(self.speed.value - _old_speed) / self.__mass
        if self.speed.value != self.acceleration.value:
            self.speed.value += self.acceleration.value

    def _update_collision(self):
        _pos = self.position
        _f = self.move_target
        self.mass_vector = self._calc_center_mass()

        _a = Vector.angle_between_vectors(self.mass_vector - _pos, _f - _pos)
        _a += math.pi

        self.collision = [(Vector(point) + self.speed.value).rotate(_a, _pos) for point in self.collision]
        self.geometry = [(Vector(point) + self.speed.value).rotate(_a, _pos) for point in self.geometry]

    def _update_collision_box(self):
        _x_array = tuple(Vector.component(self.collision, 0))
        _y_array = tuple(Vector.component(self.collision, 1))
        min_x = min(_x_array)
        min_y = min(_y_array)
        max_x = max(_x_array)
        max_y = max(_y_array)
        self.__collision_box = [min_x, min_y, max_x - min_x, max_y - min_y]

    def in_collision(self, other):
        pass

    def on_external_impact(self, other):
        if self._external_mutable:
            self.speed.value += other * CCC

    def update(self):
        self._control_impact()
        self._inertial_impact()
        self.speed.update()
        self.speed_target.update()
        self.acceleration.update()
        self.position += self.speed.value
        # self.move_vector += self.speed.value  # fixed target mode
        self._update_collision()
        self._update_collision_box()

