import os
import pygame
from config.Settings import Settings
from grafics.SpriteManager import SpriteManager
from screens.GameScreen import GameScreen
from screens.Menu import Menu
from screens.GameOver import GameOver

def create_new_screen(width, height):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    return pygame.display.set_mode((width, height))

class Game:

    def __init__(self):
        pygame.init()
        # Cria a tela do jogo
        self.screenGame = create_new_screen(Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
        # Variavel que gerencia e limita o FPS do jogo
        self.clock = pygame.time.Clock()
        self.runningGame = True
        self.events = None
        self.sprite_manager = SpriteManager()

        self.screens = {
            "menu" : Menu(self.screenGame, self.sprite_manager),
            "stage": GameScreen(self.screenGame, self.sprite_manager),
            "gameOver" : GameOver(self.screenGame, self.sprite_manager)
        }
        self.CURRENT_SCREEN = 0

    def run(self):
        while self.runningGame:
            self.handle_events()
            self.update()
            self.render()
            # controla FPS (60)
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):

        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.runningGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.screens["menu"].get_menu_option() == "START":
                        self.screenGame = create_new_screen(Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
                        self.CURRENT_SCREEN = 1

    def render(self):

        self.screenGame.fill((0, 0, 0))  # limpa tela (preto)

        if self.CURRENT_SCREEN == 0:
            self.screens["menu"].draw()
        elif self.CURRENT_SCREEN == 1:
            self.screens["stage"].draw()

        pygame.display.flip()

    def update(self):
        if self.CURRENT_SCREEN == 0:
            if self.screens["menu"] is not None:
                self.screens["menu"].update(self.events)
        elif self.CURRENT_SCREEN == 1:
            if self.screens["stage"] is not None:
                self.screens["stage"].update(self.events)

