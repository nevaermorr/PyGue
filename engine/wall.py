from utilities.generalFunctions import *
from machine.construction import *


class Wall(MetaConstruction):
    """
    a section of wall on the map
    """

    def __init__(self):
        """
        creation of the wall
        """
        # inherited constructor
        MetaConstruction.__init__(self)

    def is_passable(self):
        """
        check if it is possible to pass through this tile
        """
        # walls are not passable by default
        return False