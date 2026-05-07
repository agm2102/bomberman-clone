from config.Settings import Settings
from entities.base_classes.BaseEntity import BaseEntity
from entities.objects.Bomb import Bomb
from game_map.Block import Block
import random
import  pygame

from game_map.Door import Door
from game_map.Item import Item


def bomberman_is_spawn_area(i, j):
    # player (canto superior esquerdo)
    if i < 3 and j < 3:
        return True
    return False

def enemies_is_spawn_area(i, j):
    # inimigos (metade direita, faixa central)
    if 20 <= j <= 28 and 5 <= i <= 8:
        return True
    return False


class Map:

    def __init__(self, sprite_manager):
        BLOCK_SOLID = 0
        BLOCK_DESTRUCTIBLE = 2
        GROUND = 1

        self.has_door = False
        self.door = None

        self.has_item = False
        self.item = None

        self.spawn_enemy_area_list = []
        self.sprite_manager = sprite_manager
        self.blocks_list = []
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                if self.mapa[i][j] == 1:
                    block = Block( j * Settings.SPRITE_BLOCK_SIZE, Settings.HUD_HEIGHT + i * Settings.SPRITE_BLOCK_SIZE,
                                  sprite_manager.get("map")[BLOCK_SOLID], True, False, sprite_manager)
                    self.blocks_list.append(block)

                elif self.mapa[i][j] == 0:
                    # Sempre desenha o chão
                    block = Block(j * Settings.SPRITE_BLOCK_SIZE, Settings.HUD_HEIGHT + i * Settings.SPRITE_BLOCK_SIZE,
                                  sprite_manager.get("map")[GROUND], False, False, sprite_manager)
                    self.blocks_list.append(block)

                    if (not (bomberman_is_spawn_area(i, j) or enemies_is_spawn_area(i, j))) and random.random() > 0.9:
                        block = Block(j * Settings.SPRITE_BLOCK_SIZE, Settings.HUD_HEIGHT + i * Settings.SPRITE_BLOCK_SIZE,
                                      sprite_manager.get("map")[BLOCK_DESTRUCTIBLE], True, True, sprite_manager)
                        self.blocks_list.append(block)

                    if enemies_is_spawn_area(i, j):
                        span_enemy_area = (j, i)
                        self.spawn_enemy_area_list.append(span_enemy_area)

        self.create_door()

    def is_walkable_position(self, x, y, bomb_list):
        size_character = Settings.SPRITE_CHARACTER_OBJECTS_SIZE
        character_rect = pygame.Rect(x, y, size_character, size_character)

        for block in self.blocks_list:
            if block.is_solid():

                block_rect = block.get_rect()
                if block_rect.colliderect(character_rect):
                    return False

        if bomb_list:
            for bomb in bomb_list:
                if bomb.get_is_solid():
                    if bomb.get_rect().colliderect(character_rect):
                        return False
        return True

    def get_random_breakable_block(self):
        breakable_blocks_list = []
        for block in self.blocks_list:
            if block.is_solid() and block.is_breakable():
                breakable_blocks_list.append(block)

        return breakable_blocks_list[random.randint(0, len(breakable_blocks_list) - 1)]

    def create_door(self):
        block = self.get_random_breakable_block()
        if not self.has_door:
            self.has_door = True
            self.door = Door(block.x, block.y, self.sprite_manager)
            block.set_door(self.door)

    def spawn_item_on_map(self, type_item):

        block = self.get_random_breakable_block()
        if not self.has_item and block.get_door() is None:
            self.has_item = True
            self.item = Item(block.x, block.y, self.sprite_manager, type_item)
            block.item = self.item

    def check_explosion_hit_blocks(self, rect):
        for block in self.blocks_list:
            if block.is_solid() and block.get_rect().colliderect(rect):
                if block.is_breakable():
                    block.set_destroy()
                return True
        return False

    def draw(self, screen, camera=None):
        for block in self.blocks_list:
            block.draw(screen, camera)

        if self.door is not None and self.door.is_visible():
            self.door.draw(screen, camera)

        if self.item is not None and self.item.is_visible():
            self.item.draw(screen, camera)

    def update(self):
        for block in self.blocks_list:
            block.update()

    def get_spawn_enemy_area(self):
        return self.spawn_enemy_area_list

    def get_blocks_list(self):
        return self.blocks_list

    def get_item(self):
        return  self.item

    def remove_item(self):
        self.item = None

    def get_door(self):
        return self.door