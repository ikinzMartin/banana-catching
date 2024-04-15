import pygame as pg
import config as cfg


def display_text(screen, text, x, y):
    font = pg.freetype.SysFont("Mono", cfg.FONT_SIZE)
    return font.render_to(screen, (x,y), text, pg.Color(cfg.FONT_COLOR))


def display_rect_text(text):
    font = pg.freetype.SysFont("Mono", cfg.FONT_SIZE)
    return font.render(text, pg.Color(cfg.FONT_COLOR))


def load_image(path, scale=1):
    image = pg.image.load(path)
    width, length = image.get_size()
    image = pg.transform.scale(image, (width*scale, length*scale))
    #image = image.convert()
    #image.set_colorkey(image.get_at((0,0)))
    return image 

class EventGenerator:
    def __init__(self):
        self.next = pg.USEREVENT 
    
    def define_event(self, period):
        self.next += 1
        pg.time.set_timer(self.next, period)
        return self.next

