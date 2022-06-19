import pygame as pg
from settings import *


class Tile(pg.sprite.Sprite):
    def __init__(self, aPos, aGroups):
        super().__init__(aGroups)
        self.image = pg.image.load("../graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=aPos)
