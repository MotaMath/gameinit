import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from code.const import C_BLACK, WIN_WIDTH, C_WHITE
from code.entity import Entity
from code.factory import Factory

class Map:
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Factory.get_entity("map1_"))
        self.timeout = 20000

    def run(self):
        pygame.mixer_music.load("./asset/map1_sound.wav")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            self.menu_text(30, "Score: ", C_WHITE, (50, 15))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
