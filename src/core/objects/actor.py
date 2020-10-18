from .physic import PhysicObject
from .render import RenderObject


class Actor(PhysicObject, RenderObject):
    """ Physical scene objects,
    placeable,
    moveable
    """
    def __init__(self, name=None, color=None, position=None, collision_shape=None, render_geometry=None):
        PhysicObject.__init__(self, name, position, collision_shape)
        RenderObject.__init__(self, color, render_geometry)

    def render(self):
        RenderObject.render(self)
        self.speed.render()
        self.speed_target.render()
        self.acceleration.render()

