import pygame

from config.Settings import Settings
from entities.base_classes.BaseEntity import BaseEntity
from systems.Animation import Animation

class Explosion(BaseEntity):
    def __init__(self, x, y, explosion_part, frames):
        super().__init__(x, y, sprite_manager=None)
        self.margem = 4
        self.is_finished = False
        self.explosion_part = explosion_part  # ← guarda o tipo
        self.x = x
        self.y = y
        self.animation_controller.add_animation(explosion_part, Animation(frames, 7, False))

    def get_rect(self):
        s = Settings.SPRITE_SIZE
        m = self.margem  # margem normal
        me = m + 6# margem maior na extremidade oposta ao core

        if self.explosion_part in ["middle_right", "end_right"]:
            return pygame.Rect(self.x + m, self.y + m, s - m - me, s - m * 2)

        elif self.explosion_part in ["middle_left", "end_left"]:
            return pygame.Rect(self.x + me, self.y + m, s - m - me, s - m * 2)

        elif self.explosion_part in ["middle_down", "end_down"]:
            return pygame.Rect(self.x + m, self.y + m, s - m * 2, s - m - me)

        elif self.explosion_part in ["middle_up", "end_up"]:
            return pygame.Rect(self.x + m, self.y + me, s - m * 2, s - m - me)

        else:  # core
            return pygame.Rect(self.x + m, self.y + m, s - m * 2, s - m * 2)
    def update(self):
        self.animation_controller.update()
        self.sprite = self.animation_controller.get_frame()

        if self.animation_controller.finished():
            self.is_finished = True

    def draw(self, screen, camera=None):
        super().draw(screen, camera)
