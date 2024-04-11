
import pygame as pg
import utils as u
import config as cfg

class Button(pg.sprite.Sprite):

    def __init__(self, text, x, y, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.text = text 

    def update(self):
        """
        """
        if self.is_hover():
            self.image.fill(pg.Color("darkred"))
        else:
            self.image.fill(pg.Color("red"))
        text_rect = u.display_text(self.image, self.text, 0, 0)    

    def is_hover(self):
        return self.rect.collidepoint(pg.mouse.get_pos())
