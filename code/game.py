# Example file showing a circle moving on screen
import pygame
from code.menu import Menu
from code.map import Map
from code.score import Score
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


# Name of the game

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load("./asset/menu_song.wav")
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()
            if menu_return == MENU_OPTION[0]:
                map = Map(self.screen, "Map1")
                map_start = map.run()
            elif menu_return == MENU_OPTION[1]:
                pass
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
