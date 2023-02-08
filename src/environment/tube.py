import numpy as np


class Tube:
    """
    Class representing the moving tube on the screen.
    It is defined by its x coordinate and its speed.
    After the x coordinate plus its width reach negative numbers,
    the tube can be removed as it no longer plays any role in the game.
    """

    def __init__(self, x, gap_height, width, speed, max_x, max_y):
        """

        :param x: The x coordinate
        :param gap_height: The height of the gap in the pillar
        :param width: Width of the pillar
        :param speed: How fast does the pillar approach the 0th coordinate
        """
        self.x = x
        self.gap_height = gap_height
        # Y position should be always between 0 and 1
        self.gap_position = np.random.random() * gap_height
        self.width = width
        self.speed = speed
        self.max_x = max_x
        self.max_y = max_y

    def update(self, tick):
        """
        Updates the tube every time tick.

        :param tick: Number representing the time tick of the update
        :return: True if correctly updated, false otherwise.
        """
        self.x -= self.speed
        return True

    def get_x_coord(self):
        return self.x, self.x + self.width * self.max_x

    def collision(self, player):
        # Check if player is inside the tube
        if (player.x + player.width >= self.x > player.x) or \
                (player.x + player.width >= self.x and player.x <= self.x + self.width * self.max_x) \
                or \
                (player.x <= self.x + self.width * self.max_x < player.x + player.width):
            # Return true if y position would be in a collision state, otherwise false
            return player.y + player.height >= (self.gap_position + self.gap_height) * self.max_y \
                   or player.y <= self.gap_position * self.max_y

        return False

    def __str__(self):
        return f"(Tube: x={self.x} | pos={self.gap_position})"

    def __hash__(self):
        return self.x

    def verify(self):
        return self.x >= 0
