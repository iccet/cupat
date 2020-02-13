from ._base import *
from ._render import *

FORCE_DEFAULT_VECTOR_COLOR = FDVC = WHITE
FORCE_PARASITE_VECTOR_COLOR = FPVC = RED
FORCE_ANDOM_VECTOR_COLOR = FRVC = MAGENTA


class Force(BaseObject, RenderObject):
    """ Non placeable, rootable gameobj

    _target_force_vector:
        target to change _force_vector

    __acceleration:
        speed changing _force_vector
    """

    __acceleration = None
    _root = None
    _target_force_vector: Vector = None
    _force_vector: Vector = None

    def __init__(self, root):
        BaseObject.__init__(self, None, root.center_mass)
        RenderObject.__init__(self, FDVC)
        self._target_force_vector = self._force_vector = Vector(0, 0)
        self._root = root

    @property
    def target(self):
        return self._target_force_vector

    @target.setter
    def target(self, _tfv):
        self._target_force_vector = _tfv

    @property
    def force(self):
        return self._force_vector

    @force.setter
    def force(self, _fv):
        self._force_vector = _fv

    def in_collision(self, other):
        other.on_external_impact(self)

    def on_external_impact(self, other):
        pass

    def update(self):
        self.position = self._root.center_mass

    def draw_geometry(self, qpainter):
        color = QColor(self.color)
        pen = QPen(color, 1, Qt.SolidLine)
        qpainter.setPen(pen)
        qpainter.setBrush(color)

        _v0 = self.position
        _fvc = self.force
        _v = _v0 + _fvc
        _lvr = (_v0 + (_fvc / 3) * 2).copy().rotate(math.pi / 12, _v)
        _rvr = (_v0 + (_fvc / 3) * 2).copy().rotate(-math.pi / 12, _v)

        qpainter.drawLine(*_v0, *_v)
        qpainter.drawLine(*_v, *_lvr)
        qpainter.drawLine(*_v, *_rvr)

    def render(self, qpainter):
        self.draw_geometry(qpainter)
        qpainter.drawLine(*self._root.position, *self.target)


class ParasiteForce(Force):
    def __init__(self, root):
        super().__init__(root)
        self.color = FPVC
