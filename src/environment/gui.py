import pygame as pg


class Gui:
    def __init__(self, settings, player, tube_generator) -> None:
        self.player = player
        self.tube_generator = tube_generator
        pg.init()
        self.clock = pg.time.Clock()
        self.window = pg.display.set_mode((settings.max_x, settings.max_y))
        self.max_x = settings.max_x
        self.max_y = settings.max_y
        self.window.fill((255, 255, 255))
        self.framerate = 60
        self.frame_number = 0
        self.font = pg.font.Font("freesansbold.ttf", 12)
        pass

    def draw(self):
        self.clock.tick(self.framerate)
        self.frame_number += 1
        # reset window fill
        self.window.fill((255, 255, 255))
        # draw player
        pg.draw.rect(self.window, (255, 0, 255), self.player.get_visual(), 1)
        # draw tubes
        for tube in self.tube_generator.tubes:
            pg.draw.rect(self.window, (0, 255, 0), pg.rect.Rect(tube.x, 0, tube.width * self.max_x,
                                                                tube.gap_position * self.max_y), 1)
            pg.draw.rect(self.window, (0, 255, 0), pg.rect.Rect(tube.x,
                                                                (tube.gap_position + tube.gap_height) * self.max_y,
                                                                tube.width * self.max_x,
                                                                (1 - tube.gap_position - tube.gap_height) * self.max_y),
                         1)
        # draw frame counter
        self.draw_frame_counter()
        # update
        pg.display.flip()
        pass

    def draw_frame_counter(self):
        text = self.font.render(
            f"FPS: {self.clock.get_fps():.0f} | Frame: {self.frame_number}",
            True,
            (0, 0, 0),
        )
        textRect = text.get_rect()
        textRect.topleft = (0, 0)
        self.window.blit(text, textRect)

    def quit(self):
        pg.quit()
