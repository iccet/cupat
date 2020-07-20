from .base import *
from .render import *
from samples.colors import Colors
import math

FORCE_DEFAULT_VECTOR_COLOR = FDVC = Colors.WHITE
FORCE_PARASITE_VECTOR_COLOR = FPVC = Colors.RED
FORCE_RANDOM_VECTOR_COLOR = FRVC = Colors.MAGENTA


class Force(BaseObject):
    """ Non placeable, rootable gameobj

    _target_force_vector:
        target to change _force_vector

    __acceleration:
        speed changing _force_vector
    """

    root = None
    _target: Vector = None
    _value: Vector = None
    __acceleration = None

    def __init__(self, root: BaseObject, target: Vector):
        BaseObject.__init__(self, None, root.center_mass)
        self._target = target
        self._value = Vector(0, 0)
        self.root = root

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target: Vector):
        if isinstance(target, Vector):
            self._target = target
        else:
            raise TypeError

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, force):
        if isinstance(force, Vector):
            self._value = force
        else:
            raise TypeError

    def in_collision(self, other):
        other.on_external_impact(self)

    def on_external_impact(self, other):
        pass

    def update(self):
        # self._value += self._target.normalized()
        self.position = self.root.center_mass


class ParasiteForce(Force):
    def __init__(self, root: BaseObject, target: Vector):
        super().__init__(root, target)
        self.color = FPVC


class ForceRender(RenderObject):
    force: Force = None

    def __init__(self, force: Force, color=FDVC):
        RenderObject.__init__(self, color)
        self.force = force

    def arrow_angle(self):
        return math.pi / (2 * abs(self.force.value / 32) + 2)

    def draw_geometry(self):
        angle = self.arrow_angle()
        v0 = self.force.position
        force = self.force.value
        v = v0 + force

        arrow = v0 + (force / 3) * 2
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


class ParasiteForceRender(ForceRender):
    def __init__(self, force: Force):
        super().__init__(force, FPVC)

