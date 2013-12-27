from utilities.generalFunctions import *
from machine.construction import *


class Wall(MetaConstruction):
    """
    a section of wall on the map
    """

    def __init__(self):
        # inherited constructor
        MetaConstruction.__init__(self)

    def is_passable(self):
        # walls are not passable by default
        return False