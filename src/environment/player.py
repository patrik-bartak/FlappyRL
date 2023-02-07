from dataclasses import dataclass
import pygame as pg
import numpy as np
from settings import Settings


@dataclass
class Player:
    settings: Settings
    x: int
    y: int
    width: int
    height: int
    dx: int = 0
    dy: int = 0

    def update(self):
        self.dy += 1
        self.x += self.dx
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy = 0
        if self.y + self.height > self.settings.max_y:
            self.y = self.settings.max_y - self.height
            self.dy = 0

    def get_visual(self):
        return pg.rect.Rect(self.x, self.y, self.width, self.height)
