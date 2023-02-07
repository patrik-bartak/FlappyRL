from dataclasses import dataclass
from typing import Callable
from gui import Gui


@dataclass
class Settings:
    agent: None
    reward_function: Callable
    gui_bool: bool
    max_ticks: int
    reward_function: Callable
    acceleration: float
    max_x: int
    max_y: int
    starting_x_coordinate: int
    distance_between_tubes: float
    gap_height: int
    gap_width: int
    initial_speed: int
