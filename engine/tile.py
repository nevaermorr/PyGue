from utilities.generalFunctions import *
from machine.inventory import *


class Tile(MetaInventoryInterface):
    """
    quantum of space
    """
    
    def __init__(self, coordinates_, is_passable = True):
        # add inventory
        MetaInventoryInterface.__init__(self)
        # coordinates of this tile in context of location
        self.coordinates_ = coordinates_
        # is it possible to step on this tile?
        self.is_passable = is_passable
        # type of terrain
        self.terrain = ''
        # optional pointer to corresponding location, to where this tile leads
        self.passage = None

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