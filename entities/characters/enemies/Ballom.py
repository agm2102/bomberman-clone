from entities.base_classes.BaseEnemy import BaseEnemy
from systems.Animation import Animation

class Ballom(BaseEnemy):
    def __init__(self, x, y, sprite_manager, game_map, is_alive, speed):
        super().__init__(x, y, sprite_manager, game_map, is_alive, speed)

        frames = sprite_manager.get("ballom")


        self.animation_controller.add_animation("right_walk", Animation(frames[0:3], self.animation_speed, True))
        self.animation_controller.add_animation("left_walk", Animation(frames[3:6], self.animation_speed, True))
        self.animation_controller.add_animation("up_walk", Animation(frames[3:6], self.animation_speed, True))
        self.animation_controller.add_animation("down_walk", Animation(frames[0:3], self.animation_speed, True))
        self.animation_controller.add_animation("death", Animation(frames[6:11], self.animation_speed * 3, False))
