from .base import *
from .attachable import AttachableObject
from .render import *
from samples.colors import Colors
import math

FORCE_DEFAULT_VECTOR_COLOR = FDVC = Colors.WHITE
FORCE_PARASITE_VECTOR_COLOR = FPVC = Colors.RED
FORCE_RANDOM_VECTOR_COLOR = FRVC = Colors.MAGENTA


class Force(AttachableObject, RenderObject):
    __target: Vector = None
    __value: Vector = Vector(0, 0)
    acceleration: Vector = Vector(0, 0)

    def __init__(self, root: BaseObject, target: Vector, color=FDVC):
        AttachableObject.__init__(self, root)
        RenderObject.__init__(self, color)
        self.__target = target
        self.__value = Vector(0, 0)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: Vector):
        if isinstance(target, Vector):
            self.__target = target
        else:
            raise TypeError

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, force):
        if isinstance(force, Vector):
            self.__value = force
        else:
            raise TypeError

    def update(self):
        self.position = self.root.center_mass

    def arrow_angle(self):
        return math.pi / (2 * abs(self.__value / 32) + 2)

    def draw_geometry(self):
        angle = self.arrow_angle()
        v0 = self.position
        v = v0 + self.value

        arrow = v0 + (self.value / 3) * 2
        left_arrow = arrow.copy().rotate(angle, v)
        right_arrow = arrow.rotate(-angle, v)

        self.painter.drawLine(*v0, *v)
        self.painter.drawLine(*v, *left_arrow)
        self.painter.drawLine(*v, *right_arrow)

    def render(self):
        color = QColor(self.color)
        pen = QPen(color, 1, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.setBrush(color)
        self.draw_geometry()


class ParasiteForce(Force):
    def __init__(self, root: BaseObject, target: Vector):
        AttachableObject.__init__(self, root, target)
        RenderObject.__init__(self, FPVC)
