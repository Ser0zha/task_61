from GeometryFigures.Circle import Circle
from GeometryFigures.Line import Line
from GeometryFigures.Point import Point


class GeometryManager:
    def __init__(self, scene):
        self.scene = scene
        self.objects = []

    def add_object(self, shape_type, *params):
        obj = None
        if shape_type == "point":
            obj = Point(*params)
        elif shape_type == "line":
            obj = Line(*params)
        elif shape_type == "circle":
            obj = Circle(*params)

        if obj:
            obj.add_to_scene(self.scene)
            self.objects.append(obj)
