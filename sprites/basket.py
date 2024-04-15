import pygame as pg
import utils as u
import config as cfg

class Basket(pg.sprite.Sprite):

    def __init__(self, speed):
        pg.sprite.Sprite.__init__(self)
        # Idle
        self.idle = u.load_image("images/idle0.png",scale=1)
        self.walk = [u.load_image(f"images/walking/pixil-frame-{i}.png",scale=1) for i in range(0,3)]
        self.is_moving = False
        self.speed = speed
        basket = u.load_image(cfg.BASKET_IMAGE_PATH, scale=cfg.BASKET_SCALE)
        self.image = basket
        self.rect = basket.get_rect()
        self.rect.midbottom = (cfg.SCREEN_WIDTH//2, cfg.BASKET_POSITION_HEIGHT)

    def update(self):
        """
        Nothing
        """
        if self.is_moving:
            self.rect.move_ip(self.DIRECTION * self.speed, 0)

    def move_right(self):
        """
        """
        self.is_moving = True
        self.DIRECTION = 1

    def move_left(self):
        """
        """
        self.is_moving = True
        self.DIRECTION = -1

    def stop(self):
        self.is_moving = False

    def can_collect(self, banana):
        """
        Returns true if the basket can collect a given banana
        """
        hitbox = self.rect.move(0,self.rect.height//2)
        return hitbox.colliderect(banana.rect)
