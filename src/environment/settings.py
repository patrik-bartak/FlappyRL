from dataclasses import dataclass
from typing import Type
from agent.agents import Agent
from gui.gui import UserInterface
from environment.reward import Reward


@dataclass
class Settings:
    """Configuration for the project"""

    agent: Agent
    player_width: float
    player_height: float
    reward: Reward
    ui: str
    max_ticks: int
    acceleration: float
    max_x: int
    max_y: int
    starting_x_coordinate: float
    distance_between_tubes: float
    gap_height: float
    gap_width: float
    initial_speed: float
    framerate: int
    flap_strength: float
