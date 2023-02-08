from gui import Gui
from tube_generator import TubeGenerator
from settings import Settings
from player import Player
from human_agent import HumanAgent

MAX_X = 640
MAX_Y = 480


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
        acceleration=5.81,
        max_x=MAX_X,
        max_y=MAX_Y,
        starting_x_coordinate=500,
        distance_between_tubes=200 ,
        gap_height=0.5 ,
        gap_width=0.15,
        initial_speed=1,
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
    player = Player(settings, 100, 100, 50, 50)
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
        # Update player
        player.update()
        # Update all tubes
        ended = generator.update(tick)
        if ended:
            print("COLLISION")   
        action = settings.agent.act(state=None)
        if action == 1:
            player.dy = -10
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
