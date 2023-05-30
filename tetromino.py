import settings
import pygame as pg
from pygame.math import Vector2 as vec


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        from settings import INIT_POS_OFFSET
        self.tetromino = tetromino
        self.pos = vec(pos)
        self.pos += INIT_POS_OFFSET

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([settings.TILE_SIZE, settings.TILE_SIZE])
        self.image.fill('white')

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * settings.TILE_SIZE
class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = 'T'
        self.blocks = [Block(self,pos) for pos in settings.TETROMINOES[self.shape]]
        

    def update(self):
        pass