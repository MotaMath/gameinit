import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import SCORE_POS, C_WHITE


class Save:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("./asset/end_game.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, score):
        pygame.mixer_music.load("./asset/score.mp3")
        pygame.mixer_music.play(-1)
        self.screen.blit(source=self.surf, dest=self.rect)
        while True:
            self.save_print(48, "GOOD JOB!", C_WHITE, SCORE_POS["Title"])
            self.save_print(35, "Score", C_WHITE, SCORE_POS[0])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def show_score(self):
        pygame.mixer_music.load("./asset/score.mp3")
        pygame.mixer_music.play(-1)
        self.screen.blit(source=self.surf, dest=self.rect)
        while True:
            self.save_print(48, "SCORE!", C_WHITE, SCORE_POS["Title"])
            self.save_print(48, "1.", C_WHITE, SCORE_POS["Title"])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def save_print(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)