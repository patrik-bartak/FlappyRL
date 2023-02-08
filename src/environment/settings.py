from dataclasses import dataclass
from typing import Callable
from gui.gui import Gui


@dataclass
class Settings:
    """Configuration for the project"""

    agent: None
    reward_function: Callable
    gui_bool: bool
    max_ticks: int
    acceleration: float
    max_x: int
    max_y: int
    starting_x_coordinate: int
    distance_between_tubes: float
    gap_height: float
    gap_width: float
    initial_speed: int
    framerate: int
    flap_strength: int
