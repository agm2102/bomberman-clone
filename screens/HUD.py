import pygame
from config.Settings import Settings


class Hud:

    def __init__(self, screen, time, score, left_lifes, sprite_manager):
        self.screen = screen
        self.GRAY = (171, 171, 171)
        self.sprites = sprite_manager.get("letters_hud")

        self.hud_time = []
        self.hud_score = []
        self.hud_left_lifes = []

        self.hud = pygame.Rect(0, 0, Settings.SCREEN_WIDTH, Settings.HUD_HEIGHT)

        self.create_hud_content()  # ✅ chama aqui

    def draw(self):
        self.screen.fill(self.GRAY, self.hud)
        self.screen.blits(self.hud_time)
        self.screen.blits(self.hud_score)
        self.screen.blits(self.hud_left_lifes)

    def create_hud_content(self):
        espacamento = Settings.NUMBER_LETTER_SIZE_WIDTH
        y = 56  # centralizado verticalmente (128 / 2 - 8)

        indices_time = [19, 8, 12, 4]  # TIME  — 4 letras = 128px
        indices_score = [18, 2, 14, 17, 4]  # SCORE — 5 letras = 160px
        indices_left = [11, 4, 5, 19]  # LEFT  — 4 letras = 128px

        x_time = 170 - 120  # centro da seção 1 (170) - metade de 128
        x_score = 512 - 80  # centro da tela   (512) - metade de 160
        x_left = 853 - 64  # centro da seção 3 (853) - metade de 128

        for i, idx in enumerate(indices_time):
            self.hud_time.append((self.sprites[idx], (x_time + i * espacamento, y)))

        for i, idx in enumerate(indices_score):
            self.hud_score.append((self.sprites[idx], (x_score + i * espacamento, y)))

        for i, idx in enumerate(indices_left):
            self.hud_left_lifes.append((self.sprites[idx], (x_left + i * espacamento, y)))