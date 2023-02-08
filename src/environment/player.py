from dataclasses import dataclass
import pygame as pg
from environment.settings import Settings


@dataclass
class Player:
    settings: Settings
    x: int
    y: int
    width: int
    height: int
    dy: int = 0

    def update(self):
        self.dy += self.settings.acceleration
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy = 0
        if self.y + self.height > self.settings.max_y:
            return True
        return False

    def flap(self):
        self.dy = -self.settings.flap_strength

    def get_visual(self):
        return pg.rect.Rect(self.x, self.y, self.width, self.height)
