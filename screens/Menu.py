import pygame

from config.Settings import Settings


class Menu:
    def __init__(self, screen, sprite_manager):
        self.screen = screen
        self.sprite_menu = sprite_manager.get("screens")[0]
        self.sprite_selector = sprite_manager.get("simbol")[0]
        self.PRETO = (0, 0, 0)

        S = Settings.SCALE

        self.position_selector = {
            "start": (67 * S, 150 * S),
            "continue": (130 * S, 150 * S)
        }

        self.position_selection = self.position_selector["start"]
        self.black_square_position_x, self.black_square_position_y = self.position_selector["continue"]

    def draw(self):
        self.screen.blit(self.sprite_menu, (0, 0))
        self.screen.blit(self.sprite_selector, self.position_selection)

        pygame.draw.rect(self.screen, self.PRETO,
                         (self.black_square_position_x, self.black_square_position_y, Settings.NUMBER_LETTER_SIZE_WIDTH,
                          Settings.NUMBER_LETTER_SIZE_HEIGHT))

    def update(self, events):
        pygame.draw.rect(self.screen, self.PRETO, ( self.black_square_position_x, self.black_square_position_y, Settings.NUMBER_LETTER_SIZE_WIDTH,
                                                   Settings.NUMBER_LETTER_SIZE_HEIGHT))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.position_selection = self.position_selector["continue"]
                    self.black_square_position_x, self.black_square_position_y = self.position_selector["start"]
                elif event.key == pygame.K_LEFT:
                    self.position_selection = self.position_selector["start"]
                    self.black_square_position_x, self.black_square_position_y = self.position_selector["continue"]

    def get_menu_option(self):
        if self.position_selection == self.position_selector["start"]:
            return "START"
        else:
            return "CONTINUE"