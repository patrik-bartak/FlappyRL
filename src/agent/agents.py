from dataclasses import dataclass
from abc import ABC, abstractmethod
import numpy.random as rand
import pygame as pg
from enum import Enum


class Action(Enum):
    """
    FLAP to go up, NO_FLAP to do nothing
    """

    FLAP = 1
    NO_FLAP = 0


@dataclass
class Agent(ABC):
    """
    Interface for all agents that interact with the game
    """

    @abstractmethod
    def act(self, state) -> Action:
        """
        Mapping of states to actions that defines the policy of the agent
        """
        pass

    @abstractmethod
    def record(self, state, action, reward):
        pass


@dataclass
class HumanAgent(Agent):
    """
    Agent controlled by the player through the GUI and using the spacebar
    """

    def act(self, state) -> Action:
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
class RandomAgent(Agent):
    """
    Agent that flaps randomly with 0.1 probability
    """

    def act(self, state):
        return Action.FLAP if rand.binomial(1, 0.1) else Action.NO_FLAP

    def record(self, state, action, reward):
        pass


@dataclass
class DummyAgent(Agent):
    """
    Agent that always flaps
    """

    def act(self, state):
        return Action.FLAP

    def record(self, state, action, reward):
        pass
