import pygame

from config.Settings import Settings
from systems.AnimationController import AnimationController

class BaseEntity:
    def __init__(self, x, y, sprite_manager):
        self.rect = None
        self.x = x
        self.y = y

        self.animation_controller = AnimationController()
        self.sprite_manager = sprite_manager
        self.sprite = None

    def draw(self, screen, camera=None):
        pos = camera.apply(self) if camera else (self.x, self.y)
        screen.blit(self.sprite, pos)

    def get_rect(self):
        self.rect = pygame.Rect(self.x, self.y, Settings.SPRITE_SIZE, Settings.SPRITE_SIZE)
        return self.rect