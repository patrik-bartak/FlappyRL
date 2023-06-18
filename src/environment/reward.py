from abc import ABC, abstractmethod
from agent.agents import Action
from game.game_state import GameStateMachine


class Reward(ABC):
    @abstractmethod
    def get_reward():
        pass


class TickReward(Reward):
    def get_reward(self, state: GameStateMachine, action: Action):
        return state.tick
