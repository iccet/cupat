from ._physic import PhysicObject, Vector


class DynamicObject(PhysicObject):

    def in_collision(self, other):
        super().in_collision(other)

    def on_external_impact(self, other):
        pass

    def _update_collision(self):
        _pos = self.position
        _f = self.move_vector

        self.collision = [Vector(point) + self.speed.force for point in self.collision]
        self.geometry = [Vector(point) + self.speed.force for point in self.geometry]

    def update(self):
        self._update_collision()
        self._update_collision_box()
