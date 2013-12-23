from utilities.generalFunctions import *
import pygame
from engine.tile import *


class MetaTile(Tile):
    """
    appearance of tile
    """
    height = 25
    width = 25

    def __init__(self, coordinates_):
        # inherited constructor
        Tile.__init__(self, coordinates_)
        #visual aspects
        self.ascii = '#'
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)

        # create the reel
        self.reel = self.font.render(self.ascii, True, self.font_color)

    def compose_reel(self):
        Tile.compose_reel(self)
        self.reel.blit(self.font.render(self.ascii, True, self.font_color), (0,0))