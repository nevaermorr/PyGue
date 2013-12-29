from utilities.generalFunctions import *
from machine.construction import *


class Door(MetaConstruction):
    """
    a section of wall on the map
    """

    def __init__(self, closed=True):
        # inherited constructor
        MetaConstruction.__init__(self)
        # is it closed?
        self.closed = closed
        # is it locked?
        self.locked = False

    def is_passable(self):
        """
        is it possible to pass through this construction?
        """
        # doors are passable if open
        return not self.closed