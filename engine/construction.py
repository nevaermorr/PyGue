from utilities.generalFunctions import *
from machine.gear import *


class Construction(MetaGear):
    """
    constructional element present on the tile
    """

    def __init__(self):
        # inherited constructor
        MetaGear.__init__(self)
        # is it possible to pass through the construction
        self.passable = True

    def is_passable(self):
        return self.passable