from utilities.generalFunctions import *
from machine.construction import *


class Door(MetaConstruction):
    """
    a section of wall on the map
    """

    def __init__(self, closed=True):
        # inherited constructor
        MetaConstruction.__init__(self)
        # is it open?
        self.closed = closed
        # is it locked
        self.locked = False

    def is_passable(self):
        # doors are passable if open
        return not self.closed