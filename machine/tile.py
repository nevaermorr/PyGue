from utilities.generalFunctions import *
import pygame
from engine.tile import *
from machine.symbolicPanel import *


class MetaTile(Tile, SymbolicPanel):
    """
    complement of tile
    """
    # height in pixels
    height = 25
    # width in pixels
    width = 25

    def __init__(self, coordinates_):
        """
        creation of the tile
        """
        # inherited constructors
        Tile.__init__(self, coordinates_)
        SymbolicPanel.__init__(self, MetaTile.width, MetaTile.height)
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 50)

        # create the reel
        self.reel = pygame.Surface((MetaTile.width, MetaTile.height))

    def get_font_color(self):
        """
        obtain proper color for the font
        """
        # if there is a construction on the tile it determines the color of the font
        if self.construction:
            return self.construction.get_font_color()
        else:
            return self.font_color

    def get_ascii(self):
        """
        obtain symbol of this element
        """
        # if there is a construction on the tile it determines the symbol of the tile
        if self.construction:
            return self.construction.get_ascii()
        # default value
        return '#'