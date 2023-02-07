from dataclasses import dataclass


@dataclass
class Agent:
    def act(self, state):
        action = None
        return action

    def record(self, state, action, reward):
        pass
