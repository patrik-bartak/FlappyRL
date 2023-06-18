from abc import ABC, abstractmethod
import pygame as pg


class UserInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class NoInterface(UserInterface):
    def draw(self):
        pass


class TextInterface(UserInterface):
    def __init__(self, game_state) -> None:
        self.game_state = game_state

    def draw(self):
        print(
            f"Game State: {self.game_state.current_state.id} | Game Tick: {self.game_state.tick:04d}",
            end="\r",
        )


class GraphicalUserInterface(UserInterface):
    """Displays the game graphically"""

    font_path = "./fonts/monospace/MonospaceBold.ttf"

    def __init__(self, settings, player, tube_generator, game_state) -> None:
        self.player = player
        self.tube_generator = tube_generator
        self.game_state = game_state
        pg.init()
        self.settings = settings
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((settings.max_x, settings.max_y))
        self.max_x = settings.max_x
        self.max_y = settings.max_y
        self.window.fill((255, 255, 255))
        self.framerate = settings.framerate
        self.frame_number = 0
        self.font = pg.font.Font(self.font_path, 12)
        pass

    def draw(self):
        """Update the GUI based on the game state"""
        self.clock.tick(self.framerate)
        self.frame_number += 1
        # reset window fill
        self.window.fill((255, 255, 255))
        # draw player
        pg.draw.rect(
            self.window,
            (0, 0, 255),
            pg.rect.Rect(
                self.player.x * self.max_x,
                self.player.y * self.max_y,
                self.player.width * self.max_x,
                self.player.height * self.max_y,
            ),
        )
        # draw tubes
        for tube in self.tube_generator.tubes:
            pg.draw.rect(
                self.window,
                (0, 255, 0),
                pg.rect.Rect(
                    tube.x * self.max_x,
                    0,
                    tube.width * self.max_x,
                    tube.gap_position * self.max_y,
                ),
            )
            pg.draw.rect(
                self.window,
                (0, 255, 0),
                pg.rect.Rect(
                    tube.x * self.max_x,
                    (tube.gap_position + tube.gap_height) * self.max_y,
                    tube.width * self.max_x,
                    (1 - tube.gap_position - tube.gap_height) * self.max_y,
                ),
            )
        # draw frame counter
        self.draw_frame_counter()
        # draw end screen
        self.draw_end_screen()
        # update
        pg.display.flip()
        pass

    def draw_end_screen(self):
        if self.game_state.INITIAL.is_active:
            fail_text = pg.font.Font(self.font_path, 50).render(
                "PRESS SPACE TO START",
                True,
                (0, 0, 0),
                (200, 200, 200),
            )
            textRect = fail_text.get_rect()
            textRect.center = (self.max_x // 2, self.max_y // 2)
            self.window.blit(fail_text, textRect)
        if self.game_state.FAILURE.is_active:
            fail_text = pg.font.Font(self.font_path, 50).render(
                "GAME OVER",
                True,
                (0, 0, 0),
                (200, 200, 200),
            )
            textRect = fail_text.get_rect()
            textRect.center = (self.max_x // 2, self.max_y // 2)
            self.window.blit(fail_text, textRect)

    def draw_frame_counter(self):
        """Draw the counter for the frame and framerate"""
        text = self.font.render(
            f"FPS: {self.clock.get_fps():.0f} | Frame: {self.frame_number:04d} | Game Tick: {self.game_state.tick:04d} | Game State: {self.game_state.current_state.id} | Agent: {self.settings.agent.__class__()}",
            True,
            (0, 0, 0),
        )
        textRect = text.get_rect()
        textRect.topleft = (0, 0)
        self.window.blit(text, textRect)

    def quit(self):
        """Quit the GUI"""
        pg.quit()
