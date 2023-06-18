from dataclasses import dataclass


@dataclass
class Player:
    """
    Represents the player object in the game
    """

    x: float
    y: float
    width: float
    height: float
    acceleration: float
    flap_strength: float
    dy: float = 0

    def update(self):
        """Update the player according to the game physics and checks for collisions"""
        self.dy += self.acceleration
        self.y += self.dy
        if self.y < 0:
            self.y = 0
            self.dy = 0
        return self.collision_check()

    def collision_check(self):
        """Checks for collisions between player and border of x-y space"""
        return self.y + self.height > 1

    def flap(self):
        """Perform a flap action to go up"""
        self.dy = -self.flap_strength

    def __str__(self):
        return f"(Player x: {self.x} | y: {self.y})"
