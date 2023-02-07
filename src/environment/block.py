import pygame as pg

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500


class Block(pg.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
        pg.draw.rect(self.image, color, pg.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
