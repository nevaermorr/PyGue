from utilities.generalFunctions import *
from machine.gear import *


class Construction(MetaGear):
    """
    constructional element present on the tile
    """

    def __init__(self, sort=''):
        """
        creation of construction
        """
        # inherited constructor
        MetaGear.__init__(self)
        # is it possible to pass through the construction?
        self.passable = True
        # what sort of construction is this?
        self.sort = sort
        # is it possible to see through this construction?
        self.transparent = True

    def is_passable(self):
        """
        is it possible to pass through this construction?
        """
        return self.passable

    def is_transparent(self):
        """
        is it possible to see through this construction?
        """
        # return default value
        return self.transparent

    def get_sort(self):
        """
        obtain the type of this construction
        """
        return self.sort