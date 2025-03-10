from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT


class Factory:

    @staticmethod
    def get_entity(entity_name, position = (0,0)):
        match entity_name:
            case "map1_":
                list_map = []
                for i in range(1, 7):
                    list_map.append(Background(f"map1_{i}", (0, 0)))
                    list_map.append(Background(f"map1_{i}", (WIN_WIDTH, 0)))
                return list_map
