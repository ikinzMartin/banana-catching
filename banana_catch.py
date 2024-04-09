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
    SHOW_PLAYER_SCORE = evgen.define_event(2000)

    # define a variable to control the main loop
    running = True

    clock = pg.time.Clock()


    score = 0

    # main loop
    while running:
        clock.tick(60) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == CREATE_BANANA_EVENT: 
                start_position = rand.randint(0, int((9/10)*cfg.SCREEN_WIDTH))
                banana = Banana(start_position, cfg.BANANA_SPEED)
                bananas.add(banana)
            elif event.type == SHOW_PLAYER_SCORE:
                print(f"Player score is: {score}")

        ### TEXT
        


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

        basket_group.update()
        basket_group.draw(screen)        

        bananas.update()
        bananas.draw(screen)        

        # final display
        pg.display.update()

     
if __name__=="__main__":
    main()
