from dataclasses import dataclass
from agent import Agent
import pygame as pg


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

