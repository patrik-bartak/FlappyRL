import agent
import sys
import pygame as pg
from environment.tube_generator import TubeGenerator
from environment.settings import Settings
from environment.player import Player
from environment.reward import TickReward
from game.game_state import GameStateMachine
from gui.gui import GraphicalUserInterface, NoInterface, TextInterface
from agent.agents import HumanAgent, DummyAgent, RandomAgent, Action


def main():
    """
    Main function of the game.
    Collects settings from the experiment class.

    :return:
    """
    settings = Settings(
        # agent=HumanAgent(),
        agent=RandomAgent(),
        player_width=0.025,
        player_height=0.05,
        reward=TickReward(),
        ui="GraphicalUserInterface",
        max_ticks=1000,
        acceleration=0.001,
        # Convenient for it to be a power of 2
        max_x=1024,
        max_y=512,
        starting_x_coordinate=1,
        distance_between_tubes=0.2,
        gap_height=0.5,
        gap_width=0.05,
        initial_speed=0.005,
        framerate=60,
        flap_strength=0.01,
    )
    game_loop(settings)


def game_loop(settings):
    """
    Main loop of the game.
    Updates all the parts individually, records the states and rewards into the agent.
    If required, updates the GUI and draws it.

    :param settings: JSON representing the settings of the experiment.
    """
    player = Player(
        0.05,
        0.5,
        settings.player_width,
        settings.player_height,
        settings.acceleration,
        settings.flap_strength,
    )
    generator = TubeGenerator(player=player, settings=settings)
    gs = GameStateMachine(player, generator)
    gs.tick = 0
    # Tick for keeping the end screen up for human players
    terminal_tick = 0
    ended = False
    state_reader = (
        None  # Something that combines the player and generator data into a state
    )
    # Define reward function in the settings
    reward = settings.reward
    # Instantiate the GUI if required
    if settings.ui == "GraphicalUserInterface":
        ui = GraphicalUserInterface(settings, player, generator, gs)
    elif settings.ui == "TextInterface":
        ui = TextInterface(gs)
    else:
        ui = NoInterface()
    if not isinstance(settings.agent, HumanAgent):
        # If not human, skip initial screen
        gs.start_game()
    # while tick < settings.max_ticks and not ended:
    while True:
        if gs.INITIAL.is_active:
            # This means a human is playing
            # Check for pygame initialization
            if not pg.get_init():
                raise Exception("Cannot use HumanAgent without GUI")
            # Check for spacebar keypress
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    gs.start_game()
        elif gs.PLAYING.is_active:
            # Update player and tubes and check for collisions
            ended = player.update() or generator.update(gs.tick)
            if ended:
                gs.lose_game()

            action = settings.agent.act(state=gs)
            if action == Action.FLAP:
                player.flap()

            # Record the state, action and reward to the agent
            settings.agent.record(
                state=gs,
                action=action,
                reward=reward.get_reward(gs, action),
            )

            gs.increment_tick()
        elif gs.FAILURE.is_active or gs.SUCCESS.is_active:
            if not isinstance(settings.agent, HumanAgent):
                gs.end_game()
                continue
            terminal_tick += 1
            # Wait for 2 seconds (120 frames)
            if terminal_tick > 120:
                gs.end_game()
        elif gs.TERMINAL.is_active:
            break
        # Display GUI if needed
        ui.draw()


if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit(0)
