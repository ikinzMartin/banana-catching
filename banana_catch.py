import pygame as pg
import random as rand
from sprites.basket import Basket
from sprites.banana import Banana
import config as cfg

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640


BANANA_SIZE = (64, 32)
BANANA_INIT_FALL_SPEED = 5


def main():
     

    ### INITIALIZATION
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Bananarama")
    # make mouse invisible inside window
    pg.mouse.set_visible(False)
     
    # Set background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(pg.Color("chartreuse4"))

    # initial display to screen
    screen.blit(background, (0, 0))
    pg.display.update()

    # Basket
    basket = Basket()

    # Sprite groups
    basket_group = pg.sprite.Group(basket)
    bananas = pg.sprite.Group()

    # define a variable to control the main loop
    running = True

    clock = pg.time.Clock()

    NEW_BANANA_EVENT = pg.USEREVENT + 1
    pg.time.set_timer(NEW_BANANA_EVENT, 2000)

    SHOW_PLAYER_SCORE_EVENT = pg.USEREVENT + 2
    pg.time.set_timer(SHOW_PLAYER_SCORE_EVENT, 1000)

    score = 0

    # main loop
    while running:
        clock.tick(60) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == NEW_BANANA_EVENT: 
                start_position = rand.randint(0, int((9/10)*SCREEN_WIDTH))
                banana = Banana(start_position, cfg.BANANA_SPEED)
                bananas.add(banana)
            elif event.type == SHOW_PLAYER_SCORE_EVENT:
                print(f"Player score is: {score}")

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
