from game_map.Door import Door
from systems.CollisionManager import CollisionManager


class Stage:

    def __init__(self, screen, sprite_manager, player, enemies, game_map):
        self.screenGame = screen
        self.sprite_manager = sprite_manager

        self.game_map = game_map
        self.door = self.game_map.get_door()
        self.map_item = game_map.get_item()
        self.enemyList = enemies
        self.player = player

        self.bomb_list = self.player.get_list_bombs()
        self.explosion_list = []
        self.blocks_list = self.game_map.get_blocks_list()
        self.collision_manager = CollisionManager(self.player, self.enemyList, self.bomb_list, self.explosion_list,
                                                  self.blocks_list, self.map_item)

    def draw(self):
        self.game_map.draw(self.screenGame)
        self.player.draw(self.screenGame)

        for enemy in self.enemyList:
            if self.enemyList:
                enemy.draw(self.screenGame)

        for bomb in self.bomb_list:
            if self.bomb_list:
                bomb.draw(self.screenGame)

        if self.explosion_list:
            for explosion_part in self.explosion_list:
                explosion_part.draw(self.screenGame)

    def update(self, events):
        self.player.update(events)

        for enemy in self.enemyList:
            enemy.update(self.bomb_list)

        for explosion_part in self.explosion_list:
            explosion_part.update()

        self.game_map.update()

        self.remove_game_objects()
        self.collision_manager.check()


    def remove_game_objects(self):
        for bomb in self.bomb_list[:]:  # itera sobre uma cópia da lista
            bomb.update()
            self.explosion_list.extend(bomb.get_list_explosions())
            if bomb.get_is_exploded():
                self.bomb_list.remove(bomb)  # remove o elemento correto
                self.player.set_qtd_bombs(-1)

        for enemy in self.enemyList[:]:
            if enemy.get_is_dead() is True:
                self.enemyList.remove(enemy)
                if len(self.enemyList) == 0:
                    self.door.set_locked(False)

        for explosion_part in self.explosion_list[:]:
            explosion_part.update()
            if explosion_part.is_finished:
                self.explosion_list.remove(explosion_part)

        for block in self.blocks_list[:]:
            if block.get_is_destroyed():
                self.blocks_list.remove(block)

        if self.game_map.get_item() is not None and self.game_map.get_item().is_collected():
            self.game_map.remove_item()

    def is_stage_finished(self):
        if self.door.is_locked() is False:
            return True
        return False