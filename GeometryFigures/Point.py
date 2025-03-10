from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QBrush

from .Shape import Shape


class Point(Shape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def add_to_scene(self, scene):
        self.graphic_item = scene.addEllipse(self.x - 2, self.y - 2, 4, 4,
                                             QPen(Qt.black), QBrush(Qt.red))
