import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, aPos, aGroups):
        super().__init__(aGroups)
        self.image = pg.rect.Rect()
