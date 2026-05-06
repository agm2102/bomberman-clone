class Settings:
    # Configurações de tamanho das sprites
    SCALE = 4

    SPRITE_BLOCK_SIZE = 16 * SCALE  # 64px
    SPRITE_CHARACTER_OBJECTS_SIZE = 14 * SCALE  # 64px

    MAP_ROWS = 13
    MAP_COLS = 31
    HUD_ROWS = 2

    SCREEN_WIDTH = 256 * SCALE  # 1024px
    SCREEN_HEIGHT = (MAP_ROWS + HUD_ROWS) * SPRITE_BLOCK_SIZE  # 960px

    HUD_HEIGHT = HUD_ROWS * SPRITE_BLOCK_SIZE  # 128px — offset do mapa

    #Numeros e Letras
    NUMBER_LETTER_SIZE_WIDTH = 32
    NUMBER_LETTER_SIZE_HEIGHT = 37

