from .physic import PhysicObject
from .render import RenderObject
from .force import ForceRender, ParasiteForceRender


class Actor(PhysicObject, RenderObject):
    """ Physical scene objects,
    placeable,
    moveable
    """
    def __init__(self, name=None, color=None, position=None, collision_shape=None, render_geometry=None):
        PhysicObject.__init__(self, name, position, collision_shape)
        RenderObject.__init__(self, color, render_geometry)
        self.target_render = ForceRender(self.speed_target)
        self.acceleration_render = ParasiteForceRender(self.acceleration)

    def render(self):
        RenderObject.render(self)
        self.acceleration_render.render()
        self.target_render.render()
