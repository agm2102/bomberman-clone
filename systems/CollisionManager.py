
class CollisionManager:
    def __init__(self, bomberman, enemies_list, bombs_list, explosion_list, blocks_list, item):

        self.bombs_list = bombs_list
        self.explosion_list = explosion_list
        self.blocks_list = blocks_list
        self.item = item
        self.bomberman = bomberman
        self.enemies_list = enemies_list


    def _check_collision_player_enemies(self):
        for enemy in self.enemies_list:
            if enemy.get_is_alive():
                if self.bomberman.get_rect().colliderect(enemy.get_rect()):
                    self.bomberman.death()
                    break


    def _check_collision_explosion_enemies_player(self):
        for explosion_part in self.explosion_list:
            if self.bomberman.get_rect().colliderect(explosion_part.get_rect()) and self.bomberman.flame_pass is False:
                self.bomberman.death()
            for enemy in self.enemies_list:
                if explosion_part.get_rect().colliderect(enemy.get_rect()):
                    enemy.death()

    def _check_collision_player_item(self):
        if self.item is not None and not self.item.is_collected() :
            if self.bomberman.get_rect().colliderect(self.item.get_rect()):
                self.bomberman.apply_item_effect(self.item.get_type())
                self.item.set_collected(True)

    def check(self):
        self._check_collision_player_enemies()
        self._check_collision_explosion_enemies_player()
        self._check_collision_player_item()

