from utilities.generalFunctions import *
from machine.gear import *


class Construction(MetaGear):
    """
    constructional element present on the tile
    """

    def __init__(self):
        """
        creation of construction
        """
        # inherited constructor
        MetaGear.__init__(self)
        # is it possible to pass through the construction?
        self.passable = True

    def is_passable(self):
        """
        is it possible to pass through this construction?
        """
        return self.passable