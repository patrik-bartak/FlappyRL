from dataclasses import dataclass
from typing import Callable


@dataclass
class Settings:
    gui: None
    agent: None
    reward_function: Callable
    gui_bool: bool
    max_ticks: int
    reward_function: Callable
    acceleration: float
    starting_x_coordinate: int
    distance_between_tubes: float
    gap_height: int
    gap_width: int
    initial_speed: int
