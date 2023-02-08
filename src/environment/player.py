from dataclasses import dataclass
import pygame as pg
from environment.settings import Settings


@dataclass
class Player:
    """
    Represents the player object in the game
    """

    settings: Settings
    x: int
    y: int
    width: int
    height: int
    dy: int = 0

    def update(self):
        """Update the player according to the game physics and checks for collisions"""
        self.dy += self.settings.acceleration
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy = 0
        return self.collision_check()

    def collision_check(self):
        """Checks for collisions between player and border of x-y space"""
        return self.y + self.height > self.settings.max_y

    def flap(self):
        """Perform a flap action to go up"""
        self.dy = -self.settings.flap_strength

    def get_visual(self):
        return pg.rect.Rect(self.x, self.y, self.width, self.height)
