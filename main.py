import settings
from tetris import Tetris, Text
import pygame as pg
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(settings.FIELD_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)

    def update(self):
        self.tetris.update()
        self.clock.tick(settings.FPS)

    def draw(self):
        self.screen.fill(color=settings.BG_COLOR)
        self.screen.fill(color=settings.FIELD_COLOR, rect=(0, 0, *settings.FIELD_RES))
        self.tetris.draw()
        pg.display.flip()

    def check_events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT or (events.type == pg.K_DOWN and events.key == pg.K_ESCAPE):
                pg.quit()
                sys.exitt()
            
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()