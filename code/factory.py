import random
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.obstacle import Obstacle
from code.player import Player


class Factory:

    @staticmethod
    def get_entity(entity_name, position=(0, 0)):
        match entity_name:
            case "map1_":
                list_map = []
                for i in range(1, 6):
                    list_map.append(Background(f"map1_{i}", (0, 0)))
                    list_map.append(Background(f"map1_{i}", (WIN_WIDTH, 0)))
                return list_map
            case "predator":
                return Player("predator", (50, 500))
            case "gold":
                return Obstacle("gold", (WIN_WIDTH + 10, random.randint(60, WIN_HEIGHT - 100)))
