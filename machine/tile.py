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

    def __init__(self, x, y):
        """
        creation of the tile
        """
        # inherited constructors
        Tile.__init__(self, x, y)
        SymbolicPanel.__init__(self, MetaTile.width, MetaTile.height)
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 50)

        # colors used for shadowing tiles outside the field of view
        self.darkness_color = pygame.Color(0, 0, 0)
        self.shadow_color = pygame.Color(80, 80, 80)
        self.half_shadow_color = pygame.Color(130, 130, 130)

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

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # examine visibility of this tile
        visibility = self.get_visibility()

        # if the tile has never been seen - don't bother with displaying
        if visibility == -1:
            self.reel.fill(self.darkness_color)
            return True

        # inherited routine
        SymbolicPanel.compose_reel(self)

        # shadow out tiles that are not in hero's field of view
        # out of sight - fully shadowed
        if visibility == 0:
            self.reel.fill(self.shadow_color, None, pygame.BLEND_MULT)

        # in long view range - partially shadowed
        elif visibility == 1:
            self.reel.fill(self.half_shadow_color, None, pygame.BLEND_MULT)

        return True