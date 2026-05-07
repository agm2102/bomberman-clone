from screens.HUD import Hud
from systems.StageManager import StageManager

class GameScreen:

    def __init__(self, screen, sprite_manager):
        self.sprite_manager = sprite_manager
        self.screen = screen
        self.hud = Hud(self.screen, self.sprite_manager)
        self.stage_manager = StageManager(screen, sprite_manager, self.hud)

    def draw(self):
        self.hud.draw()
        self.stage_manager.draw()

    def update(self, events):
        self.stage_manager.update(events)