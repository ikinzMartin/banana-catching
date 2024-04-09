import pygame as pg
import utils as u
import config as cfg

class Banana(pg.sprite.Sprite):

    def __init__(self, start_x, speed):
        super().__init__()
        banana = u.load_image(cfg.BANANA_IMAGE_PATH, cfg.BANANA_SCALE)
        self.image = banana
        self.rect = banana.get_rect()
        self.rect.midtop = (start_x, 0)
        self.speed = speed

    def update(self):
        """
        Lowers the banana by the speed attribute
        """
        self.rect.move_ip(0,self.speed) 

    def dissapear(self):
        """
        Banana dissapears from screen
        """
        self.kill()

    def collect(self):
        """
        Banana has been collected
        """
        self.kill()

    def out_of_bounds(self):
        """
        Banana dissapears
        """
        return self.rect.midbottom[1] > cfg.SCREEN_HEIGHT
