class Settings:
    # Configurações de tamanho das sprites
    SCALE = 4
    SPRITE_SIZE = 16 * SCALE  # 64px

    MAP_ROWS = 13
    MAP_COLS = 31
    HUD_ROWS = 2

    # Configuração da tela e HUD
    SCREEN_WIDTH = 256 * SCALE  # 1024px
    SCREEN_HEIGHT = (MAP_ROWS + HUD_ROWS) * SPRITE_SIZE  # 960px

    HUD_HEIGHT = HUD_ROWS * SPRITE_SIZE  # 128px — offset do mapa

    #Numeros e Letras
    NUMBER_LETTER_SIZE_WIDTH = SCALE * 8
    NUMBER_LETTER_SIZE_HEIGHT = SCALE * 10

    #FPS
    FRAMES_PER_SECOND = 59


