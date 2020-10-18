from abc import ABC
from PyQt5.QtGui import QPen, QPainter, QPolygon
from PyQt5.QtCore import Qt, QPoint
from src.core.objects.render import RenderObject
from src.core.objects.physic import PhysicObject
from src.core.objects.attachable import AttachableObject
from samples.colors import Colors
from utils.regular import regular, circumscribed_radius

DEFAULT_COLOR = DC = Colors.WHITE


class Primitive(RenderObject, PhysicObject, AttachableObject, ABC): pass


class Circle(Primitive):
    radius: int = None

    def on_external_impact(self, other):
        pass

    def in_collision(self, other):
        pass

    def __init__(self, root: PhysicObject, color: str = DC):
        PhysicObject.__init__(self, position=root.position)
        RenderObject.__init__(self, color, self.collision)
        self.radius = circumscribed_radius(root)


class Box(Primitive):
    subdivide: int = 4
    collision: list = None

    def draw_geometry(self):
        pen = QPen(self.color, 1, Qt.SolidLine)
        poly = QPolygon([QPoint(*i) for i in self.geometry])
        hint = QPainter.Antialiasing

        self.painter.setPen(pen)
        self.painter.setRenderHint(hint)
        self.painter.drawPolygon(poly)

    def update(self):
        Primitive.update(self)
        self.collision = self.describe(self.root, self.subdivide)
        self.collision = list(map(lambda x: x + self.position, self.collision))
        self.geometry = self.collision

    def on_external_impact(self, other):
        pass

    def in_collision(self, other):
        pass

    @classmethod
    def describe(cls, obj, n: int = 4) -> list:
        """
        @param obj: PhysicObject
        @rtype: list
        @type n: int
        """
        radius = circumscribed_radius(obj)
        return regular(radius, n)

    def __init__(self, root: PhysicObject, n: int, color: str = DC):
        self.subdivide = n
        self.collision = self.describe(root, self.subdivide)
        AttachableObject.__init__(self, root)
        PhysicObject.__init__(self, collision_shape=self.collision, position=root.position)
        RenderObject.__init__(self, color, self.collision)

    def __iter__(self):
        for i in self.collision:
            yield i
