import pygame.key
from code.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.rect = pygame.Rect(50, 0, 200, 70)
        self.velocity_y = 0
        self.jump_power = -10
        self.gravity = 0.5
        self.ground_y = 300

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w] and self.rect.bottom >= self.ground_y:
            self.velocity_y = self.jump_power

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.velocity_y = 0