import pygame as pg
import random as rand

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640

BASKET_SIZE = (128,128)
BASKET_POSITION_HEIGHT = SCREEN_HEIGHT - BASKET_SIZE[0] - (1/32)*SCREEN_HEIGHT

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

    basket = pg.image.load("images/basket.png")
    basket = pg.transform.scale(basket, BASKET_SIZE)
    basket = basket.convert()
    basket.set_colorkey(basket.get_at((0,0)))

    banana = pg.image.load("images/banana.png")
    banana = pg.transform.scale(banana, BANANA_SIZE)
    banana = banana.convert()
    banana.set_colorkey(banana.get_at((0,0)))

    # define a variable to control the main loop
    running = True
    create_new_banana = True
    active_bananas = []

    clock = pg.time.Clock()
    NEW_BANANA_EVENT = pg.USEREVENT + 1
    pg.time.set_timer(NEW_BANANA_EVENT, 2000)
    score = 0

    # main loop
    while running:
        clock.tick(60) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == NEW_BANANA_EVENT: 
                start_position = rand.randint(0, SCREEN_WIDTH - BANANA_SIZE[0])        
                active_bananas.append((banana, (start_position, 0)))

        ### DISPLAY
        # background
        screen.blit(background, (0, 0))

        # basket
        mouse_pos = pg.mouse.get_pos()
        basket_pos = (mouse_pos[0] - BASKET_SIZE[0]//2, BASKET_POSITION_HEIGHT)
        screen.blit(basket, basket_pos)

        # draw all bananas
        for i, aban in enumerate(active_bananas):
            old_x, old_y = aban[1]
            new_pos = old_x, old_y + BANANA_INIT_FALL_SPEED
            active_bananas[i] = (banana, new_pos)

        screen.blits(active_bananas)

        # final display
        pg.display.update()
     
if __name__=="__main__":
    main()
