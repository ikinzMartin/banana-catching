import pygame as pg
import random as rand
from sprites.basket import Basket
from sprites.banana import Banana
import config as cfg
import utils as u

def setup_screen():
    # screen
    screen = pg.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
    pg.display.set_caption(cfg.SCREEN_CAPTION)
    # mouse
    pg.mouse.set_visible(False)
    # background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(pg.Color("chartreuse4"))
    return screen, background


def display_text(screen, text, x, y):
    font = pg.freetype.SysFont("Mono", cfg.FONT_SIZE)
    font.render_to(screen, (x,y), text, pg.Color(cfg.FONT_COLOR))


def main():
    ### INITIALIZATION
    pg.init()
    evgen = u.EventGenerator()
    screen, background = setup_screen()

    # Sprite groups
    basket = Basket()
    basket_group = pg.sprite.Group(basket)
    bananas = pg.sprite.Group()

    # define events
    CREATE_BANANA_EVENT = evgen.define_event(2000)

    # define a variable to control the main loop
    running = True
    paused = False

    clock = pg.time.Clock()
    score = 0

    # main loop
    while running:
        # Clock ticks
        clock.tick(60) 

        ### EVENTS
        if paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    paused = False

            # PAUSED DISPLAY
            background_pause = pg.Surface(screen.get_size(), pg.SRCALPHA)
            background_pause.fill((50,50,50,200))
            screen.blit(background_pause, (0,0))
            display_text(screen, "PAUSED", cfg.SCREEN_WIDTH//2, cfg.SCREEN_HEIGHT//2)
            pg.display.update()
            continue

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == CREATE_BANANA_EVENT: 
                start_position = rand.randint(0, int((9/10)*cfg.SCREEN_WIDTH))
                banana = Banana(start_position, cfg.BANANA_SPEED)
                bananas.add(banana)
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                print("event_detected")
                paused = True
                pg.mouse.set_visible(True)
                continue

        ### GAME LOGIC
        for banana in bananas:
            if basket.can_collect(banana):
                banana.collect()
                score += 1
            elif banana.out_of_bounds():
                banana.dissapear()
                score -= 1


        ### DISPLAY
        # background
        screen.blit(background, (0, 0))

        # Text
        display_text(screen, f"Your score: {score}", cfg.FONT_SIZE, cfg.FONT_SIZE) 

        basket_group.update()
        basket_group.draw(screen)        

        bananas.update()
        bananas.draw(screen)        

        # final display
        pg.display.update()

     
if __name__=="__main__":
    main()
