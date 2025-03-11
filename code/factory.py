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
                for i in range(1, 7):
                    list_map.append(Background(f"map1_{i}", (0, 0)))
                    list_map.append(Background(f"map1_{i}", (WIN_WIDTH, 0)))
                return list_map
            case "jump2":
                return Player("jump2", (50, 225))
            case "rocks1":
                return Obstacle("rocks1", (WIN_WIDTH - 40, 240))
