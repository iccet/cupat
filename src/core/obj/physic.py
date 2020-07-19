from .base import *
from .force import Force, ParasiteForce
import math


class PhysicObject(BaseObject):
    __mass = None
    __speed_vector: Force = None
    __acceleration_vector: Force = None
    __mass_vector: Vector = None

    _external_mutable = True
    _controls_response = True
    _static = True

    __collision_shape: list = None
    __collision_box: list = None

    def __init__(self, name: str = None, position=None, collision_shape: list = None, mass=.5):
        super().__init__(name, position)
        self.__collision_shape = [(Vector(point) + self.position) for point in collision_shape]
        self.__mass_vector = self._calc_center_mass()
        self.__mass = mass
        self.__speed_vector = Force(self)
        self.__acceleration_vector = ParasiteForce(self)
        self._update_collision_box()

    @property
    def center_mass(self):
        return self.__mass_vector

    @property
    def speed(self):
        return self.__speed_vector

    @property
    def collision(self):
        return self.__collision_shape

    @property
    def collision_box(self):
        return self.__collision_box

    @property
    def move_vector(self):
        return self.__speed_vector.target

    @property
    def acceleration(self):
        return self.__acceleration_vector

    @collision.setter
    def collision(self, shape: list):
        self.__collision_shape = shape

    @speed.setter
    def speed(self, v):
        self.__speed_vector = v

    @move_vector.setter
    def move_vector(self, _l: list):
        self.__speed_vector.target = Vector(_l)

    @acceleration.setter
    def acceleration(self, v):
        self.__acceleration_vector.force = v

    def _calc_center_mass(self):
        _col = self.collision
        _len = len(_col)
        return Vector([sum(i[0] for i in _col) / _len,
                       sum(i[1] for i in _col) / _len])

    def _calc_mass(self):
        pass

    def _instant_energy(self):
        return (abs(self.speed.force) ** 2 * self.__mass) / 2

    def _instant_impulse(self):
        return Vector(self.speed.force * self.__mass)

    def _control_impact(self):
        """ Sum of control by player or ... non player forces,
         who getting control on actor
        """
        if self._controls_response:
            _pos = self.position
            _f = self.move_vector
            self.speed.force += (_f - _pos) * CCC

    def _inertial_impact(self):
        """ Sum of all actor inertial force momentum """
        _old_speed = self.speed.force.copy()
        _new_mass_vector = self.__mass_vector.copy()
        self.__mass_vector = self._calc_center_mass()
        _moment_vector = self.__mass_vector - _new_mass_vector
        self.speed.force += _moment_vector * CCC

        self.acceleration.force = -(self.speed.force - _old_speed) / self.__mass
        if self.speed.force != self.acceleration.force:
            self.speed.force += self.acceleration.force

    def _update_collision(self):
        _pos = self.position
        _f = self.move_vector
        self.__mass_vector = self._calc_center_mass()

        _a = Vector.angle_between_vectors(self.__mass_vector - _pos, _f - _pos)
        _a += math.pi

        self.collision = [(Vector(point) + self.speed.force).rotate(_a, _pos) for point in self.collision]
        self.geometry = [(Vector(point) + self.speed.force).rotate(_a, _pos) for point in self.geometry]

    def _update_collision_box(self):
        _xar = [i[0] for i in self.collision]
        _yar = [i[1] for i in self.collision]
        min_x = min(_xar)
        min_y = min(_yar)
        max_x = max(_xar)
        max_y = max(_yar)
        self.__collision_box = [min_x, min_y, max_x - min_x, max_y - min_y]

    def in_collision(self, other):
        pass

    def on_external_impact(self, other):
        if self._external_mutable:
            self.speed.force += other * CCC

    def update(self):
        self._control_impact()
        self._inertial_impact()
        self.speed.update()
        self.acceleration.update()
        self.position += self.speed.force
        # self.move_vector += self.speed.force
        self._update_collision()
        self._update_collision_box()

