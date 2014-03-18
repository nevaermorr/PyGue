from utilities.general_functions import *
import pygame
from engine.location import *


class MetaLocation(Location):
    """
    complement of location
    """

    def __init__(self, tiles_):
        """
        creation of the location
        """
        # inherited constructor
        Location.__init__(self, tiles_)
        # specific background for location
        self.background_color = pygame.Color(20, 20, 20)
        # create empty surface
        self.reel = pygame.Surface((800, 500))

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # inherited routine
        Location.compose_reel(self)

        self.update_tiles_visibility()

        # display the floor
        from machine.symbolic_panel import SymbolicPanel
        for tile_row in self.tiles_:
            # display single tile
            for tile in tile_row:
                self.reel.blit(tile.get_reel(),
                               (tile.get_x() * SymbolicPanel.pixels_per_unit_width,
                                tile.get_y() * SymbolicPanel.pixels_per_unit_height))
        # display all entities
        for being in self.beings_:
            self.reel.blit(being.get_reel(), (being.get_x() * SymbolicPanel.pixels_per_unit_width,
                                              being.get_y() * SymbolicPanel.pixels_per_unit_height))

    def update_tiles_visibility(self):
        """
        update information about which tiles are visible for hero
        """
        for tile_row in self.tiles_:
            # for single tile
            for tile in tile_row:
                tile.calculate_visibility(self.hero)
