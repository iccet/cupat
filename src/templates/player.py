from ..core.obj._render import *
from ..core.obj._actor import Actor
from modules._collision import elasticcollision


class Player(Actor):
    """ Your advertisement could be here =) """

    _move_points = []
    _track_length = 50
    track = []
    ready = False
    track_color: str = None
    instance = None

    def __init__(self, name, color, shape, track_color=None, position=None):
        super().__init__(name, color, position, shape, shape)
        self.track_color = track_color

    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super(Player, cls).__new__(cls, *args, **kwargs)
    #     else:
    #         raise ValueError("Player already created.")
    #     return cls.instance

    def __call__(self, *args, **kwargs):
        if Player.instance is None:
            Player.instance = self.__init__(*args, **kwargs)
        else:
            raise ValueError("Player already created.")

    def update_track(self):
        if len(self.track) > self._track_length:
            self.track.pop(0)
        self.track.append(list(self.position))

    def draw_track(self, qpainter):
        color = QColor(self.track_color)
        pen = QPen(color, 1, Qt.SolidLine)
        qpainter.setPen(pen)
        qpainter.setBrush(color)

        for i in range(1, len(self.track)):
            qpainter.drawLine(*self.track[i - 1], *self.track[i])

    def render(self, qpainter):
        super().render(qpainter)
        self.draw_track(qpainter)

    @elasticcollision
    def in_collision(self, *objects):
        pass

    def update(self):
        super().update()
        self.update_track()
