from PySide6.QtCore import Qt
from PySide6.QtGui import QPen

from .Shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def add_to_scene(self, scene):
        self.graphic_item = scene.addEllipse(self.x - self.radius, self.y - self.radius,
                                             2 * self.radius, 2 * self.radius,
                                             QPen(Qt.green))
