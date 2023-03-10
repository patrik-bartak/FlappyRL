from gui.gui import Gui
from environment.tube_generator import TubeGenerator
from environment.settings import Settings
from environment.player import Player
from agent.agents import HumanAgent, DummyAgent, RandomAgent, Action


def main():
    """
    Main function of the game.
    Collects settings from the experiment class.

    :return:
    """
    settings = Settings(
        agent=HumanAgent(),
        reward_function=lambda x: 0,
        gui_bool=True,
        max_ticks=1000,
        acceleration=0.001,
        max_x=1000,
        max_y=600,
        starting_x_coordinate=1,
        distance_between_tubes=0.2,
        gap_height=0.5,
        gap_width=0.05,
        initial_speed=0.01 ,
        framerate=60,
        flap_strength=0.01
    )
    game_loop(settings)


def game_loop(settings):
    """
    Main loop of the game.
    Updates all the parts individually, records the states and rewards into the agent.
    If required, updates the GUI and draws it.

    :param settings: JSON representing the settings of the experiment.
    """
    tick = 0
    ended = False
    player = Player(settings, 0.05, 0.5, 0.05, 0.05)
    state_reader = (
        None  # Something that combines the player and generator data into a state
    )
    # Define reward function in the settings
    reward_function = settings.reward_function
    generator = TubeGenerator(player=player, settings=settings)
    # Instantiate the GUI if required
    if settings.gui_bool:
        gui = Gui(settings, player, generator)
    while tick < settings.max_ticks and not ended:
        # Update player and tubes and check for collisions
        ended = player.update() or generator.update(tick)
        if ended:
            print("COLLISION")
        action = settings.agent.act(state=None)
        if action == Action.FLAP:
            player.flap()
        # Record the state, action and reward to the agent
        # settings.agent.record(
        #     state=state_reader.get_state(),
        #     action=None,
        #     reward=reward_function(state_reader, generator),
        # )
        tick += 1
        # Display GUI if needed
        if settings.gui_bool:
            gui.draw()
    print("GAME OVER. ")


if __name__ == "__main__":
    main()
