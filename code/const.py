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
    "rock": 3,
    "pointer": 4

}

ENTITY_HEALTH = {
    "map1_1": 999,
    "map1_2": 999,
    "map1_3": 999,
    "map1_4": 999,
    "map1_5": 999,
    "map1_6": 999,
    "map1_7": 999,
    "jump2": 1,
    "rock": 1,
    "pointer": 999
}

JUMP = 1

EVENT_ENEMY = pygame.USEREVENT + 1

MILLI = random.randint(800, 2000)
