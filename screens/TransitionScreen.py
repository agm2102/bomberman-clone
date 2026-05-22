from config.Settings import Settings
from screens.HUD import _number_to_indices


class TransitionScreen:
    def __init__(self, screen, sprite_manager):
        self.stage_number = 1
        self.number_sprites = sprite_manager.get("numbers_hud")
        self.letter_sprites = sprite_manager.get("letters_hud")

        self.timer = 0
        self.duration = 120  # 2 segundos a 60fps
        self.finished = False

        self.stage = []
        self.PRETO = (0, 0, 0)
        self.screen = screen

        self.espacamento = Settings.NUMBER_LETTER_SIZE_WIDTH

        self.create_hud_content()

    def draw(self):
        self.screen.fill(self.PRETO)
        self.screen.blits(self.stage)

    def update(self):
        self.timer += 1
        if self.timer >= self.duration:
            self.timer = 0
            self.finished = True

    def is_finished(self):
        return self.finished

    def set_stage_number(self, stage_number):
        self.stage_number = stage_number

    def reset(self):
        self.timer = 0
        self.finished = False
        self.create_hud_content()

    def _build_row(self, label_indices, value_indices, x, y):

        sprites = []

        for i, idx in enumerate(label_indices):
            sprites.append((self.letter_sprites[idx], (x + i * self.espacamento, y)))

        offset = len(label_indices) + 1
        for i, idx in enumerate(value_indices):
            sprites.append((self.number_sprites[idx], (x + (offset + i) * self.espacamento, y)))

        return sprites

    def create_hud_content(self):
        self.espacamento = Settings.NUMBER_LETTER_SIZE_WIDTH
        letter_h = Settings.NUMBER_LETTER_SIZE_HEIGHT
        y = Settings.SCREEN_HEIGHT // 2 - letter_h // 2

        indices_stage  = [18, 19, 0, 6, 4]

        digits = 1 if self.stage_number < 10 else 2
        stage_digits = _number_to_indices(self.stage_number, digits)

        total_stage = (len(indices_stage) + 1 + len(stage_digits)) * self.espacamento

        padding = self.espacamento * 2
        total_width = total_stage
        x_start = (Settings.SCREEN_WIDTH - total_width) // 2

        x_stage  = x_start

        self.stage  = self._build_row(indices_stage,  stage_digits,  x_stage,  y)
