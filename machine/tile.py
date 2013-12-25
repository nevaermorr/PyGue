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
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 50)

        # create the reel
        self.reel = self.font.render(self.ascii, True, self.font_color)
