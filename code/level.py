import pygame as pg
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        self.displaySurface = pg.display.get_surface()
        self.visibleSprites = pg.sprite.Group()
        self.obstacleSprites = pg.sprite.Group()

        self.createMap()

    def createMap(self):
        for rowIndex, row in enumerate(WORLD_MAP):
            for colIndex, col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visibleSprites, self.obstacleSprites])
                if col == "p":
                    Player((x, y), [self.visibleSprites])

    def run(self):
        self.visibleSprites.draw(self.displaySurface)
