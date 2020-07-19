from .physic import PhysicObject
from .render import RenderObject


class Actor(PhysicObject, RenderObject):
    """ Physical scene obj,
    placeable,
    moveable
    """
    def __init__(self, name=None, color=None, position=None, collision_shape=None, render_geometry=None):
        PhysicObject.__init__(self, name, position, collision_shape)
        RenderObject.__init__(self, color, render_geometry)

    def on_external_impact(self, other):
        PhysicObject.on_external_impact(self, other)

    def in_collision(self, other):
        PhysicObject.in_collision(self, other)

    def render(self):
        RenderObject.render(self)
        self.acceleration.render()
        self.speed.render()
