from enum import Enum
from typing import Any
from statemachine import StateMachine
from statemachine.states import States

from environment.player import Player
from environment.tube_generator import TubeGenerator


class GameState(Enum):
    INITIAL = 0
    PLAYING = 1
    FAILURE = 2
    SUCCESS = 3
    TERMINAL = 4


class GameStateMachine(StateMachine):
    """
    The state of the game at any moment
    """

    player: Player
    generator: TubeGenerator
    tick: int = 0

    states = States.from_enum(
        GameState,
        initial=GameState.INITIAL,
        final=GameState.TERMINAL,
    )

    start_game = states.INITIAL.to(states.PLAYING)
    lose_game = states.PLAYING.to(states.FAILURE)
    win_game = states.PLAYING.to(states.SUCCESS)
    end_game = states.FAILURE.to(states.TERMINAL) | states.SUCCESS.to(states.TERMINAL)

    def __init__(self, player: Player, generator: TubeGenerator):
        super().__init__()
        self.player = player
        self.generator = generator

    def increment_tick(self):
        self.tick += 1
