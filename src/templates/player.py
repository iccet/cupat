import math

from ..core.obj.render import *
from ..core.obj.actor import Actor

from linalg.collision import Collision
from src.core.obj.base import CCC
from exceptions.player import PlayerAlreadyExist

BASIC_SHAPES = {
    "triangle": ([0, 0],
                 [math.cos(math.pi / 2) / CCC / 2, 1 / CCC / 2],
                 [1 / CCC / 2, math.cos(math.pi / 2) / CCC / 2]),
    "rocket": ([0, 0],
               [math.cos(math.pi / 3) / CCC / 2, 1 / CCC / 2],
               [math.cos(math.pi / 2) / CCC / 2 + 1 / CCC / 4, 1 / CCC],
               [1 / CCC, math.cos(math.pi / 2) / CCC + 1 / CCC / 4],
               [1 / CCC / 2, math.cos(math.pi / 3) / CCC / 2]),
    "cursor": ([0, 0],
               [math.cos(math.pi / 3) / CCC / 2, 1 / CCC / 2],
               [math.cos(math.pi / 2) / CCC / 2 + 1 / CCC / 4, 1 / CCC],
               [math.cos(math.pi / 6) / CCC / 2, 1 / CCC / 2],
               [1 / CCC / 2, math.cos(math.pi / 6) / CCC / 2],
               [1 / CCC, math.cos(math.pi / 2) / CCC + 1 / CCC / 4],
               [1 / CCC / 2, math.cos(math.pi / 3) / CCC / 2]),
    "arrow": ([0, 0],
              [math.cos(math.pi / 3) / CCC / 2, 1 / CCC / 2],
              [math.cos(math.pi / 6) / CCC / 4, 1 / CCC / 4],
              [1 / CCC / 4, math.cos(math.pi / 6) / CCC / 4],
              [1 / CCC / 2, math.cos(math.pi / 3) / CCC / 2])
}


class BasePlayer(Actor):
    """  """

    _move_points = []
    _track_length = 50
    track = []
    ready = False
    track_color: str = None

    def __init__(self, name, color, shape, track_color=None, position=None):
        super().__init__(name, color, position, shape, shape)
        self.track_color = track_color

    def update_track(self):
        if len(self.track) > self._track_length:
            self.track.pop(0)
        self.track.append(list(self.position))

    def draw_track(self):
        color = QColor(self.track_color)
        pen = QPen(color, 1, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.setBrush(color)

        for i in range(1, len(self.track)):
            self.painter.drawLine(*self.track[i - 1], *self.track[i])

    def render(self):
        super().render()
        self.draw_track()

    @Collision.Elastic
    def in_collision(self, *objects):
        pass

    def update(self):
        super().update()
        self.update_track()


class Player(BasePlayer):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Player, cls).__new__(cls)
        else:
            raise PlayerAlreadyExist
        return cls.instance
