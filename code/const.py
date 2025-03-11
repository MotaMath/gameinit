import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

C_GREEN = (128, 255, 0)
C_GRAY = (64, 64, 64)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)

MENU_OPTION = ("New", "Score", "Exit")

SPEED = {
    "map1_1": 0,
    "map1_2": 1,
    "map1_3": 2,
    "map1_4": 3,
    "map1_5": 4,
    "map1_6": 5,
    "map1_7": 6,
    "rocks1": 2,

}

EVENT_ENEMY = pygame.USEREVENT + 1
