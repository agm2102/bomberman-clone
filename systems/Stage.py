from systems.CollisionManager import CollisionManager

class Stage:

    def __init__(self, screen, sprite_manager, player, enemies, game_map, camera):
        self.camera = camera
        self.time_stage_max_mili = 200 * 60
        self.time_stage_seconds = 200
        self.timer = 0
        self.stage_finished = False
        self.screenGame = screen
        self.sprite_manager = sprite_manager

        self.game_map = game_map
        self.door = self.game_map.get_door()
        self.map_item = game_map.get_item()
        self.enemyList = enemies
        self.player = player

        self.bomb_list = self.player.get_list_bombs()
        self.explosion_list = []
        self.blocks_list = self.game_map.get_blocks_list()

        self.collision_manager = CollisionManager(self.player, self.enemyList, self.bomb_list, self.explosion_list,
                                                  self.blocks_list, self.map_item, self.door)

    def draw(self):
        self.game_map.draw(self.screenGame, self.camera)  # ← passa camera

        self.player.draw(self.screenGame, self.camera)

        for enemy in self.enemyList:
            enemy.draw(self.screenGame, self.camera)

        for bomb in self.bomb_list:
            bomb.draw(self.screenGame, self.camera)

        for explosion_part in self.explosion_list:
            explosion_part.draw(self.screenGame, self.camera)

    def update(self, events):

        self.player.update(events)

        for enemy in self.enemyList:
            enemy.update(self.bomb_list)

        for explosion_part in self.explosion_list:
            explosion_part.update()

        self.game_map.update()

        self.check_all_enemies_is_dead()
        self.remove_game_objects()
        self.collision_manager.check()

        self.timer_stage()

    def timer_stage(self):
        if self.timer % 60 == 0:
            self.time_stage_seconds -= 1
        self.timer+=1

    def get_timer(self):
        return self.time_stage_seconds

    def remove_game_objects(self):
        for bomb in self.bomb_list[:]:  # itera sobre uma cópia da lista
            bomb.update()
            self.explosion_list.extend(bomb.get_list_explosions())
            if bomb.get_is_exploded():
                self.bomb_list.remove(bomb)  # remove o elemento correto
                self.player.set_qtd_bombs(-1)

        for enemy in self.enemyList[:]:
            if enemy.get_is_dead() is True:
                self.enemyList.remove(enemy)

        for explosion_part in self.explosion_list[:]:
            explosion_part.update()
            if explosion_part.is_finished:
                self.explosion_list.remove(explosion_part)

        for block in self.blocks_list[:]:
            if block.get_is_destroyed():
                self.blocks_list.remove(block)

        if self.game_map.get_item() is not None and self.game_map.get_item().is_collected():
            self.game_map.remove_item()

    def is_stage_finished(self):
       return self.stage_finished

    def check_all_enemies_is_dead(self):
        if len(self.enemyList) == 0:
            self.door.set_locked(False)