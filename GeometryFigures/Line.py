from PySide6.QtCore import QLineF, Qt
from PySide6.QtGui import QPen

from .Shape import Shape


class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def add_to_scene(self, scene):
        self.graphic_item = scene.addLine(QLineF(self.x1, self.y1, self.x2, self.y2), QPen(Qt.blue))
