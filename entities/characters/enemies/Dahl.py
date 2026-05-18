from entities.base_classes.Enemy import Enemy


class Dahl(Enemy):
    def __init__(self, x, y, sprite_manager, game_map, is_alive, enemy_name):
        super().__init__(x, y, sprite_manager, game_map, is_alive, enemy_name)
        self.speed = 3