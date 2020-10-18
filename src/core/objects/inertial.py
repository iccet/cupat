from base import CCC
from src.modules.linalg.vector import Vector
from interfaces.iinertial import IInertial


class InertialObject(IInertial):
    mass_vector: Vector = None

    def __init__(self):
        self.mass_vector = self._calc_center_mass()

    @property
    def energy(self):
        return (abs(self.speed.value) ** 2 * self.mass) / 2

    @property
    def impulse(self):
        return Vector(self.speed.value * self.mass)

    @property
    def mass(self):
        return .5

    @property
    def center_mass(self):
        return self.mass_vector

    def _calc_center_mass(self):
        _col = self.collision
        _len = len(_col)
        return Vector([sum(Vector.component(_col, 0)) / _len,
                       sum(Vector.component(_col, 1)) / _len])

    def inertial_impact(self):
        _old_speed = self.speed.value.copy()
        _new_mass_vector = self.mass_vector.copy()
        self.mass_vector = self._calc_center_mass()
        _moment_vector = self.mass_vector - _new_mass_vector
        self.speed.value += _moment_vector * CCC

        self.acceleration.value = -(self.speed.value - _old_speed) / self.mass
        if self.speed.value != self.acceleration.value:
            self.speed.value += self.acceleration.value
