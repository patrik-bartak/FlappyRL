from dataclasses import dataclass
import pygame as pg


@dataclass
class Agent:
    def act(self, state):
        action = None
        return action

    def record(self, state, action, reward):
        pass


@dataclass
class HumanAgent(Agent):
    pass

    def act(self, state):
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                return 1
        return 0

    def record(self, state, action, reward):
        pass


@dataclass
class DummyAgent(Agent):
    pass

    def act(self, state):
        return 1

    def record(self, state, action, reward):
        pass

