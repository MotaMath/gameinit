# Example file showing a circle moving on screen
import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT

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
            menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()