""" Render object """

from PyQt5.QtGui import QColor, QPen, QBrush, \
    QPainter, QPolygon, QFont
from .base import Vector
from PyQt5.QtCore import Qt, QPoint
from abc import ABC, abstractmethod
from samples.colors import Colors


class RenderObject(ABC):
    OBJECT_CENTER_MASS_COLOR = Colors.WHITE
    OBJECT_COLLISION_BOX_COLOR = Colors.WHITE
    OBJECT_COLLISION_COLOR = Colors.WHITE
    OBJECT_NAME_COLOR = Colors.WHITE

    painter: QPainter = None  # DI QPainter
    font: QFont = QFont(*('Ubuntu', 12))
    text_color: QColor = QColor(OBJECT_NAME_COLOR)
    center_mass_color: QColor = QColor(OBJECT_CENTER_MASS_COLOR)
    box_color: QColor = QColor(OBJECT_COLLISION_BOX_COLOR)

    def __init__(self, color: str = None, geometry: tuple = None):
        self.color = QColor(color)
        if geometry is not None:
            self.geometry = [(Vector(point) + self.position).to_list() for point in geometry]
        else:
            self.geometry = geometry

    def draw_object_name(self):
        self.painter.setPen(RenderObject.text_color)
        self.painter.setFont(self.font)
        self.painter.drawText(QPoint(*self.position), self.name)

    def draw_collision_box(self):
        self.painter.setPen(RenderObject.box_color)
        self.painter.drawRect(*self.collision_box)

    def draw_center_mass(self):
        self.painter.setPen(self.center_mass_color)
        self.painter.setBrush(self.color)
        self.painter.drawEllipse(*self.center_mass, 5, 5)

    def draw_collision(self):
        brush = QBrush(Qt.SolidPattern)
        pen = QPen(self.collision_color, 1, Qt.SolidLine)
        poly = QPolygon([QPoint(*i) for i in self.collision])

        self.painter.setPen(pen)
        self.painter.setBrush(brush)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.drawPolygon(poly)

    def draw_geometry(self):
        pen = QPen(self.color, 1, Qt.SolidLine)
        poly = QPolygon([QPoint(*i) for i in self.geometry])
        hint = QPainter.Antialiasing

        self.painter.setPen(pen)
        self.painter.setBrush(self.color)
        self.painter.setRenderHint(hint)
        self.painter.drawPolygon(poly)

    def render(self):
        self.draw_collision_box()
        self.draw_geometry()
        self.draw_center_mass()
        self.draw_object_name()
