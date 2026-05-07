from config.Settings import Settings


class Camera:
    def __init__(self):
        self.offset_x = 0

    def update(self, player):
        self.offset_x = player.x - Settings.SCREEN_WIDTH // 2
        self.offset_x = max(0, self.offset_x)
        self.offset_x = min(self.offset_x, (Settings.MAP_COLS * Settings.SPRITE_BLOCK_SIZE) - Settings.SCREEN_WIDTH)

    def apply(self, objeto):
        return objeto.x - self.offset_x, objeto.y