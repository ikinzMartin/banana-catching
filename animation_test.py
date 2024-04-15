from banana_catch import setup_screen
import pygame as pg
import utils as u
import config as cfg

if __name__ == '__main__':

    pg.init()
    screen, background = setup_screen()
    
    character = u.load_image("images/idle0.png", scale=5)
    char_rect = character.get_rect(midbottom=(cfg.SCREEN_WIDTH//2, cfg.SCREEN_HEIGHT))

    walking_anim_right = [u.load_image(f"images/walking/pixil-frame-{i}.png", scale=5) for i in range(3)]
    walking_anim_left = [pg.transform.flip(image, True, False) for image in walking_anim_right]

    # Trajectory:  (-1/11)*(x-15)**2 + 20
    # Derivative: (-2/11)*(-15+x)
    jump_curve = lambda x: (-20/11)*(-15+x)
    jump_curve_adds = [jump_curve(x) for x in range(31)]
    jump_step = 0

    walking_frame = 0
    iters = 0

    running = True
    walking = False
    jumping = False

    direction = -1

    clock = pg.Clock()

    while running:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                walking = True
                direction = 1
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                walking = True
                direction = -1 
            elif event.type == pg.KEYUP and event.key in [pg.K_RIGHT, pg.K_LEFT]:
                walking = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                jumping = True
        
        background.fill(pg.Color('white'))
        screen.blit(background,(0,0))

        if jumping:
            char_rect.move_ip(0, -jump_curve_adds[jump_step])
            jump_step += 1
            if jump_step == len(jump_curve_adds):
                jumping = False
                jump_step = 0
        if walking:
            iters += 1
            if iters > 10:
                walking_frame = (walking_frame + 1)%3
                iters = 0
            char_rect.move_ip(direction*10, 0)
            walk_anim_used = walking_anim_left if direction == -1 else walking_anim_right
            screen.blit(walk_anim_used[walking_frame], char_rect)
        else:
            screen.blit(character, char_rect)

        pg.display.update()
    

