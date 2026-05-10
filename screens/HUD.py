import pygame
from config.Settings import Settings


def _number_to_indices(value, digits):
    formatted = str(value).zfill(digits)
    return [int(d) for d in formatted]


class Hud:

    def __init__(self, screen, sprite_manager):
        self.number_sprites = sprite_manager.get("numbers_hud")
        self.letter_sprites = sprite_manager.get("letters_hud")

        self.time = 200
        self.score = 0
        self.left = 0

        self.screen = screen
        self.GRAY = (171, 171, 171)

        self.hud_time = []
        self.hud_score = []
        self.hud_left_lifes = []

        self.hud = pygame.Rect(0, 0, Settings.SCREEN_WIDTH, Settings.HUD_HEIGHT)

        self.create_hud_content()

    def draw(self):
        self.screen.fill(self.GRAY, self.hud)
        self.screen.blits(self.hud_time)
        self.screen.blits(self.hud_score)
        self.screen.blits(self.hud_left_lifes)

    def _build_row(self, label_indices, value_indices, x, y):
        espacamento = Settings.NUMBER_LETTER_SIZE_WIDTH
        sprites = []

        for i, idx in enumerate(label_indices):
            sprites.append((self.letter_sprites[idx], (x + i * espacamento, y)))

        offset = len(label_indices) + 1
        for i, idx in enumerate(value_indices):
            sprites.append((self.number_sprites[idx], (x + (offset + i) * espacamento, y)))

        return sprites

    def create_hud_content(self):
        espacamento = Settings.NUMBER_LETTER_SIZE_WIDTH
        letter_h = Settings.NUMBER_LETTER_SIZE_HEIGHT
        y = Settings.HUD_HEIGHT // 2 - letter_h // 2

        indices_time  = [19, 8, 12, 4]
        indices_score = [18, 2, 14, 17, 4]
        indices_left  = [11, 4, 5, 19]

        time_digits  = _number_to_indices(self.time,  3)
        score_digits = _number_to_indices(self.score, 6)
        left_digits  = _number_to_indices(self.left,  1)

        total_time  = (len(indices_time)  + 1 + len(time_digits))  * espacamento
        total_score = (len(indices_score) + 1 + len(score_digits)) * espacamento
        total_left  = (len(indices_left)  + 1 + len(left_digits))  * espacamento

        padding = espacamento * 1
        total_width = total_time + total_score + total_left + padding * 2
        x_start = (Settings.SCREEN_WIDTH - total_width) // 2

        x_time  = x_start
        x_score = x_time  + total_time  + padding
        x_left  = x_score + total_score + padding

        self.hud_time       = self._build_row(indices_time,  time_digits,  x_time,  y)
        self.hud_score      = self._build_row(indices_score, score_digits, x_score, y)
        self.hud_left_lifes = self._build_row(indices_left,  left_digits,  x_left,  y)

    def _refresh_values(self):
        self.create_hud_content()

    def set_time(self, time):
        self.time = time
        self._refresh_values()

    def set_score(self, score):
        self.score = score
        self._refresh_values()

    def set_left(self, left):
        self.left = left
        self._refresh_values()