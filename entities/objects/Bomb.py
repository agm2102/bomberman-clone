import pygame
from config.Settings import Settings
from entities.base_classes.BaseEntity import BaseEntity
from entities.objects.Explosion import Explosion
from systems.Animation import Animation

class Bomb(BaseEntity):

    def __init__(self, x, y, sprite_manager, game_map, range_explosion):
        super().__init__(x, y, sprite_manager)

        self.game_map = game_map
        self.rect = pygame.Rect(x, y, Settings.SPRITE_CHARACTER_OBJECTS_SIZE, Settings.SPRITE_CHARACTER_OBJECTS_SIZE)

        self._bomb_timer_limit = 180
        self._bomb_timer = 0
        self.has_detonator = False
        self._is_exploded = False
        self.range_explosion = range_explosion
        self._is_solid = False

        self.frames = self.sprite_manager.get("bomb")
        self.animation_controller.add_animation("idle_bomb", Animation(self.frames, 8, True))

        self.list_explosion = []


    def update(self):
        self.animation_controller.update()
        self.sprite = self.animation_controller.get_frame()

        if not self.has_detonator:
            self._bomb_timer += 1
            if self._bomb_timer >= self._bomb_timer_limit and not self._is_exploded:
                self._is_exploded = True
                self.create_explosion()

    def get_is_exploded(self):
        return self._is_exploded

    def explode_by_detonator(self):
        self._is_exploded = True
        self.create_explosion()

    def create_explosion(self):
        frames = self.sprite_manager.get("explosion")
        size = Settings.SPRITE_CHARACTER_OBJECTS_SIZE

        # core
        self.list_explosion.append(Explosion(self.x, self.y, "core", frames[0:7]))

        directions = [
            (0, -1, "middle_up", frames[14:21], "end_up", frames[42:49]),
            (0, 1, "middle_down", frames[14:21], "end_down", frames[21:28]),
            (1, 0, "middle_right", frames[7:14], "end_right", frames[35:42]),
            (-1, 0, "middle_left", frames[7:14], "end_left", frames[28:35]),
        ]

        for dx, dy, nome_middle, frames_middle, nome_end, frames_end in directions:
            for i in range(1, self.range_explosion + 1):
                tile_x = self.x + dx * size * i
                tile_y = self.y + dy * size * i
                tile_rect = pygame.Rect(tile_x, tile_y, size, size)

                if self.game_map.check_explosion_hit_blocks(tile_rect):
                    break  # bloco sólido — para essa direção

                if i == self.range_explosion:
                    self.create_explosion_part(tile_rect, nome_end, frames_end)
                else:
                    self.create_explosion_part(tile_rect, nome_middle, frames_middle)

    def create_explosion_part(self, rect, name, frames):
        explosion_part = Explosion(rect.x, rect.y, name, frames)
        self.list_explosion.append(explosion_part)

    def get_list_explosions(self):
        return self.list_explosion

    def get_is_solid(self):
        return self._is_solid

    def set_is_solid(self, is_solid):
        self._is_solid = is_solid

    def set_has_detonator(self, has_detonator):
        self.has_detonator = has_detonator