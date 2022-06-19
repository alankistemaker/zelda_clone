import pygame as pg
pg.init()
font = pg.font.Fone(None,30)

def debug(info, y=10, x=10):
    displaySurface = pg.display.get_surface()
    debugSurf = font.render(str(info),True, 'White')
    debugRect = debugSurf.get_rect(topleft = (x,y))
    pg.draw.rect(displaySurface, 'Black', debugRect)
    displaySurface.blit(debugSurf, debugRect)
