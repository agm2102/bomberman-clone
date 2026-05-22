import pygame

from config.Settings import Settings
from entities.base_classes.BaseEntity import BaseEntity

class BaseCharacter(BaseEntity):
    def  __init__(self, x, y, game_map, sprite_manager, is_alive):
        super().__init__(x, y, sprite_manager)
        self.bombs_list = []
        self.game_map = game_map
        self.dir = None
        self.rect = pygame.Rect(self.x, self.y, Settings.SPRITE_SIZE, Settings.SPRITE_SIZE)
        self.is_alive = is_alive
        self.is_dead = False
        self.wall_pass = False

        self.directions = {
            "UP": (0, -1),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0),
            "IDLE": (0, 0)
        }

    def align_axis(self, direction):
        size = Settings.SPRITE_SIZE

        if direction in ["LEFT", "RIGHT"]:
            self.y = round(self.y / size) * size

        elif direction in ["UP", "DOWN"]:
            self.x = round(self.x / size) * size

    def _check_collision_characters_bombs(self):
        for bomb in self.bombs_list:
            if bomb.get_is_solid() is False and bomb.get_rect().colliderect(self.get_rect()) is False:
               bomb.set_is_solid(True)

    def death(self):
        self.is_alive = False

    def get_rect(self):
        self.rect = pygame.Rect(self.x, self.y, Settings.SPRITE_SIZE, Settings.SPRITE_SIZE)
        return self.rect

    def get_is_dead(self):
        return self.is_dead

    def get_is_alive(self):
        return  self.is_alive

