from entities.base_classes.Enemy import Enemy
from systems.Animation import Animation


class Pontan(Enemy):
    def __init__(self, x, y, sprite_manager, game_map, is_alive, enemy_name):
        super().__init__(x, y, sprite_manager, game_map, is_alive, enemy_name)

        self.speed = 4
        self.wall_pass = True

        self.animation_controller.add_animation("right_walk", Animation(self.frames[0:4], self.animation_speed, True))
        self.animation_controller.add_animation("left_walk", Animation(self.frames[0:4], self.animation_speed, True))
        self.animation_controller.add_animation("up_walk", Animation(self.frames[0:4], self.animation_speed, True))
        self.animation_controller.add_animation("down_walk", Animation(self.frames[0:4], self.animation_speed, True))
        self.animation_controller.add_animation("death", Animation(self.frames[4:9], self.animation_speed * 3, False))
