import random
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
    "gold": random.randint(5, 10),
}

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

JUMP = 1

EVENT_ENEMY = pygame.USEREVENT + 1
TIME_COMPLETE = pygame.USEREVENT + 2

MILLI = random.randint(100, 1000)
