from utilities.generalFunctions import *
import pygame
from engine.location import *


class MetaLocation(Location):
    """
    appearance of location
    """

    def __init__(self, tiles_):
        # inherited constructor
        Location.__init__(self, tiles_)
        # specific background for location
        self.background_color = pygame.Color(20, 20, 20)
        # create empty surface
        self.reel = pygame.Surface((800, 500))

    def compose_reel(self):
        # inherited routine
        Location.compose_reel(self)

        # display the floor
        from machine.tile import MetaTile
        for tile_row in self.tiles_:
            for tile in tile_row:
                self.reel.blit(tile.get_reel(), (tile.get_x() * MetaTile.width,
                                                 tile.get_y() * MetaTile.height))
        # display all entities
        for being in self.beings_:
            self.reel.blit(being.get_reel(), (being.get_x() * MetaTile.width,
                                              being.get_y() * MetaTile.height))