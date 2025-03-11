import pygame.key
from pygame.examples.blend_fill import data_dir

from code.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def update(self):
        pass

    def jump(self):
        pass
