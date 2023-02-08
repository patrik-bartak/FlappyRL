from dataclasses import dataclass
import pygame as pg
from enum import Enum


class Action(Enum):
    """
    FLAP to go up, NO_FLAP to do nothing
    """

    FLAP = 1
    NO_FLAP = 0


@dataclass
class Agent:
    """
    Interface for all agents that interact with the game
    """

    def act(self, state):
        action = None
        return action

    def record(self, state, action, reward):
        pass


@dataclass
class HumanAgent(Agent):
    """
    Agent controlled by the player through the GUI and using the spacebar
    """

    def act(self, state):
        # Check for pygame initialization
        if not pg.get_init():
            raise Exception("Cannot use HumanAgent without GUI")
        # Check for spacebar keypress
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                return Action.FLAP
        return Action.NO_FLAP

    def record(self, state, action, reward):
        pass


@dataclass
class DummyAgent(Agent):
    """
    Agent that always flaps
    """

    def act(self, state):
        return 1

    def record(self, state, action, reward):
        pass

