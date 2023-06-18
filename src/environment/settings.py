from dataclasses import dataclass
from typing import Callable
from agent.agents import Agent
from environment.reward import Reward
from gui.gui import GraphicalUserInterface


@dataclass
class Settings:
    """Configuration for the project"""

    agent: Agent
    player_width: float
    player_height: float
    reward: Reward
    gui_bool: bool
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
