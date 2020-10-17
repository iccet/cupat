from .physic import PhysicObject, Vector
from interfaces.idynamic import IDynamic


class StaticObject(PhysicObject):

    def update(self):
        self.collision = [Vector(point) + self.speed.value for point in self.collision]
        self.geometry = [Vector(point) + self.speed.value for point in self.geometry]

