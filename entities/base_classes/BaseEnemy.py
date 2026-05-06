import random
from entities.base_classes.BaseCharacter import BaseCharacter

class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, sprite_manager, game_map, is_alive, speed):
        super().__init__(x, y, game_map, sprite_manager, is_alive, speed)

        self.speed = speed
        self.dir = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.animation_speed = 25

    def update(self, bombs_list):
        self._check_collision_characters_bombs()

        if not self.is_alive:
            self.animation_controller.change_current_animation("death", False)
            if self.animation_controller.finished():
                self.is_dead = True
                return

        self.align_axis(self.dir)

        # tenta andar
        if self.dir:
            self.move(self.dir, bombs_list)

        self.animation_controller.update()
        self.sprite = self.animation_controller.get_frame()

        if self.dir is not None or not self.is_alive:
            self.animation_controller.update()

    def move(self, direction, bombs_list = None):
        if not self.is_alive: return

        dx, dy = self.directions[direction]

        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        if not self._game_map.is_walkable_position(new_x, new_y, bombs_list):

            self.dir = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

            if self.dir == "LEFT":
                self.animation_controller.change_current_animation("left_walk", False)
            elif self.dir == "RIGHT":
                self.animation_controller.change_current_animation("right_walk", False)
            elif self.dir == "UP":
                self.animation_controller.change_current_animation("up_walk", False)
            elif self.dir == "DOWN":
                self.animation_controller.change_current_animation("down_walk", False)
        else:
            self.x = new_x
            self.y = new_y
