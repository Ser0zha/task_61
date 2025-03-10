from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.graphic_item = None

    @abstractmethod
    def add_to_scene(self, scene):
        pass
