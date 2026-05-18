import random

from config.Settings import Settings
from entities.characters.bomberman.Bomberman import Bomberman
from entities.characters.enemies.Ballom import Ballom
from entities.characters.enemies.Dahl import Dahl
from entities.characters.enemies.Doria import Doria
from entities.characters.enemies.Minvo import Minvo
from entities.characters.enemies.Onil import Onil
from entities.characters.enemies.Ovape import Ovape
from entities.characters.enemies.Pass import Pass
from entities.characters.enemies.Pontan import Pontan
from game_map.Map import Map
from systems.Camera import Camera
from systems.Stage import Stage

class StageManager:

    def __init__(self, screen, sprite_manager, hud):
        self.stage_number = None
        self.HUD = hud
        self.STAGES = {
            1: {"enemies": {"Ballom": 6}, "item": "fire"},
            2: {"enemies": {"Ballom": 3, "Onil": 3}, "item": "bomb"},
            3: {"enemies": {"Ballom": 2, "Onil": 2, "Dahl": 2}, "item": "detonator"},
            4: {"enemies": {"Ballom": 1, "Onil": 1, "Dahl": 2, "Minvo": 2}, "item": "skate"},
            5: {"enemies": {"Onil": 4, "Dahl": 3}, "item": "bomb"},
            # BÔNUS
            6: {"enemies": {"Onil": 2, "Dahl": 3, "Minvo": 2}, "item": "bomb"},
            7: {"enemies": {"Onil": 1, "Dahl": 2, "Minvo": 3, "Doria": 1}, "item": "wall_pass"},
            8: {"enemies": {"Dahl": 2, "Minvo": 2, "Doria": 2, "Ovape": 1}, "item": "bomb_pass"},
            9: {"enemies": {"Dahl": 1, "Minvo": 3, "Doria": 2, "Ovape": 1}, "item": "fire"},
            10: {"enemies": {"Dahl": 1, "Minvo": 2, "Doria": 2, "Ovape": 2}, "item": "bomb"},
            # BÔNUS
            11: {"enemies": {"Minvo": 2, "Doria": 2, "Ovape": 2, "Pass": 1}, "item": "skate"},
            12: {"enemies": {"Minvo": 1, "Doria": 2, "Ovape": 2, "Pass": 2}, "item": "fire"},
            13: {"enemies": {"Minvo": 1, "Doria": 1, "Ovape": 3, "Pass": 2}, "item": "bomb"},
            14: {"enemies": {"Doria": 2, "Ovape": 2, "Pass": 3}, "item": "wall_pass"},
            15: {"enemies": {"Doria": 1, "Ovape": 2, "Pass": 3, "Pontan": 1}, "item": "bomb_pass"},
            # BÔNUS
            16: {"enemies": {"Doria": 1, "Ovape": 2, "Pass": 3, "Pontan": 1}, "item": "fire"},
            17: {"enemies": {"Ovape": 2, "Pass": 3, "Pontan": 2}, "item": "bomb"},
            18: {"enemies": {"Ovape": 1, "Pass": 3, "Pontan": 3}, "item": "bomb"},
            19: {"enemies": {"Ovape": 1, "Pass": 3, "Pontan": 3}, "item": "fire"},
            20: {"enemies": {"Pass": 3, "Pontan": 4}, "item": "mystery"},
            # BÔNUS
            21: {"enemies": {"Dahl": 1, "Pass": 3, "Pontan": 3}, "item": "bomb"},
            22: {"enemies": {"Dahl": 1, "Minvo": 1, "Pass": 3, "Pontan": 3}, "item": "wall_pass"},
            23: {"enemies": {"Dahl": 1, "Minvo": 1, "Pass": 4, "Pontan": 2}, "item": "bomb_pass"},
            24: {"enemies": {"Dahl": 2, "Minvo": 1, "Pass": 4, "Pontan": 2}, "item": "fire"},
            25: {"enemies": {"Dahl": 2, "Minvo": 2, "Pass": 3, "Pontan": 2}, "item": "bomb"},
            # BÔNUS
            26: {"enemies": {"Dahl": 2, "Minvo": 2, "Pass": 3, "Pontan": 2}, "item": "detonator"},
            27: {"enemies": {"Dahl": 2, "Minvo": 2, "Pass": 3, "Pontan": 2}, "item": "mystery"},
            28: {"enemies": {"Dahl": 2, "Minvo": 2, "Pass": 3, "Pontan": 2}, "item": "bomb_pass"},
            29: {"enemies": {"Dahl": 2, "Minvo": 2, "Pass": 3, "Pontan": 2}, "item": "fire"},
            30: {"enemies": {"Dahl": 2, "Minvo": 2, "Pass": 3, "Pontan": 3}, "item": "bomb"},
            # BÔNUS
            31: {"enemies": {"Dahl": 2, "Minvo": 2, "Ovape": 1, "Pontan": 3, "Pass": 2}, "item": "skate"},
            32: {"enemies": {"Dahl": 2, "Minvo": 2, "Ovape": 1, "Pontan": 3, "Pass": 2}, "item": "fire"},
            33: {"enemies": {"Dahl": 2, "Minvo": 2, "Ovape": 1, "Pontan": 3, "Pass": 2}, "item": "detonator"},
            34: {"enemies": {"Dahl": 2, "Minvo": 3, "Pontan": 3, "Pass": 2}, "item": "mystery"},
            35: {"enemies": {"Dahl": 2, "Minvo": 1, "Ovape": 1, "Pontan": 3, "Pass": 2}, "item": "bomb_pass"},
            # BÔNUS
            36: {"enemies": {"Dahl": 2, "Minvo": 2, "Pontan": 3, "Pass": 3}, "item": "flame_pass"},
            37: {"enemies": {"Dahl": 2, "Minvo": 1, "Ovape": 1, "Pontan": 3, "Pass": 3}, "item": "detonator"},
            38: {"enemies": {"Dahl": 2, "Minvo": 2, "Pontan": 3, "Pass": 3}, "item": "fire"},
            39: {"enemies": {"Dahl": 1, "Minvo": 1, "Ovape": 2, "Pontan": 2, "Pass": 4}, "item": "wall_pass"},
            40: {"enemies": {"Dahl": 1, "Minvo": 2, "Pontan": 3, "Pass": 4}, "item": "mystery"},
            # BÔNUS
            41: {"enemies": {"Dahl": 1, "Minvo": 1, "Ovape": 1, "Pontan": 3, "Pass": 4}, "item": "detonator"},
            42: {"enemies": {"Minvo": 1, "Ovape": 1, "Pontan": 3, "Pass": 5}, "item": "wall_pass"},
            43: {"enemies": {"Minvo": 1, "Ovape": 1, "Pontan": 2, "Pass": 6}, "item": "bomb_pass"},
            44: {"enemies": {"Minvo": 1, "Ovape": 1, "Pontan": 2, "Pass": 6}, "item": "detonator"},
            45: {"enemies": {"Ovape": 2, "Pontan": 2, "Pass": 6}, "item": "mystery"},
            # BÔNUS
            46: {"enemies": {"Ovape": 2, "Pontan": 2, "Pass": 6}, "item": "wall_pass"},
            47: {"enemies": {"Ovape": 2, "Pontan": 2, "Pass": 6}, "item": "bomb_pass"},
            48: {"enemies": {"Ovape": 1, "Pontan": 2, "Pass": 6, "Pontan": 1}, "item": "detonator"},
            49: {"enemies": {"Ovape": 2, "Pontan": 1, "Pass": 6, "Pontan": 1}, "item": "flame_pass"},
            50: {"enemies": {"Pontan": 2, "Pass": 6, "Pontan": 2}, "item": "flame_pass"},
        }

        self.BONUS_STAGES = {6, 11, 16, 21, 26, 31, 36, 41, 46}  # após cada fase múltipla de 5

        self.type_item = {
            "bomb": 0,
            "fire": 1,
            "skate": 2,
            "wall_pass": 3,
            "detonator": 4,
            "bomb_pass": 5,
            "flame_pass": 6,
            "mystery": 7
        }
        self.camera = Camera()
        self.screen = screen
        self.sprite_manager = sprite_manager

        self.stage = None
        self.game_map = None
        self.player = None
        self.enemies = []

        self.create_stage()

    def get_stage(self):
        return self.stage

    def draw(self):
        self.stage.draw()

    def update(self, events):
        self.stage.update(events)
        self.camera.update(self.player)

    def get_player_lives(self):
        return self.player.get_lives()

    def get_stage_timer(self):
        return self.stage.get_timer()

    def create_stage(self):
        self.stage_number = 10
        self.game_map = Map(self.sprite_manager)
        self.game_map.spawn_item_on_map(self.type_item[str(self.STAGES[self.stage_number]["item"])])
        self.generate_enemies(self.stage_number)
        self.player = Bomberman(Settings.SPRITE_SIZE * 1, Settings.SPRITE_SIZE * 1 + Settings.HUD_HEIGHT, True, self.sprite_manager, self.game_map, 3)
        self.stage = Stage(self.screen, self.sprite_manager,self.player, self.enemies, self.game_map, self.camera)

    def generate_enemies(self, stage_number):
        ENEMY_CLASS = {
            "Ballom" : Ballom,
            "Onil" : Onil,
            "Dahl" : Dahl,
            "Minvo" : Minvo,
            "Doria": Doria,
            "Ovape": Ovape,
            "Pass": Pass,
            "Pontan": Pontan,
        }
        for enemy_type in self.STAGES[stage_number]["enemies"]:
            qtd_enemies = self.STAGES[stage_number]["enemies"][enemy_type]
            for i in range(int(qtd_enemies)):
                pos = random.choice(self.game_map.get_spawn_enemy_area())
                x, y = pos[0] * Settings.SPRITE_SIZE, pos[1] * Settings.SPRITE_SIZE
                enemy_class = ENEMY_CLASS[enemy_type]
                enemy = enemy_class(x, y, self.sprite_manager, self.game_map, True, enemy_type)

                self.enemies.append(enemy)


