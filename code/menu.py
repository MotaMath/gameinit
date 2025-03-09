import pygame.image
from code.score import Score
from code.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, C_GRAY, C_BLACK, C_GREEN, C_WHITE

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("./asset/menu.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/menu_song.wav')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Wolf Master", C_BLACK, ((WIN_WIDTH / 3), 70))
            self.menu_text(10, "@Matheus Mota Ribeiro", C_BLACK, ((WIN_WIDTH / 8), 300))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_BLACK, ((WIN_WIDTH / 3), 120 + 30 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 3), 120 + 30 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Papyrus", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)