from environment.tube import Tube


class TubeGenerator:
    def __init__(self, player, settings):
        """
        TubeGenerator class takes care of generating new tubes and updating them throughout the game.

        :param player:
        :param settings:
        """
        self.accel = settings.acceleration
        self.player = player
        self.start = settings.starting_x_coordinate
        self.distance = settings.distance_between_tubes
        self.gap_height = settings.gap_height
        self.gap_width = settings.gap_width
        self.initial_speed = settings.initial_speed
        self.tubes = []
        # Number of passed tubes increases only when a tube is forgotten.
        self.passed = 0

    def update(self, tick):
        """
        Updates the tube generator by updating each individual tube.
        Remove tubes that should be forgotten as they're out of the frame.
        Generate new tubes if the previous tube is far enough.

        :param tick: Number representing the game tick.
        :return: Whether the game has ended or not. If any update crashes, game ends.
        """
        # Remove tubes that are past
        # Add new tubes if needed
        self.verify(tick)
        # Check whether game is not yet finished
        ended = self.collision()
        if ended:
            return True
        # Update each tube present
        ver = True
        for tube in self.tubes:
            ver &= tube.update(tick)
        return not ver

    def verify(self, tick):
        """
        Verifies which tubes should be removed and places new tubes if the list is empty
        or the previously generated tube is far enough for a new tube to be generated.

        :param tick: Number representing the game tick.
        """
        n = len(self.tubes)
        self.tubes = list(filter(lambda tube: tube.verify(), self.tubes))
        self.passed += abs(n - len(self.tubes))
        if (
            len(self.tubes) == 0
            or self.tubes[-1].get_x_coord()[1] + self.distance < self.start
        ):
            self.tubes.append(
                Tube(
                    self.start,
                    self.gap_height,
                    self.gap_width,
                    self.initial_speed
                )
            )

    def collision(self):
        """
        Checks whether the player collides with any of the tubes.

        :return: Returns true if collision was detected.
        """
        return any(map(lambda tube: tube.collision(self.player), self.tubes))

    def __str__(self):
        if len(self.tubes) == 0:
            return "[]"
        res = "["
        for tube in self.tubes:
            res += str(tube) + ", "
        return res[:-2] + "]"
