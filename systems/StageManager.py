import random

from config.Settings import Settings
from entities.characters.bomberman.Bomberman import Bomberman
from entities.characters.enemies.Ballom import Ballom
from entities.characters.enemies.Onil import Onil
from game_map.Map import Map
from systems.Stage import Stage

class CreateEnemies:
    def __init__(self, game_map, sprite_manager):
        self.sprite_manager = sprite_manager
        self.game_map = game_map
        self.enemies = []

    def ballom(self, qtd):
        ballom_list = []
        for i in range(qtd):
            position_x, position_y = random.choice(self.game_map.get_spawn_enemy_area())
            ballom_list.append(Ballom(
                    Settings.SPRITE_BLOCK_SIZE * position_x,
                    Settings.SPRITE_BLOCK_SIZE * position_y,
                    self.sprite_manager,
                    self.game_map,
                    True,
                    2))

        self.enemies.extend(ballom_list)

    def onil(self, qtd):
        onil_list = []
        for i in range(qtd):
            position_x, position_y = random.choice(self.game_map.get_spawn_enemy_area())
            onil_list.append(Onil(
                    Settings.SPRITE_BLOCK_SIZE * position_x,
                    Settings.SPRITE_BLOCK_SIZE * position_y,
                    self.sprite_manager,
                    self.game_map,
                    True,
                    3))

        self.enemies.extend(onil_list)

    def get_enemies(self):
        return self.enemies


class StageManager:

    def __init__(self, screen, sprite_manager):
        self.STAGES = {
            1: {"enemies": {"Ballom": 6}, "item": "fire"},
            2: {"enemies": {"Ballom": 3, "Onil": 3}, "item": "bomb"},
            3: {"enemies": {"Ballom": 2, "Onil": 2, "Dall": 2}, "item": "detonator"},
            4: {"enemies": {"Ballom": 1, "Onil": 1, "Dall": 2, "Minvo": 2}, "item": "skate"},
            5: {"enemies": {"Onil": 4, "Dall": 3}, "item": "bomb"},
            # BÔNUS
            6: {"enemies": {"Onil": 2, "Dall": 3, "Minvo": 2}, "item": "bomb"},
            7: {"enemies": {"Onil": 1, "Dall": 2, "Minvo": 3, "Kondoria": 1}, "item": "wall_pass"},
            8: {"enemies": {"Dall": 2, "Minvo": 2, "Kondoria": 2, "Ovapi": 1}, "item": "bomb_pass"},
            9: {"enemies": {"Dall": 1, "Minvo": 3, "Kondoria": 2, "Ovapi": 1}, "item": "fire"},
            10: {"enemies": {"Dall": 1, "Minvo": 2, "Kondoria": 2, "Ovapi": 2}, "item": "bomb"},
            # BÔNUS
            11: {"enemies": {"Minvo": 2, "Kondoria": 2, "Ovapi": 2, "Pass": 1}, "item": "skate"},
            12: {"enemies": {"Minvo": 1, "Kondoria": 2, "Ovapi": 2, "Pass": 2}, "item": "fire"},
            13: {"enemies": {"Minvo": 1, "Kondoria": 1, "Ovapi": 3, "Pass": 2}, "item": "bomb"},
            14: {"enemies": {"Kondoria": 2, "Ovapi": 2, "Pass": 3}, "item": "wall_pass"},
            15: {"enemies": {"Kondoria": 1, "Ovapi": 2, "Pass": 3, "Doria": 1}, "item": "bomb_pass"},
            # BÔNUS
            16: {"enemies": {"Kondoria": 1, "Ovapi": 2, "Pass": 3, "Doria": 1}, "item": "fire"},
            17: {"enemies": {"Ovapi": 2, "Pass": 3, "Doria": 2}, "item": "bomb"},
            18: {"enemies": {"Ovapi": 1, "Pass": 3, "Doria": 3}, "item": "bomb"},
            19: {"enemies": {"Ovapi": 1, "Pass": 3, "Doria": 3}, "item": "fire"},
            20: {"enemies": {"Pass": 3, "Doria": 4}, "item": "mystery"},
            # BÔNUS
            21: {"enemies": {"Dall": 1, "Pass": 3, "Doria": 3}, "item": "bomb"},
            22: {"enemies": {"Dall": 1, "Minvo": 1, "Pass": 3, "Doria": 3}, "item": "wall_pass"},
            23: {"enemies": {"Dall": 1, "Minvo": 1, "Pass": 4, "Doria": 2}, "item": "bomb_pass"},
            24: {"enemies": {"Dall": 2, "Minvo": 1, "Pass": 4, "Doria": 2}, "item": "fire"},
            25: {"enemies": {"Dall": 2, "Minvo": 2, "Pass": 3, "Doria": 2}, "item": "bomb"},
            # BÔNUS
            26: {"enemies": {"Dall": 2, "Minvo": 2, "Pass": 3, "Doria": 2}, "item": "detonator"},
            27: {"enemies": {"Dall": 2, "Minvo": 2, "Pass": 3, "Doria": 2}, "item": "mystery"},
            28: {"enemies": {"Dall": 2, "Minvo": 2, "Pass": 3, "Doria": 2}, "item": "bomb_pass"},
            29: {"enemies": {"Dall": 2, "Minvo": 2, "Pass": 3, "Doria": 2}, "item": "fire"},
            30: {"enemies": {"Dall": 2, "Minvo": 2, "Pass": 3, "Doria": 3}, "item": "bomb"},
            # BÔNUS
            31: {"enemies": {"Dall": 2, "Minvo": 2, "Ovapi": 1, "Doria": 3, "Pass": 2}, "item": "skate"},
            32: {"enemies": {"Dall": 2, "Minvo": 2, "Ovapi": 1, "Doria": 3, "Pass": 2}, "item": "fire"},
            33: {"enemies": {"Dall": 2, "Minvo": 2, "Ovapi": 1, "Doria": 3, "Pass": 2}, "item": "detonator"},
            34: {"enemies": {"Dall": 2, "Minvo": 3, "Doria": 3, "Pass": 2}, "item": "mystery"},
            35: {"enemies": {"Dall": 2, "Minvo": 1, "Ovapi": 1, "Doria": 3, "Pass": 2}, "item": "bomb_pass"},
            # BÔNUS
            36: {"enemies": {"Dall": 2, "Minvo": 2, "Doria": 3, "Pass": 3}, "item": "flame_pass"},
            37: {"enemies": {"Dall": 2, "Minvo": 1, "Ovapi": 1, "Doria": 3, "Pass": 3}, "item": "detonator"},
            38: {"enemies": {"Dall": 2, "Minvo": 2, "Doria": 3, "Pass": 3}, "item": "fire"},
            39: {"enemies": {"Dall": 1, "Minvo": 1, "Ovapi": 2, "Doria": 2, "Pass": 4}, "item": "wall_pass"},
            40: {"enemies": {"Dall": 1, "Minvo": 2, "Doria": 3, "Pass": 4}, "item": "mystery"},
            # BÔNUS
            41: {"enemies": {"Dall": 1, "Minvo": 1, "Ovapi": 1, "Doria": 3, "Pass": 4}, "item": "detonator"},
            42: {"enemies": {"Minvo": 1, "Ovapi": 1, "Doria": 3, "Pass": 5}, "item": "wall_pass"},
            43: {"enemies": {"Minvo": 1, "Ovapi": 1, "Doria": 2, "Pass": 6}, "item": "bomb_pass"},
            44: {"enemies": {"Minvo": 1, "Ovapi": 1, "Doria": 2, "Pass": 6}, "item": "detonator"},
            45: {"enemies": {"Ovapi": 2, "Doria": 2, "Pass": 6}, "item": "mystery"},
            # BÔNUS
            46: {"enemies": {"Ovapi": 2, "Doria": 2, "Pass": 6}, "item": "wall_pass"},
            47: {"enemies": {"Ovapi": 2, "Doria": 2, "Pass": 6}, "item": "bomb_pass"},
            48: {"enemies": {"Ovapi": 1, "Doria": 2, "Pass": 6, "Pontan": 1}, "item": "detonator"},
            49: {"enemies": {"Ovapi": 2, "Doria": 1, "Pass": 6, "Pontan": 1}, "item": "flame_pass"},
            50: {"enemies": {"Doria": 2, "Pass": 6, "Pontan": 2}, "item": "flame_pass"},
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

        self.screen = screen
        self.sprite_manager = sprite_manager

        self.game_map = Map(self.sprite_manager)
        self.player = Bomberman(Settings.SPRITE_BLOCK_SIZE * 1,Settings.SPRITE_BLOCK_SIZE * 1 + Settings.HUD_HEIGHT, True, sprite_manager, self.game_map, 3, 1)

        self.enemies = CreateEnemies(self.game_map, sprite_manager)


        self.stage = None

        self.create_stage()

    def get_stage(self):
        return self.stage

    def draw(self):
        self.stage.draw()

    def update(self, events):
        self.stage.update(events)

    def create_stage(self):
        stage_number = 2

        self.game_map.spawn_item_on_map(self.type_item[self.STAGES[stage_number]["item"]])

        if "Ballom" in self.STAGES[stage_number]["enemies"]:
            self.enemies.ballom(self.STAGES[stage_number]["enemies"]["Ballom"])
        if "Onil" in self.STAGES[stage_number]["enemies"]:
            self.enemies.onil(self.STAGES[stage_number]["enemies"]["Onil"])

        self.stage = Stage(self.screen, self.sprite_manager, self.player, self.enemies.get_enemies(), self.game_map)
