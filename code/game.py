import pygame
from code.save import Save
from code.menu import Menu
from code.map import Map
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


# Game Name: Predator

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load("./asset/menu_song.wav")
        pygame.mixer_music.play(-1)
        show_game = Save(self.screen)
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()
            if menu_return == MENU_OPTION[0]:
                map_run = Map(self.screen, "Map1")
                map_run.run()
            elif menu_return == MENU_OPTION[1]:
                show_game.show_score()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
