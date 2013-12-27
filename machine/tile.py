from utilities.generalFunctions import *
import pygame
from engine.tile import *
from machine.symbolicPanel import *


class MetaTile(Tile, SymbolicPanel):
    """
    appearance of tile
    """
    height = 25
    width = 25

    def __init__(self, coordinates_):
        # inherited constructor
        Tile.__init__(self, coordinates_)
        SymbolicPanel.__init__(self, MetaTile.width, MetaTile.height)
        #visual aspects
        self.ascii = '#'
        # the font color varies depending on whether it is a floor or a wall
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 50)

        # create the reel
        self.reel = pygame.Surface((MetaTile.width, MetaTile.height))

    def get_font_color(self):

        if self.construction:
            return self.construction.font_color
        else:
            return self.font_color