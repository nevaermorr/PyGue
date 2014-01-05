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
        MetaConstruction.__init__(self, 'wall')
        # walls are opaque by default
        self.transparent = False
        # walls are impassable by default
        self.passable = False