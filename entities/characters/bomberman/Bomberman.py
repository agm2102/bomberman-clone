import pygame
from config.Settings import Settings
from entities.base_classes.BaseCharacter import BaseCharacter
from entities.objects.Bomb import Bomb
from systems.Animation import Animation
class Bomberman(BaseCharacter):

    def __init__(self, x, y, is_alive, sprite_manager, game_map, speed, lives):
        super().__init__(x, y, game_map, sprite_manager, is_alive, speed)

        self.invencible_timer = 0
        self.INVENCIBLE_DURATION = 120

        self.QTD_BOMBS_LIMIT_MAX = 8
        self.RANGE_EXPLOSION_MAX = 3
        self.SPEED_MAX = 4

        self.game_map = game_map
        self.sprite_manager = sprite_manager
        self.x = x
        self.y = y
        self.lives = lives
        self.qtd_bombs = 0
        self.qtd_bombs_limit = 1
        self.range_explosion = 1

        self.wall_pass = False
        self.bomb_pass = False
        self.detonator = False
        self.flame_pass = False

        self.add_animations()

    def decrease_qtd_lives(self):
        if self.invencible_timer > 0:  # ainda invencível
            return
        self.lives -= 1
        self.invencible_timer = self.INVENCIBLE_DURATION  # ativa invencibilidade

    def spawn_bomb(self):
        tile = Settings.SPRITE_BLOCK_SIZE
        x = round(self.x / tile) * tile
        y = round(self.y / tile) * tile

        bomb = Bomb(x, y, self.sprite_manager, self.game_map, self.range_explosion)
        bomb.set_has_detonator(self.detonator)
        self.bombs_list.append(bomb)

    def apply_item_effect(self, type_item):
        if type_item == 0 and self.qtd_bombs_limit < self.QTD_BOMBS_LIMIT_MAX:
            self.qtd_bombs_limit += 1
        elif type_item == 1 and self.range_explosion < self.RANGE_EXPLOSION_MAX:
            self.range_explosion += 1
        elif type_item == 2 and self._speed < self.SPEED_MAX:
            self._speed += 1
        elif type_item == 3 and self.wall_pass is False:
            self.wall_pass = True
        elif type_item == 4 and self.detonator is False:
            self.detonator = True
        elif type_item == 5 and self.bomb_pass is False:
            self.bomb_pass = True
        elif type_item == 6 and self.flame_pass is False:
            self.flame_pass = True


    def add_animations(self):

        frames = self.sprite_manager.get("bomberman")

        self.animation_controller.add_animation("right_walk", Animation(frames[6:9], 5, True))
        self.animation_controller.add_animation("left_walk", Animation(frames[0:3], 5, True))
        self.animation_controller.add_animation("up_walk", Animation(frames[9:12], 5, True))
        self.animation_controller.add_animation("down_walk", Animation(frames[3:6], 5, True))
        self.animation_controller.add_animation("death", Animation(frames[12:19], 20, False))

    def draw(self, screen, camera=None):
        # pisca quando invencível — alterna visível/invisível a cada 5 frames
        if self.invencible_timer > 0 and self.invencible_timer % 10 < 5:
            return  # não desenha — efeito de piscar

        pos = camera.apply(self) if camera else (self.x, self.y)
        screen.blit(self.sprite, pos)

    def update(self, events = None):
        if self.invencible_timer > 0:
            self.invencible_timer -= 1

        self._check_collision_characters_bombs()

        if not self.is_alive:
            self.animation_controller.change_current_animation("death", False)
            if self.animation_controller.finished():
                return

        if self.is_alive:
            self.input_handler(events)

        if self.dir is not None or not self.is_alive:
            self.animation_controller.update()

        frame = self.animation_controller.get_frame()
        self.sprite = frame

    def move(self, direction):
        dx, dy = self.directions[direction]
        new_x = self.x + dx * self._speed
        new_y = self.y + dy * self._speed

        if self._game_map.is_walkable_position(new_x, new_y, self.bombs_list):
            self.x = new_x
            self.y = new_y

    def _check_collision_characters_bombs(self):
        for bomb in self.bombs_list:
            if bomb.get_is_solid() is False and bomb.get_rect().colliderect(self.get_rect()) is False and self.bomb_pass is False:
               bomb.set_is_solid(True)

    def get_list_bombs(self):
        return self.bombs_list

    def get_lives(self):
        return self.lives

    def set_qtd_bombs(self, qtd_bomb):
        self.qtd_bombs += qtd_bomb

    def input_handler(self, events):
        # Verifica KEYDOWN nos eventos recebidos
        if events:
            for evento in events:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        if self.qtd_bombs < self.qtd_bombs_limit:
                            self.spawn_bomb()
                            self.qtd_bombs += 1
                    if evento.key == pygame.K_b:
                        if self.detonator and self.bombs_list:
                            self.bombs_list[-1].explode_by_detonator()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            if self.dir != "LEFT":
                self.align_axis("LEFT")
            self.dir = "LEFT"
            self.move(self.dir)
            self.animation_controller.change_current_animation("left_walk", False)

        elif keys_pressed[pygame.K_RIGHT]:
            if self.dir != "RIGHT":
                self.align_axis("RIGHT")
            self.dir = "RIGHT"
            self.move(self.dir)
            self.animation_controller.change_current_animation("right_walk", False)


        elif keys_pressed[pygame.K_UP]:
            if self.dir != "UP":
                self.align_axis("UP")
            self.dir = "UP"
            self.move(self.dir)
            self.animation_controller.change_current_animation("up_walk", False)

        elif keys_pressed[pygame.K_DOWN]:
            if self.dir != "DOWN":
                self.align_axis("DOWN")
            self.dir = "DOWN"
            self.move(self.dir)
            self.animation_controller.change_current_animation("down_walk", False)

        else:
            self.dir = None