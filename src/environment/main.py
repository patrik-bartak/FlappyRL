from tube_generator import TubeGenerator
from settings import Settings


def main():
    """
    Main function of the game.
    Collects settings from the experiment class.

    :return:
    """
    settings = Settings(
        None,
        None,
        lambda: 0,
        True,
        1E10,
        9.81,
        0,
        20,
        10,
        10,
        1,
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
    player = None
    state_reader = (
        None  # Something that combines the player and generator data into a state
    )
    # Define reward function in the settings
    reward_function = settings["reward_function"]
    generator = TubeGenerator(player=player, settings=settings)
    # Instantiate the GUI if required
    gui = None
    if settings["gui_bool"]:
        gui = settings["gui"](player, generator)
    while tick < settings["max_ticks"] and not ended:
        # Update player

        # Update all tubes
        ended = generator.update(tick)
        # Record the state, action and reward to the agent
        settings["agent"].record(
            state=state_reader.get_state(),
            action=None,
            reward=reward_function(state_reader, generator),
        )
        # Display GUI if needed
        if settings["gui_bool"]:
            gui.draw()


if __name__ == "__main__":
    main()
