import pygame
from config.Settings import Settings
from entities.base_classes.BaseEntity import BaseEntity
from systems.Animation import Animation

class Explosion(BaseEntity):
    def __init__(self, x, y, explosion_part, frames):
        super().__init__(x, y, sprite_manager=None)
        self.is_finished = False
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, Settings.SPRITE_CHARACTER_OBJECTS_SIZE, Settings.SPRITE_CHARACTER_OBJECTS_SIZE)
        self.animation_controller.add_animation(explosion_part, Animation(frames, 7, False))

    def update(self):
        self.animation_controller.update()
        self.sprite = self.animation_controller.get_frame()

        if self.animation_controller.finished():
            self.is_finished = True