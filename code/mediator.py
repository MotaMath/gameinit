# from code.const import WIN_WIDTH
# from code.entity import Entity
# from code.obstacle import Obstacle
# from code.player import Player
#
#
# class EntityMediator:
#
#     @staticmethod
#     def __verify_collision_window(Entity):
#         if isinstance(Entity, Obstacle):
#             if Entity.rect.right <= 0:
#                 Entity.health -= 1
#         if isinstance(Entity, Player):
#             if Entity.rect.left >= WIN_WIDTH:
#                 Entity.health -= 1
#         if isinstance(Entity, Player):
#             if Entity.rect.right <= 0:
#                 Entity.health -= 1
#
#     @staticmethod
#     def __verify_collision_entity(ent1, ent2):
#         valid_interaction = False
#         if isinstance(ent1, Obstacle) and isinstance(ent2, Player):
#             valid_interaction = True
#         elif isinstance(ent1, Player) and isinstance(ent2, Obstacle):
#             valid_interaction = True
#         elif isinstance(ent1, Player) and isinstance(ent2, Player):
#             valid_interaction = True
#         elif isinstance(ent1, Player) and isinstance(ent2, Player):
#             valid_interaction = True
#
#         if valid_interaction:  # if valid_interaction == True:
#             if (ent1.rect.right >= ent2.rect.left and
#                     ent1.rect.left <= ent2.rect.right and
#                     ent1.rect.bottom >= ent2.rect.top and
#                     ent1.rect.top <= ent2.rect.bottom):
#                 ent1.health -= 1
#                 ent2.health -= 1
#     #
#     # @staticmethod
#     # def __give_score(enemy: Obstacle, entity_list: list[Entity]):
#     #     if enemy.last_dmg == 'Player1Shot':
#     #         for ent in entity_list:
#     #             if ent.name == 'Player1':
#     #                 ent.score += enemy.score
#     #     elif enemy.last_dmg == 'Player2Shot':
#     #         for ent in entity_list:
#     #             if ent.name == 'Player2':
#     #                 ent.score += enemy.score
#
#     @staticmethod
#     def verify_collision(entity_list: list[Entity]):
#         for i in range(len(entity_list)):
#             entity1 = entity_list[i]
#             EntityMediator.__verify_collision_window(entity1)
#             for j in range(i + 1, len(entity_list)):
#                 entity2 = entity_list[j]
#                 EntityMediator.__verify_collision_entity(entity1, entity2)
#
#     @staticmethod
#     def verify_health(entity_list: list[Entity]):
#         for ent in entity_list:
#             if ent.health == 0:
#                 entity_list.remove(ent)
