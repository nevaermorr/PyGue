from utilities.general_functions import *
import pygame
from engine.tile import *
from machine.symbolic_panel import *


class MetaTile(Tile, SymbolicPanel):
    """
    complement of tile
    """

    def __init__(self, x, y):
        """
        creation of the tile
        """
        # inherited constructors
        Tile.__init__(self, x, y)
        SymbolicPanel.__init__(
            self,
            symbol='#',
        )
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 50)

        # colors used for shadowing tiles outside the field of view
        self.darkness_color = pygame.Color(0, 0, 0)
        self.shadow_color = pygame.Color(80, 80, 80)
        self.half_shadow_color = pygame.Color(130, 130, 130)

        # create the reel
        self.reel = pygame.Surface(
            (SymbolicPanel.pixels_per_unit_width, SymbolicPanel.pixels_per_unit_height)
        )

    def get_font_color(self):
        """
        obtain proper color for the font
        """
        # if there is a construction on the tile it determines the color of the font
        if self.construction:
            return self.construction.get_font_color()
        else:
            return self.font_color

    def get_symbol(self):
        """
        obtain symbol of this element
        """
        # if there is a construction on the tile it determines the symbol of the tile
        if self.construction:
            return self.construction.get_symbol()
        # default value
        return self.symbol

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """

        # if the tile has never been seen - don't bother with displaying
        if self.get_visibility() == -1:
            self.reel.fill(self.darkness_color)
            return True

        # inherited routine - compose the basis of the reel
        SymbolicPanel.compose_reel(self)
        # display items if any present
        self.overlay_items()
        # lay proper shadow if necessary
        self.overlay_shadow()

        return True

    def overlay_shadow(self):
        """
        cover the reel with proper shadow if the tile is beyond hero's field of view
        """
        # out of sight - fully shadowed
        if self.get_visibility() == 0:
            self.reel.fill(self.shadow_color, None, pygame.BLEND_MULT)
            # nothing more will be displayed on a tile beyond field of view
            return True

        # in far view field - partially shadowed
        elif self.get_visibility() == 1:
            self.reel.fill(self.half_shadow_color, None, pygame.BLEND_MULT)

        return True

    def overlay_items(self):
        """
        add the present items to the reel
        """
        # if the tile is not visible or there is nothing to display, ignore this
        if (
            not self.get_visibility()
            or self.has_empty_inventory()
        ):
            return False

        # otherwise display the symbolic inventory
        self.reel.blit(self.inventory.get_reel(), [0, 0])

