import random
import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from code.const import C_WHITE, EVENT_ENEMY, MILLI, WIN_WIDTH, ENTITY_HEALTH
from code.entity import Entity
from code.factory import Factory


class Map:
    def __init__(self, screen, name):
        self.random_time = None
        self.timeout = 20000
        self.screen = screen
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Factory.get_entity("map1_"))
        self.entity_list.append(Factory.get_entity("jump2"))
        self.entity_list.append(Factory.get_entity("rock"))
        pygame.time.set_timer(EVENT_ENEMY, MILLI)

    def set_random_obstacle_timer(self):
        self.random_time = random.randint(800, 2000)
        pygame.time.set_timer(EVENT_ENEMY, self.random_time)

    def run(self):
        pygame.mixer_music.load("./asset/map1_sound.wav")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            self.map_print(25, " Score: ", C_WHITE, (50, 15))
            self.map_print(15, f"Time: {self.timeout / 1000:.1f}", C_WHITE, (50, 40))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(Factory.get_entity("rock"))
                    self.set_random_obstacle_timer()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def map_print(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)


