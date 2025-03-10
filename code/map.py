import pygame.display

from code.entity import Entity
from code.factory import Factory

class Map:
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Factory.get_entity("map1_"))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()