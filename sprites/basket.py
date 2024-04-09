import pygame as pg
import utils as u
import config as cfg

class Basket(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        basket = u.load_image(cfg.BASKET_IMAGE_PATH, scale=cfg.BASKET_SCALE)
        self.image = basket
        self.rect = basket.get_rect()

    def update(self):
        """
        Updates basket X position according to mouse
        """
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.rect.midbottom = (mouse_x, cfg.BASKET_POSITION_HEIGHT)

    def can_collect(self, banana):
        """
        Returns true if the basket can collect a given banana
        """
        hitbox = self.rect.move(0,self.rect.height//2)
        return hitbox.colliderect(banana.rect)
