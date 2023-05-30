import settings  
import pygame as pg
import math
from tetromino import Tetromino

class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.FONT(FONT_PATH)

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def draw_grid(self):
        for x in range(settings.FIELD_W):
            for y in range(settings.FIELD_H):
                pg.draw.rect(self.app.screen,'black',
                (x * settings.TILE_SIZE, y * settings.TILE_SIZE, settings.TILE_SIZE, settings.TILE_SIZE), width = 1)
    
    def update(self):
        self.tetromino.update()
        self.sprite_group.update

    def draw(self):
        self.app.screen.fill(settings.BG_COLOR)
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)