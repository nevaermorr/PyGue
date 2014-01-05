from utilities.generalFunctions import *
from machine.inventory import *


class Tile(MetaInventoryInterface):
    """
    quantum of space
    """

    def __init__(self, coordinates_):
        """
        creation of tile
        :param coordinates_: coordinates of the tile relative to the location
        """
        # add inventory
        MetaInventoryInterface.__init__(self)
        # coordinates of this tile in context of location
        self.coordinates_ = coordinates_
        # type of terrain
        self.terrain = ''
        # optional pointer to corresponding location, to where this tile leads
        self.passage = None
        # constructional element on this tile
        self.construction = None

    def is_passable(self):
        """
        check if it is possible to pass through this tile
        """
        # if there is some constructional element it determines the passability of the tile
        if self.construction:
            return self.construction.is_passable()
        # otherwise it is determined by the tile's natural passability;
        # by default tile is passable
        return True

    def get_coordinates(self):
        """
        get coordinates of this tile
        """
        return self.coordinates_

    def get_x(self):
        """
        get coordinate from x-axis
        """
        return self.coordinates_[0]

    def get_y(self):
        """
        get coordinate from y-axis
        """
        return self.coordinates_[1]

    def get_construction(self):
        """
        obtain access to construction present on this tile (if any)
        """
        return self.construction