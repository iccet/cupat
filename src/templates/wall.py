from ..core.obj.static import StaticObject
from ..core.obj.render import RenderObject
from linalg.collision import Collision
from samples.colors import Colors

WALL_STD_COLOR = WSC = Colors.LIGHT_BLUE
WALL_FLAT_COLOR = WFC = Colors.REGULAR_BLUE
WALL_ELASTIC_COLOR = WEC = Colors.TURQ_BLUE
WALL_STUCK_COLOR = WSTC = Colors.DARK_BLUE

SQUARE_SHAPE = ((0, 0), (0, 1), (1, 1), (1, 0))


class Wall(StaticObject, RenderObject):

    def __init__(self, name=None, color=WSC, scaling=(100, 100), position=None, collision_shape=SQUARE_SHAPE):
        _cs = [(collision_shape[i][0] * scaling[0], collision_shape[i][1] * scaling[1])
               for i in range(len(collision_shape))]
        StaticObject.__init__(self, name, position, _cs)
        RenderObject.__init__(self, color, _cs)

    @Collision.NonElastic
    def in_collision(self, *objects):
        pass

    def on_external_impact(self, other):
        print("wall impact", other)
        pass

    def render(self):
        RenderObject.render(self)

    def update(self):
        StaticObject.update(self)


class FlatWall(Wall):
    def __init__(self, scaling=(1, 1), position=None):
        super().__init__(WFC, scaling, position)


class ElasticWall(Wall):
    def __init__(self, scaling=(1, 1), position=None):
        super().__init__(WEC, scaling, position)


class StuckWall(Wall):
    def __init__(self, scaling=(1, 1), position=None):
        super().__init__(WSTC, scaling, position)

