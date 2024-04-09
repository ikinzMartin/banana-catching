import pygame as pg

def load_image(path, scale=1):
    image = pg.image.load(path)
    width, length = image.get_size()
    image = pg.transform.scale(image, (width*scale, length*scale))
    image = image.convert()
    image.set_colorkey(image.get_at((0,0)))
    return image 
