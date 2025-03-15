import pygame
from pygame import Surface, Rect, K_RETURN, K_BACKSPACE, KEYDOWN, K_ESCAPE
from pygame.font import Font
from code.const import SCORE_POS, C_WHITE, WIN_WIDTH, C_GRAY
from code.proxy import Proxy


class Save:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("./asset/end_game.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, score_total: int):
        pygame.mixer_music.load("./asset/score.mp3")
        pygame.mixer_music.play(-1)
        db = Proxy("Score")
        name = ""
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.save_print(48, "GOOD JOB!", C_WHITE, SCORE_POS["Title"])
            self.save_print(35, f"Score {score_total}", C_WHITE, SCORE_POS[0])
            self.save_print(35, f"Enter your name: ", C_WHITE, SCORE_POS[2])
            self.save_print(20, name, C_WHITE, (WIN_WIDTH / 2, 190))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        print(score_total)
                        db.save({"name": name, "score": score_total})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 8:
                            name += event.unicode
            self.save_print(20, name, C_WHITE, SCORE_POS['Name'])


    def show_score(self):
        pygame.mixer_music.load("./asset/score.mp3")
        pygame.mixer_music.play(-1)
        self.screen.blit(source=self.surf, dest=self.rect)
        db = Proxy("Score")
        list_score = db.retrieve_top10()
        db.close()
        for max_score in list_score:
            id_, name, score = max_score
            self.save_print(20, f'{name}     {score}    ', C_WHITE,
                            SCORE_POS[list_score.index(max_score)])
        while True:
            self.save_print(12, "Press ESC to return to MENU", C_GRAY, (480, 310))
            self.save_print(48, "TOP SCORE!", C_WHITE, SCORE_POS["Title"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def save_print(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)