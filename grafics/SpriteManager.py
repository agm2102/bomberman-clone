import os
from config.Settings import Settings
from grafics.LoadImages import LoadImages

class SpriteManager:
    _instance = None  # Singleton — carrega sprites apenas uma vez

    CHARACTER_SIZE = Settings.SPRITE_SIZE
    BLOCK_SIZE      = Settings.SPRITE_SIZE
    OBJECTS_SIZE      = Settings.SPRITE_SIZE

    SCREEN_WIDTH = Settings.SCREEN_WIDTH
    SCREEN_HEIGHT = Settings.SCREEN_HEIGHT

    NUMBER_LETTER_WIDTH = Settings.NUMBER_LETTER_SIZE_WIDTH
    NUMBER_LETTER_HEIGHT = Settings.NUMBER_LETTER_SIZE_HEIGHT

    SPRITE_PATHS = {
        # Personagem
        "bomberman":   ("assets/sprites/bomberman/", CHARACTER_SIZE, CHARACTER_SIZE),

        # Inimigos
        "Ballom":      ("assets/sprites/enemies/ballom/", CHARACTER_SIZE, CHARACTER_SIZE),
        "Onil":        ("assets/sprites/enemies/onil/",   CHARACTER_SIZE, CHARACTER_SIZE),
        "Dahl":          ("assets/sprites/enemies/dahl/", CHARACTER_SIZE, CHARACTER_SIZE),
        "Doria":         ("assets/sprites/enemies/doria/", CHARACTER_SIZE, CHARACTER_SIZE),
        "Minvo": ("assets/sprites/enemies/minvo/", CHARACTER_SIZE, CHARACTER_SIZE),
        "Ovape": ("assets/sprites/enemies/ovape/", CHARACTER_SIZE, CHARACTER_SIZE),
        "Pass": ("assets/sprites/enemies/pass/", CHARACTER_SIZE, CHARACTER_SIZE),
        "Pontan": ("assets/sprites/enemies/pontan/", CHARACTER_SIZE, CHARACTER_SIZE),

        # Cenário
        "map":           ("assets/sprites/map/", BLOCK_SIZE, BLOCK_SIZE),

        #bombsbomberman
        "bomb": ("assets/sprites/bomb/", OBJECTS_SIZE, OBJECTS_SIZE),

        #explosion
        "explosion": ("assets/sprites/explosion/", OBJECTS_SIZE, OBJECTS_SIZE),

        #itens
        "item": ("assets/sprites/itens/", OBJECTS_SIZE, OBJECTS_SIZE),

        #screens
        "screens": ("assets/sprites/screens/", SCREEN_WIDTH, SCREEN_HEIGHT),

        #characters
        "numbers_hud": ("assets/sprites/hud/characters/numbers/numbers_hud/", NUMBER_LETTER_WIDTH, NUMBER_LETTER_HEIGHT),
        "simbol" : ("assets/sprites/hud/characters/simbol/", NUMBER_LETTER_WIDTH, NUMBER_LETTER_HEIGHT),
        "letters_hud" : ("assets/sprites/hud/characters/letters/letters_hud/", NUMBER_LETTER_WIDTH, NUMBER_LETTER_HEIGHT)
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        loader = LoadImages()
        self._sprites = {}

        for nome, (path, width, height) in self.SPRITE_PATHS.items():
            if not os.path.exists(path):
                print(f"[SpriteManager] ⚠️ Pasta não encontrada: {path}")
                self._sprites[nome] = []
                continue
            self._sprites[nome] = loader.load_from_folder(path, width, height)

    def get(self, nome: str) -> list:
        if nome not in self._sprites:
            raise KeyError(f"[SpriteManager] Sprite '{nome}' não cadastrado.")
        return self._sprites[nome]