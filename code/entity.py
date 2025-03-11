from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    def __init__(self, name, position):
        self.name = name
        self.surf = pygame.image.load("./asset/" + name + ".png")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.crash = 1

    def move(self):
        pass
