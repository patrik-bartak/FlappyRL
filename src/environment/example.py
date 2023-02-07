import pygame as pg

pg.init()
clock = pg.time.Clock()
running = True
window = pg.display.set_mode((640, 480))
window.fill((255, 255, 255))
btn = pg.Rect(0, 0, 100, 30)
rect1 = pg.Rect(0, 30, 100, 100)

framerate = 60
frame_number = 0

font = pg.font.Font("freesansbold.ttf", 12)

move_it = False
move_direction = 1

while running:
    clock.tick(framerate)
    frame_number += 1
    window.fill((255, 255, 255))

    for e in pg.event.get():
        if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
            move_it = not move_it
            # (mouseX, mouseY) = pg.mouse.get_pos()
            # if btn.collidepoint((mouseX, mouseY)):
        if e.type == pg.QUIT:
            running = False
    # end event handling

    if move_it:
        rect1.move_ip(move_direction * 5, 0)
        if not window.get_rect().contains(rect1):
            move_direction = move_direction * -1
            rect1.move_ip(move_direction * 5, 0)

    pg.draw.rect(window, (255, 0, 255), rect1, 1)
    pg.draw.rect(window, (255, 0, 0) if move_it else (0, 255, 255), btn)
    text = font.render(
        f"FPS: {clock.get_fps():.0f} | Frame: {frame_number}", True, (0, 0, 0)
    )
    textRect = text.get_rect()
    textRect.topleft = (0, 0)
    window.blit(text, textRect)
    # update
    pg.display.flip()

# end main loop
pg.quit()
