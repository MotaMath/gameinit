import random

import pygame

from code.const import WIN_WIDTH, SPEED, EVENT_ENEMY
from code.entity import Entity


class Obstacle(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= SPEED[self.name]

    def hit(self):
        pass