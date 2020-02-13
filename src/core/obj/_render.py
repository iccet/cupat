""" ! Don`t touch non uses imports """

from PyQt5.QtGui import QColor, QPen, QBrush, \
    QPainter, QPolygon, QFont
from ._base import Vector
from PyQt5.QtCore import Qt, QPoint
from abc import ABC, abstractmethod

BLUE = "#2980b9"
RED = "#ce4250"
ORANGE = "#f59e16"
GREEN = "#268C52"
MAGENTA = "#bd93f9"
PURPLE = "#f676c0"

DARK_BLUE = "#07086f"
REGULAR_BLUE = "#0005e3"
TURQ_BLUE = "#28dfff"
LIGHT_BLUE = "#2494ea"

GRAY = "#31363b"
BLACK = "#23262a"
WHITE = "#eff0f1"

# aliases
OBJECT_CENTER_MASS_COLOR = OCMC = WHITE
OBJECT_COLLISION_BOX_COLOR = OCBC = WHITE
OBJECT_COLLISION_COLOR = OCC = WHITE
OBJECT_NAME_COLOR = ONC = WHITE


class RenderObject(ABC):

    font: tuple = ('Ubuntu', 12)

    def __init__(self, color: str = None, geometry: tuple = None):
        self.__color = color
        if geometry is not None:
            self.__render_geometry = [(Vector(point) + self.position).to_list() for point in geometry]
        else:
            self.__render_geometry = geometry

    def draw_object_name(self, qpainter):
        color = QColor(ONC)
        qpainter.setPen(color)
        qpainter.setFont(QFont(*self.font))
        qpainter.drawText(QPoint(*self.position), self.name)

    def draw_collision_box(self, qpainter):
        color = QColor(OCBC)
        qpainter.setPen(color)
        qpainter.drawRect(*self.collision_box)

    def draw_center_mass(self, qpainter):
        color = QColor(OCMC)
        qpainter.setPen(color)
        qpainter.setBrush(color)
        qpainter.drawEllipse(*self.center_mass, 5, 5)

    def draw_collision(self, qpainter):
        color = QColor(OCC)
        brush = QBrush(Qt.SolidPattern)
        pen = QPen(color, 1, Qt.SolidLine)
        qpainter.setPen(pen)
        qpainter.setBrush(brush)
        qpainter.setRenderHint(QPainter.Antialiasing)
        poly = QPolygon([QPoint(*i) for i in self.collision])
        qpainter.drawPolygon(poly)

    def draw_geometry(self, qpainter):
        color = QColor(self.color)

        pen = QPen(color, 1, Qt.SolidLine)
        qpainter.setPen(pen)
        qpainter.setBrush(color)
        qpainter.setRenderHint(QPainter.Antialiasing)
        poly = QPolygon([QPoint(*i) for i in self.geometry])
        qpainter.drawPolygon(poly)

    @abstractmethod
    def render(self, qpainter):
        self.draw_collision_box(qpainter)
        self.draw_geometry(qpainter)
        self.draw_center_mass(qpainter)
        self.draw_object_name(qpainter)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    @property
    def geometry(self):
        return self.__render_geometry

    @geometry.setter
    def geometry(self, g):
        self.__render_geometry = g
